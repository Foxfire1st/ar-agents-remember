# mcp/src/agents_remember/application/role_capsules/compilation.py

## Governing Overview

[application overview](../overview.md)

## Purpose

The admitted compile entry point: one call for a consumer that has an admitted binding and a canonical source tree — read the explicitly named source set, hand it to the pure compiler, and return **either** the capsule **or** the refusal *with* its explanation projection.

## Code Commentary

### Logic

`compile_admitted_capsule` (`compilation.py:95-138`) is the whole surface. It admits via `admit_capsule_sources` (`sources.py:78-92`), extracts the manifest bytes from the admitted set, parses them opportunistically, passes the **full** admitted `core/every-role.md` source to `compile_role_capsule` (`compiler.py:99-189`) so full-source admission and semantic-digest sealing stay intact, converts any typed refusal into an outcome rather than letting it escape, and for `CapsuleRoleSeat` filters the separately returned `shared_block` through `filter_shared_block(shared_block, binding.admitted.seat.role)` (`compilation.py:134-135`). Non-`CapsuleRoleSeat` seats (such as `CapsuleLauncherSeat`) receive the unfiltered `shared_block`, and an absent `core/every-role.md` source yields `shared_block=None`.

`CapsuleCompilationOutcome` (`compilation.py:47-92`) is **exactly one of** a compiled capsule or a refusal: its `__post_init__` (`65-69`) raises `ValueError` when neither or both are present, so an outcome cannot be half-built. It exposes `ok` (`71-73`), `capsule` (`75-79`, or `None`), `semantic_digest` (`81-85`) — *a refusal has no identity* — `render_explanation` (`87-92`) for the operator-facing line, and `shared_block: str | None = None` (`63`).

**A refusal is a value here rather than an exception**, for two reasons the docstring states: a caller that has to explain a failure needs the diagnostic manifest as much as a caller that succeeded needs the capsule, and *"compilation failure never becomes a partially valid capsule" is easier to keep true when the two outcomes are different shapes of one result.*

A source tree that cannot be read at all — a missing file, a traversal attempt, an unreadable root — produces the **same** refusal shape as a selection defect, carrying the admitted-facts half of the manifest, because those facts were true regardless and are what an operator needs to act on. Two private builders implement that split: `_manifest_bytes` (`151-155`) recovers the manifest from the admitted set, and `_failure_manifest` (`141-148`) chooses `refused_manifest` when the manifest could not be parsed versus `manifest_for_error` when it could.

This module accepts any `CapsuleTaskProjectionSource` and passes it through untouched (`11-13`, `98`, `126`). Task state is never read, rendered, or rewritten here.

### Conventions

One call, one outcome. A consumer branches on `CapsuleCompilationError.status` (reachable through `outcome.error`) rather than parsing prose, and reads `outcome.manifest` for the explanation in both success and failure.

### Invariants And Boundaries

- The outcome is **exactly one** of a capsule or a refusal; never a partial capsule and never a silent `None` pair.
- A refusal still carries a manifest. `error` is the typed refusal; `manifest` is present in both shapes, so an operator can always see who the seat was, which sources were admitted, and what stopped the run.
- `semantic_digest` is `None` for a refusal — a refusal has no identity. Do not synthesize one.
- The projection is passed through, never interpreted: no task state is read, rendered, or rewritten at this boundary.
- This module owns the read-then-compile sequencing and holds no selection rule of its own.
- `compile_role_capsule` admits and seals the full unfiltered `core/every-role.md` source; role-scoped filtering via `application/role_capsules/shared_block.py::filter_shared_block` applies solely to `CapsuleCompilationOutcome.shared_block` for `CapsuleRoleSeat` and remains separate from `render_instructions`.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root (`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The pure compiler this entry point calls and the refusal-shaped manifest builders it selects between. [1]
- The admission step whose refusal is converted into the same outcome shape. [2]
- The typed refusal carried as a value. [4]
- A supplied projection is carried in its own channel, an unverifiable one is refused, and no projection yields no context with a stable digest. [5]

- The task-projection seam accepted in `compile_admitted_capsule` and verified inside `compile_role_capsule`. [3]
- `compile_admitted_capsule` seals the full `core/every-role.md` source in `compile_role_capsule` and filters `CapsuleCompilationOutcome.shared_block` per canonical role for `CapsuleRoleSeat` via `filter_shared_block`, leaving launcher seats unfiltered and absent sources `None`. [6]

### Cross-Repo References

No sibling-repository contract consumes this entry point.
