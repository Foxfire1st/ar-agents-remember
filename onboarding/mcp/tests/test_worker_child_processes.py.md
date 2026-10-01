# mcp/tests/test_worker_child_processes.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Separately proves detached lifecycle-child ownership/reaping and the Linux native-pidfd runtime
admission boundary.

## Code Commentary

### Logic

The real-process test transfers a short-lived `Popen` to the lifecycle owner, waits for completion,
and proves the child was already reaped. Focused registry tests pin idempotent same-object retain,
PID-alias refusal, and identity-safe release. Runtime tests force Linux refusal when either native
pidfd API is unavailable and preserve non-Linux importability.

### Conventions

One real child supplies operating-system evidence; narrow mocks isolate registry identity edges.
Runtime capability absence is simulated only to prove loud admission refusal, never to install a
fallback implementation.

### Invariants And Boundaries

- Successful detached launches do not leave zombie children.
- PID reuse cannot transfer ownership implicitly.
- Linux workers require native `os.pidfd_open` and `signal.pidfd_send_signal`.
- Non-Linux importability does not claim Linux cancellation support.
- Dagger owns certifying execution.

### Todos

None recorded.

## Evidence

### Docs References

No configured external documentation applies; the process contract is repository-owned.

No external source is required for the forcing proof.

### Repo-Internal References

- A retained real child exits and has already been reaped by its owner. [1]
- Registry identity is idempotent for one object and safe against PID aliasing or reuse. [2]
- Linux refuses missing pidfd APIs while non-Linux remains importable. [3]

### Cross-Repo References

No meaningful cross-repository reference applies.

The suite executes only local child processes under the candidate interpreter.
