# mcp/src/agents_remember/controlplane/gate_decisions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/gate_decisions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Shared mutation service for addressed and lifecycle-scoped gate decisions.

## Code Commentary

### Logic

Module-level surface:

- `GateDecisionContext` (class, lines 30-37) — Stores, policy, and clock that make one gate decision atomic in meaning.
- `_target_gate` (function, lines 40-46)
- `_require_undelegated_cli_decision` (function, lines 49-54)
- `_evidence_refs` (function, lines 57-58)
- `_meet_verdict_expectation` (function, lines 61-71)
- `_reclaim_gate_log` (function, lines 74-80) — Reclaim terminal history only in the process that owns gate compaction.
- `record_gate_decision` (function, lines 83-128) — Apply one decision and return the shared raw gate response payload.
- `record_lifecycle_gate_decision` (function, lines 131-156) — Resolve a lifecycle's latest open gate, then apply the shared decision service.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `GateDecisionContext` (lines 30-37) — Stores, policy, and clock that make one gate decision atomic in meaning.. | `GateDecisionContext` | mcp/src/agents_remember/controlplane/gate_decisions.py:29-37 |
| Defines the function `_target_gate` (lines 40-46). | `_target_gate` | mcp/src/agents_remember/controlplane/gate_decisions.py:40-46 |
| Defines the function `_require_undelegated_cli_decision` (lines 49-54). | `_require_undelegated_cli_decision` | mcp/src/agents_remember/controlplane/gate_decisions.py:49-54 |
| Defines the function `_evidence_refs` (lines 57-58). | `_evidence_refs` | mcp/src/agents_remember/controlplane/gate_decisions.py:59-60 |
| Defines the function `_meet_verdict_expectation` (lines 61-71). | `_meet_verdict_expectation` | mcp/src/agents_remember/controlplane/gate_decisions.py:61-71 |
| Defines the function `_reclaim_gate_log` (lines 74-80) — Reclaim terminal history only in the process that owns gate compaction.. | `_reclaim_gate_log` | mcp/src/agents_remember/controlplane/gate_decisions.py:74-80 |
| Defines the function `record_gate_decision` (lines 83-128) — Apply one decision and return the shared raw gate response payload.. | `record_gate_decision` | mcp/src/agents_remember/controlplane/gate_decisions.py:83-128 |
| Defines the function `record_lifecycle_gate_decision` (lines 131-156) — Resolve a lifecycle's latest open gate, then apply the shared decision service.. | `record_lifecycle_gate_decision` | mcp/src/agents_remember/controlplane/gate_decisions.py:131-156 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: normalized decorator-inclusive citation ranges via scoped --fix against the frozen snapshot.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
