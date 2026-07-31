# mcp/tests/test_interaction_retention.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_interaction_retention.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-25T13:20+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[mcp tests overview](../overview.md)

## Purpose

Focused backend tests for the gate/operator-inbox interaction-retention policy.

## Code Commentary

The tests cover two behavior seams added for task 23/24. The gate-store TTL case
creates old interaction records and asserts compaction physically removes rows past
the 24-hour interaction TTL. The projection case writes pending operator-inbox
entries and asserts `read_agent_pickups` returns `waiting-for-agent` before the
5-minute pickup TTL and `check-chat` after it.

## Invariants And Boundaries

- Retention tests cover throwaway interaction data only; tasks, contracts, and ledger
  rows are intentionally outside this policy.
- The pickup projection test uses an explicit clock so UI TTL state is backend-owned.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Retention constants and policy helpers under test. | [controlplane/interaction_retention.py](agents-remember/mcp/src/agents_remember/controlplane/interaction_retention.py) |
| Gate store compaction exercised by the TTL test. | [controlplane/store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| Agent-pickup projection exercised by the state test. | [observer/snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py) |

## Update History

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
