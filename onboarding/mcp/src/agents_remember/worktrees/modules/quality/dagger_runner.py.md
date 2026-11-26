# mcp/src/agents_remember/worktrees/modules/quality/dagger_runner.py

## Governing Overview

[worktrees/modules overview](../overview.md)

## Purpose

Owns the Dagger child-process environment projection for admitted shared-engine runs: normalizing Docker client paths before directory changes, refusing conflicting ambient host variables, omitting overriding session/cloud selectors by name, and binding `_EXPERIMENTAL_DAGGER_RUNNER_HOST` and `AR_DAGGER_RUNTIME_AUTHORITY_DIGEST`.

## Code Commentary

Defines `DAGGER_HOST_ENV = "DAGGER_HOST"`, `DAGGER_RUNNER_HOST_ENV = "_EXPERIMENTAL_DAGGER_RUNNER_HOST"`, `RUNTIME_AUTHORITY_DIGEST_ENV = "AR_DAGGER_RUNTIME_AUTHORITY_DIGEST"`, and `_OVERRIDING_SELECTORS = ("DAGGER_CLOUD_ENGINE", "DAGGER_SESSION_PORT", "DAGGER_SESSION_TOKEN")`.

`native_dagger_environment(base)` starts from `native_path_environment(base)` and absolutizes every `PATH` entry plus `HOME` and `DOCKER_CONFIG` so `docker` inspection and Dagger child launches resolve the same client and configuration even after changing working directory.

`dropped_dagger_selectors(base)` returns the tuple of overriding selector keys present in `base` (names only, never values) so callers can record them in receipts, outcomes, and reports.

`authority_environment(snapshot, base)` refuses any non-blank ambient `DAGGER_HOST` or any ambient `_EXPERIMENTAL_DAGGER_RUNNER_HOST` that differs from `snapshot.endpoint` via `_refuse_host_conflict` (`DaggerRuntimeAuthorityError` with code `runtime-authority-ambient-conflict`). On admission it removes `DAGGER_HOST` and every present overriding selector, then sets `_EXPERIMENTAL_DAGGER_RUNNER_HOST = snapshot.endpoint` and `AR_DAGGER_RUNTIME_AUTHORITY_DIGEST = snapshot.snapshot_digest`.

## Relationships

Re-exported by `dagger_authority.py` and consumed by `clean_executor.py`, `diagnostic_executor.py`, and `final_codex_executor.py`. Verified by `mcp/tests/test_dagger_runtime_authority.py` and `mcp/tests/test_clean_quality_executor.py`.

## Evidence

- `native_dagger_environment` absolutizes `PATH`, `HOME`, and `DOCKER_CONFIG` before inspection and child launch. [1]
- `dropped_dagger_selectors` reports present overriding Dagger session/cloud selector key names without exposing values. [2]
- `authority_environment` refuses conflicting ambient host keys, removes `DAGGER_HOST` and overriding selectors, and binds `_EXPERIMENTAL_DAGGER_RUNNER_HOST` and the authority digest. [3]
- `_refuse_host_conflict` raises `DaggerRuntimeAuthorityError` with code `runtime-authority-ambient-conflict`. [4]
