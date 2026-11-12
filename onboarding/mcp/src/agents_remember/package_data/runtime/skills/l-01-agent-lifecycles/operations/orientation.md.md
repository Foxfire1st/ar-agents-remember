# operations/orientation.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Recover the selected native role assignment and canonical inputs without deriving scope from the execution workspace.

## Current Contract

The role launcher supports these eight role IDs: `architect`, `investigator`, `orchestrator`, `manager`, `worker`, `reviewer`, `curator`, and `bootstrap`; `bootstrap` is the taskless setup role the one start call reaches. `system-specialist` is the earlier ID of the same Investigator role. Missing, unsupported, inapplicable or conflicting role/operation/task bindings are reported rather than inferred. Projects is an execution location, not a repository identity. A manually selected taskless Architect asks only for missing outcome or registered repository details. An Investigator accepts a scoped concern of any kind from its actual parent's first message and asks that parent for missing concern/report scope; without a parent it uses the developer's request and own chat. Investigator may be selected at Projects, on a sprint, or on a sprint and master, never on a leaf. No synthetic repository, sprint, master, task or parent is created. Existing work recovers durable requirements, rulings, approvals, agent IDs and reports; reconnects do not invalidate supplied approval.

Task-bound reads use the rendered task-document files named in the handover and the harness’s own file tools before acting. For canonical task-document edits admitted to the role, use `task_doc` first; only a covered correct-input write refusal follows the declared same-tool/input-class recovery. Rendered copies are never parsed back and are refreshed by the owner’s next task_doc publication. Read only the selected packet/task scope and verify role, requirement revision, altitude, paired roots, contract and report agree. Missing admission/capability and read, validation, sync, guard, gate and permission stops remain unchanged.

Use the launching build’s `agents-remember-task` server through its actual harness tool surface and schemas. The tool-server binding supplies identity; the handover supplies a parent when one exists. Every question requiring the developer's decision goes to the reporting recipient the role instructs; if the role names none, to the parent named in host.parent, through bound role_message; when neither exists, the agent asks the developer in its own chat. Independent work continues; when none remains, the agent records its state and sends what it awaits to that recipient. A full-store refusal follows the message-handover detail: the handover stays pending, is retried once, and a second refusal is reported. Only a recipient that cannot be reached at all (archived, not found, not resumable, no runtime configured, or host unreachable) sends the question to the agent's own chat, with the refusal named. Peer communication retains its bound role-message route.

## Conventions

Canonical skills/l-01-agent-lifecycles/operations/orientation.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy, the sole generated skill target, which the tool server serves as MCP resources; no generated file defines a separate obligation.

## Invariants And Boundaries

Worker/Reviewer use memory read-only; Curator owns admitted memory writes. A dashboard role needs no parent. After compaction/reconnect restore the same assignment and inspect current AR truth before retrying an action.

## Code Commentary

### Todos

None recorded.

## Evidence


Superseded card wording retained for custody (not certified as true of any source epoch or measured candidate):

> Task-bound reads use the rendered task-document files named in the handover, read with the harness's own file tools before acting; change documents through `task_doc` only, because edits to copies are never read back and are lost on the next publication. Read only the selected packet/task scope and verify role, requirement revision, altitude, paired roots, contract and report agree.

>  —  Taskless/approved-scope intake, exact task reads, paired write surfaces, bound server and same-task recovery.  —  lines 3-13  —  mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/orientation.md:3-13  —


### Repo-Internal References

- Taskless scope, exact task-bound reads, role-admitted task_doc-first edits, paired surfaces, the bound tool server and saved-assignment recovery. [6]

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References




- The operation block's declared purpose, source path, and applicable roles. [3]

- The canonical source of this block. [4]

### Role launcher and alias

- The launcher supports these eight role IDs, including the taskless `bootstrap` setup role. [5]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.

## Current Investigator contract impact

Parentless Projects Investigator intake asks only for the missing concern/report scope from the developer request. Selected sprint/master intake uses the supplied actual references and concern channel. No repository, task or parent is synthesized; reconnecting preserves durable approvals and evidence.


- This source owns the stated current Investigator scope or canonical vocabulary.



## Current intake and developer-question evidence


- Investigator takes any scoped concern from the actual parent, uses the developer request only without a parent, and never synthesizes task identity; developer decisions go to the instructed reporting recipient, else the parent, with the stated no-recipient and unreachable exceptions.

- Orientation takes an Investigator's concern from its parent's first message or, without a parent, from the developer's request, and invents no task or trust packet; existing work restores its saved assignment first. [1]

- Developer decisions go to the instructed reporting recipient or the parent; only an agent with neither, or whose recipient cannot be reached, asks in its own chat. [2]
