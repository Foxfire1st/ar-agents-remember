# mcp/src/agents_remember/kernel/primitives/memory_cap.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/kernel/primitives/memory_cap.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-08T02:00+02:00                     |
| lastVerifiedCommitHash | `a89a6fc88d9330eb2749c87b3dcc3f6c4e46c4bd` |
| lastVerifiedCommitDate | 2026-08-14T12:44:51+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

The optional settings-owned hard bound for full quality-gate runs
(260731-EFA-L17-R3, revised by 260731-EFA-L24). Full-wrapper runs are
host-managed by default: pytest remains `-n=auto`, normal Linux/WSL RAM and swap
remain available, and Agents Remember does not introduce a ceiling. An operator
may explicitly configure `orchestration.qualityGate.memoryCapBytes` for a
constrained CI runner or another deliberately bounded environment.

## Code Commentary

### Logic

`MemoryCapPlan` is the frozen result of explicit-cap planning: the concrete
command, the mechanism, the cap bytes, and the policy key.

`plan_capped_command` picks the mechanism after a positive cap was explicitly
configured:

- **systemd scope** (primary when `systemd_scope_available()`, lines 52-71,
  says yes): `systemd-run --scope -p MemoryMax=<bytes>`, with `--user` added
  for non-root users. It deliberately does not set `MemorySwapMax=0`, so the
  host's normal swap policy remains available. An over-cap run is OOM-killed
  inside its own scope (subprocess returncode -9, shell 137).
- **rlimit fallback**: the command runs the wrapper with
  `--memory-cap-bytes <bytes>` inserted after `-m <module>` by
  `with_self_cap` (lines 79-93); the wrapper applies `RLIMIT_AS` and an
  over-cap run dies with `MemoryError`.

There is no default cap. `AR_QUALITY_MEMORY_CAP` is the env var the wrapper sets
after applying the explicit rlimit so failure output names the cap without a
second configuration source.

### Conventions

The mechanism is reported with the command so the gate can print which cap
actually ran; `systemd_run_available` is injectable for tests and probed when
omitted.

### Invariants And Boundaries

- A full run without an explicit cap is the normal host-managed path; this
  primitive is not called for that path.
- Targeted leaf runs are NOT capped: the knob bounds full-wrapper runs at the
  master integration gate only.
- This module never changes xdist auto-worker selection. `-n=auto` stays owned
  by repository pytest configuration.
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
| The gate runs uncapped full commands directly, plans explicitly capped commands here, and reports both resource modes. | `code_quality_gate_preview`; `run_strict_code_quality_gate` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:107-169; mcp/src/agents_remember/worktrees/modules/quality/gate.py:184-265 |
| The settings model for `orchestration.qualityGate`, including the host-managed `None` default. | "class QualityGateSettings:" | mcp/src/agents_remember/kernel/_agentic_settings_core.py:248-257 |
| The fail-loud parser for `orchestration.qualityGate`, including absent/empty host-managed behavior. | `_parse_quality_gate` | mcp/src/agents_remember/kernel/_agentic_settings_sections.py:382-400 |
| Proofs for availability branches, scope wrapping, the rlimit flag, and cap-kill naming. | `MemoryCapPlanningTests`, `WrapperMemoryCapTests` | mcp/tests/test_code_quality_memory_cap.py:70-150; mcp/tests/test_code_quality_memory_cap.py:151-275 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: made the cap explicitly
  opt-in, recorded the host-managed default and literal pytest `-n=auto`, and
  removed the stale `MemorySwapMax=0`/mandatory-2-GiB doctrine. Verification
  metadata remains pinned until closeout stamps the L24 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new memory-cap module; content derived from the
  current worktree source. Verification metadata pinned until closeout stamps
  the 260731-EFA-L17 commit.
