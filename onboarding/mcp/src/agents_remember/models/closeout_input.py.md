# mcp/src/agents_remember/models/closeout_input.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/closeout_input.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash |  `eb7ea60ab9919f009fef58f81afe5861aa1709da`|
| lastVerifiedCommitDate |  2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

Defines the public and durable closeout-input vocabulary shared by worktree closeout and direct landing: three typed legs (`code`, `memory`, `ledger`), each either enabled with a stripped nonblank explicit message or not applicable with a reason. It also defines field-specific refusal observations, the resolved plan, and the corrected-call shape returned to callers.

## Code Commentary

### Logic

`CloseoutMessageInput` is the raw public shape; it preserves omission, empty text, whitespace, and supplied values so the boundary can explain why a request is invalid. `ResolvedCloseoutPlan` states which legs the route and contract require. `EffectiveCloseoutInput` is the discriminated, normalized value that may cross below validation. `EnabledCloseoutLeg` rejects blank messages and stores only stripped text; `NotApplicableCloseoutLeg` carries no message and names why the leg does not apply.

### Conventions

The model does not decide enabledness. Route- and contract-aware code in `worktrees/closeout_input.py` derives the plan, then constructs this type. Consumers call `message_for` only for enabled legs and `enabled` when rendering intent.

### Invariants And Boundaries

- An enabled leg always has explicit stripped nonblank intent; a not-applicable leg never carries a sentinel empty message.
- There is no generated subject, default commit message, or compatibility input alongside this model.
- `CloseoutInvalidField`, `CloseoutCorrectedCall`, and `ResolvedCloseoutPlan` make refusal actionable without acquiring integration authority or touching Git.
- Queue selection has no dependency on this type; it remains a scheduling projection outside L1.

### Todos

None recorded. Public retry/recover/revise controls belong to L2, not this model.

## Docs References

See task `260821-CLIVE-L1`, especially L1-R1 through L1-R3 and L1-R5.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Raw observations and typed refusal vocabulary are public data. | `CloseoutMessageInput`, `CloseoutInvalidField` | mcp/src/agents_remember/models/closeout_input.py:25-33; mcp/src/agents_remember/models/closeout_input.py:57-66 |
| Effective legs are a discriminated union. | `EnabledCloseoutLeg`, `NotApplicableCloseoutLeg` | mcp/src/agents_remember/models/closeout_input.py:77-101 |
| Only enabled legs can return a commit message. | `message_for` | mcp/src/agents_remember/models/closeout_input.py:108-127 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; verification metadata remains blank until governed closeout stamps the landed code commit.
