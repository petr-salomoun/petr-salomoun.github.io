---
layout: default
title: My World Data View
description: "Data-driven investigations exploring real-world phenomena"
---

# Data Science Explorations

Making sense of the world through data.

---

## Latest Projects

{% for post in site.posts %}
<div style="margin: 2.5em 0; padding: 2em; background: linear-gradient(to right, #f8f9fa, #ffffff); border-left: 4px solid #159957; border-radius: 0 8px 8px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">

<h3 style="margin-top: 0; color: #1a1f36; border-bottom: 2px solid #159957; padding-bottom: 0.5em;"><a href="{{ post.url }}" style="color: #1a1f36; text-decoration: none;">{{ post.title }}</a></h3>

<p style="color: #586069; font-size: 0.95em; margin: 0.8em 0;">
  <strong>📅 {{ post.date | date: "%B %d, %Y" }}</strong>
  {% if post.categories %}
  <span style="margin-left: 1.5em;"><strong>📂 {{ post.categories | first }}</strong></span>
  {% endif %}
</p>

<p style="margin: 1.2em 0; font-size: 1.05em; line-height: 1.6;">{{ post.excerpt | strip_html | truncatewords: 45 }}</p>

<p style="margin-top: 1.5em;">
  <a href="{{ post.url }}" style="background: #159957; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; display: inline-block; font-weight: 600; box-shadow: 0 2px 4px rgba(0,0,0,0.2); transition: all 0.2s ease;">Read Full Analysis →</a>
  {% if post.github_repo %}
  <a href="https://github.com/{{ post.github_repo }}" target="_blank" style="margin-left: 1em; color: #155799; text-decoration: none; display: inline-block; padding: 10px 20px; border: 2px solid #155799; border-radius: 6px; font-weight: 600; transition: all 0.2s ease;">📊 View Data & Code</a>
  {% endif %}
</p>

</div>
{% endfor %}

---

## About This Blog

This blog presents **data-driven investigations** of real-world phenomena. Each project uses publicly available datasets and rigorous analytical methods to uncover patterns and insights.

**Methodology:**
- Statistical analysis and machine learning
- Public government and research datasets
- Full code transparency on GitHub
- Written for general audiences

**Topics cover diverse domains** - from infrastructure and geology to urban analytics and beyond. All analyses combine technical rigor with clear storytelling.

[Learn more about the methodology →](/about/)

---

<p style="text-align: center; color: #586069; font-size: 0.9em; margin-top: 3em;">
  <strong>Contact:</strong> <a href="mailto:petr.salomoun@gmail.com">petr.salomoun@gmail.com</a> | 
  <strong>GitHub:</strong> <a href="https://github.com/petr-salomoun">@petr-salomoun</a>
</p>

