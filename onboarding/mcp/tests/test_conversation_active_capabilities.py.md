# test_conversation_active_capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_active_capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:18:47Z |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_conversation_active_capabilities.py` proves that the active-conversation capability view derives interrupt support from the control capability gate without weakening its conservative posture for other features.

## Code Commentary

### Logic

Parameterized cases assert fixture-backed `supported` interrupt capability for Codex, Claude, and Pi, including exact evidence identity. The suite verifies the L1 active view equals the L3 control verdict and monkeypatches the control source to prove a changed interrupt verdict flows through without a second local copy. Separate cases keep steer, follow-up, attachments, history, telemetry, and live-text/thinking verdicts at their harness-specific conservative states.

### Conventions

The minimal adapter snapshot is structural because the capability builders are contract-gated, not snapshot-promoted.

### Invariants And Boundaries

Only `controls.interrupt` bridges the control gate. The suite must not make runtime fixtures silently enable unrelated active-view features.

### Todos

No durable follow-up is recorded here.

## Docs References

The configured Domain Documentation registry has no entries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is configured for this repository-local capability suite. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The active view delegates its interrupt verdict to the control capability source. | L342-L360 | [active capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/capabilities.py) |
| The control view supplies the fixture-backed interrupt verdict and retains its other control boundaries. | L318-L355 | [control capabilities.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/capabilities.py) |

## Cross-Repo References

No meaningful cross-repository boundary participates in this suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Capability evidence and its active projection are repository-local. | — | — |

## Update History

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/tests/test_conversation_active_capabilities.py` since the L2 base commit is the whole-tree
  `ruff format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever.
  Checked by parsing both revisions and comparing the abstract syntax trees (identical) and the
  comment tokens (identical), so no symbol, signature, default, decorator, control-flow branch,
  docstring, or assertion this card describes has moved, and every claim this card makes about its
  own source still holds. Noted while checking: the references table also cites line ranges inside
  `capabilities.py`, `capabilities.py`; those ranges shifted because this task edited those files,
  so treat the cited numbers as approximate and the linked cards as authoritative.

- 2026-07-24T13:18:47Z — Created for 260718-CHATS-L5I: documented the single-source interrupt-capability bridge and its conservative non-interrupt regression matrix. Verification metadata remains empty until the code commit.
