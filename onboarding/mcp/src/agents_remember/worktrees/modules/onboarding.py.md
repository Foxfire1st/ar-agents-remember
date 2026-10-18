# mcp/src/agents_remember/worktrees/modules/onboarding.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Plans changed-source onboarding coverage and performs entity fingerprint and generated route-index refresh. Its converted source-bound trace entry reports current onboarding answers and named repair findings; legacy body/history classifiers, baseline helpers, verification stamping and refresh validators were removed.


## Code Commentary

### Logic

`onboarding_refresh_plan_for_context` resolves each changed source through the exact context storage rules. Disabled sources are skipped. Unsupported or missing working-path cards block; committed-range gaps are reported as `unonboarded`. `working_paths=None` treats every changed path as working. Long-path-safe filesystem probes determine presence.

Layout-marker detection is no longer exported here as `converted_onboarding`. `onboarding_trace_gate_for_context` takes one `OnboardingTraceInputs` value carrying the candidate `code_blobs` mapping, the leaf worklist run's identical-copy groups and the working paths, delegates source-current answer evaluation to `onboarding_trace_result`, and returns repair findings. `_require_onboarded_sources` raises `RuntimeError` for missing/unsupported cards and otherwise returns its plan; the gate catches that error and prepends the corresponding missing/unsupported-card finding without discarding trace findings. Curator controller dispatch reports incomplete when converted sides are unavailable; no legacy body/history fallback remains.

`identical_changes_from_run` is the one strict reader of a run's `identicalChanges` (MIK-R177): a non-mapping map, a non-string or empty key, a non-list entry, a member that is not a non-empty string, an empty member list, or a group that omits its own representative each raise `IdenticalChangesUnreadable` naming the entry. Nothing is dropped or coerced, so a malformed group can never shorten into a one-source item, and a genuine empty mapping stays empty. The gate groups its items with exactly the groups `worklist_onboarding` uses, so an item a card row answers in the worklist is the item the gate raises; `identical_changes` carries no default, so no caller can judge ungrouped items by omission.

Entity refresh parses the catalog table, limits membership to rows whose evidence paths intersect the changed set, rejects unsupported algorithms or missing fingerprint values, computes deterministic `git-blob-set-v1` from sorted path/blob identities at HEAD, and replaces each affected row value.

Route-index preview and apply pass explicit roots, repository and `context.storage` to `build_route_indexes`; derived indexes cannot select a different path-rule authority.

The removed metadata writers, citation-coordinate exception, stale/untraced/no-impact classifiers, verified-memory baseline and exclusive prepared trace validator have no operational replacement here.

### Conventions

This module owns coverage planning, the curator trace entry and derived entity/index refresh. Shared Markdown parsing remains in kernel; source census and index rendering retain their separate kernel owners.

#### Invariants And Boundaries

- Blocking missing/unsupported onboarding is limited to working paths; transported committed gaps remain reported.
- Source-current `updated` rows require counted Markdown/reference edits; `no_impact` answers unchanged contracts, and later source movement reopens an answer. Realizes/proves-only and mechanical anchor edits do not count.
- Curator-coherence no-impact does not substitute for the onboarding row. The amended rollout rule separately credits this leaf's own measured changed card under the old producer without a changed-card row or future backfill.
- Route-index preview and apply use the exact resolved context storage authority.
- Entity fingerprints and route indexes are derived data, not semantic acceptance or verification stamps.

### Todos

None known for the MX-FIX-4 closeout caller boundary.

## Converted Onboarding Traces

The converted curator trace entry remains source-bound. It requires one `OnboardingTraceInputs` value — candidate blobs, the run's identical-copy groups and the working paths — returns trace and missing-card repair findings, and never falls back to legacy history/stamps. Missing converted comparison sides are incomplete. The removed closeout-only trace validator does not remove `onboarding_trace_result` or the current-row doctrine.


## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References



Entity fingerprint refresh and generated route-index refresh survive independently of the deleted legacy onboarding baseline/classifier/stamping branch. Cache data is not a review baseline or an additional output.


- Route-index refresh accepts the resolved storage authority and consumes one deterministic source snapshot. (`build_route_indexes`; `route_index_source_snapshot`) [12]


### Cross-Repo References

Closeout can coordinate code and external-memory worktrees, but no external
implementation governs this module.

No additional cross-repository evidence applies.


- The helper raises for missing/unsupported cards; the trace wrapper catches that RuntimeError and prepends the finding while retaining trace findings. [3]

- Source-current rows govern converted onboarding; updated needs a counted Markdown/reference edit and current candidate blob binding. [7]

- The surviving curator trace entry takes the candidate blobs and the run's identical-copy groups through one inputs value and requires current eligible answers; missing converted sides are incomplete. [13]

- Converted-tree classification remains layout-marker based at the retained knowledge-gate owner; the local converted_onboarding wrapper was removed. [1]

- The converted memory-quality entry point requires one inputs value and forwards the candidate blobs and the run's identical-copy groups; it returns trace repair findings. [4]

- The gate reads a run's groups through one strict reader: a malformed or representative-omitting group raises rather than shortening into a single source. (`identical_changes_from_run`; `IdenticalChangesUnreadable`) [14]
