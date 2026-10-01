# mcp/src/agents_remember/kernel/file_lock.py

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

## Evidence

### Docs References

No external Domain Documentation source is configured. The claims below describe the repository's own implementation; no external platform verification is claimed.

No configured domain documentation source.

### Repo-Internal References

These source owners establish the mechanics, caller policy, and regression boundaries described above.

- One physical suffix, one mutex per resource, and thread-local nesting. [1]
- Capability probing, complete transaction exclusion, and current-thread hold inspection. [2]
- Control-plane target authorization precedes primitive entry; capability errors are translated. [3]
- The host registry supplies its own policy and domain refusal. [4]


### Cross-Repo References

No separate cross-repository implementation dependency is used by this file.

No cross-repository evidence is required for these claims.
