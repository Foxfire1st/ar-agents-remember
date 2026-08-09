# mcp/src/agents_remember/serving/response_contract.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/serving/response_contract.py`  |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-08-09T03:51+02:00|
| lastVerifiedCommitHash | `7463b97a560e39367b9e31a687f09ea3f4f6b9f6`              |
| lastVerifiedCommitDate | 2026-08-09T04:22:51+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving overview](overview.md)

## Purpose

`response_contract.py` is the declared response contract for every HTTP route the serving app
registers outside the structured-conversation package. Before it, **not one of the app's 61 HTTP
routes declared a `response_model`**: nothing anywhere said what `GET /api/files/read` answers
with, and nothing could fail when that answer drifted. This module holds the models; the routes
now name them; and the actual enforcement is `mcp/tests/test_serving_response_conformance.py`,
which drives each route through the real app and validates the body that actually came back.

## Code Commentary

### Logic

**Why declarations alone are not the gate.** FastAPI applies `response_model` only to values it
serializes itself — `fastapi.routing.get_request_handler` hands a `Response` instance straight
back and never reaches `serialize_response`. Of the 61 HTTP routes, **57** return a `Response`
subclass directly (`JSONResponse` / `Response` / `StreamingResponse`) and **two** —
`GET /api/stream` and `GET /api/events` — are async generators feeding an `EventSourceResponse`.
On all 59 the decorator contributes an OpenAPI schema and validates *nothing*. Only
`GET /api/terminal/sessions` and `GET /api/harnesses` return a bare `dict` and are therefore
validated by FastAPI itself. "Declare a model everywhere plus a test that no declaration is
missing" would have been green on day one and enforced nothing on 59 routes.

**`WireResponse`** cit:([`WireResponse`], mcp/src/agents_remember/serving/response_contract.py:88-100) is the strict base every model here derives from:
`alias_generator=to_camel`, `extra="forbid"`, `frozen=True`, `populate_by_name=True` — mirroring
`serving/conversation/models.WireModel`. `extra="forbid"` is what makes a conformance check able
to fail at all: a key the handler started emitting and nobody declared is a validation error,
not a silent addition.

**Refusal shapes** cit:([`StatusRefusal`, `HttpDetailRefusal`], mcp/src/agents_remember/serving/response_contract.py:111-115; mcp/src/agents_remember/serving/response_contract.py:186-191) are separate models rather than one "status + anything" envelope,
precisely because `extra="forbid"` would make a shared permissive model accept every shape and
pin none of them. cit:([`HttpDetailRefusal`], mcp/src/agents_remember/serving/response_contract.py:186-191) is the odd one out: it is FastAPI's own
`HTTPException` body, so it is a plain `BaseModel` with no alias generator.

**The two live-enforcement models.** cit:([`TerminalCatalogEntryWire`], mcp/src/agents_remember/serving/response_contract.py:280-360) declares 64 fields in
`TerminalCatalogEntry.to_json`'s exact emission order, and its route declares
`response_model_exclude_unset=True` so re-serializing reproduces that hand-rolled, *conditional*
body byte for byte instead of back-filling nulls the dashboard has never seen.
cit:([`DetectedHarnessesResponse`], mcp/src/agents_remember/serving/response_contract.py:374-377) is the other. These two are the routes where a
declaration change is a **behaviour** change: they used to be forward-compatible pass-through,
and with `response_model` + `extra="forbid"` they now answer HTTP 500
(`ResponseValidationError`) if the payload gains a key, loses a required one, or changes type.

**The mitigation is deliberate and named.** `TerminalCatalogEntry` carries 36 optional fields and
is actively grown, so a future leaf adding one to `to_json` and forgetting
`TerminalCatalogEntryWire` would take down the cockpit's session list. The failure is therefore
moved off the wire and into CI: `test_the_catalog_wire_model_covers_every_key_to_json_emits`
scans `to_json`'s emitted key set and asserts set EQUALITY against this model's aliases. That
fires the moment the field is added, before any payload carries it — strictly earlier than
either the runtime 500 or a conformance run whose fixture happens to populate the new field.

**Unions are declared where the route really answers in more than one shape**, and each is
discriminated where it can be: cit:([`CodeNode`, `OnboardingMeta`, `OnboardingResolution`], mcp/src/agents_remember/serving/response_contract.py:628-628; mcp/src/agents_remember/serving/response_contract.py:657-657; mcp/src/agents_remember/serving/response_contract.py:721-727) (`Field(discriminator="kind")` — only a
`kind: "file"` row may carry `language`/`hasSidecar`, and only it must), cit:([`OnboardingMeta`], mcp/src/agents_remember/serving/response_contract.py:657-657),
cit:([`OnboardingResolution`], mcp/src/agents_remember/serving/response_contract.py:720-726) (the five shapes `GET /api/files/onboarding` answers with),
and cit:([`SubmissionLookup`], mcp/src/agents_remember/serving/response_contract.py:958-960).

**Three shared `responses={...}` tables** close the module, declared once because the refusal
idiom is shared, and each route adds only the statuses it can actually produce:

- cit:([`SCOPED_READ_RESPONSES`], mcp/src/agents_remember/serving/response_contract.py:1068-1074) — the files / notes / change-set family, whose
  `run_scoped` and its two siblings map every domain error onto exactly 400 and 404.
- cit:([`SESSION_CONTROL_RESPONSES`], mcp/src/agents_remember/serving/response_contract.py:1078-1085) — every `harness_control_api` route, where
  `_control_route` resolves the seat and `_control_failure_response` answers control failures
  (404 / 409 / 503).
- cit:([`ACTION_RESPONSES`], mcp/src/agents_remember/serving/response_contract.py:1090-1098) — `/api/actions/{action}`: the evaluator's refusals plus the
  not-ready projection as an `HttpDetailRefusal`.

cit:(["TerminalCleanupResult.model_rebuild()", `TerminalCleanupResult`, `TerminalCleanupSkip`], mcp/src/agents_remember/serving/response_contract.py:432-439; mcp/src/agents_remember/serving/response_contract.py:442-446; mcp/src/agents_remember/serving/response_contract.py:1102-1102) is not decoration: `TerminalCleanupResult`
references `TerminalCleanupSkip`, which is declared after it.

### Conventions

Every model is strict (`extra="forbid"`), immutable (`frozen=True`), and camel-aliased — an
undeclared key is a failure, which is the entire point. cit:([`__all__`], mcp/src/agents_remember/serving/response_contract.py:80-85) lists only the three
shared tables and `WireResponse`; the individual models are imported by name from the route
modules and are deliberately not re-exported wholesale.

**What is here and what is not — this file declares no route.** It holds **93 model classes** plus
the three shared `responses={...}` tables, and nothing else. The `response_model=` kwargs themselves
sit on the route decorators, spread across **eight** modules: `serving/app.py` (17),
`serving/conversation/control/api.py` (17), `serving/harness_control_api.py` (10),
`serving/conversation/library/api.py` (5), `serving/files.py` (4), `serving/changeset.py` (3),
`serving/conversation/active/api.py` (3), `serving/notes.py` (2). The three conversation modules name
models from the sibling `serving/conversation/response_contract.py` rather than from here (only
`StatusRefusal` crosses over, into `conversation/control/api.py`). So "which model does this route
declare" is answered in the route module, never by reading this one.

### Invariants And Boundaries

- **Import order is a hard constraint, not a preference.** The conversation surface's own
  additions live in `serving/conversation/response_contract.py` because they need
  `conversation/models.py`, and this module must stay importable *before* that package exists —
  `serving/app.py` imports the files / change-set / notes routes first.
- **Exemptions are found by structure, never by name.** `WS /api/terminal/{session}` is
  registered as a `fastapi.routing.APIWebSocketRoute`, which has no `response_model` parameter at
  all — a websocket has no response body to model. That is the only route without a declaration,
  and the exhaustiveness test finds it by route *class*, so a future undeclared HTTP route cannot
  hide behind a path skip-list.
- **The route inventory is pinned.** cit:([`test_the_declared_surface_is_the_whole_surface`], mcp/tests/test_serving_response_conformance.py:537-542) asserts
  `len(self.http) == 61` — 62 route decorators, 61 HTTP plus the one websocket — so a new
  route cannot be added without meeting this contract.
- **Declaring is not enforcing, and the module says so.** Rewriting the 59 handlers FastAPI does not
  validate — the 57 returning a `Response` subclass **and the two SSE generators** — to return models
  instead would hand enforcement to FastAPI, but it cannot be done: the bare `304` branch on
  `/api/state`, the per-status typed refusals, and the 200/202/422 fan-out of `/conversation/submit`
  each choose a status *and* a body shape that a single return type cannot express.
- **Multi-shape routes declare the success shape as `response_model` and every refusal under
  `responses={...}`** — the union members are the exact bodies the handler can emit, never a
  generic error envelope.

## 260713-TES-L2 Current Delta — Catalog Turn-Truth Wire Fields

`TerminalCatalogEntryWire` gained the eleven catalog turn-truth fields in emission order
cit:([`terminal_outcome`], mcp/src/agents_remember/serving/response_contract.py:342-354): `terminal_outcome`, `terminal_outcome_at`, `terminal_evidence_id`,
`interrupted_by`, `terminal_evidence_sequence`, `terminal_native_cursor`,
`interrupt_requested_by`, `interrupt_requested_at`, `interrupt_requested_turn_id`,
`state_signal_emitted_for`, and `non_reaction_emitted_for`. The key-set pin in
`test_serving_response_conformance.py` moved from 52 to 63, so a future `to_json` growth still
fails CI before any wire 500.

## 260713-TES-L3 Current Delta — Compound-Idle Wire Field

`TerminalCatalogEntryWire` gained `compound_idle_emitted_for`
cit:([`compound_idle_emitted_for`], mcp/src/agents_remember/serving/response_contract.py:356-356) in emission order after `non_reaction_emitted_for`; the
key-set pin in `test_serving_response_conformance.py` moved from 63 to 64. The catalog row's
marker stores the compound-idle episode signature (see `terminal_catalog.py.md`).

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

### Todos

The runtime 500 hazard on `GET /api/terminal/sessions` is a live, accepted trade rather than a
closed issue: the CI key-set equality test is what keeps it from ever being the first thing that
notices, and any future growth of `TerminalCatalogEntry.to_json` must land in
`TerminalCatalogEntryWire` in the same change.

## Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available. FastAPI's `response_model` behaviour is proven here
against the repository's own routing code and conformance suite rather than an external
document.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The models are declared here and consumed by the four serving route modules; the enforcement is
one suite, and the one live-validated model has its own producer-parity test.

| Finding | Anchor | Source |
| --- | --- | --- |
| The app routes that name these models, including the two FastAPI-validated bare-`dict` routes and the single undeclared websocket. | `api_terminal`, `api_terminal_sessions`, `api_harnesses` | mcp/src/agents_remember/serving/_app_terminal_routes.py:134-136; mcp/src/agents_remember/serving/_app_terminal_routes.py:142-150; mcp/src/agents_remember/serving/_app_terminal_routes.py:153-155 |
| The files routes consuming `RepoCatalog` / `DirectoryListing` / `FileContents` / `OnboardingResolution` under `SCOPED_READ_RESPONSES`. | `register_files_routes` | mcp/src/agents_remember/serving/files.py:296-325 |
| The change-set routes consuming `TaskChangeSet` / `LeafChangeSet` / `FileDiff` / `MasterChangeSet`. | `register_changeset_routes` | mcp/src/agents_remember/serving/changeset.py:501-554 |
| The notes routes consuming `NotesListing` / `NoteContents`. | `register_notes_routes` | mcp/src/agents_remember/serving/notes.py:168-177 |
| The harness-control routes consuming `SESSION_CONTROL_RESPONSES` plus the submit/interaction extra refusals. | `register_harness_control_routes`, `_control_route`, `_control_failure_response` | mcp/src/agents_remember/serving/harness_control_api.py:182-217; mcp/src/agents_remember/serving/harness_control_api.py:465-485; mcp/src/agents_remember/serving/harness_control_api.py:488-493 |
| The producer this contract's one live-validated model must stay key-for-key equal to. | `to_json` | mcp/src/agents_remember/serving/terminal_catalog.py:255-324 |
| The enforcement: the route inventory pin, the declaration exhaustiveness test, the catalog key-set equality test, and `validate_wire`'s `by_name=False` alias-only validation. | `validate_wire` | mcp/tests/test_serving_response_conformance.py:211-231 |
| The gate-decision body `ActionAccepted` carries through on an accepted gate verb. | `GateDecideResponse` | mcp/src/agents_remember/models/gates.py:36-44 |

## Cross-Repo References

No external repository boundary is declared here; every model describes a body this repository's
own serving app emits over localhost.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: recorded the `compound_idle_emitted_for`
  wire field (64-key pin, emission order after `non_reaction_emitted_for`) and updated the
  live-enforcement model count to 64 fields. Verification metadata pinned until closeout
  stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the eleven new
  `TerminalCatalogEntryWire` fields (63-key pin) carrying the catalog turn truth onto the
  sessions wire. Verification metadata pinned until closeout stamps the 260713-TES-L2 commit.
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
