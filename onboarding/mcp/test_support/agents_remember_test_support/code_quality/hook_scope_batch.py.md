# mcp/test_support/agents_remember_test_support/code_quality/hook_scope_batch.py

## Governing Overview

[Python quality verification overview](overview.md)

## Purpose

Single-invocation scope-batch emission for the repository's Git hook tiers. It derives the quality scope once and renders every tier scope line in a fixed order so the hook does not spawn a Python interpreter per step.

## Code Commentary

`collect_hook_scope_batch` validates the quality configuration and the hook invocation environment, derives one `GateScope`, renders the hook-tier wrapper line, adds the untracked-input lines only for a pre-commit sequencer run, and renders the three generated-copy lines and the four fixed-step lines. The generated-copy lines are computed concurrently; the returned mapping keeps the fixed key order that `_gate.sh` replays. `write_hook_scope_batch` writes each line to its own file under the caller's temporary directory. The renderers are passed in through `HookScopeLineBuilders` so this module does not import the reporting module that imports it.

## Relationships

`scope_reporting.py` supplies the line builders and the `hook-batch` subcommand; `.githooks/_gate.sh` calls that subcommand once per run and prints each line before its check. The fixed-step vocabulary is the hook's own: `ruff`, `ruff-format`, `pyright` and `evidence-lifecycle`.

## Evidence

- One invocation derives the scope and renders every hook-tier line in fixed order. [1]
- The batch writer persists one payload per scope key under the given directory. [2]
