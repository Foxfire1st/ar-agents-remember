# mcp/src/agents_remember/models/lifecycles/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Defines the immutable accepted input for a direct-landing operation. It carries code and memory
facts required by the execution and recovery owners, without ledger cache state.

## Code Commentary

### Logic

`DirectLandingOperationInput` is a strict Pydantic model with `extra="forbid"`. It carries the
configuration and contract paths, effective direct input, approval note, gate-policy snapshot,
exact code commit/tree and candidate tree, memory repository/branch/ref, and `memoryBefore` snapshot.
Hash and ref fields have declared shape constraints. The validator requires the direct-landing
route and a nonblank accepted approval note.

The model does not read Git, verify repository existence, or decide whether a live branch matches
those facts; the coordinator and recovery classifier perform that work. `ledgerPath`,
`ledgerBeforeText`, `ledgerBeforeSha256`, and `DirectLandingLedgerIntent` are retired.

### Conventions

One strict model owns this input vocabulary. Consumers pass typed facts instead of reconstructing
accepted state from queue rows, task prose, or cache files.

### Invariants And Boundaries

- Model validation establishes shape and required intent, not a proof of live publication.
- No cache path, table, byte digest, or ledger mutation intent belongs to the accepted input.
- I/O, lifecycle scheduling, and output publication remain outside this model module.

### Todos

No new file-local follow-up is established by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

| Finding | Anchor | Source |
| --- | --- | --- |
| The strict model carries code/memory identity and its `_accepted_direct_plan_is_exact` validator requires the direct-landing route plus a nonblank approval note. | `_accepted_direct_plan_is_exact` | mcp/src/agents_remember/models/lifecycles/direct_landing.py:34-39 |
| The shared snapshot's `_require_state_evidence` validator keeps actual object identity: `observed is not before` is refused while `observed == before` is reconciled. | `_require_state_evidence` | mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:47-63 |
| The coordinator captures the accepted candidate from actual Git facts. | `candidateTree` | mcp/src/agents_remember/worktrees/direct_landing.py:443-444 |
| Recovery checks the typed facts against the current repositories and refs. | `classify_direct_landing_recovery` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:77-134 |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:51 UTC — Removed the ledger byte/path/digest fields and DirectLandingLedgerIntent from the documented vocabulary; retained strict code/memory shapes and clarified the boundary between model validation and actual Git proof. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.


- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-input model package relocation; direct-landing accepted-input and ledger-intent contracts are unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.

