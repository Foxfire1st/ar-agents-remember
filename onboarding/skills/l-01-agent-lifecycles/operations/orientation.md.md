# skills/l-01-agent-lifecycles/operations/orientation.md

## Governing Overview

[overview](../overview.md)

## Purpose

The orientation operation instruction.

## Code Commentary

The instruction owns the session orientation that resolves context and source before work starts.

## Current composition and authoring contract

Orientation still binds exact role/task/root/report facts, native task-file reads and canonical task_doc writes, scoped task-server discovery, parent questions, quoted-answer provenance and permission non-bypass. It also carries the reply rule: an agent's reply in a turn reaches a sender only when that sender waits on its own call, and otherwise the reply is sent with `role_message` on `agents-remember-task`; an agent with no independent work left sends what it awaits, and from whom, to its question recipient. A developer question goes to the reporting recipient the role names, else the parent in `host.parent`, else the own chat. The reply and developer-question sections are marked for every role except Bootstrap; the other common instructions stay in the all-role region.

A Curator-only section, `Bind curation to the serving build`, supplies the existing development producer boundary in this stage: starting server or same-build CLI, clean main serving commit as ruler, no leaf self-production, fixture/scratch proof only, no install, guard disabling or substitute producer. It does not permit writes during orientation or give other roles a new producer.

## Evidence

- The current Curator-only orientation section binds deciding and writing to the starting tool server or its serving-build CLI and names clean main serving commit as the ruler. [2]

- Common orientation text is all-role, and a Curator-only section binds curation to the serving build. [1]
