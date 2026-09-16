# mcp/src/agents_remember/application/task_projection/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_projection/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T10:30+02:00 |
| lastVerifiedCommitHash | `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| lastVerifiedCommitDate | 2026-09-16T10:52:30+02:00|
| governingOverview      | `../overview.md`                           |

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

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking the configured sources. | N/A | N/A |

## Repo-Internal References

The consumer-facing sequence this module documents, and the owners each step consults.

| Finding | Anchor | Source |
| --- | --- | --- |
| The admitted context a consumer supplies, and the failure its unresolvable hints raise. | `ProjectionScopeRequest`; `resolve_task_projection_scope`; `ResolvedProjectionScope` | mcp/src/agents_remember/application/task_projection/scope.py:94-106; mcp/src/agents_remember/application/task_projection/scope.py:292-373; mcp/src/agents_remember/application/task_projection/scope.py:110-121 |
| The computation and its declared extra inputs. | `project_task_context`; `TaskProjectionRequest` | mcp/src/agents_remember/application/task_projection/projection.py:75-87; mcp/src/agents_remember/application/task_projection/types.py:289-299 |
| The compiler-facing conversion and the provider behind the one-method protocol. | `task_context_of`; `TaskProjectionSource` | mcp/src/agents_remember/application/task_projection/provider.py:37-52; mcp/src/agents_remember/application/task_projection/provider.py:56-103 |
| Every public name this module exports is importable from the package root. | `__all__` | mcp/src/agents_remember/application/task_projection/__init__.py:91-132 |
| The task-context seam this package fills: the protocol, the DTO it converts into, and the compiler that re-verifies the digest. | `CapsuleTaskProjectionSource`; `CapsuleTaskContext`; `compile_admitted_capsule` | mcp/src/agents_remember/models/role_capsules/types.py:334-346; mcp/src/agents_remember/models/role_capsules/types.py:319-330; mcp/src/agents_remember/application/role_capsules/compilation.py:89-120 |
| The import surface of every module under this package is asserted, not assumed. | `test_the_projection_modules_import_no_writer_transport_or_task_json_reader` | mcp/tests/test_task_projection.py:738-764 |
| The **other** "projection" in this repository — the closeout-queue projection this package is not. | `projection_sprints_affected_by_master` | mcp/src/agents_remember/tasks/document_refs.py:473-481 |

## Cross-Repo References

No sibling-repository contract consumes this boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: created this card for the application-tier
  task-context projection package added by the scoped-task-context leaf (`CAPS-R03@v1`). Records the
  consumer contract and both admissions (canonical task reference; the typed
  `approved-requirement-packet` route as the preferred policy, with an admitted packet location for
  an exact-text declaration), the never-writes and no-Knowledge-Substrate-dependency invariants, and
  an explicit naming disambiguation against the **closeout-queue** projection that already owns the
  word in this repository. Verification metadata is left at the leaf base commit because the source
  is uncommitted — the governed closeout stamps the real code commit.
