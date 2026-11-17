# mcp/tests/test_instruction_manifest_renewal.py

## Governing Overview

[Overview](overview.md)

## Purpose

Checks renewal and reader composition of generated reference steps and audiences.

## Code Commentary

The cases distinguish authored no-step decisions from missing generated steps, derive reference audiences from pointer topology and authored role reasons, and check corrective diagnostics for unresolved references. A checkout-level case checks that the digest-map routing reason names the declared roles and embeds no derived line numbers. Ordinary no-step cases ignore stale stored derived state. Public command cases check read-only detection, renewal and a subsequent clean check in fixture copies.

## Relationships

The renewal manifest planner produces metadata and the model helper composes it for readers. Assertions preserve authored null decisions rather than introducing a generated substitute.

## Evidence

### Repo-Internal References (renewed)

- Cases separate derivable steps, authored role reasons and no-step decisions, including stale stored derived state. [1]
- Public command cases exercise authored reference changes, no-write checking, renewal and a subsequent clean check. [2]
