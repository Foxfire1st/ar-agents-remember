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

- **The owner reference's exact three components, and the fourth addressing scheme refused without a denylist.** [20]
- The admitted version spelling, over seven inputs the task plane would also refuse. [21]
- **The reference the payload deliberately does not police: four paths the owner would refuse are still representable, so the answer cannot be the substrate's.** [22]
- **The real owner's four refusals carried verbatim, with the stored reference byte-identical — the proof that the reference is never rewritten.** [23]
- The resolved owner recorded as resolved, with no refusal fields. [24]
- **The real resolver these cases drive, rather than a stub — a stubbed resolver cannot catch the second resolver this suite exists to exclude.** [25]
- The lane row that gives this module its classification and keeps it collectable under a named lane. [26]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Cross-Repo References

No cross-repository contract is established by this file.
