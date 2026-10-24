# mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/task-publication.md

## Governing Overview

[Packaged runtime overview](../../../../../overview.md)

## Purpose

The shipped example of a repository's publication policy: the setting that decides whether a landing
goes through a pull request, the spine of when an issue exists, both landing paths, the gates that run
before a push, the merge convention, and the release line. It is example text a fresh memory repository
starts from, not a policy this repository itself is governed by.

## Code Commentary

The file opens with the landing-workflow setting, names both values, and names the reader that parses
it, so a repository owner sees the switch beside the path it changes. [1] The spine and the
issue-and-PR trigger follow: which work gets an issue, when that issue disappears, and what a leaf
claims on the board. [2]

Then the two landing paths are stated separately, which is the point of the current text. The `local`
workflow's flow is the landing itself - the merge that carries the branch is the record - and its gates
are given in one line. [3] The `pull-request` workflow publishes an already-integrated `H`: it names
`B`, `H` and `M`, the three refs the publication is judged by, and it refuses squash and rebase because
the publication merge must keep `H` as its second parent with `H`'s tree. [4] The merge-commit
preference is scoped by that heading: it is the `local` convention, and the pull-request path refuses
what it prefers. [5]

The release and changelog convention closes the file and names the version sites a release edits. [6]

## Invariants And Boundaries

This is packaged example content copied into a new repository's memory by the installer. Editing it
changes what a fresh repository starts with; it does not change this repository's own
`system/task-publication.md`, and no code path reads the example at runtime. The two copies - this
packaged one and the root `system/defaults/examples/memory-repo/task-publication.md` - are byte
identical, so a reader who follows either learns the same rule.

## Evidence

### Repo-Internal References

- The landing-workflow setting, both its values and the reader that parses it. [1]
- The spine, and the issue-and-PR trigger with the board state a claimed leaf takes. [2]
- The `local` landing flow, and its gates in one line. [3]
- The `pull-request` publication of an already-integrated `H`, with `B`, `H`, `M` and the refusal of
  squash and rebase. [4]
- The merge-commit preference under its own `local` heading, so the rule is not read as universal. [5]
- The release and changelog convention naming the version sites a release edits. [6]
