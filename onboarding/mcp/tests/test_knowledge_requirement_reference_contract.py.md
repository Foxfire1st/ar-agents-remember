# mcp/tests/test_knowledge_requirement_reference_contract.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

Requirement endpoints reference the task plane; its owner alone resolves packet authority.

## Code Commentary

### Logic

The reference carries exactly path, stableId and version with the task-plane spelling. A path the owner would refuse stays representable, so the reference model is not a second resolver. [1] [2] [3]

Cases call real consume_owner_resolution over real packet files. Missing, outside-task/non-Markdown and mismatched packets carry the owner's exact refusal; a resolved owner has no refusal fields. The database record group and derived views were retired; current tests protect references used by text-format endpoints. [9] [10] [19]

### Invariants And Boundaries

- Reference never replaces task authority.
- The owner's resolution is carried verbatim.

## Evidence

### Repo-Internal References


- Exact owner reference components. [1]


- Admitted version spelling. [2]


- Reference does not police owner paths. [3]


- Real owner refusal carried verbatim. [9]


- Resolved owner state. [10]


- The task-owner consumption seam. [19]


### Cross-Repo References

No cross-repository contract is established by this file.
