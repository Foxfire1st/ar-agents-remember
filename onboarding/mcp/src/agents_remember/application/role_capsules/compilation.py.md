# mcp/src/agents_remember/application/role_capsules/compilation.py

## Governing Overview

[application overview](../overview.md)

## Purpose

The admitted compile entry point: one call for a consumer that has an admitted binding and a
canonical source tree — read the explicitly named source set, hand it to the pure compiler, and
return **either** the capsule **or** the refusal *with* its explanation projection.

## Code Commentary

### Logic

cit:([`compile_admitted_capsule`], mcp/src/agents_remember/application/role_capsules/compilation.py:89-122) is the whole surface. It admits via
cit:([`admit_capsule_sources`], mcp/src/agents_remember/application/role_capsules/sources.py:78-94), extracts the manifest bytes from the admitted set,
parses them opportunistically, calls cit:([`compile_role_capsule`], mcp/src/agents_remember/models/role_capsules/compiler.py:84-140), and converts a typed refusal into an
outcome rather than letting it escape.

cit:([`CapsuleCompilationOutcome`], mcp/src/agents_remember/application/role_capsules/compilation.py:46-88) is **exactly one of** a compiled capsule or a refusal:
its `__post_init__` raises `ValueError` when neither or both are present, so an outcome cannot be
half-built. It exposes cit:([`ok`], mcp/src/agents_remember/application/role_capsules/compilation.py:66-68), cit:([`capsule`], mcp/src/agents_remember/application/role_capsules/compilation.py:70-75) (or `None`), and
cit:([`semantic_digest`], mcp/src/agents_remember/application/role_capsules/compilation.py:77-80) — *a refusal has no identity* — plus cit:([`render_explanation`], mcp/src/agents_remember/application/role_capsules/compilation.py:81-86) for the one
operator-facing line: the digest, or the refusal and its remedy.

**A refusal is a value here rather than an exception**, for two reasons the docstring states: a
caller that has to explain a failure needs the diagnostic manifest as much as a caller that
succeeded needs the capsule, and *"compilation failure never becomes a partially valid capsule"
is easier to keep true when the two outcomes are different shapes of one result.*

A source tree that cannot be read at all — a missing file, a traversal attempt, an unreadable
root — produces the **same** refusal shape as a selection defect, carrying the admitted-facts
half of the manifest, because those facts were true regardless and are what an operator needs to
act on. Two private builders implement that split: `_manifest_bytes` recovers the manifest from
the admitted set, and `_failure_manifest` chooses `refused_manifest` when the manifest could not
be parsed versus `manifest_for_error` when it could.

This module is also the **L3 seam for the later task projection**: it accepts any
`CapsuleTaskProjectionSource` and passes it through untouched. Task state is never read, rendered,
or rewritten here.

### Conventions

One call, one outcome. A consumer branches on `CapsuleCompilationError.status` (reachable through
`outcome.error`) rather than parsing prose, and reads `outcome.manifest` for the explanation in
both success and failure.

### Invariants And Boundaries

- The outcome is **exactly one** of a capsule or a refusal; never a partial capsule and never a
  silent `None` pair.
- A refusal still carries a manifest. `error` is the typed refusal; `manifest` is present in both
  shapes, so an operator can always see who the seat was, which sources were admitted, and what
  stopped the run.
- `semantic_digest` is `None` for a refusal — a refusal has no identity. Do not synthesize one.
- The projection is passed through, never interpreted: no task state is read, rendered, or
  rewritten at this boundary.
- This module owns the read-then-compile sequencing and holds no selection rule of its own.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The pure compiler this entry point calls and the refusal-shaped manifest builders it selects between. [1]
- The admission step whose refusal is converted into the same outcome shape. [2]
- The task-projection seam accepted here and verified inside the compiler. [3]
- The typed refusal carried as a value. [4]
- A supplied projection is carried in its own channel, an unverifiable one is refused, and no projection yields no context with a stable digest. [5]

### Cross-Repo References

No sibling-repository contract consumes this entry point. The projection seam it exposes is
consumed by a later leaf inside this master, not by another repository.

No meaningful cross-repo references found.
