# mcp/src/agents_remember/worktrees/modules/start.py

## Governing Overview

[worktree modules overview](overview.md)

## Purpose

Owns worktree start, attach, status result construction, and startup preparation for external memory and providers. Memory cannot be disabled for a task: every start runs in `external` mode, and a start that names the removed `disabled` mode — or the removed `disabled-memory` recovery answer — is refused by name before any worktree exists.

## Same-request planned parent in public preview

`start_result` consumes a `StartContractPlan`: the leaf contract plus the exact parent already validated by `ensure_master_series_contract`. Only dry-run construction carries that parent. The value passes through preflight, lineage recognition and enclosure planning to `require_parent_series`; a missing filename alone never establishes this special authority. An existing parent still goes through its normal reader/identity guard.

Apply carries no preview-parent substitute and retains the existing locked bootstrap, source/activation reconciliation, persisted-parent checks and materialization. Preview is not a reservation: later apply recomputes current facts and keeps existing refusal/recovery/CAS behavior. Organizational direct-super and ordinary standalone routes retain their existing meanings.

The moved plan/result records and memory/provider blocked projections have one home in [startup/start_plan.py](startup/start_plan.py.md). Their blocked-result vocabulary and reconciled-memory-base projection are preserved there; the removed disabled-memory projection is not restored. Startup-owned dry-run storage/ref/worktree/index state is unchanged. A registered preview still writes the daily tool-call log and, when its answer completes, the workspace-river event. There is no current ambient-lifecycle alternative event-file route. These call records are not startup publication, reservations or apply authority. The first-leaf proof checks the records rather than dropping the logs subtree from observation, so this card makes no universal no-I/O claim.






## Code Commentary

`start_result` refuses removed vocabulary first, at the top, because there it has no worktree, branch, contract, or task binding to unwind: `_removed_vocabulary_result` answers a removed `memory_mode` or `topology` (other than `disabled`) with the `memory-mode-unsupported` typed result and never substitutes `external` for what was asked; `disabled` is refused just below with its own opt-out refusal, never with the `internal` text; and `_unknown_choice_result` answers any other unknown `memory_choice` as an invalid request in the same shape as every mistyped start argument. The CLI no longer offers `disabled-memory` as a choice, so it still parses only so the start can refuse it by name.

A no-directive start still attaches to its live disabled leaf before new-parent admission: `_live_disabled_leaf_attach_result` fires only when the request names no memory directive at all and a live disabled leaf contract already exists at the requested address, returning the existing-contract result instead of letting fresh-contract admission refuse first. Genuinely new leaves, explicit disabled requests, and explicit conversions all keep the build path and its refusals.

The rest is unchanged. `start_result` consumes a request-scoped `StartContractPlan` (leaf contract plus the owner-validated preview-only parent, carried only for dry-run preview) through three stages — existing-contract reuse (a tombstone or reset recreates fresh), pre-creation preflights (stale base, fast-forward rebuild, Windows long-path check), and enclosure creation. Attach reselects and reconciles an atomic leaf's parent series before exposing the workbench; a series contract is never a workbench. The stale-base preflight blocks on `behind`/`diverged` with `choose_stale_base_recovery` (`proceed-stale` or `fast-forward`); `unknown` and `no-upstream` never block. Provider setup launches in the background after the contract is written, with `worktree_status` polling until a terminal state. Start/create and existing-start reuse delegate binding plus task-stage publication to `publish_start_task_facts`; explicit attach passes `started=False`, preserving the existing stage. The shared owner promotes a planned start to `inProgress`, mirrors its master row, revalidates and reads back the exact enclosure binding, and keeps exact retries no-ops. The persisted `lifecycleId` remains an enclosure identity, not host activity or another task-status authority. Enclosure creation makes `<enclosure>/logs/` outside both worktrees and outside Git.

## Evidence

- Removed vocabulary refused before anything is created [16]
- Unknown recovery answer is invalid, never opt-out [17]
- No-directive start keeps its live disabled leaf [18]
- Refusal chain runs before context resolution [19]
- Live contract attaches, tombstone recreates [20]

- Attach delegates with started=False and retains typed binding refusal. [26]
- The shared publisher promotes start, preserves attach stage, mirrors the row and reads binding back. [27]
- A tool call records its daily line and required detail under the retained log owner. [21]
- Completed answers use the one workspace event writer, with no ambient-lifecycle alternative. [22]
- The public result path carries the owner-validated start plan. [23]
- Only the actually carried preview parent qualifies for planned-lineage recognition. [24]
- Preview admission and memory preparation use the exact admitted parent. [25]
