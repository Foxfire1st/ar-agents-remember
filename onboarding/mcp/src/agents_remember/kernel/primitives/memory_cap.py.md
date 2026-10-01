# mcp/src/agents_remember/kernel/primitives/memory_cap.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

The optional settings-owned hard bound for full quality-gate runs
(260731-EFA-L17-R3, revised by 260731-EFA-L24). Full-wrapper runs are
host-managed by default: pytest worker count is repository-configured (currently four), normal Linux/WSL RAM and swap
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
- This module never changes xdist worker selection; repository pytest configuration
  currently supplies `-n=4`.
- Availability probing is a hint, not enforcement: the integration runner still
  fails loudly if the scope cannot start.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo
(`system/sources.md` has no entries).

No relevant external documentation is configured for the memory-cap module.

### Repo-Internal References

- Preview reports the selected resource mode and planned command. [1]
- Execution follows the selected capped or uncapped command plan. [2]
- The settings model for `orchestration.qualityGate`, including the host-managed `None` default. [3]
- The fail-loud parser for `orchestration.qualityGate`, including absent/empty host-managed behavior. [4]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
