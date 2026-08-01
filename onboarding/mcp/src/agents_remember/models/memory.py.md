# mcp/src/agents_remember/models/memory.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/memory.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:34+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`memory.py` defines response models for drift, memory quality, route index,
memory initialization, baseline, and carryover MCP tools.

## Code Commentary

`DriftCheckResponse` (L13-L23) is strict because drift summaries have a stable
status, count, report, and actionable-sample shape. Its `status` (L18) is
`DriftStatus`, **imported** from
`memory_quality.integrity.onboarding_drift_check.models` (L14 there):
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Memory MCP controllers route these tools to drift, quality, route-index, init, baseline, and carryover services. | [memory_tools.py](agents-remember/mcp/src/agents_remember/controllers/memory_tools.py) |
| `DriftStatus` (L14) — the one declaration `DriftCheckResponse.status` and `DriftSummary.status` now share. | [onboarding_drift_check/models.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py) |
| The context-packet wire face of the same alias, which gained the matching `error` field this leaf. | [drift.py](agents-remember/mcp/src/agents_remember/models/drift.py) |

## Update History

- 2026-08-01T09:34+02:00 — 260731-EFA-L4 curator: body corrected. `DriftCheckStatus =
  Literal["notChecked", "checked", "error"]` — this module's local copy, the third in the package
  — is deleted; `DriftCheckResponse.status` (L18) now reads `DriftStatus` from
  `memory_quality.integrity.onboarding_drift_check.models` (L14 there). The Invariants line was
  also wrong on its face: it said "checked/not-checked/error", and the actual members are
  `notChecked` / `checked` / `error` — `not-checked` is `FreshnessSummary.status`, an unrelated
  vocabulary. Corrected the spelling and added the no-local-copy invariant. Citations:
  `DriftCheckResponse` pinned to L13-L23 and its `status` to L18; reference rows added for the
  producing models module (L14) and for `models/drift.py`, the sibling wire face that gained the
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
