# mcp/tests/test_codex_adapter_thread_demux.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_adapter_thread_demux.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash |  `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Async observation helpers for Codex adapter consumers.

## Code Commentary

### Logic

eventually yields for a bounded number of turns before failing; live_snapshot requires a real current adapter snapshot; agent_registry reads the registry from that snapshot. An AnyIO fixture selects asyncio. No demultiplexing or queue tests remain in this file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Comments about historical matrices are not retained protection. These helpers observe a live test adapter without starting a vendor process themselves.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Eventually. | `eventually` | mcp/tests/test_codex_adapter_thread_demux.py:22-27 |
| Live snapshot. | `live_snapshot` | mcp/tests/test_codex_adapter_thread_demux.py:30-35 |
| Agent registry. | `agent_registry` | mcp/tests/test_codex_adapter_thread_demux.py:38-39 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-07T23:35:00+02:00 — 260731-EFA-L7 curator (trace delta): body verified against the current code and updated (260731-EFA-L7 (trace delta): the thread-demux suite now anchors against the `codex_app_server_adapte...). Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-03T11:10+02:00 — 260731-EFA-L6 W3-B07 curator: repaired 8 of 8 retained citation findings (6 table anchor/source findings and 2 prose citations). Deleted the external Codex vendor-suite row (2 diagnostics) under the max-reviewer 2026-08-02 14:10 disposition because its source is outside the frozen roots.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: the `PLR0913` pass reached the wire fixtures, so
  the collab-frame call shape and every line citation in this card were re-derived from the current
  source. `collab_agent_tool_call_item` no longer takes `sender_thread_id=`, `receiver_thread_ids=`
  and `agents_states=`; those three vendor thread fields are now one `CollabAgents` parameter object
  passed as `agents=`, and the card names it where it describes
  `test_collab_items_bind_agent_identity_into_the_registry`. Adding that import shifted the whole
  import block, so the four Repo-Internal References ranges were corrected (fixtures L17-L30 to
  L16-L29, adapter L31-L35 to L30-L34, models L37-L42 to L36-L41, shared seam L43-L51 to L42-L50),
  each re-read at its new position. All eighteen per-test anchors were likewise recomputed against
  the current file and now cite each test from its `def` line to its last body line; most of that
  correction is older drift this leaf merely exposed, since the anchors were already several lines
  off at the L2 base commit and the leaf itself only moved lines by one before the collab test and
  three after it. No assertion, decline path, degrade reason, bound, or ordering claim changed —
  the emitted wire shape is identical, so every behavioural claim in this card still holds.
  Verification metadata stays pinned until closeout stamps the code commit.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: updated the thread-demux native-page
  coverage record for items-first runtime probing and exact parent/child request selection.
  Verification metadata remains pinned while uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the nine new remediation
  tests — concurrent parent server requests answered per id with the oldest in the
  singular slot, the method-first degrade split (experimental/unknown methods decline +
  degrade on the parent, known-method malformed shapes and boolean rpc ids still fail
  loud), the bounded pending map declining only the newest request, and the load-shed
  queue pins (delta flood sheds oldest deltas with structural completions surviving, the
  consumer-side notice mint, and the notice-before-close-sentinel ordering). Refreshed
  the import-block citations (cit:(["class CodexAppServerAdapter:", "class FakeCodexTransport:"], mcp/src/agents_remember/serving/codex_app_server_adapter.py:104-104; mcp/tests/test_codex_app_server_adapter.py:47-47)) and the per-test anchors. Verification metadata
  stays pinned — the change is uncommitted.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: created the sidecar for the new
  thread-demux incident-regression suite (R1; review R5 degrade/registry-eviction pins).
  Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
