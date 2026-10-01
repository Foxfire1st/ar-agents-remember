# mcp/src/agents_remember/application/knowledge_currentness/observe.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**One entry's state at one code tree, and the observation cache (MIK-R03 rules 1 and 5).** An entry is a
realization or a proof (MIK-R21). It is observed at a code tree T with MIK-R08's definitions, reusing the
worklist's own resolution (`CodeTrees.resolve` from `knowledge_worklist/code.py`) and the one content
identity (`models/knowledge_files/anchor_content`), so there is no second resolver and no second hash.

## Code Commentary

### Logic

- `CodeTree(repository, tree)` is the tree a read asks about. `open_code_tree` reads its file list once
  into an `OpenedCodeTree`; `None` gives the problem "no code tree was requested" (`NO_TREE_REQUESTED`), and
  an unreadable tree (`CodeReadError`, `OSError`, `ValueError`, `subprocess.SubprocessError`) gives a problem
  naming the tree.
- `observe_entry(entry, code)` returns an `EntryObservation`: the state, the reason, and the recorded and
  observed blob and content. `_verdict` decides it.
- **The check order (architect ruling N1, 2026-09-29T19:13:41).** `_decided_without_resolving` applies the
  packet table's checks that need no resolution, in this order:
  1. no tree, or an unreadable tree: `unverifiable`, with the tree's problem;
  2. the path is absent at T (no regular file): `stale`;
  3. T's blob equals the recorded blob: `current`, whatever the locator kind;
  4. only for a changed blob, an unsupported locator kind (`_unsupported`: a kind outside
     `_SUPPORTED_LOCATORS`, or a `symbol` in a file no shipped grammar reads, such as Markdown):
     `unverifiable`.
- Otherwise `_observed_content` resolves the locator in T's blob. `None` (the symbol is bound twice or
  nowhere, or the line range has no mapping) is `stale` with `_unresolved`'s reason; content that differs is
  `stale`; equal content is `current` (`_compared`).
- **A line range recorded against a blob the store lacks is `unverifiable`** ("a needed Git object is
  unavailable"), by architect ruling 5 of 2026-09-29T18:42:37. L08's worklist classifies the same case as
  no mapping, each leaf following its own packet. Since MIK-R09 (L09 review R2-3) `_observed_content` raises it
  as `CodeObjectUnavailable`, a `CodeReadError` subclass: "the blob … the line range was recorded against is
  unavailable".
- **Git failures (ruling N2), caught in `observe_entry` since MIK-R09.** `_verdict` no longer catches: its
  exceptions reach `observe_entry`, which gives `unverifiable` in every case and sets the new
  `EntryObservation.read_failed` only for a **Git read failure** (L09 review R1 F4/F9 and R2-3):
  - a `subprocess.SubprocessError` (including `TimeoutExpired`) or `OSError`: "a Git read failed (<type>:
    <message>)", `read_failed`;
  - a `CodeReadError` from a Git read (a tree, a blob, a diff, or a `has_blob` that Git could not answer, L09
    review R3-2): its message, `read_failed`;
  - a `CodeObjectUnavailable`, or a `CodeReadError` whose cause chain holds a `GrammarUnavailableError`
    (`_git_read_failure`): its message, **not** `read_failed`: a persistent, non-Git cause. The entry is simply not
    `current`, and its reason names the object.
  - an unreadable tree (`code.problem` other than "no code tree was requested") also sets `read_failed`.

  `to_document` is unchanged. The mandatory gate (MIK-R09) treats a `read_failed` entry as an unreadable input
  (`GateContext.entry_state` raises `GitReadFailed`, so the run is `incomplete [git]` and never memoised; at a master
  landing, `knowledge-worklist-incomplete`); any other `unverifiable` keeps its item open with the named reason
  (at a master landing, `knowledge-unverifiable-at-landing`). L03's pinned reason texts are unchanged.
- **The cache (rule 5).** `observation_key` is `(blob, locator, path, recorded blob, extractor version)`.
  The locator is its canonical JSON; the path is included because its suffix chooses the grammar; the
  recorded blob is included only for a line range, whose mapping starts there (ruling 4, 18:42:37).
  `EXTRACTOR_VERSION` is `anchor-observation/v1` plus the measured tree-sitter grammar versions, so a changed
  extractor never reads an old answer. `OBSERVATIONS` is a `BoundedMemo` (ICR L56's
  `read_anchor_memo`) of **8,192 entries** (`_OBSERVATION_CAPACITY`, ruling N3): about 600 bytes per entry,
  about 5 MB in total, under 10 MB even at 1.2 KB per entry. A whole-repository run needs about 180.

### Conventions

- The observed value cached is the content identity of the resolved range, or `None` for "does not
  resolve". The cache holds answers only.

### Invariants And Boundaries

- **A failed observation is never cached.** `CodeReadError`, `SubprocessError` and `OSError` are raised
  before `cache.put`, so the next read observes again (the timeout test then finds the entry `stale`).
- **Only the caller's resolved tree is consulted.** There is no fallback to a working tree or `HEAD`
  (MIK-R03 Preservation); with no tree, every entry is `unverifiable`.
- **Reads only.** Nothing is written, re-anchored or judged (rule 6).
- **Observing never raises for Git.** Every Git failure becomes an `unverifiable` entry with a named
  reason.
- **A Git failure is told apart from an unavailable object (MIK-R09, L09 review R2-3).** Only a Git failure sets
  `read_failed`; callers never read it as "absent" or "unchanged". Proved by
  `test_a_code_object_that_is_unavailable_is_named_and_keeps_the_item_findings`,
  `test_a_recorded_blob_the_store_lacks_is_named_at_its_real_raise_site` and
  `test_a_git_failure_asking_for_a_recorded_blob_is_incomplete_and_never_kept` (`test_knowledge_gate_routes.py`).

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R03@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`03_stale-invariants-flagged-at-read-time.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The state table, the check order, the no-fallback rule and the cache contract. [1]
- The extractor version, the supported kinds and the 8,192-entry bound with its memory estimate. [2]
- The process-wide observation cache. [3]
- The requested tree, and one read of its file list with a named problem for none or an unreadable tree. [4]
- One entry's observation and its wire shape. [5]
- The cache key. [6]
- The verdict: the checks that need no resolution, then resolution and comparison; since MIK-R09 its read errors propagate to `observe_entry`. [7]
- The two causes of a failed read, told apart (L09 review R2-3). [8]
- The observation catches every read error and sets `read_failed` only for a Git failure. [9]
- A persistent unavailability is not a Git failure. [10]
- The ruling-N1 order: no tree, absent path, unchanged blob, then an unsupported kind. [11]
- Which locator kinds cannot be re-resolved in a changed blob. [12]
- Resolution through the worklist's resolver; a missing line-range blob is raised as `CodeObjectUnavailable`, and only answers are put in the cache. [13]
- The reused resolver: the worklist's tree reader and its `resolve`. [14]
- The order cases: unchanged Markdown is current, changed is unverifiable, deleted is stale. [15]
- A timed-out Git call is unverifiable and is not cached. [16]
- The cache key's contents and its reuse. [17]

### Cross-Repo References

No meaningful cross-repo references found: the module reads one code repository's object store, named by
its caller.

No cross-repo boundary is crossed by this file.
