# mcp/tests/test_capture_baseline.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Guard the capture baseline's "nothing moved" proof: which changes are doubts that force a
re-derivation, which are not, and that the proof never descends into a Git-ignored dependency
directory. The cases run against disposable repositories, so each one asserts the proof over real
Git evidence rather than a mocked helper.

## Code Commentary

### What is a doubt, and what is not

A worktree is captured, then moved in one named way and re-checked. A file edit, a staged change, a
new commit, a new untracked file, a new file in a new directory, an edit to an ignore rule, a change
to an already captured path, a restored deleted tracked file, an external ignore change in either
direction and a staged addition beside a changed external ignore each make the proof doubt, and a
doubt re-derives. A change inside an ignored folder is not a tree doubt, and a HEAD-only move is not
a tree doubt when the tree was captured with a head binding the same run still observes.

### Ignore semantics are exercised where they were wrong

The wildcard-negation case, the significant-leading-space case and the restored parent-directory
mtime case are the three shapes an eligible addition used to hide behind. The observation case
intercepts `os.scandir` and asserts no call under an ignored `node_modules` directory, so the test
measures the filesystem calls the proof makes instead of a retired helper's name. The pattern model
is the thing under test in all four.

### Scope

These are source-level regressions over the proof and its ignore model on real Git. They are not a
claim about an installed process, a whole-suite total or a review's latency.

## Evidence

- Every named kind of change to the captured tree is a doubt, and a change inside an ignored folder is not. [1]
- An eligible addition under a wildcard negation is a doubt. [2]
- A restored parent-directory mtime cannot certify an unchanged tree. [3]
- The proof observes no path under a Git-ignored dependency directory (the test instruments `os.scandir`). [4]
- An external ignore change invalidates the proof in both directions. [5]
