# mcp/src/agents_remember/worktrees/modules/onboarding.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Plans changed-source onboarding coverage and performs entity fingerprint and generated route-index refresh. Its converted source-bound trace entry reports current onboarding answers and named repair findings; legacy body/history classifiers, baseline helpers, verification stamping and refresh validators were removed.


## Code Commentary

### Logic

`onboarding_refresh_plan_for_context` resolves each changed source through the exact context storage rules. Disabled sources are skipped. A dependent document is not a source: the planner also takes the dependent document paths (`dependent_documents`, read from the memory root's `knowledge/dependents` when none are handed in) and skips any changed path one of them names, so a document with a dependent record still gets no card and no entry (MIK-R124 rules 1 and 6). `onboarding_refresh_plan` reads the dependents of both memory sides through `leaf_onboarding_trace_sides` and raises when either side cannot be read, and the trace gate turns that into its named incomplete finding. Unsupported or missing working-path cards block; committed-range gaps are reported as `unonboarded`. `working_paths=None` treats every changed path as working. Long-path-safe filesystem probes determine presence.

Layout-marker detection is no longer exported here as `converted_onboarding`. `onboarding_trace_gate_for_context` takes one `OnboardingTraceInputs` value carrying the candidate `code_blobs` mapping, the leaf worklist run's identical-copy groups and the working paths, delegates source-current answer evaluation to `onboarding_trace_result`, and returns repair findings. `_require_onboarded_sources` raises `RuntimeError` for missing/unsupported cards and otherwise returns its plan; the gate catches that error and prepends the corresponding missing/unsupported-card finding without discarding trace findings. Curator controller dispatch reports incomplete when converted sides are unavailable; no legacy body/history fallback remains.

`identical_changes_from_run` is the one strict reader of a run's `identicalChanges` (MIK-R177): a non-mapping map, a non-string or empty key, a non-list entry, a member that is not a non-empty string, an empty member list, or a group that omits its own representative each raise `IdenticalChangesUnreadable` naming the entry. Nothing is dropped or coerced, so a malformed group can never shorten into a one-source item, and a genuine empty mapping stays empty. The gate groups its items with exactly the groups `worklist_onboarding` uses, so an item a card row answers in the worklist is the item the gate raises; `identical_changes` carries no default, so no caller can judge ungrouped items by omission.

Entity refresh parses the catalog table into rows and plans by three rules: a row is in scope when
its evidence touches a changed path, when its evidence list differs from the same row at the leaf's
memory base (`entity_evidence_at_base`), or when the base holds no such row. A row in scope whose
algorithm is not `git-blob-set-v1` is reported unsupported rather than planned.
`entity_fingerprint_plan_problems` asks **every** catalog row, planned or not, for evidence paths the
code candidate tree does not hold, and that absence check is the unconditional one. The other two
diagnostics stay with the plan: an unsupported algorithm is read from the plan's unsupported rows,
and a missing fingerprint value is reported only for a row the plan requires. One line per row
carries every fault that applies to it, with its remedy;
`entity_fingerprint_plan_refusal` renders those lines as the one refusal, and both the closeout's
candidate verdict and the refresh before the memory commit ask it. A value is `git-blob-set-v1` over
the sorted path/blob identities at the **code commit's tree**
(`compute_git_blob_set_fingerprint(..., tree=...)`), never at `HEAD`. `_tree_paths` reads the
candidate tree's path set once, and an unreadable tree, base or commit refuses by name with its step
and the identity it read (`_commit_tree`, `_row_fingerprint`).

The curator side of the same rows is read-only:
`entity_evidence_findings_for_candidate(context, code_worktree)` captures the leaf's own candidate
tree and returns one finding per (catalog row, absent path), naming the file, the row and the path
and the clearing action; a candidate Git cannot read returns one incomplete finding rather than an
empty pass.

Route-index preview and apply pass explicit roots, repository and `context.storage` to `build_route_indexes`; derived indexes cannot select a different path-rule authority. `route_index_refresh_problems` asks that same planner as a dry run and returns one line naming the step, the offending input and the error when it cannot read or render them, which is the route-index half of the closeout's candidate verdict.

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

- Every catalog row is evidence-checked against the code candidate tree, planned or not; absent evidence is the unconditional check, while an unsupported algorithm and a missing fingerprint value are diagnosed from the plan's rows. [15]

- Route-index refresh accepts the resolved storage authority and consumes one deterministic source snapshot. (`build_route_indexes`; `route_index_source_snapshot`) [12]

- Source-current rows govern converted onboarding; updated needs a counted Markdown/reference edit and current candidate blob binding. [7]


- The helper raises for missing/unsupported cards; the trace wrapper catches that RuntimeError and prepends the finding while retaining trace findings. [3]





- The one entity refusal the closeout asks before the code commit and again before the memory commit. [16]
- A row's value is computed over the code commit's own tree, not `HEAD`. [17]
- The candidate tree's path set is read once, and an unreadable tree refuses by name. [18]
- A row is in scope when its evidence list differs from the same row at the leaf's memory base, or the base holds no such row. [19]
- The route-index refresh's own deterministic refusals, asked through its planner. [20]
- The curator's memory-quality finding for a row citing a path the candidate lacks, never raising on an unreadable candidate. [21]

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References



Entity fingerprint refresh and generated route-index refresh survive independently of the deleted legacy onboarding baseline/classifier/stamping branch. Cache data is not a review baseline or an additional output.




### Cross-Repo References

Closeout can coordinate code and external-memory worktrees, but no external
implementation governs this module.

No additional cross-repository evidence applies.





- Converted-tree classification remains layout-marker based at the retained knowledge-gate owner; the local converted_onboarding wrapper was removed. [1]


- The converted memory-quality entry point requires one inputs value and forwards the candidate blobs and the run's identical-copy groups; it returns trace repair findings. [4]


- The gate reads a run's groups through one strict reader: a malformed or representative-omitting group raises rather than shortening into a single source. (`identical_changes_from_run`; `IdenticalChangesUnreadable`) [14]

- The surviving curator trace entry takes the candidate blobs and the run's identical-copy groups through one inputs value and requires current eligible answers; missing converted sides are incomplete.  Anchor: `onboarding_trace_gate_for_context` `_onboarding_trace_open` `OnboardingTraceInputs` `_worklist_identical_changes` [13]
