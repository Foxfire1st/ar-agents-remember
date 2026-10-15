# mcp/src/agents_remember/models/knowledge_files/history_items.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Checks newly authored history worklist IDs without normalizing their tokens.

## Code Commentary

invalid_history_items yields each original item that fails a full match of sha256: followed by exactly64hexadecimal characters. Hex letters may be upper or lower case; surrounding whitespace and partial matches remain invalid.

## Invariants And Boundaries

This is the new-input token boundary, not a parser that rewrites or invalidates stored historical labels. Yielding invalid tokens preserves their exact evidence.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- Checks newly authored history worklist IDs without normalizing their tokens. This is the new-input token boundary, not a parser that rewrites or invalidates stored historical labels. Yielding invalid tokens preserves their exact evidence. [1]
