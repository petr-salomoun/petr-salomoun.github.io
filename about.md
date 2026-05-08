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

This blog showcases **data-driven investigations** of real-world phenomena—from bridge safety to mineral exploration to urban crime patterns. Each project combines:

- **Rigorous methodology**: Statistical analysis, machine learning, geospatial modeling
- **Public data**: All analyses use freely available government and research datasets
- **Clear communication**: Written for intelligent non-specialists
- **Full transparency**: Code and data available on GitHub

Think of it as **investigative journalism meets peer-reviewed research**, but accessible to anyone curious about what data can reveal.

---

## Current Projects

### 🌉 America's Bridges at Risk
**Analyzing 623,000 US bridges to identify structural risks**

Using Federal Highway Administration inspection data and machine learning, this analysis ranks every US highway bridge by structural risk and estimates collapse probability. Key findings include identification of 22,000 high-risk bridges and a predictive model that flags structural vulnerability patterns before they appear in official condition ratings.

[Read the full analysis →](/2026/04/25/us-bridge-risk-analysis/)

---

### ⛏️ Can Stream Water Tell Us Where the Gold Is?
**Mapping mineral deposits with geochemistry and data science**

This project uses USGS stream sediment samples and known mineral deposit locations to train a machine learning model that identifies geochemical signatures of hidden ore bodies. Combines PCA, gradient boosting classifiers, and spatial analysis to predict deposit locations from downstream chemistry alone.

[Read the full analysis →](/2026/04/12/usgs-geochemical-analysis/)

---

### 🌦️ Weather and Crime: Five Archetypes
**How climate shapes urban violence across five US cities**

Analyzing 16 million police incident records across Chicago, Houston, LA, New York, and Philadelphia to identify five distinct crime archetypes—each driven by different weather and calendar factors. Finds that heat is a confounder masking the true causal mechanisms, which emerge only after temperature is statistically removed.

[Read the full analysis →](/2026/04/26/weather-crime/)

---

## Methodology

All projects follow a consistent analytical framework:

1. **Data Collection**: Public datasets from government agencies (FHWA, USGS, city police departments)
2. **Exploratory Analysis**: Statistical profiling, correlation analysis, visualization
3. **Modeling**: Machine learning (random forests, gradient boosting), PCA, regression
4. **Validation**: Cross-validation, external datasets, historical comparison
5. **Communication**: Visualizations, narrative explanation, interactive maps where applicable

Code is primarily **Python** (pandas, scikit-learn, geopandas, matplotlib, seaborn). All analyses are fully reproducible.

---

## Technology Stack

- **Data Analysis**: Python, pandas, numpy, scikit-learn
- **Visualization**: matplotlib, seaborn, Plotly, Folium (interactive maps)
- **Geospatial**: geopandas, shapely, GeoPy
- **Publishing**: This blog is built with Jekyll and GitHub Pages, automatically synced from project README files

---

## Data Sources

Projects use public-domain data from:

- **US Federal Government**: FHWA National Bridge Inventory, USGS National Geochemical Survey, USGS Mineral Resources Data System, NOAA weather data
- **City Governments**: Open data portals from Chicago, Houston, Los Angeles, New York, Philadelphia
- **Research Institutions**: Published geochemical pathfinder element suites, crime taxonomy literature

All data citations are included in each project's full report.

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
2. Downloads and processes images
3. Generates Jekyll-compatible Markdown with frontmatter
4. Commits and pushes to the blog repository

For details, see the [blog automation documentation](https://github.com/petr-salomoun/petr-salomoun.github.io).

