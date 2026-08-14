# mcp/tests/test_chats_l5f_leaks.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_chats_l5f_leaks.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The 260718-CHATS-L5F R5 leak-fix regression suite: direct, composition-light unit coverage for the
daemon-side per-session structure release/bounding. It pins that the control service's per-session
lock map is bounded-by-construction AND released on session end, and that the queue-revision
bookkeeping map is capped with oldest-key eviction — the "keyed by session id"
CLASS-C leak class the half-time diagnosis named (`_locks` was the prime monotonic leak;
`queue_rows` was the open L3 precision-note Todo). The active-projector dormant-release companion
lives in `test_conversation_active_service.py::DormantReleaseTests`.

## Code Commentary

### Logic

A bare `ConversationControlService(cast(Any, object()))` is sufficient because `session_lock` /
`channel` / `release_session` / `_queue_row` only touch the per-session structures and the app
secret, never the runtime authorities. `_item(seq)` builds an `OperationTimelineItem` for the queue
rows.

cit:([`SessionLockLeakTests`], mcp/tests/test_chats_l5f_leaks.py:48-77): `test_release_session_drops_lock_and_every_epoch_channel` proves
`release_session(ar_session_id)` removes the session's `_locks` entry and every per-epoch channel;
`test_locks_are_bounded_by_construction_evicting_idle_first` proves `_locks` (an `OrderedDict`) is
capped at `MAX_SESSION_LOCKS_PER_APP` and `_evict_idle_locks` drops the oldest UNLOCKED lock first;
`test_a_held_lock_is_never_evicted` proves the eviction guard never drops a currently-held lock (so
an in-use serializer is never broken).

cit:([`QueueRowsBoundTests`], mcp/tests/test_chats_l5f_leaks.py:80-98): `test_queue_rows_are_bounded_with_oldest_key_eviction` proves
`_queue_row` caps `channel.queue_rows` (also an `OrderedDict`) at `MAX_QUEUE_ROWS_PER_CHANNEL`,
evicting the oldest key (`popitem(last=False)`) — a settled operation never reappears, so the bound
is invisible to live rows; `test_the_real_cap_is_a_named_constant` pins the cap as a named module
constant rather than a magic number. Since 260731-EFA-L2 the call the test drives is
`_queue_row(ControlScope(service, auth, "ar-1", "epoch-1"), channel, _item(seq))`: the service, the
`AuthorizationBinding`, the session id and the epoch travel as one frozen `ControlScope` parameter
object imported from `control.service`, in place of the four loose leading arguments. Nothing about
the cap or the eviction order changed — only how the scope reaches the helper.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this suite. | — | — |

## Repo-Internal References

The suite pins the control service's bounded/released lock map and the capped queue-revision map.

| Finding | Anchor | Source |
| --- | --- | --- |
| The `_locks` `OrderedDict`, `MAX_SESSION_LOCKS_PER_APP` cap, idle-first `_evict_idle_locks`, and `release_session` under test. | "def utc_clock" | mcp/src/agents_remember/serving/conversation/control/service.py:83-83 |
| The frozen `ControlScope` parameter object this suite now builds to call `_queue_row`. | "class ControlOperationError" | mcp/src/agents_remember/serving/conversation/control/service.py:104-104 |
| The `queue_rows` cap enforcement (`MAX_QUEUE_ROWS_PER_CHANNEL`, oldest-key `popitem`) under test. | "async def operation_queue" | mcp/src/agents_remember/serving/conversation/control/queue_projection.py:51-51 |
| The active-projector dormant-release companion to these control-side leak pins. | `CodexEngineTests` | mcp/tests/test_conversation_active_service.py:224-541 |

## Cross-Repo References

No cross-repository implementation participates in this suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the `PLR0913` parameter-object pass reached this
  suite, so the card's call-shape and every line citation it carries were re-derived from the
  current source. `_queue_row` no longer takes `(service, auth, channel, ar_session_id, epoch,
  item)`; the test now builds `ControlScope(service, auth, "ar-1", "epoch-1")` and passes it with
  the channel and the item, so the sidecar names the parameter object and its import. The added
  import line shifted both class anchors down one (`SessionLockLeakTests` L47 to L48,
  `QueueRowsBoundTests` L79 to L80), and inserting `ControlScope` into `control/service.py` ahead of
  `ControlChannel` moved the referenced lock-map region from L187-L244 to L230-L287 while
  `MAX_SESSION_LOCKS_PER_APP` stayed at L58; the `queue_projection.py` cap enforcement moved from
  L75-L103 to L81-L110. All four corrected ranges were re-read at their new positions, and a row was
  added pointing at the `ControlScope` definition. What the suite proves is unchanged: the lock map
  is still bounded and released, and the queue rows are still capped with oldest-key eviction.
  Verification metadata stays pinned until closeout stamps the code commit.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: created the sidecar for the R5 leak-fix
  regression suite — `SessionLockLeakTests` (release_session drops the lock + every-epoch channel;
  `_locks` bounded evicting idle-first; a held lock never evicted) and `QueueRowsBoundTests`
  (`queue_rows` capped with oldest-key eviction; the cap is a named constant). New source uncommitted;
  closeout owns its first source stamp.
