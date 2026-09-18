# mcp/src/agents_remember/application/role_capsules/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/role_capsules/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[application overview](../overview.md)

## Purpose

The import surface for the admitted-context resolution and composition boundary of role
capsules — the package that owns the I/O the pure compiler refuses to do.

## Code Commentary

### Logic

The package docstring states its scope exactly: this package owns resolving a confined source
root, reading the exact source set an admitted binding names, and returning a refusal as a value
with its explanation. **It holds no selection rules of its own** — selection lives in
`agents_remember.models.role_capsules`.

Only two names are exported, and the pairing is the contract:
cit:([`CapsuleAdmissionRequest`, `admit_capsule_sources`], mcp/src/agents_remember/application/role_capsules/__init__.py:13-16) describe *what to read*, and
cit:([`CapsuleCompilationOutcome`, `compile_admitted_capsule`], mcp/src/agents_remember/application/role_capsules/__init__.py:9-12) describe *the one call that reads and compiles*.

### Conventions

Consumers import from this package rather than from `compilation` or `sources` directly. A new
public name is added to `__all__` in the same edit.

### Invariants And Boundaries

- The package is the I/O boundary: this is the only role-capsule package that opens a file.
- It holds no selection or composition rule; adding one here would put policy in the I/O tier and
  split the compiler's decision surface in two.
- `__all__` is the authoritative export list and is deliberately short — four names, matching the
  two responsibilities.

### Todos

None recorded.

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The admitted compile entry point this package exports. | `compile_admitted_capsule`; `CapsuleCompilationOutcome` | mcp/src/agents_remember/application/role_capsules/compilation.py:89-122; mcp/src/agents_remember/application/role_capsules/compilation.py:46-88 |
| The root-confined source admission this package exports. | `admit_capsule_sources`; `CapsuleAdmissionRequest` | mcp/src/agents_remember/application/role_capsules/sources.py:78-94; mcp/src/agents_remember/application/role_capsules/sources.py:38-77 |
| The pure compiler this boundary feeds, which owns every selection rule. | `compile_role_capsule` | mcp/src/agents_remember/models/role_capsules/compiler.py:84-140 |
| The sibling model package whose contract this boundary resolves inputs for. | `CapsuleBinding`; `CapsuleSource` | mcp/src/agents_remember/models/role_capsules/types.py:283-300; mcp/src/agents_remember/models/role_capsules/sources.py:49-91 |

## Cross-Repo References

No sibling-repository contract consumes this boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the application-tier
  role-capsule package export surface added by the deterministic capsule compiler leaf
  (`CAPS-R02@v1`). Records the I/O-owns-no-policy invariant, the four-name export list and its
  two responsibilities, and the boundary against the pure compiler. Verification metadata is left
  at the leaf base commit because the source is uncommitted — the governed closeout stamps the
  real code commit.
