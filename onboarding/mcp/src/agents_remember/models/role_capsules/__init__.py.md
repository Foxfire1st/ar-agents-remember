# mcp/src/agents_remember/models/role_capsules/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[models overview](../overview.md)

## Purpose

The single import surface for the frozen role-capsule contract and the deterministic compiler
that fills it. Consumers import the whole contract from the package — *not* from its submodules —
so that the internal split into a content half and a diagnostic half stays an implementation
detail rather than a second public API.

## Code Commentary

### Logic

The package docstring states the two boundaries that govern every module inside it: this package
holds the frozen DTO surface plus the pure logic that turns an admitted AR binding and canonical
instruction sources into one capsule, and **it holds no I/O** — reading sources from disk is
`agents_remember.application.role_capsules`.

The re-export block is grouped by owning module, which is also the reading order of the contract:
cit:([`MANIFEST_SCHEMA`, `compile_role_capsule`, `compiled_manifest`, `refused_manifest`], mcp/src/agents_remember/models/role_capsules/__init__.py:9-14) from the compiler;
cit:([`CapsuleManifest`, `CapsuleSourceRecord`, `CapsuleConflictRecord`, `CapsuleRejection`, `CapsuleRefusalOptions`], mcp/src/agents_remember/models/role_capsules/__init__.py:15-21) from diagnostics;
cit:([`COMPOSITION_MANIFEST_SCHEMA`, `CapsuleCompositionManifest`, `parse_composition_manifest`], mcp/src/agents_remember/models/role_capsules/__init__.py:22-26) from the manifest parser;
cit:([`select_scope`], mcp/src/agents_remember/models/role_capsules/__init__.py:27-27) from selection;
cit:([`CapsuleDeclaredInstruction`, `CapsuleSource`, `specializations_declared_identity`], mcp/src/agents_remember/models/role_capsules/__init__.py:28-32) from the plan;
the DTOs from types; and cit:([`CAPSULE_LAUNCHER_MODE`, `CAPSULE_OPERATIONS`, `CAPSULE_ROLES`], mcp/src/agents_remember/models/role_capsules/__init__.py:63-67) from the vocabulary.
cit:([`__all__`], mcp/src/agents_remember/models/role_capsules/__init__.py:69-117) enumerates all 48 exported names.

### Conventions

A new public contract name is added to the re-export block **and** to `__all__` in the same edit.
Consumers write `from agents_remember.models.role_capsules import …`; reaching into a submodule
directly bypasses the frozen surface and is how a second shape gets forked.

### Invariants And Boundaries

- This package is a contract surface, not a convenience barrel: everything here is part of the
  frozen interface the master's consumers read.
- The package holds **no I/O**. `application.role_capsules` is the only role-capsule code that
  opens a file.
- The split between the content half (`types`, `compiler`) and the diagnostic half
  (`diagnostics`) is deliberate and must not be flattened by re-exporting a merged shape.
- `__all__` is the authoritative export list; an added module-level name that is not listed is
  not part of the contract.

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
| The frozen DTO surface this package re-exports. | `CapsuleAdmittedFacts`; `CapsuleCapsule`; `CapsuleCompilationResult`; `CapsuleBinding` | mcp/src/agents_remember/models/role_capsules/types.py:198-227; mcp/src/agents_remember/models/role_capsules/types.py:435-448; mcp/src/agents_remember/models/role_capsules/types.py:451-475; mcp/src/agents_remember/models/role_capsules/types.py:299-318 |
| The I/O boundary this package deliberately does not contain. | `compile_admitted_capsule`; `admit_capsule_sources` | mcp/src/agents_remember/application/role_capsules/compilation.py:89-122; mcp/src/agents_remember/application/role_capsules/sources.py:78-94 |
| The sibling package that owns admitted-context resolution and reading. | `CapsuleCompilationOutcome`; `CapsuleAdmissionRequest` | mcp/src/agents_remember/application/role_capsules/__init__.py:9-23 |
| The layer contract that places these value types in `models` and the I/O in `application`; it declares the target order (`errors < kernel < models < … < application < mcp < cli`) and states that it fails against the tree until the named leaf moves the code. | `[contract]`; `rule` | layers.toml:17-24 |
| The fitness function and where its result is produced. **Measured on this candidate: the tree does not yet satisfy its own declared target — 16 pre-existing violations, all `worktrees -> memory_quality` and its siblings; none names a role-capsule module and there are 0 undeclared imports.** Do not read this contract as currently satisfied. | `check_layering`; `LayeringReport` | mcp/test_support/agents_remember_test_support/code_quality/layering.py:334-334 |
| The unit tests that pin the fitness function itself (not this candidate's result). | `_write_tree` | mcp/tests/test_layering.py:1-12 |

## Cross-Repo References

No sibling-repository contract consumes this package directly.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the role-capsule package
  export surface added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the
  re-export grouping as the contract reading order, the `__all__`-completeness convention, and the
  no-I/O and content/diagnostic-split invariants. Verification metadata is left at the leaf base
  commit because the source is uncommitted — the governed closeout stamps the real code commit.
