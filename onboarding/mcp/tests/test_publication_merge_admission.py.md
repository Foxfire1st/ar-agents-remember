# mcp/tests/test_publication_merge_admission.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Pins the master chain-proof admission of a publication merge: the admission is additive, it admits the publication merge and only that merge, and everything else still falls through to the refusal the rule would otherwise give.

## Code Commentary

A helper builds an admitted shape from a workflow, parent set and merge tree, and the suites then work the rule from both directions: the publication merge is admitted, and a merge that is not the publication merge keeps its refusal. A further suite exercises the rule on real Git objects rather than modeled input, and the last pins the refusal text a caller sees today, so a change in wording is visible rather than silent.

## Invariants And Boundaries

The suite proves the admission rule and its refusals over constructed and real objects in this repository's test fixtures. It does not run a publication, contact a remote, or prove that a live run honoured the chain proof.

## Evidence

### Repo-Internal References



- The helper builds the admitted shape the rule is tested against. [1]



- The rule admits the publication merge and keeps the refusal for any other merge. [2]



- The landing-workflow read is exercised where the admission consumes it. [3]



- The rule is exercised on real Git objects, not only modeled input. [4]



- The refusal text a caller sees today is pinned. [5]
