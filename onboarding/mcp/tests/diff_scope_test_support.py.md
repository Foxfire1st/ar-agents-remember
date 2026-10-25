# mcp/tests/diff_scope_test_support.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Builds the two-snapshot knowledge and Git fixture used by the diff and review readers.

## Code Commentary

`build_diff_fixture` builds the read-scope topology twice — baseline and candidate — as two text trees through the rows builder, the candidate carrying exactly one authored change of each kind the packet distinguishes: a revised statement (another revision number of the same text ID, reported as removal beside unrelated addition), a source change with no record change, a removed and an added realization, and unchanged siblings. Both trees mint the same text IDs in the same order, so unchanged rows project the same UUIDs on both sides and pair as themselves. The selected source trees and logical identities remain independently observable.

Fixture rows are written by RowStore and realization constructors imported from knowledge_rows_test_support. Claim digests are re-sealed through the one production owner rather than restated in the fixture. Production read/comparison owners consume those text trees. The helper provides no canonical writer, lock or claim_no_rewrite enforcement.


`build_diff_fixture(directory) -> DiffFixture` builds the baseline with the **shared read-scope
fixture** (`build_read_scope_fixture`) and then derives the candidate from it, so the two leaves cannot
disagree about which records R07's stopping rule selects.

The baseline side reuses the read fixture's derived database, Git root, tree ID and blob map. `_build_candidate` builds a second text tree through the same read-scope builder, supplying the revised retry statement, omitted synchronization realization and added successor-path realization. Stable text-ID minting preserves unchanged projected identities; no baseline database-byte copy or production authoring transaction constructs this candidate.

**The seven transitions the fixture authors, and the case each one exists for:**

| Transition | What the candidate does | Why it exists |
| --- | --- | --- |
| revised statement | builds the retry record at a changed revision number with revised text | text records carry no predecessor edge, so the changed revision is removal beside unrelated addition, not `superseded`/`superseding` |
| source-only | rewrites `src/batch.py` in its tree while the two claims at that path keep identical rows and anchors | `source_change_only=True` with `record_field_changed=False`: the recorded anchor did not move, the bytes at the recorded path are simply not the recorded ones any more |
| removed relationship | omits the synchronization realization from the candidate text tree | its baseline source remains available to the comparison union; no retained candidate database anchor row is claimed |
| added relationship | records a new claim at `src/retry_interval.py` on the revised revision | the added direction of a one-sided item |
| unchanged siblings | both of the sibling invariant's claims, selected by both snapshots with identical rows; the rewritten code path is **one** of that sibling's two locations | the pair of statements the response must keep apart, measured on one item each way |
| outside the selection | carries the baseline mismatch-anchor realization as the fixture's outside-selection identity | the old fourth retry revision is absent from the single-revision text trees |
| unattributed change | adds `src/unmapped.py`, cited by no claim | the packet's visible unattributed gap |

**The two live Git trees borrow each other's object store** (`_borrow_objects` writes
`.git/objects/info/alternates`), because the comparison names both trees in **one** repository: a caller
comparing two snapshots runs one command in one repository, and a probe rooted in a repository that
could not resolve one of the two named trees would have to report "unavailable" for a pair that is
perfectly comparable. The candidate tree's blobs are read back from the tree it just committed
(`git rev-parse HEAD:<path>`), so the added claim's recorded identity is the blob the candidate tree
**really holds** — which is the difference between an observation that is `exact_recorded_blob` and one
that is a mismatch.

**One new helper: the byte-safe independent observation both review suites now compare against.** `independent_changed_records(root, before, after)` runs `git diff --name-status -z --no-renames <before> <after>` through the **production** runner and returns `{path: status-letter}`. Two deliberate choices are recorded in its docstring: it is a *different* Git question from the inventory's own `--raw -z`, so agreement between the two is an observation about the two trees rather than a restatement of one implementation; and it goes through `run_git` rather than the module's strict fixture helper, because `_git` decodes strictly while a pathname is bytes — a name that is not valid UTF-8 would raise there and the independent observation would be lost exactly where it is needed. It was registered nowhere new: it lives in this module's existing governed artifact and adds no contract or artifact row.


### Conventions

- **A fixture is not a probe.** `_require` fails loudly when a fixture-building store operation does not
  return the state it says it returns, so a fixture that silently stopped authoring its transition would
  be a fixture failure rather than a case that passes for the wrong reason.

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
- **The same builder supplies both text snapshots.** Stable text IDs and entry minting preserve unchanged projected identities; the candidate applies only its named deltas, rather than copying the baseline database bytes.
- **Boundary.** This module builds fixtures. It asserts nothing about the comparison — every assertion
  lives in the two case modules — and it writes only inside the `tmp_path` directory it is handed.


## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References


- `build_diff_fixture` supplies the current fixture or assertion described above. [40]


- `rebuild_after_tree` supplies the current fixture or assertion described above. [41]


- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [42]


- RowStore writes text-tree fixture rows without the retired production admission plane. [43]


- **The candidate's two new source paths, its revised statement and its authored words, and the whole candidate tree rebuilt by one call.** [56]
- The three small value types: one candidate-only realization's identities, one side of the comparison, and the fixture with every identity a case asserts against. [57]

- **The fixture builder: the shared baseline, the rebuilt candidate tree carrying the whole candidate-side delta, and the two live trees.** [58]

- **The revised statement as removal beside unrelated addition: the candidate carries the same retry record with a different statement at another revision number, and text records hold no predecessor edge (rule 1), so the pair is never a succession.**

- **The added claim, whose recorded identity is the blob the candidate tree really holds.** [61]

- **The candidate tree, the object-store borrow that lets one repository name both trees, and the hermetic Git environment.** [62]
- **The fixture's loud-failure rule: a building step that does not do what it says fails the fixture.** [63]

- **The baseline fixture this module builds on.** [64]


- The fixture value the baseline side is read from. [65]

- **The contract this module's artifact row is registered under.** [66]
- **The evidence node the contract names: the removed realization keeps its baseline source in the union.** [67]


### Cross-Repo References

The fixture writes two real temporary Git repositories and points one at the other's object store. Both
are local, created under the caller's `tmp_path`, and neither touches a configured remote or another
repository's history.

No configured cross-repository evidence is claimed.
