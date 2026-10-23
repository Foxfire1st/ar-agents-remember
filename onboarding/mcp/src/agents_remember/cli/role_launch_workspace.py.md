# mcp/src/agents_remember/cli/role_launch_workspace.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

The role start's preparation owner derives the admitted working group: non-leaf roles use Projects, an ungranted leaf creates or finds its enclosure through the existing child, and a granted direct leaf uses the existing master series checkouts without a leaf enclosure or child materialization. Native refusals retain the owner's status, reason and next action.

## Code Commentary

In the enclosed-leaf branch, the real leaf-workspace owner creates the group's `messages` link to its own leaf task-record folder before launch. It records `messagesLink` and a warning when an occupied non-link or divergent link prevents creation; it preserves that path and continues the launch. Inbound delivery retries link establishment through the delivery owner, while cleanup removes only a symlink and leaves canonical message files intact.

`_recorded_parent` reads the master's existing series contract and passes its recorded `parent_task_name` as the materializer hint — but only when that name is not the master's own folder. A contract written before 2026-09-29 records the master's own name, and passing it back resolves the leaf under `<master>/<master>`, which does not exist; the commanding sprint's folder name is the answer in that case and when there is no contract yet. `_ensure_leaf_enclosure` refuses both published terminal generations before using or materializing any root (`reopen-required`), and treats a `reopened` generation as the prepared start it is: the reset contract is durable and the archived generation stays proven, but the worktrees cleanup removed are gone, so it recreates the enclosure under the worktree name the contract already owns rather than a newly planned one. It raises typed failures for conflicting enclosure bindings and unavailable contract-owned directories. `_start_leaf_enclosure` runs preparation for this operation through the existing checked child. The child retains its root checks, writer admission and cut-off policy; the public `worktree_start` tool retains its own caller semantics. This is an operation-preparation boundary, not a statement about a persistent caller lifecycle. `_preparation_refusal` preserves the native status and reason and names the recovery — the stale-base choice, the tool call the owner returned, `task_reopen`, the series-edge reconciliation, or an inspection before repair. `_resolve_workspace` returns validated group roots and preparation `created`/`found` for an enclosed leaf or `direct` for a granted leaf. The direct branch refuses unreadable/missing/wrong-kind series authority, unavailable roots and an open direct sibling. Reports, copied documents and scratch remain in the separate series group, not the code/memory checkouts. This folder selection is not OS or shell-permission confinement.

## Real role-reports directories

`_resolve_workspace` now points report access at the group's real `role-reports` directory, creating it and refusing a symlink there. The old `task-reports` alias is only restored for existing recorded bindings; no new start uses it.

## Evidence

- The recorded master contract supplies the parent hint unless it names the master itself, where the commanding sprint supplies it; an absent contract falls back to the sprint to bootstrap. [1]
- A refusal keeps the native status and reason and names an owner-derived next action. [2]
- The canonical enclosure path is derived from the leaf document and conflicting bindings are refused. [3]

- The common resolver creates or finds the enclosure and returns its validated roots and preparation outcome. [4]

- Terminal generations refuse before any root use or materialization, and a missing or reopened enclosure is created through the child — a reopened one under the worktree name its contract already owns. [5]

- Both role-start entry points use the existing checked preparation child for this operation, retaining its root, writer-admission and cut-off checks; public worktree_start retains its caller semantics. [6]



- Call-time granted leaves reuse master series checkouts and keep role artifacts in the separate group. [7]
