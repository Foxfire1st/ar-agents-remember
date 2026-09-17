# mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py` |
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

Re-prove that a final integration output is the exact closeout pair recorded on its contract.

## Code Commentary

### Logic

`require_authorized_integration_commits` compares `(code_commit, memory_content_commit)` with the contract's two accepted closeout outputs. A mismatch refuses publication and requires a new closeout after conflict resolution. This check reads contract output facts; current source tips and ancestry belong to the separate ref-preparation boundary.

### Conventions

The retained WorktreeArgs parameter is not an alternate authority source. This module neither reads a journal to choose a candidate nor consults cache data.

### Invariants And Boundaries

- No unrecorded replay result may substitute for the accepted pair.
- There is no ledger output slot or dummy ledger identity.
- Matching output cells do not bypass the caller's ownership, source-tip, ancestry, and CAS checks.

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
| Final output authority is the contract's exact accepted pair. | n/a | [mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py](mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py) |
| Source and ref proof remain at the prepared movement boundary. | n/a | [mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py](mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py) |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Reduced exact candidate comparison to code and actual memory output; removed the retired ledger-commit member while preserving mismatch refusal. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.
- 2026-09-11T23:05:00+00:00: Repaired three claims against the current source. The card claimed a journaled operation admission (`require_plane_integration_operation`) binding the requested key to one durable authority record and a stored source-tip revalidation (`require_current_integration_sources`); both functions are deleted, the module is now the 31-line `require_authorized_integration_commits` that compares the landing output with the contract's recorded closeout commits, and the moved-source refusal lives in the pure-Git replay requirements of `prepare_integration_ref_move`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_operation_authority.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created durable integration-operation proof onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
