# mcp/tests/test_knowledge_review_resolution_and_route.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_resolution_and_route.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

**The Intent Reviewer surface's resolution and transport: which pair the surface serves, and how it
refuses.** These nine cases measure the boundary in front of the panes, not the panes themselves. They
drive the same real adapter over the same real two-snapshot comparison as
[`test_knowledge_review_surface.py`](test_knowledge_review_surface.py.md), reusing that module's
`REPOSITORY_LEAF`, `review_config`, `resolution_for`, `review_request` and `render`. `260921-ICR-L57`
moved them there verbatim when that module crossed the 1200-line rail; no case was added, dropped or
changed.

- **Resolution.** The candidate is resolved from canonical task context and never from a
  browser-chosen path. A resolution that cannot be made yields no fallback dataset and no fabricated
  record, and the entry list for the same unresolvable context refuses with the same code instead of
  answering empty.
- **Pair refusals.** An absent candidate dataset, an absent before half and a before half that is
  present but unreadable are each a typed refusal naming the side. This holds on the composition and on
  the entry route alike, instead of a substituted empty dataset or a storage error raised from inside
  the read.
- **Transport.** The request parser admits exactly the two reviewable selector kinds (an invariant or a
  family identity) and refuses every other spelling. The route serializes the port's own typed result,
  refuses by name with no adapter, and carries a refresh's previous comparison identity all the way to
  the composition that compares it.

**The before-half group (`260921-ICR-L5`).** Until that leaf, the surface's pair refusals were measured
only from the candidate's side. Three cases measure the other two states a before half can be in,
because a comparison is *between* two dataset files and a file that is not one used to make SQLite
raise from inside the read:

- **an absent before half refuses by name rather than being substituted with an empty one** — the state
  a cold-start repository reached until the first knowledge write established that side, and the state
  a leaf reaches when the fork point it named is missing;
- **a before half that is present but unreadable refuses by name** — the operator gets a state naming
  the side and the action instead of an `apsw.NotADBError` traceback, and the refusal names the
  *before* side specifically, since only one of the two sides can be repaired by authoring knowledge
  again;
- **the entry route refuses a damaged before half instead of raising** — the subject list is the first
  call a reader's surface makes and it compares every recorded identity against the pair, so the same
  corruption raised out of the route that exists to *offer* a subject.

The last one also proves the refusal is caused by the corruption rather than by a fixture that could
never answer: replacing the damaged side with the dataset that belongs there turns the same route into
an entry list.

## Code Commentary

### Logic

**`review_config` names no real root, so only the resolution's own refusals can answer.** It is imported
from the surface module. That is what makes the two candidate-resolution cases and the loader case
measure the resolver's behaviour rather than the host's filesystem.

**The three before-half cases build their own resolution, and the entry-route case builds its own task
context.** The two composition cases reuse the fixture's `DiffFixture` but hand `compose_review` a
`ReviewCandidateResolution` whose `baseline_database` is a path the case owns — an absent one, then a
file holding `b"this is not a database\n"` — so the pair is real on the candidate side and deliberately
unusable on the before side, and each asserts the typed refusal plus the fact that the refused review
did not create or rewrite the side it was asked about. The entry-route case cannot do that: the route
resolves its pair from canonical task context and the browser never names a dataset, so
`_entry_route_config` **is** that context — a coordination root, one enclosure contract under
`<coordination>/tasks/<repository>/<ENTRY_MASTER>/enclosures/leaf`, and the leaf root the contract's own
recorded worktree group derives, with the code side pointing at the fixture's own repository because a
resolution requires a live code worktree and the case is about the knowledge halves. The contract's
`repo_name` is the fixture's own namespace because the halves are copied from datasets bound to it and
carry no receipt beside them — a candidate with no receipt is read under the requested name, which is
the shipped fallback for a pair a caller assembled itself. The case then writes the fixture's candidate
bytes to the resolved candidate path and corrupt bytes to the resolved baseline path, asserts the
refusal names the baseline, and finally writes the fixture's **real** before dataset to that same path
and re-runs the route to require an entry list — which is what keeps the corruption, rather than the
fixture, as the proven cause.

**The transport cases go through the real route.** They register `register_review_routes` on a bare
`FastAPI` app and drive it through `TestClient`, so the route's own status idiom is measured: `200`
for a typed result, `400` for a malformed request and `503` with no adapter. The selector case calls
`review_request_from_query` directly: an invariant or a family identity is admitted, and `path`,
`invariant_revision`, an empty kind and `latest` are refused. The surface card records that
`260921-ICR-L2` extended this case with the selector-less answer. The case as moved does not assert it,
and was the same at the base. The selector-less route is measured by
`test_a_task_context_review_lists_the_complete_source_inventory_with_no_knowledge_at_all` in the
source-endpoints module.

**The previous-identity case measures one property per hop (`260921-ICR-L17`).**
`test_the_previous_binding_identity_reaches_the_port_and_is_compared_against_the_read` registers the
real routes over a bare `FastAPI` app and drives three requests through `TestClient`:

- a **refresh**: the transport admits `previousBindingDigest`, hands it to the port on the request (the
  case asserts `asked[-1].previous_binding_digest == previous` rather than trusting the route), and the
  composition answers `staleness.state == "stale"` with `previous_comparison_ref` equal to the carried
  value and `submission.state == "disabled_stale"` — while `comparison.binding_digest` is **not** the
  carried value, which is the assertion that the previous identity never becomes the current one;
- a **plain read**: nothing carried, `previous_binding_digest is None` at the port, `staleness.state ==
  "current"` — current by construction rather than by assumption;
- a **malformed spelling**: `400` with `offendingInput == "not-a-digest"`, which is the transport's own
  vocabulary refusal rather than an uncaught model validation error.

It depends on the surface module's `render`, which puts the previous identity on the request with
`model_copy` the way a refresh does.

**The loader case reads two answers from one unresolvable context.** `review_records_for` returns an
empty assessment collection, not a fabricated record. `list_knowledge_review_entries` for the same
context refuses with `candidate_unresolved` and no entries (`260915-KS-L45`). An empty list would read
as "this candidate records nothing to review", which is a different fact from "no candidate resolves
here".

### Conventions

Marked `pytest.mark.evidence_unit`. The module defines its own three-line `fixture` over
`build_diff_fixture` rather than importing the surface module's, because an imported fixture would
shadow a parameter and hide fixture discovery. It imports the resolver, `review_records_for`,
`list_knowledge_review_entries` and the transport (`register_review_routes`, `review_request_from_query`)
directly.

### Invariants And Boundaries

- **No resolution is faked where the resolver is the subject.** The resolution cases use a config that
  names no real root; the before-half composition cases assemble a resolution only to make one side
  deliberately unusable.
- **Behaviour-preserving split.** The nine cases, `ENTRY_MASTER` and `_entry_route_config` are
  byte-identical to the section they came from. The collected node names match the pre-split
  population; only the module name in the node id changed.
- **Catalog footprint.** The module reaches `diff_scope_test_support.py` and `read_scope_test_support.py`
  through its imports. It is declared on both artifacts' exact `consumers` rows beside its sibling, and
  registers no artifact of its own.

### Todos

None.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the boundary it measures, and the import of the surface helpers it reuses. | "The Intent Reviewer surface's resolution and transport: the pair it serves and how it refuses."; "from test_knowledge_review_surface import (" | mcp/tests/test_knowledge_review_resolution_and_route.py:1-42 |
| The unit marker and the per-case fixture. | `pytestmark`; `fixture` | mcp/tests/test_knowledge_review_resolution_and_route.py:44-44; mcp/tests/test_knowledge_review_resolution_and_route.py:47-51 |
| The surface module's config that names no real root, and the render helper that puts the previous identity on the request. | `review_config`; `render` | mcp/tests/test_knowledge_review_surface.py:125-133; mcp/tests/test_knowledge_review_surface.py:184-203 |
| The two resolution cases: the candidate comes from task context rather than a browser-chosen path, and an absent dataset refuses by name. | `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`; `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one` | mcp/tests/test_knowledge_review_resolution_and_route.py:57-70; mcp/tests/test_knowledge_review_resolution_and_route.py:73-92 |
| **The absent before half refuses by name and the refused review creates nothing: the sibling leaf `260921-ICR-L5`'s case beside the absent-candidate one above, differing in *which* half is missing — the two halves are different facts and have different next actions.** | `test_an_absent_baseline_half_refuses_by_name_rather_than_substituting_an_empty_one` | mcp/tests/test_knowledge_review_resolution_and_route.py:95-131 |
| **The corrupt before half is a typed refusal rather than an `apsw.NotADBError` raised from inside the read, and the refusal names the baseline rather than the candidate — only one of the two sides can be repaired by authoring knowledge again.** | `test_a_before_side_that_is_present_but_unreadable_refuses_by_name` | mcp/tests/test_knowledge_review_resolution_and_route.py:134-172 |
| **The entry route states the pair refusals before any subject is compared, proved against the damage rather than against the fixture: the same route that refuses the corrupted side returns an entry list once the dataset that belongs there is written back.** This is the route `_entry_route_config` builds a real task context for, because the route resolves its pair from canonical task context and the browser never names a dataset. | `test_the_entry_route_refuses_a_damaged_before_half_instead_of_raising`; `_entry_route_config`; `ENTRY_MASTER` | mcp/tests/test_knowledge_review_resolution_and_route.py:175-175; mcp/tests/test_knowledge_review_resolution_and_route.py:178-241; mcp/tests/test_knowledge_review_resolution_and_route.py:244-282 |
| The two transport cases: exactly the two reviewable selector kinds are admitted and every other spelling refused, and the route serves the typed result and refuses by name with no adapter. | `test_the_transport_admits_exactly_the_two_reviewable_selector_kinds`; `test_the_route_serves_the_typed_result_and_refuses_by_name_with_no_adapter` | mcp/tests/test_knowledge_review_resolution_and_route.py:285-303; mcp/tests/test_knowledge_review_resolution_and_route.py:306-363 |
| **The previous identity driven through every hop: carried by a refresh to the port and compared, absent on a plain read, and refused by name when malformed.** | `test_the_previous_binding_identity_reaches_the_port_and_is_compared_against_the_read` | mcp/tests/test_knowledge_review_resolution_and_route.py:366-442 |
| **The loader case: an unresolvable candidate yields no fabricated assessment, and its entry list refuses with the review's own code rather than answering empty.** | `test_the_published_assessment_loader_returns_nothing_for_an_unresolvable_candidate` | mcp/tests/test_knowledge_review_resolution_and_route.py:445-470 |
| The unit-regression lane row, beside its sibling's. | "mcp/tests/test_knowledge_review_resolution_and_route.py" | mcp/tests/test-evidence-lanes.toml:159-159 |
| The two support artifacts whose exact `consumers` lists declare this module (at `:1447` and `:1503`). | "path = \"mcp/tests/diff_scope_test_support.py\""; "path = \"mcp/tests/read_scope_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:1425-1470; mcp/tests/evidence-lifecycle.toml:1473-1529 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every case builds its datasets under
`tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`test-evidence-lanes.toml`) moved with the leaf's inserted lines: 1 row(s) re-pointed by the installed fixer (its generated bullets kept); 2 passing row(s) normalised by the fixer. The fixer's normalisation also re-measured ranges into files this leaf did not change (`test_knowledge_review_resolution_and_route.py`). No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:29:33+00:00: Generated citation repair: "mcp/tests/test_knowledge_review_resolution_and_route.py" repointed to mcp/tests/test-evidence-lanes.toml:159-159. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): created this one-to-one card for the resolution and transport cases. The worker moved them verbatim out of `test_knowledge_review_surface.py` (1475 → 1056 lines there; 470 lines and 9 cases here). The five case rows, the loader half of the loader/pane-name row, the `260921-ICR-L5` before-half prose and the `260921-ICR-L17` previous-identity prose moved from `test_knowledge_review_surface.py.md`, where they were removed. Every range was re-derived to each construct's own extent. The two before-half rows had cited ranges that were already stale before this leaf, and the entry-route row had its three ranges in the wrong order. On re-reading, the selector-kind case does not assert the selector-less answer that the surface card attributed to it. The transport text states what it asserts and records the divergence. Verification metadata remains empty until closeout stamps the code commit.
