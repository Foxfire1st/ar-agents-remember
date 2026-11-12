# mcp/tests/test_paseo_role_tools_start.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The parentless chat starts and the role-start cases of the role tools (PNT-R06), on the fixture the role-tool modules share.

## Code Commentary

`ParentlessChatStartTests` requires the dashboard's table to name every launchable role, canonical selections to pass while anything else is named, a chat to start an architect or a worker with no parent, a refused selection to match the dashboard's refusal, a chat never to replace a holder, and the launch record to name a chat that has no role. `RoleStartTests` requires worker instruction text to be no input to start permission, a repeat after a host profile change to keep the original launch, terminal enclosures to refuse both entry points before roots or a launch, a start to run the launcher's path with the caller as parent, and a start that is not carried out to name the rule or the state. Each launch status carries the same request id, and no agent other than the starter and the launcher repeats it. Starts run one at a time and a start waits for the one before it; a start that waited out its time says to call again. A repeat whose agent is archived or gone is refused with what to do, and a task-bound repeat after a changed task document reconciles the same agent. `test_a_start_uses_the_last_answer_when_catalog_discovery_fails` first saves a catalog answer, then makes fresh discovery fail: the start uses that answer, requests `metadata` followed by `selected` catalog data, creates one agent and reports it running.

## Invariants And Boundaries

The request id is the identity of a start, not a new one per attempt: it is asserted to be repeated by exactly the starter and the launcher. A held or queued start answers with an instruction to call again rather than an invented seat.

## Evidence

### Repo-Internal References

- A chat without a role starts through the dashboard's table, and a selection outside it is named. [1]


- A start runs the launcher's path with the caller as parent and one request id serves the starter and the launcher. [2]


- Starts are serialized, and a start that waited out its time says to call again. [3]
