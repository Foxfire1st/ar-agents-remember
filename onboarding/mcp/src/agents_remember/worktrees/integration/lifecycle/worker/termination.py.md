# mcp/src/agents_remember/worktrees/integration/lifecycle/worker/termination.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

- Linux launch refuses an interpreter without both native pidfd APIs and gives the canonical bootstrap recovery. [1]
- Process fingerprint, native-pidfd signaling, and public recovery evidence remain the termination seam. [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## CCR-R18@v1 Durable-Termination-Only Projection

260831-CCR-L18 tightened `worker_termination_required_result` (line 243): it returns None unless durable `workerTermination` evidence exists on the record — a retained exact worker binding is ordinary live authority until a real cancellation/termination transition records termination evidence, and an exit-proven termination on a non-`termination-required` record no longer forces a termination result. The synthetic `_public_active_worker_authority` helper (which fabricated a termination-required result from live PID/lease/fingerprint cells) was deleted; the state matrix and the projection worker observation (`_worker_observation`) now own that classification. `worker_exit_unproven` and `bounded_worker_termination_outcome` remain for the cancel/termination mutation path.
