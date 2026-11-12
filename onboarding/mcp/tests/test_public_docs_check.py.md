# mcp/tests/test_public_docs_check.py

## Governing Overview

[overview](overview.md)

## Purpose

`mcp/tests/test_public_docs_check.py` proves that the public documents and the tree agree at the candidate, and that `scripts/check-public-docs.py` can fail. It runs the check on the checkout, which must have no finding, and proves each finding kind by one in-memory mutation of the checkout's own documents: the mutation must add exactly the finding it names — the file, the line and the target. The command-line cases build a small Git repository in a temporary folder, because the script lists the files that Git tracks; one proves that a file Git does not track is not read.

## Code Commentary

`_load` imports `scripts/check-public-docs.py` by file location as module `check_public_docs`. The `tree` fixture builds the index once from the repository root, and `baseline` records the findings of the clean checkout so a mutation case can subtract them.

The cases cover the whole finding set: a broken relative link, an absolute link to a missing repository path, a missing anchor, a missing repository path, a path Git ignores or another check owns, a relative link out of `docs/`, an unreached page, a page behind two index pages, a differing step title, a missing step, a differing command line, an identifier on every page — including product-shown rule codes and sandbox names — a front page without the roadmap link, an entry point that drops an owed link, a relative link in the package description, a marker with a reason that allows its line and no other, and a marker without a reason or without a use. The command-line cases run the script as a process in a temporary Git repository: they prove it names `file:line: target` and exits non-zero, that a named path behind a symbolic link does not stop the check, and that a file Git does not track is not read or counted; a final case runs it on this checkout and proves it passes.

## Boundaries

The module proves the check's finding kinds and its exit behavior; it does not prove that the prose of any public document is true. The check's own rules are described in the card of `scripts/check-public-docs.py`.

## Evidence

- The docstring states the clean-checkout case, the mutation method and the Git-backed command-line cases. [1]
- The script is imported by file location as `check_public_docs`. [2]
- The clean checkout must have no finding. [3]
- Each link, anchor and path finding kind is proved by one mutation. [4]
- Reach, step and identifier findings are proved on every page, including product-shown names. [5]
- Entry-link and package-description findings are proved. [6]
- Markers allow their line and are findings when malformed. [7]
- The command line names file, line and target and fails on a finding; an untracked file is not read. [8]
- The script passes on this checkout. [9]
