# mcp/tests/test_l84_unique_detail_pointers.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves, over every compiled role/operation pair of the shipped lifecycle corpus (32 pairs), that each required detail is delivered once and is reached by exactly one pointer per action through its existing role or operation step, and that removing, duplicating or misdirecting any of those pointers fails.

## Code Commentary

The module compiles through the helpers of `test_l84_capsule_delivery_proofs.py` and takes its pointer tables from `test_role_capsule_audiences.py` and the shared `capsule_audience_fixtures`.

- **One pointer per action.** `duplicate_pointers` finds no duplicate in any first message (the role file, the operation file and the shared `core/every-role.md` block). Each duplicate in `RESTORED_DUPLICATES`, re-added to its first message, fails, as do a second link into one file inside another action's sentence, two wordings of one role action, and one action listed on both the role and the operation pointer list.
- **Required details.** In each compile the delivered detail references equal `ROLE_DETAILS` plus `OPERATION_DETAILS` exactly, every detail has content and a step, and each is pointed to by as many sentences as it has required actions, at any required section; a wrong section fragment fails. Every role except Bootstrap links the message-handover detail from its role file and carries one full-store-refusal pointer from its operation. The Curator's message detail is checked, and the Architect, Orchestrator and Manager reach the complete start-and-first-intake procedure in `operations/coordination.md` from one start pointer.
- **Moved pointers.** The shared `core/every-role.md` block is delivered once with its source revision and holds the settings-authority pointer once; the actions in `MOVED_ACTION_POINTERS` for the Curator, Manager, Orchestrator and Worker each point once to their detail.
- **Collaboration references.** The manifest's `tasks/collaboration-method` and `tasks/document-authoring` references equal the step and audiences derived from the first-message pointers; the collaboration method is neither injected nor a step detail. An extra audience, a removed Worker audience, or the pointer moved into the method itself fails.
- **Architect reads.** The Architect's document-authoring detail carries the retained-evidence pointer to `core/acceptance.md`; each `ARCHITECT_ACTION_READS` cue is one line that reads its delivered detail, which holds the clause in `ARCHITECT_ACTION_CLAUSES` (or the clause stands once in the shared block or the role file); the requirement-design detail keeps the task-layout sections.
- **Refused writes.** For the Architect, Orchestrator, Manager and Worker, the shared paragraph on a correct-input refusal of a covered write keeps its boundary clauses. Only the Manager receives `reference/refused-write.md` as a detail; the other roles reach it through the paragraph's served `skill://` link. Both paths lead to the complete "Honor harness permission decisions" section of `operations/orientation.md`.
- **Inline and short rules.** None of the 28 detail files named in `INLINE_RULE_CLAUSES` is delivered or linked as a detail, and each of their rules stands once in its owning section of the shared block or the role file; deleting or doubling a clause fails. Each rule in `SHARED_SHORT_RULE_CLAUSES` stands once in the shared block, its digest-map unit is a digest unit whose lines hash to the recorded SHA-256, and the actions in `REMOVED_SHORT_RULE_ACTIONS` do not appear in the role's message.
- **Grouped actions.** Each `GROUPED_DETAIL_CLAUSES` action links the whole delivered detail with no section fragment, and the emitted detail holds every listed clause.

## Evidence

- The complete per-role detail population is listed. [1]
- The direct start pointers reach the complete start-and-first-intake procedure. [2]
- Re-added duplicate pointers are enumerated by role, operation and source. [3]
- Every first message has one pointer per action and the restored duplicates fail. [4]
- Every compile delivers exactly its required details, each pointed to once per action. [5]
- Moved action pointers reach each required compile and reject removal. [6]
- The collaboration and authoring references equal their pointer-derived step and audiences. [7]
- An extra audience or an outbound pointer in the method fails. [8]
- Leaf authoring reaches the retained-evidence lifecycle. [9]
- Architect action cues read their delivered detail and reject pointer removal. [10]
- Only the Manager receives the refused-write detail; the other roles reach it through the served link. [11]
- The permission owner section keeps every facet of its stop. [12]
- Inline rules reach their owning sections and reject deletion. [13]
- Short rules use the shared delivery and the removed step reads stay absent. [14]
- Grouped actions read the whole delivered owner. [15]
