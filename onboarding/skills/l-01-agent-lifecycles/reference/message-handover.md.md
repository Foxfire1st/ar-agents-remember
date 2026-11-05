# skills/l-01-agent-lifecycles/reference/message-handover.md

## Governing Overview

[governing overview](../overview.md)

## Purpose

Owns sender notification and receipt handling when another seat waits on a finished step.

## Code Commentary

Messages carry the request and artifact locations; files carry evidence and verdicts. A held receipt means queued delivery and is not resent, while a full-store refusal follows the named retry procedure. Superseded held messages are withdrawn. Filing uses the narrowest shared task, and receipt searches preserve enclosure and transcript-root scope; delivery and turn end establish no semantic acceptance.

## Evidence

- The sender names the finished object and its files through the existing role/task route. [1]
- Held delivery, full-store refusal and withdrawal have distinct handling. [2]
- Filing and receipt searches use their actual shared-task and transcript scopes. [3]
