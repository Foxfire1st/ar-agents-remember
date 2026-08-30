# mcp/src/agents_remember/models/memory.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/memory.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-29T08:52+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`memory.py` defines response models for drift, memory quality, route index,
memory initialization, baseline, and carryover MCP tools.

## Code Commentary

L23 adds the flexible `CitationFixResponse` envelope, pinning the public operation discriminator while retaining guarded tool detail.

cit:([`DriftCheckResponse`], mcp/src/agents_remember/models/memory.py:13-27) is strict because drift summaries have a stable
status, count, report, and actionable-sample shape. Its cit:(["status: DriftStatus"], mcp/src/agents_remember/models/memory.py:19-19) is
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
| Memory-quality requests are executed by the focused controller. | `run_memory_quality_request`; `start_memory_quality_request`; `poll_memory_quality_request` | mcp/src/agents_remember/application/memory_quality/controller.py:67-144 |
| Other memory MCP application entry points retain drift, citation, route-index, init, baseline, and carryover ownership. | `drift_check_tool`; `citation_fix_tool`; `route_index_refresh_tool`; `memory_init_tool`; `memory_baseline_status_tool`; `memory_baseline_adopt_tool`; `memory_carryover_plan_tool`; `memory_carryover_apply_tool` | mcp/src/agents_remember/application/memory_tools.py:66-85; mcp/src/agents_remember/application/memory_tools.py:182-212; mcp/src/agents_remember/application/memory_tools.py:253-304; mcp/src/agents_remember/application/memory_tools.py:352-409 |
| The strict sync/start/poll request models and discriminated union. | `MemoryQualitySyncRequest`; `MemoryQualityStartRequest`; `MemoryQualityPollRequest`; `MemoryQualityCheckRequest` | mcp/src/agents_remember/models/memory.py:102-105; mcp/src/agents_remember/models/memory.py:108-111; mcp/src/agents_remember/models/memory.py:114-122; mcp/src/agents_remember/models/memory.py:125-125 |
| The typed controller fills the run envelope and guidance. | `run_memory_quality_request`; `start_memory_quality_request`; `poll_memory_quality_request` | mcp/src/agents_remember/application/memory_quality/controller.py:67-144 |
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

## Update History

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
