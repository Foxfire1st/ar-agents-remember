# docs/reference/mcp-tools.md

## Governing Overview

[overview.md](overview.md)
## Purpose

Reference documentation records the three-state dispatch contract, readiness proof, settings timing, public hosted_session_readiness, tool census, and concurrency ruling.
The memory-tool reference also distinguishes the full contract-scoped curator checklist from
subset/official quality calls, including its stable enclosure path, zeroable curator count, and
cleanup lifetime.
Since 260713-TES-L4 it also records the N16 inbox landing contract (the row lands terminal
`landed` only on correlated adapter acceptance at a turn boundary), terminal inspectability
(`include_terminal`, N11), the attribution-only `operator_inbox_consume`, and the explicit
`operator_inbox_supersede` tool (R11).

## Code Commentary

### Logic

Reference documentation records the three-state dispatch contract, readiness proof, settings timing, public hosted_session_readiness, tool census, and concurrency ruling.

**260713-TES-L4 inbox rows.** The `operator_inbox_post` row now reads "queue a durable
external-chat inbox row; the row lands (terminal `landed`) only on correlated adapter
acceptance at a turn boundary (N16)". `operator_inbox_poll` gained `include_terminal=false`
with the N11 marker-retention wording; `operator_inbox_consume` is documented as an optional
attribution marker with nothing mechanical attached; the new `operator_inbox_supersede`
row documents explicit supersession (R11) — terminal `superseded`, no false ack, skipped by
every retry/evaluation path.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization outputs. Dispatch proof remains exact-session and fail-closed.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

### Cross-Repo References

No meaningful cross-repo references.

## 260821-DAGQC-L2 Memory-Quality Contract

The reference now publishes one `request` object discriminated by `mode`: `sync` and `start` carry
execution scope/check/detail inputs, while `poll` carries only repository and run id. It documents
the hard live-work cap, same-identity reuse, typed `capacity-reached` guidance, and nondisclosing
`run-not-found` result. Flat `wait` and top-level `run_id` calls are no longer valid.

## 260928-MIK-L38 The `lifecycle_finalize_task` Row Names The Folder Master

The `lifecycle_finalize_task` row (`:163`) now says the finalizer reconciles the leaf's exact row when the leaf
declares an existing immediate parent "(or names none and its folder's `task.json` master lists it)", and that "a
sub-task naming none whose folder `task.json` is not a master is refused" (MIK-R38; ruling 2026-09-30T12:33:07 Q3,
review R1 note 5 at 13:11:32, and "sub-task" rather than "leaf" by ruling 14:12:52, so a `light` task that is its own
`task.json` is not covered by the refusal). The rest of the row, including standalone support and that the parent
task itself is not completed, is unchanged. The same clauses are in the registered tool description
(`mcp/registration/tasks.py`) and the c-09 skill.
