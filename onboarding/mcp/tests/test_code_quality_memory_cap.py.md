# mcp/tests/test_code_quality_memory_cap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_code_quality_memory_cap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-08T02:00+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The L17 proof suite for the full-gate memory cap: mechanism planning
(systemd scope vs rlimit), and the wrapper's `--memory-cap-bytes` main-path
enforcement and failure naming.

## Code Commentary

### Logic

`MemoryCapPlanningTests` (lines 70-150) pins the availability branches
(root/system manager, non-root user-manager socket), the exact systemd scope
command with `MemoryMax`/`MemorySwapMax=0` and the `--user` flag, the rlimit
fallback's self-cap flag insertion, and the malformed-module-args refusal.

`WrapperMemoryCapTests` (lines 151-275) drives the wrapper's cap main path
through a real repository:

- a non-positive cap is refused;
- a valid cap applies `RLIMIT_AS` and names the policy
  (`orchestration.qualityGate.memoryCapBytes`);
- an un-appliable cap and a cap-exceeded run fail loudly with the policy name;
- a `MemoryError` without a cap is reported as plain out-of-memory.

### Conventions

The wrapper cap path is exercised against a minimal real repository so the
rlimit application and subprocess inheritance are real, not mocked.

### Invariants And Boundaries

- The full gate never runs uncapped: planning without a cap is a refusal.
- The policy name is part of every cap failure so the operator sees exactly
  which knob to raise.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for the memory-cap suite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The planning functions under test. | `plan_capped_command`, `systemd_scope_available`, `with_self_cap` | mcp/src/agents_remember/kernel/primitives/memory_cap.py:94-135; mcp/src/agents_remember/kernel/primitives/memory_cap.py:52-71; mcp/src/agents_remember/kernel/primitives/memory_cap.py:79-93 |
| The wrapper main path that applies the rlimit and names the policy. | `main` | mcp/src/agents_remember/code_quality/check.py:861-903 |
| The gate's cap-kill naming (returncode -9 / shell 137). | `_gate_failure_message` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:346-372 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new memory-cap suite; content derived from the
  current worktree source. Verification metadata pinned until closeout stamps
  the 260731-EFA-L17 commit.
