# mcp/src/agents_remember/application/knowledge_gate/adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_gate/adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:09:38+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The composition-bound `KnowledgeGatePort` of the worktree layer (MIK-R09).** The worktree layer ranks below the
application layer and reaches the gate only through `worktrees.services.KnowledgeGatePort`. `KnowledgeGate` is its
one implementation; `application/worktree_services.py` binds it as `knowledge_gate=KnowledgeGate()` in the default
services.

## Code Commentary

### Logic

- `leaf_refusal(contract, *, code_tree, memory_tree, parent_memory_tip)` evaluates `evaluate_leaf_gate` over
  `CandidateTrees(code, memory)` with the tip the caller read, and returns `None` (not applicable, or a pass) or
  `GateResult.refusal()`.
- `direct_verdict(contract, *, code_commit, memory_tree)` delegates to `direct.direct_verdict`.
- `landing_refusal(request)` delegates to `landing.landing_refusal`.

### Conventions

- A frozen, stateless dataclass: the memo lives in [`memo`](memo.py.md), so the curator publication and the closeout
  validator's port call compute the same key and one memory-quality run recomputes once.

### Invariants And Boundaries

- **No bypass (rule 5).** A converted route with no bound gate is refused (`GATE_UNBOUND` in
  `worktrees/knowledge_gate.py`), never committed ungated; proved by the closeout-validator test with `ports(gate=False)`.

### Todos

- None.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries).

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The port implementation: recompute over the exact trees, decide, validate. | `KnowledgeGate` | mcp/src/agents_remember/application/knowledge_gate/adapter.py:17-42 |
| The leaf refusal over the candidate trees. | "def leaf_refusal(" | mcp/src/agents_remember/application/knowledge_gate/adapter.py:21-34 |
| The direct and landing answers. | "def direct_verdict("; "def landing_refusal(self, request: LandingGateRequest)" | mcp/src/agents_remember/application/knowledge_gate/adapter.py:36-42 |
| The default composition binds it. | "knowledge_gate=KnowledgeGate()," | mcp/src/agents_remember/application/worktree_services.py:222-222 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:09:38+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): created this card for the new file MIK-R09 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
