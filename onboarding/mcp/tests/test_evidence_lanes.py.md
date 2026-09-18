# mcp/tests/test_evidence_lanes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_evidence_lanes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:02+02:00 |
| lastVerifiedCommitHash | `f05ba167cd6dfb56b48a775f3da5d45528c09c82`|
| lastVerifiedCommitDate | 2026-09-18T17:19:31+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l4-ar` uncommitted source; base `0dd04d6adbca3e8ba61849b605ece3137005829e` |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Evidence-lane registry completeness and uniqueness validation.

## Code Commentary

### Logic

The retained test removes a required category, duplicates a category and reuses a marker; each malformed registry raises the specific UsageError. Small item/config and manifest fixtures remain available to consumers.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

This single registry test does not enumerate every collected node or prove the historical classification matrix. Missing authority is a refusal rather than an implicit default lane.

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
| Incomplete or ambiguous registry is refused. | `test_incomplete_or_ambiguous_registry_is_refused` | mcp/tests/test_evidence_lanes.py:66-74 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## 260918-TSIP-L4 — The Armed Hook And The Loader's Verdict (`T48`/`T49`)

Two cases added (**+32 lines**; file **74 → 106 lines**), no existing case touched.

- **`test_the_enforcing_hook_is_registered_and_armed`** asserts the armed state from the plugin
  manager's own `hasplugin`/`get_hookimpls()` — not from source text — because `evidence_lanes`
  defines `pytest_collection_modifyitems` and, until this leaf, nothing registered it: the suite
  passed while the manifest refused.
- **`test_the_shipped_loader_accepts_this_population`** runs `load_lane_manifest` against this
  worktree's real population and **pins no count**, so a leaf that adds both a module and its row
  is green while a leaf that adds only a module is red.

Two-sided evidence: unregistering the hook (`M11`) fails the armed-state case with
`assert False = hasplugin(...)`; dropping the row with the hook on (`M12`) refuses collection
outright — `ERROR: test evidence lanes have 1 finding(s): … no tests ran` — and forcing the hook
on *before* the row existed gives `INTERNALERROR> AssertionError … crashitem`, which is the
symptom `T48` recorded.

**This module's own lane is `architecture-fitness`** (`mcp/tests/test-evidence-lanes.toml:231`),
recorded by `260831-LOCR-L07`.

## Update History
- 2026-09-18T17:02+02:00 — 260918-TSIP-L4 curator (uncommitted change set on `ar/260918-tsip-l4-ar`, base `0dd04d6a`): two cases added: the hook's armed state read from the plugin manager, and the shipped loader's verdict on this population (`T48`/`T49`). Verification metadata stays at the recorded verification because the candidate is uncommitted and the governed closeout owns the real code commit; `lastUpdated` advances with this body edit.

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: created the missing sidecar for exhaustive,
  explicit, fail-loud evidence-lane classification.
