# mcp/tests/test_serving_terminal_catalog_read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_serving_terminal_catalog_read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T13:57+02:00 |
| lastVerifiedCommitHash | `a7076008db4772554123794392f84b51143004ec` |
| lastVerifiedCommitDate | 2026-09-18T16:14:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

Reviewed at 2026-09-15T13:57+02:00 against the leaf base `67b21aeb`; the module itself is an
uncommitted candidate at that base, so normal closeout owns the final verification-metadata stamping
and the hash above records only the base the card was read against.

## Purpose

This integration-lane module is the regression proof that `GET /api/terminal/sessions` **projects**
the stored terminal catalog and never produces it. Every case drives the real registered route
through the real composed app (`create_app`) or the real route-registration function, so it fails if
the request path regains any producer behaviour: a liveness sweep, an adapter probe, an evidence
cursor advance, a catalog row mutation, or a compaction.

The load-bearing distinction is instrument **reach**, which the module states for each instrument
instead of implying one total guarantee.

## Code Commentary

### Logic

Routes are entered through `_RouteUnderTest`, which composes the production catalog, the production
sweeper, and the production route registration over a temporary catalog file, then records the file's
bytes before and after. Four instruments cover disjoint paths by which this process can reach a
seat's adapter or its store:

- `_ProbeLedger` counts each observation instrument the **sweeper's** injected `LivenessProbe` uses,
  so "zero adapter evidence reads" is counted for the producer rather than inferred from the absence
  of a sweep.
- `_ReaderLedger` counts at the **readers themselves**, which is the one place a route-side read and
  a sweeper-side read have in common. `_reader_patch_targets()` composes its patch set from two
  binding shapes and neither alone is sufficient: `_READER_SEAMS` covers the plain names a read
  resolves when it is bound **by name** (the route module's own globals, installed with
  `create=True`, plus the canonical attributes on `harness_control_client` and
  `terminal_evidence`), and an identity sweep over every loaded `agents_remember` module matches
  globals whose value **is** one of `_PRODUCTION_READERS`, reached with `is` and never by name. That
  second shape is what catches a module-level `from … import reader as alias`: the aliased global
  *is* the function object, so patching names misses it and rebinding the defining module does not
  touch it either. Seven targets result, deduplicated per `(module, attribute)`. `_counting_reader`
  counts first and **delegates** to the production reader, so a mutating candidate fails on the count
  rather than on an exception the double invented.
- `_RecordingCatalog` subclasses the real `TerminalCatalog` and counts `_write_disk` — the one seam
  every durable write passes through — plus the port calls a caller asks for. Subclassing rather than
  proxying keeps the ledger honest: a write is reachable only through a real method.
- `_RecordingSweeper` counts invocations and can stand in for a stale or failing observer.

The ten cases group by claim: `StoredSnapshotProjectionTests` issues one hundred GETs and asserts
one hundred equivalent answers with every ledger at zero; `ProducerSeparationTests` splits probe,
cursor advance, row mutation and compaction into four cases, each on its own instrument rather than
as one aggregate; `RouteSeamReaderTests` pins the no-probing clause where the request path would have
to reach for it; `ObserverIndependenceTests` proves the catalog changes between two reads because the
background observer ran, and that an observer which has failed still serves the stored snapshot
instead of being repaired by the request; `RequestPathPurityGuardTests` is the negative guard that no
request enters a catalog producer; and `RouteContractStabilityTests` drives the composed app to pin
path, declared model, conditional-key behaviour and status semantics.

### Conventions

`unittest.TestCase` through `_ProjectionTestCase`, with temporary catalogs under `tempfile` and a
`FastAPI` + `fastapi.testclient.TestClient` surface rather than a parallel fake of the production
seams. The module issues real HTTP requests, so it is classified in the repository's `integration`
evidence lane (`mcp/tests/test-evidence-lanes.toml:172`) — its `TestClient` neighbours, not the
hermetic unit-lane liveness modules. It starts no process, opens no socket, and publishes nothing.
Focused host results are development evidence and grant no certification authority.

### Invariants And Boundaries

The route must keep serializing `runtime.catalog.list()` under the unchanged
`TerminalSessionsResponse` declaration with `response_model_exclude_unset=True`; re-adding
`runtime.liveness_sweeper.refresh()`, advancing a cursor, mutating a row, compacting, or adding an
adapter read during serialization each fails a named case. Two limits are deliberate and recorded
rather than papered over. First, **the reader instrument's reach is bounded by binding shape**: a
reader reached through anything that is not a module global — a function default such as
`LivenessProbe`'s `snapshot_reader` field, a closure cell, a class attribute, a dict entry, an
instance attribute — is invisible to `_ReaderLedger`; the argument-path shapes of those are covered
by the tmux counter and `record_liveness_probe` instead, and the residue was measured by the
independent reviewer as a disclosed limit banked for a hardening leaf. The module therefore claims
"no module-global reader binding reaches the request path", not "no read of any shape is possible".
Second, `test_one_hundred_gets_produce_one_hundred_equivalent_answers` is content-vacuous on its own
(an empty catalog would also give one unique response text); content is pinned by
`RouteContractStabilityTests` and the failed-observer case, so the suite is not vacuous overall but
that one case must not be cited alone as content evidence.

### Todos

None. Closing the disclosed binding-shape residue means patching a seam both shapes share (the
`harness_control_client` transport/exchange function) rather than the reader bindings, which is a
scope decision owned by a separate hardening leaf and not by this module.

## Docs References

No Domain Documentation entries are configured in the resolved memory root. The module tests
repository-owned serving behaviour, so no external domain claim is needed.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

The cases are grounded in the production route, its catalog port, and the readers a route-side read
would have to reach; these references describe the behaviour under test and do not claim a
certification result.

| Finding | Anchor | Source |
| --- | --- | --- |
| The catalog GET is a projection of stored state and names no sweeper. | `api_terminal_sessions` | mcp/src/agents_remember/serving/_app_terminal_routes.py:162-168 |
| The route serializes each row through the shared payload helper. | `_catalog_payload` | mcp/src/agents_remember/serving/_app_common.py:362-363 |
| `list()` takes the catalog `RLock` before testing `self._batch`, so a foreign thread waits for an in-flight batch and then reads the committed atomic file. | `list`; `_read_snapshot` | mcp/src/agents_remember/serving/terminal_catalog.py:80-84; mcp/src/agents_remember/serving/terminal_catalog.py:364-372 |
| The batch holds both the exclusive file lock and the `RLock` across the whole unit of work, so the in-memory buffer is reachable only reentrantly by the batch-owning thread. | `batch` | mcp/src/agents_remember/serving/terminal_catalog.py:282-313 |
| `_write_disk` is the one seam every durable write passes through, which is why the write ledger is complete regardless of the port method used. | `_write_disk` | mcp/src/agents_remember/serving/terminal_catalog.py:422-432 |
| `list_committed()` is the sweeper's own non-blocking contention read, called only from the two contention paths — not a projection read. | `list_committed` | mcp/src/agents_remember/serving/terminal_catalog.py:86-92 |
| The production readers the identity sweep resolves against by object identity. | `read_control_snapshot`; `read_entry_terminal_evidence` | mcp/src/agents_remember/serving/harness_control_client.py:133-142; mcp/src/agents_remember/serving/terminal_evidence.py:187-196 |
| The sweeper whose re-introduction on the request path the module's cases detect. | `TerminalCatalogLivenessSweeper`; `refresh` | mcp/src/agents_remember/serving/terminal_liveness.py:149-322 |
| The candidate classifies this module once, in the explicit integration lane. | "mcp/tests/test_serving_terminal_catalog_read.py" | mcp/tests/test-evidence-lanes.toml:247-247 |
|  The sweeper whose re-introduction on the request path the module's cases detect. | `TerminalCatalogLivenessSweeper` | mcp/src/agents_remember/serving/terminal_liveness.py:149-322  |
| The candidate classifies this module once, in the explicit integration lane. | "mcp/tests/test_serving_terminal_catalog_read.py" | mcp/tests/test-evidence-lanes.toml:247-247 |

## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned
regression module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_serving_terminal_catalog_read.py" repointed to mcp/tests/test-evidence-lanes.toml:247-247. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_serving_terminal_catalog_read.py" repointed to mcp/tests/test-evidence-lanes.toml:247-247. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_serving_terminal_catalog_read.py" repointed to mcp/tests/test-evidence-lanes.toml:245-245. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_serving_terminal_catalog_read.py" repointed to mcp/tests/test-evidence-lanes.toml:245-245. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_serving_terminal_catalog_read.py" repointed to mcp/tests/test-evidence-lanes.toml:243-243. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_serving_terminal_catalog_read.py" repointed to mcp/tests/test-evidence-lanes.toml:243-243. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_serving_terminal_catalog_read.py" repointed to mcp/tests/test-evidence-lanes.toml:221-221. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_serving_terminal_catalog_read.py" repointed to mcp/tests/test-evidence-lanes.toml:219-219. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 6 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_serving_terminal_catalog_read.py`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 3 generated projection bullet(s) by hand** — `mcp/tests/test_serving_terminal_catalog_read.py`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_serving_terminal_catalog_read.py"` → `mcp/tests/test-evidence-lanes.toml:212-212`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/test-evidence-lanes.toml:210-210` -> `mcp/tests/test-evidence-lanes.toml:211-211`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-17T20:42:17+00:00: Generated citation repair: `api_terminal_sessions` repointed to mcp/src/agents_remember/serving/_app_terminal_routes.py:162-168. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_catalog_payload` repointed to mcp/src/agents_remember/serving/_app_common.py:362-363. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_serving_terminal_catalog_read.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-15T11:57:00+00:00 — 260831-LOCR-L02 curator: created this file card for the leaf's new
  catalog-read regression module. Recorded what it protects (the GET route is a projection of stored
  state: no sweep, no adapter probe, no cursor advance, no row mutation, no compaction, unchanged
  path/model/conditional-key/status semantics), the four instruments and the two binding shapes the
  reader ledger needs, the negative guard, and — explicitly — the two limits the module does not
  claim: the reader instrument's binding-shape residue and the 100-GET case's content-vacuity in
  isolation. This module is ordinary version-controlled test source, so it carries no
  evidence-lifecycle registration. Verification remains closeout-owned because the source is an
  uncommitted candidate; the pinned hash records only the base the card was reviewed against.
