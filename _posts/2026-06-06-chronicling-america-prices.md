---
author: Petr Salomoun
categories:
- economic-history
date: 2026-06-06 00:00:00+00:00
description: "255,518 structured price records extracted from 112 American newspapers (1770–1963) using LLMs reveal war inflation, the Gold Standard's stabilising effect, railroad market integration, and the Great Depression's agricultural collapse."
excerpt: "LLM-extracted price data from 200 years of American newspapers confirms that wars caused massive food inflation, the Gold Standard was 1.8× more stable, railroads cut wheat price dispersion by 41%, and price controls actually worked in WWII."
github_repo: petr-salomoun/chronicling-america-prices
layout: post
tags:
- economic-history
- NLP
- GPT
- LLM
- price-data
- inflation
- newspapers
- Library-of-Congress
- data-analysis
- gold-standard
- historical-data
title: 'Chronicling America Price Dataset: 200 Years of U.S. Prices from Newspaper Archives'
updated_at: '2026-06-06T00:00:00+00:00'
---

# Chronicling America Price Dataset
## 200 Years of U.S. Prices from Newspaper Archives

> **How it works:** Raw OCR pages from 112 newspapers (Library of Congress Chronicling America archive, 1770–1963) were denoised and compressed to 20% of their original token volume using GPT-4o-mini. A second LLM pass extracted individual price mentions; a third normalized them to USD, assigned commodity codes, and applied statistical QC — yielding **255,518 structured records** with commodity classification, standardized units, and confidence scores.

**Contents:** [The Dataset](#1--the-dataset) · [Pipeline](#2--the-pipeline) · [Food Prices and Wars](#3--food-prices-track-every-american-war) · [The Great Depression](#4--the-great-depression-collapsed-agricultural-prices) · [Gold Standard](#5--the-gold-standard-stabilised-prices) · [Railroad Integration](#6--railroads-integrated-markets) · [Agricultural Expansion](#7--agricultural-expansion-deflated-grain-prices) · [Volatility by Category](#8--volatility-by-economic-category) · [Full Price Index](#9--composite-price-index) · [Summary](#10--summary-of-findings)

---

## 1 · The Dataset

| Metric | Value |
|--------|-------|
| Total records | **255,518** |
| With USD prices | 244,551 (95%) |
| Time span | 1770–1963 |
| Newspaper sources | 112 |
| Commodity types | 79 |
| Economic categories | 11 |

![Raw Pages per Year](https://raw.githubusercontent.com/petr-salomoun/chronicling-america-prices/master/report_figures/fig1_raw_pages_per_year.png)
*Coverage by year — denser after 1850 as digitization improves.*

Historical price data before the 20th century is sparse, inconsistent, and trapped in unstructured sources. Government price indices (BLS, NBER) begin reliably only around 1890. Newspaper advertisements and market reports contain rich price information going back to the colonial era — but extracting it at scale requires reading millions of pages of noisy OCR text.

This project applies modern LLMs to that problem: reading OCR text, denoising it, identifying price mentions, classifying commodities, standardizing units, and converting currencies — producing a clean JSONL dataset ready for quantitative analysis.

**Categories covered:** Food & grain, dairy, meat, sugar, beverages; labor (farm, domestic, professional, unskilled); real estate; transportation; textiles; raw materials; financial instruments; miscellaneous.

![Category Distribution](https://raw.githubusercontent.com/petr-salomoun/chronicling-america-prices/master/report_figures/fig2_category_distribution.png)
*Distribution of price records across the 11 economic categories.*

**Record format** (JSONL):
```json
{
  "commodity_id": "FOOD-GRAIN-WHEAT",
  "category_l1": "Food & Agriculture",
  "price_per_unit_usd": 1.25,
  "unit": "bushel",
  "year": 1862,
  "location": "Chicago, IL",
  "ref": "sn84026749/1862-03-15/ed-1/seq-4",
  "confidence": 0.92,
  "original_text": "Wheat No.1 Spring $1.25 per bushel"
}
```

---

## 2 · The Pipeline

The extraction pipeline has four stages, each using LLM calls with structured output:

**Stage 0 — Download:** Fetch OCR text pages from the LOC Chronicling America API for all available newspapers in the target year range.

**Stage 1 — Compress:** The LLM reads raw OCR, which is often garbled, and produces clean compressed text. It reduces data volume to about **20% of the original token count** while preserving all facts (names, prices, numerals).

**Stage 2 — Extract:** The LLM identifies individual price mentions in the compressed text and outputs structured records with commodity, price, unit, date, and location.

**Stage 3 — Normalize:** The LLM classifies each extracted mention into a 79-commodity taxonomy, standardizes units (bushels, pounds, barrels, etc.), converts historical currencies to USD, and assigns confidence scores. Statistical QC filters apply physical price bounds and outlier removal.

Each stage supports parallelization (`--workers N`) and checkpoint/resume via progress files.

The LLM-compressed OCR text (pass 0) is published as a GitHub release artifact: **[Download pass0_compressed_ocr.tar.gz (~265 MB)](https://github.com/petr-salomoun/chronicling-america-prices/releases/tag/v1.0)**.

---

## 3 · Food Prices Track Every American War

![Flour Prices Across All Wars](https://raw.githubusercontent.com/petr-salomoun/chronicling-america-prices/master/report_figures/fig3_flour_all_wars.png)
*Flour and wheat prices indexed around each major American conflict.*

The price record confirms war-driven inflation in every major conflict — and reveals a striking exception:

| War | Commodity | Price Change |
|-----|-----------|-------------|
| Civil War | Flour | **+196%** |
| WWI | Wheat | **+132%** |
| WWI | Flour | **+263%** |
| WWII (OPA controls active) | Food basket | **+25%** |
| Post-WWII (controls lifted) | Food basket | **+96%** |

WWII stands out: only a 25% rise during the war itself — far below WWI's +132–263% — suggesting the Office of Price Administration's controls worked. The 96% surge immediately after controls were lifted confirms that the underlying inflationary pressure had simply been deferred.

---

## 4 · The Great Depression Collapsed Agricultural Prices

![Food Staple Prices](https://raw.githubusercontent.com/petr-salomoun/chronicling-america-prices/master/report_figures/fig4_food_staples.png)
*Indexed prices of wheat, butter, and pork, 1910–1945.*

Between 1925–29 and 1930–34:

| Commodity | Price Change |
|-----------|-------------|
| Wheat | **-59%** |
| Butter | **-58%** |
| Pork | **-43%** |

The collapse in farm prices — not retail prices — explains much of the rural banking crisis and the cascade of farm foreclosures that deepened the Depression in agricultural regions.

---

## 5 · The Gold Standard Stabilised Prices

The dataset spans both the classical gold standard era (1879–1914) and the post-gold period, enabling a direct volatility comparison:

| Era | Wheat Price CV |
|-----|----------------|
| Gold standard (1879–1914) | **0.254** |
| Post-gold standard | **0.466** |

**The post-gold era was 1.8× more volatile.** This single figure captures the central debate in monetary history: the gold standard constrained both inflation and deflation, resulting in smaller year-to-year price swings despite the periodic panics of the late 19th century.

---

## 6 · Railroads Integrated Markets

![Wheat Price Dispersion](https://raw.githubusercontent.com/petr-salomoun/chronicling-america-prices/master/report_figures/fig9_wheat_dispersion.png)
*Geographic dispersion of wheat prices across newspaper sources, by decade.*

Price dispersion — the standard deviation of wheat prices across city markets in a given year — fell sharply as the rail network matured:

| Period | Description | Dispersion Change |
|--------|-------------|-------------------|
| 1820–1850 | Pre-railroad era | Baseline |
| 1890–1910 | Mature network | **-41%** |

The 41% reduction in geographic price variance is the quantitative fingerprint of market integration. Before the railroad, wheat prices in Chicago, New Orleans, and Boston could diverge by 30–50% due to transport costs and information lags. By 1900, arbitrage had compressed that gap to near-transport-cost levels.

---

## 7 · Agricultural Expansion Deflated Grain Prices

Between 1880–85 and 1895–1900, as homesteading opened the Great Plains:

| Commodity | Price Change |
|-----------|-------------|
| Wheat | **-38%** |
| Corn | **-32%** |

This deflation, beneficial for consumers, devastated farmers — producing the populist movement, free-silver agitation, and Bryan's 1896 campaign. The newspaper price data captures the exact magnitude of the grievance that drove late-19th-century agrarian politics.

---

## 8 · Volatility by Economic Category

![Volatility by Category](https://raw.githubusercontent.com/petr-salomoun/chronicling-america-prices/master/report_figures/fig6_volatility.png)
*Coefficient of variation by economic category, 1850–1950.*

| Category | Relative Volatility |
|----------|---------------------|
| Raw materials | Highest |
| Agricultural commodities | High |
| Manufactured goods | Moderate |
| **Wages** | **Lowest (stickiest)** |

Wages show the lowest price volatility of any category — consistent with modern labor economics findings that nominal wages are downwardly rigid. Commodity prices, especially raw materials, swing far more violently with demand shocks. This hierarchy is stable across all sub-periods in the dataset.

---

## 9 · Composite Price Index

![Food Price Index 1880=100](https://raw.githubusercontent.com/petr-salomoun/chronicling-america-prices/master/report_figures/fig8_price_index.png)
*Composite food price index (1880 = 100), 1820–1960.*

A weighted composite index across all commodity categories reveals the full arc of American price history: the long deflation of the Gilded Age, the WWI spike, the interwar roller coaster, and the post-WWII permanent step upward that defined the modern inflationary era.

---

## 10 · Summary of Findings

| Hypothesis | Result | Magnitude |
|-----------|--------|-----------|
| Civil War inflation | **Confirmed** | +196% flour |
| WWI food inflation | **Confirmed** | +132% wheat, +263% flour |
| Great Depression deflation | **Confirmed** | -59% wheat |
| Gold Standard stability | **Confirmed** | 1.8× less volatile |
| Agricultural expansion | **Confirmed** | -38% wheat |
| WWII price controls | **Confirmed** | +25% (vs +132% WWI) |
| Railroad market integration | **Confirmed** | 41% variance reduction |

The dataset's value extends beyond these headline hypotheses. As a machine-readable, structured time series spanning 1770–1963, it fills a critical gap between colonial-era price observations and the BLS-era systematic coverage. Any economic historian working on pre-1890 U.S. commodity markets now has a corpus of a quarter-million price quotes, each linked to a source newspaper page in the Library of Congress archive.

---

*June 2026 · GPT-4o-mini · Library of Congress Chronicling America API → OCR compression → LLM price extraction → normalization + QC · ~255,518 records*

**Dataset download:** [pass0_compressed_ocr.tar.gz (~265 MB)](https://github.com/petr-salomoun/chronicling-america-prices/releases/tag/v1.0)

**License:** Data derived from the Library of Congress Chronicling America collection (public domain). Processing code and derived dataset released under a permissive license requiring attribution. Any use must attribute:
> *Chronicling America Price Dataset, 2024 · Petr Salomoun · [petr.salomoun@gmail.com](mailto:petr.salomoun@gmail.com)*
