---
author: Petr Salomoun
categories:
- criminology
date: 2026-04-26 22:32:24+00:00
excerpt: 'Analyzing 16 million crime reports across five major US cities reveals five distinct patterns of how temperature, precipitation, and seasons drive different types of violence.'
github_repo: petr-salomoun/weather-crime
layout: post
tags:
- crime
- weather
- data-science
- urban-analytics
- statistical-analysis
title: 'Weather and Crime: Five Archetypes of How Climate Shapes Urban Violence'
updated_at: '2026-04-26T22:32:24+00:00'
---

# Weather and Crime: Five Archetypes of How Climate Shapes Urban Violence

**Cities:** Chicago · Houston · Los Angeles · New York · Philadelphia  
**Period:** 2020–2024  
**Data:** ~16 million police incident records  
**Weather:** NOAA GHCN-Daily station observations  

---

## The Question

Picture a beer garden on a warm Friday night in July: plenty of people outside, some cheerful, some tipsy, some loud — the occasional argument is no surprise. Statistics confirm that crime rises on such nights, and that is hardly surprising either. But *which* crimes rise with heat, and *why*? Is it anger? Is it opportunity? Or is it simply that more people are outside?

Heat is the most obvious suspect — but it is also the most confounded. Temperature does not rise alone: longer days, more people outdoors, school holidays, increased bar patronage, and tourist season all move with it. When you observe that crime rises with temperature, you are not seeing a single cause. You are seeing dozens of correlated forces bundled together.

Only when the temperature effect is removed do the true underlying patterns surface, and different crime types begin to differentiate.

This report presents a data-driven analysis of weather, calendar, and crime across five major U.S. cities from 2020 to 2024. The central finding is that **five fundamentally different crime archetypes emerge**, each with a distinct causal story supported by consistent patterns across all cities. A hot August afternoon is not the same threat to everyone — and understanding the difference has practical implications for how we think about crime prevention.

---

## Part 1 — The Temperature Signal

### Everything goes up with heat

The first thing you notice when you look at the data is that almost every crime type rises with temperature. The chart below makes this vivid: plotting crime rate deviation against daily maximum temperature, all five selected crime types show a clear upward trend, though some level off at the extremes.

![Crime rate vs temperature — Chicago](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_A_crime_vs_temperature.png)

*Figure 1a. Crime rate deviation (% from annual mean) vs daily max temperature for selected crime types in Chicago. All types rise with heat, but assault rises fastest while domestic violence rises the least.*

Below is the size of that temperature effect for Chicago — measuring by how much the crime rate increases from the coldest to the warmest days of the year.

![Temperature effect on all crimes — Chicago](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_01_heat_effect_all_crimes.png)

*Figure 1b. Temperature effect on each crime type in Chicago (2020–2024). Colours indicate the hypothesised archetype (see later in this document). All crime types increase with temperature, but the magnitude and mechanism differ.*

Assault rises **around +61%** on the hottest vs coldest days. Sexual assault: **+50%**. Even domestic violence, the most weather-insensitive crime, still shows a **+21%** increase. The pattern holds across all five cities, though the magnitude varies with local climate — Houston, where even winter days are mild, shows a compressed range.

The heatmap below makes this explicit. We have computed many weather-related metrics (factors) and selected the top 15 with the strongest effect across the various crime types. For each factor × crime combination, the colour shows the direction and magnitude of the relationship. In the raw data, temperature and its thermal composites dominate. Even the factors that appear negative are mostly thermal constructs in reverse: heating degree days and misery index are defined as inverse transformations of temperature, so their blue columns inversely mirror the red temperature columns. Apart from calendar factors (weekend, holiday), wind, and precipitation, almost no factor in the standard weather toolkit is genuinely independent of temperature.

![Top-15 factors × crime types — signed heatmap](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_D_top15_factors_heatmap.png)

*Figure 1c. Signed effect heatmap: top-15 factors (rows, ranked by average absolute effect across all crimes) × crime types (columns). Red = crime rises with factor; blue = crime falls. The thermal block at the top — temperature, apparent temperature, comfort indices, degree days — dominates and is internally collinear. Calendar and precipitation factors appear further down, where their genuinely independent effects are smaller but more differentiated across crime types.*

The dominance of the thermal cluster is not a surprise and not a problem in itself: it accurately reflects what the data show. The challenge is that almost any weather metric we choose to measure is already collinear with temperature. Searching for a "different" signal within weather data alone will keep leading back to heat. The genuinely independent factors are the calendar ones — weekends, holidays — and these are precisely the factors that reveal the structural differences between crime types explored below.


### The problem: heat is hiding the real story

Temperature co-varies with dozens of other things simultaneously: longer days, more outdoor socialising, school holidays, bar patronage, tourist season. When temperature is used to explain crime, all of those mechanisms are bundled together in a single number.

The chart below shows this directly: the factor inter-correlation matrix for Chicago. Max temperature (highlighted in orange) is strongly correlated with outdoor comfort, apparent temperature, cooling degree days, and hot streaks — and moderately with outdoor activity proxy and night comfort. These are not independent levers; they all move together.

![Factor correlation matrix — Chicago](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_B_factor_correlation_matrix.png)

*Figure 3. Pearson correlation matrix of weather and calendar factors (Chicago). Max temperature (highlighted row/column) co-varies strongly with comfort indices, outdoor activity proxy, and heat accumulation measures. These correlated factors make it impossible to attribute crime changes to temperature alone without controlling for the rest.*

Even a pair of factors as intuitively distinct as temperature and daylight hours are highly correlated, since they overlap heavily across the seasons. Only by deeper inspection can the two causal effects be separated. Plotting assault rate, temperature, and daylight hours on the same monthly axis illustrates how tightly they co-move:

![Assault rate, temperature, and daylight — Chicago](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_C_assault_temp_daylight.png)

*Figure 4. Monthly trends for Chicago (normalized 0–1): daylight hours (blue dashed), max temperature (orange), and assault rate index (red). Daylight peaks in June — a full month before temperature peaks in July — while assault tracks temperature closely and lags daylight. This phase separation is analytically useful: the one-month offset means the daylight and temperature signals can in principle be disentangled, and the crime curve clearly follows temperature rather than light.*

The radar charts below summarise each crime type's raw factor profile. In the raw data, every profile is dominated by the same seasonal factors — temperature and comfort variations pull every crime curve in the same direction.

![Crime factor radar profiles — all crimes](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/existing_crime_radars_all.png)

*Figure 5. Factor profile radar charts for all crime types (Chicago). Each axis is a weather or calendar factor; the coloured line shows how strongly each crime responds to that factor. In the raw data, the summer-heat complex (tmax, comfort, cooling DD) dominates almost every profile, making the crimes appear superficially similar.*


### Separating the temperature signal

The key analytical step is to mathematically remove the temperature component and examine what patterns remain.

Beyond making crimes appear uniformly warm-season phenomena, the temperature effect also creates the illusion of similarity between crime types that are actually driven by entirely different mechanisms. Only after removing temperature does an interpretable structure emerge:

![Crime similarity — raw rates](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_02_similarity_before_after.png)

*(Both panels show crime × crime profile similarity — how similarly two crime types respond to the same set of factors. Left panel uses all available weather and calendar factors; right panel uses only those factors that retain explanatory power after temperature is removed, so thermally collinear measures drop out.)*

The result is striking. In the raw data, **theft looks similar to sexual assault** or to domestic violence. After removing temperature, this spurious similarity collapses to near zero or negative. Theft instead pairs more tightly with **auto theft** and **burglary**, as one would expect. The illusion was created by both theft and sexual assault having a slightly weaker-than-average temperature response, making them look similar in raw profiles despite sharing no causal mechanism.

The heatmap below re-ranks the factors from scratch *after* removing temperature, selecting the top 15 by their post-residualisation effect size. Note that some thermal factors (heating degree days, apparent temperature) still appear because they retain partial predictive power even after the main temperature component is removed.

![Before and after removing temperature — dual factor heatmap](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/heat_residuals_heatmap_comparison.png)

*Figure 6b. Side-by-side factor × crime heatmaps: left panel uses all factors (same as Figure 1c); right panel re-ranks after statistically removing temperature. After detrending, the opportunistic crime cluster (burglary, robbery, auto theft) and the social-occasion signature of sexual assault become more prominent, while the thermal factors compress. Factors that survive detrending — weekends, holidays, precipitation — are the genuinely independent signals.*

After removing heat, the underlying structure becomes clear — and that structure describes five distinct archetypes.

It is possible to go further and compare two specific crime types side by side, examining which factors make them similar and which differentiate them. Consider robbery vs auto theft: in the raw factor profiles, both crimes look nearly identical — both are strongly temperature-driven (+40–50%), both peak in summer. Temperature is the great equaliser. But after removing temperature, the differences become visible: robbery responds positively to bar weather and weekends, marking it as a social, victim-present crime; auto theft responds to sustained heat and recreational weekend patterns. The same thermal signal that made them look alike was masking the distinct causal mechanisms underneath.

![Pairwise comparison — Robbery vs Auto Theft](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/pairwise_robbery_vs_auto_theft.png)

*Figure 3b. Left: raw factor profiles for robbery and auto theft look nearly identical — temperature dominates both. Right: after removing temperature, the social character of robbery (bar weather, weekend positive) diverges from the structural character of auto theft (recreational-opportunity driven). The thermal confound was hiding the distinct causal mechanisms.*

---

## Part 2 — The Five Archetypes

Some crime types show strong pattern similarities, suggesting shared causal mechanisms, and have been grouped accordingly:
- **Outdoor Aggression** — assault and vandalism
- **Opportunistic Crime** — robbery, burglary, and auto theft

The remaining three are structurally distinctive enough to stand alone: sexual assault, theft, and domestic violence.

The chart below places each archetype in a two-dimensional conceptual space, with axes chosen to capture the primary causal dimensions that the data reveal.

![Archetype taxonomy](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_03_archetype_taxonomy.png)

*Figure 4. The five crime archetypes placed in a two-dimensional conceptual space. Horizontal axis: does the crime primarily occur outdoors or indoors? Vertical axis: is it driven by social/calendar occasions or by structural/routine factors? Single-crime archetypes (Sexual Assault, Theft, Domestic Violence) are named directly after their crime; combined archetypes (Outdoor Aggression, Opportunistic Crime) group multiple crimes with a shared causal mechanism. Positions derived from weather and calendar effect patterns.*

The five archetypes are described in the sections that follow, each with the supporting evidence.

---

### Archetype 1 — Outdoor Aggression
#### *Crimes: Assault, Vandalism*

These are the crimes most directly driven by heat — and not merely because more people are outdoors. A substantial body of research links high temperatures to increased physiological arousal and irritability. Hot days produce short fuses.

The factor profile for assault and vandalism is characterised by:
- Strongly positive temperature response (+62% / +47% in Chicago)
- Little correlation with other factors after removing heat
- Positive weekend and social effects (+4% and +11% on weekends; +26% / +16% on "bar weather" days — defined as days with tmax ≥ 18 °C, no significant rain, occurring on a Friday or Saturday)
- Positive outdoor activity proxy (both victim and perpetrator need to be outdoors)

![Day-of-week: Outdoor Aggression](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_05a_dow_aggression.png)

*Figure 5a. Day-of-week profiles for assault and vandalism in Chicago. Bars show % deviation from the weekly average for each day. Weekend is shaded in yellow. Peak and trough are annotated.*

![Archetype validation — Outdoor Aggression](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/existing_xc_aggression.png)

*Figure 5. Cross-city validation: assault and vandalism signed effects for three key factors across all five cities. Each bar is one city. Red = positive effect (crime rises with that factor), blue = negative. Expected direction is labelled in each cell.*

The pattern is broadly consistent across cities. Chicago and LA show the strongest temperature effects; Houston shows a weaker range, since mild winters compress the temperature contrast. The social facilitation signal — bar weather and weekends — holds in most cities. Philadelphia is a notable exception where the weekend effect for assault is negative; this is the most discrepant result in the cross-city validation and warrants caution. Possible explanations include differences in how assault is classified in Philadelphia's reporting system, or genuine geographical differences.

**The causal story:** Heat produces agitation. The crime happens outdoors, in public, often in social settings. The opportunity and victim are incidental; the driver is the perpetrator's physiological state and social context.

---

### Archetype 2 — Opportunistic Crime
#### *Crimes: Robbery, Burglary, Auto Theft*

These crimes share a different logic: **the victim must be away from home (or away from their car) for the crime to occur.** The criminal here is not primarily driven by impulse or emotion — they need an opportunity. When people are outside and away from their homes and vehicles, that opportunity multiplies.

All three crimes show positive temperature responses, but the *day-of-week* signatures reveal important differences within this archetype.

![Day-of-week: Opportunistic Crime](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_05b_dow_opportunistic.png)

*Figure 6. Day-of-week profiles for robbery, burglary, and auto theft in Chicago. Bars show % deviation from the weekly average for each day. Weekend is shaded in yellow. Peak and trough are annotated. Note that Friday often functions as an extended weekend for social crimes, reflecting Friday-evening activity.*

**Robbery** peaks on the weekend (Sunday +13.5%, Saturday +10.8% in Chicago), consistent with its social, victim-present character — more people out in social settings on weekend evenings.

**Burglary** shows the most revealing signature: a pronounced **Monday peak** (+8.6% Chicago, +5.6% NYC, +33% Philadelphia) and a trough later in the week. The cross-city pattern is consistent: burglars strike most frequently at the start of the working week, when residents leave for work after being home all weekend. In most cities (Houston, LA, NYC, Philadelphia) Sunday is the single lowest day — confirming the victim-at-home deterrence effect. Chicago is the partial exception: the weekend is flat rather than negative, but the Monday spike is still present.

**Auto theft** runs in the opposite direction within this archetype: it peaks on weekends (+7% Saturday, +6% Sunday in Chicago). The most likely explanation is that people drive to recreational destinations and leave their cars in less-supervised locations, while the car is more visible and accessible than when driven and parked at a regular workplace.

One seasonal outlier deserves a note: Chicago auto theft peaks in **October**, while the same crime peaks in August in Houston, LA, New York, and Philadelphia — all closely tracking temperature. The Chicago anomaly is almost certainly not weather-driven: it coincides with the 2022–2023 Kia/Hyundai theft wave, a viral social-media trend that disproportionately affected Chicago. This is a useful reminder that even in a dataset of 16 million records, a single local crime wave can dominate the seasonal signal and produce an apparent phase shift relative to temperature.

![Seasonal phase comparison — DV vs street crimes](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/h6_1_seasonal_phase.png)

*Figure 7. Seasonal phase comparison: domestic violence, robbery, and assault monthly patterns (Chicago). This cross-archetype seasonal chart makes visible how DV peaks in June (aligned with temperature), while robbery and assault follow a similar summer arc — confirming the phase-separation between indoor and outdoor crime types.*

![Chicago auto theft by year — Kia/Hyundai spike](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/h7_5_autotheft_by_year.png)

*Figure 7b. Chicago auto theft rate by year (2020–2024). The 2022 spike — roughly 3× above the 2021 baseline — is the Kia/Hyundai theft wave. The 2023–24 partial recovery is visible. This year-by-year view confirms that the Chicago seasonal anomaly (October peak) is an artefact of this single year, not a structural seasonal pattern.*


**The causal story:** The criminal is opportunistic and patient. When victims are away from home or their vehicles — which happens more in warm weather, on weekends for recreation, and early in the working week for burglary — crime rises. The Monday burglary peak reflects the moment residents leave for work after a weekend at home, creating a predictable window of vacant properties. Emotion is secondary; access is primary.

---

### Archetype 3 — Sexual Assault
#### *Crime: Sexual Assault*

Sexual assault presents what is, on the surface, a paradox.

It has the **third-highest temperature response** in the dataset (+50% in Chicago). This places it squarely in the "heat-driven" category alongside assault. Yet the post-temperature residual heatmap (Figure 6b) shows that sexual assault has the strongest residual response of any crime and correlates *negatively* with outdoor comfort factors and *positively* with outdoor discomfort factors (misery index, rain). This is the opposite of outdoor crimes like assault and robbery, which respond negatively to discomfort.

The sign pattern is consistent with the crime occurring predominantly in indoor settings: rain and cold, which push people indoors, are associated with slightly *higher* sexual assault rates. The mechanism runs through social context — heat creates the gatherings and occasions; the crime occurs in private settings within those gatherings, not in parks.

![Sexual assault: heat response](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_10_sexual_assault_signature.png)

*Figure 9. Both assault and sexual assault rise with temperature, but sexual assault's increase is shallower — consistent with temperature acting as a social catalyst (creating occasions) rather than a direct physical trigger.*

![Assault vs Sexual Assault: pairwise factor profiles](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/pair_assault_vs_sexual_assault.png)

*Figure 9b. Left: raw factor profiles for assault and sexual assault look similar (temperature dominates both). Right: after removing temperature, the profiles diverge sharply. Assault is positively associated with outdoor comfort and activity (an outdoor crime); sexual assault is positively associated with discomfort factors like precipitation and misery index (an indoor crime that benefits from people being concentrated in private settings during social events).*

Heat drives sexual assault not by putting people on the street, but by creating **social occasions**: parties, bars, events where alcohol flows and inhibitions loosen. The crime itself occurs indoors or in enclosed spaces. The calendar effects confirm this: sexual assault has the highest holiday effect of any crime (+14% in Chicago, +36% in New York, +77% in Los Angeles), consistent with major social events and holiday gatherings.

Rain, which keeps people indoors, is slightly associated with *higher* sexual assault rates — the opposite of outdoor crimes. Sexual assault is the most strongly differentiated crime on the dimension that captures precipitation and victim-not-outdoors.

**The causal story:** Temperature is a social catalyst, not a physical trigger. Warm evenings produce the gatherings; the crime occurs in private settings within those gatherings. The mechanism runs through social context, not outdoor exposure.

---

### Archetype 4 — Theft
#### *Crime: Theft (General)*

Theft is one of the most analytically surprising crimes in the dataset. In the raw data it appears to cluster with sexual assault. Once temperature is removed, it belongs solidly with auto theft. Neither of those observations is the main story. The main story is the **day-of-week profile**.

![Theft vs Auto Theft: day-of-week comparison](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_07_theft_vs_autotheft_dow.png)

*Figure 10. Day-of-week profiles for theft (general) and auto theft. Theft peaks on Friday (+10%) and collapses on Sunday (−14%). Auto theft peaks on Saturday and Sunday. These near-mirror-image patterns reveal opposite causal mechanisms.*

Theft *collapses* on Sunday (−14% in Chicago). It peaks on Friday. The holiday effect is the largest and most negative of any crime (−19% in Chicago, −14% in Houston, −14% in Philadelphia). What closes on Sunday and on public holidays? **Retail shops and commercial facilities.**

After removing the temperature component, the strongest residual effects are related to discomfort (rain, wind, extreme cold or heat) — all of which keep shoppers away. The dominant signal, however, remains the calendar: the weekday/weekend and weekday/holiday contrasts in theft rates are far larger than the weather effect, confirming that shop hours, not weather, drive this crime.

![Theft residual factors after removing temperature](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/existing_theft_residual.png)

*Figure 11. Factors driving theft after statistically removing temperature. The strongest remaining signals are: weekend (negative — shops close) and holiday (negative). These confirm the retail/commercial-hours mechanism as the primary driver of theft variation.*

This pattern holds cross-city: wherever the data allow a test, theft shows the weekday/commercial-hours signature.

**The causal story:** Retail theft follows shop hours. The perpetrator is not reacting to heat or emotion — they are operating in a structured commercial environment. Crime rises and falls with foot traffic in commercial spaces.

---

### Archetype 5 — Domestic Violence
#### *Crime: Domestic Violence*

*(Note: cross-city comparison is unreliable for domestic violence due to substantial differences in police reporting definitions across cities. This archetype is characterised primarily from Chicago data.)*

Domestic violence is the most weather-insensitive crime in the dataset. After removing temperature, its factor profile is **negatively correlated with almost every other crime type** — with the exception of sexual assault, which shares the indoor character. DV is not just less weather-driven; it is driven by *different things* than street crime.

![DV vs assault: weather vs calendar](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_09_dv_vs_assault.png)

*Figure 12. Four-panel comparison of assault and domestic violence in Chicago. Top left: seasonal pattern. Top right: day-of-week pattern. Bottom left: temperature response. Bottom right: calendar factor effects. DV's temperature response is weaker and flatter; its calendar effects are larger.*

What drives DV is time spent at home together. The weekend effect is +19% and the holiday effect is +18% — among the highest of any crime. The primary driver is **co-presence**: how long household members spend in close proximity.

![Day-of-week: Domestic Violence](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_05e_dow_dv.png)

*Figure 12b. Day-of-week profile for domestic violence in Chicago. Weekend and holiday days show a consistent +15–19% elevation compared to midweek, driven by co-presence time at home rather than weather or street activity.*

A warm summer day that raises assault rates by 30% barely moves DV. But a long holiday weekend where partners or family members are home for four consecutive days will push DV rates up regardless of temperature.

**The causal story:** Domestic violence is an indoor crime driven by proximity and accumulated tension. Weather affects it only indirectly, by modulating time spent at home. The calendar — weekends, holidays, school breaks — matters far more than the thermometer.

---

## Part 3 — Cross-City Validation

The five archetypes were tested across all five cities. A key question: are these patterns specific to Chicago, or do they hold universally?

![Sign consistency matrix — all cities](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_sign_consistency.png)

*Figure 13. Cross-city sign consistency: for each crime × factor pair, how many of the five cities agree on whether the effect is positive or negative? Dark red = all cities positive; dark blue = all cities negative; pale/white = mixed signals across cities. Annotated with the count of cities showing positive / negative effects.*

**What is consistent across all five cities:**
- Temperature is positively associated with assault, robbery, vandalism, sexual assault, and auto theft in 4–5 cities
- Burglary has a flat or negative weekend effect in 4 of 5 cities
- Theft has a negative holiday effect wherever data are sufficient
- Bar weather is positive for assault and robbery in 4–5 cities
- Heating degree days (cold) suppresses all outdoor crimes in every city

**What varies:**
- Magnitude of temperature effects: compressed in warm-climate cities (Houston, LA) where winter is mild
- Outdoor activity proxy: the most variable factor across cities, reflecting genuine differences in urban form — dense New York vs sprawling Houston produce different "outdoor day" dynamics
- Philadelphia shows unusual patterns for some crimes, possibly related to data collection differences

The overall conclusion: **the archetypes are real and transferable across these five cities.** The directional patterns, not just the Chicago numbers, hold across cities with different climates, geographies, and demographic compositions — though magnitudes vary.

![Cross-city DOW: theft vs auto theft](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_dow_cross_city.png)

*Figure 14. Day-of-week profiles for theft (general) and auto theft across all five cities (city labels shown above each column). Theft data is only available for two cities (Chicago and one other) — columns with "No data available" reflect cities that do not separately report this category. Theft in Chicago shows the commercial-hours signature clearly: Friday peak, Sunday trough. Auto theft shows contrasting patterns across cities — a weekday peak in some cities (consistent with car theft from work or commuter locations) vs a weekend peak in others (recreational destination thefts), consistent with the variation discussed in Part 2. Weekend shading in yellow.*

---

## Part 4 — COVID-Era Natural Experiment and One-Off Events

### A data quality caveat

The dataset covers 2020–2024 — a period that begins during the COVID-19 pandemic and its associated lockdowns, behavioural disruptions, and social changes. This has two implications:

1. **The absolute levels of crime in 2020–2021 are not representative of normal conditions.** Comparisons of crime rates across cities should account for the fact that 2020 in particular was an abnormal year in terms of mobility, commercial activity, and reporting patterns.
2. **The pandemic creates a natural experiment.** The same weather factors operated on a very different social context, allowing us to test whether the weather–crime relationships are robust to structural changes or whether they depend on specific social conditions.

We define three analytical periods:

| Period | Years | Description |
|---|---|---|
| **Lockdown** | 2020 | Full pandemic year — strict lockdowns (Mar–May), partial reopening, second wave |
| **Transition** | 2021–22 | Vaccination rollout, uneven reopening; includes the Chicago Kia/Hyundai theft surge |
| **Post-COVID** | 2023–24 | Return to normal; best approximation of a stable baseline in this dataset |

### What changed during lockdowns

The cross-period comparison reveals several patterns, though the cross-city signal is noisy — cities responded to the pandemic differently in terms of restrictions, reporting practices, and socioeconomic disruption.

![Crime rates: differential vs post-COVID baseline — Chicago](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/h7_1b_rate_differential.png)

*Figure 16. Chicago crime rate change (%) relative to the 2023–24 post-COVID baseline, for each period. Bars above zero = elevated vs baseline; below zero = suppressed. The lockdown period (red) shows a dramatic drop in many crime types, while domestic violence changed relatively little and burglary was the only crime that rose.*

![Cross-city lockdown suppression](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/h7_6_cross_city_lockdown.png)

*Figure 16b. Cross-city comparison: 2020 lockdown crime rates as % change vs 2023–24 baseline, for each city (colours) and crime type. The large variation across cities shows that no single lockdown narrative applies universally — local factors (enforcement, reporting, economic conditions) dominate.*

**Absolute crime rate shifts (2020 vs 2023–24):**
The pattern across cities is heterogeneous: some cities show outdoor crime suppression in 2020 (consistent with reduced street activity during lockdowns), while others show elevated rates. The cross-city variation is large enough that broad claims about "outdoor crimes fell in 2020" are not reliably supported without city-by-city qualification. What the data do support more robustly:
- Domestic violence in Chicago dropped during the 2020 lockdown relative to the post-COVID baseline — consistent with reduced social activity rather than elevated co-presence. The cross-city picture (Figure 16b) is mixed, however, with some cities showing DV above baseline and others below, reflecting genuine differences in how lockdowns affected household dynamics and reporting practices.
- Burglary grew in 2020 relative to the post-COVID baseline in Chicago and consistently across all five cities in both graphs. This is the opposite of what the "residents working from home deter burglars" narrative would predict. A more likely explanation: lockdowns reduced police patrol capacity and shifted reporting thresholds, or the commercial-burglary category (which grew when empty shops became easy targets) dominates the residential category in these city-level counts.
- The cross-city variation (Figure 16b) confirms that local factors — enforcement policy, economic conditions, city-specific reporting practices — shape lockdown effects more than any single structural mechanism.

**Temperature–crime relationship:**
The size of the temperature effect (% swing from coldest to hottest days) is broadly **robust across the three periods**. Even during the 2020 lockdown, when street-level social activity was dramatically reduced, the direction of the temperature response held for most crimes. The magnitude in 2020 is less reliable given the disruption to normal patterns, but the persistence of the directional association — across a period when social activity was structurally suppressed — is consistent with the temperature–crime link reflecting something more than a pure confound with summer socialising.

**Weekend/holiday effects:**
The weekend effect weakened for retail-linked crimes (theft, robbery) during 2020, consistent with the collapse of commercial activity making the weekday/weekend distinction less meaningful. The DV weekend effect remained strong — co-presence is less contingent on whether shops are open.

---

### The Kia/Hyundai crime wave: a one-off event

The Chicago auto-theft data contains a prominent anomaly: rates jumped roughly 3× between 2021 and 2022 (from ~1.3 to ~3.7 per 100k), then partially normalised. This spike was concentrated in the months August–October 2022. All other cities in the dataset show auto-theft rates that track temperature seasonally (August peak); Chicago's October peak in the five-year average is an artefact of this single anomalous year.

The cause is known: in mid-2020, a TikTok/social-media video demonstrated a method for stealing Kia and Hyundai vehicles manufactured without immobilisers. Chicago was disproportionately affected due to its large population of these vehicles and its specific urban geography. This is a **crime-wave artefact**, not a weather-driven seasonal effect.

This example illustrates a critical limitation of aggregate weather–crime analysis: a single non-weather event can contaminate multiple years of data and produce spurious correlations or apparent phase shifts. When anomalous patterns emerge in the data, it is important to check for known one-off events before attributing them to weather or calendar factors.

The year-by-year auto-theft pattern is shown in Figure 7b above.

---



### The archetype fingerprints

Each archetype's unique combination of factor responses — its "fingerprint" — is summarised in the radar charts below. Each axis is one factor, normalised so the strongest effect across all archetypes reaches the edge. The further from the centre, the larger the effect relative to other crimes.

![Archetype radar fingerprints](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_06_archetype_radar.png)

*Figure 15. Radar chart of archetype factor fingerprints (raw rates). Each line represents the average factor profile for one archetype. In raw data, temperature dominates every profile and the archetypes appear superficially similar.*

![Archetype radar fingerprints — after heat removal](https://raw.githubusercontent.com/petr-salomoun/weather-crime/main/reports/narrative/figures/fig_06b_archetype_radar_post_heat.png)

*Figure 15b. Same radar chart after statistically removing the temperature component and retaining only non-thermal factors. The archetype fingerprints diverge visibly: Domestic Violence and Outdoor Aggression show little response to any residual factor; Sexual Assault responds strongly to holiday, discomfort, and precipitation; Theft shows a strong negative holiday effect; Opportunistic Crime retains a moderate weekend signal.*

### Summary table

| Archetype | Crimes | Primary driver | Key signature |
|---|---|---|---|
| **Outdoor Aggression** | Assault, Vandalism | Heat → irritability | Strong temperature; weekend; bar weather |
| **Opportunistic Crime** | Robbery, Burglary, Auto Theft | Victim absent from home/car | Burglary: Monday peak; auto theft: weekend peak |
| **Sexual Assault** | Sexual Assault | Heat → social occasion | Strong temperature; holiday peak; discomfort positive |
| **Theft** | Theft (General) | Commercial hours | Friday peak; Sunday −14%; holiday −19% |
| **Domestic Violence** | Domestic Violence | Co-presence time | Low weather sensitivity; weekend +19%; holiday +18% |

---

## Implications

These five archetypes carry different policy implications:

- **Reducing assault and vandalism on hot summer evenings** requires addressing both the heat-aggression link and the social context: cooling centres, modified alcohol licensing hours, and targeted street presence on high-risk nights.
- **Preventing burglary** involves signalling occupancy: lighting, engaged neighbours, and the visible cues that a property is not vacant. The consistent Monday peak across cities supports the occupancy-deterrence hypothesis directly.
- **Auto theft prevention** may benefit from targeting recreational destinations — parking lots at sports venues, parks, and transit hubs on weekends — alongside commuter locations on weekdays. The weekend peak in the aggregate data suggests recreational contexts are disproportionately represented, though any deployment decision should account for absolute volume, not just rates.
- **Sexual assault prevention** centres on the social occasions where it occurs: event safety measures, adequate venue staffing, alcohol-aware programming, and information campaigns — especially around major holidays.
- **Retail theft** follows shop hours, not weather. Physical security, staffing levels, and deterrence at high-foot-traffic commercial times (Friday afternoons, pre-holiday periods) matter more than summer patrol increases.
- **Domestic violence** interventions need to focus on the calendar of co-presence, not the thermometer. Holiday and weekend programmes — hotlines, support access, third-party intervention — are the right levers.

The same summer heat wave is a completely different event depending on which crime you are trying to prevent. Recognising this distinction should change how resources are allocated across time and space.

---

## Data and Code

- **Crime data:** Open police incident portals, Chicago, Houston, Los Angeles, New York City, Philadelphia (2020–2024)
- **Weather:** NOAA GHCN-Daily, nearest station match per city
- **Pipeline:** Python (DuckDB, pandas, scikit-learn, matplotlib)
- **Analysis scripts:** `analysis/notebooks/exploratory/hypotheses/fig_crime_fingerprints_v{4,5,6}.py`, `fig_auto_theft_calendar.py`, `fig_archetype_cross_city.py`, `fig_dv_vs_street_crime_anticorrelation.py`, `fig_covid_era_comparison.py`
- **This report's figures:** `reports/narrative/gen_narrative_figures.py` (figs 01–10, A–C)
- **Technical companion:** `reports/narrative/weather_crime_technical.md`

*For methodological details, PCA results, effect-size tables, and limitations see the technical companion document.*

---

*Prepared April 2026*

---

## Licence

This report and all figures are released under a permissive licence: free to use for any purpose. Publication or redistribution requires attribution to **Petr Salomoun** (petr.salomoun@gmail.com).