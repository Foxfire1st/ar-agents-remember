# mcp/src/agents_remember/serving/conversation/active/store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash | `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate | 2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

The projection store: the idempotence authority holding item/revision/ordinal state for one
session. Re-feeding the same evidence (rehydration, replay) reproduces the identical projection
— appends dedupe by native item id, upserts compare normalized payloads, tool-call upserts
converge by scoped block union, deltas apply in revision order with bounded delta-before-item
buffering, and provenance resolution rebuilds user items exactly once per source verdict. It
also carries the sub-agent upsert-race guards: a late agent-tagging upsert never
regresses a terminal tool-call phase, and a codex roster notice's `final-message` block survives
later block-less lifecycle upserts.

## Code Commentary

### Logic

`apply_item` (L124-L214) appends a new item (revision 1, next global ordinal) or upserts an
existing one: when `existing.kind == candidate.kind == "tool-call"` the candidate's blocks are
first unioned with the existing blocks by `block_id` (`_union_blocks` L435-L451 — candidate wins
per shared id, existing siblings survive, order stable), so partial-block tool items (invocation
first, result later) converge instead of the later whole-item replacement silently discarding
the `ToolInputBlock` (review finding F1); codex full-item re-maps are byte-identical under
union. Two upsert-race guards sit on top of that union. First (fix-round review
finding 9, L161-L166): a late tagging upsert — claude `task_started` binds the agent identity
onto the spawning tool call — hard-claims `phase="streaming"`, and reordered evidence can land
it AFTER the tool_result already completed the item; the guard keeps the existing terminal phase
(`completed`/`failed`/`interrupted`) so a settled tool call never re-opens. Second (fix-round
review finding 5, L173-L182): codex roster notices (sub-agent lifecycle rows) upsert per
lifecycle event and most of those events (`turn/started`, `turn/completed`, status) know nothing
about the agent's final message — when the candidate carries no `final-message` block, the
existing one is retained first-wins instead of being wiped by whole-item replacement.
Comparison normalizes engine-assigned fields (L49) so identical replays are no-ops; a
real change advances the revision while preserving ordinal, created-at, and provenance.
`apply_delta` (L216-L238) appends text into one existing block — targeting the mapped block id
or the kind-based default (`tool-call` → `output`, else `markdown`, L408-L412) — and buffers
deltas that arrive before their item or block (bounded 64 items × 64 deltas, L36-L39,
L300-L307), flushing them on the item's arrival (L309-L341). `apply_provenance` (L240-L271)
resolves one user item's producer from the provenance batch verdict through `_SOURCE_AUTHORITY`
(L41-L47: cockpit → operator/cockpit-composer, terminal → operator/terminal-controlled, durable
→ agent-bus/durable-inbox), exactly once per request id, with strength `exact`; absent records
leave the honest unknown-input product untouched. `page` (L273-L289) slices one chronological
window by ordinal with an older-page boundary and an honest `total_items` (only when the caller
attests the total is known). `unknown_vendor_item` (L454-L486) mints the preserved
unknown-vendor evidence item — the public item carries only a safe summary and an opaque
coordinate evidence handle; raw payloads stay server-side. It also
propagates the mapper-bound agent ref (`agent=mapped.agent`, L472), so a malformed agent-thread
frame's preserved evidence lands in the agent's view, not anonymously in the parent's.

### Input-authority preservation across native re-maps (H2/F4)

`_preserved_input_authority(existing)` names the fields a native re-map must INHERIT from the stored
item rather than overwrite. Provenance is ALWAYS preserved (a re-map must never downgrade an
already-resolved producer). For `role=="user"` input items the whole authority triple —
`lane` + `source` + `provenance` — is ONE resolved unit: input authority is resolved exactly once,
via `apply_provenance`, never by a native re-map. Non-user (harness) items keep provenance-only
preservation, so their legitimate `harness-live`↔`native-history` source transition still flows.

H2. A codex user message arrives honest `unknown-input`/`native-only`;
`apply_provenance` (source `cockpit`) resolves it to `operator`/`cockpit-composer`/`exact`; then
codex RE-MAPS the same native user item (an ordinary full-item re-map under real traffic),
re-emitting the default `unknown-input` lane/source. Before the pin, the upsert adopted the
candidate's `unknown-input` lane/source while preserving the existing resolved `exact` provenance —
SPLITTING the triple into a `lane="unknown-input"` item that carries `strength="exact"` + an
operator producer. That item violates `ConversationItem.preserve_input_authority` (`models.py`) but
is stored SILENTLY because pydantic v2 `model_copy(update=…)` skips validation; it 500-ed only later,
at the active-page route / SSE re-validation boundary (and when `projector.py` wraps the mutation
into `UpsertItemMutation`) — the intermittent active-page 500 the reviewer saw. The fix applies
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
`StoreMutation`s into envelopes. User-item provenance is tracked (L291-L298) only while not
already exact, and resolution never downgrades an exact verdict.

### Invariants And Boundaries

- Identity is the native item id; the same id re-mapped with identical content is a no-op, never
  a duplicate.
- User-item input authority (`lane` + `source` + `provenance`) is ONE resolved unit (H2): a
  native re-map inherits it intact via `_preserved_input_authority`; only `apply_provenance` may set
  it. Harness items keep provenance-only preservation so their `harness-live`↔`native-history`
  source transition still flows. The triple is applied to the comparable candidate too (F4), so an
  identical post-resolution re-map is a true no-op, not a revision bump. Because `model_copy(update=…)`
  skips validation a split triple would be held silently and only 500 at route/SSE re-validation —
  which is exactly why the whole triple must stay coupled.
- A terminal tool-call phase is never regressed (fix-round finding 9): a late
  `streaming`-claiming tagging upsert (claude `task_started` agent binding) landing after the
  tool_result settled the item keeps the existing `completed`/`failed`/`interrupted` phase —
  reordered evidence can never re-open a settled tool call.
- A roster notice's `final-message` block is retained first-wins (fix-round
  finding 5): codex sub-agent lifecycle upserts that carry no `final-message` block must not wipe
  the one an earlier upsert stored. Only tool-call upserts union blocks; every other kind keeps
  whole-item replacement semantics with this single roster retention exception (no legitimate
  native block-removal update exists in any landed tool grammar).
- Agent identity on preserved unknown-vendor evidence flows into the stored item
  (`unknown_vendor_item`, L472): a malformed agent-thread frame's evidence is attributed to the
  agent, never anonymously to the parent.
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
the union converges — and the claude `task_started` tagging upsert and
the codex roster lifecycle upserts the two retention guards cover.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `ConversationItem` and the block/provenance vocabulary define what the store compares and unions. | L341-L473 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| The submission-provenance batch is the only producer-verdict channel; absent records stay unknown-input. | L528-L530 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| Claude mappers emit split tool items (input first, output later) that the block union converges, and the `task_started` tagging upsert that hard-claims `streaming` (the finding-9 guard's subject). | L613-L650; L860-L895 | [claude.py](agents-remember/mcp/src/agents_remember/serving/conversation/projectors/claude.py) |
| The projector wraps store mutations into totally ordered envelopes. | L1130-L1183 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |

## Cross-Repo References

No cross-repository implementation participates in this store.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Session-Epoch Alignment And Recovery Delta

The active projection store now keeps page, event, recovery, and eviction state aligned with the current session epoch. Recovery re-pages from a fresh server cursor after an unusable stream, and bounded state release remains the only route that discards a dormant projection.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260727-CHATS-IM-L2 Current Delta

Roster upsert reconciliation preserves terminal status and phase when a native-history candidate
only replays a historical non-terminal row. The rule is limited to explicit backend roster ids
and yields to terminal candidates or non-history live authority.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: roster upserts now preserve a
  terminal child status when a later native-history replay carries only historical non-terminal
  evidence, while still accepting a terminal candidate or current live authority. Verification
  metadata remains pinned until closeout.

- 2026-07-26T15:34 — 260718-CHATS-L7 curator: recorded the two sub-agent upsert-race guards and
  the agent-ref propagation. Fix-round finding 9: a late `streaming`-claiming tagging upsert
  (claude `task_started` binding the agent identity onto the spawning tool call) can land after
  the tool_result completed the item — the terminal phase is now kept, never regressed
  (L161-L166). Fix-round finding 5: a codex roster notice's `final-message` block is retained
  first-wins across later block-less lifecycle upserts instead of being wiped by whole-item
  replacement (L173-L182). `unknown_vendor_item` now propagates `mapped.agent` so a malformed
  agent-thread frame's preserved evidence is attributed to the agent (L472). Refreshed all stale
  line citations (file grew 353 → 489 lines) and added the corresponding invariants.
  Verification metadata stays pinned — the L7 change is uncommitted, so no commit hash can
  attest it.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

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
