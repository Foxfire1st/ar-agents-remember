# mcp/src/agents_remember/code_quality/memory_cap.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/code_quality/memory_cap.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-08T02:00+02:00                     |
| lastVerifiedCommitHash | `1b7f6f07c5ccc64627299b5d22463ef9c267e187` |
| lastVerifiedCommitDate | 2026-08-08T02:42:36+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

The settings-owned memory bound for full quality-gate runs (260731-EFA-L17-R3).
Every full-wrapper run executes under a cap so an over-cap run dies inside its
own scope instead of taking down the WSL VM, the dashboard, and live sessions.
The policy name is part of every failure:
`orchestration.qualityGate.memoryCapBytes`.

## Code Commentary

### Logic

`MemoryCapPlan` (lines 43-51) is the frozen result of planning: the concrete
command, the mechanism, the cap bytes, and the policy key.

`plan_capped_command` (lines 94-135) picks the mechanism:

- **systemd scope** (primary when `systemd_scope_available()`, lines 52-71,
  says yes): `systemd-run --scope -p MemoryMax=<bytes> -p MemorySwapMax=0`,
  with `--user` added for non-root users (`_systemd_user_flag`, lines 72-78).
  `MemorySwapMax=0` makes the cap real on WSL/host swap. An over-cap run is
  OOM-killed inside its own scope (subprocess returncode -9, shell 137).
- **rlimit fallback**: the command runs the wrapper with
  `--memory-cap-bytes <bytes>` inserted after `-m <module>` by
  `with_self_cap` (lines 79-93); the wrapper applies `RLIMIT_AS` and an
  over-cap run dies with `MemoryError`.

The default cap is 2 GiB (`DEFAULT_FULL_GATE_MEMORY_CAP_BYTES`, line 32) — the
measured full-run plateau is ~0.5 GB RSS, and 2 GiB leaves headroom for the
address space the rlimit fallback sees. `AR_QUALITY_MEMORY_CAP` (line 36) is
the env var the wrapper sets after applying the rlimit so failure output names
the cap without a second configuration source.

### Conventions

The mechanism is reported with the command so the gate can print which cap
actually ran; `systemd_run_available` is injectable for tests and probed when
omitted.

### Invariants And Boundaries

- A full run without a cap is refused (the gate raises
  "full quality gate requires a settings-owned memory cap") — fail-closed, no
  uncapped full wrapper.
- Targeted leaf runs are NOT capped: the knob bounds full-wrapper runs at the
  master integration gate only.
- Availability probing is a hint, not enforcement: the integration runner still
  fails loudly if the scope cannot start.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo
(`system/sources.md` has no entries).

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for the memory-cap module. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The gate plans and runs the capped command, names the cap in refusals, and refuses a cap-less full run. | `QualityGatePlan`, `code_quality_gate_preview`, `run_strict_code_quality_gate`, `_gate_failure_message` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:29-35; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:77-146; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:162-219; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:249-275 |
| The settings model for `orchestration.qualityGate`. | `QualityGateSettings` | mcp/src/agents_remember/kernel/_agentic_settings_core.py:317-330 |
| The fail-loud parser for `orchestration.qualityGate`. | `_parse_quality_gate` | mcp/src/agents_remember/kernel/_agentic_settings_sections.py:476-494 |
| Proofs for availability branches, scope wrapping, the rlimit flag, and cap-kill naming. | `MemoryCapPlanningTests`, `WrapperMemoryCapTests` | mcp/tests/test_code_quality_memory_cap.py:70-150; mcp/tests/test_code_quality_memory_cap.py:151-275 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new memory-cap module; content derived from the
  current worktree source. Verification metadata pinned until closeout stamps
  the 260731-EFA-L17 commit.
