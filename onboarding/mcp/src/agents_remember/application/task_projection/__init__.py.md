# mcp/src/agents_remember/application/task_projection/__init__.py

## Governing Overview

[application overview](../overview.md)

## Purpose

The import surface for the **task-context projection** — the package that computes the smallest
complete task projection the bound role and operation need, and fills the task-context seam the
role-capsule compiler froze. This module is the consumer contract L4/L5/L7 read; it holds no
computation of its own.

**Naming disambiguation — read this before confusing the two "projections".** This package's
*projection* is a **task-context** projection: one task document, its declared requirement
packets and its admitted worktree/branch binding, rendered as model-visible Markdown. It is **not**
the **closeout-queue projection** (`tasks/document_refs.py::projection_sprints_affected_by_master`,
`application/closeout_queue.py`, the `closeout-*.py` writers), which computes *which sprints a write
affects* so the disposable closeout queue can be rebuilt. The two share the word and nothing else:
different owners, different inputs, different consumers, no shared type. Nothing in this package is
reachable from the closeout queue, and nothing in the closeout queue is reachable from here.

## Code Commentary

### Logic

The module body is a docstring, the intra-package imports, and the `__all__` export list; all
behaviour lives in the ten sibling modules. Its docstring is load-bearing rather than decorative,
because it carries the **consumer contract** the L4/L5/L7 leaves are expected to follow — the
resolve-scope → project → convert → compile sequence — and it is where the package's two
admissions and its non-goals are stated.

Two inputs are the consumer's to supply, and both are admissions rather than guesses:

- The admitted facts' task reference must be the task layer's canonical key,
  `"<repository>/<path-under-tasks/<repository>>"` — the exact form `parse_task_reference` accepts.
- A requirement the bound task document declares as **exact text** instead of as an
  `approved-requirement-packet` reference needs an admitted, version-addressed packet location.
  **Declaring the packet on the task document is the preferred route and needs no consumer input**
  (the owner ruling of 2026-09-16T10:15 recorded on the L3 leaf document).

`__all__` exports all nine public functions plus every value type a consumer or a test needs; the
supporting private helpers stay private. `RequirementDeclaration` and `PacketSectionRole` are
re-exported because they are part of a caller's vocabulary, not because they are implemented here.

### Conventions

Consumers import from this package, never from a sibling module directly. A new public name is
added to `__all__` in the same edit that introduces it.

### Invariants And Boundaries

- **This package never writes.** It does not mutate task status, raise a gate, create an approval,
  write memory, touch Git, or publish a second authoritative task database. It reads through the
  existing owners and returns a value. `test_the_projection_modules_import_no_writer_transport_or_task_json_reader`
  asserts the import surface of all ten modules, so this is a checkable property rather than a claim.
- `__all__` is the authoritative export list. A private helper promoted to public without an
  `__all__` entry is invisible to consumers and to the import-surface case.
- The Knowledge Substrate master is **not** a dependency. A later knowledge view plugs in through
  `TaskKnowledgeExpansionSource`; with no source the projection reports the channel as unadmitted
  instead of quietly omitting it.
- A projection is a **value**: `TaskProjection` is frozen and slotted, so a consumer cannot mutate
  what it was handed.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking the configured sources.

### Repo-Internal References

The consumer-facing sequence this module documents, and the owners each step consults.

- The admitted context a consumer supplies, and the failure its unresolvable hints raise. [1]
- The computation and its declared extra inputs. [2]
- The compiler-facing conversion and the provider behind the one-method protocol. [3]
- Every public name this module exports is importable from the package root. [4]
- The task-context seam this package fills: the protocol, the DTO it converts into, and the compiler that re-verifies the digest. [5]
- The import surface of every module under this package is asserted, not assumed. [6]
- The **other** "projection" in this repository — the closeout-queue projection this package is not. [7]

### Cross-Repo References

No sibling-repository contract consumes this boundary.

No meaningful cross-repo references found.
