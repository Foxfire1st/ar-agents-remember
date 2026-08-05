# mcp/tests/test_conversation_active_status.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_active_status.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Canonical status classification, revision discipline, and orchestration parity tests for
260718-CHATS-L1 (R3): proves the one evidence→vocabulary mapping, the semantic-only revision
rule, terminal-outcome handling, and that orchestration's seat projection reproduces the
pre-canonical mapping exactly.

## Code Commentary

### Logic

cit:([`ClassificationTests`], mcp/tests/test_conversation_active_status.py:73-165) pins the evidence classification per adapter state: pending
interaction → `pending-interaction`/exact with interaction id; blocked without interaction →
`declared-external-wait`; running → `active-native-turn` with the codex-only turn id (absent for
other harnesses); per-harness settling variants (claude compaction/retry, pi
compaction/auto-retry, generic reconciling); idle+ready → `settled-dispatchable`; unknown and
starting snapshots carry no turn evidence; and the process mapping (connected/starting/
disconnected/failed). cit:([`SeatParityTests`], mcp/tests/test_conversation_active_status.py:168-250) drives the full 5×5 control×activity
product through `snapshot_turn_state` (the delegated orchestration entry point) and proves
working/awaiting-input/turn-ended/stale in every cell matches the pre-canonical mapping, plus
the single projection rule's pending-interaction preference. cit:([`StatusServiceTests`], mcp/tests/test_conversation_active_status.py:253-355)
pins the revisioned envelope: honest initial waiting/unknown, revision advance only on semantic
change (identical observations keep the revision), terminal outcomes from native evidence, a
completed outcome surviving the settling → ready transition, needs-input carrying the
interaction id, lost authority keeping the last turn state while process evidence advances, and
unknown evidence never becoming `ready`.

### Conventions

Pure unit tests over the real classification/service with a fixed clock; no IPC, no projector.
The parity test deliberately exhausts the control×activity product instead of sampling it.

### Invariants And Boundaries

- Revision advances only on semantic transitions; timestamps never advance it.
- The seat projection rule is the only orchestration mapping — parity is proven, not assumed.
- Unknown evidence never becomes `ready` (model-enforced, here service-tested).

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries; the canonical vocabulary contract
is repository-owned and cited below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this suite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical status authority under test: classification, seat projection, revisioned service. | `classify_snapshot` | mcp/src/agents_remember/serving/conversation/active/status.py:153-162 |
| The delegated orchestration entry point driven by the parity suite. | `snapshot_turn_state` | mcp/src/agents_remember/serving/hosted_control_projection.py:78-101 |
| `CANONICAL_TURN_STATE_BY_EVIDENCE` fixes the vocabulary the classification tests pin. | `CANONICAL_TURN_STATE_BY_EVIDENCE` | mcp/src/agents_remember/serving/conversation/models.py:453-463 |

## Cross-Repo References

No cross-repository implementation participates in this suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260718-CHATS-L5I Current Delta

Status regressions now cover freshness classification against evidence-expected working states, so a quiet ready conversation is not marked stale while genuine active/settling loss still is.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 4 citation findings; scoped check passed.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation into
  `serving/conversation/active/status.py` (523 lines). Classification plus seat projection —
  `classify_process`, `classify_turn`, `classify_snapshot`, `seat_turn_state_for`,
  `snapshot_seat_turn_state` — now spans L101-L224, and the revisioned `ConversationStatusService`
  spans L306-L508. Was L91-L190; L252-L447.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/tests/test_conversation_active_status.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 12 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds. Noted while checking: the references table also cites line ranges inside
  `status.py`, `models.py`, `hosted_control_projection.py`; those ranges shifted because this task
  edited those files, so treat the cited numbers as approximate and the linked cards as
  authoritative.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the canonical
  status suite — classification, full-product orchestration parity, revision discipline (19
  tests). Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
