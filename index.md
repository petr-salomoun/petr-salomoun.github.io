---
layout: default
title: Home
description: "Data science explorations: uncovering patterns in infrastructure, geology, and society"
---

# Data Science Explorations

Uncovering patterns in infrastructure, geology, and society through data.

---

## Latest Projects

{% for post in site.posts %}
<div style="margin: 2.5em 0; padding: 1.5em; background: linear-gradient(to right, #f8f9fa, #ffffff); border-left: 4px solid #159957; border-radius: 0 8px 8px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">

### [{{ post.title }}]({{ post.url }})

<p style="color: #586069; font-size: 0.9em; margin: 0.5em 0;">
  📅 {{ post.date | date: "%B %d, %Y" }} 
  {% if post.categories %}
  <span style="margin-left: 1em;">📂 {{ post.categories | first }}</span>
  {% endif %}
</p>

<p style="margin: 1em 0;">{{ post.excerpt | strip_html | truncatewords: 40 }}</p>

<p style="margin-top: 1em;">
  <a href="{{ post.url }}" style="background: linear-gradient(135deg, #159957, #155799); color: white; padding: 8px 16px; border-radius: 6px; text-decoration: none; display: inline-block; font-weight: 600; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">Read Full Analysis →</a>
  {% if post.github_repo %}
  <a href="https://github.com/{{ post.github_repo }}" target="_blank" style="margin-left: 1em; color: #155799; text-decoration: none; display: inline-block; padding: 8px 16px; border: 1px solid #155799; border-radius: 6px;">📊 View Data & Code</a>
  {% endif %}
</p>

</div>
{% endfor %}

---

## About This Blog

This blog presents **in-depth data science analyses** of real-world datasets, written for a general audience. Each project combines rigorous methodology with clear storytelling.

**Current Focus Areas:**
- 🌉 **Infrastructure Safety** - Bridge risk analysis, structural engineering
- ⛏️ **Geochemical Exploration** - Mineral mapping, stream sediment analysis  
- 🌦️ **Urban Analytics** - Crime patterns, weather correlations

All projects use **publicly available data** and **open-source tools**. Code and datasets available on [GitHub](https://github.com/petr-salomoun).

[Learn more →](/about/)

---

<p style="text-align: center; color: #586069; font-size: 0.9em;">
  <strong>Contact:</strong> <a href="mailto:petr.salomoun@gmail.com">petr.salomoun@gmail.com</a> | 
  <strong>GitHub:</strong> <a href="https://github.com/petr-salomoun">@petr-salomoun</a>
</p>

