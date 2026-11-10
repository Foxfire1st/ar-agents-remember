# mcp/tests/test_cardless_knowledge_writer.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Check that the public knowledge writer plans and commits a leaf's first entries on a fresh repository before any onboarding Markdown card exists, while reference-bearing sidecars still need their card and the persisted worklist stays mandatory.

## Code Commentary

The fixture builds a fresh repository with `fresh_repository()`, writes a code identity test and a task document, runs `memory_quality_check` to persist the worklist, and asserts the memory worktree has no `onboarding/` directory. The parametrized plan-and-commit case checks that planning writes nothing, that committing writes `onboarding/app.py.json` with empty references and one realization, that a requested proof adds a `proves` sidecar for the code test, that no Markdown is created, and that a repeated commit is byte-stable. A sidecar given references without a Markdown card is refused with `R22.3-sidecar-without-markdown` and the tree is unchanged. Without a persisted worklist, the writer refuses and names `memory_quality_check`.

## Evidence

- The fresh fixture starts from a cardless memory worktree with a persisted worklist. [1]
- Planning writes nothing; committing writes an entries-only realization sidecar without Markdown. [2]
- A requested proof adds a `proves` entry and no references. [3]
- A sidecar with references still needs its Markdown card. [4]
- The cardless leaf still requires its persisted worklist. [5]
