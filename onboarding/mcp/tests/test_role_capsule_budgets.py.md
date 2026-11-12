# mcp/tests/test_role_capsule_budgets.py

## Governing Overview

[overview](overview.md)

## Purpose

Enforces recorded budgets for every yielded capsule and declared step file, with separate absolute word ceilings. Growth, a new role and a new operation are same-change decisions recorded with the raised or added budget. The test bounds sizes and pins the exact decision records by fingerprint; it does not judge whether a decision was authorized — that is evidenced by the decision records in `capsule-budgets.json` and `capsule-budgets-current.json`.

## Code Commentary

`matrix_keys` yields every role/operation capsule the manifest produces plus the launcher's; `compiled_size` counts whitespace-split words of the freshly compiled instruction text, seals excluded; `detail_sizes` measures each manifest-declared step file's complete source text and `digest_size` the separately delivered `core/every-role.md`. Live sizes are checked against the current record `skills/l-01-agent-lifecycles/capsule-budgets-current.json` through the test-support helper `capsule_budget_d695`: the record must match its pinned fingerprint; every capsule, declared detail and the digest must equal its recorded measurement and fit both its recorded limit and its ceiling; the declared-detail population must equal the manifest's step details, while four linked ordinary templates are measured and identity-checked but carry no word limit; and the frozen historical registry `capsule-budgets.json`, its snapshot helper, the predecessor `capsule-budgets-d694.json` record and helper and `core/digest-map.json` must match the hashes the record names.

The historical registry `capsule-budgets.json` keeps its own frozen checks. Its capped eleven-tenths guard, with ceilings of 4631 words for Architect, 4513 for Manager, 4100 for Curator, 4000 for Reviewer and Bootstrap, 3700 for other roles, 2700 for details and 1474 for the digest, is exercised on fixture registries. `test_d681_preserves_history_and_only_the_24_named_limits` pins its decision records and historical sizes by fingerprint and admits only the named limits plus one exact detail approval; provisional measurements keep their old limits and reject unbound records; and the handover projection budgets keep their 3300-token ceiling and formula. `test_full_matrix_binds_admitted_sources_and_rendered_identities` binds each matrix row to its admitted source revisions and rendered digest, and `test_changed_source_inside_budget_requires_a_fresh_measurement` makes a changed source stale even inside its old slack.

## Current audience, delivery and evidence contract

The mutation case patches the real measurement inputs and runs the historical-registry guard `_assert_current_fixture_budgets` on fixture registries. It supplies a good control then over-budget, live/stored-size ceiling and missing-detail failures. The guard is a size/registry check, not a meaning classifier or evidence that decision provenance was validated.

Live capsule ceilings come from the current record: 5441 words for Architect, 4522 for Manager, 4537 for Curator, 4049 for Reviewer, 4000 for Bootstrap and 3722 for other roles. Declared step details have a 2500-word ceiling and the separately delivered every-role digest a 2266-word ceiling that must equal the digest map's maximum. Registry completeness, exact recorded measurements and exact/over-limit mutation controls apply independently. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence

- The budget registry test requires capsule keys to equal the manifest-derived role/operation/launcher matrix, detail keys to equal every declared detail source, and the digest entry to have exactly size_words and budget_words. [1]

- The historical-registry guard rejects missing/orphan entries, a recorded size that differs from the measured one, any actual/stored/budget size over its supplied ceiling, a budget different from min(ceil(stored size_words*11/10), ceiling) unless a named approved limit applies, and actual size over budget. `capsule_ceiling` selects Architect 4631, Manager 4513, Curator 4100, Reviewer/Bootstrap 4000 and 3700 for other roles; its callers guard details at 2700 and the shared digest at 1474. [2]

- The tests measure whitespace-split words from freshly rendered capsule instructions, complete declared detail sources and the separately delivered every-role digest, and check them against the fingerprinted current record: exact recorded measurements, per-key limits and role-specific ceilings (Architect 5441, Manager 4522, Curator 4537, Reviewer 4049, Bootstrap 4000, otherwise 3722), details 2500 and digest 2266. Exact keys reject omissions and orphans; mutation controls invoke the real guards with changed inputs at and beyond the limits. [3]

- Live capsule ceilings are 5441 words for Architect, 4522 for Manager, 4537 for Curator, 4049 for Reviewer, 4000 for Bootstrap and 3722 for other roles; declared step details have a 2500-word ceiling and the separately delivered every-role digest a 2266-word ceiling that must equal the digest map's maximum. Registry completeness, exact recorded measurements and exact/over-limit mutation controls apply independently. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [4]

- The historical-registry capsule ceilings by role. [5]
- The current record's capsule, step-detail and digest ceilings. [6]
- The historical registry's frozen decision records, historical sizes and named limits stay pinned. [7]
