# mcp/src/agents_remember/memory_quality/style/document_shape/tables.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Report Markdown table rows whose cell count differs from the header.

## Code Commentary

### Logic

`rows_of` computes cell-divider positions at most once per pipe-bearing unfenced line and does not call the scanner for a no-pipe line. It derives stripped cells from those same positions and stores their presence in `Row.has_divider`. `starts_table` and `read_body` consume that stored fact, preserving adjacent header/delimiter checks and termination at blanks, gaps or non-row lines without rescanning.

Direct `Row` construction derives the flag when omitted. The extra field is excluded from comparison and repr, preserving the existing row-equality surface. A delimiter row still must have the same nonempty width as its header, and cell parsing keeps the existing escaped-pipe, code-span, outer-pipe and fence rules. Ragged findings and their complete repair guidance remain unchanged.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each native symbol reference resolves its definition; no prose line-number inventory overrides that binding.

- Row stores an already observed divider fact; omitted flags are derived for direct construction without changing equality or repr. [1]


- Defines the function `check_onboarding_root`. [2]


- Defines the function `check_file`. [3]


- Row materialization scans only pipe-bearing lines once and derives cells from the same positions. [4]


- Defines the function `tables` — Every GFM table in the file, as its header row and its body rows. [5]


- Table start reads the stored divider flag while requiring adjacent same-width header and delimiter. [6]

- Table body termination consumes the stored divider flag without rescanning. [7]


- Defines the function `ragged_findings`. [8]


- Defines the function `ragged_message` — Return the complete repair for a short or long table row. [9]
