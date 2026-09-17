# mcp/src/agents_remember/worktrees/integration/integration_ref_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_ref_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
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
| Observed objects and public conflict/interruption payloads. | n/a | [mcp/src/agents_remember/worktrees/integration/integration_ref_state.py](mcp/src/agents_remember/worktrees/integration/integration_ref_state.py) |
| Exact accepted/intended state classification uses the actual memory output. | n/a | [mcp/src/agents_remember/worktrees/integration/integration_ref_state.py](mcp/src/agents_remember/worktrees/integration/integration_ref_state.py) |
| Canonical ref reading preserves stable failure categories. | n/a | [mcp/src/agents_remember/worktrees/integration/integration_ref_state.py](mcp/src/agents_remember/worktrees/integration/integration_ref_state.py) |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Changed intended memory-ref classification from retired ledgerCommit to memoryContentCommit; retained missing/unreadable and torn-pair distinctions. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
