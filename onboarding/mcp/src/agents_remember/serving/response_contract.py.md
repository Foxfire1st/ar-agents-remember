# mcp/src/agents_remember/serving/response_contract.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/response_contract.py`  |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated | 2026-08-31T04:59+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving overview](overview.md)

## Purpose

Defines strict served HTTP response models. Terminal catalog, open, conflict, and assignment
responses now expose canonical task-document binding rather than leaf-key identity.

## Code Commentary

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

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The catalog wire mirrors structural binding, replacement, and the private dispatch receipt. | `TerminalCatalogEntryWire` | mcp/src/agents_remember/serving/response_contract.py:281-363 |
| Open and seat-conflict responses carry structural identity. | `TerminalOpened` | mcp/src/agents_remember/serving/response_contract.py:399-423 |
| Task assignment success/refusal use task-document identity. | `TerminalTaskAttached` | mcp/src/agents_remember/serving/response_contract.py:442-460 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

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
