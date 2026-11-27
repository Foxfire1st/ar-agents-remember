# mcp/tests/test_role_capsule_budgets_d694.py

## Governing Overview

[overview](overview.md)

## Purpose

Negative controls distinguish the frozen predecessor record `capsule-budgets-d694.json` from the renewed measurements and authored ceilings in `capsule-budgets-current.json`, through `capsule_budget_d694` and `capsule_budget_d695`. The predecessor retains its fingerprint and historical limits. Current checks reject stale measurements, population drift, changed source identities and ceiling overages; renewed growth within a ceiling has no individual budget. The live-population case compares the current corpus measurements with the current record here and in `test_role_capsule_budgets.py`.

## Code Commentary

- The current record binds the real population: every compiled capsule, declared detail and the every-role digest measured from the corpus produces no finding against `capsule-budgets-current.json`.
- The frozen predecessor record is authenticated by a pinned whole-record fingerprint. Current measurements are checked against the current sources and authored ceilings; the live record has no whole-record fingerprint check.
- For every current measured key, a changed size is stale, a removed source leaves an orphan measurement, and an unregistered key lacks a measurement. Capsule, declared-detail and digest sizes above their authored ceilings fail; ordinary templates have no size ceiling.
- The current record admits exactly the manifest's declared step details (each capped at 2500 words) and four linked ordinary templates (`file-card`, `repo-entity-catalog`, `repo-overview`, `route-local-overview`) that are measured and identity-checked but carry no word limit: an ordinary template above 2500 words passes, a declared detail at 2501 fails.
- Source identity is checked beyond word counts: same-size content edits, changed hashes or compiler-input revisions, missing files and source-inventory discrepancies are detected. The current classification controls reject detail/template population overlap and manifest or source-membership corruption.
- Synthetic fixture records exercise the current measurement, ceiling, classification and source-identity predicates. Ordinary templates retain measured source identities without acquiring a declared-detail ceiling.
- The frozen predecessor record keeps its own paths and ceilings, including a Curator capsule ceiling of 4177 words, and the current record pins its bytes and its helper by hash.

## Evidence

- The current record binds the real compiled population with no finding. [1]

- The frozen predecessor record rejects later growth and population drift. [10]
- The frozen predecessor record keeps a 4177-word Curator ceiling and its own detail population. [11]

- The current-layer predicates check renewed measurements, authored ceilings, source identities and frozen predecessor history. [12]

- Current measured keys reject stale sizes, orphan measurements and unregistered keys, with the renewal command named in the finding. [3]


- The current classification checks bind declared-detail and ordinary-template populations to the manifest. Word ceilings for capsules, step details and the digest are retired while freshness checks remain, and `COMPILED_CAPSULE_TOKEN_CEILINGS` (34 matrix keys) enforce compiled-capsule token ceilings whose failures name the measured size, ceiling and developer's decision. [4]



- An ordinary template above 2500 words carries no size limit. [5]


- Ordinary-template source identities and compiler-input revisions are checked; same-size content edits and missing sources produce findings that name the renewal command. [7]
