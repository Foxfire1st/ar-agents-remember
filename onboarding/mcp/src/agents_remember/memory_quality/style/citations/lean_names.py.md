# mcp/src/agents_remember/memory_quality/style/citations/lean_names.py

## Governing Overview

[Overview](../../overview.md)

## Purpose

Read source-written Lean identifiers for declaration discovery and citation parsing.

## Code Commentary

`read_name` keeps the exact written name and returns the offset after its last part. It uses Lean's pinned initial and continuation character ranges. A `«…»` part keeps its inner dots together. The scanner leaves a following universe list outside the name.

## Relationships

The declaration scan uses the ending offset to continue reading the header. The card parser uses `is_lean_name` to require that the entire code span is a Lean name.

## Evidence

- `read_name` reads dotted and quoted name parts at the supplied offset. [1]
