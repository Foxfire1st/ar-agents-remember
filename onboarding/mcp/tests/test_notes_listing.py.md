# mcp/tests/test_notes_listing.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

Unit evidence for the read-only coordination-notes routes in `serving/notes.py`. This is the first
Python test module for those routes. The task reader fetches the notes listing whenever a task opens,
over a tree that holds thousands of files. The module checks four things:

- the listing's **exact wire bytes** on a tree that holds every entry kind the walk must classify;
- that a directory **swapped for an escaping symlink** mid-walk is refused;
- that the listing's filesystem work **does not grow** with the number or size of the notes;
- that **live refresh**, the scoped refusals and note reads still give the answers the reader relies on.

Cost is checked by **counting `realpath` calls and refusing any content open**, not by timing. So the
scale case is deterministic on any machine, and it fails on the old per-entry-resolving walk (49 and
751 calls against the expected 4).

## Code Commentary

### Logic

**Harness.** `_client` builds an `McpRuntimeConfig` under `tmp_path` with one repository, `R`,
registers only `register_notes_routes` on a bare `FastAPI` app, and drives it through `TestClient`.
`_notes_root` is `coord/tasks/R/260101_series/notes`. `_wire` renders a payload exactly as
`JSONResponse` does (compact separators, `ensure_ascii=False`), so the case compares response bytes,
not parsed JSON.

**Cases** (5 functions, 6 collected cases):

- `test_listing_bytes_classify_every_entry_kind_and_prune_at_the_depth_cap` builds
  `_build_classification_tree`. The tree holds:
  - hidden, binary and case-tied files, and a FIFO;
  - in-root, escaping and broken file symlinks;
  - an escaping directory symlink;
  - four symlinks whose followed stat fails with `ELOOP` or `ENOTDIR`: `loop-self`, the pair
    `loop-a`/`loop-b`, `x -> x/../x`, and `bad -> a.md/child`;
  - a four-level `reports/deep/d2/d3` chain;
  - an in-root directory symlink, `alias`, that points into that chain.

  The expected bytes pin five behaviours. Files come before folders, in case-folded order. In-root
  symlinks are listed under their own path (`link-in.md`, `alias/e.md`, `alias/d3/f.md`). Escaping,
  broken, looping and file-traversing symlinks and non-regular entries are skipped. The fourth folder
  level is pruned. And `truncated` is `true`.
- `test_a_directory_swapped_for_an_escaping_symlink_before_it_is_opened_is_refused` monkeypatches
  `os.open` and `os.scandir` so that the first directory-open spelling of `notes/d` fires a swap. The
  spelling may be relative to a parent descriptor or by path. The swap replaces `d` with a symlink to a
  directory outside the root. The listing must answer 200 with only `keep.md`, and the case asserts the
  swap actually fired.
- `test_listing_work_does_not_grow_with_note_count_or_content_size[6x1B|240x64MiB]` builds sparse
  notes over three folder levels plus one in-root file symlink. `_count_realpath` wraps
  `os.path.realpath`, and `_refuse_file_opens` makes `io.open` raise. At both sizes the listing must
  return every note with its real size, and it must make exactly **4** `realpath` calls: one for the
  root, and three for the one symlink (`resolve()`, then `path_is_relative_to` resolving both the entry
  and the root).
- `test_listing_reflects_a_new_or_grown_note_on_the_next_request` lists, writes a new note, grows an
  existing one in place, and lists again. The second listing must show both at their current sizes,
  so no listing state outlives a request. This protects `ICR-R17` live refresh.
- `test_scoped_refusals_and_note_reads_keep_their_wire_answers` walks the `_REFUSALS` table:
  - list: unknown repo → 404 `unknown-repo`; multi-segment master → 400 `bad-request`; a young
    master with no notes → an empty list;
  - read: a note → 200 as text; traversal → 400 `bad-path`; a symlink escape → 400 `bad-path`; a
    missing note → 404 `not-found`; a binary note → `language: "binary"`.

### Conventions

- Wire identity is asserted as bytes (`response.content == _wire(expected)`), because the leaf's
  preservation constraint is byte identity, not parsed-JSON equality.
- The monkeypatches are installed **inside** the `TestClient` context, after app startup, so only the
  listing request is counted or refused.
- Timings, profiles and the 34-master live byte-identity comparison are **not** in this module. They
  are task-local evidence for the leaf (`notes/reports/l55-evidence/` and the review evidence folders).
  They depend on the live corpus and the host.

### Invariants And Boundaries

- Keep the scale case **count-based**, at two sizes. A timing threshold would be flaky and would not
  name the regression. The expected count of 4 is exact: a per-entry resolve coming back, or a second
  resolve per symlink, changes it.
- Do not drop an entry kind from the classification fixture to make the byte case pass. Each one
  covers a behaviour that regressed or could regress. The loop and file-traversing symlinks are the
  L55-R1-F1 regression, which made the whole listing HTTP 500 on attempt A1.
- The swap case must keep asserting that the swap fired (`assert swapped`), so it cannot pass
  vacuously if the walk stops opening directories the way the patch expects.
- The read-but-not-searchable directory deviation (accepted by ruling) has no case in this module. The
  corpus holds no such directory. The review fixtures record it as `perm_r_nox` and `link_to_rnx_dir`
  (`notes/reports/l55-review-R2-evidence/`).
- The module is registered in the `unit-regression` lane of `mcp/tests/test-evidence-lanes.toml`. It
  uses only `tmp_path` and `monkeypatch`, plus an in-process `TestClient` on a bare app. The first run
  without the lane row exited with pytest status 4, which is how the worker found the omission (event
  E5).

### Todos

No implementation scope is opened here. Re-timing the installed build on the live server belongs to
L50 (worker observation O-C).

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern the repository's
own test fixtures and assertions, so the retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

- The module's own statement of what it protects. [1]
- The isolated route harness: one repository, only the notes routes, a bare app. [2]
- The exact bytes `JSONResponse` renders, which the byte case compares against. [3]
- The classification fixture, including the `ELOOP`/`ENOTDIR` symlinks and the in-root directory alias. [4]
- Byte identity over every entry kind, with the depth cap and `truncated`. [5]
- A directory swapped for an escaping symlink at its open is refused. [6]
- The `realpath` counter and the content-open refusal. [7]
- Four resolutions at 6 × 1 B and at 240 × 64 MiB, with no note opened. [8]
- A new or grown note appears on the next request. [9]
- The refusal and read table. [10]
- The production walk under test: symlink-only confinement, descriptor descent, and the sort key's errno parity. [11]
- The routes under test. [12]
- The lane registration. [13]

### Cross-Repo References

This card covers test behavior only. There is no separate cross-repository protocol or live
installation involved.

No meaningful cross-repo references found.
