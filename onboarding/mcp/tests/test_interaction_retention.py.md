# mcp/tests/test_interaction_retention.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_interaction_retention.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T14:20+02:00                     |
| lastVerifiedCommitHash | `a714114ef94eedb8042fb4caa38d9469f4767dd6`|
| lastVerifiedCommitDate | 2026-08-01T18:06:36+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused backend tests for the gate/operator-inbox interaction-retention policy.

## Code Commentary

The tests cover two behavior seams added for task 23/24. The projection case writes pending
operator-inbox entries and asserts `read_agent_pickups` returns `waiting-for-agent` before the
5-minute pickup TTL and `check-chat` after it.

The gate case is `test_an_open_gate_past_24h_leaves_the_projection_then_leaves_the_log`
(L30-L75), and 260731-EFA-L5 split it into **two proven claims where there had been one**. It is
worth reading as the exception among that leaf's five updated suites: everywhere else the change
was "assert emptiness instead of absence", and here that would have been the wrong repair.

Before the leaf this test read `read_gates` — the dashboard projection — and then asserted the
gate log itself was empty. The second assertion held only because the projection tick
**physically rewrote every gate log as a side effect of rendering**, and that rewrite is precisely
what L5 removed: it ran in the process that owns nothing here, racing the MCP server's appends,
and it is where the measured 11.50% loss of appended gate snapshots came from. So the assertion
was never about absence in the first place — it was reading a side effect. Restating it as
emptiness would have restated the removed behaviour, because after a projection the snapshot is
now legitimately still on disk.

The two claims are therefore proven separately, against the owner of each:

- **The projection is non-destructive**, which is new and had never been asserted. The aged-out
  gate leaves the rendered set (`gates == []`), and the log is byte-identical afterwards
  (`log.read_bytes() == before`) with the record still readable through the strict
  `store.read("L1")`. Reading changing nothing is the contract the projection acquired in this
  leaf, and this is where it is held.
- **Compaction is what empties the log**, run by its owner: `store.compact("L1", now=now)` reports
  removing exactly `1`, the strict read comes back empty, and — R5 — the log `is_file()` with
  `read_bytes() == b""`. Emptied, never unlinked: an appender holding that path open must not be
  left writing into an inode that no longer has a name.

The pair is strictly stronger than the claim it replaces, because zero bytes read back through the
strict reader proves the records physically left rather than that a file disappeared.

## Invariants And Boundaries

- Retention tests cover throwaway interaction data only; tasks, contracts, and ledger
  rows are intentionally outside this policy.
- The pickup projection test uses an explicit clock so UI TTL state is backend-owned.
- The projection must stay read-only. If `read_gates` ever rewrites again, the
  `log.read_bytes() == before` assertion is what fails, and it fails for the right reason.
- Reclamation is asserted through the owning process's entry point (`GateStore.compact`), never
  as a side effect of a read.
- An emptied log stays a file. `assertFalse(path.exists())` is the shape this leaf removed and
  must not come back.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Retention constants and policy helpers under test. | `INTERACTION_RECORD_TTL_SECONDS`, `gate_keep_ids` | [controlplane/interaction_retention.py](agents-remember/mcp/src/agents_remember/controlplane/interaction_retention.py) |
| The compaction the test now drives directly, and the strict read it checks the result with; `_replace` routes through the contract's rewrite, which never unlinks. | `compact`, `read`, `_replace` | [controlplane/store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| The rewrite that makes "emptied, not unlinked" true for every store at once: an empty record set is written as an empty file. | `rewrite_lines` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The projection this test now asserts is non-destructive, and its own record that the 30 s physical prune was removed because it ran in a process that owns nothing here. | `read_gates` L514-L537 | [observer/snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |
| Agent-pickup projection exercised by the state test. | `read_agent_pickups` L553-L589 | [observer/snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |
| The suite that measures the loss this test's removed rewrite was causing, across all six stores and against the leaf's base commit. | L97-L168; L270-L310 | [test_controlplane_store_durability.py](agents-remember/mcp/tests/test_controlplane_store_durability.py) |

## Update History

- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator: this file is the **exception** among the leaf's
  five updated suites and the card now says so. `test_read_gates_prunes_open_gates_after_24h`
  became `test_an_open_gate_past_24h_leaves_the_projection_then_leaves_the_log` (L30-L75), and the
  reason is not the one that applies to the other four. Its `store.read("L1") == []` assertion was
  never a claim about absence: it passed only because the base commit's `read_gates` physically
  rewrote every gate log on the projection tick (`store.compact_current(..., rewrite=prune)`),
  which is the behaviour this leaf removed — the reclaim pass running in the process that owns
  nothing here, racing the MCP server's appends, and the source of the measured **11.50%** loss of
  appended gate snapshots. Restating it as emptiness would therefore have restated the removed
  behaviour, since a projection now legitimately leaves the snapshot on disk. The test instead
  proves two things where it proved one: the projection leaves the log **byte-identical**
  (`log.read_bytes() == before`, with the record still readable through the strict read) — a
  non-destructiveness claim that had never been asserted anywhere — and `GateStore.compact`, in
  the owning process, is what takes the record off disk, reporting `1` removed, reading back
  empty, and leaving the log `is_file()` with `read_bytes() == b""` (R5: emptied, never unlinked,
  so a concurrent appender is not left writing into a nameless inode). Rewrote Purpose and Code
  Commentary accordingly, added four invariants (projection stays read-only; reclamation is the
  owner's entry point, not a read side effect; an emptied log stays a file;
  `assertFalse(path.exists())` must not come back), and re-pointed `governingOverview` and the
  Governing Overview backlink from `../overview.md` to the route-local `overview.md`, which is the
  file that actually exists in this memory tree. Verification metadata is pinned until closeout
  stamps the L5 commit.

- 2026-07-31T16:50+02:00 — No content impact: the only change 260731-EFA-L2 made to
  `mcp/tests/test_interaction_retention.py` is the `PLR0913` parameter-object pass rewriting the two
  fixture-construction call sites. `create_gate` now takes its kind positionally with
  `anchor=GateAnchor(lifecycle_id="L1")`, and `create_operator_inbox_entry` takes
  `InboxMessage(ask=…, response=…, gate_id=…)` positionally plus `routing=InboxRouting(...)` and
  `poster=InboxPoster(...)` in place of nine loose keywords; the import block grew to name those
  objects. Checked that the seeded rows carry the same values as before, that no assertion line was
  touched, and that this card names none of those constructors, keywords, or field names — it
  describes only the two behaviours, both of which still read exactly as written: the TTL case still
  asserts compaction empties the gate store past the 24-hour interaction TTL
  (`test_read_gates_prunes_open_gates_after_24h`), and the projection case still asserts
  `read_agent_pickups` returns `waiting-for-agent` for the fresh entry and `check-chat` for the
  stale one. This card carries no line citations, so nothing needed re-anchoring.

- 2026-06-25T13:20+02:00 — Created for task 23/24 TTL compaction and agent-pickup projection coverage.
