---
layout: default
title: About
description: "About this data science blog and its methodology"
permalink: /about/
---

# About This Blog

[Home](/) | **About** | [GitHub](https://github.com/petr-salomoun)

---

## The Concept

This blog showcases **data-driven investigations** of real-world phenomena—from infrastructure safety to environmental health to urban analytics. Each project combines:

- **Rigorous methodology**: Statistical analysis, machine learning, geospatial modeling
- **Public data**: All analyses use freely available government and research datasets
- **Clear communication**: Written for intelligent non-specialists
- **Full transparency**: Code and data available on GitHub

Think of it as **investigative journalism meets peer-reviewed research**, but accessible to anyone curious about what data can reveal.

---

## Methodology

All projects follow a consistent analytical framework:

1. **Data Collection**: Public datasets from government agencies (FHWA, USGS, EPA, NOAA, city open data portals)
2. **Exploratory Analysis**: Statistical profiling, correlation analysis, visualization
3. **Modeling**: Machine learning (random forests, gradient boosting), PCA, regression, causal inference
4. **Validation**: Cross-validation, external datasets, historical comparison, robustness checks
5. **Communication**: Visualizations, narrative explanation, interactive maps where applicable

Code is primarily **Python** (pandas, scikit-learn, geopandas, matplotlib, seaborn). All analyses are fully reproducible from GitHub repositories.

---

## Technology Stack

- **Data Analysis**: Python, pandas, numpy, scikit-learn, statsmodels
- **Visualization**: matplotlib, seaborn, Plotly, Folium (interactive maps)
- **Geospatial**: geopandas, shapely, GeoPy
- **Publishing**: Jekyll, GitHub Pages, automated sync from project README files

---

## Data Sources

Projects use public-domain data from:

- **US Federal Government**: FHWA National Bridge Inventory, USGS National Geochemical Survey, USGS Mineral Resources Data System, EPA Toxics Release Inventory, NOAA weather stations
- **City Governments**: Open data portals from major US cities (crime records, demographic data)
- **Research Institutions**: Published geochemical references, epidemiological studies, validated crime taxonomies

All data citations are included in each project's full report.

---

## Topics & Scope

Projects span diverse domains—**infrastructure, geology, criminology, environmental health, urban analytics**—unified by a common approach: using data to answer questions that matter. Future analyses will continue exploring different fields where public data can reveal insights about the physical and social world.

No single domain is privileged. The only criterion is whether rigorous data analysis can produce meaningful findings.

---

## Contact

**Petr Salomoun**  
Email: [petr.salomoun@gmail.com](mailto:petr.salomoun@gmail.com)  
GitHub: [@petr-salomoun](https://github.com/petr-salomoun)

Feedback, suggestions, and collaboration inquiries welcome.

---

## License

**Blog content**: CC BY 4.0 (Creative Commons Attribution)  
**Code**: MIT License  
**Data**: Respective source licenses (all public-domain or open)

When using content from this blog, please attribute:

> Petr Salomoun, *[Project Title]* (2026). https://petr-salomoun.github.io

---

## Technical Note

This blog is **automatically updated** from the README files of GitHub project repositories. When a project's analysis is updated, the blog post is regenerated and republished within 24 hours. This ensures the blog always reflects the latest findings without manual maintenance.

The synchronization is handled by a Python script ([`sync_blog.py`](https://github.com/petr-salomoun/petr-salomoun.github.io/blob/main/scripts/sync_blog.py)) that:
1. Fetches README content from project repositories
2. Converts image paths to GitHub raw URLs
3. Generates Jekyll-compatible Markdown with frontmatter
4. Commits and pushes to the blog repository

For details, see the [blog repository](https://github.com/petr-salomoun/petr-salomoun.github.io).


