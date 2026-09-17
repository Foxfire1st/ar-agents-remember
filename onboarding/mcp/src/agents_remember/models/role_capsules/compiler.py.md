# mcp/src/agents_remember/models/role_capsules/compiler.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/compiler.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T09:38+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[models overview](../overview.md)

## Purpose

The deterministic, harness-independent role-capsule compiler: one pure function that turns
admitted facts plus canonical source bytes into an ordered capsule **and an explanation of
itself**. It opens no file, reaches no network, and calls no model — reading sources is the
application boundary's job, and this module is an ordinary function over what that boundary
admitted.

## Code Commentary

### Logic

cit:([`compile_role_capsule`], mcp/src/agents_remember/models/role_capsules/compiler.py:90-153) is the whole pipeline, and its step order is the
contract:

1. cit:([`parse_composition_manifest`], mcp/src/agents_remember/models/role_capsules/manifest.py:168-216) — parse the authored metadata;
2. cit:([`select_scope`], mcp/src/agents_remember/models/role_capsules/selection.py:114-132) — turn the admitted binding into a scope, refusals included;
3. cit:([`sources_by_path`, `identity_index`], mcp/src/agents_remember/models/role_capsules/source_set.py:50-64; mcp/src/agents_remember/models/role_capsules/source_set.py:65-90) and cit:([`admit_source_set`], mcp/src/agents_remember/models/role_capsules/source_set.py:91-108) — prove the admitted files match the locked plan;
4. cit:([`gather_candidates`, `resolve_instructions`], mcp/src/agents_remember/models/role_capsules/resolution.py:93-134; mcp/src/agents_remember/models/role_capsules/resolution.py:135-191) — reduce each identity to one block and stop on an unresolved contradiction;
5. cit:([`narrow_tool_requests`], mcp/src/agents_remember/models/role_capsules/tools.py:24-58) — narrow the requested **tool ids** to the admitted policy;
6. cit:([`skill_references`], mcp/src/agents_remember/models/role_capsules/compiler.py:154-193) — build one reference per declared skill. This step is **not** a narrowing step: no policy is consulted, and the reference is content-addressed from the admitted skill root file;
7. cit:([`semantic_digest`], mcp/src/agents_remember/models/role_capsules/compiler.py:225-272) — the seal.

The work is split across sibling modules so each part can be understood and tested alone. What
*this* module owns is the seal: the semantic digest and the diagnostic manifest.

**The digest covers admitted facts and the composed bytes, and nothing else.**
cit:([`semantic_digest`], mcp/src/agents_remember/models/role_capsules/compiler.py:225-272) builds a canonical `\t`-separated document from
the seat kind, seat key, role, operation, repository, work branch, task reference and its
document digest, the requirement identities, the specializations **actually composed**, one
`block` line per composed block with its revision, one `tool` line per requested tool id, one
`skill` line per carried skill reference (`origin`, `identity`, `revision`), and the task
context's origin/revision/digest. It deliberately excludes unselected sources, refusal
detail, wall-clock values, and the diagnostic manifest itself — so the identity of a
compilation does not move when only diagnostics do. Note the asymmetry that carries real
weight: cit:([`_selected_specializations`], mcp/src/agents_remember/models/role_capsules/compiler.py:294-297) contributes only specializations that
were **composed**; an admitted-but-unselected specialization changes the diagnostics and must
not change the capsule.

**The two capability channels enter the digest differently, and neither is a grant.**
Requested **tool ids** appear as sorted `tool` lines after being policy-narrowed; carried
**skill references** appear as `skill` lines and were never policy-checked. A skill reference is
a pointer to separately delivered content, so the only thing that can invalidate it is a missing
or unadmitted skill root file — which is refused upstream, not here.

The task-context channel is separate and verified: cit:([`verified_task_context`], mcp/src/agents_remember/models/role_capsules/compiler.py:194-224)
re-digests the supplied markdown and refuses (`task-context-digest-mismatch`) when it does not
match the digest the projection declared, because an unverifiable projection must not be
carried into a capsule.

The diagnostic half is built by cit:([`compiled_manifest`], mcp/src/agents_remember/models/role_capsules/compiler.py:388-416), with two refusal-side
builders: cit:([`refused_manifest`], mcp/src/agents_remember/models/role_capsules/compiler.py:417-432) for a refusal reached before the manifest could be
parsed, and cit:([`manifest_for_error`], mcp/src/agents_remember/models/role_capsules/compiler.py:433-447) when the admitted facts were already known.
cit:([`UNREAD_REVISION`], mcp/src/agents_remember/models/role_capsules/compiler.py:84-85) is the deliberately-not-a-content-digest revision
recorded for a declared source whose bytes were never admitted.

### Conventions

A refusal is a typed exception, never a partially filled capsule. The module-level schema
cit:([`MANIFEST_SCHEMA`], mcp/src/agents_remember/models/role_capsules/compiler.py:71-81) (`ar-role-capsule-manifest/v1`) names the diagnostic manifest
format and is itself part of the digest document.

### Invariants And Boundaries

- **No I/O, no network, no model.** Composition must succeed with model and network access
  denied; the module imports no network client. The shipped cases assert both.
- **Compilation failure never becomes a partially valid capsule.** Every defect raises a typed
  `CapsuleCompilationError` before any content is returned.
- The semantic digest excludes ephemeral facts. Adding a timestamp, an unselected source, or a
  refusal message to it would make two identical compilations differ.
- An admitted-but-unselected specialization is diagnostics, not identity.
- A task projection whose bytes do not match its declared digest is refused, not carried.
- `UNREAD_REVISION` must stay distinguishable from a real content digest; never substitute a
  computed digest for an unread source.
- **Tool requests are narrowed; skill references are carried.** `narrow_tool_requests` is the only
  policy-narrowing path and it applies to tool ids alone. `skill_references` consults no policy —
  a declared skill always yields a reference, and the only failure mode is a skill root file that
  was not admitted (refused upstream, by name). Never describe a skill reference as narrowed,
  permitted, or granted.
- A declared skill that cannot be resolved is a refusal, not a silently dropped reference:
  dropping it would be the same silent omission as dropping a required instruction block.
- **The layer contract is a target, not a description of today's tree.** `layers.toml` declares
  that a module in package `P` may import `Q` only when `rank(Q) < rank(P)`, and it deliberately
  fails against the current tree. Measured on this candidate the tree reports 16 pre-existing
  violations (all `worktrees -> memory_quality` and its siblings); **none names a role-capsule
  module**, every internal import from the new modules points at a strictly lower rank, and there
  are 0 undeclared imports. Onboarding that presents the layer contract as currently satisfied is
  wrong.

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
| The application entry point that admits bytes from disk and calls this compiler, returning success or refusal as a value. | `compile_admitted_capsule`; `CapsuleCompilationOutcome` | mcp/src/agents_remember/application/role_capsules/compilation.py:89-122; mcp/src/agents_remember/application/role_capsules/compilation.py:46-88 |
| The diagnostic shapes this module fills and the ordering rule that keeps them out of the digest. | `CapsuleManifest`; `CapsuleSourceRecord`; `CapsuleRejection` | mcp/src/agents_remember/models/role_capsules/diagnostics.py:105-217; mcp/src/agents_remember/models/role_capsules/diagnostics.py:38-58; mcp/src/agents_remember/models/role_capsules/diagnostics.py:73-96 |
| **The carried skill channel** — one content-addressed reference per declared skill, built with no policy call. | `skill_references`; `CapsuleSkillReference`; `skills_declared_identity` | mcp/src/agents_remember/models/role_capsules/compiler.py:154-193; mcp/src/agents_remember/models/role_capsules/types.py:414-434; mcp/src/agents_remember/models/role_capsules/sources.py:126-138 |
| The determinism cases: identical input to identical content and digest, order as identity, and a real binding change moving the digest. | `test_identical_input_compiles_to_identical_ordered_content_and_digest`; `test_reordering_the_composed_blocks_changes_the_semantic_digest`; `test_a_real_binding_change_does_move_the_semantic_digest` | mcp/tests/test_role_capsule_compiler.py:377-388; mcp/tests/test_role_capsule_compiler.py:422-446; mcp/tests/test_role_capsule_compiler.py:447-460 |
| Ephemeral diagnostics do not move identity, while an applicable block change does; an unrelated role never reaches another role's capsule. | `test_a_declared_but_unselected_specialization_changes_diagnostics_not_identity`; `test_changing_an_applicable_operation_block_changes_that_capsule`; `test_changing_an_unrelated_role_leaves_the_worker_capsule_untouched` | mcp/tests/test_role_capsule_compiler.py:400-421; mcp/tests/test_role_capsule_compiler.py:472-483; mcp/tests/test_role_capsule_compiler.py:461-471 |
| Composition requires neither model nor network, and no network client is imported. | `test_composition_succeeds_with_network_and_model_access_denied`; `test_the_compiler_modules_import_no_network_client` | mcp/tests/test_role_capsule_compiler.py:868-889; mcp/tests/test_role_capsule_compiler.py:890-930 |
| A refusal still produces an explanation manifest carrying its remedy, and an unverifiable projection is refused. | `test_a_refusal_still_produces_an_explanation_manifest`; `test_a_projection_whose_bytes_do_not_match_its_digest_is_refused` | mcp/tests/test_role_capsule_compiler.py:851-867; mcp/tests/test_role_capsule_compiler.py:822-836 |
| The typed refusal this module raises for every defect class. | `CapsuleCompilationError`; `CapsuleManifestError`; `CapsuleSourceError` | mcp/src/agents_remember/errors.py:464-507; mcp/src/agents_remember/errors.py:508-511; mcp/src/agents_remember/errors.py:512-513 |

## Cross-Repo References

No sibling-repository contract is consumed. The reference implementation studied during design
was eve's dynamic resolver; that is a design input recorded in the leaf's requirement packet,
not a runtime boundary of this module, and no eve code is imported.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T09:38+02:00 — 260915-CAPS-L2 curator: corrected against the A3 candidate, which added a real skill-reference producer. The pipeline is now **seven** steps: `skill_references` (this module, previously absent) builds one content-addressed reference per declared skill, and `semantic_digest` gained a `skills` parameter, so the digest document now carries a `skill <origin> <identity> <revision>` line per reference. Added the explicit statement that the two capability channels enter the digest differently and neither is a grant — tool ids are policy-narrowed, skill references are carried and never policy-checked — plus an invariant forbidding the "narrowed/permitted/granted" description of a skill reference, and a new reference row for the carried channel. Every line range in this card was refreshed (the module grew 431 → 506 lines), and the refusal row now names all three current subclasses. Verification metadata stays at the leaf base commit — the closeout stamps the real code commit.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the deterministic
  capsule compiler added by this leaf (`CAPS-R02@v1`). Records the six-step pipeline and its
  order, the digest's inclusion/exclusion rule with the admitted-but-unselected specialization
  asymmetry, the verified task-context channel, the two refusal-side manifest builders, and the
  no-I/O / no-partial-capsule invariants. Verification metadata is left at the leaf base commit
  because the source is uncommitted — the governed closeout stamps the real code commit.
