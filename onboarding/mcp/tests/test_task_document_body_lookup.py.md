# mcp/tests/test_task_document_body_lookup.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Source assertions for the dashboard’s on-demand task-document body reader: bounded named inputs rather than unrelated corpus enumeration, retained graph-join byte comparisons on the original fixture, and RF01 owner/listed-child raw-schema admission parity for dependency/graph fields. The same module checks canonical corpus enumeration against the earlier recursive glob. The original _corpus_wide_body oracle supplies no OrderFields; its fixture comparison must not be generalized to arbitrary dependency-bearing populations.

The cost is checked by counting what a call touches, not by timing it. The module records every
directory listed and every task JSON read during one call, and requires those two lists to be
identical at 4 and at 40 unrelated tasks. A read that grew with the corpus fails here, on any
machine, without a timing threshold.

## Code Commentary

### Logic

**Fixture.** `_corpus(root, unrelated=N)` builds one temporary `tasks/` tree. It holds a series
master and its leaf, a standalone document, two real masters in different repository folders
(`repo-a/master-a` and `other-folder/master-b`), and a sprint whose `executionGraph` names both of
them plus a missing `missing/task.json`. It also holds four **decoys** that the corpus-wide join never
admitted. Each decoy sorts after the real master it imitates, so a join that admitted it would show
its title:

- a historical copy under `series/notes/master-a/`;
- an archived master under `0_archive`;
- a master reached only through the symlinked repository folder `zz-linked-folder`;
- a master-shaped document at `zz-schemaless/master-b/task.json` with its `schema` key deleted.

The model gives a missing schema a default, so the schema-less decoy would validate and win the
last-wins join. Only the schema filter in `_graph_master_docs` keeps it out (added in L42-A2 for
review finding L42-R1-F2).

**Cases** (source assertions; no tests were collected or executed for this reconciliation):

- `test_every_document_kind_projects_the_same_body_as_the_corpus_wide_join` compares
  `read_task_document_body` with `_corpus_wide_body` for the master, leaf, standalone, both named
  masters and the sprint. `_corpus_wide_body` reproduces the removed path: the full
  `_iter_task_document_payloads` enumeration through `_validated_task_documents` into `documents_by_ref`; no enclosure/lifecycle map is supplied. The case compares the
  serialized bodies, then checks that the sprint graph shows `Master A`, `Master B` and the
  `repo-a/missing/task.json` fallback, and that an absent path returns `None`.
- `test_one_body_read_touches_the_same_files_whatever_the_corpus_size[leaf|master|sprint]` uses `touches`, now patching _common, _task_documents and _task_order _read_json plus os.scandir. Recorded read/listing lists must match at 4 and 40 unrelated tasks. The leaf now expects its own JSON then its owner task.json, while the master fixture expects only itself; neither lists directories in this fixture because its master rows have no explicit child files. The sprint still expects itself and the three graph-named candidate files, including the refused schema-less decoy, and only the specified repository/task-folder listings. This is not a claim that dependency-bearing ordinary masters read no children.
- `test_enumeration_keeps_exactly_the_canonical_depth_documents_the_recursive_glob_kept` adds edge
  entries: a directory named `folder.json`, JSON under `enclosures/` at two depths, a top-level JSON
  in a repository folder, and a symlinked task folder. It then requires `_iter_task_json` to equal
  the old `rglob` comprehension element for element and in order. The `folder.json` directory is
  kept, because the enumeration lists any entry named `*.json` and leaves refusal to the reader. The
  notes copy, top-level, archive, enclosure and symlinked paths are excluded.
- `test_named_order_reads_preserve_raw_corpus_admission` crosses owner versus listed-child boundaries with absent, correct and wrong raw schema. Every mutated payload also carries a futureVersionField. The requested leaf waits on L2, L2 points back to L1 and to absent L404, and the owner lists a missing L3 child. The body must remain readable; an inadmissible owner stops after leaf+owner reads, while an admitted owner attempts the named gate and missing child, with no directory listings or unrelated task read. The case compares body and corpus waitsForTasks, neededByTasks and executionGraphView, checks the expected forward/reverse IDs, and compares the four pre-existing JSON files’ bytes. It demonstrates declared tolerance for schema-bearing unknown fields and refusal of missing/wrong schema at both new boundaries, not whole-body serialized equality or a directory-wide no-new-file assertion.
- `test_ready_membership_is_indexed_once_per_native_call` uses 32 and 128 planning leaves all waiting on Completed L0, separately for body and corpus reader entry points. It saves uninstrumented serialized output, wraps derive_master_order to return counted ready IDs/iteration, and on each of two instrumented calls asserts unchanged serialized output, no more than 2*size counted equality comparisons, exactly one ready-tuple iteration and exactly size yielded items. It records those operation counts. This checks the graph adapter’s ready-membership indexing, not wall-clock timing, all reader work, SCC complexity, or an instrumented execution result from this reconciliation.

### Conventions

- The earlier recursive-glob comprehension is written out inside the enumeration case as the
  reference. It is the specification, not dead code. The case holds the new walk to the old
  semantics, including `rglob`'s treatment of symlinked folders on this Python.
- Measurements, profiles and HTTP timings are **not** in this module. They are task-local evidence
  for the leaf (`notes/reports/l42-evidence/`) and depend on the corpus.
- The module imports `FRESH` from `test_observer_projection.py`, the same way its unit-lane sibling
  `test_task_documents_graph_projection.py` does.

### Invariants And Boundaries

- Keep the scaling case **count-based**. Replacing it with a timing threshold would make it flaky
  and would stop it from saying which file was touched.
> Retained historical L42 evidence: the Worker mutation check caught 4 of 4 mutations; dropping the graph schema filter survived until the schema-less decoy made the byte-identity case fail with `AssertionError: sprint`. The original base comparison used an extracted tree because conftest put the worktree mcp/src first, and reported 3 failed/2 passed. These are predecessor task reports, not RF01 executions or collection counts. Keep each decoy and its mutation purpose; none of those checks was rerun in this reconciliation.
- The existing card records unit-regression lane registration; that external lane file was not re-adjudicated in this bounded reconciliation. Original cases use temporary paths and monkeypatching; the RF01 ready-membership case also uses record_property. The module invokes real projection readers on disposable data, not a browser or installed HTTP application.

### Todos

No implementation scope is opened here. The installed-build before/after measurement, including
concurrent master+leaf reads and projector CPU, belongs to L50 (review finding L42-R1-F1).

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern the repository's
own test fixtures and assertions, so the retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

- The module protects bounded named-input body reads and corpus admission; its RF01 docstring names owning masters and explicit children, not a one-file-only closure. [1]

- The corpus fixture and its decoys, including the schema-less master the schema filter alone excludes. [2]

- Reference body projection uses validated corpus documents and documents_by_ref without a lifecycle map. [11]


- Original fixture-specific serialized body comparison, sprint graph titles/fallback and absent-path refusal remain; RF01 separately asserts owner/listed-child schema admission by comparing dependency/graph fields with the corpus reader. [4]



- The recorder counts listings and task JSON reads through all three reader modules; a separate counted-ready wrapper asserts one ready-tuple indexing pass per graph at two sizes and entry points. [5]



- At 4/40 unrelated tasks, the fixture asserts identical touched-file lists: leaf plus owner, master alone, or sprint plus graph-named candidates; leaf/master fixtures list no directories. [6]


- The enumeration equals the earlier recursive glob, including its exclusions and symlink behavior. [7]


- The production body read uses separate sprint graph-master and addressed ordinary owner/listed-child Order joins; newly read Order inputs are raw-schema-filtered before tolerant parsing. [8]

- The bounded enumeration and the named-path probe under test. 




> Retained earlier citation wording: - The lane registration. Source caption: "mcp/tests/test_task_document_body_lookup.py"




### Cross-Repo References

This card covers test behavior only. There is no separate cross-repository protocol or live
installation involved.

No meaningful cross-repo references found.





- The lane registration. Source caption: "mcp/tests/test_task_document_body_lookup.py" [10]

- The bounded enumeration and the named-path probe under test. [9]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py::_iter_task_json - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
