# .githooks/pre-commit

## Governing Overview

[Repository overview](../overview.md)

## Purpose

The repository's fast pre-commit tier entry. It hands the `fast` tier to `.githooks/_gate.sh`, so a commit judges the staged content with deterministic lint, format, type, generated-copy and dashboard checks. It runs no test.

## Code Commentary

The header records the measured cost on a clean checkout: about 11.4 seconds cold and 10.8 seconds warm. Pyrefly completes the full pass in about 1.8 seconds (down from about 198 seconds under Pyright), and the concurrent dashboard rail runs in parallel. The peak combined resident set is about 1.09 GiB cold and 0.95 GiB warm. The script resolves its own directory and executes `_gate.sh fast` with that one argument; it performs no check itself and keeps no state.

## Relationships

`.githooks/_gate.sh` owns the tier body, the MCP environment preflight and the result line the landing check reads. `setup-hooks.sh` enables the hook per clone. The landing commit check, a continued code-side sync commit and the Dagger pipeline run this hook on the tree they publish; no product route passes `--no-verify`.

## Evidence

- The hook executes the fast tier over the staged content and its header states the measured cold and warm times and peak combined RSS. [1]

- The fast tier is the shared hook body's `run_fast_checks`, which the landing and sync commit checks invoke. [2]
