# mcp/tests/test_chats_l5f_leaks.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_chats_l5f_leaks.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The 260718-CHATS-L5F R5 leak-fix regression suite: direct, composition-light unit coverage for the
daemon-side per-session structure release/bounding. It pins that the control service's per-session
lock map is bounded-by-construction AND released on session end, and that the queue-revision
bookkeeping map is capped with oldest-key eviction — the "keyed by session id, never released"
CLASS-C leak class the half-time diagnosis named (`_locks` was the prime monotonic leak;
`queue_rows` was the open L3 precision-note Todo). The active-projector dormant-release companion
lives in `test_conversation_active_service.py::DormantReleaseTests`.

## Code Commentary

### Logic

A bare `ConversationControlService(cast(Any, object()))` is sufficient because `session_lock` /
`channel` / `release_session` / `_queue_row` only touch the per-session structures and the app
secret, never the runtime authorities. `_item(seq)` builds an `OperationTimelineItem` for the queue
rows.

`SessionLockLeakTests` (L47): `test_release_session_drops_lock_and_every_epoch_channel` proves
`release_session(ar_session_id)` removes the session's `_locks` entry and every per-epoch channel;
`test_locks_are_bounded_by_construction_evicting_idle_first` proves `_locks` (an `OrderedDict`) is
capped at `MAX_SESSION_LOCKS_PER_APP` and `_evict_idle_locks` drops the oldest UNLOCKED lock first;
`test_a_held_lock_is_never_evicted` proves the eviction guard never drops a currently-held lock (so
an in-use serializer is never broken).

`QueueRowsBoundTests` (L79): `test_queue_rows_are_bounded_with_oldest_key_eviction` proves
`_queue_row` caps `channel.queue_rows` (also an `OrderedDict`) at `MAX_QUEUE_ROWS_PER_CHANNEL`,
evicting the oldest key (`popitem(last=False)`) — a settled operation never reappears, so the bound
is invisible to live rows; `test_the_real_cap_is_a_named_constant` pins the cap as a named module
constant rather than a magic number.

### Conventions

Standard-library `unittest` (async lock tests on `IsolatedAsyncioTestCase`, the synchronous queue
tests on `TestCase`); no socket, no bridge, no runtime composition — the per-session structures are
driven directly so the bound/release is asserted at its origin.

### Invariants And Boundaries

- The leak class is closed BOTH ways: bounded-by-construction (a cap with oldest/idle-first eviction)
  AND released on session end (`release_session`) — a held lock is never the eviction victim.
- The queue-row cap is a named constant; an evicted key restarts at revision 1 only if its operation
  ever reappears, and settled operations do not, so the bound cannot corrupt a live row's revision.
- These are unit-origin pins; the open→End heap-growth composed proof rides on the E2E suite, and the
  active-projector dormant release is proven in `test_conversation_active_service.py`.

### Todos

Reviewer F1 (accepted-bounding disposition): the sync control `release_session` and the async active
`release_session` exist and are unit-tested here / in the active-service suite but are NOT wired into
the terminate/retire endpoints this leaf — the leak is closed by bounding + the tombstone's
idle-self-release, not by an explicit end-hook. Wiring locus recorded as a follow-on (expose the
`ConversationRuntime` and call `release_session` after `catalog.mark_terminated`).

## Docs References

The resolved `Domain Documentation` registry has no entries; the leak-fix contract is
repository-owned and cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this suite. | — | — |

## Repo-Internal References

The suite pins the control service's bounded/released lock map and the capped queue-revision map.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `_locks` `OrderedDict`, `MAX_SESSION_LOCKS_PER_APP` cap, idle-first `_evict_idle_locks`, and `release_session` under test. | L58; L187-L244 | [control/service.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/service.py) |
| The `queue_rows` cap enforcement (`MAX_QUEUE_ROWS_PER_CHANNEL`, oldest-key `popitem`) under test. | L75-L103 | [control/queue_projection.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/queue_projection.py) |
| The active-projector dormant-release companion to these control-side leak pins. | — | [test_conversation_active_service.py](agents-remember/mcp/tests/test_conversation_active_service.py) |

## Cross-Repo References

No cross-repository implementation participates in this suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: created the sidecar for the R5 leak-fix
  regression suite — `SessionLockLeakTests` (release_session drops the lock + every-epoch channel;
  `_locks` bounded evicting idle-first; a held lock never evicted) and `QueueRowsBoundTests`
  (`queue_rows` capped with oldest-key eviction; the cap is a named constant). New source uncommitted;
  closeout owns its first source stamp.
