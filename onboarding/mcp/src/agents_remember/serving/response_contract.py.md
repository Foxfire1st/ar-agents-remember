# mcp/src/agents_remember/serving/response_contract.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Defines strict served HTTP response models. Terminal catalog, open, conflict, and assignment
responses now expose canonical task-document binding rather than leaf-key identity.

## Code Commentary

`WireResponse` is frozen, generates camelCase aliases and forbids extra fields. Separate refusal models declare which identifier each status may echo; an untyped status-plus-arbitrary-data envelope would discard this boundary. Internal population by field name is allowed, so wire validation must still distinguish the emitted alias form. The removed route-conformance matrices are historical evidence, not an active coverage claim. cit:([`WireResponse`], mcp/src/agents_remember/serving/response_contract.py:89-109).

### Logic

`TerminalCatalogEntryWire` mirrors the conditional catalog serializer — since 260821-ARSPAWN-L1 it
also carries the caller-kind provenance field `spawned_by_kind` (`spawnedByKind` on the wire,
`str | None`, None default) beside the spawned-by session/lifecycle pair, so `/api/terminal/sessions`
rows expose caller kind only when set and old rows are unaffected; the module's key-set equality
test against `TerminalCatalogEntry.to_json` keeps the wire and the hand-rolled serializer in
lockstep. Open and seat-conflict models
carry structural identity; task assignment responses return the accepted or refused document and
role. Other serving response families remain strict and unchanged in responsibility.
ARSPAWN-L2 also mirrors `dispatch_brief_entry_id` (`dispatchBriefEntryId` on the wire), the private
catalog receipt used for dispatch reconciliation after inbox compaction.
ARSPAWN-L5 mirrors `structural_parent_task_document_ref` and `structural_parent_role`, so operator
projections can distinguish the owner of an exact reviewer generation without consulting spawn
ancestry or a runtime id.


## 260831-CCR-L23 Task-Local Requirement Models

L23 added the strict task-local requirement response models under the shared
scoped-read refusal table: `RequirementRow` (one canonical Markdown packet:
name/path/address/size/sha256), `RequirementsListing` (repo/master/document/
registered + rows for `GET /api/requirements/list`), and
`RequirementContents` (listing metadata + decoded content for
`GET /api/requirements/read`). The route family grew from 61 to 63 HTTP routes,
of which 59 return a `Response` subclass directly (the module header counts were
advanced to match).

### Conventions

Handlers that return raw `Response` objects rely on explicit conformance tests; declared FastAPI
response models validate where the framework owns serialization.

### Invariants And Boundaries

- Current public wire responses contain no legacy leaf-binding fields.
- Session ids remain operator/transport occupant correlation.
- A seat conflict is reported against task-document-and-role identity.
- The dispatch receipt is diagnostic/reconciliation evidence, not a public structural address.
- Reviewer structural parent is a canonical document+role address and remains separate from
  spawned-by correlation.

### Todos

None.

## 260921-ICR-L13 Current Delta — The Master-Net Vocabulary

This leaf added the three shapes the generation-bound master net is served in (declarative
schema only; the file grows 1136 → 1155 lines, soft band, green via
`test_file_size_detector.py`):

- `MasterNetGeneration` — the exact endpoints one net comparison was computed over, and
  their identity: `code_base`/`code_tip` plus `memory_base`/`memory_tip` (empty when the
  master shows no memory half) and the deterministic `digest`. A completed master's
  recorded result re-resolves from these rather than from the live branch tip.
  cit:([`MasterNetGeneration`], mcp/src/agents_remember/serving/response_contract.py:871-883)
- `MasterChangeSet` gains `generation: MasterNetGeneration | None` (absent only for the
  unknown-master degradation), `currentness: "current" | "superseded" | "unmeasured"`, and
  `scope: "integrated"` — the one scope the selection ever serves.
  cit:([`MasterChangeSet`], mcp/src/agents_remember/serving/response_contract.py:886-902)
- `LeafSummary` gains `state: "committed" | "working"` (default `committed`) so an
  in-flight preview rides beside the net, never silently inside it.
  cit:([`LeafSummary`], mcp/src/agents_remember/serving/response_contract.py:863-868)

Routed boundaries recorded here, not closed here: R24 owns the leaf-history catalogue and
drill-down UI on top of `leaves[].state` and per-view `generation`; R12 owns
committed-leaf historical views; the browser-class journeys belong to R25.

## 260921-ICR-L25 Current Delta — The Leaf View Names Whether Its Range Is Recorded

**`LeafChangeSet` gains `state` and `state_detail`, and they exist to keep two states apart that were
previously collapsed.** `state: Literal["recorded", "unrecorded"]` (default `"recorded"`, wire
`state`) says whether the view's own endpoints are recorded; `state_detail: str` (wire `stateDetail`)
carries the route's own sentence naming the missing endpoint and the action that produces it.

`unrecorded` is a `committed` view of a leaf whose landed commit nothing has recorded yet — the state
every live leaf is in before its closeout, and one the change-set bar probes as soon as a leaf
document is opened. It is **answered rather than refused** because the resource exists and only its
second endpoint does not, and because a `404` for it was a browser console error on the page whose
accepted criterion is zero (register B6). The counters that ride beside it are a measured zero **of
nothing**, which is exactly why the state has to be explicit: no reader may take them for "the leaf
landed nothing", and the client withholds its total for the same reason.

**`LeafChangeSet` remains a `TaskChangeSet` subclass with the `mode` echo, so this is one added
field pair and no shape change.** The class is also now the third of the three fresh fields this
route family publishes, so the annotate-only `TaskChangeSet` is untouched and the two
members it inherits (`code`, `memory`, `counters`) are unchanged. The refusal table is unchanged:
this is a `200` body contract, not a new status.

- **The served vocabulary of the leaf view's own recordedness, and its default for every existing caller.** [1]
- **The producer that publishes it, with the counter zero it exists to annotate.** [2]
- **The client mirror and the control that renders the state and withholds the total.** [3]
- **The cases that measure the discriminator and the route status.** [4]

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The master-net generation identity (four endpoints + digest) and the served net's `generation` + `currentness` + `scope`; leaf rows carry `committed`/`working` state. [5]
- **The leaf view's own recordedness: the `state` discriminator, its `recorded` default, and the route's sentence it carries (260921-ICR-L25).** [6]
- The catalog wire mirrors structural binding, replacement, and the private dispatch receipt. [7]
- Open and seat-conflict responses carry structural identity. [8]
- Task assignment success/refusal use task-document identity. [9]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
