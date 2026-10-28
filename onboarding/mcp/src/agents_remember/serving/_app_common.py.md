# mcp/src/agents_remember/serving/_app_common.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Shared serving collaborators, the runtime bundle, and projection/SSE helpers. This module carries optional review and reader ports across the layering boundary; it owns no terminal route bodies, WebSocket bridge, inbox registrar or capsule-launch resolver.

## Code Commentary

Composition carries application-tier explainer ports, native host and master-contract resolver without a serving-to-cli/application import; absence is surfaced as a named unavailable route rather than partial composition.

ServingCollaborators holds the distinct subject-review, entry-list, source-content, intent-summary, tree-view and path-reader ports plus tree-view shutdown and extra-route hooks. It now also declares `review_memory_root: ReviewMemoryRootPort | None = None`; `_ServingRuntime` carries the same optional field. The imported alias is a three-string callable returning `Path | None`, not admission logic. An omitted port is a missing capability, not an empty result. The runtime contains configuration, projector, clock, build, interval, the optional memory-root capability and the tree-child shutdown hook; it is not a terminal host. LiveProjectionInputs resolves unset landing/change-watch toggles from the replay seam. The projection dump is memoized by published instance, copied before the serve-time build tail, and reused for SSE snapshots; deltas remain individual nodes. Optional `host_activity_reconcile` supplies the config-bound full-host boot reconciliation port; omission leaves activity unknown rather than proving absence. Each runtime owns its `TaskDocumentBodyCache`. Conditional-read ETag parsing now belongs to `conditional_read`, not this helper module.

The projection stream route passes the runtime's memory-root capability to `multiplex_review_memory`. With no review identity, that helper streams ordinary events without resolving a root. A supplied identity is checked before root resolution; a missing adapter or unadmitted root produces a review-memory error event while ordinary events continue. The native worker separately checks that the root is an existing canonical non-symlink directory outside provider-runtime.

The shared runtime also carries the optional background ledger. Routes, projection owners and background loops use that same account; the runtime bundle does not restore a terminal host or notifier owner.


**L184 — NEW-LIMIT-FROM-REPORT-ONLY, boundary corrected.** A non-JSON value here would break a served response, not the projection tick: these functions prepare HTTP and SSE bodies, and their JSON mode keeps a `JSONResponse` or an SSE frame from failing on a datetime. The tick's persisted write belongs to `projection_store`, and the stable-delta decision has its own dump boundary; the earlier sentence that laid every tick's failure at this module's door was wrong. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence boundary

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs




- Anchor: Optional review/reader collaborators, distinct missing-port capabilities.





- Anchor: Current tree-child shutdown hook on collaborator and runtime.

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/_app_common.py:162-231 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 662b6266e0e4662acd043c39365bb17969ea6ff9. Retired means the anchor no longer stands, not that the cited subject was deleted [13]





- Anchor: Runtime without a terminal host or inbox registrar. [14]


- [15]



- Anchor: Projection memo keyed by published instance, not content revision. [16]





- Anchor: SSE snapshots copy the memo and inject the serve-time build tail; deltas stay bare. [17]





- Anchor: Remaining collaborator fields, not the removed compiler/terminal seams.





- Anchor: Distinct optional intent-summary port. [22]






- Anchor: Distinct tree-view port and its shutdown hook.





- Anchor: Path-reader capability separate from task review. [24]






- Anchor: The retained runtime bundle shared by routes and loops. [27]





- Anchor: Snapshot-only volatile serving build tail. [28]





- Anchor: Source-content capability is not an empty-content fallback. [30]




## Evidence

- Serving lifespan teardown invokes a supplied review_trees_shutdown hook through the startup-owned worker helper before canceling and draining background tasks. [20]

- ServingCollaborators and _ServingRuntime newly declare optional review_memory_root defaulting to None. ReviewMemoryRootPort is only a callable type alias. The projection stream route explicitly passes the runtime field to multiplex_review_memory. That helper skips root resolution for absent review identity, validates supplied selectors, resolves the port and reports missing adapter/root errors. The native worker enforces its own root-shape checks. These bodies do not prove the composition root's full leaf-admission policy.

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/_app_routes.py:161-174 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/serving/review_memory_watch.py:199-230 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848; mcp/src/agents_remember/serving/review_memory_watch.py:53-84 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848. Retired means the anchor no longer stands, not that the cited subject was deleted [31]

- Composition carries application-tier explainer ports, native host and master-contract resolver without a serving-to-cli/application import; absence is surfaced as a named unavailable route rather than partial composition. [32]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/_app_common.py:169-253 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit de5a7adbb21b2f6f22c3ced0eed9dd7189fe93c7; mcp/src/agents_remember/serving/_app_common.py:162-231 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 662b6266e0e4662acd043c39365bb17969ea6ff9; mcp/src/agents_remember/serving/_app_common.py:219-227 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit b52adc8bc0564f6328d3543e48998e9235f1e417. Retired means the anchor no longer stands, not that the cited subject was deleted.

## Retirements

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/_app_common.py:162-231 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 662b6266e0e4662acd043c39365bb17969ea6ff9. Retired means the anchor no longer stands, not that the cited subject was deleted.

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/_app_routes.py:161-174 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/serving/review_memory_watch.py:199-230 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848; mcp/src/agents_remember/serving/review_memory_watch.py:53-84 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848. Retired means the anchor no longer stands, not that the cited subject was deleted.
