# mcp/src/agents_remember/worktrees/closeout_input.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_input.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T04:55+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Owns the single route- and contract-aware closeout-input normalizer. It captures candidate provenance, derives enabled versus not-applicable legs, validates explicit messages, and returns the only `EffectiveCloseoutInput` value permitted below the public boundary.

## Code Commentary

### Logic

`resolve_closeout_plan` derives leg state from route, the already-validated contract model, memory mode, and the captured code candidate rather than from blank sentinels or memory dirtiness. Direct landing has verified-existing code, so code is not applicable; external memory and ledger are enabled. Worktree leaf code is enabled only when the stable candidate tree differs from HEAD, and external-memory leaves enable memory and ledger. Series and non-external legs receive typed reasons. Unsupported contract kinds are rejected at the model boundary; this owner does not duplicate that impossible-state guard.

`normalize_closeout_input` strips enabled messages once, reports omitted/empty/whitespace or stale/forged values as `CloseoutInputError`, and includes `invalidFields`, `resolvedPlan`, and `correctedCall`. The candidate snapshot is rechecked so a tree or HEAD change during normalization refuses. `require_effective_closeout_plan` validates durable retries against the accepted plan rather than re-deriving it after partial mutation.

`capture_closeout_candidate` delegates ordinary-leaf observation to the strict future-code
identity owner. That owner records the observed HEAD and configured base around the canonical
isolated-index add-all tree computation. Series closeout remains branch-addressed and continues
through its existing committed-tree route.

### Invariants And Boundaries

- Preview, fingerprint, journal, worker, recovery, and commit code consume the same effective input.
- Validation happens before integration-authority observation, lifecycle journal creation, worker launch, landing lock, mutation intent, or Git.
- Enabledness is contract/candidate truth, not current memory worktree dirtiness.
- A failed request has no queue, authority, journal, or Git effect.
- This module does not select or invalidate closeout-queue candidates.
- Candidate acceptance and lifecycle-operation identity are distinct: this adapter supplies exact
  Git facts, while the lifecycle journal continues to guard unproven HEAD movement.

### Todos

Revision and public recovery controls are deferred to L2.

## Docs References

No Domain Documentation source is configured for this memory root, and no external domain
contract is needed for this repository-owned adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source governs the repository-local closeout input boundary. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Leaf candidate capture consumes the strict plane-derived future-code identity, while series capture remains branch-addressed. | `capture_closeout_candidate` | mcp/src/agents_remember/worktrees/closeout_input.py:198-212 |
| Enabled/not-applicable legs derive from validated route, contract, and candidate facts. | `resolve_closeout_plan` | mcp/src/agents_remember/worktrees/closeout_input.py:79-118 |
| Typed refusal and corrected-call data are emitted together. | `CloseoutInputError`; `normalize_closeout_input` | mcp/src/agents_remember/worktrees/closeout_input.py:49-76; mcp/src/agents_remember/worktrees/closeout_input.py:121-175 |
| Retried durable input is checked against its accepted plan. | `require_effective_closeout_plan` | mcp/src/agents_remember/worktrees/closeout_input.py:178-195 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file has no external repository boundary. | — | — |

## Update History

- 2026-08-29T04:55+02:00 — MCAR-L02 citation maintenance: normalized all evidence tables to
  canonical finding/anchor/source cells after the full memory-quality check rejected the obsolete
  link-and-line format.

- 2026-08-29T04:55+02:00 — Routed ordinary-leaf capture through the strict future-code identity
  owner, documented the acceptance-versus-operation-identity boundary, repaired the governing
  overview link, and refreshed exact source citations. Verification metadata remains pinned until
  closeout stamps the real commit.
- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout input-model package relocation to `models.closeout.input`; normalization, leg planning, and retry validation behavior are unchanged.
- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata remains blank until closeout.
