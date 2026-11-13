---
license: cc-by-4.0
language:
- en
pretty_name: US Landlord-Tenant Law Dataset (50 States + DC)
tags:
- legal
- tenant
- landlord
- housing
- us-states
- security-deposit
- statutes
size_categories:
- n<1K
task_categories:
- question-answering
- text-classification
configs:
- config_name: default
  data_files: data/us-tenant-laws.csv
---

# US Landlord-Tenant Law Dataset (50 States + DC)

One row per U.S. state plus the District of Columbia (51 rows, 27 columns): security deposit rules, late fees, landlord entry, month-to-month termination notice, rent increase notice and rent control, and retaliation, each with a statute citation and an official source link where one was found.

- Snapshot date of this copy: 2026-11-05. Data last verified: 2026-10-22 (field `as_of`).
- Files: `data/us-tenant-laws.csv` (the table) and `data/us-tenant-laws.json` (same rows plus metadata).
- License: CC BY 4.0. Not legal advice (see Limitations).

## Where to get it

- GitHub: https://github.com/lamak25/us-tenant-laws
- Hugging Face: https://huggingface.co/datasets/Kamil-KKA/us-tenant-laws
- Kaggle: https://www.kaggle.com/datasets/kamilkka/us-landlord-tenant-laws-by-state
- Live version (updated first): https://redflaglease.com/data

## Summary computed from the data

Computed with `scripts/summary.py` on the CSV in this repo; text-based counts use the stated rule in the first words of the cell, so treat them as approximate.

| Measure | Value |
|---|---|
| Rows (50 states + DC) | 51 |
| Rows where `deposit_max` says there is no statutory cap | 20 |
| Rows with a numeric deposit return deadline | 49 (KY and TN blank) |
| Median deposit return deadline | 30 days (range 14 to 60) |
| Most common deadlines | 30 days: 24 states, 45 days: 7, 14 days: 5, 21 days: 5, 60 days: 4 |
| Rows where `deposit_interest` starts with "Yes" | 8 (CT, DC, MA, MD, MN, ND, NH, NJ) |
| Rows where the statewide rent control field starts with "Yes" | 4 (CA, DC, OR, WA) |
| Rows with a statute URL on all six topics | 35 of 51 |

## Columns (data dictionary)

All values are text. Empty cell = no statute found or the point was not verified (do not read it as "no rule"); values are never guessed. Numbers and booleans are stored as strings (for example `30`, `true`).

| Column | Meaning |
|---|---|
| `state` | State or district name |
| `code` | Two-letter postal code |
| `state_page_url` | Page on redflaglease.com with the full explanation for that state |
| `deposit_max` | Security deposit cap, as stated in the statute summary (free text, may include exceptions) |
| `deposit_return_deadline_days` | Days the landlord has to return the deposit (number as text; month-based or business-day rules and exceptions are explained in the statute) |
| `deposit_itemization_required` | `true` if an itemized list of deductions is required |
| `deposit_interest` | Whether interest on the deposit is required (free text or `false`) |
| `deposit_citation` | Statute citation for the deposit rules |
| `deposit_source_url` | Link to the statute text for the deposit rules |
| `late_fee_rule` | Late fee rule (cap, grace period, or a note that none was found) |
| `late_fee_citation` | Statute citation for the late fee rule |
| `late_fee_source_url` | Link to the source for the late fee rule |
| `entry_notice` | Notice a landlord must give before entering the unit |
| `entry_citation` | Statute citation for landlord entry |
| `entry_source_url` | Link to the source for landlord entry |
| `month_to_month_tenant_notice` | Notice a tenant must give to end a month-to-month tenancy |
| `month_to_month_landlord_notice` | Notice a landlord must give to end a month-to-month tenancy |
| `month_to_month_citation` | Statute citation for month-to-month termination |
| `month_to_month_source_url` | Link to the source for month-to-month termination |
| `rent_increase_notice` | Rent increase notice rule |
| `rent_increase_statewide_rent_control` | Statewide rent control or rent cap note (preemption of local rent control is noted here) |
| `rent_increase_citation` | Statute citation for rent increases |
| `rent_increase_source_url` | Link to the source for rent increases |
| `retaliation_rule` | Rule against landlord retaliation |
| `retaliation_citation` | Statute citation for retaliation |
| `retaliation_source_url` | Link to the source for retaliation |
| `as_of` | Date the dataset was last verified (YYYY-MM-DD) |

## Coverage

50 states and DC. Six topics: security deposits (cap, return deadline, itemization, interest), late fees, landlord entry notice, month-to-month termination notice, rent increase notice and statewide rent control, and retaliation. Statewide law only.

## Methodology

For each state, every value was read against the statute text (or the official agency page named in the row) and stored with its citation and a source link. States were checked between 2026-10-17 and 2026-10-22. Where a state's official code site could not be reached, the text was read from a public reproduction or an archived copy of the official page and checked against amendment lists (for example Arkansas, Mississippi, New Mexico, Tennessee and parts of Georgia); the source link in those rows may point to the reproduction rather than the official site. If no statute could be found on a point, the cell is left empty or says that none was found; nothing is filled in from memory.

## Limitations

- Not legal advice. General information; statutes change. Always read the linked statute and check for newer amendments before relying on a value.
- Statewide law only. City and county ordinances (for example New York City, San Francisco, Chicago) are not covered unless a cell says so.
- Free-text cells summarize a statute and omit many exceptions (small landlords, building size, tenant age, lease type).
- Some cells are empty; an empty cell means "not found or not verified", not "no rule".
- `deposit_itemization_required` is `true` in every row; check the statute for how and when the itemization must be delivered.

## Example questions this answers

- Which states have no cap on a security deposit?
- How many days does a landlord have to return a deposit in Texas?
- Which states require interest on security deposits?
- How much notice must a landlord give before entering a rental?
- Which states have statewide rent control or a rent cap?
- How much notice ends a month-to-month tenancy in each state?

## How to cite

RedFlagLease. *US Landlord-Tenant Law Dataset (50 States + DC)*, version 2026-10-22. https://redflaglease.com/data (CC BY 4.0). See `CITATION.cff`.

## Source and contact

Compiled by RedFlagLease, https://redflaglease.com, which also publishes a plain-language page per state at https://redflaglease.com/laws. Corrections and questions: https://redflaglease.com/contact
