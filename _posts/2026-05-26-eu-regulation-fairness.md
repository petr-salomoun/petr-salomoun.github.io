---
author: Petr Salomoun
categories:
- politics
- data-analysis
date: 2026-05-26 00:00:00+00:00
description: "GPT-5-mini scored 5.3 million paragraphs of EU legislation for narrow-group bias. 65% is neutral; agriculture and GMO approvals top the positive list; Russia/Ukraine sanctions dominate the negative."
excerpt: "5.3 million paragraphs of EU legislation scored by AI for narrow-group bias reveals that most EU law is neutral — but agriculture, GMO authorisations, and post-2022 sanctions tell a different story."
github_repo: petr-salomoun/eu-regulation-fairness
layout: post
tags:
- EU
- regulation
- fairness
- NLP
- GPT
- legislation
- sanctions
- agriculture
- EUR-Lex
- policy-analysis
title: 'EU Regulation Fairness: An AI Analysis of 65 Years of European Legislation'
updated_at: '2026-05-26T00:00:00+00:00'
---

# EU Regulation Fairness
## An AI Analysis of 65 Years of European Legislation

> **How it works:** Every paragraph of EU legislation was scored by GPT-5-mini on a **−1 to +1** scale — **+1** means it disproportionately benefits a narrow group, **−1** means it burdens one, **0** means it applies broadly and equally. This is a pattern-detection tool, not a legal verdict.

---

## 1 · The Numbers

| Metric | Value |
|--------|-------|
| Documents analyzed | **25,364** |
| Paragraphs scored | **5.3 million** |
| Words processed | **522 million** |
| Years covered | **1960–2026** |
| Overall mean score | **−0.011** |
| Mean Absolute Bias (MAB) | **0.128** |
| Benefiting narrow groups | **18.1%** |
| Burdening narrow groups | **16.5%** |
| Neutral / broadly applicable | **65.4%** |

**Scope:** Regulations, Directives, and Decisions from the Official Journal (EUR-Lex). Documents under 10,000 characters, plus Recommendations, opinions, and preparatory acts are excluded.

---

## 1b · Legislative Output Has Grown Dramatically

EU output was minimal in the 1970s, grew steadily as the single market was built, stabilised at 500–800 documents per year through the 2000s and 2010s, then broke records every year from 2022 onwards.

![Legislative output 1960–2026](https://raw.githubusercontent.com/petr-salomoun/eu-regulation-fairness/main/docs/charts/01b_volume_history.png)

| Period | Docs/year | Character |
|--------|-----------|-----------|
| 1960–1976 | <5 | Foundational treaties |
| 1977–1993 | 50–480 | Single market; slight positive bias |
| 1994–2010 | 440–790 | Mature regulatory state; near-zero bias |
| 2011–2019 | 590–790 | Sanctions growth begins; drift turns negative |
| 2020–2025 | 725–1,225 | Sanctions inflation; strongly negative mean |

The early positive bias reflects CAP build-out — rules that name specific products, geographic zones, and approved establishments. The post-2020 negative shift is driven by Russia/Ukraine sanctions: each update adds hundreds of named persons and entities, pulling the mean down.

---

## 2 · Most EU Law Is Neutral

![Score distribution](https://raw.githubusercontent.com/petr-salomoun/eu-regulation-fairness/main/docs/charts/01_distribution.png)

**65.4%** of all paragraphs score near zero — broadly applicable to everyone. Of the remaining 34.6%: **18.1%** benefits specific groups and **16.5%** burdens them. The slight overall negative mean (−0.011) is largely a sanctions artefact.

---

## 3 · A Sharp Turn After 2019

![Mean score trend](https://raw.githubusercontent.com/petr-salomoun/eu-regulation-fairness/main/docs/charts/02_mean_score_trend.png)

![Volume and MAB](https://raw.githubusercontent.com/petr-salomoun/eu-regulation-fairness/main/docs/charts/03_volume_mab.png)

![Composition](https://raw.githubusercontent.com/petr-salomoun/eu-regulation-fairness/main/docs/charts/04_composition.png)

Early decades (1960–1990) show a modest positive bias from agricultural and market-building legislation. The mean stays near zero through the 2000s, then turns persistently negative after 2011 as sanctions regimes expand. The post-2022 plunge tracks directly with Russia/Ukraine restrictive measures — each update names hundreds of individuals, pushing scores down across an ever-larger body of text.

**Key data points:**

| Year | Docs | Mean | MAB | Positive% | Negative% |
|------|------|------|-----|-----------|-----------|
| 2000 | 441 | +0.009 | 0.098 | 17.3% | 12.8% |
| 2010 | 620 | +0.012 | 0.118 | 19.0% | 13.1% |
| 2019 | 792 | −0.009 | 0.128 | 18.1% | 16.8% |
| 2020 | 725 | −0.048 | 0.165 | 17.0% | 22.4% |
| 2022 | 962 | −0.068 | 0.173 | 15.9% | 23.7% |
| 2024 | 1,144 | −0.047 | 0.164 | 18.7% | 22.1% |
| 2025 | 1,225 | −0.059 | 0.168 | 15.9% | 22.9% |

---

## 4 · Who Benefits by Sector

![Sector mean score](https://raw.githubusercontent.com/petr-salomoun/eu-regulation-fairness/main/docs/charts/05_sector_mean.png)

![Sector detail](https://raw.githubusercontent.com/petr-salomoun/eu-regulation-fairness/main/docs/charts/06_sector_detail.png)

**Agriculture (+0.028, 27.8% positive)** has the highest net positive bias of any sector. Thousands of CAP rules name specific commodities, geographic indications, and corporate products — each one scoring as a benefit to a narrow group.

**Industry (MAB 0.183)** is the most contested sector, with roughly equal volumes of pro- and anti-industry provisions — the fingerprint of a space where winners and losers are explicitly written into law.

**Finance (+0.018)** sits second on the positive side, driven by named product approvals, fund exemptions, and country-level prudential carve-outs.

---

## 5 · The Most Biased Documents

![Top documents](https://raw.githubusercontent.com/petr-salomoun/eu-regulation-fairness/main/docs/charts/07_top_docs.png)

### Most positively-biased (≥ 20 paragraphs)

| CELEX | Title | Year | Score |
|-------|-------|------|-------|
| `31993D0606` | Commission Decision — approved fishery establishments (Canada) | 1993 | +0.836 |
| `32019D1579` | Commission Implementing Decision — GMO authorisations (Monsanto/Bayer) | 2019 | +0.809 |
| `32021D0184` | Commission Implementing Decision — GMO authorisations (Bayer/Monsanto) | 2021 | +0.772 |
| `31984L0167` | Council Directive — less-favoured farming areas, Italy | 1984 | +0.768 |
| `32019R0221` | Commission Implementing Regulation — feed additive authorisations (phytase, xylanase, protease) | 2019 | +0.768 |
| `32005D0813` | Commission Decision — approved fishery establishments | 2005 | +0.761 |
| `32013D0155` | Commission Implementing Decision — EU aid to reference laboratories | 2013 | +0.748 |
| `32004D0850` | Commission Decision — approved fishery establishments | 2004 | +0.740 |
| `32008D0427` | Commission Decision — approved fishery establishments | 2008 | +0.731 |
| `32013D0451` | Commission Decision — Daimler engine encapsulation as CO₂ innovation | 2013 | +0.730 |

### Most negatively-biased (≥ 20 paragraphs)

| CELEX | Title | Year | Score |
|-------|-------|------|-------|
| `32017D0994` | Council Decision — North Korea (DPRK) restrictive measures | 2017 | −0.896 |
| `32014R0810` | Council Implementing Regulation — Ukraine/Russia sanctions | 2014 | −0.893 |
| `32011D0069` | Council Decision — Belarus officials, restrictive measures | 2011 | −0.891 |
| `32022R0408` | Council Implementing Regulation — Ukraine/Russia sanctions (Mar 2022) | 2022 | −0.891 |
| `32020R0398` | Council Implementing Regulation — Ukraine/Russia sanctions (Mar 2020) | 2020 | −0.891 |
| `32025R0631` | Council Implementing Regulation — Belarus sanctions (Mar 2025) | 2025 | −0.890 |
| `32025R0042` | Council Implementing Regulation — Venezuela sanctions (Jan 2025) | 2025 | −0.890 |
| `32014R0081` | Council Implementing Regulation — Tunisia sanctions | 2014 | −0.888 |
| `32014D0049` | Council Decision — Tunisia sanctions | 2013 | −0.888 |
| `32025R0958` | Council Implementing Regulation — Russia sanctions (May 2025) | 2025 | −0.888 |

**Positive pattern:** Feed additive and GMO authorisations naming specific products and their patent holders, approved establishment lists, company-specific state aid decisions.

**Negative pattern:** Sanctions lists — Ukraine/Russia, North Korea, Belarus, Venezuela, Tunisia. These are designed to target specific persons; the high negative score is expected and appropriate.

**Note on document types:** CFSP Decisions appear alongside Implementing Regulations because they provide the legal basis for the named-person annexes that drive the score. The pipeline includes them for this reason.

---

## 6 · What High-Scoring Paragraphs Look Like

### Benefiting specific groups

> **+1.00** · 32025H03971 · `recital-6` · *Poland-endorsement*
> "The Council recommendation of 21 January 2025 endorsed the net expenditure path of Poland…"

> **+1.00** · 32025H03971 · `recital-15` · *Poland-exemption*
> "Poland is allowed to deviate from and exceed the maximum growth rates of net expenditure to the extent that the net expenditure in excess of these maximum growth rates is not more than the increase in defence expenditure…"

> **+1.00** · 31992S1775 · `art-2-4` · *Asil Çelik exemption*
> "Notwithstanding paragraph 2, the duty shall not apply for the products concerned manufactured by Asil Celik Sanayl Ve Ticaret AS, Istanbul, Turkey (Taric additional code: 8671)."

### Burdening specific groups

> **−1.00** · 32009E0351 · `art-4-4-1` · *Myanmar sanctions list*
> "A. STATE PEACE AND DEVELOPMENT COUNCIL (SPDC) — Name / aliases / identifying information / function / date and place of birth / passport number … A1a Senior General…"

> **−1.00** · 32009E0351 · `art-4-4-2` · *Myanmar sanctions list*
> "B1a Brig-Gen Win Myint, Rangoon (Yangon) M · B1b Kyin Myaing, Wife of Brig-Gen Win Myint F…"

> **Note:** High negative scores are not inherently problematic. Sanctions against authoritarian regimes are designed to be targeted — the AI correctly identifies them as such. Whether the targeting is justified is a policy question, not a scoring one.

---

## 7 · Key Observations

### Feed Additives & GMO Cluster (2019–2021)
**Regulation 2019/221** (282 paragraphs, mean +0.77) amends authorisations for 6-phytase from *Bacillus amyloliquefaciens* (PTA-6507), endo-1,4-beta-xylanase, and protease — each tied to a specific patent holder and TARIC code. Decisions **2019/1579** and **2021/184** list Monsanto/Bayer GMO crop events by proprietary name. The question is whether these authorisations were competitively tendered and whether equivalent products from competing companies receive equivalent treatment.

### Sanctions Inflation Post-2022

| Year | Paragraphs scoring ≤ −0.4 |
|------|---------------------------|
| 2019 | ~15,000 |
| 2020 | ~38,000 (+153%) |
| 2022 | ~54,000 |
| 2024 | ~55,000 |

Each Russia/Ukraine sanctions update adds hundreds of named persons. This single mechanism explains most of the post-2019 negative drift in the mean score.

### Recitals Score Higher Than Articles
Recitals name specific beneficiaries, products, and companies — articles must be worded broadly to be enforceable. High recital scores often reflect legitimate specificity in the reasoning behind a rule, not bias in the operative text.

### What the AI Cannot See
Bias embedded in vague language ("sufficient flexibility for operators") scores near zero. So do numeric thresholds that only large incumbents can meet in practice. The AI reliably flags explicit named beneficiaries — structural bias hidden in technical specifications is largely invisible to it.

---

## 8 · Limitations

- **Not measured:** whether a provision is good policy, legally valid, lobbying-driven, or competitively tendered.
- **False positives:** Country-specific statistical corrections, individual product safety certificates, and other procedurally required named references all score high — even when the naming is routine.
- **False negatives:** Vague incumbent-friendly clauses, high minimum thresholds, and broad exemptions claimed only by a few operators score near zero.
- **Model:** GPT-5-mini reliably flags explicit named exemptions; subtle structural biases in technical thresholds are outside its detection range.

---

*May 2026 · GPT-5-mini · EUR-Lex Cellar API → paragraph extraction → LLM scoring → aggregation · ~350M tokens*

**License:** Freely usable for any purpose. Any publication must credit:
> *Analysis by Petr Salomoun · [petr.salomoun@gmail.com](mailto:petr.salomoun@gmail.com)*
