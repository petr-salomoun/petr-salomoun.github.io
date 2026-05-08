#!/usr/bin/env python3
"""
Blog synchronization script for GitHub Pages + Jekyll.

Fetches README files from GitHub repositories and publishes them as blog posts.
Handles image downloads, Markdown conversion, and git operations.

Usage:
    python sync_blog.py --all                          # Sync all configured projects
    python sync_blog.py --repo user/repo               # Sync specific repository
    python sync_blog.py --all --dry-run                # Preview without committing
    python sync_blog.py --repo user/repo --force       # Force update even if unchanged
"""

import argparse
import os
import re
import sys
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse

import requests
import frontmatter
from github import Github
from git import Repo
from PIL import Image
from io import BytesIO

class BlogSyncer:
    """Synchronizes project READMEs to Jekyll blog."""
    
    def __init__(self, config_path: str = "blog_config.yaml", token: Optional[str] = None):
        """
        Initialize the blog syncer.
        
        Args:
            config_path: Path to configuration file
            token: GitHub personal access token (or reads from GITHUB_TOKEN env var)
        """
        self.config = self._load_config(config_path)
        self.token = token or os.getenv("GITHUB_TOKEN")
        
        if not self.token:
            raise ValueError(
                "GitHub token required. Set GITHUB_TOKEN environment variable "
                "or pass --token argument."
            )
        
        self.gh = Github(self.token)
        self.blog_path = Path.cwd()
        self.posts_dir = self.blog_path / "_posts"
        self.images_dir = self.blog_path / "assets" / "images"
        
        # Ensure directories exist
        self.posts_dir.mkdir(exist_ok=True)
        self.images_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize git repo
        self.repo = Repo(self.blog_path)
    
    def _load_config(self, path: str) -> Dict:
        """Load configuration from YAML file."""
        config_file = Path(path)
        if not config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {path}")
        
        with open(config_file) as f:
            return yaml.safe_load(f)
    
    def sync_project(self, project_config: Dict, force: bool = False, dry_run: bool = False) -> bool:
        """
        Sync a single project repository to blog.
        
        Args:
            project_config: Project configuration dict from blog_config.yaml
            force: Force update even if README hasn't changed
            dry_run: Preview changes without committing
        
        Returns:
            True if post was created/updated, False otherwise
        """
        repo_name = project_config["repo"]
        print(f"\n{'[DRY RUN] ' if dry_run else ''}Syncing {repo_name}...")
        
        try:
            # Get repository
            gh_repo = self.gh.get_repo(repo_name)
            
            # Get README
            readme = gh_repo.get_readme()
            readme_content = readme.decoded_content.decode("utf-8")
            
            # Get last commit date for the README
            commits = gh_repo.get_commits(path=readme.path)
            last_modified = commits[0].commit.author.date
            
            # Generate post filename
            date_str = last_modified.strftime("%Y-%m-%d")
            slug = repo_name.split("/")[-1]  # Use repo name as slug
            post_filename = f"{date_str}-{slug}.md"
            post_path = self.posts_dir / post_filename
            
            # Check if post already exists and hasn't changed
            if post_path.exists() and not force:
                existing_post = frontmatter.load(post_path)
                if existing_post.get("updated_at") == last_modified.isoformat():
                    print(f"  ✓ Post up to date (last modified: {last_modified})")
                    return False
            
            # Process README content
            processed_content = self._process_content(
                readme_content,
                gh_repo,
                slug,
                dry_run=dry_run
            )
            
            # Create frontmatter
            post_frontmatter = {
                "layout": "post",
                "title": project_config.get("title", gh_repo.name),
                "date": last_modified,
                "updated_at": last_modified.isoformat(),
                "categories": [project_config.get("category", "data-science")],
                "tags": project_config.get("tags", []),
                "author": self.config.get("author_name", ""),
                "excerpt": self._extract_excerpt(readme_content),
                "github_repo": repo_name,
            }
            
            # Create post object
            post = frontmatter.Post(processed_content, **post_frontmatter)
            
            if not dry_run:
                # Write post file
                with open(post_path, "w") as f:
                    f.write(frontmatter.dumps(post))
                
                print(f"  ✓ Post written: {post_filename}")
            else:
                print(f"  → Would write: {post_filename}")
            
            return True
            
        except Exception as e:
            print(f"  ✗ Error syncing {repo_name}: {e}")
            return False
    
    def _extract_excerpt(self, content: str, max_length: int = 200) -> str:
        """Extract excerpt from README for blog index."""
        # Remove title
        lines = content.split("\n")
        content_lines = [l for l in lines if not l.startswith("#")]
        text = " ".join(content_lines[:5])
        
        # Clean up
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)  # Remove links
        text = re.sub(r'[*_`]', '', text)  # Remove formatting
        text = re.sub(r'\s+', ' ', text).strip()
        
        if len(text) > max_length:
            text = text[:max_length].rsplit(' ', 1)[0] + "..."
        
        return text
    
    def _process_content(self, content: str, gh_repo, slug: str, dry_run: bool = False) -> str:
        """
        Process README content for Jekyll blog.
        
        - Downloads images
        - Converts image URLs to local paths
        - Adjusts heading levels
        """
        # Create project-specific image directory
        project_images_dir = self.images_dir / slug
        if not dry_run:
            project_images_dir.mkdir(exist_ok=True)
        
        # Find all image references
        img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        images = re.findall(img_pattern, content)
        
        for alt_text, img_url in images:
            # Skip if already a local path
            if not img_url.startswith(('http://', 'https://')):
                continue
            
            # Download and save image
            local_path = self._download_image(
                img_url,
                gh_repo,
                project_images_dir,
                dry_run=dry_run
            )
            
            if local_path:
                # Convert to relative path from blog root
                rel_path = local_path.relative_to(self.blog_path)
                # Replace in content
                content = content.replace(
                    f']({img_url})',
                    f'](/{rel_path})'
                )
        
        return content
    
    def _download_image(
        self,
        url: str,
        gh_repo,
        target_dir: Path,
        dry_run: bool = False
    ) -> Optional[Path]:
        """
        Download image from URL and save to target directory.
        
        Args:
            url: Image URL
            gh_repo: GitHub repository object
            target_dir: Directory to save image
            dry_run: Preview without actually downloading
        
        Returns:
            Path to saved image, or None if download failed
        """
        try:
            # Parse URL to get filename
            parsed = urlparse(url)
            filename = Path(parsed.path).name
            
            # Handle GitHub raw URLs specially
            if 'raw.githubusercontent.com' in url or 'github.com' in url:
                # Extract path from GitHub URL
                parts = parsed.path.split('/')
                if 'blob' in parts or 'raw' in parts:
                    # Remove 'blob' or 'raw' and branch name
                    idx = parts.index('blob') if 'blob' in parts else parts.index('raw')
                    repo_path = '/'.join(parts[idx+2:])
                    filename = Path(repo_path).name
            
            target_path = target_dir / filename
            
            if dry_run:
                print(f"    → Would download: {filename}")
                return target_path
            
            # Download image
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Process image (resize if needed)
            img = Image.open(BytesIO(response.content))
            
            # Resize if larger than max width
            max_width = self.config.get("image_max_width", 1200)
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Save
            quality = self.config.get("image_quality", 85)
            img.save(target_path, quality=quality, optimize=True)
            
            print(f"    ✓ Downloaded: {filename}")
            return target_path
            
        except Exception as e:
            print(f"    ✗ Failed to download image {url}: {e}")
            return None
    
    def commit_and_push(self, message: str, dry_run: bool = False):
        """
        Commit changes and push to remote.
        
        Args:
            message: Commit message
            dry_run: Preview without actually committing
        """
        if dry_run:
            print(f"\n[DRY RUN] Would commit with message: {message}")
            return
        
        # Stage all changes
        self.repo.index.add(['_posts/*', 'assets/images/*'])
        
        # Commit
        if self.repo.is_dirty():
            author_name = self.config.get("author_name", "Blog Sync Bot")
            author_email = self.config.get("author_email", "bot@example.com")
            
            self.repo.index.commit(
                message,
                author_name=author_name,
                author_email=author_email
            )
            
            # Push
            origin = self.repo.remote(name='origin')
            origin.push()
            
            print(f"\n✓ Changes committed and pushed: {message}")
        else:
            print("\n✓ No changes to commit")
    
    def sync_all_projects(self, force: bool = False, dry_run: bool = False):
        """
        Sync all projects configured in blog_config.yaml.
        
        Args:
            force: Force update even if READMEs haven't changed
            dry_run: Preview without committing
        """
        projects = self.config.get("projects", [])
        
        if not projects:
            print("No projects configured in blog_config.yaml")
            return
        
        print(f"Syncing {len(projects)} project(s)...")
        
        updated_count = 0
        for project in projects:
            if self.sync_project(project, force=force, dry_run=dry_run):
                updated_count += 1
        
        if updated_count > 0:
            commit_msg = f"Sync blog posts: {updated_count} project(s) updated"
            self.commit_and_push(commit_msg, dry_run=dry_run)
        else:
            print("\n✓ All posts up to date")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Sync GitHub project READMEs to Jekyll blog"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Sync all projects from config"
    )
    parser.add_argument(
        "--repo",
        type=str,
        help="Sync specific repository (format: owner/repo)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force update even if README hasn't changed"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without committing"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="blog_config.yaml",
        help="Path to configuration file"
    )
    parser.add_argument(
        "--token",
        type=str,
        help="GitHub personal access token (or use GITHUB_TOKEN env var)"
    )
    
    args = parser.parse_args()
    
    if not args.all and not args.repo:
        parser.error("Must specify either --all or --repo")
    
    try:
        syncer = BlogSyncer(config_path=args.config, token=args.token)
        
        if args.all:
            syncer.sync_all_projects(force=args.force, dry_run=args.dry_run)
        elif args.repo:
            # Find project config for this repo
            project = next(
                (p for p in syncer.config["projects"] if p["repo"] == args.repo),
                None
            )
            
            if not project:
                # Create minimal config if not in config file
                project = {
                    "repo": args.repo,
                    "title": args.repo.split("/")[-1],
                    "category": "data-science",
                    "tags": []
                }
            
            if syncer.sync_project(project, force=args.force, dry_run=args.dry_run):
                commit_msg = f"Update blog post: {args.repo}"
                syncer.commit_and_push(commit_msg, dry_run=args.dry_run)
            else:
                print("\n✓ Post up to date")
        
    except Exception as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
