# mcp/src/agents_remember/serving/conversation/active/store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `41b2fd6452ee572799fa10c4f9c820ab549ec3d2`|
| lastVerifiedCommitDate | 2026-07-19T19:12:25+02:00|
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

### Conventions

The store holds no IO, no envelope minting, and no cursor knowledge — the projector wraps
`StoreMutation`s into envelopes. User-item provenance is tracked (L215-L222) only while not
already exact, and resolution never downgrades an exact verdict.

### Invariants And Boundaries

- Identity is the native item id; the same id re-mapped with identical content is a no-op, never
  a duplicate.
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

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the projection
  store — idempotent item/revision/ordinal authority, the review-F1 tool-call block union,
  bounded delta buffering, one-shot provenance resolution, honest page slicing. Verification is
  blank because the new source file is uncommitted; closeout owns its first source stamp.
