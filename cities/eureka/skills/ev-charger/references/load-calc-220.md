---
title: "CEC 220.83(A) — Service Load Calculation for Existing Dwellings"
category: "Load Calculations"
relevance: "EV charger reviews where panel capacity must be verified"
key_code_sections: "CEC 220.83(A), 220.83(B), 230.42, 230.79"
---

# CEC 220.83 — Optional Calculation for Existing Dwelling Units

Source: 2025 California Electrical Code (Title 24, Part 3), Articles 220 and 230.

This is the standard method for determining whether an existing residential service panel has sufficient capacity for an added EV charger load. It applies to **existing dwelling units** with 120/240V or 208Y/120V, 3-wire service.

---

## 220.83(A) — Without Additional A/C or Space Heating

Use this method when adding an EV charger to an existing home and NOT simultaneously adding central A/C or electric space heating.

### Step 0: VERIFY THE APPLICANT'S ADDITION

> **CRITICAL**: Before applying demand factors, **independently add up every line item** the applicant checked on the load calc worksheet. Do NOT trust their stated "Total General Load." Applicants frequently make arithmetic errors. Write out the full addition, compare to their stated total, and flag any discrepancy. Even if the final panel sizing result doesn't change, the form must be accurate before permit issuance.

### Step 1: List All Loads

| Load Type | How to Calculate |
|-----------|-----------------|
| General lighting & receptacles | 3 VA per square foot of dwelling |
| Small-appliance branch circuits | 1,500 VA per 20A kitchen/dining circuit (minimum 2 circuits) |
| Laundry branch circuit | 1,500 VA |
| All fastened-in-place appliances | Nameplate rating |
| Range / oven / cooktop | Nameplate rating |
| Clothes dryer | Nameplate rating |
| Water heater | Nameplate rating |
| **EV charger** | **Nameplate rating (volts × amps)** |

### Step 2: Apply Demand Factors

| Load Portion | Demand Factor |
|-------------|---------------|
| First 8,000 VA (8 kVA) | **100%** |
| All remaining VA | **40%** |

> **City worksheet discrepancy**: Some cities (including Buena Park) use "first 10,000 watts at 100%" on their load calc worksheet instead of the CEC's "first 8 kVA at 100%." The city's version is slightly more conservative (counts more load at the full rate). **When reviewing for a specific city, use the city's threshold if they provide a worksheet.** When no city worksheet exists, use the CEC 8,000 VA threshold.

### Step 3: Calculate Total Service Load

```
Total General Load = Sum of all loads from Step 1
Calculated Load = First 8,000W at 100% + (Remainder × 40%)
                = 8,000 + ((Total General Load - 8,000) × 0.40)
```

### Step 4: Determine Minimum Panel Size

Convert calculated load to amperes:
```
Minimum Amperes = Calculated Load (watts) ÷ 240 volts
```

Then check: **Existing panel amperage must be ≥ calculated minimum amperes.**

---

## 220.83(B) — With Additional A/C or Space Heating

Use this method when adding BOTH an EV charger AND central A/C or electric space heating.

### Demand Factors

| Load | Demand Factor |
|------|---------------|
| Air-conditioning equipment | **100%** |
| Central electric space heating | **100%** |
| Less than 4 separately controlled space-heating units | **100%** |
| First 8,000 VA of all other loads | **100%** |
| Remainder of all other loads | **40%** |

**Important**: Use the LARGER of air conditioning or space heating — not both (they are unlikely to operate simultaneously).

---

## Service Panel Sizing Table

Based on CEC 220.83(A), 230.42, and Annex D. This maps total calculated service load to minimum panel size:

| Total Calculated Service Load (Watts) | Minimum Service Panel (Amps) |
|---------------------------------------|------------------------------|
| Up to 24,000 | 100A |
| 24,001 – 30,000 | 125A |
| 30,001 – 36,000 | 150A |
| 36,001 – 48,000 | 200A |
| 48,001 – 54,000 | 225A |

**The existing panel size must be EQUAL TO or LARGER than the minimum required.**

If not: **flag for panel upgrade** — do not reject the permit outright, but note that a panel upgrade is needed.

---

## Worked Example: Adding 40A EV Charger to Existing Home

**Given**: 1,800 sq ft home, 200A existing panel, gas heating/cooking, electric water heater (4,500W), A/C (6,000W), electric dryer (5,000W), adding 40A (9,600W) EV charger.

**Step 1 — List loads:**

| Load | Watts |
|------|-------|
| General lighting: 1,800 × 3 | 5,400 |
| Kitchen circuits (2 × 1,500) | 3,000 |
| Laundry circuit | 1,500 |
| Water heater | 4,500 |
| Clothes dryer | 5,000 |
| A/C | 6,000 |
| **EV charger (240V × 40A)** | **9,600** |
| **Total General Load** | **35,000** |

**Step 2 — Apply demand factors (220.83(B), since adding with A/C):**

| Portion | Calculation | Result |
|---------|------------|--------|
| A/C (larger of A/C or heating) | 6,000 × 100% | 6,000 |
| First 8,000 of other loads | 8,000 × 100% | 8,000 |
| Remaining other loads | (29,000 - 8,000) × 40% | 8,400 |
| **Total Calculated Load** | | **22,400W** |

**Step 3 — Minimum panel size:**
- 22,400W ÷ 240V = 93.3A → **100A minimum**
- Existing 200A panel: **PASS**

---

## Minimum Service Disconnect Ratings (230.79)

| Installation Type | Minimum Rating |
|------------------|---------------|
| One-circuit installations | 15A |
| Two-circuit installations | 30A |
| **One-family dwelling** | **100A, 3-wire** |
| All other installations | 60A |

---

## Service-Entrance Conductor Sizing (230.42)

Service-entrance conductors shall have ampacity not less than the maximum load to be served. Sized as the largest of:

1. **Noncontinuous loads + 125% of continuous loads**
   - Since EV charging is continuous: service conductors must handle the continuous load at 125%
2. **Maximum load after applying adjustment/correction factors** from Table 310.16

---

## Common Residential Loads Reference

Use these typical wattages when specific nameplate data is unavailable:

| Appliance | Typical Watts |
|-----------|--------------|
| House (per sq ft) | 3 VA/sq ft |
| Kitchen circuits (each) | 1,500 |
| Laundry circuit | 1,500 |
| Electric oven | 2,000 |
| Electric stovetop | 5,000 |
| Microwave | 1,500 |
| Garbage disposal | 1,000 |
| Dishwasher | 3,500 |
| Garbage compactor | 1,000 |
| Instant hot water (at sink) | 1,500 |
| Electric clothes dryer | 4,500 |
| Central heating (gas) + A/C | 6,000 |
| Window A/C | 1,000 |
| Whole-house / attic fan | 500 |
| Central electric furnace | 8,000 |
| Evaporative cooler | 500 |
| Electric water heater (storage) | 4,000 |
| Electric tankless water heater | 4,000 |
| Swimming pool or spa | 4,000 |

### EV Charger Wattage by Amperage

| Circuit Amperage | Charger Load (240V) |
|-----------------|-------------------|
| 20A circuit → 16A continuous | 3,840W |
| 30A circuit → 24A continuous | 5,760W |
| 40A circuit → 32A continuous | 7,680W |
| 50A circuit → 40A continuous | 9,600W |
| 60A circuit → 48A continuous | 11,520W |
| 70A circuit → 56A continuous | 13,440W |
