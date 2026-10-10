# Portal account

Every online Laguna filing needs a City permit-portal account. Applying, paying invoices, tracking status, requesting inspections, and the dashboard all sit behind sign-in; the catalog and public record search are readable without it. [1]

The applicant creates and uses the account. The agent explains the steps and waits. It never types, reads, stores, or replays a password, verification code, MFA prompt, passkey, or social-login consent.

## Before signing up: pick one email

The portal's sign-in is **Tyler Identity**, Tyler's hosted login, not a City login. The portal's `#/registration` page redirects to it. [1]

The City's registration guide warns: if the applicant signs in with Google, Apple, Microsoft, or Facebook using a personal email, and uses a business email for the portal, **the accounts will not link**. [1]

So, before anyone creates an account, ask:

- Which email should own this permit? Contractors usually want the business email; homeowners usually want their own.
- Does that person already have a Laguna portal account? If so, use it. Do not create a second one.

Tell the applicant to use that one email for every step and every later sign-in.

## Sign-up steps (the applicant does each one)

1. Open the City portal at `https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/home` and choose Login or Register. [1]
2. Either sign in with a social account whose email is the chosen email, or choose Create an Account and enter the chosen email and a password. [1]
3. Enter the verification code Tyler emails to that address. [1]
4. Fill the remaining required fields (the ones marked with an asterisk) and press Submit. [1]
5. Confirm the portal dashboard opens and shows the expected name. Record only the visible identity label in `browser-state.json`, as `online-submission.md` P0 requires.

Nothing at sign-up asks for a contractor licence, business licence, or proof of ownership. Those come later: the City issues permits to an owner-builder or a City-licensed contractor, and every business working in the city needs a Laguna Beach business licence. [2] Keep those facts for the filing theory and issuance; do not ask for them to create an account.

## See fees and City comments: be a contact on the record

On a record page, the Fees, Reviews, Attachments, Contacts, and Meetings tabs say "You must be a contact on this record to see this information" unless the signed-in person is listed as a contact on that record. [3]

- When filing, add the applicant (and the owner, where the City's contact instructions ask) as contacts on the record. The portal map lists each work class's contact roles.
- If someone else files (a contractor or expediter), the homeowner sees fees and plan-check comments only if they are a contact on the record. Say this before filing, so the right people are added.
- If a needed person is missing from an already-filed record, ask the City to add them. Do not create a duplicate record to get access.

## When something goes wrong

- Wrong email used, accounts not linked: stop. Do not file from the second account. Ask the applicant which account owns the record and contact the City about account linking; the guide names a City contact address for portal account questions. [1]
- Verification email missing: the applicant checks spam and requests a new code. The agent does not handle the code.
- Contractor not found in the contact search: the City's panel-class instructions say a contractor without an account must ask the Building Division to add them, with their CSLB licence number, before proceeding. [4]

## Sources

1. City of Laguna Beach, Public Permitting Portal Online Account Registration Guide: https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000 (read 2026-08-10; returns HTTP 403 to direct downloads, so open it in a visible browser). The portal's `#/registration` page redirected to Tyler Identity when read the same day; no account was created.
2. City Building Permits page: https://www.lagunabeachcity.net/government/departments/community-development/building-permits (read 2026-07-08).
3. City portal record search: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/search (record tabs read 2026-08-10).
4. City instructions for the Electrical type's "Residential Electrical Service Panel up to 400 AMP" work class, `ContactInstructions`, in `assets/portal-maps/portal-snapshot.json` (read 2026-10-09).
