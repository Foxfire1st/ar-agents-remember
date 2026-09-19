# mcp/src/agents_remember/models/role_capsules/selection.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/selection.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `47570cd827428c171613c8cb01e01f0b1cb26f73` |
| lastVerifiedCommitDate | 2026-09-20T01:58:41+02:00|
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

- cit:([`narrow_role`], mcp/src/agents_remember/models/role_capsules/selection.py:191-213) and cit:([`narrow_operation`], mcp/src/agents_remember/models/role_capsules/selection.py:194-206) refuse an unknown role or operation by **exact
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
| The frozen vocabularies membership is tested against: `capsule_role_or_none` answers by exact membership in the frozen registry. | "exact membership in the frozen registry" | mcp/src/agents_remember/models/role_capsules/vocabulary.py:171-183 |
| The three selection refusals this module's callers branch on. | `STATUS_UNKNOWN_ROLE`; `STATUS_UNKNOWN_OPERATION`; `STATUS_OPERATION_NOT_APPLICABLE` | mcp/src/agents_remember/models/role_capsules/statuses.py:11-13 |
| The parsed manifest and its per-role applicability entries. | `CapsuleCompositionManifest`; `CapsuleRoleEntry`; `CapsuleLauncherEntry` | mcp/src/agents_remember/models/role_capsules/manifest.py:120-167; mcp/src/agents_remember/models/role_capsules/manifest.py:63-82; mcp/src/agents_remember/models/role_capsules/manifest.py:83-93 |
| The compiler step that calls this selection first. | `compile_role_capsule` | mcp/src/agents_remember/models/role_capsules/compiler.py:89-145 |
| The unknown-role, unknown-operation, non-applicable-operation and launcher cases; the two launcher cases -- the launcher composes its own core, and no role's operation is inherited to it -- are now one case, because they are one rule. | `test_unknown_role_is_refused_and_never_acquires_a_capsule`; `test_unknown_operation_is_refused_instead_of_falling_back`; `test_operation_the_role_cannot_run_is_refused_instead_of_substituted`; `test_the_launcher_seat_composes_its_own_core_and_inherits_no_role_operation` | mcp/tests/test_role_capsule_compiler.py:526-542; mcp/tests/test_role_capsule_compiler.py:545-550; mcp/tests/test_role_capsule_compiler.py:553-558; mcp/tests/test_role_capsule_compiler.py:561-580 |

## Cross-Repo References

No sibling-repository contract defines this selection rule.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-09-19T22:40+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): **re-read each claim below against the construct its range now covers, corrected the wording where the construct had moved, re-derived every range from the construct's real extent in the file the claim cites, and only then left the card's stamp to closeout.** No `Generated citation repair` bullet is written: these are curator edits, not a mechanical projection. `selection.py.md:84` — re-read: the two launcher cases were consolidated into one, `test_the_launcher_seat_composes_its_own_core_and_inherits_no_role_operation`, whose docstring says 'The positive shape and the refusal it implies are one rule -- the launcher's composition is its own -- so they are one case'. Both halves the claim names survive inside it.

2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `compile_role_capsule` repointed to mcp/src/agents_remember/models/role_capsules/compiler.py:89-145. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `narrow_operation` repointed to mcp/src/agents_remember/models/role_capsules/selection.py:194-206. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the role/seat/operation
  selection module added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the
  lookup-not-inference rule, the three distinct selection refusals, the launcher-as-seat-kind
  handling, and the no-fallback/no-alias invariants. Verification metadata is left at the leaf base
  commit because the source is uncommitted — the governed closeout stamps the real code commit.
