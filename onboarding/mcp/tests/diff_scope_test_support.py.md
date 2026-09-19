# mcp/tests/diff_scope_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/diff_scope_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T03:15+02:00 |
| lastVerifiedCommitHash | `47570cd827428c171613c8cb01e01f0b1cb26f73` |
| lastVerifiedCommitDate | 2026-09-20T01:58:41+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l08` uncommitted source; base `1ff1893f44d875073d58af863238501a6be35288` |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**The curator-stage comparison's fixture: one baseline snapshot and one curator-updated candidate.**
The comparison is decided by a topology **no single-snapshot fixture can carry**, because half of its
obligations are statements about what *changed between two snapshots* rather than about what one
snapshot holds. The module therefore builds the same identity topology **twice** — the baseline and the
candidate — through the public store operations, and the candidate carries exactly one authored change
of each kind the packet distinguishes.

**It is registered as a governed artifact** — `shared-support` / `internal-canonical` /
`integration` / `local-composition` / `cadence = "affected"` / `lifetime = "permanent"` /
`consumer_scope = "exact"` — under the contract `knowledge-diff-cases`, whose evidence node is
`mcp/tests/test_knowledge_diff_scope.py::test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union`
(the node that owns the packet's first non-conforming example). A new test module that imports it must
be added to its `consumers` list in the same change: the validator derives each artifact's real test
importers and refuses a declared set that differs, so the failure is a **hard collection error for the
whole catalog**, not a warning.

## Code Commentary

### Logic

`build_diff_fixture(directory) -> DiffFixture` builds the baseline with the **shared read-scope
fixture** (`build_read_scope_fixture`) and then derives the candidate from it, so the two leaves cannot
disagree about which records R07's stopping rule selects.

The baseline side re-uses the read fixture's database, Git root, tree id and blob map unchanged. The
candidate side is built by copying the baseline's **closed database bytes** and then curating through
the public store operations — a curator's starting point is the baseline's records, and copying the
closed file is what makes that literal rather than re-authored (and therefore possibly different) —
with its own Git tree written beside it.

**The seven transitions the fixture authors, and the case each one exists for:**

| Transition | What the candidate does | Why it exists |
| --- | --- | --- |
| revised statement | authors a successor revision of the retry identity (`predecessors=(subject,)`) and moves the realization onto it | the `superseded`/`superseding` pair; a revised statement must not render as a deletion plus an unrelated addition |
| source-only | rewrites `src/batch.py` in its tree while the two claims at that path keep identical rows and anchors | `source_change_only=True` with `record_field_changed=False`: the recorded anchor did not move, the bytes at the recorded path are simply not the recorded ones any more |
| removed relationship | deletes the claim at `src/synchronization.py`, **leaving its anchor row recorded** | the packet's own non-conforming example made measurable: deleting a link must not erase the earlier code |
| added relationship | records a new claim at `src/retry_interval.py` on the revised revision | the added direction of a one-sided item |
| unchanged siblings | both of the sibling invariant's claims, selected by both snapshots with identical rows; the rewritten code path is **one** of that sibling's two locations | the pair of statements the response must keep apart, measured on one item each way |
| outside the selection | records a fourth retry revision carrying no claim, selected by neither side | `present_outside_selection` — "present-but-outside-the-selected-scope is not deletion" |
| unattributed change | adds `src/unmapped.py`, cited by no claim | the packet's visible unattributed gap |

**Two measured substrate rules shaped the fixture, and both were hit while building it:**

- `create_invariant_revision` **refuses** a second revision with the same identity and another sealed
  payload (`duplicate_identity`, next action *"author a successor with its own identity and this revision
  as an exact predecessor"*), so a revised statement is necessarily an old/new **pair** of immutable
  revision payloads.
- The schema's `realization_claim_no_rewrite` trigger refuses rewriting a claim in place, so the
  candidate's revision of a *relationship* is its removal plus the authoring of the successor's own
  claim. The removed relationship's anchor row stays recorded, which is what keeps the before-side
  source observable after the link is gone.

**The two live Git trees borrow each other's object store** (`_borrow_objects` writes
`.git/objects/info/alternates`), because the comparison names both trees in **one** repository: a caller
comparing two snapshots runs one command in one repository, and a probe rooted in a repository that
could not resolve one of the two named trees would have to report "unavailable" for a pair that is
perfectly comparable. The candidate tree's blobs are read back from the tree it just committed
(`git rev-parse HEAD:<path>`), so the added claim's recorded identity is the blob the candidate tree
**really holds** — which is the difference between an observation that is `exact_recorded_blob` and one
that is a mismatch.

`DiffFixture` exposes every identity a case asserts against as a **named field** (the five revision ids,
the moved/unchanged/removed/added/outside-selection claim ids, the sibling invariant, and the four
paths), and `DiffSide` carries one side's fixture, database path, Git root, tree id and blob map.

### Conventions

- **A fixture is not a probe.** `_require` fails loudly when a fixture-building store operation does not
  return the state it says it returns, so a fixture that silently stopped authoring its transition would
  be a fixture failure rather than a case that passes for the wrong reason.
- `_claim_row_digest` recomputes a claim's row digest through `records.claim_row_digest` — the same
  function the write path used to seal it — rather than restating the digest's composition here where it
  could drift from the production rule.
- `_git` runs with `GIT_CONFIG_NOSYSTEM=1` and a per-repository `HOME`, so the fixture is independent of
  the host's Git configuration.
- The stored role is read back through the vocabulary's own decoder (`stored_realization_role`) so the
  re-sealed draft carries a `RealizationRole` the type admits rather than a bare string.

### Invariants And Boundaries

- **The baseline is the shared read-scope fixture, and that is a contract rather than a convenience.**
  It is what keeps the two leaves from disagreeing about which records the R07 stopping rule selects, and
  it is why the diff support module declares the read-support module as a real import in the evidence
  catalog.
- **`_CANDIDATE_TREE_TEXT` is the whole candidate tree as one table**, so the two trees differ in exactly
  the named ways and every other body is the baseline's own text byte for byte.
- **The candidate database starts as the baseline's bytes.** A candidate built by re-authoring would be a
  different dataset for reasons unrelated to the transitions under test.
- **Boundary.** This module builds fixtures. It asserts nothing about the comparison — every assertion
  lives in the two case modules — and it writes only inside the `tmp_path` directory it is handed.

### Todos

None recorded. One carried **fixture debt** belongs here and is stated rather than implied: the fixture
authors **0 `family_predecessor` rows** (measured census 2 invariant / 0 family before, 4 / 0 after), so
the **family half of the coverage decision's rule-2 subsumption is unexercised**. Adding one
schema-valid family edge to this shared fixture is what would close it, and that is carried to
`KS-R09`/`L9` as fixture debt rather than half-done inside a review boundary.

## Docs References

No Domain Documentation entries are configured in this memory root. The statements below are grounded in
repository source and package-local evidence only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The candidate's two new source paths, its revised statement and its authored words, and the whole candidate tree as one table.** | `SUCCESSOR_PATH`; `UNMAPPED_PATH`; `RETRY_REVISED_STATEMENT`; `_CANDIDATE_TREE_TEXT` | mcp/tests/diff_scope_test_support.py:92-125 |
| The three small value types: one candidate-only realization's identities, one side of the comparison, and the fixture with every identity a case asserts against. | `AddedRealization`; `DiffSide`; `DiffFixture` | mcp/tests/diff_scope_test_support.py:129-186 |
| **The fixture builder: the shared baseline, the copied database, the curating candidate and the two live trees.** | `build_diff_fixture`; `_build_candidate` | mcp/tests/diff_scope_test_support.py:189-281 |
| **The revised statement as a successor, with the substrate's own `duplicate_identity` rule as its reason.** | `_author_revised_revision` | mcp/tests/diff_scope_test_support.py:284-312 |
| **The relationship revision as removal-plus-authoring, because the claim trigger refuses an in-place rewrite.** | `_move_retry_claim`; `_remove_retired_claim` | mcp/tests/diff_scope_test_support.py:315-335; mcp/tests/diff_scope_test_support.py:362-378 |
| **The fourth revision neither side selects, which is what makes `present_outside_selection` measurable.** | `_add_unselected_revision` | mcp/tests/diff_scope_test_support.py:338-359 |
| **The added claim, whose recorded identity is the blob the candidate tree really holds.** | `_add_successor_claim` | mcp/tests/diff_scope_test_support.py:381-418 |
| The claim row digest recomputed through the production sealer rather than restated here. | `_claim_row_digest` | mcp/tests/diff_scope_test_support.py:421-456 |
| **The candidate tree, the object-store borrow that lets one repository name both trees, and the hermetic Git environment.** | `_write_candidate_tree`; `_borrow_objects`; `_git` | mcp/tests/diff_scope_test_support.py:459-506 |
| **The fixture's loud-failure rule: a building step that does not do what it says fails the fixture.** | `_require` | mcp/tests/diff_scope_test_support.py:509-516 |
| **The baseline fixture this module builds on.** | `build_read_scope_fixture` | mcp/tests/read_scope_test_support.py:266-283 |
| The fixture value the baseline side is read from. | `ReadScopeFixture` | mcp/tests/read_scope_test_support.py:174-239 |
| **The contract this module's artifact row is registered under.** | "contract:knowledge-diff-cases" | mcp/tests/evidence-lifecycle.toml:1391-1391 |
| **The artifact row that registers this module, and the replacement contract it declares.** | "introduced_by = \"260915-KS-L8\""; "replacement_contract = \"contract:knowledge-diff-cases\"" | mcp/tests/evidence-lifecycle.toml:1376-1376; mcp/tests/evidence-lifecycle.toml:1379-1391 |
| The unit-lane row that keeps the scope module in the certifying collection path. | "mcp/tests/test_knowledge_diff_scope.py" | mcp/tests/test-evidence-lanes.toml:107-107 |
| The integration-lane row that keeps the boundary module in the certifying collection path. | "mcp/tests/test_knowledge_diff_boundaries.py" | mcp/tests/test-evidence-lanes.toml:211-211 |
| The artifact row on which the boundary module is declared as a consumer (its consumer list names `mcp/tests/test_knowledge_diff_boundaries.py`). | "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1413-1413 |
| The artifact rows on which the scope module is declared as a consumer (each row's consumer list names `mcp/tests/test_knowledge_diff_scope.py`). | "id = \"knowledge-diff-cases\""; "id = \"knowledge-read-scope-cases\"" | mcp/tests/evidence-lifecycle.toml:60-62; mcp/tests/evidence-lifecycle.toml:65-67 |
| **The contract this module's artifact row is registered under.** | "contract:knowledge-diff-cases" | mcp/tests/evidence-lifecycle.toml:1391-1391 |
| **The artifact row that registers this module, and the replacement contract it declares.** | "260915-KS-L8"; "contract:knowledge-diff-cases" | mcp/tests/evidence-lifecycle.toml:1376-1376; mcp/tests/evidence-lifecycle.toml:1379-1391 |
| The unit-lane row that keeps the scope module in the certifying collection path. | "mcp/tests/test_knowledge_diff_scope.py" | mcp/tests/test-evidence-lanes.toml:107-107 |
| The integration-lane row that keeps the boundary module in the certifying collection path. | "mcp/tests/test_knowledge_diff_boundaries.py" | mcp/tests/test-evidence-lanes.toml:211-211 |
| The artifact row on which the boundary module is declared as a consumer (its consumer list names `mcp/tests/test_knowledge_diff_boundaries.py`). | "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1413-1413 |
| The artifact rows on which the scope module is declared as a consumer (each row's consumer list names `mcp/tests/test_knowledge_diff_scope.py`). | "contract:knowledge-diff-cases"; "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1379-1391; mcp/tests/evidence-lifecycle.toml:1401-1413 |
| **The evidence node the contract names: the removed realization keeps its baseline source in the union.** | "test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union" | mcp/tests/test_knowledge_diff_scope.py:309-342 |

## Cross-Repo References

The fixture writes two real temporary Git repositories and points one at the other's object store. Both
are local, created under the caller's `tmp_path`, and neither touches a configured remote or another
repository's history.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured cross-repository evidence is claimed. | — | — |
| **The contract this module's artifact row is registered under.** | "contract:knowledge-diff-cases" | mcp/tests/evidence-lifecycle.toml:1391-1391 |
| **The artifact row that registers this module, and the replacement contract it declares.** | "260915-KS-L8"; "contract:knowledge-diff-cases" | mcp/tests/evidence-lifecycle.toml:1376-1376; mcp/tests/evidence-lifecycle.toml:1379-1391 |
| The artifact row on which the boundary module is declared as a consumer (its consumer list names `mcp/tests/test_knowledge_diff_boundaries.py`). | "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1413-1413 |
| The artifact rows on which the scope module is declared as a consumer (each row's consumer list names `mcp/tests/test_knowledge_diff_scope.py`). | "contract:knowledge-diff-cases"; "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1379-1391; mcp/tests/evidence-lifecycle.toml:1401-1413 |

## Update History
- 2026-09-20T01:21+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 2 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `diff_scope_test_support.py.md:156` (contract:knowledge-diff-cases) — re-read the claim against the landed registry: `contract:knowledge-diff-cases` is at 1391 and the cited 1379-1379 no longer reaches it; `diff_scope_test_support.py.md:171` (contract:knowledge-diff-cases) — re-read the claim against the landed registry: `contract:knowledge-diff-cases` is at 1391 and the cited 1379-1379 no longer reaches it.
- 2026-09-20T01:20+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 5 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `diff_scope_test_support.py.md:146` (?, ?) — re-read the claim against the landed source: the construct moved and the cited range was widened to the line that actually carries it, per the checker's own remedy; `diff_scope_test_support.py.md:152` ("260915-KS-L8", "contract:knowledge-diff-cases") — re-read the claim against the landed source: the construct moved and the cited range was widened to the line that actually carries it, per the checker's own remedy; `diff_scope_test_support.py.md:156` ("contract:knowledge-diff-cases", "contract:knowledge-read-scope-cases") — re-read the claim against the landed source: the construct moved and the cited range was widened to the line that actually carries it, per the checker's own remedy; `diff_scope_test_support.py.md:169` ("260915-KS-L8", "contract:knowledge-diff-cases") — re-read the claim against the landed source: the construct moved and the cited range was widened to the line that actually carries it, per the checker's own remedy; `diff_scope_test_support.py.md:171` ("contract:knowledge-diff-cases", "contract:knowledge-read-scope-cases") — re-read the claim against the landed source: the construct moved and the cited range was widened to the line that actually carries it, per the checker's own remedy.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 5 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `diff_scope_test_support.py.md:146` ("introduced_by = \"260915-KS-L8\"", "replacement_contract = \"contract:knowledge-diff-cases\""); `diff_scope_test_support.py.md:152` ("260915-KS-L8", "contract:knowledge-diff-cases"); `diff_scope_test_support.py.md:156` ("contract:knowledge-diff-cases", "contract:knowledge-read-scope-cases"); `diff_scope_test_support.py.md:169` ("260915-KS-L8", "contract:knowledge-diff-cases"); `diff_scope_test_support.py.md:171` ("contract:knowledge-diff-cases", "contract:knowledge-read-scope-cases").
- 2026-09-18T17:53:05+00:00: 260915-KS-L23 residue clearance (seat A): every citation into `mcp/tests/evidence-lifecycle.toml` re-read against the file as it stands and repointed where the leaf's own consumer-row appends had moved the construct: `contract:knowledge-diff-cases` from `mcp/tests/evidence-lifecycle.toml:1390-1390` to `mcp/tests/evidence-lifecycle.toml:1391-1391` (the artifact row's `replacement_contract` declaration); `introduced_by = "260915-KS-L8"` / `contract:knowledge-diff-cases` from `mcp/tests/evidence-lifecycle.toml:1284-1284; mcp/tests/evidence-lifecycle.toml:1287-1287; mcp/tests/evidence-lifecycle.toml:1372-1382; mcp/tests/evidence-lifecycle.toml:1383-1383; mcp/tests/evidence-lifecycle.toml:1386-1386` to `mcp/tests/evidence-lifecycle.toml:1388-1388; mcp/tests/evidence-lifecycle.toml:1391-1391` (the artifact row's own `introduced_by` and `replacement_contract` lines, which is where the cited ranges had pointed before the file moved); the cross-repo `"260915-KS-L8"` / `"contract:knowledge-diff-cases"` row from `mcp/tests/evidence-lifecycle.toml:1280-1280; mcp/tests/evidence-lifecycle.toml:1283-1283; mcp/tests/evidence-lifecycle.toml:1284-1284; mcp/tests/evidence-lifecycle.toml:1287-1287; mcp/tests/evidence-lifecycle.toml:1372-1382; mcp/tests/evidence-lifecycle.toml:1383-1383; mcp/tests/evidence-lifecycle.toml:1386-1386` to `mcp/tests/evidence-lifecycle.toml:1388-1388; mcp/tests/evidence-lifecycle.toml:1391-1391`; `contract:knowledge-read-scope-cases` from `mcp/tests/evidence-lifecycle.toml:1412-1412` to `mcp/tests/evidence-lifecycle.toml:1413-1413` (that artifact row's `replacement_contract` line); the dual-row consumer claim from `mcp/tests/evidence-lifecycle.toml:1273-1276; mcp/tests/evidence-lifecycle.toml:1287-1307; mcp/tests/evidence-lifecycle.toml:1287-1287; mcp/tests/evidence-lifecycle.toml:1375-1382; mcp/tests/evidence-lifecycle.toml:1395-1402; mcp/tests/evidence-lifecycle.toml:1403-1403; mcp/tests/evidence-lifecycle.toml:1386-1386; mcp/tests/evidence-lifecycle.toml:1407-1407; mcp/tests/evidence-lifecycle.toml:1408-1408` (and its cross-repo variant `mcp/tests/evidence-lifecycle.toml:1303-1303; mcp/tests/evidence-lifecycle.toml:1273-1298; mcp/tests/evidence-lifecycle.toml:1307-1307; mcp/tests/evidence-lifecycle.toml:1375-1382; mcp/tests/evidence-lifecycle.toml:1395-1402; mcp/tests/evidence-lifecycle.toml:1403-1403; mcp/tests/evidence-lifecycle.toml:1386-1386; mcp/tests/evidence-lifecycle.toml:1407-1407; mcp/tests/evidence-lifecycle.toml:1408-1408`) to `mcp/tests/evidence-lifecycle.toml:1391-1391; mcp/tests/evidence-lifecycle.toml:1413-1413` — the two artifact rows whose `consumers` lists name `mcp/tests/test_knowledge_diff_scope.py`; and the scope-module row's contract ids from `mcp/tests/evidence-lifecycle.toml:1266-1266; mcp/tests/evidence-lifecycle.toml:1271-1271; mcp/tests/evidence-lifecycle.toml:53-65` to `mcp/tests/evidence-lifecycle.toml:60-62; mcp/tests/evidence-lifecycle.toml:65-67` — the two `[[contract]]` blocks whose `id` the row's anchors name. Each new range was read against the file on this candidate (the cited construct is on the named line) and the pre-move ranges are recorded here rather than deleted; no claim wording, anchor or range was removed, and no row outside this residue was touched. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1390-1390. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1412-1412. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1390-1390. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1412-1412. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1390-1390. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1412-1412. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:106-106. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:202-202. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1408-1408. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:106-106. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:202-202. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1408-1408. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1408-1408. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1386-1386. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1407-1407. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1386-1386. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1407-1407. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1386-1386. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1407-1407. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:105-105. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:200-200. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:105-105. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:200-200. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:103-103. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:198-198. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1403-1403. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:103-103. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:198-198. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1403-1403. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1403-1403. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1382-1382. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:101-101. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1402-1402. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1382-1382. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:101-101. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1402-1402. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1382-1382. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1402-1402. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1290-1290. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1310-1310. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1290-1290. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1310-1310. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1290-1290. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1310-1310. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:88-88. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:174-174. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1287-1287. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "260915-KS-L8"; "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1284-1284; mcp/tests/evidence-lifecycle.toml:1287-1287. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:88-88. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_diff_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:174-174. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1307-1307. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 24 generated projection bullet(s) by hand while resolving the memory sync** — `contract:knowledge-diff-cases`, `mcp/tests/test_knowledge_diff_scope.py`, `mcp/tests/test_knowledge_diff_boundaries.py`, `contract:knowledge-read-scope-cases`, `260915-KS-L8`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 8 generated projection bullet(s) by hand** — `mcp/tests/test_knowledge_diff_scope.py`, `mcp/tests/test_knowledge_diff_boundaries.py`, `contract:knowledge-read-scope-cases`, `contract:knowledge-diff-cases`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_knowledge_diff_scope.py"` → `mcp/tests/test-evidence-lanes.toml:83-83`; `"mcp/tests/test_knowledge_diff_boundaries.py"` → `mcp/tests/test-evidence-lanes.toml:167-167`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/evidence-lifecycle.toml:1273-1273` -> `mcp/tests/evidence-lifecycle.toml:1274-1274`; `mcp/tests/evidence-lifecycle.toml:1270-1273` -> `mcp/tests/evidence-lifecycle.toml:1271-1271; mcp/tests/evidence-lifecycle.toml:1274-1274`; `mcp/tests/test-evidence-lanes.toml:165-165` -> `mcp/tests/test-evidence-lanes.toml:166-166`; `mcp/tests/evidence-lifecycle.toml:1293-1293` -> `mcp/tests/evidence-lifecycle.toml:1294-1294`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-17T01:15:00+00:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): created this one-to-one card for the comparison's shared fixture and registered its governance. It records the module's reason for existing — **the comparison is decided by a topology no single-snapshot fixture can carry**, so the fixture builds one topology twice through the public store operations — the seven transitions the candidate authors with the case each exists for, and the **two measured substrate rules** that shaped it (a same-identity second revision is refused `duplicate_identity`, so a revised statement is necessarily an old/new pair; and the claim trigger refuses an in-place rewrite, so a relationship revision is a removal plus an authoring with the removed relationship's anchor row left recorded). It states the object-store borrow that lets **one** repository name both trees (a caller runs one command in one repository), that the added claim's recorded identity is the blob the candidate tree really holds, and the two properties that keep the fixture honest: **the baseline is the shared read-scope fixture** so the two leaves cannot disagree about the stopping rule's selection, and `_require` makes a fixture step that stopped doing what it says a fixture failure rather than a silently green case. **The family-edge debt is stated here as a gap rather than as coverage**: the fixture authors 0 `family_predecessor` rows, so the family half of the coverage decision's rule-2 subsumption is unexercised, and adding one schema-valid family edge is the closing input carried to `KS-R09`/`L9`. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
