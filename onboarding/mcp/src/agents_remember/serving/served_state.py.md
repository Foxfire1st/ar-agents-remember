# mcp/src/agents_remember/serving/served_state.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/served_state.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-15T20:42+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`       |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[serving overview](overview.md)

## Purpose

Declares the workspace state body emitted by `/api/state` and SSE snapshots: the observer projection plus serving-process identity, response-time notifier heartbeat facts, and the observer stage's own health reading.

## Code Commentary

### Logic

`ServedWorkspaceProjection` extends the observer projection with four optional keys: `servingBuild`, `agentNotifierHeartbeat`, the retained `supervisorHeartbeat` rename alias, and `terminalObserverHealth` (`LOCR-R17@v1`). `SERVED_TAIL_FIELDS` lists exactly that extension. `served_state_tail` emits both heartbeat names from the same payload, and it emits the observer-health payload under the `servingBuild` rule rather than the heartbeat rule: a caller with no valid record for the CURRENT serving lifetime has nothing honest to report, so the key is ABSENT rather than null, and no other served field changes value or meaning. Once present, that payload carries its own explicit nulls (`lastAttemptAt: null` is a reported fact about this lifetime). An absent build or absent heartbeat object likewise emits no corresponding key; inside an existing heartbeat payload, unknown/never-ticked fields remain explicit nulls. Build fields use `exclude_none=True`. cit:([`ServedWorkspaceProjection`, `SERVED_TAIL_FIELDS`, `served_state_tail`], mcp/src/agents_remember/serving/served_state.py:50-109).

### Invariants And Boundaries

- The tail is computed at serve time and merged onto a copy of the memoized projection dump.
- It does not enter `WorkspaceProjection` or persisted `latest-state.json`.
- Response-time age changes do not change the content revision/ETag, preserving body-free 304 responses. The observer-health tail is per-response arithmetic on a persisted row, so it must never enter the memoized body or the projector's content revision either.
- Only full SSE snapshots receive the tail; per-entity delta events carry none.
- The separate dumps preserve omitted build facts and explicit heartbeat nulls without re-parsing the entire projection on every request.
- `terminalObserverHealth` is additive and omissive: absence is the declared answer whenever no valid record for the current serving lifetime exists, and a served read never rewrites, repairs, creates or deletes that record. With the key present, every pre-existing served field stays byte-identical — the change is exactly one extra key.
- The historical dedicated conformance matrix was removed by the retained-test cleanup; its old enforcement claim is not current protection. That gap is now partly re-covered for this tail: `mcp/tests/test_terminal_observer_health.py::TerminalObserverHealthServedTailTests` drives the real `_state_response` handler and the real `stream_events` generator, including the ETag/304 branch and the snapshot/delta asymmetry.

### Conventions

These are declared wire names. The module composes existing build and heartbeat payload types rather than owning their measurements.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Serving-only fields extend the observer model and remain outside its persisted shape. | `ServedWorkspaceProjection` | mcp/src/agents_remember/serving/served_state.py:50-66 |
| One assembly point preserves both omission and null semantics, including the observer-health key's absent-versus-null rule. | `served_state_tail` | mcp/src/agents_remember/serving/served_state.py:78-109 |
| The tail's exact key list, so assembly and contract cannot drift apart silently. | `SERVED_TAIL_FIELDS` | mcp/src/agents_remember/serving/served_state.py:68-75 |
| The declared wire form of the fourth key. | `TerminalObserverHealthPayload` | mcp/src/agents_remember/serving/terminal_observer_health.py:177-191 |
| The served-tail cases that drive this assembly through the production route handler and stream generator. | `TerminalObserverHealthServedTailTests` | mcp/tests/test_terminal_observer_health.py:734-931 |

## Docs References

No Domain Documentation source is configured.

## Cross-Repo References

No external repository boundary governs this assembly.

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `served_state_tail` repointed to mcp/src/agents_remember/serving/served_state.py:78-109. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`,
  base `99534dc5`, `served_state.py` +25/−7): the tail gained its fourth key, so this card's current
  contract was corrected in the body rather than annotated. `ServedWorkspaceProjection` now declares
  `terminalObserverHealth` beside `servingBuild` and the two heartbeat names, `SERVED_TAIL_FIELDS`
  lists four keys, and `served_state_tail` takes an optional `observer_health` argument that follows
  the **`servingBuild` rule rather than the heartbeat rule**: a caller with no valid record for the
  current serving lifetime gets an ABSENT key, never a fabricated status and never another
  lifetime's bytes, while a present payload carries its own explicit nulls. Recorded the two
  invariants that make that safe: the observer-health reading is per-response arithmetic on a
  persisted row, so it must not enter the memoized body or the projector's content revision (the
  ETag/304 path is unchanged), and a served GET/SSE never rewrites, repairs, creates or deletes the
  row — with the key present, the change is exactly one extra key and every pre-existing served
  field stays byte-identical. The retained note that the historical dedicated conformance matrix was
  removed is now partly re-covered: `test_terminal_observer_health.py::TerminalObserverHealthServedTailTests`
  drives the real `_state_response` handler and the real `stream_events` generator over the ETag/304
  branch and the snapshot/delta asymmetry. Reference ranges were re-derived against the candidate
  (`ServedWorkspaceProjection` `49-69` → `50-66`, `served_state_tail` `72-91` → `81-109`) and a
  `SERVED_TAIL_FIELDS` row was added. Verification metadata remains closeout-owned; no stamp advanced.

- 2026-09-06T22:06:54+00:00 — Reconciled the current three-key tail, omitted-object versus null-field semantics, and retired test-evidence claim. Original verification pins and history retained.


- 2026-08-30T17:08:05+02:00 — ARSPAWN-L4 Dagger repair: repointed the shared build-payload model
  to its bounded core-model home. Tail behavior is unchanged; verification remains closeout-owned.

- 2026-08-30T15:15:36+02:00 — 260821-ARSPAWN-L4: repointed the served-state tail to the shared
  `models.core` wire authority used by MCP `server_info`. Wire ownership changed; tail
  assembly semantics did not. Verification remains closeout-owned.

- 2026-08-02T20:43+02:00 — W2-B08: anchored 2 served-state consumer/conformance references with exact app and test anchors; ranges remain generated by the scoped fixer. Verification metadata stays pinned until closeout.

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): repaired the two
  `observer/projection.py` citations — the Purpose prose and the first reference row — after that
  module was restructured. cit:([`WorkspaceProjection`], mcp/src/agents_remember/observer/projection.py:1131-1153)
  points to the class and its `extra="forbid"` configuration. No body claim changed.

- 2026-08-01T08:05+02:00 — 260731-EFA-L4 curator: created for the new
  `serving/served_state.py`. Documented `ServedWorkspaceProjection` (the two serve-time keys
  that `/api/state` and the SSE `snapshot` were injecting into an already-dumped, undeclared
  dict), `SERVED_TAIL_FIELDS`, and `served_state_tail`'s deliberate two-dump split (build
  omitted via `exclude_none`, heartbeat nulled without it). Recorded the five reasons the tail
  is NOT a `WorkspaceProjection` field — layer, the `_ProjectionBodyCache` memo, the ETag
  revision, `latest-state.json`, and the snapshot-only shape — and that enforcement is
  `test_served_state_conformance.py` rather than per-request validation. Verification metadata
  is a placeholder pinned to the leaf base `abc7cbcc`; closeout stamps the real commit.
