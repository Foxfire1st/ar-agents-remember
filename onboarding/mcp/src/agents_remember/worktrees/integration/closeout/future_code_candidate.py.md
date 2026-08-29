# mcp/src/agents_remember/worktrees/integration/closeout/future_code_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/future_code_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T05:17+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns the exact pre-commit route identity for an ordinary future-code candidate. It binds the
contract-recorded code base and a stable observed HEAD to the canonical isolated-index full
add-all tree without staging the user's real index.

## Code Commentary

### Logic

`FutureCodeCandidateIdentity` is a frozen strict three-field model: observed HEAD, configured
base, and candidate tree. `capture_future_code_candidate` refuses non-leaf use, observes HEAD
around the existing `worktree_candidate_tree` computation, and translates expected
Git/filesystem/model failures into the central typed future-candidate error.
`require_current_future_code_candidate` recomputes
the complete route identity and rejects any bound-field drift.

### Conventions

The model uses the canonical public camel-case field names required by the future-code acceptance
variant. Every observation receives a distinct enclosure-local temporary directory and index; the
directory and index are removed when that observation exits.

### Invariants And Boundaries

- This module wraps, but does not duplicate, the canonical add-all tree algorithm.
- Concurrent observations cannot unlink or reuse each other's temporary index.
- Callers cannot supply the authoritative tree during capture.
- Captured identity cells are immutable.
- A direct-existing/series route is not a compatibility case and is explicitly refused.
- The identity is semantic-acceptance input. It does not weaken the lifecycle journal's separate
  HEAD/mutation reconciliation.
- Expected derivation failures are typed; no official-checkout or repository-id fallback exists.

### Todos

The issued acceptance schema and its persistence owner consume this model in the later
memory-candidate acceptance boundary.

## Docs References

No Domain Documentation source is configured for this memory root. The behavior is entirely
defined by repository-owned Git and worktree contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is needed for this repository-local identity owner. | — | — |

## Repo-Internal References

The strict model, capture sequence, and currentness check are intentionally colocated; the
low-level Git algorithm remains separately owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| The frozen strict route model prohibits mutation and undeclared identity fields. | `FutureCodeCandidateIdentity` | mcp/src/agents_remember/worktrees/integration/closeout/future_code_candidate.py:15-22 |
| Capture observes HEAD around the one canonical isolated-index add-all tree calculation. | `capture_future_code_candidate` | mcp/src/agents_remember/worktrees/integration/closeout/future_code_candidate.py:25-52 |
| Reuse requires exact equality of the complete bound route identity. | `require_current_future_code_candidate` | mcp/src/agents_remember/worktrees/integration/closeout/future_code_candidate.py:55-68 |
| Each capture gives the canonical helper its own enclosure-local temporary index. | `_candidate_tree` | mcp/src/agents_remember/worktrees/integration/closeout/future_code_candidate.py:71-78 |
| Capture and stale-input outcomes use the package's central typed error family. | `FutureCodeCandidateError` | mcp/src/agents_remember/errors.py:94-99 |
| The underlying helper seeds a temporary index from HEAD, applies `git add -A`, writes the tree, and removes the index. | `worktree_candidate_tree` | mcp/src/agents_remember/worktrees/modules/git.py:32-56 |

## Cross-Repo References

No meaningful cross-repository boundary applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| This owner acts only inside the contract-resolved code worktree. | — | — |

## Update History

- 2026-08-29T10:40+02:00 — Moved the owner into the closeout integration package after the
  structural gate showed that another root-level worktrees module exceeded the package cap; no
  identity semantics changed.

- 2026-08-29T05:17+02:00 — A003 self-review repair: made the bound identity immutable and gave
  concurrent observations distinct automatically cleaned temporary indexes.

- 2026-08-29T04:55+02:00 — Citation maintenance: normalized all evidence tables to the
  canonical finding/anchor/source contract after the first full memory-quality pass.

- 2026-08-29T04:55+02:00 — Created for the strict future-code candidate identity and canonical
  isolated-index reuse boundary. Verification metadata remains empty until closeout creates the
  real code commit.
