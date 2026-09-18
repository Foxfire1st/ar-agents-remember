# mcp/src/agents_remember/worktrees/integration/integration_ref_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_ref_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Read exact protected-ref observations and classify them against accepted and intended integration states.

## Code Commentary

### Logic

`classify_integration_authority_refs` reads code and optional external-memory source refs from their recorded repositories. Before-state comes from accepted source commits; intended state comes from `codeCommit` and `memoryContentCommit`. Exact before-state is `unchanged`. A combination in which every observed ref is either its accepted old value or its intended new value is `intended`, including a torn pair. An unexpected object or unreadable/missing ref is `conflict`.

The public payload distinguishes mechanically recoverable publication interruption from a developer decision. `_read_ref` preserves repository-unreadable, ref-missing, and ref-unreadable categories. Observation itself performs no mutation.

### Conventions

Public payloads report before, intended, and observed facts rather than inferring success from a contract status. The memory intent is the actual accepted memory output, never a ledger commit.

### Invariants And Boundaries

- Observed refs are evidence, not publication capability.
- Missing/unreadable refs never fall back to expected or cached values.
- A conflicting ref state is not presented as a mechanically recoverable interruption.
- The code/memory pair uses the same two-output model as integration publication.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| Observed objects and public conflict/interruption payloads. | `observed_objects` | mcp/src/agents_remember/worktrees/integration/integration_ref_state.py:156-156 |
| The total live classifier reads the actual memory output to decide accepted versus intended state. | `classify_integration_authority_refs` | mcp/src/agents_remember/worktrees/integration/integration_ref_state.py:127-168 |
| Canonical ref reading preserves stable failure categories. | `_read_ref` | mcp/src/agents_remember/worktrees/integration/integration_ref_state.py:171-205 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Changed intended memory-ref classification from retired ledgerCommit to memoryContentCommit; retained missing/unreadable and torn-pair distinctions. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
