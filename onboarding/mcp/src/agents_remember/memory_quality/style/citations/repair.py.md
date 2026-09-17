# mcp/src/agents_remember/memory_quality/style/citations/repair.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/repair.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T01:15+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Plan exact-name tier-1 citation repairs. Generate one extent per anchor and merge only
overlapping/adjacent extents in the same file; never widen discontiguous anchors into one
enclosing range. Search cited files first, then the wider code tree only when **no cited file exists
any more**. Repoint only a unique exact-name match. Since CCR-R10 (260831-CCR-L10) every
`Repair` also carries the oracle-chosen `ResolvedLocation` per anchor - the extent the
repair actually followed - so the deterministic projection binds the exact resolution without a
second lookup or a second authority.

Since 260831-LOCR-L33 a tree-wide retarget additionally has to **prove continuity**: the anchor must
have existed in a cited file at the document's `lastVerifiedCommitHash` and must have carried the
same extent KIND there as the extent found now. An exact name matching somewhere is not the claim's
evidence having moved - a mention inside a tuple and the function that declares the same name are
different facts - and nothing here infers an origin from similarity. Missing provenance is grounds
to refuse, never a licence to guess.

Renames, deletions, typos, and ambiguity are declined because syntax cannot distinguish them
safely. Tree-wide mode plans only failing citations. Document-scoped normalization also
regenerates passing ranges through `migration._scoped` so verified mention spans are
preserved.

## Code Commentary

### Logic

The refusal vocabulary is five codes, four of them raised from `_retarget` in a fixed cheapest-first
order, each with its own remediation text in `DECLINE_REMEDIATION`:

- `ANCHOR_ABSENT` / `ANCHOR_AMBIGUOUS` (lines 39-40, 45-79) - no single tree-wide sighting exists.
- `ANCHOR_LEFT_LIVE_FILE` (line 41) - **a cited file still exists**, so the anchor leaving it is a
  stale range rather than a move; the message names every live cited file and every candidate the
  tree holds.
- `ANCHOR_CONTINUITY_UNPROVEN` (line 42) - the extent the claim was verified against cannot be
  established at its stamp; the message names the failed leg.
- `ANCHOR_KIND_CHANGED` (line 43) - the origin extent's kind differs from the tree-wide match's kind.

Module-level surface (decorator-inclusive ranges):

- `ResolvedLocation` (class, lines 81-93) - One anchor's chosen extent exactly as the shared oracle resolved it, carried on `Repair` for the deterministic projection (CCR-R10).
- `Repair` (class, lines 96-102) - The source list `--fix` would write for one claim, plus the resolved locations it followed.
- `Decline` (class, lines 104-114) - Why one claim stays for the curator, and the facts it needs to work it down; `message` appends the code's remediation.
- `Cited` (class, lines 117-122) - One of a claim's sources and the file it named, when that file still exists.
- `targets` (function, lines 125-128)
- `chosen` (function, lines 131-141) - The one extent this citation means, or `None` when the file offers a choice (a single occurrence needs no tiebreaker; otherwise the claim's own range decides).
- `Origin` (class, lines 144-156) - What the claim's anchor WAS in its cited sources at its verification stamp: a kind, a detail, and the commit/path it was read from. `kind is None` exactly when the origin could not be established.
- `Continuity` (class, lines 159-240) - One memory document's verification provenance. `commit()` resolves `lastVerifiedCommitHash` to one reachable commit; `origin()` derives the one extent the claim was verified against through the ESTABLISHED path (`claim_change_router.classify_citation` -> `Histories.code.file` or the ledger-mapped memory file -> `FileView.extents(anchor)` -> the existing `chosen` tiebreaker), never a second derivation; `_holds`/`_file` are its two legs.
- `continuity_for` (function, lines 243-253) - Reads the document's `lastVerifiedCommitHash` through `parse_table_metadata`; a missing/unreadable stamp yields the empty `Continuity`, whose origin is unproven - the refusal, never a guess.
- `_Plan` (class, lines 256-272) - One claim's repair as it accumulates: the spans found, the first refusal, and every resolved location.
- `_Placement` (class, lines 275-282) - The cited targets, sources, sightings, and continuity authority for one anchor, held for the whole claim. It exists to keep `_place`/`_retarget` under the armed `PLR0913`/`PLR0917` parameter limits.
- `plan` (function, lines 285-309) - The tiebreaker, applied to one claim; returns the sources and the full `ResolvedLocation` tuple. Its optional `continuity` argument is the document's verification provenance; `None` means the caller has no continuity authority (the scoped pass) and a relocation is then refused rather than guessed.
- `_carried` (function, lines 312-333) - The sources that survive unchanged because nothing here could regenerate them.
- `_place` (function, lines 336-353) - Where this anchor's range comes from: a cited file first, the wider tree second.
- `_retarget` (function, lines 356-387) - The wider-tree answer, admitted only after the three refusals above, cheapest first.
- `_left_a_live_file` (function, lines 390-403), `_no_single_sighting` (lines 405-412), `_continuity_unproven` (lines 414-426), `_kind_changed` (lines 428-439) - The four refusal constructors; `_named_kind` (lines 441-446) gives a kind its sentence article.
- `_ambiguous_in_file` (function, lines 448-458)
- `_written` (function, lines 460-472) - The generated source list: one range per anchor, merged per file, then what survives.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- Resolution is exact-name only; `ResolvedLocation` records the extent the repair actually
  followed (in-file tiebreaker or tree-wide `Sightings.unique`) so no second lookup or
  second authority can answer the projection differently (CCR-R10).
- **A relocation must prove continuity.** All three of these must hold before a tree-wide match is
  admitted: no cited file still exists, the tree-wide sighting is unique, and the extent the claim
  was verified against is readable at the document's stamp with the same extent KIND. A name match
  is not evidence that the claim's subject moved.
- **File deletion does not establish that the replacement evidence supports the claim.** The first
  design of this guard only refused while a cited file survived, so deleting the cited file fell
  through to the same tree-wide lookup and reproduced the identical wrong binding while reporting
  success. The lesson is the rule: "provenance-based matching fails open when provenance is
  unavailable" is an argument for *refusing*, not for a cheaper guard.
- **The origin is derived through the established path, never re-derived.** `Continuity.origin`
  consumes `classify_citation`, the provenance history reader, the existing extent layer, and the
  existing `chosen` tiebreaker; it introduces no second notion of where an anchor lives.
- **An unprovable origin refuses.** A missing `lastVerifiedCommitHash`, an unreachable commit, a
  cited file that cannot be read at the stamp, a non-unique origin across cited files, or a caller
  that passes no continuity authority at all (the scoped pass) each produce an unproven `Origin` and
  therefore `anchor_continuity_unproven`.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| The five refusal codes, including the three new continuity-refusal codes. | `ANCHOR_ABSENT`; `ANCHOR_AMBIGUOUS`; `ANCHOR_LEFT_LIVE_FILE`; `ANCHOR_CONTINUITY_UNPROVEN`; `ANCHOR_KIND_CHANGED` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:39-43 |
| Every decline code has a curator-facing remediation naming the next action. | `DECLINE_REMEDIATION` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:45-79 |
| Defines the class `ResolvedLocation` (lines 81-93) - One anchor's chosen extent exactly as the shared oracle resolved it, carried on `Repair` (CCR-R10). | `ResolvedLocation` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:81-93 |
| Defines the class `Repair` (lines 96-102) - The source list `--fix` would write for one claim, plus its resolved locations. | `Repair` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:96-102 |
| Defines the class `Decline` (lines 104-114) - Why one claim stays for the curator, and the facts it needs to work it down. | `Decline` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:104-114 |
| Defines the class `Cited` (lines 117-122) - One of a claim's sources and the file it named, when that file still exists. | `Cited` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:117-122 |
| Defines the function `targets` (lines 125-128). | `targets` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:125-128 |
| Defines the function `chosen` (lines 131-141) - The one extent this citation means, or `None` when the file offers a choice. | `chosen` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:131-141 |
| What the claim's anchor was in its cited sources at its verification stamp, or why that cannot be established. | `Origin` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:144-156 |
| The per-document verification provenance a relocation has to prove itself against, derived through the established classification/provenance/extent path. | `Continuity` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:159-240 |
| A document with no metadata table, no stamp, or an unreadable one yields the empty continuity whose origin is unproven. | `continuity_for` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:243-253 |
| Defines the class `_Plan` (lines 256-272) - One claim's repair as it accumulates: the spans found, the first refusal, and every resolved location. | `_Plan` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:256-272 |
| The per-claim placement authority bundle that keeps the placement helpers under the armed parameter limits. | `_Placement` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:275-282 |
| Defines the function `plan` (lines 285-309) - The tiebreaker, applied to one claim, now taking the document's continuity authority. | `plan` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:285-309 |
| Defines the function `_carried` (lines 312-333) - The sources that survive unchanged because nothing here could regenerate them. | `_carried` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:312-333 |
| Defines the function `_place` (lines 336-353) - Where this anchor's range comes from: a cited file first, the wider tree second. | `_place` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:336-353 |
| The wider-tree admission order: a live cited file refuses first, then no/ambiguous sighting, then unproven origin, then a kind change. | `_retarget`; `_left_a_live_file`; `_no_single_sighting`; `_continuity_unproven`; `_kind_changed`; `_named_kind` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:356-387; mcp/src/agents_remember/memory_quality/style/citations/repair.py:390-403; mcp/src/agents_remember/memory_quality/style/citations/repair.py:405-412; mcp/src/agents_remember/memory_quality/style/citations/repair.py:414-426; mcp/src/agents_remember/memory_quality/style/citations/repair.py:428-439; mcp/src/agents_remember/memory_quality/style/citations/repair.py:441-446 |
| Defines the function `_ambiguous_in_file` (lines 448-458). | `_ambiguous_in_file` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:448-458 |
| Defines the function `_written` (lines 460-472) - The generated source list: one range per anchor, merged per file, then what survives. | `_written` | mcp/src/agents_remember/memory_quality/style/citations/repair.py:460-472 |
| The origin is read through the established citation classifier, never a second derivation. | `classify_citation` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:254-274 |
| The verification-provenance owner the continuity proof reads cited evidence through. | `Histories` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:110-136 |
| The code-commit-to-memory-commit ledger mapping the memory leg resolves through. | `memory_commit` | mcp/src/agents_remember/memory_quality/style/citations/provenance.py:138-147 |
| The document metadata reader that supplies `lastVerifiedCommitHash`. | `parse_table_metadata` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/discovery.py:17-19 |
| The deterministic projection consumes the resolved locations a `Repair` carries. | `plan_projection` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:167-221 |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `memory_commit` repointed to mcp/src/agents_remember/memory_quality/style/citations/provenance.py:138-147. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: refreshed for the continuity-based relocation
  rule. Body now records the three new refusal codes (`anchor_left_live_file`,
  `anchor_continuity_unproven`, `anchor_kind_changed`), the `Origin`/`Continuity` types and
  `continuity_for`, the `continuity` argument on `plan`, the `_Placement` bundle, and `_retarget`'s
  cheapest-first admission order. Recorded *why* it matters and why the first design was wrong: an
  earlier guard only refused while a cited file survived, so **deleting** the cited file fell through
  to the same tree-wide lookup and reproduced the identical wrong binding while reporting success —
  file deletion does not establish that the replacement evidence supports the claim, and
  "provenance-based matching fails open when provenance is unavailable" is an argument for refusing,
  not for a cheaper guard. Recorded that the origin is derived through the established path
  (`classify_citation` → `Histories` → `FileView.extents` → the existing `chosen` tiebreaker), not a
  second derivation, and that an unprovable origin refuses. Every module-surface bullet and reference
  row re-anchored to the post-change source ranges.

- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: refreshed for the CCR-R10
  deterministic anchor-range projection change-set (code commit 709dd076). Body now reflects the
  new `ResolvedLocation` carrier, `Repair.locations`, the `_Plan.locations`
  accumulator, and the anchor-bearing `add` signature in `_place`/`_place_elsewhere`;
  every module-surface bullet and reference row re-anchored to the post-change source ranges;
  verification metadata pinned to 709dd076.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
