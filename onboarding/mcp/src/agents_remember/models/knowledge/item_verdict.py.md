# mcp/src/agents_remember/models/knowledge/item_verdict.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Carries the gate-owned answer for one worklist item without introducing a reviewer-specific satisfaction rule.

## Code Commentary

`ItemVerdict` has the closed state vocabulary `answered`, `open`, `undecided`. `witness` names the answering row or the words `counted change`; `row_id` can identify a stale row even when the item is open; `reason` is bounded prose. All three supporting fields are optional at the schema level. The model does not validate that each state has its semantically required witness/reason: the gate producer supplies those facts.

The review adapter returns no item states for a worklist whose recorded pairing does not match the comparison; a matching incomplete worklist yields `undecided` reasons. A matching complete worklist delegates to public `item_verdicts`, reusing this computation’s classification when admitted.

## Invariants And Boundaries

An answered item is not a review approval, and a displayed state cannot satisfy or waive work. No I/O or decision policy lives in this model; optional DTO fields alone do not guarantee visible wording.

## Evidence

- The value declares three states and optional witness/row/reason fields, with no state-specific model validator. [1]
- The public gate function owns per-item verdicts and produces undecided answers on unreadable candidate input. [2]
- The review adapter gates verdicts on comparison binding and complete computation, then delegates to the gate. [3]
