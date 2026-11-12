# mcp/test_support/agents_remember_test_support/testing/git_command.py

## Governing Overview

[Testing support overview](overview.md)

## Purpose

Provide the shared real-Git `_init` and `_commit` fixture primitives for the runner and object-memo tests. They use the guarded production Git runner against each caller-supplied temporary repository.

## Code Commentary

`_init` creates a main branch and fixture identity. `_commit` writes the named file, stages it, commits it and returns HEAD. Both consuming test modules import these helpers directly; the move retains their assertions and creates no alternate product Git route.

## Evidence

- Shared fixture primitives create and commit real temporary repositories through the guarded runner. [1]
