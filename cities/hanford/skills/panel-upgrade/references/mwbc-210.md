---
title: "CEC Article 210 — Multiwire Branch Circuit (MWBC) Requirements"
category: "Branch Circuits"
relevance: "Panel upgrade reviews where existing MWBCs must be properly reconnected in new panel"
key_code_sections: "CEC 100 (MWBC definition), 210.4(A), 210.4(B), 200.4(B), 200.4(B)(2), 240.15(B)(1), 300.13(B)"
---

# CEC Article 210 — Multiwire Branch Circuits (MWBCs)

Source: 2025 California Electrical Code (Title 24, Part 3), Articles 100, 200, 210, 240, and 300.

Multiwire branch circuits are common in older residential wiring and must be properly reconnected during a panel upgrade. Incorrect reconnection of MWBCs can cause dangerous overloading of the neutral conductor. This is a critical inspection item.

---

## What Is a Multiwire Branch Circuit?

### CEC Article 100 — Definition

A **multiwire branch circuit** is a branch circuit that consists of:
- **Two or more ungrounded (hot) conductors** that have a **voltage potential between them** (i.e., they originate from different poles/phases)
- A **common neutral conductor** (grounded conductor)

In a standard 120/240V residential panel, this means:
- The two hot conductors must be on **opposite legs** (Line A and Line B)
- They share one neutral
- The neutral carries only the **difference** in current between the two hots (not the sum)

**Why this matters for panel upgrades**: When moving circuits from the old panel to the new panel, the two hot conductors of an MWBC must end up on **opposite legs**. If both hot wires land on the same leg, the neutral can be dangerously overloaded.

---

## MWBC Requirements

### 210.4(A) — Same Panel

All conductors of a multiwire branch circuit shall originate from the **same panelboard or distribution equipment**. You cannot split an MWBC across two panels.

### 210.4(B) — Simultaneous Disconnect

All ungrounded conductors of a multiwire branch circuit shall be provided with a means that will **simultaneously disconnect all ungrounded conductors** at the point where the circuit originates.

| Method | Acceptable? |
|--------|-------------|
| **2-pole breaker (common trip)** | Yes — preferred method |
| **Two single-pole breakers with approved handle tie** | Yes — but only for MWBCs that serve **line-to-neutral loads only** |
| **Two separate single-pole breakers (no tie)** | **NO** — violates 210.4(B) |

*Per CEC 210.4(B) and 240.15(B)(1)*

---

## Neutral Handling for MWBCs

### 200.4(B) — Grouping and Identification

Where more than one MWBC (or combination of MWBCs and regular circuits) passes through a junction box, the neutral of each MWBC shall be **identified or grouped** with its associated ungrounded conductors by:
- Cable assemblies (wires already grouped in the same cable)
- Wire ties or tape at each junction box
- Labeling

### 200.4(B)(2) — Without Loops or Splices

The identification or grouping must be done in a manner that does not require loops or splices to determine which neutral belongs to which circuit.

### 300.13(B) — Neutral Pigtail Requirement

The continuity of a neutral conductor shall **not depend on a connected device** (receptacle or switch). This means:

- At each device box, the MWBC neutral must be **pigtailed** (spliced with a short jumper to the device)
- The neutral must **NOT** be wired as a feed-through (daisy-chained through the device terminal screws)
- If the device is removed, the neutral must remain continuous

**Why**: If a receptacle in a feed-through configuration is removed, the neutral is broken for downstream outlets. On an MWBC, this means the remaining hot circuit has no neutral return path, causing dangerous voltage to appear on connected equipment.

---

## Common MWBC Violations During Panel Upgrades

1. **Both hots on the same leg** — neutral overloaded; no net cancellation of current
2. **No handle tie or 2-pole breaker** — circuits cannot be simultaneously disconnected for maintenance
3. **Neutral feed-through at devices** — neutral continuity depends on device connection
4. **MWBC not identified** — inspector cannot verify proper pole placement without grouping/labeling
5. **Shared neutral between non-MWBC circuits** — two circuits on the same leg sharing a neutral (overload)

---

## How to Verify MWBCs During Panel Upgrade Review

1. **Identify all MWBCs** in the existing wiring — look for 12/3 or 14/3 NM cable, or 3-conductor + ground in conduit
2. **Confirm opposite legs** — the two hots must connect to breakers on alternating bus stabs (opposite phases)
3. **Verify simultaneous disconnect** — 2-pole breaker or approved handle tie
4. **Check neutral pigtails** — downstream devices should not rely on feed-through neutral connections
5. **Confirm grouping** — if multiple MWBCs exist, each must be identifiable at the panel
