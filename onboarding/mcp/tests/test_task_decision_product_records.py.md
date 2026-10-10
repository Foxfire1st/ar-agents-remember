# mcp/tests/test_task_decision_product_records.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Server tests for the rule-6 product-record marking: writer constants are marked as product-written records while authored text is not, and a finalizer entry keeps its stored shape while being marked.

## Code Commentary

Two cases pin `is_product_record_decision`: the writers' own exact strings and prefixes mark records, the named authored decisions (including near-misses like the unpunctuated finalize sentence) do not match, and the finalizer's prepended newest record is marked without changing its stored shape. The page matches no text; the marking lives in the document projection. No test proves arbitrary authored text cannot collide (exact/prefix string match only).

## Evidence

- Writer constants are marked and the named authored decisions are not. [1]
- A finalizer entry keeps its shape and is marked. [2]
