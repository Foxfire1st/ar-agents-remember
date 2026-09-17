# mcp/tests/diff_scope_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/diff_scope_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T03:15+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
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
| **The contract this module's artifact row is registered under.** | "contract:knowledge-diff-cases" | mcp/tests/evidence-lifecycle.toml:1250 |
| **The artifact row that registers this module, and the replacement contract it declares.** | "260915-KS-L8"; "contract:knowledge-diff-cases" | mcp/tests/evidence-lifecycle.toml:1247; mcp/tests/evidence-lifecycle.toml:1250 |
| The unit-lane row that keeps the scope module in the certifying collection path. | "mcp/tests/test_knowledge_diff_scope.py" | mcp/tests/test-evidence-lanes.toml:76-76 |
| The integration-lane row that keeps the boundary module in the certifying collection path. | "mcp/tests/test_knowledge_diff_boundaries.py" | mcp/tests/test-evidence-lanes.toml:159-159 |
| The artifact row on which the boundary module is declared as a consumer (its consumer list names `mcp/tests/test_knowledge_diff_boundaries.py`). | "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1268-1277 |
| The artifact rows on which the scope module is declared as a consumer (each row's consumer list names `mcp/tests/test_knowledge_diff_scope.py`). | "contract:knowledge-diff-cases"; "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1239-1256; mcp/tests/evidence-lifecycle.toml:1268-1277 |
| **The evidence node the contract names: the removed realization keeps its baseline source in the union.** | "test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union" | mcp/tests/test_knowledge_diff_scope.py:309-342 |

## Cross-Repo References

The fixture writes two real temporary Git repositories and points one at the other's object store. Both
are local, created under the caller's `tmp_path`, and neither touches a configured remote or another
repository's history.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured cross-repository evidence is claimed. | — | — |

## Update History

- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): created this one-to-one card for the comparison's shared fixture and registered its governance. It records the module's reason for existing — **the comparison is decided by a topology no single-snapshot fixture can carry**, so the fixture builds one topology twice through the public store operations — the seven transitions the candidate authors with the case each exists for, and the **two measured substrate rules** that shaped it (a same-identity second revision is refused `duplicate_identity`, so a revised statement is necessarily an old/new pair; and the claim trigger refuses an in-place rewrite, so a relationship revision is a removal plus an authoring with the removed relationship's anchor row left recorded). It states the object-store borrow that lets **one** repository name both trees (a caller runs one command in one repository), that the added claim's recorded identity is the blob the candidate tree really holds, and the two properties that keep the fixture honest: **the baseline is the shared read-scope fixture** so the two leaves cannot disagree about the stopping rule's selection, and `_require` makes a fixture step that stopped doing what it says a fixture failure rather than a silently green case. **The family-edge debt is stated here as a gap rather than as coverage**: the fixture authors 0 `family_predecessor` rows, so the family half of the coverage decision's rule-2 subsumption is unexercised, and adding one schema-valid family edge is the closing input carried to `KS-R09`/`L9`. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
