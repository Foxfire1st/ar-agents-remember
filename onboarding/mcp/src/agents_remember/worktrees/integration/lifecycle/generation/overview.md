# Direct-Landing Generation Resume

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/lifecycle/generation/` |

## Governing Overview

[Parent overview](../overview.md)

## Purpose

This package defines the pure resume transition for a retained direct-landing generation. The lifecycle control and store layers own admission and persistence.

## Hot Path Summary

Use `resume.py` to advance a retained direct-landing generation's attempt while preserving its accepted input and mutation evidence.

## How It Is Built

`requeued_same_generation` returns a modified copy of the retained record. It increments the attempt and clears completion, failure, guidance and cancellation fields. The copy uses status `running` and phase `direct-preflight`.

| Source File | Onboarding | Role |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | Documentation-only namespace |
| `resume.py` | [resume.py.md](resume.py.md) | Pure retained-generation resume transition |

## Invariants And Boundaries

- The transition returns a copy. Journal validation and persistence remain with the lifecycle store.
- Resume preserves generation identity, task intent and immutable accepted input.
- Only mutation legs in `reconciled-unchanged` state are archived into mutation history and reset to `pre-mutation`, clearing their before, observed and expected-output-tree fields. Proven output remains retained.

## Evidence

- The direct resume transition increments the attempt, keeps accepted intent and preserves proven outputs. [2]
