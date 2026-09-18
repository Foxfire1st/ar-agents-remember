# mcp/src/agents_remember/models/role_capsules/selection.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/selection.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[models overview](../overview.md)

## Purpose

Explicit role, seat-kind, and operation selection over the canonical manifest. **Selection is a
lookup, not an inference.** The seat and the operation arrive on the admitted binding; the
manifest is asked which blocks that pair composes from. There is no model call, no scoring, no
fallback operation, no nearest-match role, and no combinatorial role-by-phase rule language —
three ordinary lookups and two refusals.

## Code Commentary

### Logic

cit:([`select_scope`], mcp/src/agents_remember/models/role_capsules/selection.py:114-132) is the entry point and returns a
cit:([`CapsuleScope`], mcp/src/agents_remember/models/role_capsules/selection.py:56-113) whose cit:([`declared`], mcp/src/agents_remember/models/role_capsules/selection.py:70-112) method yields the declared instruction units for that
seat. cit:([`_role_scope`], mcp/src/agents_remember/models/role_capsules/selection.py:133-148) resolves the role branch and
cit:([`_require_operation_allowed`], mcp/src/agents_remember/models/role_capsules/selection.py:149-175) enforces applicability.

Two refusals carry most of the weight here, and they are deliberately **distinct** because they
have distinct remedies:

- cit:([`narrow_role`], mcp/src/agents_remember/models/role_capsules/selection.py:191-213) and cit:([`narrow_operation`], mcp/src/agents_remember/models/role_capsules/selection.py:176-190) refuse an unknown role or operation by **exact
  membership** in the frozen vocabulary, so a caller-controlled string can never acquire a role;
- `_require_operation_allowed` refuses an operation the selected role cannot run rather than
  replacing it with a neighbouring one, *because silently substituting a different operation is
  a silent fallback wearing a lookup's clothes*.

The ambient launcher is reached as a seat kind, not a role: it composes `core/launcher.md` plus
`core/authority.md`, and it is refused any operation it does not itself declare. Identity is
therefore never derived from caller text.

### Conventions

`CapsuleScope` is constructed only by `select_scope`, so a caller cannot assemble a scope that
bypassed selection. A new role or operation does not belong here — it belongs in
`vocabulary.py` plus the manifest.

### Invariants And Boundaries

- Selection never infers. An unknown role, an unknown operation, and an operation the role
  cannot run are three separate typed refusals with three separate remedies.
- No fallback operation, no nearest-match role, no default seat. A missing applicability entry is
  a refusal, not an empty composition.
- Membership is exact string equality against `CAPSULE_ROLES` / `CAPSULE_OPERATIONS`; no case
  folding, prefix matching, or alias table exists.
- This module reads no file and calls no model; the manifest arrives already parsed.

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
| The frozen vocabularies membership is tested against. | `CAPSULE_ROLES`; `CAPSULE_OPERATIONS`; `capsule_role_or_none` | mcp/src/agents_remember/models/role_capsules/vocabulary.py:64-75; mcp/src/agents_remember/models/role_capsules/vocabulary.py:77-89; mcp/src/agents_remember/models/role_capsules/vocabulary.py:108-121; mcp/src/agents_remember/models/role_capsules/vocabulary.py:98-108; mcp/src/agents_remember/models/role_capsules/vocabulary.py:133-144 |
| The three selection refusals this module's callers branch on. | `STATUS_UNKNOWN_ROLE`; `STATUS_UNKNOWN_OPERATION`; `STATUS_OPERATION_NOT_APPLICABLE` | mcp/src/agents_remember/models/role_capsules/statuses.py:11-13 |
| The parsed manifest and its per-role applicability entries. | `CapsuleCompositionManifest`; `CapsuleRoleEntry`; `CapsuleLauncherEntry` | mcp/src/agents_remember/models/role_capsules/manifest.py:120-167; mcp/src/agents_remember/models/role_capsules/manifest.py:63-82; mcp/src/agents_remember/models/role_capsules/manifest.py:83-93 |
| The compiler step that calls this selection first. | `compile_role_capsule` | mcp/src/agents_remember/models/role_capsules/compiler.py:90-153 |
| The unknown-role, unknown-operation, non-applicable-operation and launcher cases. | `test_unknown_role_is_refused_and_never_acquires_a_capsule`; `test_unknown_operation_is_refused_instead_of_falling_back`; `test_operation_the_role_cannot_run_is_refused_instead_of_substituted`; `test_launcher_seat_composes_its_own_core_and_is_not_a_tenth_role`; `test_launcher_is_refused_an_operation_no_role_inherits_to_it` | mcp/tests/test_role_capsule_compiler.py:500-518; mcp/tests/test_role_capsule_compiler.py:519-526; mcp/tests/test_role_capsule_compiler.py:527-534; mcp/tests/test_role_capsule_compiler.py:535-543; mcp/tests/test_role_capsule_compiler.py:544-556 |

## Cross-Repo References

No sibling-repository contract defines this selection rule.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the role/seat/operation
  selection module added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the
  lookup-not-inference rule, the three distinct selection refusals, the launcher-as-seat-kind
  handling, and the no-fallback/no-alias invariants. Verification metadata is left at the leaf base
  commit because the source is uncommitted — the governed closeout stamps the real code commit.
