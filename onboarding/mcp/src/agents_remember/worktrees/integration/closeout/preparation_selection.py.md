# mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46:58+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Owning overview](overview.md)

## Purpose

Canonical lifecycle selection for private preparation evidence.

## Code Commentary

### Logic

`_require_preparation_certificates` checks four exact original code certificates for every intent and the selected fifth certificate for memory legs. These requirements apply to admitted private closeout preparation; they do not impose a gate prerequisite on interactive memory-quality preparation.

This owner loads exact content-addressed intent/output objects, binds operation/generation and original selected certificate predecessors, and applies single journal compare-and-swap transitions. Command start is selected before launch. Output selection checks the original raw commit relationship. Logical refs are independently observed; private commands and objects do not consume approval or prove published commits.

### Conventions

Use the named source owners directly. The implementation is present in landed IAS; this preparation pass does not advance verification stamps.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `selected_preparation_intents` owns the corresponding behavior described above. | `selected_preparation_intents` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py:34-54` |
| `select_preparation_intent` owns the corresponding behavior described above. | `select_preparation_intent` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py:57-80` |
| `_require_intent_owner` owns the corresponding behavior described above. | `_require_intent_owner` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py:196-212` |
| `_last` owns the corresponding behavior described above. | `_last` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py:215-218` |
| `_replace_last` owns the corresponding behavior described above. | `_replace_last` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py:221-231` |
| `_select` owns the corresponding behavior described above. | `_select` | `mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py:234-244` |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository source is needed for this card. | N/A | N/A |

## Update History

- 2026-09-06T21:46:58+00:00 — Reconciled landed IAS helper ownership and source anchors. Verification pins and historical evidence remain unchanged; no certification or delivery is asserted.

### 2026-09-06T17:13:06+00:00 — Initial L34 implementation card

Created from the current source. Verification metadata is intentionally unset until a genuine commit-based verification occurs; no test or acceptance result is asserted.
