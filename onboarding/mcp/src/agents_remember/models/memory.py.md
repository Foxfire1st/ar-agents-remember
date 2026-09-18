# mcp/src/agents_remember/models/memory.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/memory.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-18T19:22+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`memory.py` defines response models for drift, memory quality, route index,
memory initialization, baseline, and carryover MCP tools.

## Code Commentary

L23 adds the flexible `CitationFixResponse` envelope, pinning the public operation discriminator while retaining guarded tool detail.

cit:([`DriftCheckResponse`], mcp/src/agents_remember/models/memory.py:13-27) is strict because drift summaries have a stable
status, count, report, and actionable-sample shape. Its cit:(["status: DriftStatus"], mcp/src/agents_remember/models/memory.py:20-20) is
`DriftStatus`, **imported** from
`memory_quality.integrity.onboarding_drift_check.models`:
`notChecked | checked | error`. The local
`DriftCheckStatus = Literal["notChecked", "checked", "error"]` this module used
to declare was the last of three hand-copies of one vocabulary — identical in
content to the producer's, which is exactly why it was worth deleting: an
identical copy is not a safe copy, it is one more place for the next member not
to arrive. `models.drift.DriftSummary` reads the same alias, so the two wire
faces of drift status are now one declaration. Memory quality, route index,
initialization, baseline, and carryover responses use flexible tool envelopes
because their underlying service payloads still carry operation-specific
details. The carryover models document the 2.5.2 compact wire shape: both
declare optional `decisions` (source paths grouped by carryover decision) and
`reportPath` (the temp report holding the full candidate records), and the
apply model adds `carriedPaths` (paths whose onboarding actually carried).
`MemoryQualityCheckResponse` explicitly declares the optional leaf-checklist path, status, and
component counts even though the envelope remains flexible. Those fields exist only on a full
contract-scoped call; subset and official-memory calls omit them.
`RouteIndexRefreshResponse` likewise declares `staleIndexes`, so a dry-run's changed-index paths
are present in the agent-facing response schema instead of relying only on the flexible envelope.

For 260821-DAGQC-L2 the quality wire has one extra-forbid discriminated request union. `sync` and
`start` share only repository, normalized-check input, detail limit, and optional contract path;
`poll` permits only repository and run id. The response status vocabulary includes typed
`capacity-reached` and `run-not-found`, both with bounded guidance, in addition to live and terminal
run states.

## Invariants And Boundaries

- Drift status is constrained to the producer's three tool states, spelled
  `notChecked` / `checked` / `error` (camelCase `notChecked`, not
  `not-checked` — that hyphenated spelling is `FreshnessSummary.status`, a
  different vocabulary).
- That constraint is not declared here. `DriftStatus` is imported from the
  module that produces it; this model must not reintroduce a local copy, however
  identical.
- Flexible memory-service responses should still include the public operation
  name and shared token metadata.
- Checklist status is constrained to `action-required | ready-for-closeout`; all component counts
  are non-negative and omission remains the unscoped/subset meaning.
- `staleIndexes` is optional because older or non-preview route-index payloads may omit it; when
  present it is the list of index paths whose rendered bytes differ from the onboarding census.
- Request modes are exact and extra-forbid: no `wait`/`run_id` compatibility grammar or poll-time
  execution fields are accepted.
- `capacity-reached` carries no run id because no work was admitted; `run-not-found` remains
  nondisclosing across absent, evicted, restarted, and wrong-repository lookup.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Memory-quality requests are executed by the focused controller. | `run_memory_quality_request`; `start_memory_quality_request`; `poll_memory_quality_request` | mcp/src/agents_remember/application/memory_quality/controller.py:249-255; mcp/src/agents_remember/application/memory_quality/controller.py:258-264; mcp/src/agents_remember/application/memory_quality/controller.py:267-273 |
| Other memory MCP application entry points retain drift, citation, route-index, init, baseline, and carryover ownership. | `drift_check_tool`; `citation_fix_tool`; `route_index_refresh_tool`; `memory_init_tool`; `memory_baseline_status_tool`; `memory_baseline_adopt_tool`; `memory_carryover_plan_tool`; `memory_carryover_apply_tool` | mcp/src/agents_remember/application/memory_tools.py:66-85; mcp/src/agents_remember/application/memory_tools.py:182-212; mcp/src/agents_remember/application/memory_tools.py:253-304; mcp/src/agents_remember/application/memory_tools.py:352-416; mcp/src/agents_remember/application/memory_tools.py:318-332; mcp/src/agents_remember/application/memory_tools.py:418-435 |
| The strict sync/start/poll request models and discriminated union. | `MemoryQualitySyncRequest`; `MemoryQualityStartRequest`; `MemoryQualityPollRequest`; `MemoryQualityCheckRequest` | mcp/src/agents_remember/models/memory.py:102-105; mcp/src/agents_remember/models/memory.py:108-111; mcp/src/agents_remember/models/memory.py:114-122; mcp/src/agents_remember/models/memory.py:125-131 |
| The typed controller fills the run envelope and guidance. | `run_memory_quality_request`; `start_memory_quality_request`; `poll_memory_quality_request` | mcp/src/agents_remember/application/memory_quality/controller.py:249-255; mcp/src/agents_remember/application/memory_quality/controller.py:258-264; mcp/src/agents_remember/application/memory_quality/controller.py:267-273 |
| "status: DriftStatus" is the shared status declaration. | "status: DriftStatus" | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:14-14 |
| `DriftCheckResponse.status` uses the shared `DriftStatus` alias. | `DriftCheckResponse` | mcp/src/agents_remember/models/memory.py:13-27 |
| `DriftSummary.status` uses the same shared `DriftStatus` alias. | `DriftSummary` | mcp/src/agents_remember/models/drift.py:13-23 |
| The context-packet wire face includes its matching `error` field. | `DriftSummary`; `error` | mcp/src/agents_remember/models/drift.py:13-23 |

## 260815-DAG-L3 Attestation Response Field

`MemoryQualityCheckResponse` now exposes optional `attestationPath`, pairing the structured curator
readiness artifact with the existing rendered checklist path and zero/actionable counters.

## 260821-DAGQC-L2 Canonical Memory-Quality Request

The public request is exactly one discriminator-selected object. `sync` and `start` carry execution
inputs; `poll` carries only `repo_id` and `run_id`. Extra fields are refused by the models, so the
registration, payload adapter, controller, and published schema share one grammar. The response adds
`capacity-reached` and bounded guidance without inventing an admitted run.

## MCAR-L02 Combined Quality Response

`MemoryQualityResponse` now carries raw `qualityChecklistStatus`, combined `checklistStatus`,
`coherenceStatus`, canonical authority path, coherence record digest, and `closeoutReady`. These
cells make it impossible to serialize an apparently ready combined response without the shared
coherence validator accepting the exact candidate.

## MCAR-L03 Memory-Quality Wire Shape

Candidate responses declare scope authority, acceptance eligibility, the exact pair, and bounded
pair-refusal evidence. Candidate poll accepts the one original contract path; official poll omits
it. `scope-refused` is terminal domain evidence and is never rewritten as a successful completion.

## KS-R23@v1 The Counts Name Their Ruler

D-33 measured that the MCP tool surface executes a **fixed** serving build while the candidate under
measurement carries different code, and that nothing in the output let a reader tell the two apart — so
for the changes that touch the measuring machinery itself, a tool-produced count could not show the fix.
The three response models that report a measurement now declare the ruler: `servingBuild` is
`ServingBuildPayload | None` on `MemoryQualityCheckResponse` (`:84`), on `CitationFixResponse` (`:143`)
and on `CitationMigrateResponse` (`:164`), stamped by `measuring_build_stamp()`
(`mcp/src/agents_remember/application/runtime/startup.py:36-51`) at the memory-quality controller's
three public entry points and in both citation tools
(`mcp/src/agents_remember/application/memory_tools.py:246`, `:283`).

It is **declared** rather than left to the flexible envelope, by this package's own rule in
`models/base.py` — *what this package writes, this package declares*: `FlexibleToolResponse` sets
`extra="allow"`, so an undeclared stamp would validate and stay invisible in the tool's own schema.
`drift_check` deliberately carries no stamp: it is a tree-integrity count rather than a curation count,
and D-33 names the memory-quality and citation surfaces.

## Update History
- 2026-09-18T19:55:32+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document** (two table rows). (a) The request-model row's last range `125-125` (`mode: Literal["poll"]`) stopped six lines above `type MemoryQualityCheckRequest = Annotated[…` at `131`; it was widened to `125-131`. (b) The entry-point row cited `memory_tools.py:352-409` for `memory_carryover_plan_tool`, whose definition is at `416`; the range was widened to `352-416`, so the tail of the cited span is the entry point the claim names. Claims, anchors and every other range are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `run_memory_quality_request`; `start_memory_quality_request`; `poll_memory_quality_request` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:249-255; mcp/src/agents_remember/application/memory_quality/controller.py:258-264; mcp/src/agents_remember/application/memory_quality/controller.py:267-273. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `run_memory_quality_request`; `start_memory_quality_request`; `poll_memory_quality_request` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:249-255; mcp/src/agents_remember/application/memory_quality/controller.py:258-264; mcp/src/agents_remember/application/memory_quality/controller.py:267-273. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "status: DriftStatus" repointed to mcp/src/agents_remember/models/memory.py:20-20. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T19:22+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **recorded the three `servingBuild` declarations this leaf's item 26 added, which this card did not mention.** `MemoryQualityCheckResponse` (`:84`), `CitationFixResponse` (`:143`) and `CitationMigrateResponse` (`:164`) each declare `servingBuild: ServingBuildPayload | None`, stamped from `measuring_build_stamp()` at the controller's three public entry points and in `citation_fix_tool`/`citation_migrate_tool`; the section above states why the field is declared on the model rather than left to the flexible envelope, and that `drift_check` is deliberately excluded. Read against the delivered but **uncommitted** working tree, so the verification stamp is not advanced: no commit carries these bytes and closeout stamps the real code commit. The existing reference rows were left untouched for the citation-range repair pass that owns them.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored both controller request-surface rows (67-144 to 98-208) shifted by the CCR-R08 +57-line controller insertion. Citation-only re-anchor; no content impact.

- 2026-08-29T21:46+02:00 — MCAR-L03: exposed exact pair identity/refusals and contract-bound poll
  input on the memory-quality wire. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Added typed raw-quality and structured-coherence readiness fields.
  Verification remains closeout-owned.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: replaced the optional flat wait/run-id grammar with strict discriminated sync/start/poll request models; added typed capacity refusal and guidance fields. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: `MemoryQualityCheckResponse` gained the optional async
  `status` (`started`/`running`/`completed`/`failed`/`run-not-found`) and `runId` fields (L15-R7);
  the synchronous shape is unchanged. Verified at code commit de3a0fd9.

- 2026-08-15T09:10+02:00 — L3 content update: added the structured curator attestation path to
  the memory-quality response model; verification remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T17:26+02:00 — L19 report-folder delta: exposed
  `RouteIndexRefreshResponse.staleIndexes` in the agent-facing schema so the curator checklist can
  name exact route-index work; verification metadata remains pinned for governed closeout.
- 2026-08-11T16:54+02:00 — Declared the full scoped curator-checklist path, status, and component
  counts on the memory-quality wire model without changing subset or official-memory payloads.
- 2026-08-11T14:40+02:00 — Re-read the application memory-tool surface after its scoped-quality
  extension and regenerated every shifted entry-point range; this response-model contract is unchanged.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T15:32:44+02:00 — 260731-EFA-L6 S18-B08 curator: split the shared status declaration from both response consumers and the context-packet error field, with regenerated model extents.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:34+02:00 — 260731-EFA-L4 curator: body corrected. `DriftCheckStatus =
  Literal["notChecked", "checked", "error"]` — this module's local copy, the third in the package
  — is deleted; `DriftCheckResponse.status` (cit:(["status: DriftStatus"], mcp/src/agents_remember/models/memory.py:19-19)) now reads `DriftStatus` from
  `memory_quality.integrity.onboarding_drift_check.models`. The Invariants line was
  also wrong on its face: it said "checked/not-checked/error", and the actual members are
  `notChecked` / `checked` / `error` — `not-checked` is `FreshnessSummary.status`, an unrelated
  vocabulary. Corrected the spelling and added the no-local-copy invariant. Citations:
  `DriftCheckResponse` pinned to cit:([`DriftCheckResponse`], mcp/src/agents_remember/models/memory.py:13-27) and its `status` to cit:(["status: DriftStatus"], mcp/src/agents_remember/models/memory.py:19-19); reference rows added for the
  producing models module and for `models/drift.py`, the sibling wire face that gained the
  matching `error` field this leaf. Verification metadata pinned until closeout stamps the L4
  commit.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/models/memory.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-10T09:00+02:00 — Carryover plan/apply models gained documented optional `decisions`/`reportPath` (plus `carriedPaths` on apply) for the 2.5.2 response compaction (GitHub #52).
- 2026-05-28T19:52+02:00: Created for memory and onboarding response contracts.
