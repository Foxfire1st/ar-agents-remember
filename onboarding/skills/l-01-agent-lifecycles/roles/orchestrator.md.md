# skills/l-01-agent-lifecycles/roles/orchestrator.md

## Permission notices and addressing

The Orchestrator reports permission-blocked starts and forwards the Manager's permission notices upward; the `held`/`permission-pending` relay procedure is in `operations/coordination.md` and `reference/coordination/shared/closeout-recovery.md`. Sprint/master containment, Manager coordination, ordinary role/task returns and actual-parent-ID developer questions retain their distinct authority.

## Message/file transport and return addressing

Message-file payload rules are routed from `roles/orchestrator.md`'s Reference index to `reference/message-handover.md`. Ordinary report-written notices and final report-path returns use the supplied parent role/task address, including an instructed reporting-recipient change. Developer-needed questions remain addressed to the actual parent/instructed-recipient ID. Fixed launch-parent identity and existing role/peer/write/acceptance boundaries remain preserved.

## Governing Overview

[overview](overview.md)

## Purpose

This source defines the sprint-bound orchestrator: it coordinates one selected sprint when two or more masters are worked on at the same time, or when the developer explicitly asks for one above a single master. It reuses each Architect-named Manager, starts one Manager for each other master, verifies Manager delivery with separately addressed evidence, and hands the master exit over. It operates at Projects altitude; a Paseo agent's state is not an AR acceptance ledger.

## Coordination default and reporting duty

The role text selects the Orchestrator when two or more masters are worked on at the same time, or when the developer explicitly asks for one above a single master; it reuses each existing Manager the Architect names and starts one Manager for each other master. The Orchestrator decides ordinary requirement readings and operational rulings itself, keeps its rulings record, requirement-change list and status file under the selected task's notes for the Architect to read, and messages the Architect on the same route to forward the Manager's matters for the Architect unchanged, send developer questions and children's permission notices, and send one final report-path notice, with no status-only messages or other landing notices.

## Code Commentary

### The Current Shape

The compressed Tier-1 role page has five sections: `## Coordinate the sprint`, `## Communicate with the Architect`, `## Changes to the plan`, `## Verify, boundaries, and result contract`, and `## Reference index`. The page keeps sprint coordination, verification without loop takeover, the plan-change spirit test and the compact result contract; its Reference index links `templates/manager-brief.md`, `operations/coordination.md#start-leaf-stages-and-deliver-the-first-intake`, `templates/curator-handoff-list.md`, `reference/coordination/shared/seat-recovery.md`, `reference/coordination/shared/master-state.md`, `reference/tasks/document-authoring.md#preserve-decisions-and-approved-intent`, `reference/coordination/shared/closeout-recovery.md#recover-an-unfinished-closeout`, `reference/knowledge/commands.md`, `reference/message-handover.md`, `reference/sandbox-actors.md` and `reference/coordination/shared/child-questions.md`.

**Coordinate the sprint.** Reuse Architect-named Managers and start one Manager per other master with `role_start`; those Managers coordinate their Workers, Reviewers, Curators and Investigators. Decide ordinary requirement readings and operational rulings itself, keeping the rulings record, requirement sentences and status file; verify Manager delivery without taking over the leaf diff, repair or evidence loop, and route collection/import test failures as landed-leaf regressions.

On an `IDENTITY MISMATCH:` notice from a child seat, the Orchestrator archives that seat, checks both its task folder and the folder named by the reported binding for writes, and starts a replacement.

**Communicate with the Architect.** Forward the Manager's Architect matters unchanged and send developer questions, permission notices and one final report-path notice to the Architect, with no status-only messages or other landing notices; ordinary returns use role/task refs while developer questions use parent ID (own chat if dashboard-started).

**Changes to the plan.** Only the Orchestrator applies the spirit test: a change within the spirit of what the Architect and developer accepted is made and recorded in the task's decision log; one against it goes to the Architect and developer for a joint decision. During fix verification the test cannot add a fix leaf, reopen a resolved issue or widen the sealed findings list.

**Verify, boundaries, and result contract.** Keep seat boundaries and collect the owed report fields: rulings record, requirement-change list, status paths, decision messages, finished-or-unfinishable report-path message, blocker records, verified Manager delivery and pending questions.

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


- A parent-started Orchestrator forwards the Manager's matters for the Architect unchanged and sends developer questions, permission notices and one final report-path message on the same route (with no status-only messages or other landing notices), continues independent work when delivery is held or refused, and uses its own chat for developer decisions when dashboard-started without a parent. [18]



- Orchestrator may assign an Investigator a concern under its own sprint or sprint/master, never a leaf; the scoped concern is its first message to the returned Investigator ID. [19]


- Orchestrator keeps canonical sprint/master containment, Manager leaf ownership, separately addressed review/publication evidence, unchanged forwarding of Manager Architect matters and actual-parent developer questions. Held child permissions use the coordination notice route; covered correct-write recovery is separate from product guards. [20]


- On an `IDENTITY MISMATCH:` notice from a child seat, the Orchestrator archives that seat, checks its task folder and the reported binding's folder for writes, and starts a replacement. \[21] [21]
