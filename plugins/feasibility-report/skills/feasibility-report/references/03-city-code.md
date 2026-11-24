# Step 3: City code

## 1. Read the city's own rules

1. Call `crossbeam_municipal_code` with `city` alone for the chapter index. Pick the chapters this project turns on: the zone's development standards, the chapters the profile's **Questions** table names (the ADU section, the use table, nonconforming structures, grading, signs), parking, and the procedure for this permit.
2. Call it again with each `chapter` (or `section`). Read the text; a long chapter comes back in pages.
3. Note the "codified through" date and any adopted-but-not-codified ordinances the answer lists. An ordinance listed there may change a section: add it to the City questions if it touches this project.
4. Cite each rule under that city's own code name and section, for example "Example City Municipal Code § 17.28.020(E)(4)". Never put one city's abbreviation on another city's section.

Each rule you read here is `CODE`. Your reading of how it applies to this lot is `INFERRED` unless the text decides it outright.

For each question in the profile, find the city rule if there is one, and for each limit note the number you will put in the fit table (`07-report.md` section 3). Always find the review path (ministerial or discretionary, which departments) and any decision timeline.

## 2. When CrossBeam has no code for this city

The tool returns the list of cities it has instead. A missing city is a gap in CrossBeam, not a missing law. Find the local law yourself, then use CrossBeam's state law to check it and fill around it.

1. **Say it plainly** in the sources line: "CrossBeam does not yet have <city>'s municipal code."
2. **Find the local law** (`find-local-law.md`). If your host can search the web or fetch pages, find the city's own code text, its adopted building code amendments and its handouts. Read the section text. A rule read from the official published text is `CODE`, with the publisher, the "current through" date and the date you read it in the sources list. A summary, blog or law-firm note is never `CODE`: tag what it says `INFERRED` and say where it came from.
3. **If you cannot search,** ask the person for the city's code link or the section text, or carry each city rule as a City question.
4. **Use state law either way** (section 4 below): it sets what the city must allow and what it may not require, so it decides many questions even when the city text is missing, and it is the test for a local rule you did find.
5. **Ask `crossbeam_ask` the city question too** (`06-synthesize.md`). It may know the city from CrossBeam's own notes, but an Ask answer about city law is a cross-check, not the code.

## 3. Preemption is a judgment, not a rule of thumb

In California, state ADU and housing law sets a floor that a city cannot go below, and a city rule more restrictive than state law can be void. Do not decide this by "stricter wins" or "state wins". Read both texts, say which one controls and why, and tag your conclusion `INFERRED` unless a statute or an HCD letter (`crossbeam_hcd_letters`) says it about this city's rule. Other states have their own rules: read the state's text before you say a local rule does not apply.

## 4. Use state law when the city layer is thin

CrossBeam holds state law (`crossbeam_lookup_code`, and in California `crossbeam_hcd_letters`) for every city in a covered state, including the cities it has no local data for. Use it on every question, and most of all when the city's own text is missing or uncertain:

1. **State floors decide by themselves.** Where state law says what a city must allow (a minimum unit size, a setback the city may not exceed, parking it may not require near transit, a review it must make ministerial, a decision deadline), that answer holds whatever the city code says. Report it as `CODE` with the state section, and say "the City may set a more permissive rule; it may not go below this".
2. **State ceilings limit what the city can add.** Where state law caps a local rule (fees, standards the city may apply, approvals it may require), say so and test any local rule you found against it (section 3).
3. **State codes fill building questions.** Most building, fire, energy and accessibility requirements come from the state's adopted codes, with local amendments on top. When you have the state code section but not the city's amendments, report the state rule as `CODE` and add "Does the City amend <section>?" to the City questions.
4. **Say which layer is unknown.** When only the city layer is missing, the card says what state law guarantees, then "City rule not read: <how to get it>". Never fill the gap with a typical value from another city.
5. **Compare what you found.** When you found the local rule outside CrossBeam, compare it with the state text you read: the same, more permissive (fine), or more restrictive (may be preempted, section 3). Say which in the card.
