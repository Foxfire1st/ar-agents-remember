# mcp/tests/migration_census_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/migration_census_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `47570cd827428c171613c8cb01e01f0b1cb26f73`|
| lastVerifiedCommitDate |  2026-09-20T01:58:41+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The migration-census cases' shared fixture: one initialized candidate dataset whose every identity was
produced by the shipped candidate batch operation, its namespace, its authored route and its frozen
baseline, plus the command builders and the seed that write the corpus the census's cases measure. The
fixture is a small **real** corpus rather than a rich one, because what the cases have to distinguish
is state rather than scale: four artifacts and five claims carry a parsed card, an artifact that did
not parse, a card whose declared source is absent at the baseline, a route overview, a supported claim,
a contradicted claim, a piece recorded outside the cohort, and one claim text recorded twice.

## Code Commentary

### Logic

**Every record this fixture holds is written through the shipped application entry point, because a row
inserted directly would let the cases test arithmetic against a state the real write path cannot
produce.** The docstring states the reason and the shape: the census is a read over records the one
candidate batch operation wrote, so `CensusHarness.apply` builds a `ChangeBatch` around a freshly
resolved `CandidateResolution` and hands it to `change_knowledge_candidate`; the namespace is created
by `initialize_knowledge_namespace` and the fixture's single route is authored by the shipped
`author_route` over a `RouteDraft`. Nothing in the module issues a raw `INSERT`, and the only place a
census payload is constructed is inside a command model the write path will validate.

**`census_harness` is the one entry point, and it yields a frozen `CensusHarness` binding six facts:**
the database path under a `tempfile.TemporaryDirectory`, a `RepositoryIdentity` whose id is a fresh
`uuid4()`, the `Authorship` written by `write_authorship` under `authorization_ref`
`requirement:KS-R21@v1`, the `destination` returned by `admitted_knowledge_destination`, the authored
`route_id`, and the validated `FrozenBaseline`. The dataset is initialized once and the fixture asserts
its own preconditions rather than passing silently: a namespace that was not `created`, a route the
writer refused and a seed the batch refused each raise an `AssertionError` naming the refusal, and all
three are marked `pragma: no cover` because the ids and drafts above them are exact.

**The harness's four methods are its whole vocabulary, and each one exists to remove a way a case could
be written wrong.** `context()` re-resolves a `CandidateResolution` on every call, because a successful
batch makes the previous context stale — a case that reused one would assert against a snapshot the
dataset has already moved past. `store()` opens the dataset for reading through
`open_admitted_knowledge_store`, so a case reads what the write path stored rather than what it
submitted. `apply()` is the only write route and it always goes through `change_knowledge_candidate`.
`provenance()` builds one artifact's `CensusProvenance` at the context's own knowledge baseline, which
is why every command carries the same frozen baseline without a case having to thread it through.

**`_validated_baseline` and `_author_route` are the two shared setup steps, and both go through the
factory or writer that would refuse a bad input.** `_validated_baseline` calls
`require_frozen_baseline(CODE_TREE, MEMORY_TREE)` — two forty-character object-id strings, `"a" * 40`
and `"b" * 40`, because a baseline whose side is a ref name is not frozen — and raises when the factory
returns a refusal. `_author_route` opens the store, authors the fixture's one route through
`author_route` and returns the authored id, raising with the refusal if the writer refused, and closes
the store in a `finally` block so a failure cannot leak the connection.

**The builders are thin and total, and the two specs exist so a builder takes one value rather than
eight.** `InventoryRowSpec` carries an inventory row's declared facts with the observed doc type
defaulting to `file-level-onboarding` and the artifact kind to `file_level_onboarding`;
`inventory_row_for` turns one spec into a `CensusInventoryRowCommand` with fresh `uuid4()` record and
revision ids, the fixture's route as its governing route, and a provenance at the spec's location.
`ClaimSpec` carries a claim's text, its curator-authored kind, its applicability, its disposition and
an optional assessment and realization state; `claim_command_for` builds the `CensusClaimCommand` with
exactly one `CensusClaimEvidence` whose `evidence_state` is `assessed` when a verdict was supplied and
`unassessed` when it was not, and with a realization only when `realization_state` was given.
`disposition_command_for` builds one `recorded` migration disposition, and `link_command_for` derives
one from it with a `CensusDispositionLink` pointing at a record the caller names.

`seed_census` is the fixture's contract in executable form: four inventory rows, five claims and four
dispositions in one batch. The rows are the parsed card with its declared source, the generated
artifact that did not parse with its observed content, the card whose declared source is absent, and
the route overview; the claims are a supported one, a contradicted one, a historical piece whose
applicability is `historical_non_applicable` and whose disposition is `historical`, and the repeated
text recorded twice at two locations; the dispositions cover the parsed card, the unparsed artifact,
the absent-source card and one artifact under an `unmapped/` path. The constants above them are the
fixture's shared vocabulary — four artifact paths, three claim texts, the repeated claim text, the
addressed route and the two tree ids — so a case can name the state it is asserting against instead of
repeating a literal.

### Conventions

- **Lane and marker.** `mcp/tests/test-evidence-lanes.toml:128` files this leaf's case module under
  `unit-regression`, and this file declares no `pytestmark` of its own: it defines no `test_` function,
  so it contributes no case to any population and cannot be counted as coverage.
- **This file is a registered durable artifact, not an unregistered helper.** It is
  `contract:migration-census-cases` with an owning `[[contract]]` row and a `[[artifact]]` row in
  `mcp/tests/evidence-lifecycle.toml` — kind `shared-support`, authority `internal-canonical`,
  category `unit-regression`, fidelity `local-composition`, cadence `affected`,
  `introduced_by = "260915-KS-L21"`, lifetime `permanent`, `consumer_scope = "exact"` with exactly its
  one consuming module named. Its executable evidence node is
  `mcp/tests/test_migration_census.py::test_the_seed_writes_every_census_record_kind_through_the_shipped_batch_operation`,
  and the artifact row's own `introduced_by` names this leaf as its introducer while the catalogue's
  pinned populations stand at fifteen contracts and sixty-five artifacts against a pinned digest.
- **Imports come from the shipped surfaces.** The application seam, the route writer and store, the
  migration baseline factory, and the census payload, command and link models are imported by their
  public names; the fixture imports no private name of the production package.
- **The fixture is disposable and its identifiers are fresh.** Every run builds its dataset under a new
  `TemporaryDirectory` with a new repository id, route id, and record and revision ids, so nothing in
  the fixture depends on a previous run's state or on a shared path.
- **Setup failure is loud.** The three `pragma: no cover` guards exist so that a change to the shipped
  write path surfaces as an `AssertionError` carrying the refusal rather than as a confusing case
  failure further away.

### Invariants And Boundaries

- **Every identity is produced by the shipped write path.** No row is inserted directly, and no bulk
  writer exists beside `change_knowledge_candidate`; a fixture that fabricated rows would test the
  census's arithmetic against a state the real write path refuses.
- **The baseline is two exact object ids.** `CODE_TREE` and `MEMORY_TREE` are forty-character strings
  validated through `require_frozen_baseline`, because a baseline whose side is a ref name is not
  frozen and would move with a commit.
- **A context is re-resolved per batch.** The harness's `context()` is called fresh every time, because
  a successful batch makes the previous context stale.
- **The dataset is real and it is closed.** The fixture holds a real APSW-backed SQLite file under a
  temporary directory, and every store it opens is closed in a `finally` block.
- **One evidence record per claim, and one realization only when one was declared.** The evidence state
  is `assessed` exactly when a curator's verdict was supplied, so an unassessed claim is a state the
  fixture can produce and not an omission a case has to invent.
- **The corpus is the fixture's contract.** Four inventory rows, five claims, four dispositions, and
  the exact states the census's cases separate; a change to that shape is a contract change, not a
  convenience edit.
- **The fixture is not a test module.** It defines no `test_` function, so it adds no case to any
  population, and it is registered as an artifact precisely so its blast radius is measured rather than
  assumed.
- **A refused setup is an assertion failure, never a silent pass.** The namespace, the route and the
  seed each carry a guard that raises with the refusal's own code.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The docstring states why the fixture writes through the shipped path and why the corpus is small and real rather than rich: what the cases must distinguish is state, not scale. | `change_knowledge_candidate` | mcp/tests/migration_census_test_support.py:1-13 |
| The four artifact paths and the addressed route are the fixture's shared vocabulary, so a case names the artifact it is asserting against rather than repeating a literal. | `PARSED_CARD`; `UNPARSED_ARTIFACT`; `ABSENT_SOURCE_CARD`; `ROUTE_OVERVIEW`; `ADDRESSED_ROUTE` | mcp/tests/migration_census_test_support.py:57-71 |
| The three claim texts and the one repeated text are the states the accounting has to separate: supported, contradicted, historical, and one text recorded twice. | `SUPPORTED_CLAIM_TEXT`; `CONTRADICTED_CLAIM_TEXT`; `HISTORICAL_CLAIM_TEXT`; `REPEATED_CLAIM_TEXT` | mcp/tests/migration_census_test_support.py:63-69 |
| The two tree ids are exact object ids rather than refs, because a baseline whose side is a ref name is not frozen. | `CODE_TREE`; `MEMORY_TREE`; `require_frozen_baseline` | mcp/tests/migration_census_test_support.py:73-76; mcp/src/agents_remember/memory/migration/baseline.py:90-125 |
| The harness type binds the six facts a case needs — the database path, the repository identity, the admitted destination, the authorship, the authored route and the validated baseline. | `CensusHarness`; `RepositoryIdentity` | mcp/tests/migration_census_test_support.py:79-88 |
| The context is re-resolved on every call, because a successful batch makes the previous context stale. | `context`; `CandidateResolution`; `resolve_candidate_context` | mcp/tests/migration_census_test_support.py:90-102; mcp/src/agents_remember/application/knowledge.py:267-289 |
| The harness's remaining three methods are its whole surface: it opens the dataset for reading through `open_admitted_knowledge_store`, resolves a fresh context and hands one `ChangeBatch` to the shipped entry point, and builds one artifact's provenance at its own frozen baseline so every command carries that baseline without a case threading it through. | `open_admitted_knowledge_store`; `ChangeBatch`; `change_knowledge_candidate`; `provenance`; `CensusProvenance` | mcp/tests/migration_census_test_support.py:104-124; mcp/src/agents_remember/application/knowledge.py:208-221; mcp/src/agents_remember/application/knowledge.py:318-341; mcp/src/agents_remember/models/knowledge/census.py:106-146 |
| `census_harness` is the single entry point: a temporary directory, a fresh repository id, an authorship under `requirement:KS-R21@v1`, an initialized namespace, an authored route and a validated baseline, yielded as one harness. | `census_harness`; `write_authorship`; `initialize_knowledge_namespace`; `admitted_knowledge_destination` | mcp/tests/migration_census_test_support.py:127-154; mcp/src/agents_remember/application/knowledge.py:117-139; mcp/src/agents_remember/application/knowledge.py:140-158; mcp/src/agents_remember/application/knowledge.py:175-207 |
| A namespace that was not created, a route the writer refused and a seed the batch refused each raise with the refusal's own code, so a change to the shipped write path surfaces as a named assertion failure. | `_validated_baseline`; `_author_route` | mcp/tests/migration_census_test_support.py:157-163; mcp/tests/migration_census_test_support.py:166-184 |
| The fixture's one route is authored through the shipped writer over a `RouteDraft`, and the store that writer was given is closed in a `finally` block. | `author_route`; `RouteDraft`; `finally` | mcp/tests/migration_census_test_support.py:166-184; mcp/src/agents_remember/memory/knowledge/routes.py:176-184; mcp/src/agents_remember/memory/knowledge/routes.py:250-306 |
| The inventory-row spec and its builder keep one row's declared facts in a value, so the builder takes a spec rather than eight arguments and returns a real command with fresh record and revision ids, the fixture's route as its governing route, and a provenance at the spec's location. | `InventoryRowSpec`; `inventory_row_for`; `CensusInventoryRowCommand`; `CensusInventoryRowPayload` | mcp/tests/migration_census_test_support.py:187-199; mcp/tests/migration_census_test_support.py:215-241; mcp/src/agents_remember/models/knowledge/census.py:147-194; mcp/src/agents_remember/models/knowledge/census.py:290-305 |
| `ClaimSpec` carries one claim's declared facts and its optional curator verdict, including the realization state that decides whether a realization row exists at all. | `ClaimSpec` | mcp/tests/migration_census_test_support.py:201-212 |
| `inventory_row_for` turns one spec into a real command with fresh record and revision ids, the fixture's route as its governing route, and a provenance at the spec's location. | `inventory_row_for`; `CensusInventoryRowCommand`; `CensusInventoryRowPayload` | mcp/tests/migration_census_test_support.py:215-241; mcp/src/agents_remember/models/knowledge/census.py:147-194; mcp/src/agents_remember/models/knowledge/census.py:290-305 |
| `claim_command_for` records exactly one evidence row per claim — `assessed` when a verdict was supplied and `unassessed` when it was not — and a realization only when one was declared. | `claim_command_for`; `CensusClaimEvidence`; `CensusClaimRealization` | mcp/tests/migration_census_test_support.py:244-289; mcp/src/agents_remember/models/knowledge/census.py:239-259; mcp/src/agents_remember/models/knowledge/census.py:260-273 |
| `disposition_command_for` builds one `recorded` migration disposition, and `link_command_for` derives one whose `CensusDispositionLink` points at a record the caller names. | `disposition_command_for`; `link_command_for`; `CensusDispositionLink` | mcp/tests/migration_census_test_support.py:292-310; mcp/tests/migration_census_test_support.py:402-419; mcp/src/agents_remember/models/knowledge/census.py:274-289 |
| `seed_census` is the fixture's contract in executable form, written as one batch: four inventory rows, five claims, four dispositions, and a refusal guard that raises with the batch's own refusal. | `seed_census` | mcp/tests/migration_census_test_support.py:313-399 |
| **The registered rows that make this file governed evidence:** the `migration-census-cases` contract names this file as its owner and the seed case as its evidence node, and the artifact row names its kind, its authority, its category, its fidelity, its introducer, its lifetime, its exact consumer scope and its one consumer. | `migration-census-cases`; `evidence_node`; `shared-support`; `260915-KS-L21`; `contract:migration-census-cases`; `mcp/tests/test_migration_census.py` | mcp/tests/evidence-lifecycle.toml:74-77 |
| The catalog's pinned populations stand at fifteen contracts and sixty-five artifacts against a pinned digest, and the case module this fixture serves is the `unit-regression` lane member carrying the leaf's 48 cases. | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256`; `unit-regression` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-46; mcp/tests/test-evidence-lanes.toml:5-5 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Its inputs are this repository's own
application seam, route writer and census models, plus a temporary directory the fixture creates and
owns; the frozen baseline it binds is a pair of object-id **strings**, and no case it supports reads a
second repository, a network or a Git object.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `migration_census_test_support.py.md:166` (`evidence_node`).
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the shared support module the census's 48 cases build on. It records that the fixture produces every identity through `change_knowledge_candidate` rather than by inserting rows, because the census is a read over records the one candidate write path produced and the states its accounting must separate — a claim with no assessment, a curator's recorded verdict, a piece outside the cohort, one claim text recorded twice, an artifact that did not parse and a card whose declared source is absent — are not states a row-inserting fixture can reach. It records the harness's five bound facts and its four methods, including the deliberate re-resolution of the context on every call because a successful batch makes the previous one stale; the two setup steps that go through `require_frozen_baseline` and the shipped route writer; the two specs and the three command builders that keep one evidence row per claim and create a realization only when one was declared; and `seed_census` as the fixture's corpus written as a single batch behind a refusal guard. It also records the registry work this leaf carries: the `migration-census-cases` contract owning this file with the seed case as its executable evidence node, the `shared-support` artifact row with `consumer_scope = "exact"` and one named consumer, and the `unit-regression` lane member — with the catalogue's pinned populations standing at fifteen contracts and sixty-five artifacts. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
