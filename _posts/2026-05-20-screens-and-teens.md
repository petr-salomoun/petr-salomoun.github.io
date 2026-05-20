---
author: Petr Salomoun
categories:
- education
- public-health
date: 2026-05-20 00:00:00+00:00
excerpt: "700,000 observations across 80 countries and 20 years reveal that screen time's effect on youth is far more nuanced than the headlines suggest — and that uniform bans could hurt the kids who need help most."
github_repo: petr-salomoun/screens-and-teens
layout: post
tags:
- screen-time
- youth
- education
- mental-health
- PISA
- data-analysis
- social-media
title: 'Screens and Teens: What 700,000 Students Across 80 Countries Actually Tell Us'
updated_at: '2026-05-20T00:00:00+00:00'
---

# Shall We Ban Gaming or Social Media?

*An analysis of screen time effects on academic performance and mental health using PISA (690,000 students, 80 countries, 2003–2022) and YRBSS (15,203 US high schoolers, 2023)*

---

## The Data

Two massive public datasets underpin this analysis:

| Dataset | What It Measures | Sample | Countries | Years |
|---------|-----------------|--------|-----------|-------|
| **PISA** | Academic performance (Math, Science, Reading) + screen activities | 690,000 | 80 | 2003–2022 |
| **YRBSS** | Mental health, social media use, cyberbullying | 15,203 | USA | 2023 |

**Total: ~700,000 observations across 80 countries spanning 20 years**

---

## Part I: Smartphones Kill Education — But Not in the Way You Think

### Math Is Not the Victim

Everyone blames smartphones for the PISA math score decline. But **math was already declining before smartphones**. The real smoking gun is Science and Reading:

| Period | Math Rate | Reading Rate | Science Rate |
|--------|-----------|--------------|--------------|
| Pre-2012 | −0.67 pts/year | **+0.33 pts/year** | **+0.17 pts/year** |
| 2012–2018 | −0.83 pts/year | **−1.50 pts/year** | **−2.00 pts/year** |

**Both Science AND Reading reversed from improvement to decline** exactly when smartphones reached mass adoption (2012: ~45% penetration). Math just accelerated an existing decline.

![Domain Comparison](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/fresh_discovery/fig1_domain_comparison.png)

### The Science Inflection Point

![Science Inflection](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/deep_dive/fig1_science_inflection.png)

The inflection at 2012 coincides with both smartphone mass adoption and the rise of Instagram and other social media platforms (launched 2010–2012). PISA's 3-year intervals cannot separate these effects.

![Technology Timeline](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/todo_fixes/fig_instagram_vs_smartphone_timeline.png)

---

## Part II: SES — The Elephant in the Room

Before any screen effect analysis, one number dominates everything:

**Socioeconomic status explains 2–5× more variance than any screen activity.**

| Predictor | Math β | Reading β | Science β |
|-----------|--------|-----------|-----------|
| **SES** | **0.340** | **0.313** | **0.326** |
| Gaming | +0.036 | +0.022 | +0.049 |
| Social Media | −0.071 | −0.029 | −0.064 |
| Video | −0.161 | −0.156 | −0.169 |
| News | −0.230 | −0.239 | −0.234 |

The SES quintile gap is **94 math points** — from poorest to richest. The largest screen effect (News β = −0.17) is half the SES effect. Without controlling for SES, all screen time research is confounded.

![SES as Dominant Confounder](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_ses_dominant.png)

A small group of students (2.6%) reports zero use of ALL leisure screen activities. These are severely deprived — mean SES of −0.87, scoring 90 points below peers. Their inclusion in "zero screen use" groups conflates deprivation with choice. **All dose analyses use access-only students** (N = 61,055).

### Cultural Clusters Beyond SES

East Asian countries score 90 points above what their SES predicts; Latin American countries score 22 below — reflecting educational system quality and cultural factors that SES cannot capture.

![SES by Region](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round4/fig_ses_by_region.png)

### Screen Harm Scales with Wealth

The opportunity cost of screen time is higher for wealthy students. For Q1 students, gaming shows a *positive* effect (+0.18) and SM is neutral. For Q4, every activity is negative, with video (−0.24) and SM (−0.16) hitting hardest. This pattern is consistent across Math, Reading, and Science.

![Q1 vs Q4 Effects](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_q1_vs_q4.png)

### Activity Usage by Sex × SES

Sex drives activity choice more than SES does. Boys game more across all SES levels (Δ ≈ 0.5–0.7 hrs/day), while girls use more social media and video. SES differences within sex are small (Δ < 0.2 hrs/day), and cross-country variation is modest, suggesting these patterns are universal.

![Screen Activity Usage by Sex × SES](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_usage_sex_ses.png)

Here is how screen activity types correlate with PISA results separately for sexes after adjusting for SES:

![Activity Effects by Sex](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_effects_by_sex.png)

*SES-adjusted standardized effects (β) of each activity on outcomes, separately for males and females. Green = positive effect, Red = negative effect.*

---

## Part III: The Paradox — Does Studying Make You Stupid?

Raw data show students who spend more time on homework score *worse*. Email (β=−0.25) and News (β=−0.22) show similar patterns. The resolution: **Email and Homework** correlate at r=0.63 and capture the same thing — struggling students doing more schoolwork (reverse causation). **Both are excluded from further leisure analysis.**

![Homework Paradox](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/confounder_revision/fig3_homework_paradox.png)

**News is different** — it retains a strong independent effect (β=−0.154) even after controlling for all other activities. It represents genuine harmful leisure consumption, not reverse causation.

---

## Part IV: Every Activity Has an Optimal Dose

Across all five leisure screen activities, we find dose-response curves ranging from inverted-U (clear optimum at moderate use) to monotonically declining (optimum at zero). The optimal dose varies dramatically by **sex** and **SES**.

![Deviation from Subgroup Optimum](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_deviation_5act_ses_sex.png)

*Blue=Boys, Red=Girls. Solid=Q1 (poor), Dashed=Q4 (rich).*

### Summary: The Optimum Shifts with Wealth and Sex

*Zero-use penalties in parentheses (access-only sample, N=61,055)*

| Activity | Poor Boys Optimum | Rich Boys Optimum | Poor Girls Optimum | Rich Girls Optimum |
|----------|-------------------|-------------------|--------------------|--------------------|
| **Gaming** | **2–4h** (−63) | 1–2h (−26) | 2–4h (−25) | **Never** (0) |
| **Social Media** | 1–2h (−20) | **Never** (0) | 1–2h (−40) | **Never** (0) |
| **Video** | Never (0) | **Never** (0) | 1–2h (−11) | **Never** (0) |
| **Browsing** | 1–2h (−25) | 30–60m (−7) | 1–2h (−32) | 1–2h (−14) |
| **News** | **Never** (0) | **Never** (0) | **Never** (0) | **Never** (0) |
| **Total** | 2–4h | 1–2h | 2–4h | 1–2h |

The pattern is consistent: **the optimum shifts left (toward less use) for wealthier students.** A uniform screen time cap at low levels helps rich students but **hurts poor ones** — poor students' optima are at 1–2h or 2–4h depending on activity.

### Why Zero Screen Time Helps Rich and Hurts Poor Students?

Rich students' screen time displaces beneficial activities (reading, enrichment) — higher opportunity cost. Poor students have less to displace. Gaming provides cognitive benefits (spatial reasoning), SM reduces social exclusion. Video and news have no compensatory benefit.

![Displacement Hypothesis](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_displacement.png)

| Activity | Q1 Zero-Use Penalty | Q4 Zero-Use Penalty |
|----------|---------------------|---------------------|
| **Gaming** | **−63 pts** | −5 pts |
| **SM** | **−20 pts** | 0 pts |
| **Browsing** | **−25 pts** | −7 pts |
| **Video** | 0 pts | 0 pts |
| **News** | 0 pts | 0 pts |

### Beyond Academics — Wellbeing and Belonging Optima Diverge

**What's best for grades is not always what's best for happiness or social belonging.** Girls are less affected academically but disproportionately harmed in wellbeing.

![Dose-Response by Sex × SES (5 Activities × 3 Outcomes)](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_dose_response_sex_ses.png)

| Activity | Academic Optimum | Life Satisfaction Optimum | Belonging Optimum | Aligned? |
|----------|-----------------|--------------------------|-------------------|----------|
| **Gaming** | 2–4h | 30–60m | Never/<30m | NO |
| **Social Media** | 1–2h | 30–60m | 2–4h | NO |
| **Video** | Never/<30m | 30–60m | 1–2h | NO |
| **Browsing** | 1–2h | 30–60m | 30–60m | Partial |

The most striking divergence: SM's academic optimum is low use, but belonging optimum is moderate-to-high. SM serves a real social function even as it hurts grades.

### Optimal Activity Combination by Subgroup

Activities interact — the optimal level of one depends on others. A grid search across 625 combinations finds:

| Group | Gaming | Social Media | Browsing | Video |
|-------|--------|--------------|----------|-------|
| **Poor Boys** | **2–4h** | 1–2h | 1–2h | 30–60m |
| **Rich Boys** | 1–2h | 1–2h | 30–60m | **Never** |
| **Poor Girls** | 2–4h | 1–2h | 1–2h | 1–2h |
| **Rich Girls** | **Never** | 1–2h | 1–2h | 30–60m |

SM at 1–2h is the only universal optimum across all subgroups. Video is the clearest "reduce" signal.

---

## Part V: Gaming — The Most Beneficial

Gaming shows the clearest positive effect for most groups, stronger for boys, and far more beneficial for poor than rich students.

![Gaming Corrected for Poverty](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_gaming_corrected.png)

| SES Level | Males | Females |
|-----------|-------|---------|
| **Low SES** | β = **+13.9** | β = +6.1 |
| Mid SES | β = +4.8 | β = −1.5 |
| **High SES** | β = +1.2 (n.s.) | β = **−6.3** |

For poor boys, **not gaming at all** is more harmful than heavy gaming (−63 vs −8 points). The widest subgroup divergence of any activity.

### Gaming Subgroup Profiles

- **Male non-gamers** (N~1,079 in Q1): Lowest SES (−0.23), lowest Math (389), highest video consumption — toxic activity mix: deprived of beneficial activity, compensating with the most harmful
- **Male heavy gamers** (4h+): Lower SES than moderate gamers, higher SM and video use — heavy gaming is part of a general high-consumption pattern
- **Female non-gamers** dominate (74% of non-gamers are female) — gender preference or social stigma, not access limitation

### The Gaming Stigma Effect on Girls

Gaming improves girls' academics but consistently hurts their belonging and life satisfaction — a pattern consistent with social stigma rather than the activity itself being harmful.

![Gaming Stigma](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round8/fig_gaming_stigma.png)

Rich girls who game at moderate levels lose **0.23 belonging points** while gaining only modestly in academics. By contrast, rich boys who game at the same level *gain* belonging (+0.36). Girls avoid gaming and shift to SM and video — activities that hurt their outcomes more. De-stigmatizing gaming for girls could yield academic gains without the belonging penalty.

---

## Part VI: Video and News — The Clearest Harms

### Video Is 1.8× More Harmful Than Social Media

| Activity | Math β |
|----------|--------|
| **News** | −0.174 |
| **Video** | −0.143 |
| **Social Media** | −0.081 |

Video (β = −0.143) vs Social Media (β = −0.081): **Video is 1.8× more harmful**. The optimal dose for video is zero or near-zero for nearly all subgroups. Prolonged passive consumption where the brain "switches off".

![Video Dose Response](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_video_dose_response.png)

### News — The Most Harmful and Least Suspected

News is **universally harmful** with no beneficial dose for any subgroup. The optimum is "Never" across all groups:

| Subgroup | Penalty at 1–2h | Penalty at 4h+ |
|----------|-----------------|-----------------|
| Poor Boys | −31 pts | −75 pts |
| Rich Boys | −23 pts | −80 pts |
| Poor Girls | −15 pts | −55 pts |
| Rich Girls | −18 pts | −73 pts |

Among 15-year-olds, "reading the news" means scrolling algorithmically-curated content feeds. Despite being the least-consumed activity (60% never or rarely use it), News has the strongest negative effect of any screen activity. Heavy news consumers are not information seekers — they are general over-consumers of everything, a profile suggesting compulsive scrolling behavior.

![News Dose Response](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_news_dose_response.png)

---

## Part VII: Social Media — Boys vs Girls

SM's effect is not a single number. It varies dramatically by both sex and SES:

![SM Stratified Effects](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_sm_stratified.png)

| Group | SM → Math (β) | SM → Life Satisfaction (β) | SM → Belonging (β) |
|-------|---------------|---------------------------|---------------------|
| **Poor Boys (Q1)** | −0.015 (n.s.) | **+0.040** | **+0.062** |
| Rich Boys (Q4) | **−0.183** | +0.010 (n.s.) | +0.039 |
| **Poor Girls (Q1)** | −0.019 (n.s.) | **−0.053** | +0.033 |
| Rich Girls (Q4) | **−0.133** | **−0.052** | +0.033 |

Key patterns:
- **Academic harm scales with wealth**: SM is essentially harmless for Q1 students but strongly negative for Q4
- **Wellbeing effects are sex-dependent**: Boys show positive SM → life satisfaction; girls show negative effects
- **Belonging is universally positive**: SM → school belonging is mildly positive for all subgroups

| Sex | SM → Life Satisfaction (β) |
|-----|---------------------------|
| Males | **+0.031** (positive) |
| Females | **−0.064** (negative) |

---

## Part VIII: Mental Health — YRBSS Data

For health outcomes, we turn to the YRBSS 2023 (N=15,203 US high school students). Every health outcome worsens with SM frequency:

| Outcome | Non-Users | Constant Users | Difference |
|---------|-----------|----------------|------------|
| Poor mental health | 15% | 24% | +9 pp |
| Sad/hopeless 2+ weeks | 31% | 41% | +10 pp |
| Considered suicide | 19% | 23% | +4 pp |
| Cyberbullied | 31% | 41% | +10 pp |
| Current alcohol | 9% | 27% | +18 pp |

![YRBSS Health Outcomes](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_yrbss_health_outcomes.png)

### Girls Are Hit Harder

![Sex Differences in SM Health Effects](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_yrbss_sex_differences.png)

| Outcome | Boys (None→Constant) | Girls (None→Constant) |
|---------|----------------------|-----------------------|
| Poor mental health | 11% → 18% | 21% → 35% |
| Considered suicide | 13% → 17% | 29% → 31% |
| Cyberbullied | 23% → 29% | 45% → 61% |

Girls have higher baselines and steeper gradients. 61% of girls using SM constantly report being cyberbullied vs 29% of boys.

### The Vulnerability Multiplier

SM's mental health effect is almost entirely concentrated among already-vulnerable youth:

| ACE Level | Poor MH at Low SM | Poor MH at High SM | SM Gradient |
|-----------|-------------------|---------------------|-------------|
| 0 ACEs (N=12,007) | 7% | 10% | **+3 pp** |
| 1 ACE (N=3,108) | 24% | 31% | +7 pp |
| 2+ ACEs (N=4,988) | 34% | 51% | **+17 pp** |

For healthy students (0 ACEs), SM barely matters (+3pp). For traumatized students (2+ ACEs), SM amplifies vulnerability by +17pp. **SM amplifies pre-existing vulnerabilities rather than causing problems in healthy teens.**

![SM × Adverse Childhood Experiences](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_yrbss_ace_interaction.png)

---

## Part IX: Cyberbullying — The Real Hit

Out of 15,203 US high school students surveyed, **4 in 10 (41%)** reported being cyberbullied. After adjusting for sex, age, LGBQ status, adverse childhood experiences, and sleep:

| Predictor | Prevalence (Not Bullied) | Prevalence (Bullied) | Risk Multiplier |
|-----------|--------------------------|----------------------|-----------------|
| Poor Mental Health | ~12% | ~47% | **4.0×** |
| Considered Suicide | ~5% | ~38% | **7.6×** |

**The cyberbullying effect (35 pp difference) is 7× larger than the difference between low and heavy SM use (15 pp).** PAF = 59% — an estimated 59% of all poor mental health cases involve cyberbullying.

Targeting cyberbullying directly would be far more effective than limiting screen time.

![Cyberbullying Impact](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/todo_fixes/fig_cyberbullying_impact.png)

---

## What This Means: Policy Implications

### Do:
1. **Target video streaming and news scrolling** — clearest displacement effects; news universally harmful (β=−0.17, optimal = never for all groups)
2. **Address cyberbullying** — the dominant mechanism (7× larger effect than SM intensity, PAF = 59%)
3. **Set SES-differentiated guidelines** — poor students need 1–2h+ for optimal outcomes; rich students should stay below 1h for most activities
4. **Encourage activity substitution** — switching from video to gaming yields +0.28 β for poor boys, no reduction in total screen time needed

### Don't:
1. **Ban all screen time** — zero use costs poor boys up to 63 Math points (gaming) or 40 points (SM for poor girls)
2. **Treat all activities equally** — video is 1.8× worse than social media; gaming has positive effects for disadvantaged boys
3. **Apply uniform screen time limits** — a one-size cap helps rich students and hurts poor ones
4. **Ignore SES in research** — SES effects are 2–5× larger than screen effects; without controlling for it, all screen time research is confounded

### Activity Substitution Guide

| Subgroup | Activity Ranking (best → worst) | Best Switch | Academic β Gain |
|----------|----------------------------------|-------------|-----------------|
| **Poor Boys** | Gaming > Browsing > SM > News > Video | Video → Gaming | **+0.28** |
| **Rich Boys** | Gaming > Browsing > SM > News > Video | SM → Gaming | +0.19 |
| **Poor Girls** | Gaming > Browsing > SM > News > Video | Video → Gaming | +0.22 |
| **Rich Girls** | Browsing > Gaming > SM > Video > News | Video → Browsing | +0.17 |

A poor boy switching 1 hour of passive video to gaming gains the equivalent of **~25 Math points** — without any reduction in total screen time.

---

## Personalized Recommendations

**Universal rules (all subgroups):**
- **Never allow news scrolling** — universally harmful (β=−0.17), no beneficial dose for any group
- **Minimize video streaming** — strongest displacement effect, optimal is zero or near-zero for all groups
- **Prioritize cyberbullying prevention** over any time limit

The recommendations below are *per-activity caps within a total daily budget*:

#### Poor Families with Boys
**Total ~4h/day: Gaming ≤2–4h | SM ≤1–2h | Browsing ≤1–2h | Video <30min | News: never**
- Gaming is their strongest positive — zero gaming costs 63 pts
- If total must be reduced, cut video first

#### Poor Families with Girls
**Total ~4h/day: Gaming ≤2–4h | SM ≤1–2h | Browsing ≤1–2h | Video <1h | News: never**
- Gaming helps academics but hurts belonging — tradeoff
- SM hurts girls' satisfaction even when academic effects are neutral — monitor mood

#### Wealthy Families with Boys
**Total ~2–3h/day: Gaming ≤1–2h | SM ≤1–2h | Browsing ≤30–60min | Video: none | News: never**
- Eliminate video — rich boys score best with zero
- SM at 1–2h balances belonging against academic cost

#### Wealthy Families with Girls
**Total ~2–3h/day: Gaming: none | SM ≤1–2h | Browsing ≤1–2h | Video <30min | News: never**
- Most restricted subgroup — but not zero across the board
- SM at 1–2h still optimal (universal finding)
- Priority: content quality and cyberbullying prevention over time limits

---

## Limitations

1. **Cross-sectional design** — causation uncertain
2. **Self-reported screen time** — measurement error
3. **YRBSS lacks SES control** — mental health findings have caveat
4. **Activity categories broad** — "gaming" includes many types
5. **Instagram/smartphone separation impossible** — events clustered 2010–2012
6. **COVID contaminates 2020+ data** — cannot separate screen effects from pandemic effects

---

*Analysis: PISA 2022, YRBSS 2023. Total observations: ~700,000 across 80 countries. Corrected for poverty confounding, sex interactions, and activity substitution.*
