# mcp/src/agents_remember/memory_quality/style/citations/lean_tokens.py

## Governing Overview

[Overview](../../overview.md)

## Purpose

Classify the tokens that can affect Lean section and end labels.

## Code Commentary

The scanner uses a pinned inventory for built-in and Init tokens. A known token takes precedence over an unescaped identifier. File-declared atoms are possible tokens throughout the file. The declaration scan also allows competing readings for unclassified tokens when imports fall outside the inventory.

## Relationships

Syntax bodies can extend the `prec` and `stx` grammar. Atom collection keeps candidate literals when the source alone cannot establish a boundary. It can include a subsequent command's string operands, leaving a named declaration's key unverifiable. Cite the declaration by line range when this occurs.

## Evidence

- `ScopeTokens.read_label` classifies the optional label for the scope reader. [1]
