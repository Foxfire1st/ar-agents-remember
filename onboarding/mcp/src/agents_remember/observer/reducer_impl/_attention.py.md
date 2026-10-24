# mcp/src/agents_remember/observer/reducer_impl/_attention.py

## Governing Overview

[overview](../overview.md)

## Purpose

Pure deterministic attention ranking — newest first, with every row acknowledged on the same terms — over actionable drift and blocked-start occurrences and the five native kinds — permission wait, held message, stalled task, landed notice, abandoned notice — that `_attention_native.py` builds from the task, host, held-store and terminal facts of the pass, with no provider or setup builder and no session-stale/lifecycle alarm builder.

## Code Commentary

`build_attention_queue` sorts by age and ID — youngest first, so the newest entry is on top, and an entry with no age counts as zero (:79-80) — and folds every row against matching current acknowledgements, with no class exempt: a live native cause can be acknowledged like a notice, and dismissing it changes nothing at its cause (v2 rule 7). Blocked starts end through complete native-reader recovery/removal proof; unknown health or a missing projected node is not recovery. Drift uses actionable fingerprints: equal or missing fingerprints preserve acknowledgement; changed complete findings can resurface. A later timestamp alone is not a new occurrence. Worktree debt remains independently operational, not a synthesized session status.

### 20261023-L190-v2 Newest First, And No Row Above The Acknowledgement

The queue's total order is `(waitSeconds or 0.0, item.id)` (:80). Rule 1's severity ordering is withdrawn with `_SEVERITY_RANK`; severity stays on the row, unranked, so the bell can still name the highest one served. `waitSeconds` is the age the row already carries, so an age-only tick re-orders nothing and `diff_projection` still emits nothing.

The dismissal fold (:79) no longer asks whether a row is dismissible. Rule 7 makes the acknowledgement the only thing that hides a row, and `itemClass` only says how the occurrence also ends. The module still owns the one fold: nothing here infers recovery from age, a missing node or a vanished acknowledgement.

## Evidence boundary

This account is current source interpretation only. It creates no executed test/host/bootstrap result and supplies no new CODE or MEMORY grade.
