# mcp/tests/test_code_quality_memory_cap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_code_quality_memory_cap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-08T02:00+02:00 |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b` |
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The L17/L24 proof suite for the optional full-gate hard cap: mechanism planning
(systemd scope vs rlimit), retained host swap, and the wrapper's `--memory-cap-bytes` main-path
enforcement and failure naming.

## Code Commentary

### Logic

`MemoryCapPlanningTests` (lines 70-150) pins the availability branches
(root/system manager, non-root user-manager socket), the exact systemd scope
command with `MemoryMax` but no `MemorySwapMax=0`, plus the `--user` flag, the rlimit
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

- This suite plans only an explicit cap; the host-managed full path bypasses this
  primitive and is proven in `test_worktree_quality_gate_runner.py`.
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
| The planning functions under test. | `plan_capped_command`, `systemd_scope_available`, `with_self_cap` | mcp/src/agents_remember/kernel/primitives/memory_cap.py:92-130; mcp/src/agents_remember/kernel/primitives/memory_cap.py:50-67; mcp/src/agents_remember/kernel/primitives/memory_cap.py:77-89 |
| The wrapper main path that applies the rlimit and names the policy. | `main` | mcp/src/agents_remember/code_quality/check.py:988-1036 |
| The gate's cap-kill naming (returncode -9 / shell 137). | `_gate_failure_message` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:457-481 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: recorded that
  systemd explicit caps retain host swap and that uncapped full execution is a
  separate host-managed gate path. Verification metadata remains pinned until
  closeout stamps L24.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new memory-cap suite; content derived from the
  current worktree source. Verification metadata pinned until closeout stamps
  the 260731-EFA-L17 commit.
