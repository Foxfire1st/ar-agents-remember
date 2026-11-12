# mcp/src/agents_remember/memory/knowledge/tree_observation.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**What a source observation *is*, shared by every reader of a code-tree pair.** The config review's
inventory, the comparison's expansion and the attribution partition all read the same three values —
the two bound sides, the paths they differ at, and the seam that produces them — so the vocabulary
lives here rather than inside any one of its readers. Nothing in this module measures anything: a
probe produces these values, and a reader of them states what the measurement could and could not
carry.

## Code Commentary

### Logic

`TreeSide` is one side's source binding: the exact code tree id and the repository root it lives in.
The two travel together because they answer different questions — the tree id is the *identity* the
comparison resolved against, and the root is *where* a caller runs the command the expansion
publishes. `tree_id=None` is a supported state, not a failure: the record half of a comparison is
complete without a source half.

`TreeChange` is one path two code trees differ at, with Git's own status letter and what can be
rendered (`text`/`binary`/symlink/submodule/`unknown`), a mode-change flag, and the reason an
`unknown` is unknown. `path` is the raw filename exactly as Git recorded it — a tab or newline inside
a name is part of the address, which is why the observation that produces these values reads a
NUL-delimited Git interface rather than lines. `detail` states why `content` is `unknown` and is empty
for a measured classification, so a reader never has to guess whether an unknown was measured and
failed or simply not reported.

`TreePaths` is the honesty boundary of the whole source half of a review. `available` is separate from
`paths` on purpose: a probe that could not run (an absent root, a tree this repository does not hold)
has **not** observed *no changes*, and reporting its silence as "nothing changed between the trees"
would be a fabricated fact. `entries` is the same measurement at full resolution — one `TreeChange`
per *carriable* path, held in agreement with `paths` by a `__post_init__` that refuses a value whose
paths are not exactly the entry paths. `partial` says the path set was measured while part of it could
not be reported whole, and `unrepresentable` carries the changed paths whose *name* is not valid UTF-8
in full rather than dropped, with `unrepresentable ⇒ partial` enforced at construction: a Git pathname
is bytes and this surface carries text, so dropping such a path would make a partial change set read
as a whole one.

`TreeDifferenceProbe` is the Git seam narrowed to one question (`Callable[[TreeSide, TreeSide],
TreePaths]`): a callable rather than a class so the application layer can pass the same kind of seam
the anchor resolver is, and so a case can substitute an observation without a repository.
`no_tree_difference_probe` is the honest answer for a comparison whose sides named no code tree: the
record half is complete and the source half was not requested.

### Conventions

- Frozen dataclasses: an observation is a measured value, never accumulated into.
- Every `detail` is prose written **for a reader**; nothing in it is parsed by the package, and the
  typed fields (`available`, `partial`, `paths`, `entries`, `unrepresentable`) are what a caller
  branches on.

### Invariants And Boundaries

- **An unavailable observation is never an empty change set.** `available=False` contributes no
  expansion at all and says so through its `detail`.
- **Paths and entries are two renderings of one measurement.** A value whose paths are not exactly
  its entry paths describes no observation and is refused at construction.
- **An unrepresentable path implies a partial observation.** A complete observation beside an
  unrepresentable path describes no measurement and is refused at construction.
- **Boundary.** This module declares shapes. It performs no Git command, opens no database, resolves
  no anchor and partitions nothing — probes produce these values elsewhere, and readers state their
  scope from them.

### Todos

None recorded. The module was extracted whole from `diff_display.py` in leaf `260921-ICR-L4`'s
seam-extraction fix round along the established seam policy (one implementation, purpose-named
adjacent module, original keeps re-exporting); `diff_display` re-exports every name here, so an
importer that has always read them from the display seam keeps working.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **One side's source binding: the exact tree and the root the command runs in, with `tree_id=None` a supported state.** [1]
- **One changed path: the raw filename as the address, Git's status, the renderability, the mode flag and the reason an unknown is unknown.** [2]
- **The observation: availability apart from paths, entries held in agreement with paths, and the unrepresentable-implies-partial rule.** [3]
- **The Git seam as one question, and the probe that observes nothing for a comparison whose sides named no code tree.** [4]
- **The shared vocabulary defined once and re-exported at the display seam, so existing importers keep working.** [5]
- **The two readers that consume this vocabulary beside the display.** [6]

### Cross-Repo References

No cross-repository behavior is implemented in this file. Every statement runs against values the
caller supplied; no second repository, ledger or coordination path is read.

No meaningful cross-repo references found.
