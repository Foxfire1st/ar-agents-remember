# mcp/tests/test_knowledge_read_paths.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**What a *path* is to this read: an address, not a pattern.** Five nodes in `integration` (row
`mcp/tests/test-evidence-lanes.toml:158`) covering the one contract the review corrected most sharply — the
predicate that decides which spellings are addressable, and the requirement that **a refusal describe the
actual cause**.

644 lines. This module exists because the path cases pushed `test_knowledge_read_boundaries.py` past the
repository's 1 200-line hard limit in fix round 2; the cases moved here rather than the limit being waived.

## Code Commentary

### Logic

**`test_a_pathspec_magic_spelling_is_refused_by_the_typed_path_and_never_answered_as_absence`** (`:178`) —
the boundary node. It refuses a leading-`:` spelling at **both** typed boundaries (`SourceAnchorDraft`'s
write path and `PathSeed`'s seed path) and measures the Git facts themselves with its own subprocess calls,
so the premise is evidence rather than prose.

**`test_a_path_holding_glob_characters_is_authorable_seedable_and_observed_as_its_blob`** (`:256`) — the
node the review's correction rests on. It commits its own tree holding **both** `src/a1.py` and
`src/a[1].py`, measures `git ls-tree` addressing `src/a[1].py` literally with `rc=0`, then (1) authors a
`SourceAnchorDraft` at that path through the typed write path, (2) stores the claim and anchor through the
ordinary store operation, (3) constructs `PathSeed(path="src/a[1].py")`, and (4) reads it back through
`read_knowledge_scope` asserting `exact_recorded_blob` with the observed blob equal to the tree's blob.
**The mutation that inverts this result is the read path re-admitting a glob refusal**, which flips the
outcome to `unsupported_locator` — the exact flip the reviewer measured on the pre-fix candidate.

**`test_a_stored_path_that_cannot_be_addressed_is_refused_rather_than_reported_absent`** (`:370`) — a row
written by something other than the typed API is reported `unsupported_locator` with the spelling refusal
in `detail`, **not** `path_absent`.

**`test_a_failed_tree_lookup_is_unavailable_rather_than_an_absent_path`** (`:445`) and
**`test_a_git_that_cannot_run_is_unavailable_rather_than_an_absent_path`** (`:539`) — the two producers of
`recorded_object_unavailable` pinned separately. The second drives the `OSError` producer by intercepting
the single `ls-tree` call while delegating every other command to the real runner; the first reads a real
stored anchor against a tree the repository does not hold and asserts the availability producer's own
`detail`, while the same claim against the fixture's real tree is a genuine `path_absent`.

**The rule, restated once:** Git pathspec **magic** is the leading-`:` family (`:(exclude)`, `:!`,
`:(top)`, `:/`) plus `..`, absolute paths, `~`, drive/UNC spellings, backslashes and NUL. The characters
`*`, `?` and `[` are **literal characters** to `ls-tree`, so a legitimate anchor containing them must be
authorable, seedable and resolvable — and **a caller must never be told a path is absent when the real
reason is its spelling.** `git ls-files` is the command that *does* glob those characters, and it is not the
command a stored anchor path is handed to.

### Conventions

- `pytestmark = pytest.mark.integration`; the module is registered in the integration lane, and it is one
  of the three declared consumers of `knowledge-read-scope-cases`.
- Every Git fact the module relies on is measured by the module itself with `subprocess`, against a tree it
  commits in `tmp_path`.
- A refusal node asserts the resolution state **and** the `detail`'s distinguishing content, because for
  this contract the code alone (`unsupported_locator`) is deliberately shared with the symbol-locator case.

### Invariants And Boundaries

- **The non-zero-exit branch of `_tree_entry` is not covered here or anywhere.** This module drives the
  `OSError` producer and the availability producer; the third branch is an explicitly disclosed unasserted
  defensive branch (L9 ledger **A6**). The erratum withdrew the claim that a mutation made it reachable.
- **A sibling node in the boundaries module carries a `detail` assertion at `:521-526`** which is a
  pre-existing node's extension, not a new case — a fact the round's own change summaries under-described.
  It is recorded here so a successor reading the change set sees four edits rather than three.
- **Boundary.** This is a test module. It declares one lane, asserts behaviour and owns no production
  contract.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The pathspec-magic boundary node: a leading-`:` spelling refused at both typed boundaries, with the Git facts measured by the module itself.** [1]
- **The glob-character node the review's correction rests on: authored, stored, seeded and resolved to its own blob.** [2]
- **The unaddressable-stored-spelling node: a refusal of the spelling, never an absence from the tree.** [3]
- **The lookup that ran and could not answer, refused as unavailable rather than absent.** [4]
- **The lookup that could not be run at all, reported as the same fact.** [5]
- **The corrected predicate this module measures: leading `:` refused; `*`, `?` and `[` admitted as literal characters.** [6]
- **The write-path boundary that applies the shared rule, so a malformed anchor cannot be authored.** [7]
- **The seed boundary that applies the same rule, so a refused spelling cannot be presented as a seed.** [8]
- **The pre-existing sibling node's `detail` assertion, which round 3 added (the fourth worktree edit).** [9]
- The lane row this module occupies. [10]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
