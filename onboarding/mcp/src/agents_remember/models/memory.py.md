# mcp/src/agents_remember/models/memory.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`memory.py` defines response models for drift, memory quality, route index,
memory initialization, baseline, and carryover MCP tools.

## Code Commentary

L23 adds the flexible `CitationFixResponse` envelope, pinning the public operation discriminator while retaining guarded tool detail.

cit:([`DriftCheckResponse`], mcp/src/agents_remember/models/memory.py:15-29) is strict because drift summaries have a stable
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

## Evidence

### Repo-Internal References

- Memory-quality requests are executed by the focused controller. [1]
- Other memory MCP application entry points retain drift, citation, route-index, init, baseline, and carryover ownership. [2]
- The strict sync/start/poll request models and discriminated union. [3]
- `DriftCheckResponse.status` uses the shared `DriftStatus` alias. [4]
- `DriftSummary.status` uses the same shared `DriftStatus` alias. [5]
- The context-packet wire face includes its matching `error` field. [6]

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
