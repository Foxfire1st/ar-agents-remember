# mcp/tests/test_role_capsule_budgets_d694.py

## Governing Overview

[overview](overview.md)

## Purpose

Negative controls for the fingerprinted budget records: the frozen predecessor record `capsule-budgets-d694.json` and the live current record `capsule-budgets-current.json`, checked through the test-support helpers `capsule_budget_d694` and `capsule_budget_d695`. The module proves each record and its predicates reject growth, population drift and changed sources; the live population check itself runs against the real corpus here and in `test_role_capsule_budgets.py`.

## Code Commentary

- The current record binds the real population: every compiled capsule, declared detail and the every-role digest measured from the corpus produces no finding against `capsule-budgets-current.json`.
- Both records are authenticated by a pinned fingerprint of the whole record; changing any field, a limit, a measurement or a population fails as a changed binding before any source check runs.
- For every recorded key, a size one word above its measurement is stale, a size above its limit exceeds it, a removed key names no current source and an unregistered key is missing a budget.
- The current record admits exactly the manifest's declared step details (each capped at 2500 words) and four linked ordinary templates (`file-card`, `repo-entity-catalog`, `repo-overview`, `route-local-overview`) that are measured and identity-checked but carry no word limit: an ordinary template above 2500 words passes, a declared detail at 2501 fails.
- Source identity is checked beyond word counts: a same-size content change, a changed hash or compiler-input revision, a missing file and an approved source with no file each produce a finding, and population, manifest-classification and source-inventory corruption raise.
- Synthetic fixture records exercise the predicates only; the one case that admits a synthetic record patches the expected fingerprint while keeping the real authentication function, and the frozen owners it checks are copied byte for byte from the repository.
- The frozen predecessor record keeps its own paths and ceilings, including a Curator capsule ceiling of 4177 words, and the current record pins its bytes and its helper by hash.

## Evidence

- The current record binds the real compiled population with no finding. [1]
- Any changed field of the current record fails as a changed binding. [2]
- Each recorded key rejects unmeasured growth, over-limit size, removal and unregistered keys. [3]
- The declared-detail population equals the manifest's step details, the detail ceiling is 2500, and digest and Curator capsule overages fail. [4]
- An ordinary template above 2500 words carries no size limit. [5]
- A declared detail at 2501 words fails its 2500 ceiling. [6]
- Ordinary-template source drift is still rejected. [7]
- Whole-record authentication precedes source checks. [8]
- A synthetic record admitted by a patched fingerprint still authenticates the frozen owners and rejects a changed ordinary template. [9]
- The frozen predecessor record rejects later growth and population drift. [10]
- The frozen predecessor record keeps a 4177-word Curator ceiling and its own detail population. [11]
- The current-layer predicates and fingerprints. [12]
