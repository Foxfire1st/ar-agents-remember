# mcp/src/agents_remember/observer/worktree_provider_admission.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/observer/worktree_provider_admission.py` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-01T00:52+02:00                                      |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                  |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[observer overview](overview.md)

## Purpose

`worktree_provider_admission.py` centralizes active-enclosure admission for
worktree-scoped runtime projection. It separates the stricter provider-alarm
boundary from the broader Engine Room boundary: worktree providers/setup progress
are operational only for active provider-relevant lifecycle phases, while engine
process facts may still project for any non-terminal enclosure lifecycle.

The durable **enclosure contract is the source of truth for liveness**, not the lifecycle event
log. The log is a best-effort demotion signal that can be pruned for inactivity (see
`event_retention.py`); a *missing* log therefore must never retire a live worktree. This module
also derives the inverse protection — `series_retained_lifecycle_ids` — that the projection store
feeds back into event retention so a not-yet-retired master series' logs are kept.

## Code Commentary

### Logic

`admitted_worktree_groups(enclosures, lifecycle_logs, *, now)` folds lifecycle
logs with `project_lifecycle`, joins each enclosure by `lifecycleId`, rejects
cleanup-completed/abandoned enclosures, rejects closeout/integration-completed
enclosures, and admits only provider-relevant phases (`request`,
`trust-checkpoint`, `reframe-research`, `decide`, `build`). Crucially, a **missing**
lifecycle log no longer rejects the enclosure: the demotion test is now
`if lifecycle is not None and (terminal or non-provider-phase): continue`, so only a
*present* log that is genuinely terminal or past the provider phases demotes the stack —
a pruned log leaves the durable enclosure admitted. The returned values are worktree group
basenames, matching provider-runtime file layout and the served `ProviderNode.worktreeGroup`.

`active_enclosure_worktree_groups(enclosures, lifecycle_logs, *, now)` uses the
same lifecycle map but keeps any enclosure whose cleanup is not archived
(`ARCHIVED_CLEANUP_STATES = {"completed", "abandoned"}`). Its terminal check is likewise
`if lifecycle is not None and terminal: continue` — a missing log keeps the group live. This
was the Engine Room regression: a running worktree vanished an hour after its last lifecycle
event because the log it keyed on had been pruned for inactivity. Projection uses this broader
set to avoid git-probing engine facts for historical enclosures while still showing active
close/integration work.

`series_retained_lifecycle_ids(enclosures, *, now)` is the inverse — the durable-state retention
that supersedes the inactivity TTL. It groups leaf enclosures by master series (`(repoName,
taskName)`), and for every series that is **not** retired, returns *all* of its leaves'
`lifecycleId`s. `_series_is_retired(group, *, now)` is true only when every leaf is archived
(cleanup in `ARCHIVED_CLEANUP_STATES`) **and** the most recent leaf contract's finalize time is
older than the one-week grace (`MASTER_ARCHIVE_GRACE_SECONDS`); a fully-archived series whose
contract timestamps are unreadable is released immediately. `_contract_finalized_at(contract_path)`
reads the leaf contract's file mtime (its finalize/cleanup stamp) as that grace anchor, returning
`None` when unreadable. Enclosures without a `lifecycleId` or `taskName` (fleeting/standalone) are
never returned here, so they keep the ordinary inactivity TTL.

`_project_lifecycle_map` is the shared fold helper; `_enclosure_is_provider_relevant`
(cit:([`_enclosure_is_provider_relevant`], mcp/src/agents_remember/observer/worktree_provider_admission.py:147-154)) is the provider-specific contract-status gate — it rejects an enclosure with no
`lifecycleId` or no `worktreeGroup`, then an archived one, then a closeout- or
integration-completed one.

Since 260731-EFA-L4 that archived check reads the module constant:
`if enclosure.cleanup in ARCHIVED_CLEANUP_STATES:` (cit:([`ARCHIVED_CLEANUP_STATES`], mcp/src/agents_remember/observer/worktree_provider_admission.py:18-18)).
The provider gate, `active_enclosure_worktree_groups`, and `_series_is_retired` cite that shared
vocabulary in their implementation bodies (cit:([`admitted_worktree_groups`, `active_enclosure_worktree_groups`, `_series_is_retired`], mcp/src/agents_remember/observer/worktree_provider_admission.py:24-45; mcp/src/agents_remember/observer/worktree_provider_admission.py:48-73; mcp/src/agents_remember/observer/worktree_provider_admission.py:104-118)).

### Conventions

The module receives already-read `EnclosureNode`s and lifecycle event logs. It
does not read contracts, provider-runtime files, or observer logs itself; those
remain owned by `snapshots.py` and `projection_store.py`.

### Invariants And Boundaries

- Provider alarms are admitted before provider nodes reach the reducer; the reducer
  still treats admitted provider failures as real.
- Worktree provider-state files alone are not operational truth.
- **The durable enclosure contract — not the lifecycle event log — decides liveness.** A missing
  log (pruned for inactivity) never retires a live enclosure from either admission set; only a
  *present*, genuinely terminal/post-phase log demotes it.
- **A live master series protects its whole history.** `series_retained_lifecycle_ids` returns every
  leaf id of any non-retired series; a series retires only when all leaves are archived AND the
  one-week grace past the last finalized contract has elapsed. This set is what the projection store
  hands to `event_retention.prune_expired_lifecycle_event_logs` as `protected_lifecycle_ids`.
- Series grouping ignores enclosures with no `taskName`/`lifecycleId`, so fleeting/standalone work is
  never series-protected.
- Engine-process admission is intentionally broader than provider admission so
  non-terminal close/integration work can stay visible without paging provider alarms.
- **One archived-cleanup vocabulary, three readers.** cit:([`ARCHIVED_CLEANUP_STATES`], mcp/src/agents_remember/observer/worktree_provider_admission.py:18-18) declares the shared cleanup vocabulary; the provider gate, the
  active-enclosure set and `_series_is_retired` (cit:([`admitted_worktree_groups`, `active_enclosure_worktree_groups`, `_series_is_retired`], mcp/src/agents_remember/observer/worktree_provider_admission.py:24-45; mcp/src/agents_remember/observer/worktree_provider_admission.py:48-73; mcp/src/agents_remember/observer/worktree_provider_admission.py:104-118)) are the cited readers.
- Group joins always use the worktree group basename.

### Todos

No file-local todos.

## Docs References

No relevant external documentation was found after checking the in-repo design docs.
This file implements repository-local worktree lifecycle admission policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found after checking in-repo design docs for active-enclosure admission. | n/a | n/a |

## Repo-Internal References

The projection store consumes both admission sets: strict provider groups for
provider/setup readers and broader active enclosure groups for Engine Room facts.
Focused projection tests pin active provider admission, parked/terminal/provider-phase
rejection, and close-phase Engine Room visibility.

| Finding | Anchor | Source |
| --- | --- | --- |
| Provider admission joins enclosures and rejects only a *present* terminal/non-provider-phase log — a missing (pruned) log leaves the durable enclosure admitted. | `admitted_worktree_groups` | mcp/src/agents_remember/observer/worktree_provider_admission.py:24-45 |
| The archived-cleanup vocabulary is declared once. | `ARCHIVED_CLEANUP_STATES` | mcp/src/agents_remember/observer/worktree_provider_admission.py:18-18 |
| Active-enclosure groups keep any non-archived enclosure live; a missing log never drops the group (the Engine Room disappearing-worktree regression). | `active_enclosure_worktree_groups` | mcp/src/agents_remember/observer/worktree_provider_admission.py:48-73 |
| A non-retired master series retains all its leaf lifecycle ids; retirement requires every leaf archived AND the one-week grace past the last finalized contract mtime. | `series_retained_lifecycle_ids`; `_series_is_retired`; `_contract_finalized_at` | mcp/src/agents_remember/observer/worktree_provider_admission.py:76-101; mcp/src/agents_remember/observer/worktree_provider_admission.py:104-118; mcp/src/agents_remember/observer/worktree_provider_admission.py:121-127 |
| The projection store reads enclosures first, then passes `series_retained_lifecycle_ids(...)` as the retention `protected_lifecycle_ids`. | `project_and_write` | mcp/src/agents_remember/serving/projections/projection_store.py:212-275 |
| Retention honors that protection set, exempting protected logs from inactivity pruning. | `prune_expired_lifecycle_event_logs` | mcp/src/agents_remember/observer/event_retention.py:73-107 |

## Cross-Repo References

No meaningful cross-repo references found. This is an internal observer admission
boundary over local coordination state.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: deduplicated the lifecycle-retention admission
  reference onto `series_retained_lifecycle_ids`, `_series_is_retired`, and `_contract_finalized_at`,
  and narrowed the shared-vocabulary row to its declaration.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-02T16:56+02:00 — 260731-EFA-L6 curator W1-B06: anchored 7 citation claims
  (6 Logic/History citations and 1 Repo-Internal reference row); scoped result 0 findings.

- 2026-08-01T00:52+02:00 — 260731-EFA-L4 curator: the card named `ARCHIVED_CLEANUP_STATES` only
  as `active_enclosure_worktree_groups`' rule and described `_enclosure_is_provider_relevant`
  as "the provider-specific contract-status gate" without saying that it carried its own
  hand-written `{"completed", "abandoned"}` copy of the same vocabulary. Verified against the
  diff: the literal at L152 is now `if enclosure.cleanup in ARCHIVED_CLEANUP_STATES:`, so the
  constant at L18 is the single owner for all three readers that consult it (L67, L106, L152).
  Corrected the Logic paragraph, added the line ranges for `_enclosure_is_provider_relevant`
  (cit:([`_enclosure_is_provider_relevant`], mcp/src/agents_remember/observer/worktree_provider_admission.py:147-154)), added an invariant naming all three call sites, and added a reference row. The two
  existing self-reference rows carry symbol names rather than line ranges and were re-checked
  against the current source — `admitted_worktree_groups` L24, `active_enclosure_worktree_groups`
  L48, `series_retained_lifecycle_ids`/`_series_is_retired`/`_contract_finalized_at` all still
  present — so nothing else moved.
- 2026-06-30T00:00:00+02:00 — L5 (260628_operations-integration): made admission resilient to a pruned lifecycle log
  (a MISSING log no longer retires a live enclosure in either `admitted_worktree_groups` or
  `active_enclosure_worktree_groups` — the durable enclosure is the source of truth; this fixed a
  running worktree disappearing from the Engine Room an hour after its last event). Added
  `series_retained_lifecycle_ids` / `_series_is_retired` / `_contract_finalized_at` and the
  `ARCHIVED_CLEANUP_STATES` / `MASTER_ARCHIVE_GRACE_SECONDS` constants so a not-yet-retired master
  series protects every leaf's event log from the inactivity TTL (retire = all leaves archived + a
  one-week grace from the last finalized contract). Updated Purpose, Logic, Invariants, and
  Repo-Internal References. Verification metadata pinned until closeout stamps the L5 code commit.
- 2026-06-28T05:38+02:00 — Created for task 29: extracted worktree-scoped provider
  admission and broader active-enclosure group derivation so stale provider-runtime
  files and historical enclosure contracts do not page or slow the dashboard. Verification
  metadata pinned until closeout stamps the task-29 code commit.
