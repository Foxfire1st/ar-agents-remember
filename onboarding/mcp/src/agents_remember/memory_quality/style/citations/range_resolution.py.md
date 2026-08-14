# mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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
- `absent_findings` (function, lines 334-356) — The anchors no range held, each naming EVERY location in the tree that does hold it.
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
| Defines the function `vanished_finding` (lines 359-378) — A source into THIS repository at a path that no longer exists.. | `vanished_finding` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:359-378 |
| Defines the function `claim_findings` (lines 381-404). | `claim_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:381-404 |
| Defines the function `prose_findings` (lines 407-440) — The prose serialisation: ``cit:`` constructs, and the spelling that preceded them.. | `prose_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:407-440 |
| Defines the function `misplaced_findings` (lines 443-461) — The prose form written into a table cell -- the wrong serialisation, not a defect-free row.. | `misplaced_findings` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:443-461 |
| Defines the function `check_document` (lines 464-481). | `check_document` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:464-481 |
| Defines the function `overshoot` (lines 484-487) — How far past the end of the file a bounds finding reaches -- for worst-first order.. | `overshoot` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:484-487 |
| Defines the function `worst_first` (lines 490-496) — The complete offender list, deepest overrun first (L6-R15).. | `worst_first` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:490-496 |
| Defines the function `check_onboarding_root` (lines 499-532) — Every citation in the memory tree, resolved against both repositories.. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:499-532 |
| Defines the function `_check_documents` (lines 535-568) — Check the selected documents against one already-validated source generation.. | `_check_documents` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:535-568 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
