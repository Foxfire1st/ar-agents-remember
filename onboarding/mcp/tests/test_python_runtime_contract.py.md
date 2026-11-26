# mcp/tests/test_python_runtime_contract.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Unit tests verifying `scripts/check-python-runtime.py`, GitHub workflow uv minor-line configuration, and Dagger uv minor-line image/digest helpers under the uv-managed Python 3.14 contract.

## Code Commentary

### Logic

Eight test functions cover the runtime checker, CI workflows, and Dagger helper contracts using controlled subprocess shims and repository file inspection:

- `test_unsupported_minor_is_named_before_importing_new_stdlib_modules` runs the checker under a simulated 3.13.15 interpreter whose `compression` import fails, asserting exit 1, empty stdout, and the named refusal stating expected minor, observed version, and executable.
- `test_builtin_readline_is_reported` removes `readline.__file__` and asserts the checker reports `"built-in"` without crashing.
- `test_different_patch_of_the_managed_minor_is_accepted` verifies another patch release of the contract minor under uv's minor symlink is accepted.
- `test_patch_directory_is_refused_even_when_it_is_the_link_target` verifies an environment bound directly to a patch directory instead of uv's minor symlink is refused.
- `test_minor_link_outside_uv_directory_is_refused` verifies a minor symlink outside `UV_PYTHON_INSTALL_DIR` / `uv_python_directory()` is refused.
- `test_uv_version_and_image_digest_are_recorded_in_provenance` verifies `--uv-version` and `--uv-image-digest` are emitted in `provenance` and folded into `buildFingerprint`.
- `test_workflows_install_uv_minor_line_and_record_resolved_version` checks `.github/workflows/quality-checks.yml` and `.github/workflows/publish-mcp-to-pypi.yml` install `astral-sh/setup-uv` at `${AR_UV_VERSION}.x` and record resolved uv version.
- `test_dagger_uv_minor_and_image_digest_helpers` checks `.dagger/src/agents_remember_quality/main.py` constructs `ghcr.io/astral-sh/uv:<AR_UV_VERSION>` and extracts its resolved `sha256` digest.

### Conventions

Tests run in isolation with simulated interpreter attributes and temporary uv directories; they do not execute `uv`, Docker, or Dagger.

- Helper fixtures construct synthetic `UV_PYTHON_INSTALL_DIR` layouts with `cpython-3.14-linux-x86_64-gnu` minor symlinks pointing at patch-directory targets, so minor-link validation is exercised without host network downloads or real `uv` invocations.
- Subprocess harnesses inject temporary `sitecustomize` / shim modules to simulate unsupported minor versions (`3.13.15` with failing `compression` imports) and built-in `readline` modules lacking `__file__`.
- Workflow and Dagger tests parse tracked `.github/workflows/quality-checks.yml`, `.github/workflows/publish-mcp-to-pypi.yml`, and `.dagger/src/agents_remember_quality/main.py` directly against `scripts/python-runtime-contract.env` (`AR_PYTHON_MINOR=3.14`, `AR_UV_VERSION=0.13`).

### Invariants And Boundaries

Preserve exact refusal, minor-link, provenance, workflow, and Dagger helper assertions:

- Wrong-minor refusal must report expected minor, observed version, and executable path before importing any Python 3.14-only standard-library module.
- `pyvenv.cfg` home validation must reject both direct patch directories and minor symlinks outside `uv_python_directory()` without spawning `uv`.
- Provenance output must record observed `uvVersion`, `pythonBuild`, and optional `uvImageDigest` and fold them into `buildFingerprint`.
- This source inspection does not claim a newly executed test or acceptance result.

### Todos

None recorded.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test fixtures and assertions, so the exact source is the direct evidence.

### Repo-Internal References

- The negative admission witness proves the named minor refusal precedes any newer standard-library import. [3]
- Built-in `readline`, alternate patches, patch-directory refusal, outside-uv-directory refusal, and provenance recording are verified against `scripts/check-python-runtime.py`. [4]
- Workflow minor-line uv setup and Dagger minor-line image/digest helpers are verified against the tracked workflow and Dagger files. [5]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.
