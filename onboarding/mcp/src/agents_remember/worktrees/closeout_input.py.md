# mcp/src/agents_remember/worktrees/closeout_input.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_input.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

Owns the single route- and contract-aware closeout-input normalizer. It captures candidate provenance, derives enabled versus not-applicable legs, validates explicit messages, and returns the only `EffectiveCloseoutInput` value permitted below the public boundary.

## Code Commentary

### Logic

`resolve_closeout_plan` derives leg state from route, the already-validated contract model, memory mode, and the captured code candidate rather than from blank sentinels or memory dirtiness. Direct landing has verified-existing code, so code is not applicable; external memory and ledger are enabled. Worktree leaf code is enabled only when the stable candidate tree differs from HEAD, and external-memory leaves enable memory and ledger. Series and non-external legs receive typed reasons. Unsupported contract kinds are rejected at the model boundary; this owner does not duplicate that impossible-state guard.

`normalize_closeout_input` strips enabled messages once, reports omitted/empty/whitespace or stale/forged values as `CloseoutInputError`, and includes `invalidFields`, `resolvedPlan`, and `correctedCall`. The candidate snapshot is rechecked so a tree or HEAD change during normalization refuses. `require_effective_closeout_plan` validates durable retries against the accepted plan rather than re-deriving it after partial mutation.

### Invariants And Boundaries

- Preview, fingerprint, journal, worker, recovery, and commit code consume the same effective input.
- Validation happens before integration-authority observation, lifecycle journal creation, worker launch, landing lock, mutation intent, or Git.
- Enabledness is contract/candidate truth, not current memory worktree dirtiness.
- A failed request has no queue, authority, journal, or Git effect.
- This module does not select or invalidate closeout-queue candidates.

### Todos

Revision and public recovery controls are deferred to L2.

## Docs References

See task `260821-CLIVE-L1` L1-R1, L1-R2, L1-R3, and L1-R5.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate identity is captured before normalization. | `capture_closeout_candidate` | `mcp/src/agents_remember/worktrees/closeout_input.py:197-211` |
| One function derives all enabled/not-applicable legs from validated contract and candidate facts. | `resolve_closeout_plan` | `mcp/src/agents_remember/worktrees/closeout_input.py:78-117` |
| Typed refusal and corrected-call data are emitted together. | `normalize_closeout_input`, `CloseoutInputError` | `mcp/src/agents_remember/worktrees/closeout_input.py:48-75`; `mcp/src/agents_remember/worktrees/closeout_input.py:120-174` |
| Retried durable input is checked against its accepted plan. | `require_effective_closeout_plan` | `mcp/src/agents_remember/worktrees/closeout_input.py:177-194` |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout input-model package relocation to `models.closeout.input`; normalization, leg planning, and retry validation behavior are unchanged.
- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata remains blank until closeout.
