# mcp/tests/test_bootstrap_uv_minimum_version.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Protect the host bootstrap's numeric uv floor, PATH selection, diagnostics and pre-mutation refusal without procuring uv.

## Code Commentary

The module sources the guarded bootstrap for comparator/gate probes and invokes the actual main path for refusals. Fake PATH executables report equal/newer/older or unreadable versions; decimal comparisons include missing parts, major changes and leading zeroes. Accepting a shim proves gate selection and its log, not a real successful environment build. Missing/older/unreadable output is checked against the actual diagnostics; nonzero version-command output is not relabelled empty.

Each executable test uses temporary XDG data/cache/config roots. The existing-environment refusal case can check a marker when a venv is present. The sync-failure case (`test_sync_failure_names_both_uv_versions`) is parametrized over directory and symlink predecessors (`linked=[False, True]`), runs `main` directly via `run_driver` against a fake `uv` shim and fake runtime Python shim without copying scripts or requiring a live host runtime, asserts stderr names both observed and minimum uv versions, verifies predecessor restoration (including symlink vs directory kind and `.restore-marker`), and checks the failed partial venv is retained under `XDG_CACHE_HOME/agents-remember/venv-backups`. The no-uv-fetch case checks absence of curl, wget and a `uv==` pin in the script; its textual guard is narrower than a whole-program effects proof. Real successful-build/package-equivalence evidence belongs to the separate producer run receipts.

## Evidence

- Decimal-part ordering rejects lexical-order mistakes, covers the 0.13 minor line, and treats missing parts as zero. [1]
- The gate accepts a newer PATH uv and prints its exact version/path/minimum. [2]
- A failed sync names both observed and minimum uv versions and restores both directory and symlink predecessors from reserved backup paths. [4]
- The sync-failure case runs via `run_driver` with fake uv/runtime shims, restores directory or symlink predecessors, and retains the failed candidate under venv-backups. [5]

- Unreadable and failed version outputs retain their diagnostic token rather than inventing empty text. [3]
