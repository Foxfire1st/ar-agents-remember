# mcp/src/agents_remember/controlplane/interaction_retention.py

| Field                  | Value                                                                  |
| ---------------------- | ---------------------------------------------------------------------- |
| repository             | agents-remember                                                        |
| path                   | `mcp/src/agents_remember/controlplane/interaction_retention.py`        |
| doc_type               | `file-level-onboarding`                                                |
| lastUpdated            | 2026-08-01T19:45+02:00                                                 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                          |

## Governing Overview

[controlplane overview](overview.md)

## Purpose

Central retention policy for short-lived gate and operator-inbox interaction data.

## Code Commentary

### 260731-EFA-L5 R1 An `applied` Approval Is An Authority Record, Not Garbage

**`applied` is out of `PRUNE_IMMEDIATE_GATE_STATES`.** That set is now exactly
`{"cancelled", "expired"}`. This is one of the three reproduced ways a single human approval could
be spent twice, and it is the one that lived in this file.

For the kinds a server-side mutation consumes, the `applied` snapshot is the whole and only proof
that an approval was spent: `enforcement.evaluate_gate` refuses a second consume *solely* because it
finds one in the fold. Delete it and the fold returns to permitted-gateless — "no gate; existing
approval channel governs" — and the same approval buys a second mutation, with no error and no log
line. Until this leaf the pass below pruned `applied` **at any age**, so any later decision on the
lifecycle erased the marker within milliseconds (`controlplane/gate_decisions.py::_reclaim_gate_log` runs after
every decision, and an answered `agent-question` is enough). It was already wrong before this leaf —
the same states were pruned on the dashboard's 30s projection tick, so the marker survived at most
half a minute — and moving reclamation into the deciding process made it prompt and deterministic
rather than merely likely.

**`CONSUMED_APPROVAL_GATE_KINDS`** is the new set, built as `MUTATING_TOOL_GATE_KINDS |
SEAM_CONSUMED_GATE_KINDS`: the five mutating-tool kinds (`worktree-intent`, `closeout-approval`,
`push-approval`, `integration-approval`, `cleanup-approval`) plus `master-handover-approval`, the
master-exit seam gate `worktrees/modules/integrate.py` folds before it integrates. Only two of the
six are asked about today; being a superset costs nothing, because a kind nobody applies contributes
no records, and the test suite pins that every kind an enforcement path evaluates is in this set, so
adding an enforcement rung for one of the other four cannot silently outrun its retention.

**Open decision — `master-handover-approval` is in this set ahead of its consumer.**
`worktrees/modules/integrate.py` folds `all_current()`, evaluates `handover_gate_guard` and refuses
or integrates; it calls no `apply_gate` and no `claim_approval`, so nothing writes an `applied`
snapshot of this kind today. That is not a dropped record — the consume was never written on any
commit. It is left open because the claim would need a different key (the gate is matched
cross-lifecycle by `enclosure` and lives on a different log than the integrating lifecycle's) and
because closeout's `integration_reopen` path means a legitimate re-integration would start
requiring a fresh gate. `SEAM_CONSUMED_GATE_KINDS` exists now so the retention half is ready the
moment that consume is written; until then this entry retains nothing, because there is nothing to
retain.

**`_keep_gate` consults the authority branch before the clock.** The first thing it does is

> if the snapshot is `applied`, keep it iff its kind is in `CONSUMED_APPROVAL_GATE_KINDS`

with no reference to `now` or `ttl_seconds` at all. **There is no TTL here, deliberately.** A
retention window would be a guess about how long a human takes before retrying a closeout, and this
code has made that guess twice — 30 seconds, then zero — and was wrong both times. Growth is instead
bounded by the thing that actually bounds it: approvals a human granted and a mutating tool
consumed, a handful per lifecycle, in a log that lives beside that lifecycle's events. Everything
else keeps the retention it always had — withdrawn and superseded gates go immediately, live ones
age out on the 24-hour TTL.

**Every other kind's `applied` snapshot stays immediately prunable, and that is deliberate too.**
`agent-question` (applied by `serving/hosted_interactions.py` on every answered vendor interaction,
and unbounded in a long adapter session), `alarm-ack`, `provider-retry` and `plan-approval` are never
passed to `evaluate_gate`, so their `applied` record refuses nothing — it is pure history.

### 260731-EFA-L5 Why `cancelled` And `expired` Stay Prunable And `applied` Does Not

The asymmetry has a reason worth keeping, because "terminal state" alone does not explain it.
Dropping a gate's last snapshot returns `evaluate_gate` to the permitted-gateless verdict. For two
of these three that is the *intended* meaning; for the third it is the replay:

- **`cancelled` — the gate was withdrawn.** It never carried an approval, and cancelling it says
  precisely "this gate no longer governs", so falling back to the chat/commit approval channel is
  the correct outcome. Retention is not even what removes it in production:
  `application/gate_tools.py::gate_decide_tool` calls `GateStore.delete` on the record at the moment the
  cancel is recorded.
- **`expired` — the gate was superseded.** `expire_gate` is written only when a newer gate opens on
  the same lifecycle, so the replacement is in the *same log with a newer `ts`* and governs the fold.
  Dropping the expired snapshot drops history, never authority.
- **`applied` — the gate was granted and spent.** There is nothing to fall back to. The approval
  exists, it was consumed, and the only record saying so is this one.

### 260731-EFA-L6 Source-Path Alignment

This leaf did not change the retention policy; it changed where the paths this card names live.
`age_seconds` is now imported from `controlplane/stamps.py` instead of `observer/timeutil.py`
and is still the projection clock used by `_keep_gate`, `_keep_inbox_entry`, `pickup_state`,
and `pickup_age_seconds`. The two reclamation-path references above were corrected to
`controlplane/gate_decisions.py::_reclaim_gate_log` and
`application/gate_tools.py::gate_decide_tool`, matching the `controllers/` → `application/`
move. The authority-branch comment also dropped its closing sentence about why a count cannot be
wrong about human retry time; the retained bound is still "bounded by approvals granted and
consumed, with a cap (not a TTL) as the future escape hatch".

### 260712-TRH-L5 Confirmed-Gone Secondary Retention

`inbox_keep_ids` remains the final retention boundary after the supervisor's same-lock
confirmed-gone reconciliation. The 48-hour pending TTL and 500-row folded-current cap are
unchanged; `current=` lets the transaction reuse its single authoritative fold rather than
reading the append-only log again. Ladder-resolved snapshots, including the stable
`subject-session-confirmed-gone` reason, are still removed immediately by this policy.

### 260707-HFX2-L20 Monotonic Inbox Compaction

`inbox_keep_ids` uses the same monotonic fold as the live inbox store. Once a consumed or
ladder-resolved snapshot exists, a physically later pending snapshot produced by an in-flight
delivery cannot extend that row's pending retention or return it to the redelivery pool.

Defines the shared timing constants: `gate_response_wait` defaults to a 300-second wait and 5-second
poll cadence, ordinary consumed interaction records have a 24-hour TTL, pending inbox rows have a
separate hard 48-hour TTL, and task-row pickup feedback switches
from `waiting-for-agent` to `check-chat` after 300 seconds. `gate_keep_ids` and `inbox_keep_ids` take
validated records plus a projection clock and return the ids still worth keeping in compacted logs.
`delete_after_wait` distinguishes non-enforcement gates, which can be deleted after the wait tool
returns their decision, from worktree/closeout/integration/cleanup gates that a mutating tool still has
to consume/apply.

**HFX3 health-first supersession (developer ruling 2026-07-09)**: no inbox row outranks system
health. `_keep_inbox_entry` keeps a pending/unacked row only for
`INBOX_PENDING_TTL_SECONDS` (48 hours), drops `ladder-resolved` rows immediately, and applies the
ordinary 24-hour audit window to consumed rows. `inbox_keep_ids` then enforces
`INBOX_MAX_CURRENT_ROWS = 500`, keeping the newest rows when a producer exceeds the cap. If an
expired condition still holds, the supervisor may recreate one fresh coalesced row; the durable
record is the task/report/gate artifact on disk, never the notification row. This supersedes the
HFX2-L1 immortal-pending rule that contributed to the 2026-07-09 escalation storm.

## Invariants And Boundaries

- **An `applied` snapshot of a `CONSUMED_APPROVAL_GATE_KINDS` kind is never reclaimed, at any age.**
  It is the only proof a human approval was spent, and `evaluate_gate` refuses a replay solely
  because it is in the fold. Put `applied` back into `PRUNE_IMMEDIATE_GATE_STATES`, or add a TTL to
  the authority branch, and the replay window re-opens silently — no error, no log line.
- **This module is one of three closed defects, not the fix.** Retaining the record is necessary and
  not sufficient: the marker also has to survive a concurrent rewrite (`durable_store.py`'s lock)
  and the check-then-write has to be one step (`store.GateStore.claim_approval`). Durability of a
  record is not atomicity of a decision.
- **The retained set is bounded by grants, not by a clock.** Deliberately no TTL: the two clocks
  this code has tried (30 seconds, then zero) were both wrong, because a retention window is a guess
  about how long a human takes before retrying a closeout.
- This module owns policy only: stores perform the filesystem rewrite, tools decide when to call store
  deletion, and projection readers supply the clock for passive TTL cleanup.
- Interaction records are throwaway; durable task docs, contracts, ledgers, and closeout results remain
  outside this policy.
- Pending inbox rows are disposable notification state: they expire after 48 hours and the folded
  inbox is hard-capped at 500 current ids, newest-first.
- A `ladder-resolved` inbox row is neither pending nor acked; compaction drops it immediately.

## Update History

- 2026-08-11T19:58+02:00 — No content impact: reviewed the gate-model import move into the
  structural package; retention sets, authority preservation, and TTL behavior are unchanged.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T03:47+02:00 — 260731-EFA-L6 curator: aligned this card with the current source
  paths: `age_seconds` comes from `controlplane/stamps.py`, the deciding-process reclaimer is
  `controlplane/gate_decisions.py::_reclaim_gate_log`, and the cancellation deletion is
  `application/gate_tools.py::gate_decide_tool`. Retention policy (the `applied` authority
  branch, no-TTL bound, inbox 48h/500-row cap) is unchanged. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-08-01T19:45+02:00 — 260731-EFA-L5 (durable store integrity). This card carried **no** L5
  content and described a retention policy that no longer exists. Recorded: `applied` is out of
  `PRUNE_IMMEDIATE_GATE_STATES` (now exactly `{"cancelled", "expired"}`); the new
  `CONSUMED_APPROVAL_GATE_KINDS = MUTATING_TOOL_GATE_KINDS | SEAM_CONSUMED_GATE_KINDS` and why being
  a superset is free; that `_keep_gate`'s authority branch runs **before** the clock is consulted
  and takes neither `now` nor `ttl_seconds`; that there is **no TTL at all**, deliberately, because
  a retention window is a guess about a human's retry time and this code made that guess twice
  (30s, then zero) and was wrong both times, so growth is bounded by approvals actually granted and
  consumed. Recorded the asymmetry with its reason: dropping the last snapshot returns
  `evaluate_gate` to permitted-gateless, which is the *intended* meaning for a withdrawn gate
  (already deleted at decision time by `gate_decide_payload`) and a superseded one (its replacement
  is in the same log with a newer `ts`), but for a granted and spent gate there is nothing to fall
  back to. Recorded that every other kind's `applied` stays immediately prunable and why
  (`agent-question` and friends never reach `evaluate_gate`). Added the open decision that
  `master-handover-approval` sits in this set ahead of its consumer, since `integrate.py` never
  writes an `applied` for it. Added three invariants, including that this module is one of three
  closed defects and not the fix. Also corrected the `lastUpdated` field, which read
  `2026-07-31T00:00` while the newest history entry was `2026-07-31T16:35`. Verification metadata
  pinned until closeout stamps the L5 commit.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/controlplane/interaction_retention.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 6 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: documented the unchanged 48-hour pending TTL
  and 500-row cap as fallback retention and the pre-folded-current transaction seam used after
  confirmed-gone resolution. Verification metadata remains pinned until closeout stamps the
  candidate commit.

- 2026-07-10T22:18+02:00 — 260707-HFX2-L20: made inbox compaction use the shared terminal-dominant
  fold so stale in-flight delivery snapshots cannot resurrect pending retention.

- 2026-07-10T02:39+02:00 — HFX3 retro curation: replaced the superseded immortal-pending account
  with the reviewed health-first contract: 48-hour pending TTL, 500-row hard cap, newest-first
  eviction, immediate ladder-resolved reclamation, and artifact-not-row durability. Added the
  governing-overview backlink. Verification metadata remains pinned until closeout stamps the
  eventual two-parent code commit.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8: `_keep_inbox_entry` now drops `ladder-resolved` terminal
  rows during compaction while continuing to protect pending/unacked rows. Verification metadata
  pinned until closeout stamps the HFX2-L8 commit.
- 2026-07-08T14:10+02:00 — 260707-HFX2-L1: `_keep_inbox_entry` now keeps every `pending` row
  regardless of age (R1: compaction never removes an unacked row); the 24h TTL applies only to
  `consumed` rows. Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
- 2026-06-25T13:10+02:00 — Created for task 23/24 gate/inbox retention, wait defaults, and pickup TTLs.
