# mcp/tests/test_knowledge_review_source_content.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **production-composition evidence for `ICR-R03@v1`**: one inventory entry opens the exact available
before/after source content *for its bound comparison*, with truthful per-side states for content that
cannot be rendered, and with no silent fallback to a working tree. The twenty cases measure that through
the operations the dashboard really serves — a real leaf enclosure with a real linked worktree, the real
review payload's own inventory (`/api/review/intent`), the real capture owner, and the real expansion
route (`/api/review/intent/source-content`) wired through `register_review_routes` to the real
application owner — and nothing here injects a prebuilt expansion, a fake diff payload or a
hand-assembled resolution.

Two properties make the assertions evidence rather than restatement. **Every text is read back out of Git
independently of the owner under test**, through a subprocess `git show <tree>:<path>` observation whose
failure is an assertion failure and never an empty string. And **the route is exercised over an HTTP
transport** (`TestClient` against the real route table), so a case that passes has proved the query
contract, the refusal status and the served body together rather than an in-process call.

## Code Commentary

### Logic

**The fixture is the sibling review suite's, extended rather than rebuilt.** `content_fixture`
(`:169-174`) calls `build_endpoint_fixture(tmp_path / "content", datasets=False)` imported from
`test_knowledge_review_source_endpoints` — the R01 production-composition fixture — so these cases measure
the *same* real enclosure, worktree and capture path the source-endpoint cases measure rather than a
second, drifting one. `_materialize_unusual` (`:127-166`) then writes **real instances** of every content
class the packet names into that worktree: a real binary blob (`BINARY_PATH`), a real symlink
(`SYMLINK_PATH`), a real nested repository recorded as a gitlink (`SUBMODULE_PATH`), a mode-only change
(`MODE_ONLY_PATH`), a file→symlink type change (`TYPE_CHANGE_PATH`), an oversized document
(`OVERSIZED_PATH`) and a name containing a tab and a newline (`ODD_NAME_PATH`). Each is a measurement of
what Git actually reports, not a state a test can assert into existence, which is why the fixture creates
them on disk and commits through the shipped fixture helpers.

**The independent observation is a subprocess Git, deliberately not the owner's own reader.**
`_blob_text` (`:89-94`), `_object_id` (`:97-101`) and `_subprocess_git` (`:104-116`) run `git show` and
`git rev-parse` with a pinned environment, return `None` on a non-zero exit, and hand back **undecoded
bytes** so an observation of binary content is byte-exact as well. Every "the expansion carries the
content of the two bound objects" assertion compares the served value against one of these, which is what
makes it a measurement of the fixture rather than a restatement of the read.

**The routes are wired the way the composition root wires them.** `_served` (`:177-191`) builds a bare
`FastAPI` app and calls `register_review_routes` with the three real owners — `read_knowledge_review`,
`list_knowledge_review_entries` and `read_review_source_content` — so `_listed_inventory` (`:194-207`) is
the browser's own listing and `_expand` (`:210-227`) is the browser's own expansion, refusals included
(`_status` is attached to the body so a refusal's status and its code are asserted together).
`_expansion` (`:230-239`) is the one place the *listed* generation is carried into the expansion, which is
how the generation-bound cases name what the listing published rather than what the server would choose.

**`_unchanged_paths` (`:247-266`) is the path-confinement falsifier.** It lists the recorded base tree's
paths that the listed change set does not contain, through the support module's own `_git`; each is a real
file at the recorded base and in no change set, so a route that reads any addressable path serves them and
only the packet's boundary forbids it.

**The twenty cases, in the four groups the module's own section comments mark:**

| Case | Property |
| --- | --- |
| `test_a_modified_file_opens_both_endpoints_own_bytes` (`:269-311`) | the modified path opens the base tree's bytes and the captured tree's, each read independently, and the two differ exactly as those objects do; the answer also names the objects it rests on |
| `test_an_added_unmapped_file_opens_its_entire_candidate_text` (`:314-334`) | the packet's conforming example: an added file's whole candidate text, with a measured absence and its reason on the before side |
| `test_a_deleted_file_opens_its_entire_base_text_beside_a_measured_absence` (`:337-355`) | the mirror image: the complete base text, an absent after side, and the proof that the file really is gone |
| `test_a_tab_and_a_newline_in_a_name_is_the_address_its_content_opens_at` (`:358-381`) | the listed path is the address: a name with a tab and a newline opens its own object with no re-quoting and no substituted neighbour |
| `test_a_binary_entry_states_its_kind_identity_and_size_with_no_text` (`:384-400`) | binary content is `binary`, carries its exact object and byte length, and never an empty document |
| `test_a_symlink_entry_carries_the_link_target_and_never_a_document` (`:403-417`) | a symlink's content is its target, stated as such |
| `test_a_submodule_entry_reports_the_recorded_pointer_and_no_file_bytes` (`:420-436`) | a gitlink is the commit it records, and no blob is invented for it |
| `test_a_mode_only_change_shows_identical_bytes_and_names_the_mode` (`:439-454`) | the one change a content read must not present as an edit: identical bytes, one object id, the mode change stated |
| `test_a_type_change_opens_each_side_by_its_own_kind` (`:457-470`) | a file that became a symlink reads as a document on one side and a target on the other |
| `test_oversized_content_is_a_stated_bounded_expansion` (`:473-492`) | past the bound, a prefix that says it is one, with the exact size and the whole object still reachable by identity |
| `test_the_expansion_stays_bound_when_the_branch_advances_after_the_listing` (`:495-557`) | the packet's "advance the branch between list and expansion" exercise: the *listed* bytes are served, the move is stated as `superseded`, and the control shows a re-listing carries the new generation |
| `test_a_missing_object_is_unavailable_on_its_side_while_the_other_stays_inspectable` (`:560-596`) | one side's object is gone: that side is `unavailable`, the other stays readable, and the pair is admitted by a *measured* change set |
| `test_a_pruned_base_blob_is_unavailable_on_its_side_while_the_candidate_side_is_served` (`:599-638`) | a real prune of one loose blob: both trees are whole, so the generation *is* measured, and the unreadable object is named rather than substituted |
| `test_an_unmeasured_generation_still_confines_the_path_to_a_measured_change_set` (`:641-676`) | the verifier's finding: an unmeasured pair must not become an open file reader — both falsifying paths are refused by name |
| `test_a_generation_that_names_a_commit_is_refused_rather_than_served` (`:679-722`) | only the object's own type separates a commit id from a tree id, and the control beside it shows the listed tree id still opens |
| `test_a_path_outside_the_measured_change_set_is_refused_by_name` (`:725-749`) | an unchanged path no recorded realization links is refused by name; with no knowledge bound (`datasets=False`) only the inventory's entries are readable. The one other admitted population — unchanged context a recorded realization of the same comparison links — is measured in `test_knowledge_review_attributed_source_content.py` |
| `test_a_baseline_that_is_not_the_recorded_base_is_refused` (`:752-770`) | the server reads this leaf's recorded base and substitutes no other generation |
| `test_a_query_that_does_not_name_the_generation_is_refused_by_the_transport` (`:773-795`) | a missing tree id is a bad request naming the input it expected: the server never chooses the generation for a caller |
| `test_an_unwired_process_refuses_the_route_by_name` (`:798-821`) | a process composed without the port answers 503 with "no review adapter is wired" rather than serving an empty file |
| `test_the_listed_entry_and_its_expansion_describe_the_same_path` (`:824-842`) | the expansion echoes the listed generation, path, status and reference, so what was opened is what was listed |

### Conventions

`pytestmark = pytest.mark.evidence_unit` (`:62`) is the module's lane marker, and the module's path is
registered in `mcp/tests/test-evidence-lanes.toml`'s `unit-regression` lane at `:111`. It also appears as a
**source-derived consumer** in the two `consumer_scope = "exact"` rows of `mcp/tests/evidence-lifecycle.toml`
that its imports make it a consumer of (`diff_scope_test_support.py` at `:1412`, `read_scope_test_support.py`
at `:1445`) — so the catalog's consumer sets stay exact rather than approximate, and the leaf registers no
artifact and no contract of its own.

Every case is deterministic: no case depends on wall-clock ordering, the Git observations pin `PATH`,
`HOME` and `GIT_CONFIG_NOSYSTEM` (`:112`), and the only subprocess is that observation — the route is
driven in-process through `TestClient`, so no case starts a server, reaches the network or touches a live
coordination tree. Each case builds its own enclosure and worktree under `tmp_path`.

### Invariants And Boundaries

- **Production composition only.** No case injects a preconstructed expansion, a fake diff payload or a
  hand-assembled resolution; every value the answer carries is produced by the shipped owner.
- **The generation is the caller's, never the server's.** Both tree ids travel in the query and the
  request parser refuses a blank one (`:773-795`), which is what keeps an opened entry bound to the
  generation the reader was looking at.
- **A missing object is a stated state, not an empty file.** `absent`, `unavailable`, `binary`,
  `symlink` and `submodule` are each distinguished from `present`, and no case accepts a substituted
  working-tree byte for a side that could not be read.
- **The boundary is the measured change set, plus recorded-realization context.** With an unmeasurable
  requested pair the leaf's own review still bounds the path, and the falsifiers prove it (`:641-676`);
  this fixture binds no knowledge, so the attributed-unchanged admission (260921-ICR-L43) never
  applies here and is measured by the sibling attributed module.
- **Damage is injected into real artifacts** — a deleted loose object, an unheld tree id, a commit id in
  a tree-id field — so the states are measured on the real readers rather than simulated.
- **No case reaches a browser or a pane.** The surface itself is R12/R13/R17/R20/R21 territory; this leaf
  measures the two routes.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the module's own helpers, cases and docstring. Three details a
reader should carry: the fixture is **shared with the R01 source-endpoint suite** rather than rebuilt, so
these cases measure the same real enclosure and capture path; every text is asserted against an
**independent subprocess `git show`**, never against the owner's own reader; and the route is driven over
the real HTTP transport, so a passing case has proved the query contract and the served body together.

- The module's own statement of the requirement it is the production-composition evidence for, and of the load-bearing property behind each case. [1]
- The lane marker and the content-class constants, one path per class the packet names. [2]
- The independent Git observation: undecoded bytes, `None` on an error, and an isolated environment. [3]
- **The content classes materialized for real: a blob, a symlink, a gitlink, a mode change, a type change, an oversized document and a name that is not a line.** [4]
- **The shared R01 production fixture these cases extend rather than duplicate.** [5]
- **The routes wired as the composition root wires them, over the real application owners.** [6]
- The listing read and the expansion read, with the status carried beside the body so a refusal is asserted as one. [7]
- The falsifiers for path confinement: the recorded base's paths that no change set contains. [8]
- **The modified path opens both bound objects' own bytes, each against an independent observation.** [9]
- The packet's conforming example, and deletion as its mirror image. [10]
- **The listed path is the address, however unusual the name.** [11]
- **The non-textual kinds, each opened as what it is rather than as an empty document.** [12]
- The two changes a content read must not present as an edit: a mode-only change and a type change. [13]
- The bound itself, and the case that measures it. [14]
- **The generation binding: the listed bytes survive the branch moving, the move is stated, and the control re-lists.** [15]
- **The two availability cases: an unheld tree, and a real prune of one loose blob.** [16]
- **The verifier's finding, and the object-type refusal with its control.** [17]
- **The refusal family: an unconfined path, a substituted baseline, an incomplete query and an unwired process.** [18]
- The closing identity case: what was opened is what was listed. [19]
- **The transport this module drives: the third route constant, the selector that carries the caller's generation, and the port the composition supplies.** [20]
- The refusal code the route answers with, added to the review vocabulary in the same change. [21]
- **The lane row and the two consumer rows this module's registration produced, with the counts they do not move.** [22]

### Cross-Repo References

No cross-repository behavior is measured in this file. It creates a local repository, an enclosure and a
task-artifact root under `tmp_path` for each case.

No meaningful cross-repo references found.
