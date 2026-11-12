# skills/l-01-agent-lifecycles/roles/orchestrator.md

## Permission notices and addressing

When a send answers `held` because a child waits at a permission prompt, or a wait returns `permission-pending`, the Orchestrator follows the coordination operation's permission-notice relay for the upward route, child identity and supplied permission facts; held delivery itself follows the every-role held-delivery rule. Sprint/master containment, Manager coordination, ordinary role/task returns and actual-parent-ID developer questions retain their distinct authority.

## Message/file transport and return addressing

Messages are short wake-ups naming work and files; report/verdict/evidence content travels in file-only `body` or existing-file `attach`, not pasted text. Within a shared task the files stay in its record and a leaf workspace exposes the folder link. Wake text uses the settings limit without a pinned number. Ordinary report-written notices and final report-path returns use the supplied parent role/task address, including an instructed reporting-recipient change. Developer-needed questions remain addressed to the actual parent/instructed-recipient ID. These are distinct message purposes, not an ID exception to the return rule. Fixed launch-parent identity and existing role/peer/write/acceptance boundaries remain preserved.

## Governing Overview

[overview](overview.md)

## Purpose

This source defines the sprint-bound orchestrator: it coordinates one selected sprint when two or more masters are worked on at the same time, or when the developer explicitly asks for one above a single master. It reuses each Architect-named Manager, starts one Manager for each other master, verifies Manager delivery with separately addressed evidence, and hands the master exit over. It operates at Projects altitude; a Paseo agent's state is not an AR acceptance ledger.

## Coordination default and reporting duty

The role text selects the Orchestrator when two or more masters are worked on at the same time, or when the developer explicitly asks for one above a single master; it reuses each existing Manager the Architect names and starts one Manager for each other master. The Orchestrator decides ordinary requirement readings and operational rulings itself, keeps its rulings record, requirement-change list and status file under the selected task's notes for the Architect to read, and messages the Architect only for the five developer-needed categories, the permission notices from children and one final report-path notice.

## Code Commentary

### The Current Shape

The file is one role page: `## Work from canonical truth` (`:12-18`), `## Coordinate role agents` (`:20-36`), `## Record operational decisions` (`:38-48`), `## Handle blockers and independent investigations` (`:50-54`), `## Communicate with the Architect` (`:56-70`), `## Changes to the plan` (`:72-79`), `## Verify and hand over` (`:81-97`), `## Result contract` (`:99-107`), `## Messages` (`:109-111`), `## Continue the assigned work` (`:113-115`), `## Organise your own work` (`:117-127`), `## Developer questions and answers` (`:129-131`) and `## Questions received from children` (`:133-137`). The page keeps sprint coordination, verification without loop takeover, the plan-change spirit test and the whole owed result; procedures sit behind "Before you …, read" pointers to `templates/manager-brief.md`, `operations/coordination.md`, `operations/closeout.md`, `operations/recovery.md`, `operations/orientation.md` and the detail files `reference/coordination/shared/seat-recovery.md`, `reference/coordination/shared/master-state.md`, `reference/coordination/shared/child-questions.md`, `reference/tasks/document-authoring.md`, `reference/knowledge/commands.md`, `reference/message-handover.md` and `reference/sandbox-actors.md`.

**Work from canonical truth (`:12-18`).** Resolve the sprint and only the documents needed for current decisions, read the rendered task-document files named in the handover, and change documents through `task_doc` first; never fabricate refs.

**Coordinate role agents and record decisions (`:20-48`).** Reuse Architect-named Managers and start one Manager per other master with `role_start`; those Managers coordinate their Workers, Reviewers, Curators and Investigators. Decide ordinary requirement readings and operational rulings itself, keeping the rulings record, requirement sentences and status file; message the Architect only for developer decisions plus one final report-path notice.

**Verify and hand over (`:81-97`).** Verify each Manager's delivery and aggregate evidence without taking over the loop; the Worker's and Reviewer's Curator hand-off lists go directly to the Curator, which this seat never relays.

In the same section, a test file that fails at collection or does not import is a regression of a landed leaf, routed for repair at once rather than left as a mark, and the Manager sends a Worker's skeleton to the Architect at once; the Worker writes the bodies after the Architect answers.

**Changes to the plan (`:72-79`).** Only the Orchestrator applies the spirit test: a change within the spirit of what the Architect and developer accepted is made and recorded in the task's decision log; one against it goes to the Architect and developer for a joint decision. During fix verification the test cannot add a fix leaf, reopen a resolved issue or widen the sealed findings list.

**Result contract (`:99-107`).** The owed result is collected whole here: rulings record, requirement-change list, status paths, decision messages, finished-or-unfinishable report-path message, blocker records, verified Manager delivery and pending questions.

**Organise, ask, escalate (`:109-137`).** Seat-owned harness freedom with boundary acts; developer questions follow the orientation operation's route; children's questions and the developer's answers follow `reference/coordination/shared/child-questions.md`.

### Invariants And Boundaries

- A parent-started seat does not converse with the developer; a dashboard-started Orchestrator has no
  parent and puts developer decisions in its own chat. It never wears another role's hat.
- Start, intake, message and permission-relay procedures belong to `../operations/coordination.md`.
- No seat-local watcher, polling, nudging, or timer loop; a finding held only in a chat is a bug.

## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full code quality, full tests, certification, and independent review are explicit operations only; memory quality is the curator's standing exception — the curator always runs it complete, and that result travels with the landing edge as prerequisite evidence, never relabelled as full green. Requested reviews retain the sealed finding list under the settings round limit.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Cross-Repo References

No meaningful cross-repo references.

## Investigator assignment

The Orchestrator coordinates concurrent masters through their Managers and may start Investigator on its own sprint, or on its sprint and one of its masters, for a concern or check belonging to no leaf. Leaf checks stay with their Worker and Reviewer. A refusal preserves actual parent routing or the parentless blocker; no invented Architect or recipient identity replaces it.

## Evidence

- Orchestrator coordinates one selected sprint through its Managers, follows started work through canonical facts and verifies delivery without taking over the Manager's leaf diff, repair and evidence loop. [16]

- The Orchestrator Result contract names its rulings and status artifacts, developer-decision and final report-path messages, verified Manager delivery and separately addressed reports, findings, review, curation and publication. [17]

- A parent-started Orchestrator sends upward only developer-needed matters, permission notices and one final report-path message, continues independent work when delivery is held or refused, and uses its own chat for developer decisions when dashboard-started without a parent. [18]

- Orchestrator may assign an Investigator a concern under its own sprint or sprint/master, never a leaf; the scoped concern is its first message to the returned Investigator ID. [19]

- Orchestrator keeps canonical sprint/master containment, Manager leaf ownership, separately addressed review/publication evidence and actual-parent developer questions. Held child permissions use the coordination notice route; covered correct-write recovery is separate from product guards. [20]
