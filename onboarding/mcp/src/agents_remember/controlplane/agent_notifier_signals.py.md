# mcp/src/agents_remember/controlplane/agent_notifier_signals.py

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/controlplane/agent_notifier_signals.py`   |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated | 2026-08-11T09:50+02:00 |
| lastVerifiedCommitHash |                                                                `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |                                                                2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                  |

## Governing Overview

[overview.md](overview.md)

## Purpose

Persists agent-notifier cooldown evidence using structural owner identity plus private occupant
correlation. It prevents repeated delivery without making a runtime id the durable address.

## Code Commentary

### Logic

The record and target carry task-document reference, role, and optional current agent/lifecycle
correlation. Cooldown equality compares the full routed target plus finding kind/detail. The store
reads once per sweep, appends under declared ownership, and compacts bounded history.

### Conventions

Task document and role express the owner seat; agent and lifecycle ids are delivery evidence for the
current occupant.

### Invariants And Boundaries

- Replacement changes private correlations without changing the structural owner.
- Cooldown never matches a partial target.
- This log is delivery suppression evidence, not inbox authority.

### Todos

The retained legacy log filename is removed only with its governed durability migration.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Cooldown records carry structural and private correlation fields separately. | `AgentNotifierSignalRecord` | mcp/src/agents_remember/controlplane/agent_notifier_signals.py:33-49 |
| Target equality includes the full routed seat and finding. | `AgentNotifierSignalKey` | mcp/src/agents_remember/controlplane/agent_notifier_signals.py:64-71 |
| The store bounds and serializes cooldown evidence. | `AgentNotifierSignalCooldownStore` | mcp/src/agents_remember/controlplane/agent_notifier_signals.py:74-181 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current control-plane card for `agent_notifier_signals.py` with plane-owned seat identity, routing, and enforcement boundaries.
- 2026-08-10T09:45+02:00 — 260731-EFA-L9 curator repair: refreshed the renamed signal-store card and L9 primitive path.


- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded the `AgentNotifierSignal*` identifiers and the retained durable names (`ar-supervisor-signal/v1`, `supervisor-signals.jsonl`, `store="supervisor-signals"`) with their migration removal point. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-03T02:46:27+02:00 — W3-B05 curator: anchored 5 Tier-2 table citations and 1 Tier-2 prose citation with exact source paths; fixer generated all ranges.
- 2026-08-01T20:15+02:00 — 260731-EFA-L5 curator (correction pass). **One stale citation and one
  unsourced number.** The `AGENT_NOTIFIER_SIGNAL_OWNERSHIP` row cited `durable_store.py`
  **L327-L336**; the constant is at **L398** — the file grew 598 → 699 lines mid-pass, so every
  range written earlier is off. Replaced with a symbol-name citation and no range. Re-read the three
  citations into this module's own source and left them: `AgentNotifierSignalRecord` (cit:([`AgentNotifierSignalRecord`], mcp/src/agents_remember/controlplane/agent_notifier_signals.py:30-46)), the path/read/append row L83-L107 (`log_path` L83, `read` L86, `append` L103), `last_sent` /
  `in_cooldown` L109-L155 (L109, L131), and `compact` L157-L213 (L157, `_compact_locked` L178,
  `_replace` L206). The **10.50 percent** figure is now attributed rather than asserted: it appears
  only in the `durable_store.py` docstring, which is also the only place 10.20, 9.20 and 0.00 appear
  — unlike the 31.45 percent this card also quotes, which four independent files carry. Removed the
  "never torn" assertion about the base commit: `torn_lines == 0` is asserted by
  `test_controlplane_store_durability.py` against the **current** tree, not the base commit, and no
  recorded base-commit run is stored anywhere in the tree. This card's read-policy statements were
  already correct — it says plainly that `_compact_locked` reclaims from the tolerant read and that
  compaction therefore drops an unparseable cooldown row — and were left unchanged.
- 2026-08-01T18:30+02:00 — 260731-EFA-L5 (durable store integrity). Recorded the 10.50 percent
  measured loss and the routing of all file I/O through `durable_store.py` under
  `AGENT_NOTIFIER_SIGNAL_OWNERSHIP` (dashboard as sole writer and compaction owner): `append` checks
  the declared writer and locks, `compact` holds one lock across the new `_compact_locked`
  read-filter-rewrite half, `_replace` delegates to `rewrite_lines` and no longer unlinks an
  emptied log, and `AgentNotifierSignalRecord` now inherits `DurableRecord` for `extra="forbid"` plus
  a validated `schemaVersion`. Recorded why a single-writer store is still locked unconditionally
  and that its twin measured 31.45 percent when a draft trusted the single-writer claim. Stated
  that the tolerant read drives this store's rewrite, so compaction drops an unparseable cooldown
  row, and that the failure mode is fail-open. Corrected the Todos section, which still described
  this store as an unbounded log with no compactor after HFX2-L13 added `compact` — a contradiction
  with this card's own HFX2-L13 section. Repaired six citations: three intra-file ranges the leaf
  moved, one row that carried only two cells in a three-column table, and two pre-existing
  cross-file ranges that pointed at unrelated code (`_signal_emit` is at
  `serving/supervisor.py` L850, not L701-L747; the `AgentNotifierSignalCooldownStore` import is at
  `serving/app.py` L81, not L70). Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `AgentNotifierSignalTarget` and `AgentNotifierSignalKey`, and re-signed
  `last_sent(signal, *, records=None)` and `in_cooldown(signal, *, now, cooldown_seconds,
  records=None)` onto the key. `in_cooldown` now forwards the whole key to `last_sent` in one
  argument, so the two can no longer compare on different field sets — the L17 seat-role identity
  is part of the key by construction rather than by both call sites remembering to pass it.
  Matching semantics are unchanged. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: extended persisted cooldown identity with seat role so
  different seats on one leaf do not suppress one another.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: created for the new persisted supervisor signal
  cooldown store, including the known unbounded-log/no-compactor limitation tracked for HFX2-L11.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L9 commit.
