# mcp/src/agents_remember/models/closeout/input.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/closeout/input.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `1ddf7fdac40fa3e9c30b8ded693d440e07d6a8b6` |
| lastVerifiedCommitDate | 2026-09-13T22:07:53+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[models overview](../overview.md)

## Purpose

Defines the public and durable closeout-input vocabulary shared by worktree closeout and direct landing: three typed legs (`code`, `memory`, `ledger`), each either enabled with a stripped nonblank explicit message or not applicable with a reason. It also defines field-specific refusal observations, the resolved plan, and the corrected-call shape returned to callers.

It is additionally the one definition of the memory-content commit message. `EffectiveCloseoutInput.memory_content_message(code_commit)` renders this closeout's own message with exactly one final-paragraph `Code-Commit: <sha>` trailer naming the code commit the same closeout landed, so both sanctioned closeout routes attribute their memory content from a single rendering rather than two that could drift apart.

## Code Commentary

### Logic

`CloseoutMessageInput` is the raw public shape; it preserves omission, empty text, whitespace, and supplied values so the boundary can explain why a request is invalid. `ResolvedCloseoutPlan` states which legs the route and contract require. `EffectiveCloseoutInput` is the discriminated, normalized value that may cross below validation. `EnabledCloseoutLeg` rejects blank messages and stores only stripped text; `NotApplicableCloseoutLeg` carries no message and names why the leg does not apply.

`CODE_COMMIT_TRAILER_KEY` names that trailer key, and `memory_content_message(code_commit)` is where it is rendered: `f"{self.message_for('memory')}\n\n{CODE_COMMIT_TRAILER_KEY}: {code_commit}"`. The closeout's own message is used verbatim and the trailer is appended as its own final paragraph — never substituted for the body, and appended `\n\n` away from it because `git interpret-trailers` reads a trailer block only from the end of the message, which is also why a `Code-Commit:` line a caller wrote earlier in the body cannot be mistaken for this attribution. Both routes that commit memory content render through this method: `worktrees/modules/closeout_external.py::_commit_memory_content` and `worktrees/integration/direct_landing/direct_landing_execution.py::_direct_memory_commit`. The ledger leg does not: it still calls plain `message_for("ledger")` and carries no trailer, because the `memory.md`-only commit names no code commit.

### Conventions

The model does not decide enabledness. Route- and contract-aware code in `worktrees/closeout_input.py` derives the plan, then constructs this type. `message_for` stays the raw public echo of one enabled leg's message — the code leg, the ledger leg, and the public effective-input echo use it — while the memory-content leg is rendered through `memory_content_message(code_commit)`, so the attribution has one definition and cannot drift between the worktree and direct-landing routes. `enabled` is used when rendering intent.

### Invariants And Boundaries

- An enabled leg always has explicit stripped nonblank intent; a not-applicable leg never carries a sentinel empty message.
- The attribution has exactly one definition here, and the body it is appended to is the closeout's own message verbatim: `memory_content_message` never replaces the body, and it never invents an attribution for a commit that has no code counterpart to name.
- The trailer has to be inside the commit object when the object is created, because the message is hashed into it. Both callers render the message at the commit seam for that reason; `prove_git_commit` journals the resulting sha on the next statement, so anything added later could only be a rewrite of an already-proved object (`git notes` is not bound by the hash).
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
| Raw observations and typed refusal vocabulary are public data. | `CloseoutMessageInput`, `CloseoutInvalidField` | mcp/src/agents_remember/models/closeout/input.py:34-42; mcp/src/agents_remember/models/closeout/input.py:66-75 |
| Effective legs are a discriminated union. | `EnabledCloseoutLeg`, `NotApplicableCloseoutLeg` | mcp/src/agents_remember/models/closeout/input.py:86-109 |
| Only enabled legs can return a raw commit message; this stays the public echo. | `message_for` | mcp/src/agents_remember/models/closeout/input.py:129-133 |
| The attribution key is a module constant, and the memory-content body is the closeout's own message plus exactly one final-paragraph trailer naming the code commit the same closeout landed. | `CODE_COMMIT_TRAILER_KEY`; `memory_content_message` | mcp/src/agents_remember/models/closeout/input.py:9-16; mcp/src/agents_remember/models/closeout/input.py:135-150 |
| The memory-content message is rendered at the commit seams: the worktree route and the direct-landing route both call `memory_content_message`, while the ledger leg keeps `message_for("ledger")` and no trailer. | `_commit_memory_content`; `_direct_memory_commit`; `_commit_ledger_mapping` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:136-196; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:215-276; mcp/src/agents_remember/worktrees/modules/closeout_external.py:212-251 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): recorded that this model now owns the attribution as well as the messages — `CODE_COMMIT_TRAILER_KEY` plus `memory_content_message(code_commit)`, which returns the closeout's own message verbatim with exactly one final-paragraph `Code-Commit: <sha>` trailer naming the code commit that same closeout landed. Stated the one-definition rule (both closeout routes render through it; the `memory.md`-only ledger leg keeps `message_for("ledger")` and carries none) and why the seam is the message construction rather than a later step. Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; verification metadata remains blank until governed closeout stamps the landed code commit.
