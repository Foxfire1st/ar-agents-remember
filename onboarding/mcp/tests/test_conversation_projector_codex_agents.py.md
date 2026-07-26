# mcp/tests/test_conversation_projector_codex_agents.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_projector_codex_agents.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T00:02+02:00 |
| lastVerifiedCommitHash |  `a401e3dba0bc6e9723451edbfdefb8d77c42945d`|
| lastVerifiedCommitDate |  2026-07-27T00:27:33+02:00|
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
(L131-L328) maps synthesized wire frames (built by `_agent_wire_fixtures`, parent thread
`vendor-1`) directly through `codex.map_evidence_frame`: a `spawnAgent` call stays the
parent's own untagged tool-call while minting a roster notice; a single-receiver
`sendInput` carries the agent ref but a multi-receiver `wait` does not; a terminal collab
roster carries the final-message block; `subAgentActivity` binds `agentPath` and
interrupted status into the same roster row; unknown collab/activity shapes degrade to
preserved `MappedUnknownVendor`; `thread/started` mints a registration only for a proven
non-parent (parent boot/resume is silent, and without the parent context the shape alone
mints nothing); agent-thread lifecycle frames drive roster status while an agent
`turn/completed` never feeds the parent-scoped status service.

`CodexAgentEngineTests` (L438-L930) drives the real `ActiveSessionProjector` over a
`_MultiplexedBridge` (extends the `_ScriptedBridge` harness with per-thread native pages and
demux-keyed frames): the 2026-07-24 incident stream multiplexes into one contiguous
ordinal space with one upserted roster settled by the agent's turn completion, agent
items carrying the bound ref while parent items stay byte-identical (no agent dimension);
block-less lifecycle roster upserts never wipe the final message (fix-round finding 5);
plural `pending_interactions` project labeled and resolve per id while the singular
parent path is untouched; the page-driven backfill test
(`test_page_backfills_agent_content_when_live_delivery_is_partial`, L730-L807) proves a partial
live delivery (roster and lifecycle crossed, the agent's content did not) is completed from
native authority — the content backfills thread-scoped (`{AGENT}:msg-1`) and agent-attributed,
the thread is marked walked once (`_agent_native_walked`) so later pages do not re-read it, and
a native `subAgentActivity` spawn record referencing ANOTHER agent mints no roster row (no
`codex-agent-other-agent`, not even a thread-scoped duplicate); per-thread twin suppression
keeps a live-settled agent turn
from re-projecting through `thread/read` while genuine agent history backfills (thread-scoped
ids: `{AGENT}:item-1` suppressed, `{AGENT}:item-0` kept, L809-L868) and the
agent bucket never suppresses the parent re-walk; the lazy agent-native walk refuses
unlived or parent threads; and a malformed agent-thread frame's preserved unknown-vendor
evidence is tagged with the agent ref (fix-round finding 4) while the identical parent
failure stays untagged.

The remediation pair pins the concurrent-parent-pending projection.
`test_concurrent_parent_pendings_all_project_and_resolve_per_id` (L622-L678): two
concurrent parent pendings plus an agent pending all project into the interaction lane —
the singular slot carries the parent's OLDEST (back-compat), parent-thread entries project
plainly (no agent ref), the agent entry carries its identity — and one parent pending
settling resolves per id while the others stay waiting.
`test_parent_singular_rotation_resolves_evicted_and_keeps_rotated_live` (L679-L729): an
A→B singular rotation (oldest answered, the adapter rotates the next-oldest into the slot,
leaving the multiplexed tuple for the same id) RESOLVES the evicted id while the rotated
id stays live under the singular path; the later settle resolves both, none left waiting.

### Conventions

Fixtures are minimal synthesized shapes proven field-for-field against the vendored
protocol; intentionally malformed shapes stay inline where asserted. The suite reuses the active-service harness (`_identity`, `_authorization`, `_ControlledEntry`, `SECRET`) from
`test_conversation_active_service`. Each engine test asserts the single-cursor-domain
invariant explicitly (contiguous `global_ordinal` range).

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The vendored-shape builders the mapped frames come from. | L25-L35 | [_agent_wire_fixtures.py](agents-remember/mcp/tests/_agent_wire_fixtures.py) |
| The codex mapper under test: collab/activity roster grammar, demux-keyed mapping, unknown-vendor degrade. | L43-L43 | [projectors/codex.py](agents-remember/mcp/src/agents_remember/serving/conversation/projectors/codex.py) |
| The projector engine under test: multiplexed projection, roster upserts, per-thread native suppression, the page-driven agent backfill with thread-scoped ids, plural pendings with concurrent-parent projection and singular rotation. | L36-L36 | [active/projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |
| The scripted-bridge harness this suite extends with per-thread native pages. | L55-L62 | [test_conversation_active_service.py](agents-remember/mcp/tests/test_conversation_active_service.py) |
| The additive agent grammar on conversation items. | L37-L42 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |

## Cross-Repo References

The collab/activity item variants and notification shapes are vendored codex app-server
protocol; the fixture module pins each shape to its proving file in the vendor checkout.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `CollabAgentToolCall` / `SubAgentActivity` variants, exact camelCase enums, and turn/thread notification params. | L7-L28 of the fixture docstring | [codex app-server protocol v2](https://github.com/openai/codex/tree/main/codex-rs/app-server-protocol/src/protocol/v2) |

## Update History

- 2026-07-27T00:02+02:00 — 260718-CHATS-L7R curator: recorded the backfill coverage —
  `test_page_backfills_agent_content_when_live_delivery_is_partial` (L730-L807): partial live
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
  path). Anchored the new tests (L622-L729) and refreshed the tier spans (engine tier L438-L849).
  Verification metadata stays pinned — the change is uncommitted.
- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: created the sidecar for the new codex
  projector sub-agent suite (R2/R5/R6; fix-round findings 3/4/5 pins). Verification is
  blank because the new source file is uncommitted; closeout owns its first source stamp.
