# mcp/tests/test_dagger_registry_lock.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dagger_registry_lock.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Regress the host Dagger registry and checkout coordinator composition: an undeclared linked-checkout caller can transact against the host registry while live coordinator writes remain refused.

## Code Commentary

### Logic

The `registry` fixture constructs a synthetic linked checkout, points the checkout detector at its package source, and removes the execution-mode declaration; it does not impersonate a trusted process. `_Inspector` supplies engine facts without launching Docker, while `_admit` runs the real declaration parsing, snapshot, owner, registry and admission path.

The four cases prove: (1) coordinator lock/append refusal before creating its parent while host admission, continuation and exact release succeed; (2) replacement authority stays behind the live-owner barrier until both original owners release; (3) nested and outer exceptions preserve then release a real subprocess `flock` and the per-resource mutex observed by another thread; and (4) ignored `flock` yields the typed registry refusal before state/owner files exist, then the same registry recovers after the injected defect is removed.

### Conventions

Use bounded ten-second subprocess/thread operations. `_process_lock_status` returns 17 only when a separate interpreter is excluded by the physical lock, and zero after release. The tests preserve the physical `authority.lock.lock` identity and assert the resource path `authority.lock` itself is not created.

### Invariants And Boundaries

- Test setup deliberately leaves `declared_execution_mode()` unset.
- Host registry success never authorizes a live coordinator path.
- The inspector is a double; these cases establish registry composition and real POSIX exclusion, not a live Dagger engine run.
- The ineffective-lock test checks both the public `DaggerRuntimeAuthorityError` finding and its `LockCapabilityError` cause, and refuses before authority state exists.

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
| Linked checkout setup and real host admission entry. | `registry`; `_admit` | mcp/tests/test_dagger_registry_lock.py:35-48; mcp/tests/test_dagger_registry_lock.py:51-87 |
| Undeclared coordinator containment remains enforced while host admission succeeds. | `test_host_admission_keeps_undeclared_checkout_coordinator_writes_refused` | mcp/tests/test_dagger_registry_lock.py:90-115 |
| Two owners keep a replacement authority behind the transition barrier. | `test_undeclared_registry_preserves_transition_barrier_and_exact_owner_release` | mcp/tests/test_dagger_registry_lock.py:118-137 |
| Independent process and thread probes exercise nested exception release. | `_process_lock_status`; `_thread_can_take_mutex`; `test_registry_nested_exception_retains_then_releases_thread_and_process_exclusion` | mcp/tests/test_dagger_registry_lock.py:140-159; mcp/tests/test_dagger_registry_lock.py:162-167; mcp/tests/test_dagger_registry_lock.py:170-187 |
| Ineffective flock refuses before state publication and recovers on the same path. | `test_registry_refuses_ineffective_flock_before_state_and_can_recover` | mcp/tests/test_dagger_registry_lock.py:190-204 |
| Registry entry owns the domain error and exact physical lock. | `AuthorityRegistry` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:588-846 |

## Cross-Repo References

No separate cross-repository implementation dependency is used by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these claims. | N/A | N/A |

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:28+02:00 — Created the four-case registry composition regression card against the prepared L30 code; distinguished real process/thread exclusion from the engine-inspection double.
