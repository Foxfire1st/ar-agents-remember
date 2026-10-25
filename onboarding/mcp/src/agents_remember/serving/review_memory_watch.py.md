# mcp/src/agents_remember/serving/review_memory_watch.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Multiplexes connection-owned native invalidations for one admitted live leaf memory worktree into the existing state SSE stream.

## Code Commentary

`multiplex_review_memory` opts in only when the connection supplies a complete canonical `(repo, master, leaf)` identity and the injected root resolver admits it. With no identity it forwards ordinary stream events without root admission or a watch. The resolver runs off-loop; cancellation drains its thread before the connection finishes. Invalid, missing or unwired roots emit `review.memory.error` with identity/detail/nextAction while leaving the ordinary stream usable.

The native worker enumerates non-symlink directories once on startup, explicitly excluding `.git`, `provider-runtime`, `__pycache__`, `.cache`, generated `.index.json` and editor temporary/lock spellings. It installs nonrecursive RustNotify handles with polling disabled, then blocks on native notifications (`watch(40, 10, 0, stop)`). Directory registrations reconcile only on relevant native directory events, installing the replacement before closing old handles; there is no timer-driven rescan. Ordinary authored directories named tmp or captures are not excluded.

A separate readiness future prevents an edit during registration from being swallowed by the initial baseline. Later invalidations coalesce in a size-one queue. Events carry `review.memory` and an opaque per-connection nonce/counter revision, never a Git/tree identity or a semantic delta. Closing the stream sets the stop event and shields joining the native worker; merge cleanup cancels/awaits its pending reads and closes owned generators.

## Invariants And Boundaries

The watch reads no Git objects or knowledge index, stores no projection state, and creates no always-on review watcher. It does not itself refresh counts or subject content; consuming frontend invalidation owns that. Source regression assertions are not an executed timing or installed-budget result in this analysis.

## Evidence

- Only an explicitly selected, admitted review connection receives a watch; failures retain the ordinary stream. [1]
- Cancellation waits for root-admission completion. [2]
- Generated/cache/editor spellings are excluded from native watch input. [3]
- Directory enumeration does not follow symlink directories. [4]
- Nonrecursive native handles are installed and event-reconciled with replacement-before-retirement ordering. [5]
- The native wait uses a zero timeout and no filesystem polling loop. [6]
- Readiness is separate from coalesced updates; revisions are connection-local and close joins the worker. [7]

- The source regression queues a genuine native edit during registration and asserts distinct baseline/update events. [8]


- The source HTTP-disconnect regression requires worker exit before serving shutdown. [9]
