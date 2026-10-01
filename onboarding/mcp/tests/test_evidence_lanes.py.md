# mcp/tests/test_evidence_lanes.py

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

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Incomplete or ambiguous registry is refused. [1]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.

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

**This module's own lane is `architecture-fitness`** (`mcp/tests/test-evidence-lanes.toml:233`),
recorded by `260831-LOCR-L07`.
