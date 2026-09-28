# mcp/tests/test_task_document_body_lookup.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_document_body_lookup.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:27:50+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28` |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Unit evidence that the dashboard's on-demand task-document body read
(`read_task_document_body`, served by `/api/task-document`) is **bounded by what it names**, not by the
task corpus, and that it still projects **exactly the bytes** the earlier corpus-wide projection
produced. The same module also checks that the corpus enumeration the always-on projection still
needs (`_iter_task_json`) returns exactly the list the earlier recursive glob returned.

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

**Cases** (3 functions, 5 collected cases):

- `test_every_document_kind_projects_the_same_body_as_the_corpus_wide_join` compares
  `read_task_document_body` with `_corpus_wide_body` for the master, leaf, standalone, both named
  masters and the sprint. `_corpus_wide_body` reproduces the removed path: the full
  `_iter_task_document_payloads` enumeration fed to `_master_docs_by_ref`. The case compares the
  serialized bodies, then checks that the sprint graph shows `Master A`, `Master B` and the
  `repo-a/missing/task.json` fallback, and that an absent path returns `None`.
- `test_one_body_read_touches_the_same_files_whatever_the_corpus_size[leaf|master|sprint]` uses the
  `touches` fixture, which monkeypatches `os.scandir` and both modules' `_read_json`, to record
  listings and reads. At 4 and at 40 unrelated tasks the recorded lists must be equal. For a leaf or
  a master the only read is the document itself and **no directory is listed**. For the sprint the
  reads are the sprint plus the three files at graph-named paths (the schema-less decoy is read and
  then refused). The listings are the tasks root, its three real repository folders, and only the
  named task folders.
- `test_enumeration_keeps_exactly_the_canonical_depth_documents_the_recursive_glob_kept` adds edge
  entries: a directory named `folder.json`, JSON under `enclosures/` at two depths, a top-level JSON
  in a repository folder, and a symlinked task folder. It then requires `_iter_task_json` to equal
  the old `rglob` comprehension element for element and in order. The `folder.json` directory is
  kept, because the enumeration lists any entry named `*.json` and leaves refusal to the reader. The
  notes copy, top-level, archive, enclosure and symlinked paths are excluded.

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
- Do not remove a decoy to make a case pass. Each one fails a specific mutation. The worker's
  mutation check caught 4 of 4 mutations. The reviewer's M2 (dropping the schema filter) survived
  until the schema-less decoy was added, and now fails the byte-identity case with
  `AssertionError: sprint`.
- `mcp/tests/conftest.py` puts this worktree's `mcp/src` first on the path. A PYTHONPATH swap
  therefore cannot run these cases against another tree. A base comparison needs an extracted copy
  of that tree, which is how the scaling cases were shown to fail on base (3 failed, 2 passed).
- The file is registered in the `unit-regression` lane. It uses only `tmp_path` and `monkeypatch`
  and composes no application.

### Todos

No implementation scope is opened here. The installed-build before/after measurement, including
concurrent master+leaf reads and projector CPU, belongs to L50 (review finding L42-R1-F1).

## Docs References

The repository has no configured Domain Documentation source. These claims concern the repository's
own test fixtures and assertions, so the retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it protects. | "The on-demand task-document body reads one document, not the task corpus." | mcp/tests/test_task_document_body_lookup.py:1-7 |
| The corpus fixture and its decoys, including the schema-less master the schema filter alone excludes. | `_corpus` | mcp/tests/test_task_document_body_lookup.py:69-119 |
| The reference projection: the corpus-wide enumeration fed to the unchanged join builder. | `_corpus_wide_body` | mcp/tests/test_task_document_body_lookup.py:122-135 |
| Byte identity for every document kind, the sprint's graph titles and fallback, and `None` for an absent path. | `test_every_document_kind_projects_the_same_body_as_the_corpus_wide_join` | mcp/tests/test_task_document_body_lookup.py:138-159 |
| The recorder that counts listed directories and read files. | `touches` | mcp/tests/test_task_document_body_lookup.py:170-187 |
| The same touched files at 4 and at 40 unrelated tasks; no listing at all for a leaf or a master. | `test_one_body_read_touches_the_same_files_whatever_the_corpus_size` | mcp/tests/test_task_document_body_lookup.py:190-228 |
| The enumeration equals the earlier recursive glob, including its exclusions and symlink behavior. | `test_enumeration_keeps_exactly_the_canonical_depth_documents_the_recursive_glob_kept` | mcp/tests/test_task_document_body_lookup.py:231-263 |
| The production read under test, and the only place that reads masters for it. | `read_task_document_body`; `_graph_master_docs` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:161-201; mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:204-224 |
| The bounded enumeration and the named-path probe under test. | `_iter_task_json`; `_canonical_task_json_candidates` | mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py:74-90; mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py:93-113 |
| The lane registration. | "mcp/tests/test_task_document_body_lookup.py" | mcp/tests/test-evidence-lanes.toml:211-211 |

## Cross-Repo References

This card covers test behavior only. There is no separate cross-repository protocol or live
installation involved.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.

- 2026-09-28T16:27:50+02:00 — 260921-ICR-L42 curator (uncommitted candidate tree `27409ea9f3320689c28c6a810c9a88afa288bbba` over code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): created this card for the new module. It has 3 functions and 5 cases, including the schema-less decoy added in L42-A2. The card is derived from the candidate source and the L42 review evidence. The stamp names the code base, and closeout owns the real commit stamp.
