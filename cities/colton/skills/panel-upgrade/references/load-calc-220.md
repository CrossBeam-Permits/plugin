---
title: "CEC 220.83(A) — Service Load Calculation for Panel Upgrades"
category: "Load Calculations"
relevance: "Panel upgrade reviews where target service size must be verified against calculated load"
key_code_sections: "CEC 220.83(A), 220.83(B), 230.42, 230.79"
---

# CEC 220.83 — Optional Calculation for Existing Dwelling Units

Source: 2025 California Electrical Code (Title 24, Part 3), Articles 220 and 230.

This is the standard method for determining the required service size when upgrading a residential panel. It applies to **existing dwelling units** with 120/240V or 208Y/120V, 3-wire service.

For panel upgrades, the question is: **is the target panel size large enough for the calculated total service load?**

---

## 220.83(A) — Without Additional A/C or Space Heating

Use this method when upgrading a panel for a home that is NOT simultaneously adding central A/C or electric space heating.

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
| Pool / spa equipment | Nameplate rating |
| EV charger (if present/planned) | Nameplate rating (volts x amps) |
| Any other permanently connected loads | Nameplate rating |

### Step 2: Apply Demand Factors

| Load Portion | Demand Factor |
|-------------|---------------|
| First 8,000 VA (8 kVA) | **100%** |
| All remaining VA | **40%** |

> **City worksheet discrepancy**: Some cities (including Buena Park) use "first 10,000 watts at 100%" on their load calc worksheet instead of the CEC's "first 8 kVA at 100%." The city's version is slightly more conservative (counts more load at the full rate). **When reviewing for a specific city, use the city's threshold if they provide a worksheet.** When no city worksheet exists, use the CEC 8,000 VA threshold.

### Step 3: Calculate Total Service Load

```
Total General Load = Sum of all loads from Step 1
Calculated Load = First 8,000W at 100% + (Remainder x 40%)
                = 8,000 + ((Total General Load - 8,000) x 0.40)
```

### Step 4: Determine Minimum Panel Size

Convert calculated load to amperes:
```
Minimum Amperes = Calculated Load (watts) / 240 volts
```

Then check: **Target panel amperage must be >= calculated minimum amperes.**

---

## 220.83(B) — With Additional A/C or Space Heating

Use this method when the panel upgrade also involves adding or upgrading central A/C or electric space heating.

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

Based on CEC 220.83(A), 230.42, and Annex D:

| Total Calculated Service Load (Watts) | Minimum Service Panel (Amps) |
|---------------------------------------|------------------------------|
| Up to 24,000 | 100A |
| 24,001 - 30,000 | 125A |
| 30,001 - 36,000 | 150A |
| 36,001 - 48,000 | 200A |
| 48,001 - 54,000 | 225A |
| 54,001 - 72,000 | 320A |
| Over 72,000 | 400A |

**The target panel size must be EQUAL TO or LARGER than the minimum required.**

---

## Worked Example: 200A Panel Upgrade for Typical Home

**Given**: 1,800 sq ft home, currently 100A panel, upgrading to 200A. Gas heating, A/C (6,000W), electric water heater (4,500W), electric dryer (5,000W), adding EV charger (9,600W).

**Step 1 — List loads:**

| Load | Watts |
|------|-------|
| General lighting: 1,800 x 3 | 5,400 |
| Kitchen circuits (2 x 1,500) | 3,000 |
| Laundry circuit | 1,500 |
| Water heater | 4,500 |
| Clothes dryer | 5,000 |
| A/C | 6,000 |
| EV charger (240V x 40A) | 9,600 |
| **Total General Load** | **35,000** |

**Step 2 — Apply demand factors (220.83(B), since including A/C):**

| Portion | Calculation | Result |
|---------|------------|--------|
| A/C (larger of A/C or heating) | 6,000 x 100% | 6,000 |
| First 8,000 of other loads | 8,000 x 100% | 8,000 |
| Remaining other loads | (29,000 - 8,000) x 40% | 8,400 |
| **Total Calculated Load** | | **22,400W** |

**Step 3 — Minimum panel size:**
- 22,400W / 240V = 93.3A -> **100A minimum**
- Target 200A panel: **PASS** (200A >> 100A needed)

**Why upgrade to 200A if 100A is sufficient?** The load calc shows current loads fit in 100A. But the upgrade provides headroom for:
- Future EV charger additions
- Heat pump conversion (electrification)
- Kitchen remodel with electric range
- General load growth

The load calc confirms the upgrade is not undersized — it does not prevent oversizing.

---

## Worked Example: Undersized Panel Upgrade (FAIL Case)

**Given**: 2,400 sq ft home, upgrading from 60A to 100A. All-electric: electric furnace (10,000W), electric water heater (4,500W), electric dryer (5,000W), electric range (12,000W), A/C (6,000W).

**Step 1 — List loads:**

| Load | Watts |
|------|-------|
| General lighting: 2,400 x 3 | 7,200 |
| Kitchen circuits (2 x 1,500) | 3,000 |
| Laundry circuit | 1,500 |
| Electric range | 12,000 |
| Water heater | 4,500 |
| Clothes dryer | 5,000 |
| Electric furnace | 10,000 |
| A/C | 6,000 |
| **Total General Load** | **49,200** |

**Step 2 — Apply demand factors (220.83(B)):**

| Portion | Calculation | Result |
|---------|------------|--------|
| Electric furnace (larger of heating or A/C) | 10,000 x 100% | 10,000 |
| First 8,000 of other loads | 8,000 x 100% | 8,000 |
| Remaining other loads | (39,200 - 8,000) x 40% | 12,480 |
| **Total Calculated Load** | | **30,480W** |

**Step 3 — Minimum panel size:**
- 30,480W / 240V = 127A -> **125A minimum**
- Target 100A panel: **FAIL** (100A < 125A needed)
- **Correction**: Must upgrade to at least 125A (150A or 200A recommended)

---

## Minimum Service Disconnect Ratings (230.79)

| Installation Type | Minimum Rating |
|------------------|---------------|
| One-circuit installations | 15A |
| Two-circuit installations | 30A |
| **One-family dwelling** | **100A, 3-wire** |
| All other installations | 60A |

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
| Electric range (combined) | 12,000 |
| Microwave | 1,500 |
| Garbage disposal | 1,000 |
| Dishwasher | 3,500 |
| Garbage compactor | 1,000 |
| Instant hot water (at sink) | 1,500 |
| Electric clothes dryer | 4,500 |
| Central heating (gas) + A/C | 6,000 |
| Window A/C | 1,000 |
| Whole-house / attic fan | 500 |
| Central electric furnace | 8,000 - 15,000 |
| Heat pump | 6,000 - 12,000 |
| Evaporative cooler | 500 |
| Electric water heater (storage) | 4,000 - 4,500 |
| Electric tankless water heater | 18,000 - 36,000 |
| Swimming pool pump | 2,000 - 3,000 |
| Pool/spa heater (electric) | 4,000 - 11,000 |
| EV charger (Level 2, 40A) | 9,600 |
| EV charger (Level 2, 48A) | 11,520 |
| EV charger (Level 2, 60A) | 14,400 |

**Note on tankless water heaters**: Electric tankless units draw 18,000-36,000W — they are one of the most load-intensive residential appliances and frequently trigger the need for a panel upgrade to 200A or higher.
