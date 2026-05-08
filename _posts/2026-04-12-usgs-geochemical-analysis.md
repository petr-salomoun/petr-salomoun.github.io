---
author: Petr Salomoun
categories:
- geology
date: 2026-04-12 22:43:25+00:00
excerpt: '> Sixty thousand scoops of river mud, half a million deposit records, and
  > a few hundred lines of Python in search for gold. ---'
github_repo: petr-salomoun/usgs-geochemical-analysis
layout: post
tags:
- geochemistry
- mining
- PCA
- machine-learning
- mineral-exploration
- USGS
title: Can Stream Water Tell Us Where the Gold Is?
updated_at: '2026-04-12T22:43:25+00:00'
---

# Can stream water tell us where the gold is?
## Mapping America's hidden mineral deposits with data science

> *Sixty thousand scoops of river mud, half a million deposit records, and
> a few hundred lines of Python in search for gold.*

---

## The idea

Picture a gold prospector in 1849.  He has a pan, a mule, and a hunch.  He wades into a cold Sierra Nevada creek, scoops up a pan of gravel, and swirls it until the heavy gold flakes settle to the bottom.  Then he follows the trail upstream — panning, walking, panning again — until the flakes run out.  Somewhere up there is the vein.

It is slow, dangerous, and romantic.  Most prospectors found nothing. Many found death. A few found fortunes.

Now imagine doing the same thing using a laptop, from the comfort of your home.

The US Geological Survey spent decades collecting river-bed sediment samples from 67,740 streams across the entire country.  Instead of panning for gold, they measured the chemistry of every scoop — arsenic, antimony, mercury, thallium, and 34 other elements.  Each sample is a chemical fingerprint of the rocks the stream passed over upstream.

The same agency catalogued every known US mineral deposit — 429,205 gold mines, copper porphyries, uranium fields — in a freely downloadable database.

**The question:** can a computer learn to recognise the chemical footprint of a gold deposit from the mud downstream — and point to places where that footprint exists but no mine has been found?

That is what this project does.  We *mine data to find gold*.

Every river carries a chemical memory of the rocks it has crossed.  If a
stream passes over a buried gold deposit, trace amounts of antimony, arsenic,
and other metals leach from the ore body and settle into the river-bed sediment
a few kilometres downstream — a faint but measurable chemical shadow of the
mineralisation upstream.

**We all love the glittering precious metal, so throughout this report, gold is the running example**, but the pipeline runs the same analysis for all 28 commodity groups tracked by the MRDS.  If your target is copper, uranium, or rare earths — it is all in there.


---

## The data

| Dataset | Source | Records | What it contains |
|---|---|---|---|
| NGS stream sediment | [USGS National Geochemical Survey](https://mrdata.usgs.gov/geochem/) | 67,740 samples | Concentrations (ppm) of 38+ elements per site |
| MRDS mineral deposits | [USGS Mineral Resources Data System](https://mrdata.usgs.gov/mrds/) | 429,205 deposits | Location, commodity (gold, copper, …), type, development status |

Both datasets are publicly available at no cost.  The pipeline downloads them
automatically.

![NGS sample coverage](images/01_ngs_sample_coverage_us.png)
*67,740 NGS stream-sediment collection sites across the United States.*

![MRDS deposits by development status](images/02_mrds_by_status_conus.png)
*429,205 MRDS mineral deposit records coloured by development status (active, past-producer,
prospect, occurrence).  Most known deposits in the western US are past-producers; the
Colorado Plateau and Basin and Range show the densest concentrations.*

---

## How the analysis works: following gold from mine to river mouth

The pipeline processes the data in five analytical steps.  Each step is a
distinct scientific question; together they form a progression from raw
chemistry to spatial prediction.

### Step 1 — Labelling the landscape

Before any statistics can be run, we need to know which samples are "near" a
gold deposit, which are "far", and which are in between.

This sounds simple but has a subtlety: a sample might be 0.8 km from a gold
mine *and* 1.2 km from a copper deposit.  To capture both relationships, every
NGS sample gets a separate distance measurement to the nearest deposit of
**each** commodity — gold, copper, iron, uranium, and so on for all 28 commodity
groups.  This is done by building a spatial index (a k-d tree) for each
commodity's deposits and querying the nearest neighbour for every sample.

Three zones are defined per commodity:

| Zone | Distance | What it means |
|---|---|---|
| **Core** | < 1 km | Sediment directly downstream of a deposit — strongest chemical signal |
| **Halo** | 1–7 km | Dispersal plume — signal still present but diluting |
| **Background** | > 7 km | No deposit influence — used as the reference population |

> **All three thresholds are configurable** in `usgs_config.yaml`
> (`proximity.core_radius_km`, `proximity.halo_max_km`,
> `proximity.background_exclusion_radius_km`).  Try tightening the core to
> 0.5 km or widening the halo to 10 km and see how the signal changes.

A 2 km "exclusion buffer" around all known deposits is subtracted from the
background: sediment that close to *any* deposit, even an unknown secondary
one, should not be used as a chemical baseline.

> **Why this matters for gold:** Nevada's Basin and Range province has dozens of
> gold mines within 20 km of each other.  Without the exclusion buffer, samples
> labelled "background" might actually sit between two gold deposits and carry
> elevated arsenic — which would make gold deposits look *less* distinctive, not
> more.

---

### Step 2 — Measuring the chemical signal

With zones defined, the first statistical question is: which elements are
elevated near gold deposits compared to genuinely pristine background?

```
enrichment ratio = median concentration in core zone
                  ─────────────────────────────────────
                  median concentration in background
```

The background median is computed after removing extreme outliers (values more
than a few interquartile ranges above the 75th percentile), so that a single
contaminated sample cannot distort the reference level.

**Gold enrichment results — elements measured at < 1 km from a gold deposit vs background:**

| Element | Enrichment near gold | Significance | Notes |
|---|---|---|---|
| SB (antimony) | **7.5×** | ★★★ | Strongest gold tracer in this dataset |
| AU (gold itself) | **3.75×** | ★★★ | Measurable in only 70 core samples (< 0.2 % detection) |
| MN (manganese) | ~2× | ★★ | Broadly elevated in hydrothermal-altered zones |
| AS (arsenic) | **1.9×** | ★★ | Classic Au pathfinder |
| CR (chromium) | ~1.7× | ★★ | Elevated in mafic-hosted and orogenic Au systems |
| HG (mercury) | ~1.3× | ★ | Present but modest enrichment |
| TL (thallium) | ~1.2× | ★ | Trace indicator |
| AG (silver) | 0.70× | — | *Depleted* near gold deposits in this dataset |

The last two rows are worth pausing on.  Gold itself is measurable in barely 0.2 % of NGS samples — the detection limit is above the concentration actually present in most stream sediments.  And silver is *lower* near gold deposits than in background, which is unusual.  This reflects the fact that the MRDS "gold" category includes a mix of deposit types; many are low-sulphidation epithermal systems where Ag is not typically co-deposited with Au.

The dominant signal is antimony — a near-perfect tracer for the Sb–Au epithermal association — followed by arsenic.

![Gold element enrichment](images/09b_enrichment_gold.png)
*Log₂(enrichment ratio) for each element near gold deposits vs background.
Positive values (red) mean elevated near gold; negative (blue) means depleted.
Antimony (SB) and gold itself (AU) dominate, followed by manganese and arsenic.
Silver (AG) is the only element with a significant negative signal.*


**Counter-intuitive result — silver is *depleted* near gold deposits:**
The enrichment analysis shows silver (AG) at 0.70× near gold — lower than typical background.
For other sulphide-associated commodities (iron, zinc), calcium (CA) is also
frequently depleted — an effect of hydrothermal acid leaching of carbonate minerals.
In both cases the composite score explicitly accounts for this: elements that are
systematically *lower* near deposits contribute negatively to the score,
making the combined test more sensitive than looking for high values alone.

![Element enrichment matrix — core (filtered)](images/07b_element_commodity_matrix_core_filtered.png)
*Enrichment ratios for key element × commodity combinations at the core zone
(< 1 km).  Red = elevated near deposits; blue = depleted.  Only elements with
a strong signal (|log₂| > 0.5) for at least one commodity are shown.
Gold's column shows the SB and AU positive loading; silver (AG) appears depleted.
The full matrix (all 38+ elements × all 28 commodities) is also available as
`images/07_element_commodity_matrix_core.png`.*


![Element enrichment matrix — halo (filtered)](images/08b_element_commodity_matrix_halo_filtered.png)
*Same filtered matrix for the halo zone (1–7 km).  The halo signal is generally
weaker than the core, consistent with chemical dilution with distance from the deposit.
Cross-commodity patterns — e.g. antimony elevated near both gold and lead deposits —
reflect genuine geochemical overlaps between deposit families.*

---

### Step 3 — Turning multi-element patterns into a single score (PCA)

Looking at each element separately is useful but incomplete.  Gold deposits
don't just elevate antimony — they elevate antimony *and* arsenic *and* chromium
*together*, in a correlated pattern.  A sample with high arsenic but normal
antimony might be near an arsenic-only source (like a mine waste pile), not a gold
mine.  The correlation between elements carries information that single-element
tests discard.

Principal Component Analysis (PCA) is a standard technique for compressing
correlated variables into a smaller number of independent dimensions.  Applied
to geochemistry, it finds the combination of elements that best separates
deposit-proximal samples from background — the "geochemical fingerprint" of
each deposit type.

**How it works:**

1. For each commodity, select the element suite from published geological
   literature (e.g. for gold: Au, As, Sb, Hg, Ag, Tl, Bi, Te, Se, Mn, Ba,
   Co, Ni, Cr).
2. Log-transform concentrations (element data span several orders of magnitude
   and are log-normally distributed; the transform makes them roughly Gaussian).
3. Subtract the mean and divide by the standard deviation of each element
   across the dataset.
4. Run PCA.  The first principal component (PC1) aligns with the direction of
   maximum variance in the data.  For geochemical data trained on deposit-zone
   samples, PC1 typically aligns with the enrichment-vs-background contrast while
   other PCs capture different patterns — e.g. regional geological background, 
   or specific deposit subtypes. 
5. Read off which elements load positively on PC1 (elevated near deposits) and
   which load negatively (depleted near deposits).
6. Compute a composite score for every sample:

```
score = Σ log(element) for positive-loading elements
      − Σ log(element) for negative-loading elements
```

This single number summarises whether the sample's chemistry looks like it is
sitting on top of a gold deposit, far from one, or somewhere in between.

![Gold PCA loadings](images/10b_pca_loadings_gold.png)
*PCx loading for each element in the gold pathfinder suite.  Bar height = loading magnitude;
direction (positive/negative) = whether the element drives the composite score up or down.
CR, TL, TE, AU top the positive side; BI and AG are the main negative loaders.*

**Why use a predefined element suite instead of all 38+ elements?**
Using all elements does not improve performance and introduces several
problems.  First, many elements (barium, calcium, sodium) reflect regional
geological background — the type of bedrock — rather than mineralisation.
Including them adds noise that drowns out the deposit signal.  Second,
elements like aluminium and titanium are essentially constant across igneous
and metamorphic terranes; they contribute zero discriminating power and waste
degrees of freedom in the PCA.  Third, the predefined suites encode 50 years of
published research on which elements co-mobilise with each commodity — this
domain knowledge acts as a feature filter that makes the model both more
accurate and more interpretable.

![PCA formula heatmap](images/10_pca_formula_heatmap.png)
*PC1 loading values for each element × commodity combination.  Red cells
(positive loading) indicate the element drives the composite score up near
deposits; blue cells (negative loading) drive it down.*

**Results for gold (PC1) — what actually came out of the pipeline:**

| Element | Role on PC1 | Geological meaning |
|---|---|---|
| CR, TL, TE, AU | positive (top loadings) | Trace metals — strong gold/hydrothermal association |
| BA, AS, NI, HG | positive | Epithermal and orogenic system indicators |
| CO, MN, SB, SE | positive | Broadly co-mobile in hydrothermal systems |
| BI, AG | negative | Depleted in the composite gold signal |

PC1 explains **28.4 %** of variance in the combined signal+background population for gold.  The composite score aggregates all positive loaders minus all negative loaders, giving a single number that tracks how closely a sample's chemistry resembles the gold-deposit signature.

A sample is flagged as a **PCA anomaly** when its composite score is substantially higher than typical background values (specifically: above the 75th percentile of background scores plus twice the interquartile range). These are the candidate exploration targets.

| PC1 — deposit signal | PC2 — regional background |
|---|---|
| ![Gold PCA — PC1](images/13_pca_heatmap_gold.png) | ![Gold PCA — PC2](images/13b_pca_heatmap_gold_pc2.png) |
| *PC1 score: concentrates in Nevada, the Black Hills (SD) — the major US gold provinces.* | *PC2 score: captures a different dimension — regional geology rather than deposit proximity.  The two maps together illustrate that different principal components bring complementary detection signals.* |

![Uranium PCA heatmap](images/15_pca_heatmap_uranium.png)
*Uranium PC1 score for comparison.  The Colorado Plateau (Utah/Colorado/Arizona/New
Mexico) and the Wyoming Powder River Basin light up without any geological
input to the model — validating that the geochemical signal alone encodes
spatial information about mineralisation.*

![PCA halo profile for gold](images/17_pca_halo_gold.png)
*Gold composite score vs distance from nearest gold deposit.  Scores are highest
inside 1 km, remain elevated through the 3–5 km halo, and return to background
beyond 7 km.  This dispersal length is consistent with stream transport of
fine particulate material.  Some components have their maxima notably in the halo
rather than the core, due to the different mobility of elements in the river system;
these help detect deposits further away where the core signal is already weakened.*

---

### Step 4 — Learning the difference: machine-learning classification

PCA identifies the chemical pattern without knowing in advance what that
pattern should look like — it is an unsupervised method.  The machine-learning
step takes the opposite approach: it uses the known deposit locations as a
training signal to learn a classifier that predicts whether a given sample is
near a deposit.

**The model:** a random forest — an ensemble of decision trees, each trained on
a random bootstrap sample of the data and a random subset of features.
Predictions are made by majority vote across all trees.  One model is trained per commodity.

**Training data:**
- Positive class: samples in the core zone (< 0.5 km from a gold deposit).
- Negative class: samples in the background zone (> 7 km from any deposit).
- Because background samples vastly outnumber core samples, the negative class
  is randomly undersampled to a 3:1 ratio.  Without this step the model would
  achieve 99 % accuracy simply by predicting "not a deposit" for everything —
  but it would miss every real deposit.

**Features:** log-transformed concentrations of the pathfinder element suite.

**Results (held-out test set, 25 % of data not used for training):**

| Commodity | ROC-AUC | What it means |
|---|---|---|
| Gold | **0.9996** | Near-perfect separation of core from background |
| Uranium | 1.000 | Perfect separation (small core population, n=1,086) |
| Silver | 0.961 | Very strong separation |
| Copper | 0.888 | Strong separation |
| Top predictors for gold | — | Bismuth (BI, 29 %), silver (AG, 22 %), antimony (SB, 18 %), thallium (TL, 16 %) |

ROC-AUC (Receiver Operating Characteristic — Area Under the Curve) measures how
well the classifier distinguishes the two classes regardless of the
classification threshold.  A value of 1.0 is perfect; 0.5 is chance.

**An honest note on the near-perfect score for gold:**
ROC-AUC = 0.9996 does not mean the model can predict unknown gold deposits perfectly.  It
means that, *among known deposits*, the chemistry at core-zone samples is so
different from background that a simple classifier can almost perfectly separate them.
Two factors inflate this number: (1) the model is trained and tested on samples
near *already-discovered* deposits, and there is a strong sampling bias — samples
concentrate near known deposits; (2) samples from the same mining district appear in both train and
test sets, so some of the apparent generalisation is actually pattern-matching
within a familiar district.  Real predictive power would require testing against
deposits discovered *after* the chemistry data was collected.

The result is still meaningful: it confirms that the geochemical signal of gold
mineralisation is strong, self-consistent, and learnable — a necessary
foundation for any prospectivity application.

**Three methods, one story — comparing how each approach ranks gold's pathfinder elements:**

| Element | Enrichment ratio | PCA (PC1 loading) | ML feature importance |
|---|---|---|---|
| SB (antimony) | **7.5×** ★★★ | positive | 0.178 (3rd) |
| AU (gold itself) | **3.75×** ★★★ | positive (top-5) | 0.120 (5th) |
| BI (bismuth) | 1.19× | **negative** | **0.287 (1st)** |
| AG (silver) | **0.70× depleted** | negative | 0.222 (2nd) |
| TL (thallium) | 1.24× ★ | positive (top-5) | 0.162 (4th) |
| AS (arsenic) | 1.87× ★★ | positive | lower rank |
| HG (mercury) | 1.34× ★ | positive | lower rank |

This comparison reveals both agreement and complementarity:
- **Agreement:** Antimony, thallium, and arsenic appear as positive signals in all three methods.
- **Complementarity:** Bismuth (BI) and silver (AG) are the *top two* ML features despite being negative in PCA and nearly flat (or depleted) in enrichment ratios.  This is because the random forest exploits *multivariate interactions* — it learns that the combination of elevated BI with suppressed AG is a strong discriminator, even though neither element is strongly anomalous on its own.  PCA and enrichment ratios look at each element's marginal distribution; the random forest finds interaction patterns that single-variable tests miss.
- **What to trust:** For identifying the dominant geochemical signal, enrichment ratios and PCA are more interpretable and geologically grounded.  For prediction (classifying samples as core vs background), the ML model's feature importances better reflect which variables actually discriminate — even if those variables don't tell a simple geochemical story.
We benefit from using all of them: chemistry, ML, and PCA (and its individual components) track different signals, either reinforcing each other into a
stronger prediction or one detecting signal even where another method fails.

---

### Step 5 — Pinpointing the source: spatial gradient ascent

Now, all our methods predict a deposit may be nearby, and often we have a signal cluster
in a wider area.  How do we know exactly where to start the search?

The next step attempts to pinpoint the most probable location based on concentration differences in
nearby samples.  Once we have a cluster, the gradient ascent algorithm searches in the direction
where the composite score increases most steeply.

The algorithm works like finding the highest point in a foggy mountain range
by always walking uphill:

1. **Cluster** the anomalous samples using a density-based algorithm (DBSCAN)
   that groups nearby points without needing to specify the number of clusters
   in advance.
2. **Smooth** the z-scores across the cluster by computing an
   inverse-distance-weighted score field on a 200 m grid.  This acts like a
   local average, suppressing single-sample spikes while preserving the
   spatial trend.
3. **Walk uphill:** starting from the score-weighted centre of the cluster,
   take steps of 100 m in the direction the score increases most steeply.
4. **Stop** when the slope flattens out (the gradient is less than 1 % of the
   steepness at the starting point), or when the walk has moved too far from
   the cluster, or after a maximum of 150 steps.
5. The stopping point is the predicted deposit location.  A confidence score
   is computed from how strongly elevated the cluster scores are relative to
   background.

The predicted locations are shown as ★ star markers in the **Gradient
Predictions** layer of the interactive map, together with the cluster constituents.
A gradient prediction implies a cluster of anomalies nearby, so even if the location is imprecise,
the area is definitely worth exploring.

It is the ultimate "where to dig" prediction of this analysis; it is time to close the laptop and pick up the pick and shovel.
Data can only take you so far.

> **Important caveat about "upstream":** The gradient ascent climbs the *score gradient* — it moves toward the area of highest predicted geochemical anomaly.  It does not follow the actual water flow network upstream.  In real drainage basins, the true deposit may be several kilometres in a different direction from the anomaly cluster, depending on stream directions.  The current predictions should be treated as "anomaly centroids" rather than precise deposit coordinates.  Hydrological analysis is beyond the scope of this experiment; once in the area, follow the stream.

---

## What the data says: five findings

### 1. Gold's chemical shadow extends up to 10 km from the mine

The halo profile confirms that the gold composite score — whose halo plots are dominated by chromium (CR), thallium (TL), tellurium (TE), gold (AU), and barium (BA), the top-5 PC1 elements by loading² — remains elevated well beyond the deposit boundary and remains strong up to about 5 km from the nearest gold deposit in the data.  Beyond 7 km the signal gradually returns to background levels.  This is the downstream dispersal plume captured by stream sediment.

### 2. Geochemistry alone can reproduce the map of US mining districts

Without any geological or topographic input, the PCA composite scores for gold,
uranium, and copper cluster in exactly the right places: Nevada for gold, the
Colorado Plateau for uranium, Arizona for copper.  The chemistry encodes spatial
information about mineralisation, validating the method — although a strong sampling
bias is present.

### 3. Some elements are *missing*, not elevated, near certain deposits

Silver (AG) is statistically *lower* near gold deposits than in background (0.70× enrichment ratio) — a real and measurable signal in this dataset.  This likely reflects the MRDS "gold" category's dominance by low-sulphidation epithermal systems, where gold is not typically co-deposited with silver.  The composite score explicitly accounts for this: elements that are systematically *lower* near deposits contribute negatively to the score, making the combined test more sensitive than looking for high values alone.

### 4. The signal is strong enough for ML classifiers to learn

ROC-AUC of 0.9996 for gold and 0.96 for silver means the multi-element patterns are robust,
internally consistent, and learnable by standard supervised methods.  Antimony (SB) and thallium (TL)
rank consistently across all three methods — enrichment ratio, PCA loading, and ML feature importance —
validating that these are genuine geochemical tracers.  Interestingly, bismuth (BI) and silver (AG)
emerge as the *top two* ML discriminators despite being negative loaders in PCA, illustrating that
the supervised model finds multivariate interaction patterns that the unsupervised enrichment and PCA
analyses miss.  Copper at AUC 0.89 and several other commodities at 0.80–0.99 further validate the
geochemical signal across deposit types.

### 5. Gradient ascent predictions cluster in geologically expected regions

The predicted deposit locations are not randomly scattered.  They concentrate
in known mining provinces, consistent with the idea that they are tracking
real geochemical anomalies rather than noise.  Predictions in areas without
known deposits are the most prospectively interesting — potential exploration
leads that would require field follow-up to evaluate.

> **An important caveat about sampling bias:** Both the ML classifier and the
> PCA anomaly scores are inherently biased towards areas with high sampling
> density — which, in the NGS dataset, largely coincides with historically
> active mining regions.  The USGS collected more samples near known mines
> (because those areas were already of interest), so the model has seen far
> more examples from Nevada or Arizona than from less-explored regions.
>
> The gradient ascent step compounds this sampling bias: it needs a **cluster** of anomalous
> samples to initiate a walk, so it will always predict more deposit locations
> in densely sampled areas. 
>
> This indeed leads to 'rediscovering' known mines, but by the same token
> makes similar signals in unexplored areas even more interesting.

---

## The interactive map

`interactive_map.html` is a fully **offline**, self-contained map — no
internet connection is needed once the file is downloaded (unless OpenStreetMap tile layers are required).
Open it in any modern browser (Chrome, Firefox, Safari, Edge).

![Interactive map of candidates](images/interactive_map.png)

> **Download interactive map:**
> [interactive_map.html](https://github.com/petr-salomoun/usgs-geochemical-analysis/releases/download/v1.0/interactive_map.html)
> (~200 MB — download and open locally in any modern browser; no internet required after download)

All Leaflet mapping code, styles, and base tiles are baked into the HTML file
at build time, so the map works on restricted networks and can be shared as a
single attachment.

### Layer panel (right side of the map)

The layer control panel organises layers into five sections.  All layers are
hidden by default to keep the map fast; enable them one at a time or in
combination.

| Section | What it shows | Marker |
|---|---|---|
| **Deposits** | Known MRDS mineral deposits, one group per commodity | Coloured triangle, colour = commodity |
| **Gradient Predictions** | Predicted deposit source locations (pair-vector algorithm) | ★ filled star, colour = commodity |
| **ML Predictions** | NGS samples the ML classifier predicts as deposit-proximal | Small filled circle, colour = commodity |
| **PCA Anomalies** | Samples with anomalously high PCA composite score | Rotated square (diamond), colour = commodity |
| **Element Anomalies** | Samples anomalous in a single element (univariate IQR threshold) | Small filled circle, colour by element |

### Suggested tour

1. Enable **Deposits → Gold** to see the spatial distribution of known gold
   deposits across the western US.
2. Enable **PCA Anomalies → Gold** alongside it.  Do the anomaly clusters (diamond
   markers) coincide with the known deposits (triangles)?  Are there clusters in
   areas without known deposits?  Then add **ML Predictions → Gold** (filled circles)
   to see how the supervised classifier's view compares to the unsupervised PCA.
3. Enable **Gradient Predictions → Gold** (★ stars) to see the inferred deposit-source
   locations predicted from the anomaly clusters.
4. Switch to **Uranium**: enable Deposits, PCA Anomalies, and Gradient
   Predictions together to see the Colorado Plateau concentration.
5. Use **Element Anomalies → AS** (arsenic) alongside the gold PCA layer to
   compare the univariate arsenic signal with the multi-element composite.
   Notice that PCA anomalies are more geographically focused than the raw
   arsenic anomaly alone.

### Base tiles

Use the tile switcher (top-left) to toggle between:
- **White canvas** (default) — clean background for analytical work
- **OpenStreetMap** — geographic context (requires internet; may show tile errors due to a known issue on OpenStreetMap's side)

---


## Data files

| File | Description |
|---|---|
| `interactive_map.html` | Offline interactive map (single self-contained HTML file) |
| `data/ngs_mrds_correlated.gpkg` | All 67,740 NGS samples with composite scores, anomaly flags, and ML predictions |
| `data/pca_scores.csv` | Per-sample PCA scores and anomaly flags for 28 commodities |
| `data/gradient_predictions.csv` | Predicted deposit locations: coordinates, commodity, confidence |

---

## Science report

For the full methodology, statistical details, caveats, and output-file
reference, see [DETAILS.md](DETAILS.md).

---

## Try it yourself

### Requirements

```
Python >= 3.10
geopandas >= 1.0
pandas >= 2.0
numpy
matplotlib
seaborn
scikit-learn
folium >= 0.20
```

### Running the pipeline

```bash
git clone <this-repo>
pip install -r requirements.txt

python collector.py            # ~5–30 min  — downloads ~200 MB from USGS
python explorer.py             # ~5–10 min  — per-element anomaly flags
python ngs_mrds_correlator.py  # ~10–20 min — spatial join, enrichment analysis
python pca_analysis.py         # ~5–15 min  — PCA scoring per commodity
python ml_pipeline.py          # ~10–30 min — classifiers + gradient ascent
python visualizer.py           # ~5–10 min  — interactive map + static charts
```

To regenerate only the map without re-running the full pipeline:

```bash
python visualizer.py --map-only
```

### Key configuration parameters (`usgs_config.yaml`)

| Parameter | Default | Effect |
|---|---|---|
| `proximity.core_radius_km` | 1.0 | Core-zone radius |
| `proximity.halo_max_km` | 7.0 | Outer halo boundary |
| `proximity.background_exclusion_radius_km` | 2.0 | Exclusion buffer |
| `gradient.cluster_radius_km` | 5.0 | DBSCAN cluster radius for gradient ascent |
| `gradient.confidence_threshold` | 0.38 | Minimum prediction confidence |
| `gradient.ascent_step_m` | 100 | Walk step size |

---

## Licence and attribution

Data: USGS public-domain (no copyright restrictions on the underlying data).

Code and analysis: free to use for any purpose (personal, commercial, academic),
but **attribution is required for any publication of derived work** — please cite
or credit the author:

> Petr Salomoun, *Mapping America's Hidden Minerals — a Data Science Journey* (2026).
> [petr.salomoun@gmail.com](mailto:petr.salomoun@gmail.com)

Bug reports and suggestions are welcome.