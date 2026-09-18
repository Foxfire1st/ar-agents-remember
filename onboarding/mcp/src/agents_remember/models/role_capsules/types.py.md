# mcp/src/agents_remember/models/role_capsules/types.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/types.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[models overview](../overview.md)

## Purpose

The frozen input/output contract for the deterministic role-capsule compiler: the value
types an admitted AR binding, a compiled capsule, and the diagnostic manifest are made of.
Every later consumer (task projection, MCP delivery, a harness adapter) reads these shapes
and does not redefine them — a consumer that believes one is wrong reports that to the owner
rather than forking a second shape.

## Code Commentary

### Logic

Three planes are kept structurally apart, because collapsing any two of them is the failure
this contract exists to prevent:

- **admitted input** — cit:([`CapsuleAdmittedFacts`, `CapsuleBinding`], mcp/src/agents_remember/models/role_capsules/types.py:198-227; mcp/src/agents_remember/models/role_capsules/types.py:299-318).
  Every field is decided by an existing AR owner: the seat, the task reference and its
  document digest, the requirements, the work branch, and the `CapsuleToolPolicy` snapshot
  that cit:(["def permits"], mcp/src/agents_remember/models/role_capsules/types.py:193-194) answers subset questions from. The compiler never infers a role from prose
  and never grants a capability.
- **content output** — cit:([`CapsuleCapsule`], mcp/src/agents_remember/models/role_capsules/types.py:450-463) carries ordered cit:([`CapsuleInstructionUnit`], mcp/src/agents_remember/models/role_capsules/types.py:378-395) values, the optional task context, skill references, requested tools,
  and the `semantic_digest` that names the compilation.
- **diagnostic output** — the manifests live in the sibling `diagnostics` module and never
  feed that digest.

The seat is a two-shaped union rather than one widened type: cit:([`CapsuleRoleSeat`], mcp/src/agents_remember/models/role_capsules/types.py:130-150) carries a role and an altitude, while cit:([`CapsuleLauncherSeat`], mcp/src/agents_remember/models/role_capsules/types.py:153-179) carries a
routing condition and deliberately returns `None` for both `role` and `block_identity`. That
is the type-level form of "the ambient launcher is a routing condition, not a tenth role" —
a launcher cannot silently acquire a role by defaulting a field.

Two digests are computed here and nowhere else: cit:([`compute_content_digest`], mcp/src/agents_remember/models/role_capsules/types.py:81-86) over raw bytes and
cit:([`compute_semantic_digest`], mcp/src/agents_remember/models/role_capsules/types.py:87-92) over a canonical document string. Both are `sha256`-prefixed and validated by
cit:([`_require_digest`], mcp/src/agents_remember/models/role_capsules/types.py:99-113), so a caller cannot hand a shape a digest-shaped string that is not one.

The selection and conflict vocabularies are declared as module constants
cit:([`SELECTION_SHARED_CORE`, `SUPERSEDE_EXPLICIT`, `CONFLICT_EQUAL_AUTHORITY`], mcp/src/agents_remember/models/role_capsules/types.py:68-78) so that a selection reason or a
conflict kind has exactly one spelling across the compiler, the resolution module, and the
diagnostic manifest.

### Conventions

Every value type is a `@dataclass(frozen=True, slots=True)` with a `__post_init__` that
refuses a blank or malformed field rather than normalizing it. Immutability is not decorative:
these objects travel into the diagnostic manifest, and the digest is computed over their
fields, so an in-place edit would silently desynchronize identity from content.

### Invariants And Boundaries

- **Layer placement is load-bearing.** This package holds only dependency-free value types,
  canonical source parsing, and selection logic, so it sits in `models`. The module opens no
  file, reaches no network, and calls no model; reading a source file from disk, resolving an
  admitted coordination root, and encoding bytes belong to
  `mcp/src/agents_remember/application/role_capsules`.
- The admitted input is **not** derived from the manifest or from prose. `CapsuleBinding.operation`
  is an explicit value; a caller-controlled string can never become a role.
- `CapsuleToolPolicy.granted` is what an existing AR owner already permits. A capsule *requests*
  capabilities; nothing here can add a tool the policy did not already permit.
- A digest field must be a `sha256:`-prefixed digest; a blank identity or a blank authority is
  refused at construction.
- `CapsuleLauncherSeat.role` and `.block_identity` return `None` permanently. Do not "fix" them
  into returning a launcher-named role — the launcher has its own core block and no role block.
- These shapes are frozen for the master's consumers. Extending them is an owner decision;
  a consumer must not fork a local variant.

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
| The frozen role and operation vocabulary these types are declared against. | "type CapsuleRole = Literal["; "type CapsuleOperation = Literal["; `CAPSULE_ROLES`; `CAPSULE_OPERATIONS` | mcp/src/agents_remember/models/role_capsules/vocabulary.py:36-47; mcp/src/agents_remember/models/role_capsules/vocabulary.py:50-60; mcp/src/agents_remember/models/role_capsules/vocabulary.py:82-93; mcp/src/agents_remember/models/role_capsules/vocabulary.py:98-108 |
| The stable refusal codes a binding or selection defect resolves to. | `CAPSULE_STATUSES` | mcp/src/agents_remember/models/role_capsules/statuses.py:27-41 |
| The pure compiler that consumes these shapes and produces the sealed result. | `compile_role_capsule` | mcp/src/agents_remember/models/role_capsules/compiler.py:84-139 |
| The diagnostic half of the contract, kept structurally out of the digest. | `CapsuleManifest`; `CapsuleSourceRecord`; `CapsuleRejection` | mcp/src/agents_remember/models/role_capsules/diagnostics.py:105-137; mcp/src/agents_remember/models/role_capsules/diagnostics.py:38-56; mcp/src/agents_remember/models/role_capsules/diagnostics.py:73-94 |
| The application boundary that does the I/O this module refuses to do. | `compile_admitted_capsule`; `admit_capsule_sources` | mcp/src/agents_remember/application/role_capsules/compilation.py:89-122; mcp/src/agents_remember/application/role_capsules/sources.py:68-89 |
| Compound identity, digest and order properties are pinned by executable cases. | `test_identical_input_compiles_to_identical_ordered_content_and_digest`; `test_reordering_the_composed_blocks_changes_the_semantic_digest` | mcp/tests/test_role_capsule_compiler.py:377-388; mcp/tests/test_role_capsule_compiler.py:422-446 |

## Cross-Repo References

No sibling-repository contract defines these value types. The reference implementation this
master studied is eve's dynamic resolver, which is a design input to CAPS-R02 rather than a
runtime boundary of this module; no eve code is imported here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `CapsuleCapsule` repointed to mcp/src/agents_remember/models/role_capsules/types.py:450-463. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the frozen role-capsule
  contract added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the
  three-plane separation (admitted input / content output / diagnostic output), the two-shaped
  seat union that keeps the launcher out of the role registry, the two digest functions, and the
  `models` layer placement that keeps file and network I/O in the application boundary.
  Verification metadata is left at the leaf base commit because the source is uncommitted — the
  governed closeout stamps the real code commit, and no hash was invented here.
