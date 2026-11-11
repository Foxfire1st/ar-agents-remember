# l-01-agent-lifecycles/roles/orchestrator.md

## Current supported-pair account — R100/R116 composition

When a send answers `held`, the Orchestrator follows the held-delivery rule: the product queues eventual delivery and the message is never resent. A child waiting at a permission prompt is named to the Orchestrator's parent, or to the developer in its own chat without one, and each parent passes the notice upward unchanged.


## Message/file transport and return addressing

Messages are short wake-ups naming work and files; report/verdict/evidence content travels in file-only `body` or existing-file `attach`, not pasted text. Within a shared task the files stay in its record and a leaf workspace exposes the folder link. Wake text uses the settings limit without a pinned number. Developer-decision messages and the one finished-or-unfinishable report-path message go with `role_message` on `agents-remember-task` to the parent agent ID in the handover.


## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

A native Orchestrator coordinates one selected sprint’s tasks and owners at Projects altitude when two or more masters are worked on at the same time, or when the developer explicitly asks for one above a single master.

## Current Contract

Read only the canonical task/packet/report/predecessor facts needed for the current decision. Read the rendered task-document files named in the handover, read with the harness's own file tools before acting; change documents through `task_doc` only, because edits to copies are never read back and are lost on the next publication. Missing requirement or owner facts are named from their source.

Start distinct Manager, Worker, Reviewer and Curator agents only under the selected sprint; reuse each existing Manager named by the Architect and start one Manager per other master. Keep actual IDs, reconcile unknown starts by the same request ID and follow assignments through bound messages/results without a separate poller.

Verify each Manager's delivery and aggregate evidence; it may inspect the supplied actual diffs for acceptance without taking over the leaf-diff or repair loop, which the Manager owns. Request independent review and affected curation when the brief or risk requires it. The leaf's Worker and Reviewer send their Curator hand-off lists directly to the Curator with producer data unchanged; the Orchestrator reads their reports for state and does not relay that data.

## Conventions

Canonical skills/l-01-agent-lifecycles/roles/orchestrator.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy, the sole generated skill target, which the tool server serves as MCP resources; no generated file defines a separate obligation.

## Invariants And Boundaries

Paseo turn status is execution metadata, not AR acceptance/landing. A parent-bound Orchestrator sends its parent only the five developer-decision occasions, child permission notices and the one finished-or-unfinishable report path, while ordinary requirement readings and operational rulings stay with it; without a parent it reports in its own chat. No fabricated task, identity, duplicate execution or second semantic ledger.

## Code Commentary

### Logic

The orchestrator owns durable portfolio execution behind the architect.

### Conventions

Edit the canonical
role, then synchronize.

### Invariants And Boundaries

- Seat identity is `(canonical task document, role)` and occupant replacement is plane-owned.

- Structural dispatch and structural gate decision fail closed on missing or ambiguous authority.

- The orchestrator is backend-only and does not become manager, worker, reviewer, curator, or
  developer-facing architect.

- This packaged artifact must remain byte-identical to the canonical role.

### Todos

None recorded.
## Working folders and reports

Agent-authored temporary files, experiments and working copies live only in the handover's real `workspace.scratchRoot`, outside code, memory and task folders; reports and evidence go in the handover's local report folder, which the product copies to canonical notes before removal.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| Selected-sprint truth, one Manager per master, same-agent follow-through and producer/evidence preservation. | lines 8-24 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:8-24 |

- Root skills are canonical and the sync script publishes byte-identical package and harness copies. [2]

### Cross-Repo References

No sibling repository evidence is needed for this doctrine file.

No meaningful cross-repo references found.


## Current Investigator contract impact

This packaged copy derives from the canonical roles/orchestrator.md. The Orchestrator coordinates concurrent masters through their Managers and may start Investigator under its own sprint for a concern/check belonging to no leaf. Leaf checks stay with their Worker/Reviewer. A refusal preserves actual parent routing or the parentless blocker; no invented Architect or recipient identity replaces it. Investigator is a child concern/report carrier, not a leaf transaction owner. Mirror synchronization remains the owner; this file adds no independent instruction.


- This source owns the stated current Investigator scope or canonical vocabulary.

- The Orchestrator reuses each existing Manager named in the Architect's handover and starts one Manager for each other master with role_start under its own sprint; those Managers coordinate their Workers, Reviewers and Curators. [1]

- The Orchestrator sends the Architect only developer-requiring questions and child permission notices with role_message to the parent agent ID, keeps ordinary requirement readings and operational rulings itself, and follows the held-delivery rule when a send answers held. [3]
