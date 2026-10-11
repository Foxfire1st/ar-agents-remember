# operations/coordination.md

## Current supported-pair account — R100/R116 composition

The Manager starts Worker, Reviewer and Curator together through one role_start_set; Worker opens immediately, the other seats are held unless first Reviewer work is supplied. Public messaging takes a unique live seat, refuses ambiguity, and holds behind already-held messages when a start, permission prompt or non-steerable turn prevents delivery. Permission decisions are never answered by transport; the upward notice names the role/task/agent/permission, and the product delivers held work when admissible without sender resubmission. CODE and MEMORY lanes keep separate counts; the settings limit and recorded architect/developer authority govern extra rounds. Direct peer packages are not relayed by Manager.

This account controls the named changed seams; contradictory earlier card wording below is retained only as historical evidence. Unchanged role duties and R117 file-only wake/report transport are preserved. Source inspection supplies no new runtime test, CODE verdict, review counter or acceptance.

- The Manager starts Worker, Reviewer and Curator together through one role_start_set; Worker opens immediately, the other seats are held unless first Reviewer work is supplied. Public messaging takes a unique live seat, refuses ambiguity, and holds behind already-held messages when a start, permission prompt or non-steerable turn prevents delivery. Permission decisions are never answered by transport; the upward notice names the role/task/agent/permission, and the product delivers held work when admissible without sender resubmission. CODE and MEMORY lanes keep separate counts; the settings limit and recorded architect/developer authority govern extra rounds. Direct peer packages are not relayed by Manager. [5]


## Message/file transport

This packaged copy makes role messages short wake-ups naming requested work or a handover and its files. Complete report, verdict, list and evidence contents travel through file-only `body` or existing-file `attach`, never pasted into message text. Within a shared task, message files remain with its record and a leaf workspace exposes the message-folder link. Wake text uses the effective settings limit, not a number pinned in this role/template. This transport account changes neither the file's existing role/write boundaries nor requirement, review, curation or landing authority.

- Messages wake; complete payloads and evidence travel as files. [4]


## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Start and reach native role agents for exact canonical AR assignments while keeping delivery with Paseo and semantic truth with AR.

## Current Contract

The review budget comes from `orchestration.loops.defaults.maxRounds`, read when the next round begins; agents read the effective task limit, including approved extra rounds, from `task_doc`’s `reviewState.limit` on `agents-remember-task`. Code and memory reviews use the same settings limit with separate counts and sealed findings. Beyond-limit work needs a recorded architect or developer approval; the Manager asks the task’s Architect, not the developer. The Reviewer records its own CODE begin/result; MEMORY retains its separate sealed reports, IDs and pass count without opening or resetting CODE state.

The Architect delegates coordination first to one Manager for one master or one Orchestrator for concurrent masters; direct coordination is only the developer’s choice. A bound start supplies the role, required canonical references and request ID, resolves the AR paired enclosure, writes the handover and returns the actual agent/report/artifact identities.

Architect may start every role except Architect; Orchestrator may start Manager, Worker, Reviewer, Curator and Investigator under its sprint; Manager may start Worker, Reviewer, Curator and Investigator under its master. Other roles start none. An unknown start is reconciled by the same request ID. A rejected candidate returns finding-specific repair to the same Worker.

The Manager prepares a leaf’s Worker, Reviewer and Curator as siblings in one `role_start_set` call. Worker opens; Reviewer and Curator stay held until addressed work, unless the call carries Reviewer work. This replaces staggered Curator creation at the first freeze without changing who may start which role or the direct leaf repair loop.

`role_message` names one recipient by actual agent ID or unambiguous role/task selection, attributes the sender and never cancels a running turn. Two live leaf occupants refuse with both IDs; no newest candidate is selected. Unavailable starts, permission prompts and unwritable turns hold work in FIFO order. The sender does not resend held work. Capacity, missing, archived and ambiguous outcomes remain explicit. A wait reports the consumed turn or a pending/timeout/uncertain outcome; it is not semantic completion. Dashboard-started agents need no parent.

## Conventions

Canonical skills/l-01-agent-lifecycles/operations/coordination.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

Use the bound `role_start`, Manager leaf `role_start_set` and `role_message` on `agents-remember-task`. A held permission answer still requires the upward named-chat notice; only the developer answers the prompt. Product delivery removes the parent’s second-send duty. Preserve canonical task and paired paths; do not create an independent Paseo Git worktree, background scheduler, duplicate owner or acceptance ledger. Avoid mutually waiting agents.

## Code Commentary

### Todos

None recorded.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| One coordinating agent under the Architect, bound start/messaging, same-request recovery and execution metadata boundary. | lines 3-15 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/coordination.md:3-15 |

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The operation block's declared purpose, source path, and applicable roles. [2]
- The canonical source of this block. [3]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.

## Current Investigator contract impact

The exact role-start permission table includes Investigator for Orchestrator under its sprint and Manager under its master; Architect retains its permitted coordinating scope. Other roles start none. Existing request-ID reconciliation, direct leaf repair and Manager transaction ownership remain unchanged.

- This source owns the stated current Investigator scope or canonical vocabulary. [1]

## Current Contract Evidence

- Current review-budget and preserved ownership obligations are defined by these source instructions. [4]
