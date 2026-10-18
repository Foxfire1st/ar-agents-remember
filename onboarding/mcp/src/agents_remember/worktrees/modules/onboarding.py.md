# mcp/src/agents_remember/worktrees/modules/onboarding.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Plans and applies closeout-time onboarding metadata, route overview metadata,
route index, and entity fingerprint refreshes for changed code paths.

## Retained Legacy Refresh Helpers (CCR-R12@v5)

The retained legacy refresh helpers stamp existing sidecar/overview verification metadata, refresh
entity fingerprints and regenerate route indexes after the accepted code commit. The body/history
and stamp discussion below describes those unconverted helpers and their historical use, not the
ordinary converted path: converted cards get no verification stamps and use the source-bound
trace gate. MIK-R46 refuses ordinary unconverted operations even before any official line converts;
the retained legacy branch is not an allowed fallback for those operations. `refresh_onboarding_metadata_for_context` and
`refresh_route_overview_metadata_for_context` do not perform memory-quality, curator-coherence, or
semantic body validation on this path; those validators remain explicit preparation/curation
owners. This separation lets closeout publish mechanical metadata while keeping semantic review
outside the transaction. Full suites and quality checks are explicit developer actions.

## Code Commentary

### Logic

`contract_memory_verified_commit` chooses the accepted memory-content commit, or the task memory base before a closeout has recorded one. A ledger-cache commit is never a body-review baseline. This keeps the existing dirty-plus-committed memory membership tied to real memory content.

The module finds changed source sidecars — gating each changed source on the
boolean `resolver.is_sidecar_storage(storage)` predicate (sidecar-backed storage
modes only) — validates required verification metadata, updates
`lastVerifiedCommitHash` and `lastVerifiedCommitDate`, parses
route overview metadata, updates affected route overviews, runs generated route
index refreshes, parses repo entity fingerprint tables, computes
`git-blob-set-v1` fingerprints, and updates affected entity rows after the code
commit exists. The shared metadata/route parsing helpers
(`onboarding_metadata_row`, `markdown_table_cells`, `table_metadata`,
`normalize_route`, `route_contains_changed_path`, `ROUTE_OVERVIEW_DOC_TYPES`)
live in `kernel/onboarding_doc.py` and are re-exported here as a facade.

`refresh_onboarding_metadata_for_context` also stamps the task's regenerated citation documents
(`_refresh_regenerated_documents`, 260731-EFA-L16): the citation gate clears a changed claim by
making its citation CURRENT, which the fixer achieves without the document's own source file
changing, so those documents are outside the changed-source plan — any onboarding document the
task touched in the memory worktree that carries verification metadata advances to the new code
commit here, except route overviews and entity catalogs (their own refresh passes own them).

`onboarding_refresh_plan_for_context` carries the two-tier responsibility split
(issue #83) through its keyword-only `working_paths`: paths in the working set
without onboarding land in the blocking `missing`/`unsupported` buckets exactly
as before, while committed-range paths (transported merges, pre-committed
slices) without onboarding collect in the non-blocking `unonboarded` list, so
already-onboarded artifacts gate regardless of author but never-onboarded files
are not blanket-onboarded at closeout. `working_paths=None` keeps the strict
legacy semantics. `contract_memory_verified_commit(contract)` resolves the
body-gate baseline (`memory_content_commit` →
`memory_base_commit`), `_changed_memory_paths` widens gate membership to dirty
∪ committed-since-verified memory paths, and `_joined_sample` caps gate error
path joins at `PATH_SAMPLE_LIMIT`.

The retained unconverted helper path also enforces its historical closeout content gate. `classify_sidecar_updates` sorts
each changed source's sidecar by meaningful body change (content outside the
verification metadata rows and Update History, vs the last verified memory
commit via `commit_text_or_none` — `memory_verified_commit`, falling back to
HEAD when empty) and new Update History lines into four cases:
body+history passes; body without history is `untraced` (traceability);
history-only still recognizes a historical `No content impact:` marked entry and is collected as
`attested_no_impact`; everything else (unchanged, metadata-only, unmarked history-only) is
`stale`. The verified-commit baseline means sidecar
work already committed in the memory worktree before closeout still classifies
honestly, and a new sidecar committed early passes like an untracked one
(absent at the baseline). `require_updated_sidecar_content` first applies the exact accepted
no-content identities supplied by the current curator-coherence authority, then raises on any
remaining `stale`/`untraced` content. Only a matching `stale` identity can move to
`attested_no_impact`; `untraced` content remains closed. The check returns the attested source
paths so closeout payloads can surface them and accepts an explicit `memory_tree` (the
worktree wrapper passes the memory worktree) and safely skips sidecars that do
not resolve under that tree rather than reporting false stale findings;
`validate_onboarding_refresh_plan_for_context` wires it into the worktree
closeout path before the code commit.

Route overviews get the same body gate scoped by domain evidence. The refresh
plan includes both overviews whose `sourceRoute` contains a current-leaf code
path and overview documents changed in the memory worktree since the task's
verified memory baseline. The latter closes the synced-source deadlock: a
curator may repair older route drift during this task even when the source
change predates the leaf's current code range, and closeout will validate and
stamp that authored overview in the same transaction.

`validate_memory_refresh_attestations` composes the existing sidecar and nearest-governing
route-overview body gates independently, aggregates both classifications, and raises one
refresh-validation error if either surface refuses (`onboarding.py:865-943`). The legacy helper path
therefore shares its current-memory body/history/no-impact
checks instead of accepting a green result from only one surface.

Direct task editing is itself domain evidence for those baseline-relative
overview candidates. Their body/history gate therefore still rejects an
unchanged or metadata-only document and requires substantive route prose plus
history (or the existing specific no-route-impact disposition); it does not
turn changed-memory membership into a blanket attestation. The one generated
exception is a pure citation-coordinate refresh: `_citation_coordinates_only_changed`
normalizes only complete final reference-table cells shaped as
`path:line[-line]`, so a sanctioned citation-fixer range shift can be stamped
without inventing an Update History claim. Any changed prose, anchor, path,
table shape, non-reference cell, or other body content remains visible and
therefore still needs truthful history.

`_nearest_governing_route` picks the longest matched route per changed path
(`.` loses to any deeper route); `classify_route_overview_updates` classifies
only those nearest-governing overviews as stale / untraced / attested (including still-recognized
historical `No route impact:` markers), while ancestor-matched overviews — including the repo-root
overview matched by happenstance — are collected as
`stamped_without_body_review` (skipped when their body was reviewed anyway) and
never gate closeout.

Since 260731-EFA-L2 that classification is three named steps, and
`classify_route_overview_updates` is just the loop that appends each returned bucket name:

- `_overview_revision(overview_path, *, memory_root, baseline_ref, changed_memory)` → `(body
  meaningfully changed, history lines added, citation-coordinates-only) | None`. **`None` is not a verdict** — it means the
  overview is outside the memory tree or absent from the baseline, neither of which is a stale
  signal, so those overviews drop out of the classification entirely.
- `_governing_overview_bucket(..., allow_citation_only, citation_only)` → the gating bucket for
  a domain-evident overview: `None` once it is properly updated (body changed *and* history added),
  or for an allowed task-edited citation-coordinate-only refresh; otherwise
  `untraced` / `attested_no_impact` / `stale`.
- `_route_overview_bucket(overview_path, *, memory_root, baseline_ref, changed_memory,
  evidence)` → the bucket for one matched overview. Source and task-edited evidence
  classify like a sidecar, with the citation-only exception restricted to the
  latter; an ancestor match returns
  `stamped_without_body_review` when its body went unreviewed, and `None` otherwise.

`OnboardingBodyGateEvidence` groups the memory tree, verified-memory baseline, and candidate-bound
accepted identities at the body-gate boundary. `refresh_onboarding_metadata(contract, change)`,
`refresh_onboarding_metadata_for_context(context, change, *, memory_tree=None,
memory_verified_commit="", accepted_no_impact=...)` and
`refresh_route_overview_metadata_for_context(context, change, *, memory_tree=None,
memory_verified_commit="", accepted_no_impact=...)` all take a `VerifiedChange` (from
`modules.models`)
in place of the separate `changed_paths` / `verified_commit` / `verified_date` / `working_paths`
arguments, so a refresher cannot stamp one commit's hash beside another's path list.
`require_updated_route_overview_content` applies only matching candidate-bound no-route-impact
decisions, then raises on remaining stale/untraced content and returns accepted routes;
`validate_route_overview_refresh_plan_for_context` runs it (with `memory_tree`
and `memory_verified_commit` plumbed from the worktree wrapper) before the code
commit. New overview files absent from the verified baseline pass without
classification.

MX-FIX-4 keeps route-index authority attached to that same resolved context:
both preview and apply pass `context.storage` explicitly to
`build_route_indexes()`. Closeout therefore cannot generate derived memory
using a different path-rule interpretation from the refresh plan it validated.

`validate_onboarding_refresh_plan_for_context` now takes its missing/unsupported refusal from
`_require_onboarded_sources` (same text). Since MIK-R30 a converted memory tree is dispatched to
`onboarding_trace_gate_for_context` / `validate_onboarding_traces_for_context` instead of the Update History
body gates above, and gets no verification stamps; see the section "260928-MIK-L30 The Converted-Tree
Dispatch (MIK-R30)".

### Conventions

This module owns closeout orchestration and classification; shared Markdown
parsing stays in `kernel/onboarding_doc.py`, deterministic source census stays
in `kernel/route_index_census.py`, and rendering stays in
`kernel/route_index.py`.

#### Invariants And Boundaries

- Sidecar and nearest-governing overview body/history gates run before code
  commit; ancestor overviews are reported but do not become false blockers.
- A route overview changed since the verified memory baseline is planned and
  body-reviewed even when its source drift predates the current leaf code range.
- Baseline-relative membership supplies domain evidence, not permission for a
  metadata-only stamp; stale and untraced authored overviews still refuse.
- Only task-edited overview changes confined to generated citation coordinates
  may pass without invented history; substantive body and reference-identity
  changes remain gate-visible.
- Working-tree missing onboarding blocks, while transported committed-range
  gaps remain explicitly reported as `unonboarded`.
- Route-index preview and apply must use the exact `context.storage` authority
  resolved for the refresh plan; no builder default may replace it.
- Generated indexes and entity fingerprints are derived after their owning
  authored bodies are validated.

### Todos

None known for the MX-FIX-4 closeout caller boundary.

## 260928-MIK-L30 The Converted-Tree Dispatch (MIK-R30)

MIK-R30 introduced converted-tree trace entry points alongside the retained legacy helpers; MIK-R53
now source-binds their answers. The older worker/reviewer base-against-worktree result on an
unconverted ICR L47 clone is historical, not fresh execution or present permission to use that
branch. MIK-R46 ordinary unconverted operations refuse with the conversion step.

- **`converted_onboarding(context, memory_tree=None)`** is true when the memory tree holds
  `knowledge/layout.json`. On such a tree `refresh_onboarding_metadata_for_context` and
  `refresh_route_overview_metadata_for_context` return `[]` before planning: a converted card or overview
  carries no `lastVerifiedCommit*` metadata (MIK-R30 rule 5).
- **`_require_onboarded_sources`** is today's missing/unsupported sidecar refusal, factored out of
  `validate_onboarding_refresh_plan_for_context` with the same message, so both gates share it.
- **`onboarding_trace_gate_for_context(context, changed_paths, sides, inputs)`** is the
  curator's memory-quality entry point: it never raises, and returns the `OnboardingTraceResult` and its
  repair findings (one per missing trace, one per unreadable input). `inputs` is one
  `OnboardingTraceInputs` value object carrying the candidate `code_blobs` (each changed path's blob,
  or `None` for a deletion), the leaf worklist run's `identicalChanges` and the `working_paths`; both
  the blobs and the groups are forwarded to `onboarding_trace_result`, and the shared
  missing-onboarding refusal is prepended as a `memory-refresh-attestation-failed` finding when it
  applies.
- **`validate_onboarding_traces_for_context(..., inputs)`** is the closeout validator's entry
  point with the same inputs object: it runs the shared missing-onboarding refusal, forwards the
  candidate blobs and the run's groups, then raises `RuntimeError(result.refusal())` naming every
  missing trace.
- **`identical_changes_from_run(document)`** is the one strict reader of a run's `identicalChanges`
  (MIK-R177). A non-mapping map, a non-string or empty key, a non-list entry, a member that is not a
  non-empty string, an empty member list and a group that omits its own representative each raise
  `IdenticalChangesUnreadable` naming the entry; nothing is dropped or coerced, so a malformed group
  can never shorten into a one-source item. A genuine empty mapping stays empty and each group keeps
  the run's order.
- **Why the groups are a required input (MIK-R177).** The gate builds its items with the same
  identical-copy groups `worklist_onboarding` uses, so an item a card row answers in the worklist is
  the item the gate raises. `identical_changes` carries no default, so no caller can judge ungrouped
  items by omission; a caller that cannot read a complete run's groups refuses by name instead.
- **Who dispatches.** `controller._onboarding_refresh_gate` and `prepared_certification._realize_prepared_memory`
  call these only when `leaf_onboarding_trace_sides` returns sides; otherwise they call today's
  the retained legacy validators. Dispatch syntax is not permission to bypass the unconditional
  ordinary-operation refusal of unconverted memory.
- **Current ordinary-candidate rule (MIK-R53).** Only an eligible source-current onboarding row
  answers: `updated` additionally requires a real counted Markdown/reference edit; `no_impact`
  covers an unchanged contract. Realizes/proves-only edits do not count, and later source movement
  reopens the answer. Curator-coherence no-impact does not substitute for that row. The older L30
  counted-edit-or-row ruling is historical; amended L53 rule 1 separately permits this leaf's own
  counted changed cards under the old MAIN-LINE producer, with no updated or changed-card
  no_impact/backfill. The old planned cutover deletion note predates MIK-R46 legacy retirement.

- A tree holding the layout marker is converted. [1]
- No route-overview stamps on a converted tree. [2]
- Today's missing-onboarding refusal, shared by both gates. [3]
- The converted memory-quality entry point requires and forwards candidate blobs and the run's identical-copy groups; it returns trace repair findings. [4]
- The converted closeout entry point requires the same inputs, then refuses missing traces. [5]
- No card stamps on a converted tree. [6]
- Both entry points evaluate source-current rows; updated also needs a counted Markdown/reference edit. [7]
- Historical fallback dispatch is retained internally; an ordinary unconverted leaf now refuses before either gate. [8]

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `contract_memory_verified_commit` chooses accepted memory content or the task base as the review baseline. [9]
- `_changed_memory_paths` combines dirty and committed-since-verified paths from that baseline. [10]

The retained legacy plan validator refuses missing or unsupported source sidecars before memory commit when reached (`validate_onboarding_refresh_plan_for_context`, mcp/src/agents_remember/worktrees/modules/onboarding.py:826-864). The metadata wrapper passes the verified change and accepted no-impact set into the context refresh (`refresh_onboarding_metadata`, mcp/src/agents_remember/worktrees/modules/onboarding.py:1069-1081). External closeout refreshes entity fingerprints before memory-content publication (`_refresh_external_memory`, mcp/src/agents_remember/worktrees/modules/closeout_external.py:121-147); the downstream cache is derived from attributed Git history and is not a body-review baseline. These contracts are source-backed; the removed support slices are not current test evidence.



- Drift checking verifies the same sidecar and entity fingerprint metadata maintained here. (`classify_entity_fingerprint`; `classify_sidecar_onboarding_units`) [11]
- Route-index refresh accepts the resolved storage authority and consumes one deterministic source snapshot. (`build_route_indexes`; `route_index_source_snapshot`) [12]

| Sidecar and route-overview attestations are checked independently and aggregated before refresh publication. (`validate_memory_refresh_attestations`) | L867-L942 | [mcp/src/agents_remember/worktrees/modules/onboarding.py](mcp/src/agents_remember/worktrees/modules/onboarding.py) |

### Cross-Repo References

Closeout can coordinate code and external-memory worktrees, but no external
implementation governs this module.

No additional cross-repository evidence applies.

- Current source delta inspected statically: Document required blobs and current-row doctrine; retain useful legacy-helper/history prose, not ordinary unconverted permission. [13]
