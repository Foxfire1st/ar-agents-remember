# mcp/src/agents_remember/application/knowledge_currentness/observe.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_currentness/observe.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T19:59:41+02:00 |
| lastVerifiedCommitHash | `719acba61e491d0b7f1ee82dbeea5314ecec5083`|
| lastVerifiedCommitDate | 2026-09-29T20:27:14+02:00|
| governingOverview | `../overview.md` |

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
  no mapping, each leaf following its own packet.
- **Git failures (ruling N2).** A `CodeReadError` gives `unverifiable` with its message; a
  `subprocess.SubprocessError` (including `TimeoutExpired`) or `OSError` gives `unverifiable` with "a Git
  read failed (<type>: <message>)".
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

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R03@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`03_stale-invariants-flagged-at-read-time.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The state table, the check order, the no-fallback rule and the cache contract. | "The checks run in the table's order" | mcp/src/agents_remember/application/knowledge_currentness/observe.py:1-37 |
| The extractor version, the supported kinds and the 8,192-entry bound with its memory estimate. | `EXTRACTOR_VERSION`; `_SUPPORTED_LOCATORS`; `_OBSERVATION_CAPACITY` | mcp/src/agents_remember/application/knowledge_currentness/observe.py:70-76; mcp/src/agents_remember/application/knowledge_currentness/observe.py:80-80 |
| The process-wide observation cache. | `OBSERVATIONS` | mcp/src/agents_remember/application/knowledge_currentness/observe.py:84-84 |
| The requested tree, and one read of its file list with a named problem for none or an unreadable tree. | `CodeTree`; `open_code_tree` | mcp/src/agents_remember/application/knowledge_currentness/observe.py:89-97; mcp/src/agents_remember/application/knowledge_currentness/observe.py:110-125 |
| One entry's observation and its wire shape. | `EntryObservation` | mcp/src/agents_remember/application/knowledge_currentness/observe.py:128-156 |
| The cache key. | `observation_key` | mcp/src/agents_remember/application/knowledge_currentness/observe.py:159-166 |
| The verdict: Git failures become `unverifiable` with a named reason. | `_verdict` | mcp/src/agents_remember/application/knowledge_currentness/observe.py:217-235 |
| The ruling-N1 order: no tree, absent path, unchanged blob, then an unsupported kind. | `_decided_without_resolving` | mcp/src/agents_remember/application/knowledge_currentness/observe.py:238-255 |
| Which locator kinds cannot be re-resolved in a changed blob. | `_unsupported` | mcp/src/agents_remember/application/knowledge_currentness/observe.py:264-275 |
| Resolution through the worklist's resolver; a missing line-range blob is raised, and only answers are put in the cache. | `_observed_content`; `cache.put` | mcp/src/agents_remember/application/knowledge_currentness/observe.py:278-306 |
| The reused resolver: the worklist's tree reader and its `resolve`. | `CodeTrees`; `has_blob` | mcp/src/agents_remember/application/knowledge_worklist/code.py:191-332 |
| The order cases: unchanged Markdown is current, changed is unverifiable, deleted is stale. | `test_unverifiable_names_why_for_no_tree_an_unreadable_tree_and_an_unsupported_locator` | mcp/tests/test_knowledge_currentness.py:340-365 |
| A timed-out Git call is unverifiable and is not cached. | `test_a_failed_or_timed_out_git_call_is_unverifiable_with_its_reason` | mcp/tests/test_knowledge_currentness.py:368-378 |
| The cache key's contents and its reuse. | `test_observations_are_keyed_by_blob_locator_and_extractor_version_and_reused` | mcp/tests/test_knowledge_currentness.py:469-502 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads one code repository's object store, named by
its caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): created this card for the new file MIK-R03 adds. It records the architect rulings of 2026-09-29: 18:42:37 rulings 4 (the extended cache key) and 5 (a missing line-range blob is `unverifiable` here), and 19:13:41 rulings N1 (the check order), N2 (Git failures are `unverifiable`, never cached) and N3 (the 8,192-entry bound). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
