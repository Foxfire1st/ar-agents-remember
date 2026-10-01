# mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py

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

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Sources` (lines 65-91) — Line-cached reads of the code and memory files a run touches.. [1]
- Defines the class `Tally` (lines 95-107) — What the run measured, beside the findings -- see modes 2, 5 and the ceiling.. [2]
- Defines the class `Run` (lines 111-123) — Everything one document sweep carries, including its immutable source index.. [3]
- Defines the class `Resolved` (lines 127-131) — One citation and the file it named.. [4]
- Defines the class `ClaimScope` (lines 135-147) — One row, what it resolved to, and how to read those files.. [5]
- Defines the function `containing_identifiers` (lines 150-154) — Longer identifiers in ``body`` that carry ``symbol`` -- mode 1's evidence.. [6]
- Defines the function `elsewhere_in_file` (lines 157-161) — Every line of the file holding the anchor, capped -- the fix, usually.. [7]
- Defines the function `anchor_evidence` (lines 164-182) — Where the anchor actually is, or what the range holds instead.. [8]
- Defines the function `finding` (lines 185-193). [9]
- Defines the function `table_format_finding` (lines 196-215) — A table still in the superseded shape -- the whole migration, named in one message.. [10]
- Defines the function `malformed_findings` (lines 218-228). [11]
- Defines the function `pairing_findings` (lines 231-265) — A claim holding one half of a citation. Neither half means anything alone.. [12]
- Defines the function `repeated_sources` (lines 268-273) — Exact repeated source texts within this Claim, in first-seen order.. [13]
- Defines the function `duplicate_source_findings` (lines 276-288) — Exact repeated sources within this Claim; separate Claims remain independent.. [14]
- Defines the function `out_of_bounds` (lines 291-293) — Every citation of this claim whose range runs past the end of its own file.. [15]
- Defines the function `unsatisfied` (lines 296-314) — Every anchor of this claim that no resolved range holds.. [16]
- Defines the function `bounds_findings` (lines 317-331) — A range past the end of the file its own citation names.. [17]
- Defines the function `absent_findings` (lines 334-356) — The anchors no range held, each naming EVERY location in the tree that does hold it.. [18]
- Defines the function `vanished_finding` (lines 359-378) — A source into THIS repository at a path that no longer exists.. [19]
- Defines the function `claim_findings` (lines 381-404). [20]
- Defines the function `prose_findings` (lines 407-440) — The prose serialisation: ``cit:`` constructs, and the spelling that preceded them.. [21]
- Defines the function `misplaced_findings` (lines 443-461) — The prose form written into a table cell -- the wrong serialisation, not a defect-free row.. [22]
- Defines the function `check_document` (lines 464-481). [23]
- Defines the function `overshoot` (lines 484-487) — How far past the end of the file a bounds finding reaches -- for worst-first order.. [24]
- Defines the function `worst_first` (lines 490-496) — The complete offender list, deepest overrun first (L6-R15).. [25]
- Defines the function `check_onboarding_root` (lines 499-532) — Every citation in the memory tree, resolved against both repositories.. [26]
- Defines the function `_check_documents` (lines 535-568) — Check the selected documents against one already-validated source generation.. [27]
