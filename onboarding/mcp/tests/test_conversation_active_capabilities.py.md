# test_conversation_active_capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_active_capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:18:47Z |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for this repository-local capability suite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The active view delegates its interrupt verdict to the control capability source. | `_codex_capabilities`; `_claude_capabilities`; `_pi_capabilities` | mcp/src/agents_remember/serving/conversation/active/capabilities.py:112-200; mcp/src/agents_remember/serving/conversation/active/capabilities.py:203-248; mcp/src/agents_remember/serving/conversation/active/capabilities.py:251-339 |
| The control view supplies the fixture-backed interrupt verdict and retains its other control boundaries. | `_codex_controls`; `_claude_controls`; `_pi_controls` | mcp/src/agents_remember/serving/conversation/control/capabilities.py:145-173; mcp/src/agents_remember/serving/conversation/control/capabilities.py:176-209; mcp/src/agents_remember/serving/conversation/control/capabilities.py:212-237 |

## Cross-Repo References

No meaningful cross-repository boundary participates in this suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| Capability evidence and its active projection are repository-local. | — | — |

## Update History
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 2 table citations for the active-to-control interrupt bridge and harness control fixtures; fixer-generated ranges verified.

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
