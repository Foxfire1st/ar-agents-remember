# mcp/src/agents_remember/serving/conversation/active/store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:00+02:00 |
| lastVerifiedCommitHash | `68b3205526dae210cd902eef39d93c4f4352c2d4`|
| lastVerifiedCommitDate | 2026-07-21T01:12:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

The projection store: the idempotence authority holding item/revision/ordinal state for one
session. Re-feeding the same evidence (rehydration, replay) reproduces the identical projection
— appends dedupe by native item id, upserts compare normalized payloads, tool-call upserts
converge by scoped block union, deltas apply in revision order with bounded delta-before-item
buffering, and provenance resolution rebuilds user items exactly once per source verdict.

## Code Commentary

### Logic

`apply_item` (L101-L148) appends a new item (revision 1, next global ordinal) or upserts an
existing one: when `existing.kind == candidate.kind == "tool-call"` the candidate's blocks are
first unioned with the existing blocks by `block_id` (`_union_blocks` L303-L319 — candidate wins
per shared id, existing siblings survive, order stable), so partial-block tool items (invocation
first, result later) converge instead of the later whole-item replacement silently discarding
the `ToolInputBlock` (review finding F1); codex full-item re-maps are byte-identical under
union. Comparison normalizes engine-assigned fields (L49) so identical replays are no-ops; a
real change advances the revision while preserving ordinal, created-at, and provenance.
`apply_delta` (L150-L162) appends text into one existing block — targeting the mapped block id
or the kind-based default (`tool-call` → `output`, else `markdown`, L296-L300) — and buffers
deltas that arrive before their item or block (bounded 64 items × 64 deltas, L36-L39,
L224-L231), flushing them on the item's arrival (L233-L246). `apply_provenance` (L164-L195)
resolves one user item's producer from the provenance batch verdict through `_SOURCE_AUTHORITY`
(L41-L47: cockpit → operator/cockpit-composer, terminal → operator/terminal-controlled, durable
→ agent-bus/durable-inbox), exactly once per request id, with strength `exact`; absent records
leave the honest unknown-input product untouched. `page` (L197-L213) slices one chronological
window by ordinal with an older-page boundary and an honest `total_items` (only when the caller
attests the total is known). `unknown_vendor_item` (L322-L353) mints the preserved
unknown-vendor evidence item — the public item carries only a safe summary and an opaque
coordinate evidence handle; raw payloads stay server-side.

### 260718-CHATS-L5 H2/F4 — input-authority preservation across native re-maps

`_preserved_input_authority(existing)` names the fields a native re-map must INHERIT from the stored
item rather than overwrite. Provenance is ALWAYS preserved (a re-map must never downgrade an
already-resolved producer). For `role=="user"` input items the whole authority triple —
`lane` + `source` + `provenance` — is ONE resolved unit: input authority is resolved exactly once,
via `apply_provenance`, never by a native re-map. Non-user (harness) items keep provenance-only
preservation, so their legitimate `harness-live`↔`native-history` source transition still flows.

H2 (L4 verdict E2). A codex user message arrives honest `unknown-input`/`native-only`;
`apply_provenance` (source `cockpit`) resolves it to `operator`/`cockpit-composer`/`exact`; then
codex RE-MAPS the same native user item (an ordinary full-item re-map under real traffic),
re-emitting the default `unknown-input` lane/source. Before the pin, the upsert adopted the
candidate's `unknown-input` lane/source while preserving the existing resolved `exact` provenance —
SPLITTING the triple into a `lane="unknown-input"` item that carries `strength="exact"` + an
operator producer. That item violates `ConversationItem.preserve_input_authority` (`models.py`) but
is stored SILENTLY because pydantic v2 `model_copy(update=…)` skips validation; it 500-ed only later,
at the active-page route / SSE re-validation boundary (and when `projector.py` wraps the mutation
into `UpsertItemMutation`) — the intermittent active-page 500 the L4 reviewer saw. The fix applies
`_preserved_input_authority` at BOTH the real upsert AND (F4) the comparable candidate BEFORE the
normalized-equality check, so an identical `unknown-input` re-map of an already-resolved user item
compares equal and stays a true no-op (revision `2→2→2`, zero redundant `upsert-item`) rather than
bumping a revision per identical re-map.

Scope proven exact (reviewer constructor audit): every user-role constructor in the active pipeline
emits only the `unknown-input`/`native-history`/`unknown_input_provenance` default (codex/pi/claude),
interaction items are `role="system"`, `MappedUnknownVendor.role` defaults to `system`, and the
library normalizers never reach this store — so `apply_provenance` is the SOLE lane/source/producer
resolution authority for user items and the pin cannot freeze a legitimate lane transition (none
exists pre-`apply_provenance`). The unresolved honest path (`source=None` → stays
`unknown-input`/`native-only`, R6.4) is unaffected; rehydration rebuilds a fresh store and
re-resolves, so the pin is never persisted state.

### Conventions

The store holds no IO, no envelope minting, and no cursor knowledge — the projector wraps
`StoreMutation`s into envelopes. User-item provenance is tracked (L215-L222) only while not
already exact, and resolution never downgrades an exact verdict.

### Invariants And Boundaries

- Identity is the native item id; the same id re-mapped with identical content is a no-op, never
  a duplicate.
- User-item input authority (`lane` + `source` + `provenance`) is ONE resolved unit (L5 H2): a
  native re-map inherits it intact via `_preserved_input_authority`; only `apply_provenance` may set
  it. Harness items keep provenance-only preservation so their `harness-live`↔`native-history`
  source transition still flows. The triple is applied to the comparable candidate too (F4), so an
  identical post-resolution re-map is a true no-op, not a revision bump. Because `model_copy(update=…)`
  skips validation a split triple would be held silently and only 500 at route/SSE re-validation —
  which is exactly why the whole triple must stay coupled.
- Only tool-call upserts union blocks; every other kind keeps whole-item replacement semantics
  (no legitimate native block-removal update exists in any landed tool grammar).
- Buffering is bounded by construction; eviction of pending deltas is silent only for shapes
  that never complete, which the unknown-vendor path already covers.
- Page windows are ordinal-sliced, never viewport-derived; `total_items` is omitted unless the
  native walk completed and the evidence window never evicted.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The normalized item/block grammar
is the repository-owned strict wire contract cited below.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this store. | — | — |

## Repo-Internal References

The strict item/block/provenance models define the stored products; the submission-provenance
batch supplies the source verdicts; the per-harness mappers emit the partial-block tool items
the union converges.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `ConversationItem` and the block/provenance vocabulary define what the store compares and unions. | L315-L403 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The submission-provenance batch is the only producer-verdict channel; absent records stay unknown-input. | L352-L380 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| Claude and pi mappers emit split tool items (input first, output later) that the block union converges. | L196-L230; L269-L307 | [claude.py](agents-remember/mcp/src/agents_remember/serving/conversation/projectors/claude.py) |
| The projector wraps store mutations into totally ordered envelopes. | L604-L656 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |

## Cross-Repo References

No cross-repository implementation participates in this store.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: documented the H2/F4 `_preserved_input_authority`
  pin — for `role=="user"` items the `lane`/`source`/`provenance` authority triple stays intact
  across a native re-map (authority resolves only via `apply_provenance`), closing the silent
  `model_copy`-skips-validation split that violated `preserve_input_authority` and 500-ed the
  active-page route only at re-validation; harness items keep provenance-only preservation so their
  source transition still flows; F4 applies the pin to the comparable candidate too so an identical
  post-resolution re-map is a true no-op. Scope proven exact by the reviewer's constructor audit.
  Verification metadata stays pinned until L5 closeout stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the projection
  store — idempotent item/revision/ordinal authority, the review-F1 tool-call block union,
  bounded delta buffering, one-shot provenance resolution, honest page slicing. Verification is
  blank because the new source file is uncommitted; closeout owns its first source stamp.
