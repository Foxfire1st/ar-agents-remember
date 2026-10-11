# mcp/tests/test_bootstrap_uv_minimum_version.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Protect the host bootstrap's numeric uv floor, PATH selection, diagnostics and pre-mutation refusal without procuring uv.

## Code Commentary

The module sources the guarded bootstrap for comparator/gate probes and invokes the actual main path for refusals. Fake PATH executables report equal/newer/older or unreadable versions; decimal comparisons include missing parts, major changes and leading zeroes. Accepting a shim proves gate selection and its log, not a real successful environment build. Missing/older/unreadable output is checked against the actual diagnostics; nonzero version-command output is not relabelled empty.

Each executable test uses temporary XDG data/cache/config roots. The existing-environment refusal case can check a marker when a venv is present. The sync-failure case requires an existing venv and a checker-valid canonical runtime, uses a failing sync shim, and checks predecessor restoration and backup removal; it skips if no checker-valid runtime is available. Runtime lookup probes candidates read-only and builds none. The no-uv-fetch case checks absence of curl, wget and an uv== pin in the script; its textual guard is narrower than a whole-program effects proof. Real successful-build/package-equivalence evidence belongs to the separate producer run receipts.

## Evidence

- Decimal-part ordering rejects lexical-order mistakes and treats missing parts as zero. [1]
- The gate accepts a newer PATH uv and prints its exact version/path/minimum. [2]
- Unreadable and failed version outputs retain their diagnostic token rather than inventing empty text. [3]
- A failed sync names both versions and restores an existing environment when the checker-valid runtime prerequisite is met. [4]
