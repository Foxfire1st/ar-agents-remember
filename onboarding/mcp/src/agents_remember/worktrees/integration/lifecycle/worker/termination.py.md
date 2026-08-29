# mcp/src/agents_remember/worktrees/integration/lifecycle/worker/termination.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/worker/termination.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T16:27+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[worktree integration overview](../../overview.md)

## Purpose

Platform-owned worker identity, signal, and exit-proof boundary.

## Code Commentary

### Logic

The public surface includes `require_linux_worker_runtime`, `worker_process_fingerprint`,
`signal_worker_and_prove_exit`, `public_worker_termination_evidence`,
`worker_termination_required_result`, `bounded_worker_termination_outcome`, and
`observe_worker_termination`. Linux launch admission requires callable native `os.pidfd_open` and
`signal.pidfd_send_signal` and points an incompatible environment to the canonical project-venv
bootstrap. Worker authority remains durable until exact process identity and termination are
proven. Signal, permission, launch, or observation failure records a termination-required/public
recovery result and blocks replacement instead of optimistically clearing the PID or lease.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.
- Linux cancellation uses the interpreter's native pidfd APIs; this module owns no `ctypes`
  syscall wrapper, compatibility dependency, or silent `killpg` fallback.
- Child ownership and zombie reaping are separate and live in `child_processes.py`.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Linux launch refuses an interpreter without both native pidfd APIs and gives the canonical bootstrap recovery. | `require_linux_worker_runtime` | mcp/src/agents_remember/worktrees/integration/lifecycle/worker/termination.py:20-34 |
| Process fingerprint, native-pidfd signaling, and public recovery evidence remain the termination seam. | `worker_process_fingerprint`; `signal_worker_and_prove_exit`; `public_worker_termination_evidence` | mcp/src/agents_remember/worktrees/integration/lifecycle/worker/termination.py:35-50; mcp/src/agents_remember/worktrees/integration/lifecycle/worker/termination.py:53-103; mcp/src/agents_remember/worktrees/integration/lifecycle/worker/termination.py:222-240 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-29T16:27+02:00 — Added the explicit Linux native-pidfd runtime admission contract and
  recorded that compatibility signaling and child reaping are separate, non-duplicated concerns.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/worker/termination.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
