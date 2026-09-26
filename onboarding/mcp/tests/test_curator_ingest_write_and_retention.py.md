# mcp/tests/test_curator_ingest_write_and_retention.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_ingest_write_and_retention.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T17:20:00+02:00 |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d` |
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview.md](overview.md)

## Purpose

One curator ingest run's own **writes, retentions, replays and refusals**: nine cases over a real pair of
repositories beside a real contract, measuring what one run of the operation actually does to the store
rather than what its plan intended. Eight drive `ingest_curator_list` directly and the ninth drives the
curator's own command line, so the ordinary CLI route is measured and not only the application seam.

**Why it exists as a module of its own.** `260921-ICR-L32` extracted it from
`mcp/tests/test_curator_family_authoring.py`, which crossed the repository's 1200-line hard rail during
`260921-ICR-L28`'s fix round (1056 lines and 15 cases when that leaf took its census, **1320** when it
landed). That breach violated L22's F5 ruling that the ≥1200 offender census must not gain a new offender,
so the purpose-named sibling restores the standing condition without widening a limit: the parent is
**818** lines, this module is **578**, and the census returns to **27** offenders under the rail's own
`git ls-files '*.py'` file set and **26** under the narrower `mcp/`-only scope (each number quoted with the
scope it was measured in, because the population is scope-dependent). The case population moved rather
than shrank: **20 collected across the pair** (11 + 9), the evidence catalog still reports **16 contracts /
66 artifacts**, and the two `consumer_scope="exact"` rows this module needed were derived from the shipped
census's own failing-run output — it named `mcp/tests/fixtures/repository_profiles/node/package-lock.json`
and `mcp/tests/snapshot_lifecycle_test_support.py` as missing exactly this path. See
`test_curator_family_authoring.py.md` for the parent's own record; the two cards share one story.

## Code Commentary

**The nine cases, and the fact each one pins.** Every case asserts a property of the store or of the
report, never of an internal call count.

| case | the fact it measures |
| --- | --- |
| `test_an_external_source_is_retained_in_a_manifest_and_never_becomes_a_git_anchor` | An external source survives the run as a **bounded manifest entry** named by the record's own origin reference, and **no source anchor is fabricated** for it — a URL is a declared source, not a repository path with a Git blob. |
| `test_a_declaration_whose_entry_is_refused_spends_no_identity` | A refused entry's allocated family identity is never recorded, so the journal cannot name a family the dataset did not receive. |
| `test_a_replayed_revision_still_writes_the_family_plane_its_entry_now_authors` | A replayed invariant revision does not skip the family plane the same run authors — the two planes are one run's work, not two passes. |
| `test_an_exact_replay_writes_nothing_and_spends_no_identity` | An exact replay writes no row, spends no identity and leaves the journal byte-identical. |
| `test_a_changed_no_family_basis_on_a_stored_revision_is_refused_by_name` | A **changed** no-family basis on an immutable stored revision is refused by name, while an exact retry of the recorded basis stays a replay — the refusal distinguishes a re-decision from a repeat. |
| `test_a_run_that_writes_nothing_retains_no_manifest_and_says_so` | A run that writes nothing retains **no manifest**, and the report says so while still carrying what the list declared: an empty result is reported as measured emptiness, not as a missing answer. |
| `test_a_source_with_neither_version_nor_retrieval_time_is_refused` | A source declaration findable again by neither version nor retrieval time is refused rather than stored as an unfindable row. |
| `test_a_planning_run_writes_no_family_row_and_says_so` | A **planning** run projects the family plane and writes neither a row nor a file — the dry run's write-nothing contract holds on the plane this module was split out to measure. |
| `test_the_curator_command_line_authors_the_family_plane_and_reports_it` | The curator's own **command line** reaches both planes and prints them, so the ordinary route a curator actually runs is measured end to end rather than only the seam beneath it. |

**The fixtures are siblings', imported rather than duplicated.** The authoring and read-back helpers come
from `test_curator_family_authoring` (`FAMILY_ALPHA`, `GUARANTEE_ALPHA`, `NO_FAMILY_BASIS`,
`OTHER_SYMBOL`, `candidate_of`, `citation`, `committed_revision`, `conditions_of`) and the list fixture
from `test_knowledge_curator_ingest_list` (`AUTHORIZATION`, `CODE_SYMBOL`, `GONE_PATH`, `SourcePair`,
`entry`, `pair`) — the sibling-fixture pattern this test tree already uses for shared support, and the
reason the two modules stay one logical suite even though the rail forced them into two files.

**Three local helpers keep the cases one claim wide.** `with_sources(one, sources)` attaches a source list
to a list entry, `source(...)` builds one declared source in its two findable forms, and
`provenance_of(database, revision_id)` reads back what a stored revision's provenance actually holds — so
each case states its input and its measured output without re-implementing the harness.

## Invariants And Boundaries

- The module's `pytestmark` is `pytest.mark.evidence_unit` (`:71`), and it carries its own lane row inside
  the `unit-regression` list of `mcp/tests/test-evidence-lanes.toml` (`:22`).
- It is registered as a consumer of the two artifacts the shipped census named, in
  `mcp/tests/evidence-lifecycle.toml` (`:698`, `:1284`), with `consumer_scope="exact"`. Both rows were
  **derived from the census's own findings**, not guessed: removing them reproduces the two
  `consumer proof differs from source-derived ownership` findings and nothing else.
- Nothing here re-implements the writer, the candidate resolution or the batch: the cases drive
  `ingest_curator_list` and the shipped CLI (`main`), and they read the store back through SQLite rather
  than trusting the report.
- A planning run is asserted to write **nothing**; a case that ever made planning write would be a
  behaviour change, not a test fix.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The admitted ingest plans per-entry outcomes and commits accepted operations through the existing batch owner. | `ingest_curator_list` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1111-1235 |
| The committed batch state the writing cases assert. | `COMMITTED` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:215-215 |
| The CLI entry point the ninth case drives, and the adapter that owns its arguments. | `main` | mcp/src/agents_remember/cli/__main__.py:73-75 |
| The sibling fixtures imported rather than duplicated: the family plane's authored meaning. | `candidate_of`; `conditions_of`; `committed_revision` | mcp/tests/test_curator_family_authoring.py:166-166; mcp/tests/test_curator_family_authoring.py:230-230; mcp/tests/test_curator_family_authoring.py:286-286 |
| The list fixture and the contract pair the cases are built on. | `SourcePair`; `pair`; `entry` | mcp/tests/test_knowledge_curator_ingest_list.py:166-166; mcp/tests/test_knowledge_curator_ingest_list.py:183-183; mcp/tests/test_knowledge_curator_ingest_list.py:346-346 |
| The lane row and the two consumer rows this module's extraction needed, both derived from the census's own failing-run output. | `unit-regression`; "consumer_scope = \"exact\"" | mcp/tests/test-evidence-lanes.toml:22-22; mcp/tests/evidence-lifecycle.toml:698-698; mcp/tests/evidence-lifecycle.toml:1284-1284; mcp/tests/evidence-lifecycle.toml:96-96 |
| The catalog pin the split re-took from a fresh `sha256sum`, with its population unchanged. | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| The parent this module was extracted from, whose own docstring points at this sibling's subject. | `test_curator_ingest_write_and_retention` | mcp/tests/test_curator_family_authoring.py:32-32 |

## Cross-Repo References

No cross-repository behavior is implemented in this file; the contract pair the cases build is a
disposable repository pair created by the imported fixture, not a configured external repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-26T22:01:44Z — Reconciled the ingest citation with the current admitted operation and its per-entry outcomes; verification stamps remain unchanged.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `main` repointed to mcp/src/agents_remember/cli/__main__.py:73-75. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **created.** This module is L32's extraction from the over-rail `mcp/tests/test_curator_family_authoring.py` (1320 lines at L28), and it had no card, which was the leaf's one `missingOnboardingCount`. The card records the nine cases and the fact each pins, the sibling-fixture imports that keep the two modules one suite, the three local helpers, the lane row, and the two `consumer_scope="exact"` rows derived from the shipped census's own findings. The line-count and census figures are quoted with their **scope** (27 rail's own, 26 `mcp/`-only; 16 contracts / 66 artifacts) because the population is scope-dependent. No verification stamp is advanced as a commit: the candidate is uncommitted, so the header's pair is the leaf's base commit plus this working-tree delta, and the governed closeout owns the real stamp.
