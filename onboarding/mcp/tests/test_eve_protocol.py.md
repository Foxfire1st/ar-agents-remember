# mcp/tests/test_eve_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_eve_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T05:17+02:00 |
| lastVerifiedCommitHash | `f79f4db745ad00b908d6ce4871d0b4ab2320207c` |
| lastVerifiedCommitDate | 2026-09-20T05:22:07+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l39-ar`, uncommitted; base `756c47b37fa16324a836a44336655413d10fffaa` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Wire-contract conformance for the eve session protocol reader, and — since the A2 revision — for the
**exact bytes the production client puts on the wire**. The file's own docstring states why it exists:
the cursor is the one piece of this adapter that **cannot be repaired after the fact** — an off-by-one
or a frame-boundary mistake silently drops or duplicates a durable event, and the sessions that
suffered it are the ones already running. So these cases pin the decoder's index arithmetic and the
envelope parsing against eve's documented shapes, and the request bodies against the transport the
adapter actually uses.

## Code Commentary

### Logic

Nine `unittest.TestCase` classes, one per contract face:

- `EveRouteTests` — routes are ID-addressed and exact; a negative cursor and an empty identity segment
  are refused. Nothing here can create or follow a replacement session.
- `EveStreamHeaderTests` — the declared stream version is **required, not inferred from the JSON**:
  each of `21`–`25` is accepted, `26` and a missing header raise. The optional tail-index header reads
  or is absent, and a non-numeric one raises. Header lookup is case-insensitive and a blank value
  counts as absent.
- `EveAcceptanceTests` — the durable session id may come from the body or the session-id header, and
  an acceptance carrying **no** identity fails instead of unbinding the session.
- `EveFrameTests` — the envelope is read field by field (including `deliveryIds` and the `raw_frame()`
  round-trip), a pre-version-20 event with no `meta.id` still parses, and five malformed shapes are
  refused.
- `EveCursorTests` — frames split across reads keep their absolute index; blank keep-alive lines do
  **not** consume one; a trailing frame without a newline is still decoded by `finish()`; an oversized
  frame is refused; a frame exactly at the ceiling is still read.
- `EveEnvelopeIdentityTests` — `turn_id` reads the documented coordinate and nothing else, and is
  optional.
- `EveReplayWindowTests` — the bounded replay window: a repeated id is a replay and a first sight is
  not, the window evicts oldest-first and stays bounded, a size-1 window still recognises its single
  entry, an event with no id is **never** a replay, and a non-positive window is refused at
  construction.
- `EveWireBodyTests` — the body builders themselves: create and follow-up **both** spell the queued
  policy, and the cancel body addresses the exact observed turn.
- `EveWireRequestTests` — the production `EveRuntimeProcess` driven through `httpx.MockTransport`
  against a `_Recorder`, so the request the adapter really sends is asserted rather than inferred from
  a fake. This is the face that pins the wire, and it does not require a server.

### Conventions

- The module inserts `mcp/src` on `sys.path` itself, the sibling-test convention in this suite.
- `_frame(...)` builds one NDJSON frame with a deterministic envelope id, so a case reads as the
  protocol shape it pins rather than as JSON construction.
- Cases are added to a `unittest.TestCase`, so they join the existing unit population rather than
  introducing a second test framework to this suite.
- `_StartedRuntime` subclasses the production process so the wire cases exercise real `start`,
  `create_session`, `send_message` and `cancel_turn` code against a recorded transport.

### Invariants And Boundaries

- These cases pin **framing, parsing and the outgoing request bodies**. They do not start an eve
  process, do not exercise the adapter's session state, and prove nothing about delivery, acceptance
  or terminal state — that is `test_eve_adapter.py`'s scope.
- The keep-alive case is load-bearing for correctness, not for tidiness: advancing the index on a
  blank line would drift the persisted cursor away from the durable record.
- **A policy asserted only on the create is not asserted.** The follow-up carries its own body, so the
  queued policy is pinned on both shapes; a second, unasserted follow-up body is how a steer
  inheritance hides.
- Asserting both directions is the local style: each case also pins the refusal it would otherwise
  hide.

### Todos

None known.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the shapes under test come from the eve wire contract and are mirrored by the module under test. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The routes, header gates, acceptance parsing and frame schema these cases pin. | `parse_stream_version`; `parse_stream_tail_index`; `parse_session_acceptance`; `parse_event_frame` | mcp/src/agents_remember/serving/eve_protocol.py:147-222 |
| The absolute-index decoder and its frame ceiling. | `EveNdjsonDecoder`; `DEFAULT_MAX_FRAME_BYTES` | mcp/src/agents_remember/serving/eve_stream_cursor.py:15-69 |
| The bounded replay window whose occupancy and eviction these cases pin. | `EveEventDeduplicator`; `EVE_REPLAY_WINDOW`; `retained` | mcp/src/agents_remember/serving/eve_protocol.py:224-268 |
| The production request builders and the transport these wire cases drive. | `create_session_body`; `follow_up_body`; `cancel_turn_body`; `EveRuntimeProcess` | mcp/src/agents_remember/serving/eve_runtime_client.py:62-89; mcp/src/agents_remember/serving/eve_runtime_client.py:118-372 |
| The adapter cases that consume this same wire layer one level up. | `EveAdapterReconnectTests`; `EveAdapterReconcileTests`; `EveAdapterInterruptTests` | mcp/tests/test_eve_adapter.py:661-907 |
| The test suite this file joins and its fixture/collection conventions. | `## Fixture Roles And Claims`; `## Isolation And Collection` | onboarding/mcp/tests/overview.md:846-867; onboarding/mcp/tests/overview.md:868-871 |

## Cross-Repo References

No external repository boundary is implemented by this test.

| Finding | Anchor | Source |
| --- | --- | --- |
| The protocol shapes under test are the pinned published `eve` package's contract, not a sibling repository's. | `eve` | mcp/src/agents_remember/serving/eve_protocol.py:32-40 |

## Update History
- 2026-09-20T05:17+02:00 — 260915-KS-L39 curator (cross-card pointer repair, the same class as the two entries below; uncommitted CYCLE-01 change set on `ar/260915-ks-l39-ar`, code base `756c47b3`): **this card is reconciled, not extended — its one memory-tree row was re-pointed because a different document grew above the two headings it cites, and no claim, anchor or body byte of this card changed.** `onboarding/mcp/tests/overview.md` gained the `260915-KS-L39` record at the top of the route, which shifted `## Fixture Roles And Claims` from `:800` to `:846` and `## Isolation And Collection` from `:822` to `:868` — a constant `+46`, since the insertion is above both. The row now cites each heading's own section extent, `:846-867` and `:868-871`, which is the form the previous repairs used and the form that carries the anchor without depending on a bare heading line. The source file `mcp/tests/test_eve_protocol.py` is byte-identical to this leaf's base, so no verification stamp was advanced and none was invented; the retained `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is the one L34 left. `reviewedWorkingCandidate` names this leaf's candidate because the card's bytes moved under that retained pair and this is the candidate the reading was performed against. No commit was made.
- 2026-09-20T03:26+02:00 — 260915-KS-L35 curator (cross-card pointer repair, the same class as the entry below; uncommitted change set on `ar/260915-ks-l35-ar`, code base `7abacd8e`): **this card's one memory-tree row was re-pointed again because a different document grew above the two headings it cites — no claim, no anchor and no body byte of this card changed.** `onboarding/mcp/tests/overview.md` gained the `260915-KS-L35` record at the top of the route, which shifted `## Fixture Roles And Claims` from `:761` to `:800` and `## Isolation And Collection` from `:783` to `:822` — a constant `+39`, since the insertion is above both. The row now cites each heading's own section extent, `:800-821` and `:822-825`, exactly the form the previous repair used; citing the heading line alone is not used because the checker's own strip of the trailing newline makes a bare heading line ambiguous while the lines below it are blank. The target document was not edited to suit this pointer, both anchors are unchanged, and the source file `mcp/tests/test_eve_protocol.py` is byte-identical to this leaf's base, so no verification stamp was advanced and none was invented — the retained `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is the one L34 left, and the `reviewedWorkingCandidate` row is left naming L34's candidate because this pass changed only a coordinate into another document.
- 2026-09-20T02:50+02:00 — 260915-KS-L34 curator (cross-card pointer repair; uncommitted change set on `ar/260915-ks-l34-ar`, memory base `3faf5b50`): **this card's one memory-tree row was re-pointed because a different document grew and moved the two headings it cites — no claim of this card changed.** The row cites the suite and collection conventions of `onboarding/mcp/tests/overview.md`, and that route overview gained a new section above those two headings, which shifted `## Fixture Roles And Claims` from `:725` to `:761` and `## Isolation And Collection` from `:747` to `:783` (a constant `+36`, since the insertion is above both). The row now cites each heading's own section extent — `:761-782` and `:783-786` — rather than the heading line alone, because a single-line range cannot carry the anchor *and* the checker's own strip of the trailing newline makes a bare heading line ambiguous while the two lines below it are blank; a section extent is what the claim is actually about anyway. The claim, both anchors, and every other row in this document are unchanged, and the target document was not edited to suit the pointer. No verification stamp advanced and none was invented: this is another route's insertion, not a change to `mcp/tests/test_eve_protocol.py`, which is byte-identical to this leaf's base. The metadata carries a `reviewedWorkingCandidate` row naming this candidate because the card's bytes moved under the retained pair.

- 2026-09-18T19:53:42+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document** (one table row, two heading anchors). The row cited `mcp/tests/overview.md:724-724` and `:746-746` — the blank lines above the two section headings it names — so both ranges were widened by one line (`724-725`, `746-747`) to reach `## Fixture Roles And Claims` and `## Isolation And Collection` themselves. The claim and both anchors are unchanged; the target document is another card and was not edited. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T13:27+02:00 — 260915-KS-L13 curator (range-closure pass): **the one row whose memory-tree ranges had gone stale was re-pointed to the lines that now carry its anchors.** The row cites this route's own suite/collection conventions in `onboarding/mcp/tests/overview.md`; the L13 and later insertions moved those two headings, so `:608-628` / `:630-632` were replaced by the checker-named live extents `:724-724` (`## Fixture Roles And Claims`) and `:746-746` (`## Isolation And Collection`). Both anchors are unchanged and both ranges are in bounds; no claim was deleted or softened. No verification stamp advanced: the source is uncommitted and the governed closeout owns the real code and memory commits.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): this file more than doubled
  (238 → 526 lines) and is the round's main test-strengthening surface. Three new faces are recorded:
  `EveReplayWindowTests` pins the bounded window's eviction, size-1 and id-less cases plus the
  non-positive refusal; `EveWireBodyTests` pins that create **and** follow-up both spell the queued
  policy; `EveWireRequestTests` drives the **production** `EveRuntimeProcess` through
  `httpx.MockTransport` and a `_Recorder`, so the sent request is asserted rather than inferred from a
  fake. The "six contract faces" count was corrected to the actual nine, and the boundary that these
  cases pin framing plus outgoing bodies (never adapter session state) was made explicit. Citation
  tables rewritten into the `Finding | Anchor | Source` shape; verification metadata moves to the
  leaf's current base `e9300687`, with the governed closeout stamping the real code commit.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: created this card for a test module added by the
  native eve session-adapter change set. Records the six contract faces, the deliberately narrow
  framing-and-parsing scope, and why the keep-alive case is correctness-bearing. Verification
  metadata is pinned to the leaf's base commit `67b21aeb` because the candidate is deliberately
  uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was
  invented here.
