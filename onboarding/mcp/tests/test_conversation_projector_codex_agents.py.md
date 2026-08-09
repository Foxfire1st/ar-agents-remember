# mcp/tests/test_conversation_projector_codex_agents.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_projector_codex_agents.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-09T16:43+02:00                   |
| lastVerifiedCommitHash |  `2dea095cd68454a7a68893e37c07dbd8daa86d32`|
| lastVerifiedCommitDate | 2026-08-09T18:00:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Codex projector sub-agent mapping tests (R2/R5/R6): roster minting and
upserts from collab/activity evidence, demux-keyed live projection, multiplexed pending
interactions — including concurrent PARENT-thread pendings and the singular-slot rotation
semantics — per-thread native twin suppression, and the page-driven agent native backfill with
thread-scoped native ids; proving sub-agent work projects
into ONE per-seat cursor domain with an agent dimension, never into parent items and
never into fabricated identities.

## Code Commentary

### Logic

Two tiers drive the real mapper and projector engine. `CodexCollabMapperTests`
cit:([`CodexCollabMapperTests`], mcp/tests/test_conversation_projector_codex_agents.py:132-373) maps synthesized wire frames (built by `_agent_wire_fixtures`, parent thread
`vendor-1`) directly through `codex.map_evidence_frame`: a `spawnAgent` call stays the
parent's own untagged tool-call while minting a roster notice; a single-receiver
`sendInput` carries the agent ref but a multi-receiver `wait` does not; a terminal collab
roster carries the final-message block; `subAgentActivity` binds `agentPath` and
interrupted status into the same roster row; unknown collab/activity shapes degrade to
preserved `MappedUnknownVendor`; `thread/started` mints a registration only for a proven
non-parent (parent boot/resume is silent, and without the parent context the shape alone
mints nothing); agent-thread lifecycle frames drive roster status while an agent
`turn/completed` never feeds the parent-scoped status service.

cit:(["class CodexAgentEngineTests1(unittest.IsolatedAsyncioTestCase):"], mcp/tests/test_conversation_projector_codex_agents_engine_1.py:89-89) drives the real `ActiveSessionProjector` over a
`_MultiplexedBridge` (extends the `_ScriptedBridge` harness with per-thread native pages and
demux-keyed frames): the 2026-07-24 incident stream multiplexes into one contiguous
ordinal space with one upserted roster settled by the agent's turn completion, agent
items carrying the bound ref while parent items stay byte-identical (no agent dimension);
block-less lifecycle roster upserts never wipe the final message (fix-round finding 5);
plural `pending_interactions` project labeled and resolve per id while the singular
parent path is untouched; the selected-child backfill test
cit:([`test_selected_agent_backfills_content_when_live_delivery_is_partial`], mcp/tests/test_conversation_projector_codex_agents_engine_1.py:419-513) proves a partial
live delivery (roster and lifecycle crossed, the agent's content did not) is completed from
native authority — the content backfills thread-scoped (`{AGENT}:msg-1`) and agent-attributed,
the thread is marked walked once (`_agent_native_walked`) so later pages do not re-read it, and
a native `subAgentActivity` spawn record referencing ANOTHER agent mints no roster row (no
`codex-agent-other-agent`, not even a thread-scoped duplicate); per-thread twin suppression
keeps a live-settled agent turn
from re-projecting through `thread/read` while genuine agent history backfills (thread-scoped
ids: `{AGENT}:item-1` suppressed, `{AGENT}:item-0` kept);
cit:([`test_per_thread_twin_suppression_and_lazy_agent_native_walk`], mcp/tests/test_conversation_projector_codex_agents_engine_2.py:193-252) covers the
same twin-suppression behavior, and the
agent bucket never suppresses the parent re-walk; the lazy agent-native walk refuses
unlived or parent threads; and a malformed agent-thread frame's preserved unknown-vendor
evidence is tagged with the agent ref (fix-round finding 4) while the identical parent
failure stays untagged.

The remediation pair pins the concurrent-parent-pending projection.
cit:([`test_concurrent_parent_pendings_all_project_and_resolve_per_id`], mcp/tests/test_conversation_projector_codex_agents_engine_1.py:311-366): two
concurrent parent pendings plus an agent pending all project into the interaction lane —
the singular slot carries the parent's OLDEST (back-compat), parent-thread entries project
plainly (no agent ref), the agent entry carries its identity — and one parent pending
settling resolves per id while the others stay waiting.
cit:([`test_parent_singular_rotation_resolves_evicted_and_keeps_rotated_live`], mcp/tests/test_conversation_projector_codex_agents_engine_1.py:368-417): an
A→B singular rotation (oldest answered, the adapter rotates the next-oldest into the slot,
leaving the multiplexed tuple for the same id) RESOLVES the evicted id while the rotated
id stays live under the singular path; the later settle resolves both, none left waiting.

### Conventions

Fixtures are minimal synthesized shapes proven field-for-field against the vendored
protocol; intentionally malformed shapes stay inline where asserted. The suite reuses the active-service harness (`_identity`, `_authorization`, `_ControlledEntry`, `SECRET`) from
`test_conversation_active_service`. Each engine test asserts the single-cursor-domain
invariant explicitly (contiguous `global_ordinal` range). Three construction shapes are parameter
objects: `collab_agent_tool_call_item(item_id, tool, agents=CollabAgents(sender_thread_id,
receiver_thread_ids=…, states=…))` keeps the vendor's three thread-bearing fields together because
they are one fact; `ActiveSessionProjector` takes a
`ProjectedSession(identity/authorization/entry/mapper/secret)` plus
`readers=BridgeReaders(evidence/native_page/transcript/provenance/snapshot)`; and
`_MultiplexedBridge.read_native_page` carries no `byte_budget`, matching the reader seam.

### Invariants And Boundaries

- One page, one SSE, one cursor domain per seat; the agent dimension rides items, lanes
  are unchanged (agent items ride `harness`).
- Parent items never gain an agent dimension; unknown shapes degrade to preserved
  unknown-vendor with evidence refs, never guessed semantics.
- Concurrent parent-thread pendings project plainly (no agent ref) alongside agent
  pendings; the singular slot carries the parent's oldest, a slot ROTATION resolves the
  evicted id, and the rotated id stays live under the singular path.
- The per-thread native walk is page-driven (fix-round finding 3): `page()` backfills each live
  agent thread once per projector (walk-once marking, a failed walk retries on a later page),
  native ids are thread-scoped (`<threadId>:<nativeId>`) so forked copies never collide with
  parent items, and spawn records mint no roster rows from the walk; `refresh_agent_native`
  stays the public seam these tests drive.
- Roster upserts are merges: a block-less upsert never wipes previously bound blocks.

### Todos

`refresh_agent_native` is no longer latent — `page()`'s backfill loop is its production driver;
live multiplexed-approval
traffic is fixture-proven only (the multiplexed-traffic soak ran under a never-policy), and live
`subAgentActivity` is unprobed (`multi_agent_v2` is default-off on the installed 0.145.0).

## Docs References

No Domain Documentation source is configured; the wire shapes are proven against the
vendored codex protocol via the shared fixture module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The vendored-shape builders the mapped frames come from, plus the `CollabAgents` thread bundle. | `CollabAgents` | mcp/tests/_agent_wire_fixtures.py:63-77 |
| The codex mapper under test: collab/activity roster grammar, demux-keyed mapping, unknown-vendor degrade. | `map_evidence_frame`; "def _map_collab_tool_call(" | mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:311-311; mcp/src/agents_remember/serving/conversation/projectors/codex.py:146-199 |
| Roster identity and per-thread binding under test: `is_agent_roster_item`, the registry-backed agent ref, `bind_thread`, `reconcile_roster`, and the `scope_native_item` thread-scoped id prefix. | `is_agent_roster_item`; `bind_thread`; `reconcile_roster`; `scope_native_item` | mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py:33-41; mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py:80-93; mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py:95-122; mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py:124-131 |
| Per-thread native twin suppression under test: a native output is dropped when its turn or user request id was already seen live in that thread's bucket. | `suppress_live_twins` | mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:254-281 |
| The page-driven agent backfill under test: the paged `_walk` scopes every evidence handle to `<thread>:<nativeId>`, drops roster items, and binds the thread. | `_walk` | mcp/src/agents_remember/serving/conversation/active/projector/child_history.py:139-173 |
| Plural pendings under test: the parent pending rotates singly while multiplexed thread-keyed pendings are upserted/resolved concurrently against it. | `apply`; `_apply_multiplexed` | mcp/src/agents_remember/serving/conversation/active/projector/interaction_projection.py:44-54; mcp/src/agents_remember/serving/conversation/active/projector/interaction_projection.py:56-79 |
| The two parameter objects the suite wires the engine through. | `ProjectedSession`; "The whole read surface a projection is assembled from: five bridge reads, one session." | mcp/src/agents_remember/serving/conversation/active/projector/facade.py:42-56; mcp/src/agents_remember/serving/conversation/active/projector/wiring.py:37-37 |
| The scripted-bridge harness this suite extends with per-thread native pages. | `_ScriptedBridge` | mcp/tests/test_conversation_active_service.py:75-169 |
| The additive agent grammar on conversation items. | "class ConversationAgentRef(WireModel):" | mcp/src/agents_remember/serving/conversation/_models_blocks.py:137-137 |

## Cross-Repo References

The collab/activity item variants and notification shapes are vendored codex app-server
protocol; the fixture module pins each shape to its proving file in the vendor checkout.

| Finding | Anchor | Source |
| --- | --- | --- |
| `CollabAgentToolCall` / `SubAgentActivity` variants, exact camelCase enums, and turn/thread notification params. | "camelCase enums"; "all four fields are required" | mcp/tests/_agent_wire_fixtures.py:10-10; mcp/tests/_agent_wire_fixtures.py:116-116 |

## 260727-CHATS-IM-L2 Selected-Child Continuity Delta

The suite replaces page-driven all-child backfill expectations with explicit selection. It proves
roster-only parent paging, selected-child content hydration, a second wave where a cyclic child is
locally unavailable while the first child, healthy sibling, and parent remain live, same-child
singleflight, a slow child that does not hold the projector apply lock, visible 64-read capacity
refusal, and unavailable-to-recovered revision-two state. Opaque source continuations are consumed
without native-id cursor assumptions.

## Update History

- 2026-08-09T16:43+02:00 — 260713-TES-L5 hotfix curator: revalidated the twin-suppression claim
  after the shared native fallback insertion and repaired its moved `suppress_live_twins` range.
  The suite source itself is unchanged.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 7 repeated path:start-end Citation objects from 2 same-claim citation group(s) at card line(s) 129, 132; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 12 citation entries (21 findings); corrected the 3 obsolete historical/current prose citations and the checker-blind twin-suppression range residue under the max-reviewer ruling; remaining active citation result is zero.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived the 2 remediation-pair citations, both
  read back against the current 1295-line source. The IM-L2 selected-child tests were inserted
  ahead of them, so `test_concurrent_parent_pendings_all_project_and_resolve_per_id` L626-L681 →
  L737-L792 and `test_parent_singular_rotation_resolves_evicted_and_keeps_rotated_live` L682-L732 →
  L794-L843; both bodies still prove exactly what the paragraph claims (plain parent entries, the
  singular slot on the parent's oldest, per-id resolution; and the A→B rotation resolving the
  evicted id while the rotated id stays live). At that point the engine-tier paragraph's
  page-driven backfill reference was left for follow-up; the IM-L2 delta replaced it with the
  selected-child test, now cited as
  cit:([`test_selected_agent_backfills_content_when_live_delivery_is_partial`], mcp/tests/test_conversation_projector_codex_agents_engine_1.py:419-513) — and the
  surrounding spans drifted with it: mapper tier L132-L329 → L135-L334, engine tier L438-L930 →
  L464-L1291, and the twin-suppression span L809-L868 → `test_per_thread_twin_suppression_and_lazy_agent_native_walk`
  L1174-L1233.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the projector-engine citation, broken by
  the `active/projector.py` -> `active/projector/` package split (commit `3a8ff70`). The stamped
  `L38-L40` was already degenerate before the split — in the old 1409-line `projector.py` those
  three lines were `StoreMutation,` / `unknown_vendor_item,` / `)` inside an import block, and they
  matched only because they coincide with THIS test file's own import of the projector. Replaced
  the one over-broad row with five rows that each point at the module holding the behaviour it
  names, all read back in the code worktree: `agent_authority.py` L33-L131 (roster identity,
  `bind_thread`, `reconcile_roster`, `scope_native_item`'s `<thread>:` id prefix),
  `native_ingestion.py` L215-L242 (`suppress_live_twins`, bucketed per thread),
  `child_history.py` L139-L173 (the paged `_walk` with thread-scoped evidence refs),
  `interaction_projection.py` L44-L79 (`apply` rotating the single parent pending, then
  `_apply_multiplexed` upserting/resolving the thread-keyed plural pendings around it), and the two
  parameter objects `ProjectedSession` cit:([`ProjectedSession`], mcp/src/agents_remember/serving/conversation/active/projector/facade.py:42-56) + `BridgeReaders` cit:([`BridgeReaders`], mcp/src/agents_remember/serving/conversation/active/projector/wiring.py:35-48). Beyond my worklist and NOT fixed: the other two rows in this table
  (`_agent_wire_fixtures.py` L25-L36, `projectors/codex.py` L47) cite this test file's own import
  line numbers rather than lines in the linked file, so they point at unrelated text.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2: the suite's fixture and projector wiring moved to
  parameter objects, so Conventions now names them — `collab_agent_tool_call_item(...)` takes
  `agents=CollabAgents(sender, receiver_thread_ids=…, states=…)` instead of three loose thread
  keywords, `ActiveSessionProjector` takes a `ProjectedSession` plus `readers=BridgeReaders(...)`
  instead of ten keywords, and `_MultiplexedBridge.read_native_page` dropped `byte_budget` to stay
  signature-compatible with the reader seam. The two new import lines pushed every anchor in
  Repo-Internal References down, so all five were re-anchored against the current import block
  (fixtures L25-L35 → L25-L36, projector L36-L36 → L38-L40, models L37-L42 → L41-L46, codex
  L43-L43 → L47, scripted bridge L55-L62 → L59-L66). No test, mapped shape, roster or ordinal
  assertion changed.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: superseded page-driven backfill coverage
  with selected-child hydration, second-wave/sibling continuity, unlocked I/O, singleflight,
  explicit capacity, typed failure, and recovery regressions. Verification metadata remains
  pinned while uncommitted.

- 2026-07-27T00:02+02:00 — 260718-CHATS-L7R curator: recorded the then-current page-driven backfill
  coverage: partial live
  delivery + native authority → content backfilled, thread-scoped (`{AGENT}:msg-1`) and
  attributed, walk-once marking (`_agent_native_walked`), and a spawn-record native frame minting
  no roster row; the lazy-walk assertions moved to thread-scoped ids (`{AGENT}:item-0` kept,
  `{AGENT}:item-1` suppressed). The seam is no longer latent (page-driven), and the engine tier
  span grew L438-L849 → L438-L930. Verification metadata stays pinned — the change is
  uncommitted.
- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the concurrent-parent-pending
  projection pair — all pendings project into the interaction lane (parent entries plainly, the
  agent entry labeled; the singular slot on the parent's oldest) with per-id resolution, and the
  A→B singular-rotation semantics (evicted id resolves, rotated id stays live under the singular
  path). Anchored the new tests cit:([`test_concurrent_parent_pendings_all_project_and_resolve_per_id`, `test_parent_singular_rotation_resolves_evicted_and_keeps_rotated_live`], mcp/tests/test_conversation_projector_codex_agents_engine_1.py:311-366; mcp/tests/test_conversation_projector_codex_agents_engine_1.py:368-417) and refreshed the tier spans (engine tier L438-L849).
  Verification metadata stays pinned — the change is uncommitted.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: created the sidecar for the new codex
  projector sub-agent suite (R2/R5/R6; fix-round findings 3/4/5 pins). Verification is
  blank because the new source file is uncommitted; closeout owns its first source stamp.
