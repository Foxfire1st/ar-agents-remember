# mcp/src/agents_remember/controlplane

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

This route retains generic durable-store mechanics, gate record/policy/enforcement and store values, attention acknowledgements, retention policy, stamps and disposable closeout projections. Removed operator inboxes, expectation/signal stores, orchestration packet routing and timed relay have no current owner here.

## Construction And Ownership

durable_store.py owns validated JSONL mutation and held-lock replacement; records.py/store.py and gate_policy.py/enforcement.py retain gate values and pure policy. attention_dismissals.py owns the remaining acknowledgement set. closeout_queue_records.py and closeout_queue_store.py hold the disposable projection, not canonical task truth. The route does not restore removed public gate tools, dashboard decisions, terminal catalogs or notifier scheduling.

## Verification Boundary

Static source/intent inspection only. The removal inventory and Git history, not archived cards or historical references to removed sources, hold the deletion history. No guard is changed and no runtime, MEMORY grade or acceptance is inferred.

## Evidence
- Retained reference account (no fresh execution or acceptance inferred): Gates mirror the observer event substrate (envelope + append-only JSONL store). [1]
- Retained reference account (no fresh execution or acceptance inferred): Gate policy validation and delegated decision checks. [2]
- Retained reference account (no fresh execution or acceptance inferred): Gate response models, including the structural public boundary and internal exact correlations. [4]
- Retained reference account (no fresh execution or acceptance inferred): The attention acknowledgement store keeps current lifecycle-scoped queue dismissals only. [6]
- Provider degradation records its own state/events and can stop a critical provider; no removed operator-inbox posting occurs. [7]
- Retained reference account (no fresh execution or acceptance inferred): Guarded durable-store composition preserves coordinator containment and held-lock rewrite. [8]
- Retained reference account (no fresh execution or acceptance inferred): Shared kernel exclusion is independent of caller authorization. [9]
- Retained reference account (no fresh execution or acceptance inferred): Durable-store role declaration follows application entry paths: `prepare_mcp_process` declares the MCP role, while dashboard `_dev_app` declares in the reload worker and `run` declares on the foreground/daemon command path. [10]
- Retained reference account (no fresh execution or acceptance inferred): The projection tick reads folded gates and pending expectation rows without rewriting them. [12]

- Undeclared checkout targets are restricted; primary checkout is refused [18]
- Applied gate permits only matching exact-operation recovery [20]
- Default human policy and explicit delegation/pinned kinds are kernel-owned [21]
- Delegation rejects owning-lifecycle decisions and missing required reviewer evidence [22]
- Protected ids can exceed the nominal cap; pending compaction awaits surfaced expiry; spent gate kinds survive TTL [28]
- Projection requires exact source identity and owns scratch rather than semantic WAL [38]
- Canonical publication precedes projection invalidation/rebuild and returns refresh failures as effects [39]

- Current role_identity canonicalizes the one earlier specialist spelling to investigator; the removed orchestration packet router has no current ownership. [40]
- Lifecycle pruning removes whole unprotected dormant directories [41]
- The attention acknowledgement store keeps current lifecycle-scoped queue dismissals only.  Anchor: "class AttentionDismissalStore" [6]
- Guarded durable-store composition preserves coordinator containment and held-lock rewrite. [8]
- Shared kernel exclusion is independent of caller authorization. [9]
- The projection tick reads folded gates and pending expectation rows without rewriting them.  Anchor: "def read_gates(coordination_root: Path, *, now: datetime"; "def read_expectation_rows(" [12]
- JSONL admission precedes shared locking; appends fsync and replacement requires a held lock  Anchor: exclusive_access; append_line; append_lines; rewrite_lines [14]
- Ownership is advisory; inbox has no single compaction owner; schema accepts only major 1  Anchor: StoreOwnership; ownership register; schema_version_supported [15]
- Mutex/flock exclusion is reentrant and capability-probed  Anchor: exclusive_file_lock; _verify_lock_capability [16]
- Atomic publication fsyncs content and replaces before directory flush; Windows directory flush is unavailable  Anchor: atomic_write_bytes; _fsync_directory [17]
- Approval spending folds/evaluates/applies under one log lock  Anchor: claim_approval [19]
