# mcp/test_support/agents_remember_test_support/testing/review_git_trees.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Build the shared isolated real-Git code/memory world used by focused recorded-tree reviewer tests. Preserve paired-tree identity, converted records, history and native capture semantics while keeping each fixture independent.

## Code Commentary

Build the shared isolated real-Git code/memory world used by focused recorded-tree reviewer tests. Preserve paired-tree identity, converted records, history and native capture semantics while keeping each fixture independent.

`World.contract` writes the enclosure the shipped reader parses. `closeout` and `integration` supply whole lifecycle sections: the closeout section always carries a status, then any cells given, and an integration section is written only when one is supplied. A test therefore writes a landed leaf's delivery records — the closeout's memory content commit and the integration landing's code commit — without hand-writing the file's YAML, and a non-live world points the leaf at `removed-code`/`removed-memory` addresses instead of live worktrees (`:191-192`); the calling test, not the fixture, removes the group's directories.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- Build the shared isolated real-Git code/memory world used by focused recorded-tree reviewer tests. Preserve paired-tree identity, converted records, history and native capture semantics while keeping each fixture independent. [1]

- The fixture enclosure takes closeout and integration cells, always writes a closeout status, and points a landed leaf at `removed-code`/`removed-memory` addresses instead of live worktrees; the calling test removes the directories itself. [2]
