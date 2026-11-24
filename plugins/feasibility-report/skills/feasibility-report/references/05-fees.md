# Step 5: Fees

## 1. Ask CrossBeam for an estimate

Call `crossbeam_fees` with `city`, `permit_type` (for example `adu`, `new_sfr`, `remodel`) and what you know: `adu_sqft` or `new_floor_area_sqft`, `primary_dwelling_sqft` for an ADU over 750 sf, `new_dwelling_units`, `address`, `stories`. Pass a `valuation` only if the person gave one. Answer the fee questions it returns if the facts are in hand, or list them under the City questions.

Report the subtotal, the schedule's effective date and source, and the fees set at intake (named, never priced). Tag each line `CROSSBEAM` with the schedule it cites. Say "estimate"; the City sets the final fees.

## 2. When CrossBeam has no fee schedule

`coverage: "none"` means CrossBeam has no fee schedule for that city. Then:

1. Say it plainly: "CrossBeam does not have <city>'s fee schedule."
2. Give the parts state law sets, each only after you read it (`04-state-law.md`): for example, when impact fees may be charged on an ADU and how they scale with size, and school district fees for residential area over a threshold. Tag each `CODE` with its section. Do not price a line you have no schedule for.
3. Say how to get the fees:
   - If your host can search the web, find the city's adopted fee schedule and the school district's developer fee rate (`find-local-law.md` section 2). Price from it, cite it with its date, and tag those lines `INFERRED` until the City confirms, since you are applying a schedule CrossBeam has not checked.
   - Otherwise, the person asks the City's Building counter for a fee estimate for this program, and the school district for its fee per square foot.
4. Add "Fee estimate for <program>: plan check, permit, impact, school and utility connection fees" to the City questions.
5. If the person gave a field estimate (for example "$10k+"), keep it as `FIELD` and say whether what you found supports it.

## 3. Fees that depend on timing

If a law that starts later changes a fee (`04-state-law.md` section 3), say which filing date gets which rule, and ask the City whether fees lock at application or at permit issuance.
