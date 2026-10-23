# mcp/src/agents_remember/controlplane/attention_dismissals.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`attention_dismissals.py` keeps the bounded current acknowledgements for every published attention kind: the surviving operational kinds (provider-down, failed-setup, blocked-start, actionable-drift), the two terminal notices `task-landed` and `task-abandoned`, and — since L190 v2 — the three live native causes permission wait, held message and stalled task. One acknowledgement hides exactly one occurrence, and the kind vocabulary refuses any kind this build does not publish, so a row written by an earlier build is never read as a current one. Dismissing a live cause changes nothing at its cause: the prompt stays unanswered, the message stays held, and the task's stage and its seats stay as they are. These are disposable UI facts, not an audit or authority log. An occurrence ends when a pass observes that it ended — native recovery/removal, a changed complete drift finding, an answered prompt, a delivered or withdrawn message, a resumed bound turn — and that observation is what reclaims its record. The store's count and byte bound (`MAX_DISMISSALS = 256`, `MAX_DISMISSAL_BYTES = 64 * 1024`, oldest first) is the only other way a row leaves, and nothing here ends an occurrence on a new clock tick or an inferred session status.

## Code Commentary

### 260731-EFA-L5 The Single-Writer Store That Lost The Most

This log measured the **worst loss of the six** at the base commit: **31.45 percent** of writes
lost — the one base-commit figure carried at several independent sites (`durable_store.py`,
`agent_notifier_signals.py`, `test_durable_store_contract.py`, `test_observer_projection.py`) rather
than at one. It also had a
single writer. Both facts are true at once, and the reason is the most important thing on this card.

`dismiss()` is a whole-file read/upsert/rewrite keyed by `itemId`, so concurrent button clicks need serialization even in one dashboard process. `reconcile(observations)` is another whole-read/filter/rewrite over the same file and holds that same lock across both halves; a single declared writer does not make concurrent read-modify-writes safe.

The raising was the colliding temp path: `_replace` built `<log>.tmp` with nothing to distinguish
one writer from another, so two concurrent rewriters shared it, one `os.replace`d it away and the
other raised. That reached the operator as a 500 on a click.

An earlier draft of this leaf left this store **unlocked** on the strength of it being
single-writer. The proof run measured the 31.45 percent doing exactly that. This is why
`StoreOwnership` has no `serialized` field: "only one process writes this file" is a deployment
fact, not a structural one.

### 260731-EFA-L5 What Changed

Every rewrite now holds the log's lock across the read **and** the rewrite:

- `dismiss(record)` and `reconcile(observations)` hold `exclusive_access` across the complete read and rewrite.
- `_replace` delegates to `durable_store.rewrite_lines`, which requires the held lock, uses the shared durable replacement boundary and leaves an empty current set as an empty file rather than unlinking it.
- An unchanged reconciliation performs no physical rewrite; a cleanup `OSError` returns the pre-cleanup current map, retaining suppression.

`AttentionDismissalRecord` now inherits `DurableRecord` instead of `BaseModel`, so it picks up
`extra="forbid"` (previously declared locally) plus a validated `schemaVersion`: an unknown major
raises `ValidationError` at parse time and this store's tolerant reader skips the row, with no
version branch in the reader.

`ATTENTION_DISMISSAL_OWNERSHIP` declares the dashboard both the sole writer and the compaction
owner.

**Note on the read policy.** `read()` stays tolerant — these are disposable UI facts, and one bad
row must not 500 the dismiss endpoint or freeze a tick. Because it is the store's only reader, the
rewrites above are driven by the tolerant read, so a compaction here *does* drop an unparseable row
permanently. That is safe precisely because this log carries no authority; it would stop being safe
the moment a decision depended on one of these rows.

### 260707-HFX2-L12 CS-6 Update

`AttentionDismissalStore.read()` tolerates malformed/torn UI rows and folds valid rows by `itemId`; it does not interpret a malformed native source as healthy. Malformed acknowledgement rows can disappear on a required rewrite because they carry no execution authority.

`AttentionDismissalRecord` carries itemId, validated dismissedAt, supported kind and optional actionableFingerprint in workspace/attention-dismissals.jsonl. `dismiss` upserts, `current` folds duplicates.

`AttentionObservation` records actual read-start, completeness, existing/healthy IDs and fingerprints. Only complete observations begun at/after the click reclaim proved recovery/removal or changed fingerprints. Unread kinds, failed enumeration, unknown health and missing fingerprints prove no end. Missing stored fingerprint adopts the first complete available one.

### 20261023-L190-v2 Every Published Entry Is Acknowledged, And The Store Is Bounded

MIK-R200@v2 rule 7 makes the acknowledgement the developer's, not the cause's: every published entry is dismissed once per occurrence. The kind vocabulary grows the three live native causes (`supported_kind`, :56-75), and the backend's 409 `not-dismissible` refusal is gone, so `serving/actions.py:112-117` compares kinds and accepts. A retired spelling still refuses, which is what keeps an older row from being read as a current acknowledgement.

The record needs no second notion of identity: `itemId` is the occurrence identity the builder published — `permission-wait:{agent}:{prompt}`, `held-message:{recipient}:{message}`, `task-stalled:{task}:{interval start}`, and a notice's own occurrence id.

Reclamation now comes from the same pass that publishes the row. `ProjectionInputState._observe_native_kinds` supplies one `AttentionObservation` per complete live kind (`serving/projections/projection_inputs.py:750-787`), and `reconcile` keeps a record whose occurrence is still in that observation's existing set, reclaiming it when the occurrence is gone, is observed healthy, or its known fingerprint changed. An incomplete observation, an unreadable publication or an unknown host supplies no observation at all, so no record of that kind is reclaimed.

Rule 10's bounds are enforced on the one write path. `_bounded` (:265-279) orders rows oldest first — an unparseable stamp ranks oldest, so it leaves first — and drops them until `MAX_DISMISSALS` (:41) and `MAX_DISMISSAL_BYTES` (:44) hold over the exact document `_render` writes. An evicted record may let its entry show again; that is accepted, as for a notice, and shedding only ever removes: nothing here re-derives an occurrence from a source fact.

## Invariants And Boundaries

- Disposable UI acknowledgement, never approval or mutation authority.
- Native complete per-kind proof governs cleanup; retained projection state is not a census and unknown is not healthy.
- Click/read-start ordering and whole read/rewrite locking preserve concurrent clicks; empty sets stay as empty files.
- Cleanup OSError retains prior suppression; click OSError is `dismissal-not-held` HTTP 503, not success.
- The acknowledgement set is bounded: at most `MAX_DISMISSALS` rows and `MAX_DISMISSAL_BYTES` over the written document, shedding oldest first, and an evicted record can only let an entry reappear.

## Evidence

### Repo-Internal References

- Projection input refreshers collect native per-kind AttentionObservations and reconcile acknowledgements through AttentionDismissalStore. A record can be reclaimed for source absence, healthy recovery or a changed known fingerprint only when the observation is complete and started no earlier than its dismissal; the first complete fingerprint can instead be adopted. Unread/incomplete kinds retain their acknowledgements. Reconciliation is locked, avoids unchanged physical writes and returns prior current acknowledgements if cleanup fails; this is not prune_lifecycles after a lifecycle fold. [1]
- Whole read/rewrite exclusion and cleanup-failure retention preserve concurrent acknowledgements. [5]
