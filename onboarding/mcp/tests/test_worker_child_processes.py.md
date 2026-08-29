# mcp/tests/test_worker_child_processes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worker_child_processes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T16:10+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No configured external documentation applies; the process contract is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required for the forcing proof. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A retained real child exits and has already been reaped by its owner. | `test_retained_worker_child_is_reaped_by_its_owner` | mcp/tests/test_worker_child_processes.py:19-29 |
| Registry identity is idempotent for one object and safe against PID aliasing or reuse. | `test_child_registry_is_idempotent_and_refuses_numeric_pid_aliasing`; `test_reaper_does_not_release_a_pid_now_owned_by_another_process` | mcp/tests/test_worker_child_processes.py:32-58 |
| Linux refuses missing pidfd APIs while non-Linux remains importable. | `test_linux_worker_boundary_refuses_a_python_without_native_pidfd`; `test_non_linux_import_boundary_does_not_require_pidfd` | mcp/tests/test_worker_child_processes.py:61-77 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite executes only local child processes under the candidate interpreter. | — | — |

## Update History

- 2026-08-29T16:10+02:00 — Created for the Python 3.13 migration's native-pidfd and separate
  child-reaping proof. Verification remains closeout-owned.
