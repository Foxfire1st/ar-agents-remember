# mcp/src/agents_remember/serving/response_contract.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/response_contract.py`  |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated | 2026-09-22T11:00:00+02:00 |
| lastVerifiedCommitHash | `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` |
| lastVerifiedCommitDate | 2026-09-29T00:17:28+02:00|
| governingOverview      | `overview.md`                                           |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| **The served vocabulary of the leaf view's own recordedness, and its default for every existing caller.** | `LeafChangeSet`; "state: Literal[\"recorded\", \"unrecorded\"]"; `state_detail` | mcp/src/agents_remember/serving/response_contract.py:843-860 |
| **The producer that publishes it, with the counter zero it exists to annotate.** | `leaf_changeset` | mcp/src/agents_remember/serving/changeset.py:455-497 |
| **The client mirror and the control that renders the state and withholds the total.** | `TaskChangeset`; `ChangeSetButton` | dashboard/src/data/changeset.ts:41-48; dashboard/src/panels/detail-panel/changeSetBar.tsx:47-181 |
| **The cases that measure the discriminator and the route status.** | `test_an_unrecorded_committed_endpoint_is_answered_with_its_own_state_rather_than_read_from_head`; `test_the_route_answers_an_unrecorded_committed_view_without_a_status_error` | mcp/tests/test_knowledge_review_source_endpoints.py:682-728; mcp/tests/test_knowledge_review_source_endpoints.py:731-779 |

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The master-net generation identity (four endpoints + digest) and the served net's `generation` + `currentness` + `scope`; leaf rows carry `committed`/`working` state. | `MasterNetGeneration`; `MasterChangeSet`; `LeafSummary` | mcp/src/agents_remember/serving/response_contract.py:871-883; mcp/src/agents_remember/serving/response_contract.py:886-902; mcp/src/agents_remember/serving/response_contract.py:863-868 |
| **The leaf view's own recordedness: the `state` discriminator, its `recorded` default, and the route's sentence it carries (260921-ICR-L25).** | `LeafChangeSet`; `state_detail` | mcp/src/agents_remember/serving/response_contract.py:843-860 |
| The catalog wire mirrors structural binding, replacement, and the private dispatch receipt. | `TerminalCatalogEntryWire` | mcp/src/agents_remember/serving/response_contract.py:281-400 |
| Open and seat-conflict responses carry structural identity. | `TerminalOpened` | mcp/src/agents_remember/serving/response_contract.py:403-443 |
| Task assignment success/refusal use task-document identity. | `TerminalTaskAttached` | mcp/src/agents_remember/serving/response_contract.py:446-460 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 2 citations into `mcp/tests/test_knowledge_review_source_endpoints.py` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-25T23:45+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **body update — `LeafChangeSet` gains the `state`/`stateDetail` pair, and the section above records why.** It is a declarative addition with a `recorded` default, so every existing caller and every existing response is unchanged; what it buys is the distinction between a range **unrecorded** (the live leaf before its closeout) and one **measured empty**, since the counters beside an unrecorded range are a zero of nothing (register B6). **Citation accounting:** the three L13 `cit:`s and the four rows of the reference table were re-derived from each class's own declaration at this tip — the L25 insertion sits **above** `LeafSummary`, so `MasterNetGeneration` `:857-869` → `:871-883`, `MasterChangeSet` `:872-882` → `:886-902`, `LeafSummary` `:849-854` → `:863-868`, and the three terminal rows were re-derived too (`TerminalCatalogEntryWire` `:281-363` → `:281-400`, `TerminalOpened` `:399-423` → `:403-443`). **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.

- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **the master-net vocabulary.** The section above records `MasterNetGeneration`, the three new `MasterChangeSet` members and `LeafSummary.state` with measured ranges; the R24/R12/R25 boundaries are recorded as routed, not closed. No earlier claim is superseded (additive schema). Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-06T22:06:54+00:00 — Preserved source-verified runtime semantics from retired test onboarding; no removed coverage is claimed and verification pins are unchanged.

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: recorded the `RequirementRow`/`RequirementsListing`/`RequirementContents` models and the 61-to-63 route-count advance for the new requirement endpoints.

- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: added the reviewer
  structural-parent pair to the strict terminal catalog wire mirror. Verification remains
  closeout-owned.

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — No content impact: final ARSPAWN-L2 review confirmed the private
  receipt field is diagnostic/reconciliation evidence only and the strict wire mirror remains
  accurate. Verification remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: mirrored the catalog's optional private
  `dispatchBriefEntryId` receipt. Verification remains closeout-owned.

- 2026-08-21T03:30+02:00 — 260821-ARSPAWN-L1 fix round 2: `TerminalCatalogEntryWire` gained `spawned_by_kind` (`spawnedByKind` on the wire, `str | None`, None default) beside the spawned-by pair, mirroring the catalog row's conditional `to_json` emission; old `/api/terminal/sessions` rows unaffected; the key-set equality test keeps wire and serializer in lockstep. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `response_contract.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 13 citations (citation_anchor_missing=3, citation_prose_not_in_cit_form=7, citation_source_malformed=3); final scoped citation check clean.
- 2026-08-01T14:05+02:00 — 260731-EFA-L4 curator (correction pass), body only. The **Invariants**
  bullet said "Rewriting the 59 `Response`-returning handlers…", attributing a `Response` return to
  all 59. The module's own line (L47) says "the 59 handlers", without that attribution, and its L11-L18
  gives the split the card's Logic section already carried correctly: **57** return a `Response`
  subclass, **2** are SSE async generators feeding an `EventSourceResponse` (`GET /api/stream`,
  `GET /api/events`) — 59 on which `response_model` is schema only — and the remaining **2**
  (`GET /api/terminal/sessions`, `GET /api/harnesses`) return a bare `dict` and *are* validated by
  FastAPI. Bullet corrected; the conclusion it draws was already right. Added a **Conventions**
  paragraph making the file's scope unambiguous: it declares **93 model classes** plus the three
  shared `responses={...}` tables and **no route** — the `response_model=` kwargs live on decorators
  across **eight** modules (`app.py` 17, `conversation/control/api.py` 17, `harness_control_api.py`
  10, `conversation/library/api.py` 5, `files.py` 4, `changeset.py` 3, `conversation/active/api.py`
  3, `notes.py` 2), counted with `grep -c "response_model=" ` over
  `mcp/src/agents_remember/`, with the conversation modules drawing their models from
  `serving/conversation/response_contract.py` (only `StatusRefusal` crosses over). Re-checked all 17
  line citations in this card against the current file — every one lands on the symbol its claim
  names, including the ends (`HttpDetailRefusal` L186-**L191**, `TerminalCleanupSkip` L430-**L434**,
  `OnboardingResolution` L709-**L719**, `validate_wire`'s `by_name=False` at **L231**, and
  `len(self.http) == 61` at **L536**); none needed repair. Verification metadata untouched.

- 2026-08-01T08:12+02:00 — 260731-EFA-L4 curator: created for the new
  `serving/response_contract.py`. Documented why declaration alone is not the gate (57 of 61
  handlers return a `Response` directly and two are SSE generators, so FastAPI validates only
  `GET /api/terminal/sessions` and `GET /api/harnesses`), the `WireResponse` strictness base, the
  per-shape refusal models, the discriminated/plain unions, the three shared `responses={...}`
  tables, the `TerminalCleanupResult.model_rebuild()` forward reference, the deliberate
  import-order split from `conversation/response_contract.py`, and the websocket exemption found
  by route class rather than by path. Recorded the real behaviour change and its mitigation on
  the two bare-`dict` routes — a drifted `TerminalCatalogEntry.to_json` is now a live 500, held
  off by the CI key-set equality test that fires when the field is added. Verification metadata
  is a placeholder pinned to the leaf base `abc7cbcc`; closeout stamps the real commit.
