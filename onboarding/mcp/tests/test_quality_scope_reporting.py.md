# mcp/tests/test_quality_scope_reporting.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_scope_reporting.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Contract tests for the code-quality wrapper's reported scope and provenance. The suite proves that
each fixed rail names non-vacuous inputs and results, untracked exposure does not mutate Git state,
caller altitude describes the actual candidate tree, and the GitHub workflow stays on the
deterministic non-test hook instead of invoking a second Dagger/test rail.

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

## L23 Final Candidate Disposition

Quality reporting proofs bind the staged candidate and task-derived diff base to one authoritative
Dagger result and deterministic enclosure exports. A second host projection cannot satisfy the
acceptance contract.

## R39 Scope Authority

Scope/provenance tests require Dagger to retain the accepting wrapper and dashboard test rails
while GitHub PR validation calls only the deterministic targeted hook. Obsolete host
quality-environment assertions were removed; no second host report path can satisfy acceptance.

## 260815-DAG Master Full-Gate Repair

`CallerProvenanceTests` count-fix: the dashboard measurement assertion now pins the live
`434 TypeScript inputs` (was 426), matching the current tsc input count. No other scope or
provenance assertions changed.

## 260821-DAGQC-L4 Route Impact

The repository-policy assertion now checks the hook's precise statement that acceptance is
Dagger-only. This is wording ownership, not a new test route or a ban on all host diagnostics:
direct targeted Vitest unit/component loops remain non-certifying, while pytest, Playwright,
changed-lines CLI execution, the direct Python wrapper, and acceptance remain Dagger-attested.

## 260824-PDLS Admission Boundary

The shared quality configuration fixture now receives `QUALITY_TEST_ADMISSION`. Scope-reporting
behavior remains unchanged, while pytest-capable configuration stays unreachable to diagnostics.

## 2026-08-26 Canonical Rail And Product-Scope Reporting

Scope-order assertions now derive the fixed rail names from `quality_steps` instead of maintaining
a parallel list, and the report contract explicitly includes the `evidence-lifecycle` rail.
Radon and Coverage.py unit text now counts product Python files only; tests remain execution inputs,
not measurement targets. CRAP mocks patch the canonical calculator module directly.

## Update History

- 2026-08-26T10:44:52+02:00 — Reconciled scope reporting with canonical rail derivation, the evidence-lifecycle rail, and product-only measurement units.
- 2026-08-24T21:23+02:00 — Added typed admission to quality configuration.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: recorded the hook assertion's
  precise acceptance-only wording and the separate diagnostic-only Vitest boundary. No route
  topology changed; Dagger acceptance remains pending.
- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: updated the dashboard
  TypeScript-input count assertion to the live 434 measurement (was 426). Verified at code
  commit e5cb139f.

- 2026-08-14T11:27+02:00 — R39 curator: aligned scope reporting with Dagger-only acceptance and
  non-test CI. Verification remains closeout-owned.
- 2026-08-14T09:37+02:00 — Reopened L23 cadence: the workflow assertion now requires the
  pull-request-only deterministic hook and forbids the GitHub Dagger action.
- 2026-08-14T06:38+02:00 — L23 final candidate review: quality reporting proofs retain exact
  staged/diff-base scope and one authoritative Dagger result with deterministic enclosure exports.

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
