# mcp/tests/test_atomic_series_activation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_series_activation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

This focused suite forces the durable source-pair selector contract independently from the public
selecting transaction. It protects multiple-live-series behavior, exact replacement/release,
effective vacancy, corrupt-authority preservation, and read-only queue projection.

## Code Commentary

### Logic

`ActivationFixture` builds real Git/task/series-contract worlds for two masters sharing a source
pair. The tests prove absence is vacant; switching selection pauses old work without removing either
contract; same selection is idempotent; different source pairs isolate files; terminal selected
contracts become effective vacancy; malformed bytes are archived before selecting repair; a
nonregular symlink entry is quarantined without following or changing its target; explicit release
persists vacancy and last-owner identity; another selected master cannot be released; and
terminal cleanup releases before contract deletion while preserving a newer selection.

The final cases keep malformed selector bytes intact through terminal cleanup and translate a
source-alias identity failure into a bounded projection source problem.

### Conventions

Tests use real temporary repositories/contracts for store and identity behavior, with mocking only
at the focused alias failure boundary. Injected timestamps make revision/archive assertions stable.

### Invariants And Boundaries

- Multiple live contracts are the expected baseline, not an error fixture.
- Tests distinguish selected master from last selected master after durable vacancy.
- Queue behavior is asserted only as observation/waiting/problem projection.
- No Dagger or acceptance claim is implied by this focused source suite.

### Todos

Exact test claims and citations are reconciled to the frozen inventory; verification remains
unstamped until the real code commit exists.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selector derivation, observation, replacement, and waiting reasons are the primary subject. | `atomic_series_source_pair`; `observe_atomic_series`; `publish_atomic_series_selection`; `activation_waiting_reason` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:105-127; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:170-187; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:190-249; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:298-311 |
| Durable cancellation and terminal vacancy transitions are forced separately. | `release_atomic_series_selection`; `release_terminal_atomic_series_selection_if_exact` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:24-55; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:58-79 |
| Queue projection converts unreadable authority into bounded source problems. | `project_series_activation` | mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py:30-53 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of selector replacement, isolation,
  archive, vacancy, and exact-release forcing.

- 2026-08-26T05:40+02:00 — Added the completed nonregular selector quarantine forcing case to the
  suite description. Final ranges remain post-Dagger-owned.

- 2026-08-26T02:55+02:00 — Drafted focused selector-test onboarding; post-Dagger test inventory,
  nonregular-entry case, exact ranges, and verification remain open.