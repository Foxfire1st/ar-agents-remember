# mcp/src/agents_remember/models/role_capsules/sources.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/sources.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T09:38+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80` |
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l11-ar` uncommitted source; base `a29a20c6eefea424a7e0321a54fcda2ed1b35098` |
| governingOverview      | `../overview.md`                           |

## Governing Overview

[models overview](../overview.md)

## Purpose

The **locked instruction-unit plan**, the loaded-source value, and the identity helpers that give
every block and skill reference one canonical spelling. Building the plan before reading anything
is what makes the "a required block is missing" check non-vacuous.

## Code Commentary

### Logic

cit:([`CapsuleDeclaredInstruction`], mcp/src/agents_remember/models/role_capsules/sources.py:32-49) is one *declared* instruction unit — a composition root
plus the block identity it must resolve to, plus the authorities that routed it.
cit:([`CapsuleSource`], mcp/src/agents_remember/models/role_capsules/sources.py:50-104) is the loaded counterpart: identity, composition root,
root-relative path, raw `content` bytes, and the `revision` that is the content digest of
those bytes.

The ordering rule is explicit: *the plan says which identities must resolve, and loading is
validated **against** the plan rather than defining it.* A loader that only ever fetched what
the manifest asked for could not express "this required block was never admitted" — which is
exactly the defect class the compiler must be able to report.

`CapsuleSource` carries **three guards of its own**, all reachable and all tested:

- its declared `revision` must equal the digest of its own bytes, or the value is refused — a
  source whose revision is not content-addressed breaks determinism at its root;
- cit:(["except UnicodeDecodeError as error:"], mcp/src/agents_remember/models/role_capsules/sources.py:85-101) decodes the bytes as UTF-8 and refuses
  **`source-not-utf8`** when they do not decode; and
- a source that decodes to nothing but whitespace is refused as **`source-empty`**, a typed
  `CapsuleSourceError` on the same boundary — *not* a bare `ValueError` escaping
  `CapsuleSource.text` (defect **D25**, repaired by `260915-CAPS-L11`). The two refusals are one
  class of defect and take one shape deliberately: `compile_admitted_capsule` catches only
  `CapsuleCompilationError`, so an untyped raise here would surface to an operator as a
  traceback rather than as the named refusal the compiler's own boundary promises. Emptiness is
  discovered while blocks are composed — *after* admission succeeded and a real manifest parsed —
  so the guard is reachable only through a real composition, which is why the leaf's case drives
  the shipped corpus rather than a fixture.

**The identity helpers are one vocabulary, and they cover skills as well as blocks.**
cit:([`instruction_identity`], mcp/src/agents_remember/models/role_capsules/sources.py:145-148) renders a block identity as `"<root>:<name>"`;
cit:([`specializations_declared_identity`], mcp/src/agents_remember/models/role_capsules/sources.py:151-172) resolves a nested
`specializations/<group>/<name>.md` to the same identity regardless of grouping folder;
cit:([`skills_declared_identity`], mcp/src/agents_remember/models/role_capsules/sources.py:175-185) renders a **skill** identity as `"<origin>#<skill>"` —
the origin is part of the identity because a bare skill name collides across servers, so the same
name from two servers is deliberately two different references; cit:([`shared_core_reference`], mcp/src/agents_remember/models/role_capsules/sources.py:205-208) names a
shared core block; and cit:([`root_of_identity`], mcp/src/agents_remember/models/role_capsules/sources.py:188-202) answers which composition root an identity belongs to
**for both shapes** — `<root>:<name>` carries its root, while a skill identity does not and is
recognised by its separator instead. Having exactly one function answer that is what keeps the
admitted-root agreement check and the identity index from disagreeing about skill identities.

Two module constants carry the on-disk convention: cit:([`INSTRUCTION_FILE_SUFFIX`], mcp/src/agents_remember/models/role_capsules/sources.py:27-28) and
cit:([`SPECIALIZATION_ROOT_DIRECTORY`], mcp/src/agents_remember/models/role_capsules/sources.py:27-28).

### Conventions

Every path here is **root-relative POSIX**. A `CapsuleSource.revision` is always the digest of
the bytes actually held in `content`; it is never copied from the manifest. Skill identities use
`#` and block identities use `:`; do not conflate the separators.

### Invariants And Boundaries

- This module holds values, their guards, and identity rules only. It reads no file — the
  filesystem lives in `mcp/src/agents_remember/application/role_capsules/sources.py`.
- A declared plan is built **before** any read. Do not reorder that: deriving the plan from what
  was successfully loaded would make a missing mandatory block unrepresentable.
- The declared identity of a nested specialization is path-invariant across grouping folders;
  two paths that resolve to one identity are a duplicate, not two blocks.
- `content` and `revision` must agree. A source whose revision was not computed from its own
  bytes breaks the "same bytes compile to the same capsule" property at its root.
- **`source-not-utf8` is raised here**, in the value layer, not in the application layer. A
  source that does not decode is a defect; it is never truncated, replaced, or decoded leniently.
- **`source-empty` is raised here too**, as a typed `CapsuleSourceError` rather than a
  `ValueError` (D25, `260915-CAPS-L11`). An admitted source that decodes to whitespace only is a
  source defect of the same class as the non-UTF-8 one: it is refused by name, with the source
  path and a next action, and it never escapes `CapsuleSource.text` as an exception the
  compiler's refusal boundary does not catch.
- `skills_declared_identity` requires a **non-blank** origin and name and raises `ValueError`
  otherwise; identity is `origin + skill`, so dropping the origin silently merges two servers'
  skills into one reference.

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
| The value types these shapes are composed from and the shared digest guards. | `CapsuleBlockIdentity`; `CapsuleDigest`; `compute_content_digest` | mcp/src/agents_remember/models/role_capsules/types.py:52-86 |
| The admission boundary that reads the bytes these values carry. | `admit_capsule_sources`; `CapsuleAdmissionRequest` | mcp/src/agents_remember/application/role_capsules/sources.py:78-94; mcp/src/agents_remember/application/role_capsules/sources.py:38-77 |
| The module that proves the admitted set agrees with this declared plan in both directions, including every declared skill root. | `admit_source_set`; `_require_declared_present`; `_require_declared_skills_present` | mcp/src/agents_remember/models/role_capsules/source_set.py:91-108; mcp/src/agents_remember/models/role_capsules/source_set.py:174-194; mcp/src/agents_remember/models/role_capsules/source_set.py:195-228 |
| The resolution step that reduces each declared identity to one block. | `gather_candidates`; `resolve_instructions` | mcp/src/agents_remember/models/role_capsules/resolution.py:93-134; mcp/src/agents_remember/models/role_capsules/resolution.py:135-191 |
| The identity helper the carried skill reference is built from: `skills_declared_identity` renders the skill identity, and the compiler's `skill_references` calls it once per skill the seat declares. | `skills_declared_identity` | mcp/src/agents_remember/models/role_capsules/sources.py:175-185 |
| Admission preserves content-addressed revisions and refuses a missing source. | `test_admission_reads_every_requested_source_with_its_content_digest`; `test_admission_refuses_a_missing_source_instead_of_skipping_it` | mcp/tests/test_role_capsule_admission.py:275-289; mcp/tests/test_role_capsule_admission.py:311-319 |
| The value guards for this module's declared `CapsuleSource.text`, including the non-UTF-8 refusal. | `test_a_source_whose_revision_is_not_its_own_digest_is_refused`; `test_a_source_with_no_readable_instruction_text_is_refused_by_name`; `test_a_source_with_a_blank_identity_or_path_is_refused` | mcp/tests/test_role_capsule_compiler.py:973-985; mcp/tests/test_role_capsule_compiler.py:988-996; mcp/tests/test_role_capsule_compiler.py:999-1012; mcp/tests/test_role_capsule_compiler.py:1157-1189 |

## Cross-Repo References

No sibling-repository contract defines these values.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-09-20T01:01+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 4 enforced citation rows this card carried (citation_claim_reopened, citation_anchor_absent_from_range). Three of them were one table row: the earlier mechanical projection had already repointed the blank-identity guard to `mcp/tests/test_role_capsule_compiler.py:1157-1189` and that range was verified against the source and left untouched, while the row's other two anchor names — `test_a_source_that_decodes_to_nothing_is_refused` and `test_a_source_that_is_not_utf8_text_is_refused` — exist nowhere in the tree because the empty-body and the non-UTF-8 case were consolidated into one test, so the Anchor cell now names `test_a_source_with_no_readable_instruction_text_is_refused_by_name`, which asserts both refusals at 993-1020 and is already inside the cited `988-996`. No range was changed, no claim wording was re-worded, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 1 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `test_a_source_with_a_blank_identity_or_path_is_refused`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `instruction_identity` repointed to mcp/src/agents_remember/models/role_capsules/sources.py:145-148. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `specializations_declared_identity` repointed to mcp/src/agents_remember/models/role_capsules/sources.py:151-172. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `skills_declared_identity` repointed to mcp/src/agents_remember/models/role_capsules/sources.py:175-185. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `shared_core_reference` repointed to mcp/src/agents_remember/models/role_capsules/sources.py:205-208. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `root_of_identity` repointed to mcp/src/agents_remember/models/role_capsules/sources.py:188-202. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T15:50+02:00 — 260915-CAPS-L11 curator (**final-verification leaf**): repaired this card's citation ranges against the L11 candidate (`a29a20c6` + the five declared paths) and recorded the **D25 repair** the candidate delivers. `CapsuleSource.text` now refuses an emptied source as a typed **`CapsuleSourceError(status="source-empty")`** instead of raising a bare `ValueError` that `compile_admitted_capsule` does not catch — one refusal shape for the non-UTF-8 and empty-source defects, stated in the body and in the invariants, with the new `source-empty` case ranging to `mcp/tests/test_role_capsule_admission.py`. Advance, not rewrite: `CapsuleSource` 50-95 → **50-104**, `text` 74-93 → **74-103**, `instruction_identity` 96-101 → **105-110**, `specializations_declared_identity` 102-125 → **111-134**, `skills_declared_identity` 126-138 → **135-147**, `root_of_identity` 139-155 → **148-164**, `shared_core_reference` 156-172 → **165-181**, and the types row 81-86 → **52-86** so it holds the `CapsuleBlockIdentity` anchor it names. The L14 curator's D7 table-shape repair above is untouched, as is every earlier entry and every verification stamp.

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T09:38+02:00 — 260915-CAPS-L2 curator: corrected against the A3 candidate, which grew this module 136 → 172 lines and changed what it owns. Added the **`CapsuleSource.text` UTF-8 guard and the `source-not-utf8` refusal** — this is where that code actually lives, and my curation report had wrongly recorded it as nonexistent after checking only the application layer — plus the revision-equals-digest and whitespace-only guards. Documented the **skill identity** helper `skills_declared_identity` (`<origin>#<skill>`, origin required so two servers' same-named skills stay distinct) and `root_of_identity`, which answers the composition root for **both** identity shapes and is what keeps the admitted-root check and the identity index from disagreeing. Added the matching invariants and two reference rows. Refreshed every range. Verification metadata stays at the leaf base commit — the closeout stamps the real code commit.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the locked
  instruction-unit plan added by the deterministic capsule compiler leaf (`CAPS-R02@v1`).
  Records why the plan is built before any read (a non-vacuous missing-block check), the three
  identity helpers and the grouping-folder-invariant specialization identity, and the
  content/revision agreement invariant. Verification metadata is left at the leaf base commit
  because the source is uncommitted — the governed closeout stamps the real code commit.
