# mcp/src/agents_remember/kernel/file_lock.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/file_lock.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../../../overview.md` |

## Governing Overview

[Governing route overview](../../../overview.md)

## Purpose

Own the shared, policy-free POSIX exclusion primitive for one local file resource. Control-plane logs and the host Dagger registry share the same physical lock protocol while retaining their separate authorization policies.

## Code Commentary

### Logic

`lock_path_for` appends `.lock` to the whole resource name, so `authority.lock` continues to use `authority.lock.lock`. `thread_mutex_for` returns one per-path `RLock`, with first registration serialized by a registry mutex. Each outer `exclusive_file_lock` creates the lock parent, takes the thread mutex, probes filesystem exclusion, then holds `flock` across the caller transaction.

The capability probe opens the same lock twice through distinct file descriptions. A refused second acquisition caches that path as verified; a successful second acquisition raises `LockCapabilityError`. Failed probes do not cache success. `_LockDepth` is thread-local: same-thread nesting shares the outer hold, restores the previous depth on exit, and other threads still acquire both locks. `lock_held` reports the calling thread's actual nesting state.

### Conventions

Callers authorize the resource before entering. The kernel primitive neither declares an execution role nor routes coordinator data. The mutex is acquired before `flock`; it makes thread exclusion independent of file-handle reuse. This is the single owner of lock naming, nesting state, per-resource mutexes, and capability cache.

### Invariants And Boundaries

- Hold exclusion across the complete read-modify-write transaction.
- Nested exits and exceptions preserve the outer hold, then release both locks on the final exit.
- Never acquire another resource's lock while holding this one.
- Lock capability failure is explicit; there is no unlocked or per-process-only continuation.
- Control-plane authorization remains in `durable_store.exclusive_access`; host registry policy remains in `AuthorityRegistry.exclusive_access`. Moving mechanics does not grant checkout coordinator access.

### Todos

None identified in this bounded source review.

## Docs References

No external Domain Documentation source is configured. The claims below describe the repository's own implementation; no external platform verification is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation source. | N/A | N/A |

## Repo-Internal References

These source owners establish the mechanics, caller policy, and regression boundaries described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| One physical suffix, one mutex per resource, and thread-local nesting. | `lock_path_for`; `thread_mutex_for`; `_LockDepth` | mcp/src/agents_remember/kernel/file_lock.py:36-38; mcp/src/agents_remember/kernel/file_lock.py:41-55; mcp/src/agents_remember/kernel/file_lock.py:19-27 |
| Capability probing, complete transaction exclusion, and current-thread hold inspection. | `_verify_lock_capability`; `exclusive_file_lock`; `lock_held` | mcp/src/agents_remember/kernel/file_lock.py:58-84; mcp/src/agents_remember/kernel/file_lock.py:87-114; mcp/src/agents_remember/kernel/file_lock.py:117-119 |
| Control-plane target authorization precedes primitive entry; capability errors are translated. | `exclusive_access`; `require_lock_held` | mcp/src/agents_remember/controlplane/durable_store.py:319-360; mcp/src/agents_remember/controlplane/durable_store.py:363-381 |
| The host registry supplies its own policy and domain refusal. | `AuthorityRegistry` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:588-846 |
| Regression proves process/thread exclusion, nested exception release, and ineffective-lock refusal. | `test_registry_nested_exception_retains_then_releases_thread_and_process_exclusion`; `test_registry_refuses_ineffective_flock_before_state_and_can_recover` | mcp/tests/test_dagger_registry_lock.py:170-187; mcp/tests/test_dagger_registry_lock.py:190-204 |

## Cross-Repo References

No separate cross-repository implementation dependency is used by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these claims. | N/A | N/A |

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:28+02:00 — Created the shared lock-owner card against prepared code commit 6e4ab81f6ae52bce35003377bb3aec7877554ed7; preserved the physical lock protocol and separate caller authorization boundaries.
