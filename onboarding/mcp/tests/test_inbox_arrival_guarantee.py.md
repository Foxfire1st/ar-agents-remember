# mcp/tests/test_inbox_arrival_guarantee.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_inbox_arrival_guarantee.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T14:29+02:00 |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32` |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The R7 regression-matrix forcing suite for 260713-TES-L4 (25 test methods): two simultaneous
repository architects resolve by repo+sprint scope (never global first-match); replacement
mid-flight reaches the successor at POST time; owner-address derivation branches (role-only,
unknown/existing seats, lifecycle addresses, peer preservation); explicit supersession is
terminal, visible, and skipped by every retry/evaluation path; terminal markers are
inspectable via `include_terminal` (N11); pending rows past the retention boundary resolve
`expired` before compaction and the 500-row cap drops terminal-oldest-first with counted
drops (D4/§9); the notifier loop survives bad settings reads with last-good configuration
(R7/N5); the relay-death watcher posts once per stale heartbeat identity (N5); and
`session_retire` surfaces stranded rows to the retiring authority without refusing (N2). All
tests were red before implementation and drive the production sweep/tool surfaces.

## Code Commentary

### Logic

- `ScopedArchitectCustodyTests` cit:([`ScopedArchitectCustodyTests`], mcp/tests/test_inbox_arrival_guarantee.py:94-175) — two simultaneous repository
  architects resolve by their binding scope; an exact-leaf architect wins within its master;
  global first-match is never a fallback (R13).
- `PostTimeOwnerRebindingTests` cit:([`PostTimeOwnerRebindingTests`], mcp/tests/test_inbox_arrival_guarantee.py:177-229) — a message addressed to a retired
  manager reaches the same-leaf+role replacement at post time without a new post (N14).
- `PostTimeAddressBranchTests` cit:([`PostTimeAddressBranchTests`], mcp/tests/test_inbox_arrival_guarantee.py:232-332) — role-only owner addresses resolve to
  the current manager; unknown seat and lifecycle addresses resolve to the derived owner;
  existing owner seats resolve without a role hint; peer-worker and non-owner lifecycle
  addresses are preserved verbatim; the empty-address helper returns false.
- `ExplicitSupersessionTests` cit:([`ExplicitSupersessionTests`], mcp/tests/test_inbox_arrival_guarantee.py:335-400) — `operator_inbox_supersede` is terminal,
  visible in poll with `include_terminal`, and skipped by retry; poll defaults to pending-only
  (R11/N11).
- `TtlAndCapEvictionTests` cit:([`TtlAndCapEvictionTests`], mcp/tests/test_inbox_arrival_guarantee.py:403-510) — a pending row past the retention
  boundary resolves `expired` before compaction; the cap drops terminal markers oldest-first
  and surfaces the drop counts (D4/§9).
- `SettingsResilienceTests` cit:([`SettingsResilienceTests`], mcp/tests/test_inbox_arrival_guarantee.py:513-555) — the sweep keeps last-good settings
  after a failed read, fails loud per tick, and never dies; with no last-good it skips and
  retries (R7/N5).
- `RelayDeathWatchTests` cit:([`RelayDeathWatchTests`], mcp/tests/test_inbox_arrival_guarantee.py:558-624) — a never-ticked heartbeat is silent; a stale
  heartbeat posts once per tick identity and re-arms on a fresh tick; corrupt marker content
  reads as none; settings failure falls back to the default cutoff; delivery failure is
  best-effort (N5).
- `RelayDeathLoopTests` cit:([`RelayDeathLoopTests`], mcp/tests/test_inbox_arrival_guarantee.py:627-651) — the watcher loop runs the check on its
  independent cadence and continues after failures.
- `RetireSurfacingTests` cit:([`RetireSurfacingTests`], mcp/tests/test_inbox_arrival_guarantee.py:654-736) — `session_retire` surfaces stranded pending
  rows to the retiring authority and still succeeds; no pending rows means nothing surfaced
  (N2).

### Conventions

Simulation-harness style shared with the L2/L3 relay suites: temp-rooted stores, fake catalog
rows, injected clocks, and production sweep/tool entry points (`run_agent_notifier_sweep`,
`post_operator_inbox_entry`, `deliver_inbox_entry`, `session_retire_tool`,
`relay_death_watch_loop`) rather than hand-aligned unit calls.

### Invariants And Boundaries

- A landed/superseded/unresolved/expired row produces no retry, nudge, or escalation ever
  (N16/R11).
- Supersession is always explicit — never inferred from artifacts, branches, or task state.
- Architect custody is scope-resolved with a role-only mailbox fallback; a second repository's
  architect can never capture another repo's rows.
- The relay-death watcher posts at most once per stale heartbeat identity and never relays its
  own death.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in the resolved `system/sources.md`; the
deliver-until-LANDED semantics are same-repository runtime behavior proven by source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this contract; the R7 matrix and the N-rulings are the authority. | `ScopedArchitectCustodyTests` | mcp/tests/test_inbox_arrival_guarantee.py:94-175 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The scoped custody resolver under test. | `derive_architect_owner` | mcp/src/agents_remember/controlplane/signal_routing.py:129-138 |
| The post-time re-resolution under test. | `_post_address`; `_is_owner_addressed` | mcp/src/agents_remember/serving/operator_inbox_posts.py:110-144; mcp/src/agents_remember/serving/operator_inbox_posts.py:176-193 |
| The supersede tool under test. | `operator_inbox_supersede_tool` | mcp/src/agents_remember/application/operator_inbox_tools.py:153-180 |
| The supersede transition under test. | `mark_superseded` | mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:265-293 |
| Terminal inspectability under test. | `list_for_mailbox` | mcp/src/agents_remember/controlplane/operator_inbox_store.py:160-187 |
| Retention/cap eviction under test. | `inbox_keep_ids`; `evaluate_pending_expiry_findings` | mcp/src/agents_remember/controlplane/interaction_retention.py:140-163; mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:175-198 |
| Last-good settings loop under test. | `_agent_notifier_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:108-140 |
| Relay-death watcher under test. | `post_relay_death_signal`; `relay_death_watch_loop` | mcp/src/agents_remember/serving/relay_death_watch.py:100-152; mcp/src/agents_remember/serving/relay_death_watch.py:167-174 |
| Retire surfacing under test. | `_surface_stranded_rows` | mcp/src/agents_remember/application/terminal_tools.py:1025-1095 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary participates in this suite. | — | — |

## 260713-TES-L5 Current Delta — Nudge Store Dropped From Context

The TTL/cap-eviction harness drops `OrchestrationNudgeStore` from the sweep context (the
sweep no longer owns a nudge store); the arrival-guarantee matrix itself is unchanged.

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T14:29+02:00 — Re-read post-time owner rebinding and regenerated the
  `_post_address`/`_is_owner_addressed` ranges around their current declarations; verification
  metadata remains unchanged for governed closeout.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged inbox-arrival guarantee harness; the existing assertions remain accurate. Verification metadata remains pinned until closeout.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the nudge-store removal from the
  TTL/cap harness context. Verification metadata pinned until closeout stamps the
  260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: created this file-level onboarding card for
  the new arrival-guarantee forcing suite (25 test methods: scoped custody, post-time
  rebinding, supersession, terminal inspectability, TTL/cap eviction, settings resilience,
  relay-death watch, retire surfacing). Verification metadata pinned until closeout stamps the
  260713-TES-L4 commit.
