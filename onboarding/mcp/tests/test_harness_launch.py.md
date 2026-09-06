# mcp/tests/test_harness_launch.py

| Field                  | Value                              |
| ---------------------- | ---------------------------------- |
| repository             | agents-remember                    |
| path                   | `mcp/tests/test_harness_launch.py` |
| doc_type               | `file-level-onboarding`            |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash |                                    `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |                                    2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Harness-specific launch vocabulary and exact model identity.

## Code Commentary

### Logic

Pi accepts only the full provider-qualified catalog key. Effective launch refuses a different model. Applying native knobs preserves fixed argv/environment and rejects duplicate selector authority; a parameterized harness population carries the selected model and effort through each native vocabulary.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Catalog identity owns selection; an ambiguous model suffix is not a substitute. These cases do not start vendor processes or prove every historical catalog-validation edge.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Pi requires the exact provider qualified catalog key. | `test_pi_requires_the_exact_provider_qualified_catalog_key` | mcp/tests/test_harness_launch.py:40-71 |
| Effective launch still refuses a genuinely different model. | `test_effective_launch_still_refuses_a_genuinely_different_model` | mcp/tests/test_harness_launch.py:108-116 |
| Apply launch knobs preserves fixed argv and refuses duplicate authority. | `test_apply_launch_knobs_preserves_fixed_argv_and_refuses_duplicate_authority` | mcp/tests/test_harness_launch.py:119-154 |
| Every harness carries a clean selection into its own launch vocabulary. | `test_every_harness_carries_a_clean_selection_into_its_own_launch_vocabulary` | mcp/tests/test_harness_launch.py:178-185 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 3 repository-internal launch-policy and runner-contract references for effective echo/knob checks, Codex config parsing, and discovery/failure ordering; final scoped result 0 (checker-clean).

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_harness_launch.py`
  since the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3
  line(s) with no token change whatsoever. Checked by parsing both revisions and comparing the
  abstract syntax trees (identical) and the comment tokens (identical), so no symbol, signature,
  default, decorator, control-flow branch, docstring, or assertion this card describes has moved,and every claim this card makes about its own source still holds.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: added the R2 resolved-identity acceptance
  coverage — the opus[1m] regression pin (alias collapsed onto the default's `resolved_model` now
  validates via `_resolves_to_same_model`), the still-refuses-a-genuinely-different-model direction,
  and `_select_current_model` preferring the requested alias over the default collapse. Verification
  metadata stays pinned (uncommitted); closeout re-stamps the candidate commit.
- 2026-07-15T23:16+02:00 — Created for 260714-ACPUI-L2 with complete selection, dynamic
  model-gated validation, Pi identity, echo verification, duplicate-selector census, and
  unrelated-argument preservation coverage; final-audited the no-configured-domain-source evidence.
  Verification metadata is blank until closeout stamps the new source file's first commit.
