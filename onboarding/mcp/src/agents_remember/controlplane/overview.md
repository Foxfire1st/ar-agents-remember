# mcp/src/agents_remember/controlplane

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

This route retains generic durable-store mechanics, gate record/policy/enforcement and store values, attention acknowledgements and terminal notices, retention policy, stamps, the held-message store with its bounded discovery, and disposable closeout projections. Removed operator inboxes, expectation/signal stores, orchestration packet routing and timed relay have no current owner here.

## Construction And Ownership

durable_store.py owns validated JSONL mutation and held-lock replacement; records.py/store.py and gate_policy.py/enforcement.py retain existing approval values and their pure policy/enforcement. No product surface authors new gates; GateStore.claim_approval consumes an existing approval under its log lock and returns the gateless policy without creating a lifecycle lock directory when the log is absent. Stored approval history is not a native host lifecycle or a second task state. attention_dismissals.py owns the workspace acknowledgement set for all seven published kinds — the two surviving operational kinds (actionable-drift, blocked-start), the three live native causes (permission-wait, held-message, task-stalled) and the two terminal notices (task-landed, task-abandoned) — one acknowledgement per occurrence, while a kind written by an earlier build (provider-down, failed-setup) is still refused as not current. A dismissal hides one current occurrence and changes nothing at its cause; the occurrence ends when a pass observes native recovery, a changed complete drift finding, an answered prompt, a delivered or withdrawn message or a resumed bound turn, and that observation reclaims the row. The kept set is bounded to MAX_DISMISSALS = 256 and a 64 KiB whole-document bound, evicting oldest first in ascending (age, itemId) order, so an evicted acknowledgement may let its entry show again but never makes one appear. attention_notices.py is the separate disposable store for those terminal notices: it holds confirmed occurrences, interrupted intents and the creation cut (`StoreCut`), bounded by count and bytes, and it is written whole under its own ownership lock. Its observations reclaim an occurrence only after a complete source read proves it gone, healthy or changed, protecting acknowledgements newer than that read. Incomplete/unread kinds are retained. closeout_queue_records.py and closeout_queue_store.py hold the disposable projection, not canonical task truth. The route does not restore removed public gate tools, dashboard decisions, terminal catalogs, expectation projection rows or notifier scheduling. Spent approval kinds survive automatic TTL reclamation; legacy gate logs require the explicit removed-stores command for physical removal. Lock-only lifecycle residue is a distinct class requiring a complete native terminal-contract census. The former dormant lifecycle event-directory cleanup is not a current retention owner.

## Verification Boundary

Static source/intent inspection only. The removal inventory and Git history, not archived cards or historical references to removed sources, hold the deletion history. No guard is changed and no runtime, MEMORY grade or acceptance is inferred.

## Historical acknowledgement inventory

These former current claims are retained as history, not as instructions or present implementation evidence.

> attention_dismissals.py owns the workspace acknowledgement set for actionable-drift, provider-down, failed-setup and blocked-start occurrences.

## Evidence
- Retained gate logs have strict authority reads and a separate tolerant projection reader; their namespace is not a current lifecycle event stream. [1]

- Retained reference account (no fresh execution or acceptance inferred): Gate policy validation and delegated decision checks. [2]
- The structural gate facade re-exports kernel vocabulary only, not removed public gate-response operations or a native task-state model. [4]

- Provider degradation records its own state/events and can stop a critical provider; no removed operator-inbox posting occurs. [7]

- Guarded durable-store composition preserves coordinator containment and held-lock rewrite. [8]

- Retained reference account (no fresh execution or acceptance inferred): Durable-store role declaration follows application entry paths: `prepare_mcp_process` declares the MCP role, while dashboard `_dev_app` declares in the reload worker and `run` declares on the foreground/daemon command path.  Anchor: `prepare_mcp_process` `_dev_app` `run` [10]

- Undeclared checkout targets are restricted; primary checkout is refused [18]
- Applied gate permits only matching exact-operation recovery [20]
- Default human policy and explicit delegation/pinned kinds are kernel-owned [21]
- Delegation rejects owning-lifecycle decisions and missing required reviewer evidence [22]
- Consumed approval kinds keep applied authority without TTL; explicit removed-stores removal is distinct from native-census-qualified lock-only residue. Old inbox caps/expiry have no current owner here. [28]

- Projection requires exact source identity and owns scratch rather than semantic WAL [38]
- Canonical publication precedes projection invalidation/rebuild and returns refresh failures as effects [39]

- Current role_identity canonicalizes the one earlier specialist spelling to investigator; the removed orchestration packet router has no current ownership. [40]
- Workspace acknowledgements admit only published kinds and reclaim only with complete, time-qualified native observations; partial/unread kinds and newer clicks remain protected. [6]

- Shared kernel exclusion is independent of caller authorization. [9]

- JSONL admission precedes shared locking; appends fsync and replacement requires a held lock  Anchor: exclusive_access; append_line; append_lines; rewrite_lines [14]

- Daemon ownership checks are advisory and independent of unconditional locking; schema admission rejects unknown majors, without preserving an inbox ownership register. [15]

- Mutex/flock exclusion is reentrant and capability-probed  Anchor: exclusive_file_lock; _verify_lock_capability [16]
- Atomic publication fsyncs content and replaces before directory flush; Windows directory flush is unavailable  Anchor: atomic_write_bytes; _fsync_directory [17]
- Approval spending folds/evaluates/applies under one log lock  Anchor: claim_approval [19]

- Approval claiming keeps fold/evaluate/applied append under one log lock; no existing log yields gateless policy before opening a lock. [42]

- Workspace acknowledgements admit actionable-drift, blocked-start, permission-wait, held-message, task-stalled, task-landed and task-abandoned once per current occurrence; acknowledgement does not end a live cause. Source-based reconciliation protects unread/incomplete kinds and newer acknowledgements and reclaims absent/healthy/changed occurrences only from complete time-qualified observations. Rewrites remove admission-dropped malformed or retired provider rows, and count/serialized-byte bounds may evict the oldest acknowledgements even while their occurrences remain live. [43]
