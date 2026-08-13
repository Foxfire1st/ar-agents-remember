# mcp/tests/test_quality_scope_reporting.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_scope_reporting.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-11T22:28+02:00               |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Contract tests for the code-quality wrapper's reported scope and provenance. The suite proves that
each fixed rail names non-vacuous inputs and results, untracked exposure does not mutate Git state,
caller altitude describes the actual candidate tree, and generated/dashboard workflow rails use
the shared reporting contract.

## Code Commentary

L23 verifies closeout provenance with an enclosure reports root and runs live lint parity only when the dashboard-local ESLint executable is actually available.

### Logic

`WrapperScopeOutputTests` pins scope-before-result ordering, nonzero units, distinct Radon/coverage
populations, and refusal of a vacuous CRAP scope. `ConfigTruthTests` rejects missing or inert tool
configuration. `UntrackedExposureTests` proves source/test/dashboard siblings are reported without
index mutation and that enumeration failure refuses. `CallerProvenanceTests` covers pre-push ref
input, staged closeout, clean integration, generated targets, and every dashboard/workflow rail.

The two assertions that execute installed Node tooling now use `skipUnless(shutil.which("node"))`.
Absence of the external runtime is an explicit environment skip; when Node is present the live
ESLint result set and all dashboard CI provenance rails are still asserted unchanged.

### Conventions

Temporary repositories are real Git repositories. Helpers construct only the minimal config and
workflow text needed to prove scope; live tool assertions skip only when their external executable
is unavailable.

### Invariants And Boundaries

- A PASS result must follow a non-vacuous, explicitly described scope.
- Reporting untracked inputs must not stage or otherwise mutate them.
- Closeout and integration labels describe the actual staged or clean candidate they certify.
- Missing Node may skip only the assertions that invoke Node; it cannot make a present runtime's
  lint or workflow result set pass vacuously.

### Todos

None.

## Docs References

No external Domain Documentation source is configured; the quality contract is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Wrapper result ordering and populations are non-vacuous. | `WrapperScopeOutputTests` | mcp/tests/test_quality_scope_reporting.py:135-327 |
| Configuration and untracked-input failures refuse rather than pass. | `ConfigTruthTests`; `UntrackedExposureTests` | mcp/tests/test_quality_scope_reporting.py:328-361; mcp/tests/test_quality_scope_reporting.py:362-547 |
| Caller provenance distinguishes pre-push, staged closeout, and clean integration inputs. | `CallerProvenanceTests`; `test_closeout_labels_the_already_staged_candidate`; `test_integration_invocations_name_the_clean_checkout` | mcp/tests/test_quality_scope_reporting.py:548-760; mcp/tests/test_quality_scope_reporting.py:608-614; mcp/tests/test_quality_scope_reporting.py:615-627 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T22:28+02:00 — 260731-EFA-L19 final curator pass: rewrote the generic symbol inventory
  as the current scope/provenance contract and recorded exact Node-unavailable skips for the two
  live dashboard assertions. Verification metadata remains pinned until governed closeout.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded the targeted
  pre-push tier assertion and the integration-invocation provenance tests.
  Verification metadata stays pinned until closeout stamps the 260731-EFA-L17
  commit.

- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 curator (trace delta): body verified against the current code and updated (260731-EFA-L7 (trace delta): the count-fix delta pins the live 426-TypeScript-input measurement (tsc...). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: the count-fix delta: the `426 TypeScript inputs` assertion matches the live measurement after the sync merge added `liveThinking.test.tsx`. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the npm-shim re-scoping of the sequencer-contract test (FL4). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
