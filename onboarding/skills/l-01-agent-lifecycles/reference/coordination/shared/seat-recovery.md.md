# skills/l-01-agent-lifecycles/reference/coordination/shared/seat-recovery.md

## Governing Overview

[overview](../../../overview.md)

## Purpose

The rules Managers, Architects and Orchestrators follow, within their assigned scope, for recovering idle, unfinished, stopped or unavailable-provider work. It grants no additional authority.

## Code Commentary

When every agent of a leaf is idle, the coordinator reads each agent's last lines; a seat whose turn ended silently while helpers or a process it started still run is told to collect its results and finish, while a valid declared helper or background wait (`WAITING FOR SUBAGENTS:` or `WAITING FOR BACKGROUND:`) stays a wait until its next undeclared end. A developer-stopped or archived seat is restarted or replaced only on the developer's explicit word, and replacement never discards work: the successor saves the worktree state as evidence and its freeze names each change kept, rewritten or removed. When a provider is unavailable, its work moves in the same turn to an available model through an already authorized fallback role set, with replacement seats started by `role_start`; a defaults switch goes upward (the Manager to the Architect, the Architect under direct coordination to the developer) without waiting or probing. A developer-specified model or unapproved substitute needs the developer's decision first, and a safety refusal is handled through the same model-change authority instead of retrying the refused model. The Architect, Orchestrator and Manager roles each point here before recovering such work.

## Evidence

- Idle leaves are read first, and a silent turn with running helpers or a process the seat started is told to collect its results and finish, while a declared helper or background wait stays a wait. [1]

- Stopped or archived seats change only on the developer's word, and replacement preserves the predecessor's work. [2]
- Unavailable-provider work moves through an authorized fallback role set, and other model changes go up for decision. [3]
