# mcp/src/agents_remember/models/role_capsules/source_set.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/source_set.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T09:38+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[models overview](../overview.md)

## Purpose

Validation of an admitted source set against the manifest's declared plan — in **both
directions**. This module is what makes "a required block is missing" a falsifiable statement
rather than a vacuous one.

## Code Commentary

### Logic

The compiler never derives the file list from the manifest. *Deriving it would make "a required
block is missing" unfalsifiable — the compiler would only ever see the subset the manifest asked
for, so the check could not fail.* Instead the plan is locked first
(cit:([`CapsuleDeclaredInstruction`], mcp/src/agents_remember/models/role_capsules/sources.py:32-49)), the admitted paths are supplied explicitly, and
cit:([`admit_source_set`], mcp/src/agents_remember/models/role_capsules/source_set.py:91-108) proves the two agree both ways through five gates:

| Gate | Source | Direction | Refuses |
| --- | --- | --- | --- |
| `_require_manifest_admitted` | mcp/src/agents_remember/models/role_capsules/source_set.py:109-136 | manifest → admitted | the manifest itself was not admitted |
| `_require_identities_agree` | mcp/src/agents_remember/models/role_capsules/source_set.py:137-173 | admitted → declared | a path admitted as an identity the manifest does not route it from, or read from the wrong composition root |
| `_require_declared_present` | mcp/src/agents_remember/models/role_capsules/source_set.py:174-194 | manifest → admitted | a path the manifest routes **to** that was never admitted — the missing mandatory block |
| `_require_declared_skills_present` | mcp/src/agents_remember/models/role_capsules/source_set.py:195-228 | manifest → admitted | a **declared skill whose root file was never admitted**, so its revision would be a fiction |
| `_require_specializations_admitted` | mcp/src/agents_remember/models/role_capsules/source_set.py:229-250 | binding → admitted | a repository specialization selected without being admitted on the binding |

The skill gate is checked for **every declared skill, not only the selected seat's**, because a
skill file is a declared source like any other and admitting an incomplete source set is the
condition this module exists to refuse. The compiler additionally refuses a *referenced* skill
that is missing, so the metadata plane and the compiled plane both fail closed.

cit:([`sources_by_path`], mcp/src/agents_remember/models/role_capsules/source_set.py:50-64) and cit:([`identity_index`], mcp/src/agents_remember/models/role_capsules/source_set.py:65-90) build the two lookup maps the gates
consume.

The both-directions property is the whole design: a one-directional check would accept a set
that is merely "mostly right", **and a source set that is merely "mostly right" is exactly the
state that produces a capsule missing mandatory material.** Every refusal is a typed value.

### Conventions

A new gate belongs here rather than in the loader or the compiler, because this is the only
module that holds both the declared plan and the admitted set at once.

### Invariants And Boundaries

- Both directions are checked. Removing either direction silently converts a mandatory-block
  defect into a successful compilation.
- The admitted set is never used to *define* the plan. The plan comes from the manifest.
- A source whose declared composition root disagrees with the root it was routed from is refused;
  so is a specialization that the binding never admitted.
- **A declared skill's root file must be admitted**, or its content-addressed revision would be a
  fiction. This is checked for every declared skill, not only the selected seat's, because a skill
  file is a declared source like any other. Both planes fail closed: this gate refuses the missing
  bytes, and the compiler refuses the missing reference.
- Refusals are typed `CapsuleCompilationError` values; nothing here repairs, skips, or
  substitutes a source.
- This module holds no filesystem access — it validates already-admitted `CapsuleSource` values.

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
| The locked plan and admitted-source shapes this module compares. | `CapsuleDeclaredInstruction`; `CapsuleSource` | mcp/src/agents_remember/models/role_capsules/sources.py:32-49; mcp/src/agents_remember/models/role_capsules/sources.py:50-95 |
| The refusals this module raises. | `STATUS_MISSING_REQUIRED_INSTRUCTION`; `STATUS_SOURCE_NOT_DECLARED`; `STATUS_SOURCE_ROOT_MISMATCH`; `STATUS_SPECIALIZATION_NOT_ADMITTED` | mcp/src/agents_remember/models/role_capsules/statuses.py:14-21 |
| The compiler step that runs this validation before resolution. | `compile_role_capsule` | mcp/src/agents_remember/models/role_capsules/compiler.py:89-145 |
| The YAML-free source of the declared plan: the parsed canonical manifest. | `parse_composition_manifest` | mcp/src/agents_remember/models/role_capsules/manifest.py:168-216 |
| Missing mandatory material and wrongly-rooted/undeclared sources are refused rather than omitted. | `test_missing_mandatory_material_is_refused_rather_than_omitted`; `test_a_source_the_manifest_does_not_declare_is_refused`; `test_a_source_read_from_the_wrong_composition_root_is_refused`; `test_repository_specialization_must_be_admitted_on_the_binding` | mcp/tests/test_role_capsule_compiler.py:583-606; mcp/tests/test_role_capsule_compiler.py:609-613; mcp/tests/test_role_capsule_compiler.py:616-623; mcp/tests/test_role_capsule_compiler.py:626-631 |
| **The declared-skill gate** and its two directions: an incomplete admitted set refuses, and a referenced-but-missing skill refuses. | `_require_declared_skills_present`; `test_a_skill_reference_whose_root_file_is_not_admitted_is_refused`; `test_a_source_set_with_no_admitted_bytes_is_refused` | mcp/src/agents_remember/models/role_capsules/source_set.py:195-226; mcp/tests/test_role_capsule_admission.py:1040-1063; mcp/tests/test_role_capsule_admission.py:1135-1156 |

## Cross-Repo References

No sibling-repository contract defines this validation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `compile_role_capsule` repointed to mcp/src/agents_remember/models/role_capsules/compiler.py:89-145. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T09:38+02:00 — 260915-CAPS-L2 curator: corrected against the A3 candidate, which grew this module 213 → 255 lines and added a **fifth gate**. The card said "four gates"; it now documents `_require_declared_skills_present` — a declared skill whose root file was never admitted is refused, checked for **every** declared skill rather than only the selected seat's, because a skill file is a declared source like any other and a reference without admitted bytes has a fictional revision. Recorded that both planes fail closed (this gate refuses the missing bytes; the compiler refuses the missing reference) and added the matching invariant and reference row. Refreshed every range. Verification metadata stays at the leaf base commit — the closeout stamps the real code commit.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the admitted-source-set
  validation added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the
  four gates and their directions, and the load-bearing invariant that the both-directions check
  is what makes a missing mandatory block falsifiable. Verification metadata is left at the leaf
  base commit because the source is uncommitted — the governed closeout stamps the real code
  commit.
