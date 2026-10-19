# mcp/src/agents_remember/serving/intent_summary_cache.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Reuse native intent summaries only through an app-owned dependency-observed ChangesetCache.

## Code Commentary

The port supplies initial inputs and a native reader that reports resolved dependencies. The cache key includes repository/master/leaf. Production resets observed dependencies on each native read; unavailable results also observe initial repository object stores so later object availability can invalidate reuse. A newly discovered repository outside initial inputs prevents retention until another complete read; additional resolved inputs participate in validation. The response serializes the typed native result without inventing counts. The response wrapper owns conditional HTTP behavior; this adapter does not authorize paths or promise an atomic whole-workspace snapshot. retained_inputs counts retained intent-summary keys, not filesystem dependency records.


## Current Behavior

the summary's `cached_read` now passes `Retention(keep=..., unknown=lambda result: result.state == "unavailable")` (`:72-83`). A refused summary may settle while Git cannot describe the working view (the `UNKNOWN_STATUS` stamp); a counted summary may not. The adapter still owns the summary key, its initial/resolved observations and the `unavailable` object-store observation; the app-owned cache owns the bound and admission. This adds the unknown-status condition to the earlier 'reuse only through ...' account; it does not make a cancelled or unknown summary reusable as a counted answer.

## Evidence

- Configurable dependency-observing port. [1]
- Native production, additional dependencies and retention condition. [2]
- Conditional response owner and retained-key diagnostic. [3]

## 260928-MIK-L177 The Age Window Is In The Key, Not In An Admission Record

The finite age bound is now `int(self._clock() // self._max_age_seconds)` and nothing else: `_window`
mints it and `_response` puts it in the cache key. The key therefore moves by itself when the window
rolls over, and no admission record can mint an old key again — the earlier form decided the epoch by
reading `self._kept`, so a record evicted by the admission table made the next read answer with the
epoch the *old* answer was still stored under. `_kept` remains as a bounded record of the last windows
per question, for inspection only. `max_age_seconds <= 0` falls back to the default.
