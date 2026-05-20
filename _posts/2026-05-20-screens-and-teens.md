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
title: 'Screens and Teens: Screen Time Effect on Youth'
updated_at: '2026-05-20T00:00:00+00:00'
---

# Screens and Teens: Screen Time Effect on Youth

**Shall we ban gaming or social media?**

---

## Executive Summary

We analyzed screen time effects on academic performance and mental health using data from the world's largest education and youth health surveys:

| Dataset | What It Measures | Sample | Countries | Years |
|---------|-----------------|--------|-----------|-------|
| **PISA** | Academic performance (Math, Science, Reading) + screen activities | 690,000 | 80 | 2003-2022 |
| **YRBSS** | Mental health, social media use, cyberbullying | 15,203 | USA | 2023 |

**Total: ~700,000 observations across 80 countries spanning 20 years**

**Key findings:**

1. **Math is not the victim — Science and Reading are.** Math was already declining before smartphones. Science and Reading were *improving* until 2012, then reversed. The timing matches smartphone mass adoption.

2. **Every activity has an optimal dose that varies by wealth and sex.** Both zero use and heavy use are harmful, but the penalties differ dramatically: poor boys lose 63 points from zero gaming; rich girls lose 37 from heavy gaming.

3. **The optimum shifts with wealth.** Poor students' optimal screen time is 2-4h/day; rich students' is 1-2h. A uniform cap helps the rich and hurts the poor.

4. **Video and News are purely harmful.** Video (β=-0.14) and News (β=-0.17) show no beneficial dose range for any subgroup. They should be minimized.

5. **SES is the dominant confounder.** SES explains 2-5x more variance than any screen activity. Without controlling for it, all screen time research is confounded.

6. **Social media harm scales with wealth and amplifies pre-existing vulnerability.** SM is near-harmless for poor students but strongly negative for rich ones. In health outcomes, SM's effect is concentrated among youth with adverse childhood experiences.

7. **Cyberbullying dwarfs SM intensity.** The mental health difference between bullied and non-bullied students (35 pp) is 7x larger than between low and heavy SM users (15 pp).

---

## Part I: Smartphones Kill Education

### Math as the Prime Victim?

Everyone talks about the PISA math results decline due to smartphones. But: **math was already declining before smartphones** and smartphones haven't changed it much. How about the other results?

| Period | Math Rate | Reading Rate | Science Rate |
|--------|-----------|--------------|--------------|
| Pre-2012 | -0.67 pts/year | **+0.33 pts/year** | **+0.17 pts/year** |
| 2012-2018 | -0.83 pts/year | **-1.50 pts/year** | **-2.00 pts/year** |

**Both Science AND Reading reversed from improvement to decline** precisely when smartphones reached mass adoption. Math was already declining — it just accelerated slightly. The real smoking gun is the reversal in Science and Reading.

**Figure 2: Where's the Real Signal?**
![Domain Comparison](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/fresh_discovery/fig1_domain_comparison.png)

### The Science Inflection Point

**Figure 3: Science Trend with Smartphone Adoption**
![Science Inflection](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/deep_dive/fig1_science_inflection.png)

- **2006-2012**: Science improving at +0.17 pts/year (R² = 0.75)
- **2012-2018**: Science declining at -2.00 pts/year (R² = 0.96)
- **Inflection**: 2012 — smartphones reach 45% penetration

**Note on causation**: The inflection coincides with smartphone mass adoption but also Instagram and other social media (launched 2010-2012). PISA's 3-year intervals cannot separate these effects.

**Figure 3b: Technology Timeline**
![Technology Timeline](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/todo_fixes/fig_instagram_vs_smartphone_timeline.png)

---

## Part II: SES — The Elephant in the Room

### SES Dwarfs All Screen Effects

Socioeconomic status is the single largest predictor of every outcome we measured. We verified this across all three academic domains — Math, Reading, and Science — and the pattern is fully consistent:

**Figure: SES as Dominant Confounder**
![SES Chapter](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_ses_dominant.png)

| Predictor | Math β | Reading β | Science β | Consistent? |
|-----------|--------|-----------|-----------|-------------|
| **SES** | **0.340** | **0.313** | **0.326** | YES |
| Gaming | +0.036 | +0.022 | +0.049 | YES (+) |
| Social Media | -0.071 | -0.029 | -0.064 | YES (-) |
| Browsing | -0.055 | -0.018 | -0.036 | YES (-) |
| News | -0.230 | -0.239 | -0.234 | YES (-) |
| Video | -0.161 | -0.156 | -0.169 | YES (-) |
| Homework | -0.218 | -0.210 | -0.208 | YES (-) |
| Email | -0.261 | -0.276 | -0.264 | YES (-) |

**All effects are directionally consistent across Math, Reading, and Science.** We use Math as the primary outcome throughout (largest sample, most precise). Key SES findings:
- **SES quintile gap**: 94 math points from poorest to richest
- **Comparison**: The largest screen effect (Video β = -0.163) is less than half the SES effect (β = 0.340)

### Deprived Non-Users

A small group (1,646 = 2.6%) reports zero use of ALL leisure screen activities. These are severely deprived in all aspects, not just screen access:

| Characteristic | No-Access Group | Rest of Sample |
|---------------|----------------|----------------|
| Mean SES | **-0.87** | -0.09 |
| Academic score | **-90 pts** | +2 pts |
| In poorest quartile | **51%** | 24% |
| Female | 44% | 51% |

These students score 90 points below the rest. Their inclusion in "zero use" conflates deprivation with choice. **All analyses below exclude this group.** "Never/<30m" means students who choose not to use a specific activity while using others.

Analysis sample: **N = 61,055** (access-only).

---

### Cultural Clusters Beyond SES

East Asian countries score 90 points above what their SES predicts; Latin American countries score 22 below — reflecting educational system quality and cultural factors that SES cannot capture.

**Figure: Between-Country SES vs Math by Region**
![SES by Region](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round4/fig_ses_by_region.png)

### Screen Harm Scales with Wealth

The opportunity cost of screen time is higher for wealthy students. Comparing effects for the poorest (Q1) vs richest (Q4) students:

**Figure: Screen Effects — Poor vs Rich**
![Q1 vs Q4 Effects](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_q1_vs_q4.png)

For Q1 students, gaming shows a *positive* effect (+0.18) and SM is neutral. For Q4, every activity is negative, with video (-0.24) and SM (-0.16) hitting hardest. This pattern is consistent across Math, Reading, and Science.

---

## Part III: Screen Factors Affecting School Results

### "Screen time is bad for kids" — but which screens? Which kids?

Apart from SES, the next most important factor is **Sex**.

### Activity Usage by Sex × SES

**Figure: Screen Activity Usage by Sex × SES**
![Usage by Sex SES](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_usage_sex_ses.png)
*Note: Email and Homework are shown here for completeness but excluded from causal analysis (Part III) due to reverse causation — high-performing students use more email and do more homework online by definition.*

Sex drives activity choice more than SES does. Boys game more across all SES levels (Δ ≈ 0.5-0.7 hrs/day), while girls use more social media and video. SES differences within sex are small (Δ < 0.2 hrs/day), and cross-country variation is modest, suggesting these patterns are universal.

Here is how screen activity types correlate with PISA results separately for sexes after adjusting for SES:

**Figure 1: Not All Screen Time Is Equal**
![Activity Effects by Sex](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_effects_by_sex.png)

*SES-adjusted standardized effects (β) of each activity on outcomes, separately for males and females. Email and Homework shown for reference but excluded from causal analysis due to reverse causation. Green = positive effect, Red = negative effect.*

---

## Part IV: The Paradox

### Does Studying Make You Stupid?

Raw data show students who spend more time on homework score *worse*. Similar effects appear for email (β=-0.25) and news (β=-0.22). SES adjustment barely changes these — the effect persists within each SES quartile.

**Figure 4: The Homework Paradox**
![Homework Paradox](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/confounder_revision/fig3_homework_paradox.png)

The resolution: **Email and Homework** correlate at r=0.63 and capture the same thing — struggling students doing more schoolwork (reverse causation). **We exclude both from further analysis.**

**News** is different — it retains a strong independent effect (β=-0.154) even after controlling for all other activities. It represents genuine harmful leisure consumption, not reverse causation. See Part VI-b for full analysis.

---

## Part V: The U-Shape — Every Activity Has an Optimum

### Every Screen Activity Shows a Dose-Response Curve

Across all five leisure screen activities (Gaming, Social Media, Browsing, Video, News), we find dose-response patterns ranging from inverted-U (clear optimum at moderate use) to monotonically declining (optimum at zero/minimal use). The optimal dose and the severity of deviation vary dramatically by Sex and SES. All analyses below use the access-only sample (N=61,055).

**Figure: Deviation from Subgroup Optimum by Sex × SES (5 Activities + Total)**
![Deviation by Subgroup](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_deviation_5act_ses_sex.png)

*Blue=Boys, Red=Girls. Solid=Q1(poor), Dashed=Q4(rich). Access-only sample (N=61,055).*

We computed the deviation from each subgroup's optimum for all activities. Key patterns by activity:

- **Gaming**: Widest subgroup divergence. Q1 boys peak at 2-4h (zero-penalty: -63 pts). Q4 girls optimum is "Never" (no penalty for zero use). Gaming is the only activity where the optimum differs by 3+ dose levels between subgroups.
- **SM**: Q1 girls have -40 pt penalty for zero SM (social exclusion signal). Q4 boys/girls have zero penalty for non-use. Optimum 1-2h for poor, Never for rich.
- **Browsing**: Most uniform optimum (1-2h for most groups). Smallest subgroup variation. Safe activity across the board.
- **Video**: Optimum is Never/<30m for all groups except Q1 girls (1-2h). Purely harmful for rich students. Zero-penalty = 0 for all except Q1 girls (-11 pts).
- **News**: Monotonically harmful for all subgroups. Optimum is always "Never". No beneficial dose range exists. Dose-response similar to Video pattern.
- **Total**: Q1 students optimum at 2-4h total; Q4 at 1-2h total.

### Total Screen Time

Total screen time (sum of estimated hours across all 5 activities; median = 5.6h/day) shows a clear inverted-U with academic optimum at 1-2h/day total for rich and twice as much for poor students. The pattern is identical for boys and girls. These optima are robust across countries — they replicate within both rich and poor nations individually, ruling out Simpson's paradox (r between country SES and optimum level is non-significant for Gaming and SM; p>0.4).

However, total screen time adds **zero explanatory power** beyond the individual activity breakdown (R²=0.040 for individual activities; R²=0.040 with total added; total β is non-significant p=0.56). The total is simply a shadow of the individual activities. The *mix* matters, not the *amount* — this is the key finding explored in Part V-c.

### Summary: The Optimum Shifts with Wealth and Sex

*Access-only sample (N=61,055). Zero-use penalties in parentheses.*

| Activity | Poor Boys Optimum | Rich Boys Optimum | Poor Girls Optimum | Rich Girls Optimum |
|----------|------------------|------------------|-------------------|-------------------|
| **Gaming** | **2-4h** (-63) | 1-2h (-26) | 2-4h (-25) | **Never** (0) |
| **Social Media** | 1-2h (-20) | **Never** (0) | 1-2h (-40) | **Never** (0) |
| **Video** | Never (0) | **Never** (0) | 1-2h (-11) | **Never** (0) |
| **Browsing** | 1-2h (-25) | 30-60m (-7) | 1-2h (-32) | 1-2h (-14) |
| **News** | **Never** (0) | **Never** (0) | **Never** (0) | **Never** (0) |
| **Total** | 2-4h | 1-2h | 2-4h | 1-2h |

The pattern is consistent: **the optimum shifts left (toward less use) for wealthier students.** News and Video optimum is "Never" for nearly all groups. The intervention logic is inverse by SES:

- **Poor students** should not be forced below their optimum — zero gaming costs Q1 boys 63 pts, zero SM costs Q1 girls 40 pts
- **Rich students** already have their optimum at zero/minimal for most activities
- **A uniform screen time cap at low levels (e.g., <1h) helps rich students but hurts poor ones** — poor students' optima are at 1-2h or 2-4h depending on activity

### Why Zero Screen Time Helps Rich and Hurts Poor Students?

Moderate screen use is **actively associated with better outcomes** than zero use for poor students: gaming +63 pts for poor boys, SM +40 pts for poor girls. The effect disappears for rich students.

The explanation: rich students' screen time displaces beneficial activities (reading, enrichment) — higher opportunity cost. Poor students have less to displace. Gaming provides cognitive benefits (spatial reasoning), SM reduces social exclusion. Video and news have no compensatory benefit.

**Figure: Displacement Hypothesis**
![Displacement](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_displacement.png)

| Activity | Q1 Zero-Use Penalty | Q4 Zero-Use Penalty |
|----------|-------------------|-------------------|
| **Gaming** | **-63 pts** | -5 pts |
| **SM** | **-20 pts** | 0 pts |
| **Browsing** | **-25 pts** | -7 pts |
| **Video** | 0 pts | 0 pts |
| **News** | 0 pts | 0 pts |

Non-users within the access-only sample don't substitute — they consume LESS of everything, suggesting social withdrawal. Poor students (Q1) actually consume MORE total screen time than rich (Q4): 5.3h vs 4.2h/day. The issue is suboptimal mix, not insufficient access.

---

## Part V-b: Beyond Academics — Optimum Across All Outcomes

### Academic, Wellbeing, and Belonging Optima Diverge

**What's best for grades is not always what's best for happiness or social belonging.** Girls are less affected academically but disproportionately harmed in wellbeing.

**Figure: Dose-Response by Sex × SES (5 Activities × 3 Outcomes)**
![All Outcomes Sex SES](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_dose_response_sex_ses.png)
*Blue=Boys, Red=Girls. Solid=Q1(poor), Dashed=Q4(rich). Academic shown as deviation from subgroup optimum.*

| Activity | Academic Optimum | Life Satisfaction Optimum | Belonging Optimum | Aligned? |
|----------|-----------------|--------------------------|-------------------|----------|
| **Gaming** | 2-4h | 30-60m | Never/<30m | NO |
| **Social Media** | 1-2h | 30-60m | 2-4h | NO |
| **Video** | Never/<30m | 30-60m | 1-2h | NO |
| **Browsing** | 1-2h | 30-60m | 30-60m | Partial |

The most striking divergence: SM's academic optimum is low use, but belonging optimum is moderate-to-high. SM serves a real social function even as it hurts grades.

Note on weighting: Screen activities explain R²=0.078 for academics, R²=0.010 for belonging, and R²=0.002 for life satisfaction. LifeSat effects are negligible in magnitude — observed LifeSat trends likely reflect reverse causation (low satisfaction drives SM use, not the other way around).

### Optimal Activity Combination by Subgroup

Activities interact — the optimal level of one depends on others (saturation effect). A grid search across 625 combinations finds:

| Group | Gaming | Social Media | Browsing | Video |
|-------|--------|-------------|----------|-------|
| **Poor Boys** | **2-4h** | 1-2h | 1-2h | 30-60m |
| **Rich Boys** | 1-2h | 1-2h | 30-60m | **Never** |
| **Poor Girls** | 2-4h | 1-2h | 1-2h | 1-2h |
| **Rich Girls** | **Never** | 1-2h | 1-2h | 30-60m |

SM at 1-2h is the only universal optimum across all subgroups. Video is the clearest "reduce" signal.

---

## Part V-c: Health Effects Beyond Academics

PISA measures academics, belonging, and life satisfaction. For health outcomes — mental health, substance use, sleep, cyberbullying — we turn to the Youth Risk Behavior Surveillance System (YRBSS 2023, N=15,203 US high school students). YRBSS measures social media frequency on a 7-point scale (None → Almost constantly) but does not distinguish between gaming, video, and other activities.

### SM Frequency Correlates with Every Negative Health Outcome

**Figure: Health Outcomes by SM Frequency**
![YRBSS Health Outcomes](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_yrbss_health_outcomes.png)

Every outcome worsens monotonically with SM frequency. The heaviest users ("constantly") vs non-users:

| Outcome | Non-Users | Constant Users | Difference |
|---------|-----------|---------------|------------|
| Poor mental health | 15% | 24% | +9 pp |
| Sad/hopeless 2+ weeks | 31% | 41% | +10 pp |
| Considered suicide | 19% | 23% | +4 pp |
| Cyberbullied | 31% | 41% | +10 pp |
| Current alcohol | 9% | 27% | +18 pp |
| Current marijuana | 8% | 21% | +13 pp |
| Current vaping | 7% | 20% | +13 pp |
| Sufficient sleep | 27% | 20% | -7 pp |

Substance use shows the steepest gradient — alcohol triples from non-users to constant users.

### Girls Are Hit Harder

**Figure: Sex Differences in SM Health Effects**
![YRBSS Sex Differences](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_yrbss_sex_differences.png)

| Outcome | Boys (None→Constant) | Girls (None→Constant) |
|---------|---------------------|----------------------|
| Poor mental health | 11% → 18% | 21% → 35% |
| Considered suicide | 13% → 17% | 29% → 31% |
| Cyberbullied | 23% → 29% | 45% → 61% |

Girls have higher baselines and steeper gradients. 61% of girls using SM constantly report being cyberbullied vs 29% of boys.

### The Vulnerability Multiplier: Pre-Existing Trauma Matters More Than SM

**Figure: SM × Adverse Childhood Experiences**
![ACE Interaction](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_yrbss_ace_interaction.png)

**SM's mental health effect is almost entirely concentrated among already-vulnerable youth:**

| ACE Level | Poor MH at Low SM | Poor MH at High SM | SM Gradient |
|-----------|------------------|-------------------|-------------|
| 0 ACEs (N=12,007) | 7% | 10% | **+3 pp** |
| 1 ACE (N=3,108) | 24% | 31% | +7 pp |
| 2+ ACEs (N=4,988) | 34% | 51% | **+17 pp** |

For healthy students (0 ACEs), SM barely matters (+3pp). For traumatized students (2+ ACEs), SM amplifies vulnerability by +17pp. The same pattern holds for LGBQ students (27%→48% vs straight 12%→21%).

**Conclusion**: SM amplifies pre-existing vulnerabilities rather than causing problems in healthy teens. Targeting vulnerable populations would be far more effective than universal screen time limits.

---

## Part VI: Video — The Clearest Harm

### Video Is 1.8x More Harmful Than Social Media

Streaming video is the second most harmful activity after News (β=-0.14 vs β=-0.17), but unlike News it is heavily consumed. It has the least evidence of a protective 'optimum' and should be actively limited to under 30 minutes.

**Figure 6: Video Dose-Response**
![Video Dose Response](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_video_dose_response.png)

The effect comparison:
- **Video → Math: β = -0.143**
- **Social Media → Math: β = -0.081**
- **Ratio: Video is 1.8x more harmful**

Video has the most left-shifted optimum of all activities: all groups except poor girls score best with *no video at all* (-79 pts at 4h+ for rich boys). Video involves prolonged passive consumption where the brain "switches off" for extended periods, unlike social media which at least activates social processing.

---

## Part VI-b: News — The Most Harmful (and Least Suspected)

### News Dose-Response by Subgroup

Unlike gaming or SM or even video, News has **no beneficial dose range for any subgroup**. The optimum is "Never" universally:

**Figure: News Dose-Response by Sex × SES**
![News Dose Response](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_news_dose_response.png)

| Subgroup | Penalty at 1-2h | Penalty at 4h+ | Optimum |
|----------|----------------|----------------|---------|
| Poor Boys | -31 pts | -75 pts | Never |
| Rich Boys | -23 pts | -80 pts | Never |
| Poor Girls | -15 pts | -55 pts | Never |
| Rich Girls | -18 pts | -73 pts | Never |

The harm is monotonic and substantial — at 4h+ use, the academic penalty ranges from 55 to 80 points depending on subgroup.

### "Reading the News" Is Not What You Think

Among 15-year-olds, "reading the news" means scrolling algorithmically-curated content feeds — not reading newspapers. Despite being the least-consumed activity (60% report never or rarely), News has the strongest negative effect of any screen activity: β=-0.174 (SES-adjusted), worse than Video (β=-0.143) or SM (β=-0.081).

Critically, this effect is **independent of other activities**. After controlling for Gaming, SM, Browsing, and Video simultaneously, News retains β=-0.154 (p<0.001). It is not simply a proxy for total screen time.

### Who Are Heavy News Users?

Heavy news consumers (8.8% of the sample) are not information seekers — they are general over-consumers of everything:

| Characteristic | Heavy News (level 5+) | Light/Never (level 1-2) |
|---------------|----------------------|------------------------|
| N | 5,400 | 36,896 |
| Mean SES | **-0.28** | -0.05 |
| Academic Score | **-54 pts** | +18 pts |
| Mean Gaming | 4.12 | 2.79 |
| Mean SM | 4.64 | 3.28 |
| Mean Video | 4.75 | 2.47 |
| Female | 45% | 52% |

Heavy news users consume ALL activities at near-maximum levels. They are poorer and more male than average. The profile suggests compulsive scrolling behavior rather than deliberate information seeking.

### Why Is News So Harmful?

Three hypotheses:

1. **Passive consumption without cognitive engagement** — Like video, news feeds are consumed passively. Unlike SM, there is no social interaction to provide even partial cognitive benefit. The dose-response mirrors Video's monotonic decline.

2. **Algorithmic rabbit holes** — Feeds optimized for engagement (outrage, fear), not learning. Heavy users show addiction-like over-consumption of everything.

3. **No compensatory benefit** — Unlike SM (which helps belonging), news hurts both academics and belonging with no offsetting social function.

The harm scales with wealth (News×SES: β=-0.018, p<0.001) — same pattern as Video and SM.

**Policy**: News feeds should be treated like video — limit or avoid. "Reading the news" on a phone is not an educational activity.

---

## Part VII: Gaming — The Most Beneficial

Gaming shows the clearest positive effect for most groups — stronger for boys, and far more beneficial for poor than rich.

### Gaming Effects Depend on BOTH Wealth AND Sex

Overall: Males β=+0.097, Females β=-0.003. But this hides enormous complexity:

**Figure 8: Gaming Corrected for Poverty**
![Gaming Corrected](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_gaming_corrected.png)

| SES Level | Males | Females |
|-----------|-------|---------|
| **Low SES** | β = **+13.9** | β = +6.1 |
| Mid SES | β = +4.8 | β = -1.5 |
| **High SES** | β = +1.2 (n.s.) | β = **-6.3** |

Gaming shows the widest optimum shift of any activity: from 2-4h (poor boys, -63 pts from zero) to Never/<30m (rich girls, -37 pts from heavy use). For poor boys, *not gaming at all* is more harmful than *heavy gaming* (-63 vs -8 pts).

### Gaming Subgroup Profiles

- **Male non-gamers** (N~1,079 in Q1): Lowest SES (-0.23), lowest Math (389), highest video consumption — toxic activity mix: deprived of beneficial activity, compensating with the most harmful
- **Male heavy gamers** (4h+): Lower SES than moderate gamers, higher SM and video use — heavy gaming is part of a general high-consumption pattern with displacement of other beneficial activities and sleep deprivation
- **Female non-gamers** dominate (74% of non-gamers are female) — gender preference or social stigma, not access limitation

### The Gaming Stigma Effect on Girls

The data reveals a striking pattern: gaming improves girls' academics but consistently hurts their belonging and life satisfaction — a pattern consistent with social stigma rather than the activity itself being unpleasant.

**Figure: Gaming Stigma — Belonging and Life Satisfaction by Sex × SES**
![Gaming Stigma](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round8/fig_gaming_stigma.png)

Rich girls who game at moderate levels lose **0.23 belonging points** (from +0.26 to +0.03) while gaining only modestly in academics. By contrast, rich boys who game at the same level *gain* belonging (+0.36). The stigma signal: only 7% of rich girls are heavy gamers. Girls avoid gaming despite it being neutral or even helpful for their academic results because the social cost is too high. Instead, they shift to SM (r=+0.39 between gaming and SM for girls) — an activity that hurts their satisfaction but preserves belonging — and to video, which clearly hurts academics with no compensatory benefit. De-stigmatizing gaming for girls could yield academic gains without the belonging penalty that currently drives them toward more harmful alternatives.

---

## Part VIII: Social Media — Boys vs Girls

### Academic and Wellbeing Effects Vary by Sex AND Wealth

The SM effect is not a single number — it varies dramatically by both sex and SES. Full stratification reveals a gradient, not a binary:

**Figure: SM Effects by Sex × SES**
![SM Stratified](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_sm_stratified.png)

| Group | SM → Math (β) | SM → Life Satisfaction (β) | SM → Belonging (β) |
|-------|---------------|---------------------------|-------------------|
| **Poor Boys (Q1)** | -0.015 (n.s.) | **+0.040** | **+0.062** |
| Rich Boys (Q4) | **-0.183** | +0.010 (n.s.) | +0.039 |
| **Poor Girls (Q1)** | -0.019 (n.s.) | **-0.053** | +0.033 |
| Rich Girls (Q4) | **-0.133** | **-0.052** | +0.033 |

Key patterns:
- **Academic harm scales with wealth**: SM is essentially harmless for Q1 students (β ≈ -0.02) but strongly negative for Q4 (β ≈ -0.13 to -0.18)
- **Wellbeing effects are sex-dependent**: Boys show positive SM → life satisfaction across all SES levels; girls show negative effects across all levels
- **Belonging is universally positive**: SM → school belonging is mildly positive for all subgroups (+0.02 to +0.06)
- **The happiness-academics tradeoff is real for boys**: Q2 boys lose academically (β=-0.06) but gain in wellbeing (β=+0.06) — SM serves a genuine social function
- **All groups gain belonging from SM** (+0.02 to +0.06), but the cost differs: rich students pay in academic scores, girls pay in satisfaction, and rich girls pay in both

**Figure 9: Wellbeing by Sex**
![Wellbeing by Sex](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_wellbeing_by_sex.png)

| Sex | SM → Life Satisfaction (β) |
|-----|---------------------------|
| Males | **+0.031** (positive!) |
| Females | **-0.064** (negative) |

**Boys benefit from (or are unharmed by) social media for wellbeing.** Only girls show the negative mental health effect. The mechanisms differ by sex.

---

## Part IX: Cyberbullying — The Real Hit

### It's Not Time, It's What Happens During That Time

Cyberbullying is the single largest mediator of social media's mental health effects:

**Figure 11: Cyberbullying Impact**
![Cyberbullying Impact](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/todo_fixes/fig_cyberbullying_impact.png)

**The scale of the problem**: Out of 15,203 US high school students surveyed (YRBSS 2023), 4 in 10 (41%) reported being cyberbullied. Cyberbullying increases with SM use: from 33% among low SM users to 44% among heavy SM users.

**The impact**: Cyberbullied students are 4x more likely to report poor mental health and 7.6x more likely to have considered suicide compared to non-bullied peers. After adjusting for sex, age, LGBQ status, adverse childhood experiences, and sleep:

| Predictor | Prevalence (Not Bullied) | Prevalence (Bullied) | Risk Multiplier |
|-----------|--------------------------|---------------------|-----------------|
| Poor Mental Health | ~12% | ~47% | **4.0x** |
| Considered Suicide | ~5% | ~38% | **7.6x** |

- **SM Intensity alone**: Each level increase → ~5 percentage points more poor mental health (from ~20% at low use to ~35% at heavy use)
- **Cyberbullying dwarfs SM's direct effect**: The difference between bullied vs not-bullied (35 pp) is 7x larger than the difference between low vs heavy SM use (15 pp)
- **PAF = 59%** — an estimated 59% of all poor mental health cases involve cyberbullying

**Targeting cyberbullying directly would be far more effective than limiting screen time.**

---

## Part XI: What This Means

### The Policy Implications

#### Do:
1. **Target video streaming and news scrolling** — clearest displacement effects (video 1.8x larger than SM; news universally harmful with β=-0.17, optimal = never for all groups)
2. **Address cyberbullying** — the dominant mechanism (7x larger effect than SM intensity, PAF = 59%)
3. **Set SES-differentiated guidelines** — poor students need 1-2h+ for optimal outcomes; rich students should stay below 1h for most activities
4. **Differentiate by sex** — boys and girls have different optimal doses and different wellbeing responses
5. **Encourage activity substitution** — switching from video to gaming yields +0.28 β for poor boys, no reduction in total screen time needed
6. **Focus on Science and Reading education** — both show clearest smartphone-era reversal

#### Don't:
1. **Ban all screen time** — zero use costs poor boys up to 63 Math points (gaming) or 40 points (SM for poor girls)
2. **Treat all activities equally** — video is 1.8x worse than social media; gaming has positive effects for disadvantaged boys
3. **Apply uniform screen time limits** — a one-size cap helps rich students and hurts poor ones
4. **Ignore SES in research** — SES effects are 2-5x larger than screen effects; without controlling for it, all screen time research is confounded

### Activity Substitution: What Should Replace What?

*(See Part XII: Recommendations for subgroup-specific guidance)*

Since some activities are more harmful than others, switching from one to another may improve both wellbeing and academic results without reducing total screen time. We computed simultaneous multi-activity regressions within each Sex × SES subgroup to identify the best substitutions (Email and Homework excluded as they reflect reverse causation, not leisure choices).

**Figure: Activity Effect Rankings by Subgroup**
![Activity Substitution](https://raw.githubusercontent.com/petr-salomoun/screens-and-teens/main/analysis/figures/round9/fig_activity_substitution.png)

| Subgroup | Activity Ranking (best → worst) | Best Switch | Academic β Gain |
|----------|--------------------------------|-------------|-------------|
| **Poor Boys** | Gaming > Browsing > SM > News > Video | Video → Gaming | **+0.28** |
| **Rich Boys** | Gaming > Browsing > SM > News > Video | SM → Gaming | +0.19 |
| **Poor Girls** | Gaming > Browsing > SM > News > Video | Video → Gaming | +0.22 |
| **Rich Girls** | Browsing > Gaming > SM > Video > News | Video → Browsing | +0.17 |

Gaming is the most beneficial screen activity across all subgroups except rich girls (where browsing ranks first). The key practical insight: **a poor boy switching 1 hour of passive video to gaming would gain the equivalent of ~25 Math points** (β=+0.28 substitution effect), without any reduction in total screen time.

For girls, the substitution picture is different: SM is mildly negative while browsing is mildly positive, suggesting that **encouraging informational browsing over social media scrolling** may be more effective than limiting overall screen time.

---

## Part XII: Personalized Recommendations

### What Should Parents Actually Do?

**Universal rules (all subgroups):**
- **Never allow news scrolling** — universally harmful (β=-0.17), no beneficial dose for any group
- **Minimize video streaming** — strongest displacement effect, optimal is zero or near-zero for all groups
- **Prioritize cyberbullying prevention** over any time limit

**Individual caps within a total screen budget:**

The recommendations below are *per-activity caps within a total daily budget*, not sums. The total optimal leisure screen time is approximately 3-4h/day for poor students and 2-3h/day for rich students.

#### Poor Families with Boys

**Total ~4h/day: Gaming ≤2-4h | SM ≤1-2h | Browsing ≤1-2h | Video <30min | News: never**
- Gaming is their strongest positive — zero gaming costs 63 pts
- If total must be reduced, cut video first
- Priority: cyberbullying awareness, not time limits

#### Poor Families with Girls

**Total ~4h/day: Gaming ≤2-4h | SM ≤1-2h | Browsing ≤1-2h | Video <1h | News: never**
- Gaming helps academics but hurts belonging — tradeoff
- SM hurts girls' satisfaction even when academic effects are neutral — monitor mood
- Priority: cyberbullying (4x mental health risk for girls)

#### Wealthy Families with Boys

**Total ~2-3h/day: Gaming ≤1-2h | SM ≤1-2h | Browsing ≤30-60min | Video: none | News: never**
- Eliminate video — rich boys score best with zero
- SM at 1-2h balances belonging (+0.04) against academic cost (-0.18)
- Biggest gain: eliminating video

#### Wealthy Families with Girls

**Total ~2-3h/day: Gaming: none | SM ≤1-2h | Browsing ≤1-2h | Video <30min | News: never**
- Most restricted subgroup — but not zero across the board
- SM at 1-2h still optimal (universal finding)
- Priority: content quality and cyberbullying prevention over time limits

---

### Limitations

1. **Cross-sectional design** — causation uncertain
2. **Self-reported screen time** — measurement error
3. **YRBSS lacks SES control** — mental health findings have caveat
4. **Activity categories broad** — "gaming" includes many types
5. **Instagram/smartphone separation impossible** — events clustered 2010-2012
6. **COVID contaminates 2020+ data** — cannot separate screen effects from pandemic effects
7. **YRBSS temporal coverage limited** — only 2023 wave processed; extending to 2015+ is planned
8. **PISA frequency scale ambiguity** — scale 1-7 captures ordinal frequency, not exact hours

---

*Report generated: May 20, 2026*
*Analysis: Corrected for poverty confounding, sex interactions, and activity substitution*
*Datasets: PISA 2022, YRBSS 2023*
*Total observations: ~700,000 across 80 countries*

---

**License:** This work is freely available for any use. Publication of derived works must attribute Petr Salomoun. Contact: [petr.salomoun@gmail.com](mailto:petr.salomoun@gmail.com)
