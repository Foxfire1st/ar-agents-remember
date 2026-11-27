# skills/l-01-agent-lifecycles/roles/worker.md

## Stage starts and completion

The Manager starts the Worker at build, the Reviewer when the Worker asks at its first freeze and the Curator after code PASS; Worker cannot start its checker or accept/publish its own implementation. Its stage requires the candidate to meet the requirement and pass its clean-copy freeze checks. The Worker runs the listed final checks once on the code-passed tree and reports to the Reviewer and Manager. Own failures are corrected on its own ground; blocked/unrun evidence remains explicit. A record-only repair stays on the same review round only with candidate unchanged; repeated cases demand property/construction reasoning rather than case chasing.

## Message/file transport

Message-file payload and receipt rules are routed from `roles/worker.md`'s Reference index to `reference/message-handover.md`; the canonical source and packaged copy share this contract without changing write/start powers, peer destinations or independent acceptance authority.

## Governing Overview

[overview](overview.md)

## Purpose

This canonical Worker implements one selected leaf’s approved primary requirement and explicit preservation constraints in its paired code worktree (memory read-only).

## Logic

`roles/worker.md` is a concise Tier-1 role manual (24 lines). It directs building the environment per `system/tools.md` (reporting missing tools and recording the interpreter), calling `read_ar_files` (`task_context`, open briefs) and `knowledge_read` (`workspace.memoryRoot`, `view="source_context"`) before edits or diagnosis, following `workspace.memoryRoot` `system/{coding,design,skill-writing}-guidelines.md` (helpers too; never edit skill guidelines), and sending Manager a skeleton before bodies when plan shape is open or changes and waiting.

It declares the `<!-- ar:gives freeze-handoff to reviewer: ... -->` and `<!-- ar:gives producer-list to curator: ... -->` contract markers, keeps candidates uncommitted (running unfamiliar commands from scratch), forbids role starts, Reviewer/Curator acts, memory/status edits, closeout, commit/merge/push/publish or requirement/packet rewrites, requires repairing own/instrument breaks (naming repairs in the report) and fixing faulty input on the same tool, stops after 3 failed repairs on one item and tells Manager, and marks build `done` via `task_doc(set_step)`.

Its `## Reference index` routes detailed procedures to `reference/knowledge/{use,commands,serving-build}.md`, `reference/tasks/document-authoring.md`, `templates/turn-report.md#shape`, `templates/curator-handoff-list.md`, `reference/writing/visual-explainers.md`, `reference/message-handover.md`, `reference/worker/sync-and-repairs.md`, `reference/sandbox-actors.md`, `operations/orientation.md#ask-for-a-developer-decision`, and `core/acceptance.md`.

## Conventions

- One leaf, one worker seat, one physical attempt journal, one link-only turn report, and one curator hand-off list.
- Native reads in the actual worktree are the edit precondition.
- Worker owns edits and the report; native role-start authority is not granted to this role.
- Fix rounds resume the same worker when possible and append round evidence.
- New scope or a missing decision returns to the actual task owner/developer through the admitted own-chat or bound-parent route.

## Invariants And Boundaries

- Worker identity is the canonical leaf document plus `worker` role.
- Worker never commits, closes out, integrates, decides gates, or mutates accepted memory.
- Worker never absorbs manager, reviewer, curator, architect or orchestrator work.
- No duplicate owner or background poller substitutes for canonical task and bound host facts.
- Use actual returned/handed-over agent IDs; do not invent a parent, recipient or delivery result.

## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction.

## Current composition and authoring contract

Worker implements the approved leaf only, leaves code uncommitted, uses memory read-only, builds its environment per `system/tools.md`, reads guidelines and briefs before editing, sends skeletons when plan shape is open or changes, keeps the 3-repair stop and `task_doc(set_step)` completion rule, and routes detailed freeze/sync/repair/out-of-scope-record procedures via its `## Reference index` to `operations/implementation.md`, `reference/worker/sync-and-repairs.md`, `templates/turn-report.md#shape`, and `templates/curator-handoff-list.md`.

## Working files

`roles/worker.md` ends with its `## Reference index` table; scratch-root rules are carried by `core/every-role.md` and `reference/sandbox-actors.md` rather than an inline closing paragraph in `roles/worker.md`.

## Evidence

### Repo-Internal References

- The worker records the complete acceptance envelope exactly once for its owned primary stable requirement ID and version. [8]


- The worker implements one selected leaf and writes one report at the handover's report path. [10]




- The Worker implements the selected leaf's approved primary requirement and preservation constraints. The handover supplies the canonical task, exact packet, paired roots, contract and report path. Completion requires clean-copy handover checks on the frozen candidate and any listed final checks once on the code-passed tree, with reports to the Reviewer and Manager. [1]




- Worker reads selected packets and rendered task files via file tools (no .json), verifies paired roots and contract agreement, writes code only with memory read-only as context, and reports missing bindings/fields to their owner without guessing a different task or workspace. [2]





- Worker reads the selected requirement/task with its own file tools, reads the repository's `system/coding-guidelines.md` in full before the first source edit and follows it for every line of source, tests and product messages (a helper told to do the same), uses `read_ar_files` and opens a current saved source brief when present before editing and reads attributed proof evidence before diagnosing a test failure, and reads existing design guidelines before its first UI edit. [3]



- Worker freezes and first asks Manager to start Reviewer, then sends that Reviewer its exact freeze and journal attempt IDs; after code PASS it sends the Curator the exact-freeze structured producer list after serving-build handoff-check. [4]


- Worker writes one canonical task report, carries the leaf Requirement Attempt Journal attempt IDs with its freeze and reads the turn-report shape at that freeze; the detailed implementation output procedure remains the owner. [5]


- After code PASS, Worker sends Curator structured producer data verbatim for that exact freeze in the shared template shape and first runs serving-build handoff-check against that freeze. [6]

- Worker owns code and its build/evidence step completion, not memory, review, lifecycle/status, commits or acceptance; its completed matching own steps may be marked done through task_doc and unfinished work is never marked complete. [7]


- Worker stage completion requires meeting the requirement, passing coding-guidelines handover checks on a clean copy of the frozen candidate and running any listed final checks once on the code-passed tree. The Worker repairs its own failing checks and reports those it cannot pass or run. [9]


- Worker escalates three unsuccessful own repairs and costly/repeated small repairs to Manager, preserves build-only authority, and uses the bounded writer ladder only for its admitted tool class while validation/transaction guards retain their stops. [11]


- Worker first notifies Manager at freeze so Reviewer can be started; after code PASS Manager starts Curator. Worker starts no role, cannot accept its own implementation, repairs its own failing checks and retains a record-only review round only while candidate bytes stay unchanged. [12]


- Worker marks only its own build/evidence step done when complete through task_doc, never curation, review, task status or acceptance. [13]


- After three unsuccessful own repairs of the same check or finding, Worker records its attempts and remaining failure and tells Manager rather than continuing that repair loop. [14]



- A sealed finding in the Worker's own task files is repaired directly without prior plan or Manager go-ahead, the freeze reports per-finding before/after test evidence, and supported leaf sync is governed by reference/worker/sync-and-repairs.md. [16]





- The role directs opening available saved briefs before its source work. Compact rows can give applicable card status and a brief pointer with saved freshness. Fuller replies can include rule text. Knowledge_read names whole records and their evidence. [18]
