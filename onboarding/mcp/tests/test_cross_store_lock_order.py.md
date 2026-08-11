# mcp/tests/test_cross_store_lock_order.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_cross_store_lock_order.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forcing regressions for the cross-store lock order (260731-EFA-L16): the 2026-08-05 production
incident where the liveness sweep held the `TerminalCatalog` batch lock across the
hosted-interaction synchronizer's operator-inbox/gate lock acquisitions while the supervisor
sweep held the inbox lock across a catalog read — an ABBA cycle that then parked the uvicorn
event loop on the catalog RLock and stopped the serving daemon from accepting (killed twice in
one day, py-spy-verified).

## Code Commentary

### Logic

`_SharedStores` builds the daemon's real sharing shape in a temp dir — ONE `TerminalCatalog`
instance and ONE operator-inbox log per process, plus the real `HostedInteractionSynchronizer`
and a `AgentNotifierContext` over the supporting stores — with a `_FakeHost` seam (every session
probes alive, nothing is owned) and a `counting_observe` wrapper that keeps every pass honest:
each test asserts the synchronizer actually ran, so no pass is vacuous. The pins:

1. the synchronizer's gate/inbox mutex acquisitions never execute while the calling thread holds
   `catalog.batch()` — a flagging batch wrapper plus a checking `durable_store.thread_mutex_for`
   record every violation, driven on the full sweep AND on the starting fast path
   (`_refresh_starting_rows`, whose cheap exits — nothing starting, busy sweep lock, starting
   rate limit — are pinned beside it);
2. `TerminalCatalogLivenessSweeper.refresh` and `run_agent_notifier_sweep` run concurrently on
   threads against the shared stores and both finish — rendezvous wrappers park the liveness
   sweep INSIDE its catalog batch and the supervisor INSIDE its inbox transaction, release both
   at once, and daemon threads with join timeouts are the deadlock detector, so against the
   pre-fix tree this test fails by timeout ("the ABBA is live") without hanging the suite;
3. a probe whose `sync_collector` is `None` (the direct callers outside a batch — WS attach,
   paste) keeps the legacy inline synchronizer call, driven both through a direct
   `observe_terminal_liveness` call and through `_observe_catalog_entry` without a collector;
4. `ConversationControlService.resolve_entry` runs its blocking catalog read in a worker
   thread, proven by a `resolve_running_entry` spy that records the executing thread;
5. the active side's `_projector_for` resolution is offloaded the same way;
6. the terminal-image handler runs both its `catalog.get` and its `_write_paste_image` disk
   write in worker threads, with the 200 response proving both paths were actually exercised.

### Conventions

The tests target lock placement and thread placement, not sweep or synchronizer behavior; the
quarantine contract, the fold→resolve→compact inbox transaction, and the wire shapes are
deliberately out of scope here. Verification metadata stays blank until closeout stamps the L16
commit.

### Invariants And Boundaries

- One store's lock is never held while another store's lock is acquired (the cross-store
  lock-order doctrine these tests enforce).
- No route body executes a catalog lock acquisition on the event-loop thread.
- The pre-fix tree must FAIL the rendezvous test by deadlock timeout — a green run against the
  pristine base would mean the reproduction is broken, not that the defect is absent.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The liveness sweep path driven on one thread (batch lock holder). | `TerminalCatalogLivenessSweeper` | mcp/src/agents_remember/serving/terminal_liveness.py:121-280 |
| The supervisor sweep path driven on the other thread (inbox lock holder). | `run_agent_notifier_sweep` | mcp/src/agents_remember/serving/agent_notifier.py:95-182 |
| The synchronizer whose store I/O is pinned outside the catalog batch. | `HostedInteractionSynchronizer` | mcp/src/agents_remember/serving/hosted_interactions.py:52-266 |
| The offloaded control choke point. | `resolve_entry` | mcp/src/agents_remember/serving/conversation/control/service.py:291-299 |
| The offloaded active-side resolution. | `_projector_for` | mcp/src/agents_remember/serving/conversation/active/service.py:160-177 |
| The offloaded image handler. | "async def _terminal_image_response(" | mcp/src/agents_remember/serving/_app_terminal_routes.py:634-634 |
| The intra-store lock contract the cross-store doctrine extends. | `thread_mutex_for` | mcp/src/agents_remember/controlplane/durable_store.py:344-358 |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T20:20+02:00 — 260731-EFA-L16 curator: the quality wrapper's diff-coverage rail grew
  the file from five pins to the current set — the starting-fast-path placement pin with its
  early returns, and the legacy inline direct-observe pin — and the wrapper's ruff/type findings
  were repaired. Verification stays blank until closeout stamps the L16 commit.
- 2026-08-05T19:58+02:00 — 260731-EFA-L16 curator: created the sidecar for the cross-store
  lock-order forcing tests (synchronizer placement, rendezvous-parked ABBA reproduction on the
  real sweep paths, event-loop offload of control/active/image resolution). Verification is
  blank because the new source file is uncommitted; closeout owns its first source stamp.
