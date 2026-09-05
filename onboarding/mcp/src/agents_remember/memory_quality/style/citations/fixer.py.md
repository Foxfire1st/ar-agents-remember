# mcp/src/agents_remember/memory_quality/style/citations/fixer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/fixer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T01:15+02:00 |
| lastVerifiedCommitHash | `709dd07671b07d85ac49eaf3b77f4609b1e5fc5f` |
| lastVerifiedCommitDate | 2026-09-04T00:53:17+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Regenerate citation ranges from anchors. Tree-wide mode edits only failing claims;
`--document` additionally normalizes every claim in that exact document, including a passing
provisional range; other documents remain byte-identical. Since CCR-R10 (260831-CCR-L10), every
repaired claim whose anchor resolves uniquely in the frozen source-index snapshot also stages a
deterministic anchor-to-range projection (see
`deterministic_projection.py.md`) with a generated no-content-impact Update History bullet,
bound to snapshot id, prior claim digest, resolved extent, new document digest, and repair-tool
version. Malformed sources, missing anchors, superseded table shapes, ambiguous/absent locations,
and now projection refusals are declined with a complete work order.

## Code Commentary

### Logic

Module-level surface (decorator-inclusive ranges):

- `Candidate` (class, lines 46-55) - One gating claim, or one passing claim selected for scoped normalisation.
- `Applied` (class, lines 58-66) - One claim's source list, before and after.
- `Refused` (class, lines 69-96) - One claim `--fix` left for the curator agent, with the facts it needs.
- `Result` (class, lines 99-110) - What one run of the fixer did, everything it refused, and every deterministic projection it staged.
- `table_sites` (function, lines 113-123) - Every conforming table row, with the span of its Source cell.
- `prose_sites` (function, lines 126-147) - Every `cit:` that opens and closes on ONE line, and the count of those that do not.
- `cit_bounds` (function, lines 150-160) - Each `cit:` opening parenthesis on the line, and its closer when there is one.
- `prose_site` (function, lines 163-167)
- `sites` (function, lines 170-173) - Every claim in one document whose source list can be rewritten in place.
- `scope_of` (function, lines 176-182)
- `failing` (function, lines 185-192) - Whether this claim carries a defect a regenerated range could clear.
- `Walk` (class, lines 195-203) - Run-scoped trees, sources, documents, and result for one candidate walk.
- `candidates` (function, lines 206-241) - Every repairable or duplicate-bearing claim, plus scoped passing claims.
- `Staging` (class, lines 244-250) - One run's pending writes: per-document edit batches, history bullets, and the shared UTC stamp (CCR-R10).
- `fix_onboarding_root` (function, lines 253-329) - Regenerate every repairable range in the memory tree, and report the rest; one run-level `Staging` collects edits and generated projection bullets, history bullets are inserted newest-first under each document's Update History heading, and every staged projection's `new_document_digest` is bound to its own document batch before the write.
- `_decide` (function, lines 332-398) - Decides one candidate; repairing claims additionally plan a deterministic projection (`deterministic_projection.plan_projection`) whose decline becomes a `Refused` and whose success is appended to `Result.projections` with its history bullet staged for the same batch.
- `_scoped_source` (function, lines 401-430) - Normalise each citation, exact-deduplicate it, and preserve verified spans.
- `_scoped_citation` (function, lines 433-489) - One original Source segment, generated only from anchors that segment verifies.
- `payload` (function, lines 492-537) - The complete offender list and the complete repair list, never a sample (L6-R15); since CCR-R10 also carries `projectionCount`, the full `projections` list, and `repairToolVersion`.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to
this module. The caller owns the write guard: `fix_onboarding_root` writes wherever it is
pointed, so the onboarding root must be a leaf memory worktree, never the official memory repo.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- A rewritten claim and its generated no-content-impact bullet always land in ONE document batch,
  so a mechanically moved range is never an untraced body edit (CCR-R10).
- `new_document_digest` binds the complete per-document batch, including grouped history bullets.
- Projection declines are deterministic and never fall back to the old range.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `Candidate` (lines 46-55) - One gating claim, or one passing claim selected for scoped normalisation. | `Candidate` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:46-55 |
| Defines the class `Applied` (lines 58-66) - One claim's source list, before and after. | `Applied` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:58-66 |
| Defines the class `Refused` (lines 69-96) - One claim `--fix` left for the curator agent, with the facts it needs. | `Refused` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:69-96 |
| Defines the class `Result` (lines 99-110) - What one run of the fixer did, everything it refused, and every staged deterministic projection. | `Result` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:99-110 |
| Defines the function `table_sites` (lines 113-123) - Every conforming table row, with the span of its Source cell. | `table_sites` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:113-123 |
| Defines the function `prose_sites` (lines 126-147) - Every `cit:` that opens and closes on ONE line, and the count of those that do not. | `prose_sites` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:126-147 |
| Defines the function `cit_bounds` (lines 150-160) - Each `cit:` opening parenthesis on the line, and its closer when there is one. | `cit_bounds` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:150-160 |
| Defines the function `prose_site` (lines 163-167). | `prose_site` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:163-167 |
| Defines the function `sites` (lines 170-173) - Every claim in one document whose source list can be rewritten in place. | `sites` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:170-173 |
| Defines the function `scope_of` (lines 176-182). | `scope_of` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:176-182 |
| Defines the function `failing` (lines 185-192) - Whether this claim carries a defect a regenerated range could clear. | `failing` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:185-192 |
| Defines the class `Walk` (lines 195-203) - Run-scoped trees, sources, documents, and result for one candidate walk. | `Walk` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:195-203 |
| Defines the function `candidates` (lines 206-241) - Every repairable or duplicate-bearing claim, plus scoped passing claims. | `candidates` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:206-241 |
| Defines the class `Staging` (lines 244-250) - One run's pending per-document edit batches, history bullets, and shared UTC stamp (CCR-R10). | `Staging` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:244-250 |
| Defines the function `fix_onboarding_root` (lines 253-329) - Regenerate every repairable range in the memory tree, stage projection bullets, bind document digests, and report the rest. | `fix_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:253-329 |
| Defines the function `_decide` (lines 332-398) - Decides one candidate and plans its deterministic projection when it is a repairing claim. | `_decide` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:332-398 |
| Defines the function `_scoped_source` (lines 401-430) - Normalise each citation, exact-deduplicate it, and preserve verified spans. | `_scoped_source` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:401-430 |
| Defines the function `_scoped_citation` (lines 433-489) - One original Source segment, generated only from anchors that segment verifies. | `_scoped_citation` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:433-489 |
| Defines the function `payload` (lines 492-537) - The complete offender list and the complete repair list, never a sample (L6-R15), plus the projection list and repair-tool version (CCR-R10). | `payload` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:492-537 |
| The deterministic projection transaction lives in its own module driven by this fixer. | `plan_projection` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:167-218 |

## Update History

- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: refreshed for the CCR-R10
  deterministic anchor-range projection change-set (code commit 709dd076). Body now reflects the
  `Staging` seam (`fix_onboarding_root`/`_decide`), `Result.projections`,
  the per-document digest binding for staged projections, and the `payload` additions
  (`projectionCount`/`projections`/`repairToolVersion`); every module-surface
  bullet and reference row re-anchored to the post-change source ranges; verification metadata
  pinned to 709dd076.

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
