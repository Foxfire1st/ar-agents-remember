# mcp/tests/test_task_sprint_linkage.py

## Governing Overview

[overview](overview.md)

## Purpose

Holds the shared temporary sprint↔master linkage fixture and canonical judgment-register helpers, plus one test of the linkage report. It writes typed master/sprint documents and snapshots their bytes for consuming structural-publication tests. The attach/render/registration inventory in its docstring is not the current executed population.

## Code Commentary

### Current Contract

SprintLinkageTests defines test_linkage_report_answers_with_counts_and_location. It asserts counts/updated/reportPath and equality of the report's facts to logged whole linkageFacts; its dry answer has no reportPath. Its deterministic 100-token content assertion excludes log with the coordination root fixed to 40 characters. Shared helpers remain; this adapter fixture is not a whole server/session proof.

`_judgment_row` authors a judgment-register row whose author defaults to `architect`, and `_register_section` builds the register section from such rows.

### Logic

The current evidence boundary is the source-listed behavior below. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The test-shaped filename is kept because other suites import its fixture and helpers. Helper availability is not a passing test.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file.

- Shared helper _judgment_register [1]

- Shared helper _judgment_row [2]

- Shared helper _register_section [3]

- A judgment-register row's author defaults to `architect`. [5]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.

- SprintLinkageTests defines test_linkage_report_answers_with_counts_and_location. It asserts counts/updated/reportPath and equality of the report's facts to logged whole linkageFacts; its dry answer has no reportPath. Its deterministic 100-token content assertion excludes log with the coordination root fixed to 40 characters. Shared helpers remain; this adapter fixture is not a whole server/session proof or a no-tests module. [4]
