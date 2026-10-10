# Laguna Beach — Commercial Zoning Use-Routing (the "WHAT" layer)

## How to use this table

1. Get the parcel's zone from `lookup_property`. If the parcel is in the Downtown Specific Plan (CBD districts), use the DSP section below, not the zone rows.
2. Classify the tenant's use from the plans and application. Match it to the closest listed use. The zone chapters list uses by name; a use that is not listed is not permitted by right.
3. Read the cell. Then open the cited section with `lookup_municipal_code` (chapter 25.18, 25.19, 25.20, 25.21, 25.25, 25.32 or 25.40) and confirm the wording before you answer. Conditions sit in the section text (enclosed building, floor limits, Main Beach alcohol rule).
4. Restaurant and bar scopes: this table says only whether the use is allowed. Review the work under the `restaurant-ti` skill.
5. A use change also needs a Zone Clearance (§25.05.045(B)(2)), and a CDP if the new use needs more parking than the prior legal use (intensification of use, §25.07.006). See `coastal-development-permit.md`.

**Legend.** P = permitted by right. CUP = Conditional Use Permit, Planning Commission (§25.05.030). AUP = Administrative Use Permit (§25.05.020). "Not listed" = not permitted by right; every zone except M-1A lets the Planning Commission approve, by CUP after a public hearing, a use it finds "similar to and no more obnoxious or detrimental" than a listed use (LB/P §25.18.004(Z); C-N §25.19.006(N); C-1 §25.20.006(R); CH-M §25.21.004(A)(6) with a hotel; SLV §25.25.006(O)). Present that as a possible route, never as likely. M-1A prohibits "All uses not specifically listed" (§25.32.004(A)) except its own similar-use CUP (§25.32.003(L)).

**Source and limits.** Use lists are from the codified LBMC (eCode360, codified through 2026-04-28; the City source document (not included in this plugin)). Ord. 1732 did not amend these use lists (the City source document (not included in this plugin)). Ord. 1730 was adopted 2026-07-21 but is not yet codified; if it touches a use list, the corpus does not show it. Confirm the cell with Planning at pre-application; the table is the answer, the confirmation is a caveat.

## Zones

LB/P = Local Business-Professional (Ch. 25.18). C-N = Commercial Neighborhood (Ch. 25.19). C-1 = Local Business District (Ch. 25.20). CH-M = Commercial Hotel-Motel (Ch. 25.21). SLV = South Laguna Village Commercial (Ch. 25.25). M-1A = Light Industrial (Ch. 25.32).

| Use | LB/P (25.18) | C-N (25.19) | C-1 (25.20) | CH-M (25.21) | SLV (25.25) | M-1A (25.32) |
|---|---|---|---|---|---|---|
| General retail store or shop | CUP (.004(A), (F) clothing, (C) books) | P (.002(F), (Z), (AA)) | P, enclosed building (.004(A)) | CUP, only as ancillary retail with a hotel/motel (.004(A)(1)) | P (.002(F), (T)) | Prohibited, except incidental sales up to 10% of floor area of a permitted industrial use (.002(E)(3); .004(C)) |
| Business or professional office | P (.002(D)) | P (.002(D)) | Above ground floor only: CUP, max 50% of the building's gross floor area (.006(S)(7)). Ground floor: not listed | Not listed | P (.002(N)); converting ground-floor retail to office: CUP (.006(D)) | CUP, not medical, sole access not from a primary road (.003(B)); P if related to a permitted industrial use (.002(E)(4)) |
| Medical or dental office or clinic | P (.002(B)) | P (.002(Q)) | Above ground floor only: CUP, max 50% (.006(S)(4)) | Not listed | P (.002(N)); ground-floor retail conversion: CUP (.006(D)) | Not permitted (excluded in .003(B)) |
| Personal service (barber, beauty, nail; "day spa" is named only in SLV) | P (.002(A)) | P (.002(U)) | P (.004(A)(2)) | CUP with a hotel/motel (.004(A)(2)) | P (.002(D)) | Not listed |
| Massage establishment | Not listed | Not listed | CUP (.006(K)) | Not listed | Not listed | Not listed |
| Health club, gym, fitness studio | P (.002(G)) | CUP (.006(E)) | CUP, "Recreation facilities, all" (.006(L)) | CUP with a hotel/motel, "Recreational facilities" (.004(A)(3)) | CUP (.006(K)) | CUP, "Country clubs or recreation facilities, all" (.003(A)) |
| Sit-down cafe or restaurant, no alcohol | CUP (.004(J)) | P (.002(E)) | P, no dancing or entertainment (.004(A)(3)) | CUP, only incidental to a hotel/motel (.004) | CUP (.006(A)) | Not listed (lunch room only as incidental to industry, .002(F)(6)) |
| Take-out restaurant | CUP (.004(J)) | CUP (.006(C)) | CUP (.006(F)) | Not listed | CUP (.006(A)) | Not listed |
| Restaurant or bar serving alcohol, or with entertainment | CUP (.004(K), (L)) | CUP (.006(B)) | CUP (.006(C), (H)) | CUP, incidental to a hotel/motel (.004) | CUP (.006(A)) | Not listed |
| Drive-in restaurant | Not permitted (.004(J)) | Not permitted (.002(E)) | CUP (.006(G)) | Not listed | Not listed | Not listed |
| Market or grocery | CUP (.004(N)) | P (.002(P)) | P (.004(A)(6)) | Not listed | CUP (.006(B)) | Not listed |
| Liquor sales (off-sale) | CUP (.004(O)) | CUP (.006(J)) | Off-sale alcohol prohibited within 200 yards of Main Beach (.004(A)); otherwise not listed as its own use | Off-sale alcohol limit near Main Beach also stated (.004) | CUP (.006(G)) | Not listed |
| Bank or financial office | CUP (.004(I)) | P (.002(I)); CUP in the Commercial/Tourist Corridor (see note) | Not listed | Not listed | P (.002(B)) | Not listed |
| Art gallery or art studio | CUP (.004(P), (Q)) | P (.002(A)) | Photographic galleries P (.004(A)(7)); studios CUP above ground floor (.006(S)(12)) | Not listed | P (.002(A)) | Artists' studios P (.002(F)(1)) |
| Dry cleaning or laundry | P (.002(F)) | P (.002(O)) | Self-service laundry P (.004(A)(5)) | Not listed | CUP (.006(C)) | Cleaning plant P (.002(B)(3)) |
| Pet grooming | CUP (.004(S)) | P (.002(V)); CUP in the Corridor | Not listed | Not listed | P (.002(Q)) | Not listed |
| Veterinary clinic or animal hospital | Not listed | CUP (.006(I)) | Not listed | Not listed | CUP (.006(E)) | Small animal hospital P (.002(F)(2)) |
| Church or religious assembly | CUP (.004(V)) | Not listed | CUP (.006(D)) | Not listed | Not listed | Not listed |
| School (business, music, dance) | Nursery school CUP (.004(U)) | Not listed | Public and private schools CUP (.006(M)); business colleges and music/dance schools CUP above ground floor (.006(S)(1), (5)) | Not listed | Not listed | Not listed |
| Child day care | P (.002(M)) | Not listed | Nursery schools CUP above ground floor (.006(S)(6)) | Not listed | Not listed | Not listed |
| Auto repair | Not listed | Not listed | CUP, enclosed building (.006(B)) | Not listed | Not listed | P, enclosed building (.002(E)(1)) |
| Light manufacturing, warehouse, storage | Not listed | Not listed | Not listed | Not listed | Not listed | P (.002(A), (C)) |
| Short-term lodging | AUP (.006) | AUP (.004(A)) | AUP (.005(A)) | AUP (.005) | CUP (.006(L)) | Not listed |

**C-N Commercial/Tourist Corridor (§25.19.007).** Where a C-N parcel is in the Land Use Plan's Commercial/Tourist Corridor, financial offices, packaging and postal services, copy services, pet grooming and trade services need a CUP, and "the use shall not exceed fifty percent of the gross floor area of the entire structure and shall be located above the ground floor level." Check the Land Use Plan designation, not just the zone.

**LB/P Three Arch Bay commercial area (§25.18.010).** The LB/P area on South Coast Highway next to Three Arch Bay has its own use list. Read §25.18.010 instead of the LB/P column.

**Other zones.** Uses in the Laguna Canyon Annexation Specific Plan (Ch. 25.48), Lagunita (Ch. 25.24), Institutional (Ch. 25.28) and other districts are not in this table. Open the chapter with `lookup_municipal_code` and read its uses permitted and CUP sections; if a use is not there, route the question to Planning without a verdict.

## Downtown Specific Plan (Ch. 25.40)

The DSP districts (CBD-1, CBD-2, CBD Visitor Commercial, CBD Office, CBD MFR, CBD Public Parks, Arts, CBD Central Bluffs) use DSP Table 5-1, incorporated by §25.40.030. A transcription is at the City source document (not included in this plugin) (2022 certified DSP; the retail table there is a selection, not the full table). Rule: "Land uses not listed in Table 5-1 are not allowed except as deemed by the Planning Commission via CUP to be similar to and no more obnoxious or detrimental than a listed use."

Common rows from that transcription (confirm against Table 5-1 before relying on them):

| Use | CBD-1 | CBD-2 | CBD VC | CBD Office | Arts | CBD CB |
|---|---|---|---|---|---|---|
| Office, ground floor | CUP | CUP | Not allowed | P | CUP | Not allowed |
| Office, second floor | P | P | P | P | P | P |
| Medical, dental, clinics | P | CUP | CUP | P | Not allowed | Not allowed |
| Health club, spa, fitness center | CUP | CUP | Not allowed | Not allowed | Not allowed | Not allowed |
| Restaurant with waiter service, no alcohol | P | P | P | CUP | P | CUP |
| Restaurant with alcohol, live entertainment or dancing | CUP | CUP | CUP | CUP | CUP | CUP |
| Massage, therapeutic | CUP | CUP | CUP | CUP | CUP | CUP |
| Personal services | P | P | CUP | P | P | CUP |
| Clothing, shoes, accessories | CUP | P | P | Not allowed | P | CUP |
| Cannabis retail | Not allowed | Not allowed | Not allowed | Not allowed | Not allowed | Not allowed |

**Spas in the DSP: use the "Health club, spa, fitness center" row, not "Personal services".** Table 5-1 lists "Health Club, Spa, Fitness Center" as its own use (CUP in CBD-1 and CBD-2, not allowed elsewhere), so a day spa, med spa or wellness spa downtown takes that row. A specific row governs a general one; "Personal services" covers barber, beauty and nail shops. Outside the DSP, only SLV names a "day spa" (25.25.002(D), with barber, beauty and nail salons); in the other zones a spa is not named, so say whether it reads as a personal service shop or a recreation or health facility is the Director's call, and confirm at pre-application. Therapeutic massage is its own row in both tables.

Table 5-1 footnotes (a), (b), (c), (g) and the caps (15 ice cream/dessert shops, 20 branded stores in the DSP) carry conditions; read them in the source before answering.
