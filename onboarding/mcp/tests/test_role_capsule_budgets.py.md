# mcp/tests/test_role_capsule_budgets.py

## Governing Overview

[overview](overview.md)

## Purpose

Checks renewed measurements for every yielded capsule and declared step file against their authored word ceilings. Historical budget decisions and predicates remain separate. The source-defined checks do not decide whether a ceiling change was authorized.

## Code Commentary

`matrix_keys` yields every role/operation capsule the manifest produces plus the launcher's; `compiled_size` counts whitespace-split words of the freshly compiled instruction text, seals excluded; `detail_sizes` measures each manifest-declared step file's complete source text and `digest_size` the separately delivered `core/every-role.md`. Live sizes are checked against the current record `skills/l-01-agent-lifecycles/capsule-budgets-current.json` through the test-support helper `capsule_budget_d695`: every capsule, declared detail and the digest must equal its renewed measurement and fit its authored ceiling; the declared-detail population must equal the manifest's step details, while eight linked ordinary templates are measured and identity-checked without a word ceiling; and the frozen historical registry `capsule-budgets.json`, its snapshot helper, the predecessor `capsule-budgets-d694.json` record and helper must match the hashes the record names.

The historical registry `capsule-budgets.json` keeps its own frozen checks. Its capped eleven-tenths guard, with ceilings of 4631 words for Architect, 4513 for Manager, 4100 for Curator, 4000 for Reviewer and Bootstrap, 3700 for other roles, 2700 for details and 1474 for the digest, is exercised on fixture registries. `test_d681_preserves_history_and_only_the_24_named_limits` pins its decision records and historical sizes by fingerprint and admits only the named limits plus one exact detail approval; provisional measurements keep their old limits and reject unbound records; and the handover projection budgets keep their 3300-token ceiling and formula. `test_full_matrix_binds_admitted_sources_and_rendered_identities` binds each matrix row to its admitted source revisions and rendered digest, and `test_changed_source_inside_budget_requires_a_fresh_measurement` makes a changed source stale even inside its old slack.

## Current audience, delivery and evidence contract

The mutation case patches the real measurement inputs and runs the historical-registry guard `_assert_current_fixture_budgets` on fixture registries. It supplies a good control then over-budget, live/stored-size ceiling and missing-detail failures. The guard is a size/registry check, not a meaning classifier or evidence that decision provenance was validated.

The current record sets capsule ceilings of 5500 words for Architect, 4600 for Manager, 4537 for Curator, 4200 for Reviewer, 4000 for Bootstrap, 3800 for Orchestrator and 3742 for other roles. Declared step details have a 2500-word ceiling and the separately delivered every-role digest a 2327-word ceiling. Registry completeness, exact renewed measurements and exact/over-ceiling controls apply independently. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence




- The historical-registry guard rejects missing/orphan entries, a recorded size that differs from the measured one, any actual/stored/budget size over its supplied ceiling, a budget different from min(ceil(stored size_words*11/10), ceiling) unless a named approved limit applies, and actual size over budget. `capsule_ceiling` selects Architect 4631, Manager 4513, Curator 4100, Reviewer/Bootstrap 4000 and 3700 for other roles; its callers guard details at 2700 and the shared digest at 1474. [2]


- The historical-registry capsule ceilings by role. [5]



- The historical registry's frozen decision records, historical sizes and named limits stay pinned. [7]

- MIK-R101@v1 rule 6 records growth, a new role and a new operation as decisions in the same change as the raised or added budget. [8]

- The budget registry test requires capsule keys to equal the manifest-derived role/operation/launcher matrix, detail keys to equal every declared detail source, and the digest entry to contain exactly size_words. [1]

- The tests measure whitespace-split words from freshly rendered capsule instructions, complete declared detail sources and the separately delivered every-role digest, then compare them with renewed measurements in `capsule-budgets-current.json` (current word ceilings are retired; only freshness and exact population completeness are checked). Exact populations reject omissions and orphans. Historical fixture mutation controls separately exercise exact and over-limit inputs. These are source assertions, not a fresh test run. [3]




- The current record's capsule, step-detail and digest ceilings. [6]

### Repo-Internal References (renewed)

- While `capsule-budgets-current.json` retains historical word-ceiling fields (5500 Architect, 4600 Manager, 4537 Curator, 4200 Reviewer, 4000 Bootstrap, 3800 Orchestrator, 3742 other roles; 2500 step-detail; 2327 digest), `_current_area_findings` in `capsule_budget_d695.py` no longer enforces word ceilings and checks only registry completeness and exact renewed measurement freshness. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [4]
