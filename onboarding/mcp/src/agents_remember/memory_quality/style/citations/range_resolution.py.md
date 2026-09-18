# mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Validate anchored citations in memory tables and prose.

## Code Commentary

### Logic

Module-level surface:

- `Sources` (class, lines 65-91) — Line-cached reads of the code and memory files a run touches.
- `Tally` (class, lines 95-107) — What the run measured, beside the findings -- see modes 2, 5 and the ceiling.
- `Run` (class, lines 111-123) — Everything one document sweep carries, including its immutable source index.
- `Resolved` (class, lines 127-131) — One citation and the file it named.
- `ClaimScope` (class, lines 135-147) — One row, what it resolved to, and how to read those files.
- `containing_identifiers` (function, lines 150-154) — Longer identifiers in ``body`` that carry ``symbol`` -- mode 1's evidence.
- `elsewhere_in_file` (function, lines 157-161) — Every line of the file holding the anchor, capped -- the fix, usually.
- `anchor_evidence` (function, lines 164-182) — Where the anchor actually is, or what the range holds instead.
- `finding` (function, lines 185-193)
- `table_format_finding` (function, lines 196-215) — A table still in the superseded shape -- the whole migration, named in one message.
- `malformed_findings` (function, lines 218-228)
- `pairing_findings` (function, lines 231-265) — A claim holding one half of a citation. Neither half means anything alone.
- `repeated_sources` (function, lines 268-273) — Exact repeated source texts within this Claim, in first-seen order.
- `duplicate_source_findings` (function, lines 276-288) — Exact repeated sources within this Claim; separate Claims remain independent.
- `out_of_bounds` (function, lines 291-293) — Every citation of this claim whose range runs past the end of its own file.
- `unsatisfied` (function, lines 296-314) — Every anchor of this claim that no resolved range holds.
- `bounds_findings` (function, lines 317-331) — A range past the end of the file its own citation names.
- `moved_extent` (function, lines 334-355) — The ONE construct a cited file still holds under this
  anchor, when the range only moved: a pure move is the anchor resolving exactly once in a cited file,
  outside every cited range, so the file kept the thing and the pointer went stale. Resolving nowhere
  (gone or renamed) or more than once (ambiguous) returns ``None`` and stays enforced.
- `absent_findings` (function, lines 357-408) — The anchors no range held. A row `moved_extent` can
  place is REPORTED as a stale range never billed as curator work: same code,
  `severity="warning"`, `reportOnly=True`, a message naming the lines the anchor now occupies, riding
  `reportOnlyFindings` so it is counted and rendered without entering `findingCount` or the
  curator-actionable arithmetic. Every other absent anchor keeps the enforced finding that names
  EVERY location in the tree holding it.
- `vanished_finding` (function, lines 359-378) — A source into THIS repository at a path that no longer exists.
- `claim_findings` (function, lines 381-404)
- `prose_findings` (function, lines 407-440) — The prose serialisation: ``cit:`` constructs, and the spelling that preceded them.
- `misplaced_findings` (function, lines 443-461) — The prose form written into a table cell -- the wrong serialisation, not a defect-free row.
- `check_document` (function, lines 464-481)
- `overshoot` (function, lines 484-487) — How far past the end of the file a bounds finding reaches -- for worst-first order.
- `worst_first` (function, lines 490-496) — The complete offender list, deepest overrun first (L6-R15).
- `check_onboarding_root` (function, lines 499-532) — Every citation in the memory tree, resolved against both repositories.
- `_check_documents` (function, lines 535-568) — Check the selected documents against one already-validated source generation.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- **A pure move is reported, never billed as curator work.** An absent anchor that still resolves
  exactly once in a cited file is a stale range: it is published `reportOnly=True` with severity
  `warning`, so it is counted, rendered and reviewed without entering `findingCount` or the
  curator-actionable arithmetic. The classification cannot swallow the class it separates — an
  anchor resolving nowhere or more than once keeps the enforced finding exactly as before.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `Sources` (lines 65-91) — Line-cached reads of the code and memory files a run touches.. | `Sources` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:65-91 |
| Defines the class `Tally` (lines 95-107) — What the run measured, beside the findings -- see modes 2, 5 and the ceiling.. | `Tally` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:95-107 |
| Defines the class `Run` (lines 111-123) — Everything one document sweep carries, including its immutable source index.. | `Run` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:111-123 |
| Defines the class `Resolved` (lines 127-131) — One citation and the file it named.. | `Resolved` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:127-131 |
| Defines the class `ClaimScope` (lines 135-147) — One row, what it resolved to, and how to read those files.. | `ClaimScope` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:135-147 |
| Defines the function `containing_identifiers` (lines 150-154) — Longer identifiers in ``body`` that carry ``symbol`` -- mode 1's evidence.. | `containing_identifiers` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:150-154 |
| Defines the function `elsewhere_in_file` (lines 157-161) — Every line of the file holding the anchor, capped -- the fix, usually.. | `elsewhere_in_file` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:157-161 |
| Defines the function `anchor_evidence` (lines 164-182) — Where the anchor actually is, or what the range holds instead.. | `anchor_evidence` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:164-182 |
| Defines the function `finding` (lines 185-193). | `finding` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:185-193 |
| Defines the function `table_format_finding` (lines 196-215) — A table still in the superseded shape -- the whole migration, named in one message.. | `table_format_finding` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:196-215 |
| Defines the function `malformed_findings` (lines 218-228). | `malformed_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:218-228 |
| Defines the function `pairing_findings` (lines 231-265) — A claim holding one half of a citation. Neither half means anything alone.. | `pairing_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:231-265 |
| Defines the function `repeated_sources` (lines 268-273) — Exact repeated source texts within this Claim, in first-seen order.. | `repeated_sources` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:268-273 |
| Defines the function `duplicate_source_findings` (lines 276-288) — Exact repeated sources within this Claim; separate Claims remain independent.. | `duplicate_source_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:276-288 |
| Defines the function `out_of_bounds` (lines 291-293) — Every citation of this claim whose range runs past the end of its own file.. | `out_of_bounds` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:291-293 |
| Defines the function `unsatisfied` (lines 296-314) — Every anchor of this claim that no resolved range holds.. | `unsatisfied` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:296-314 |
| Defines the function `bounds_findings` (lines 317-331) — A range past the end of the file its own citation names.. | `bounds_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:317-331 |
| Defines the function `absent_findings` (lines 334-356) — The anchors no range held, each naming EVERY location in the tree that does hold it.. | `absent_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:334-356 |
| Defines the function `vanished_finding` (lines 359-378) — A source into THIS repository at a path that no longer exists.. | `vanished_finding` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:409-428 |
| Defines the function `claim_findings` (lines 381-404). | `claim_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:431-454 |
| Defines the function `prose_findings` (lines 407-440) — The prose serialisation: ``cit:`` constructs, and the spelling that preceded them.. | `prose_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:457-490 |
| Defines the function `misplaced_findings` (lines 443-461) — The prose form written into a table cell -- the wrong serialisation, not a defect-free row.. | `misplaced_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:493-511 |
| Defines the function `check_document` (lines 464-481). | `check_document` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:514-531 |
| Defines the function `overshoot` (lines 484-487) — How far past the end of the file a bounds finding reaches -- for worst-first order.. | `overshoot` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:534-537 |
| Defines the function `worst_first` (lines 490-496) — The complete offender list, deepest overrun first (L6-R15).. | `worst_first` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:540-546 |
| Defines the function `check_onboarding_root` (lines 499-532) — Every citation in the memory tree, resolved against both repositories.. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:549-582 |
| Defines the function `_check_documents` (lines 535-568) — Check the selected documents against one already-validated source generation.. | `_check_documents` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:585-618 |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: `vanished_finding` repointed to mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:409-428. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `claim_findings` repointed to mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:431-454. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `prose_findings` repointed to mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:457-490. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `misplaced_findings` repointed to mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:493-511. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `check_document` repointed to mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:514-531. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `overshoot` repointed to mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:534-537. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `worst_first` repointed to mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:540-546. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `check_onboarding_root` repointed to mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:549-582. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_check_documents` repointed to mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:585-618. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T19:21+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded the pure-move classification this change adds, which the card did not carry. `absent_findings` no longer bills every absent anchor alike: a new `moved_extent` decides the row structurally — the anchor still resolving EXACTLY ONCE in a cited file, outside every cited range, is a stale range caused by somebody's inserted registration, and it is published `reportOnly=True` at `warning` (same `citation_anchor_absent_from_range` code, a message saying the range is STALE BY A MOVE and naming the lines the anchor now occupies) so it is counted and reviewed without entering `findingCount` or the curator-actionable arithmetic. Resolving nowhere or more than once stays enforced, which is why the classification cannot swallow the class it separates. Documentation only: no source byte was touched by this pass. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are NOT advanced — these sources are uncommitted, so no commit carries their bytes; the candidate is named in the `reviewedWorkingCandidate` metadata row and the governed closeout owns the real commits.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
