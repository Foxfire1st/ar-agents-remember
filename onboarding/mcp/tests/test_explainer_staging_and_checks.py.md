# mcp/tests/test_explainer_staging_and_checks.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Regression suite covering explainer publish-staging path confinement, task-lock serialization between draft staging and staging pruning, stray-file replacement during starter and exemplar seeding, publish refusal on missing kit licence notices, and Chromium runtime enforcement of media-control rules on script-inserted audio and video elements.

## Code Commentary

Five behavioral tests exercise both direct module helpers and the registered `render` tool surface. Symlink confinement cases link `state/publish-staging`, `state/`, reused draft working paths, and discard targets to outside directories with marker files and assert `PathRefused` directly and `publication.refusal == "path-held"` through the tool without outside deletion. Lock-serialization cases coordinate prune and render threads with events under `HANG_GUARD_SECONDS` and a lock-contention probe (`_observe_contending_lock` using `try_file_lease`), verify task-lock exclusion with no in-flight staging loss or deadlock, and run two identical concurrent renders behind a start barrier asserting clean `published` and `unchanged` outcomes. Package-copy tests replace stray regular files at `starters` and `exemplar` while preserving symlink refusal. Kit-licence tests remove `shiki/4.5.0/LICENSE` from a temporary `KIT_ROOT` while keeping the verified shipped CSS in the draft and assert `kit-problem` refusal with `kit-file-absent`. Browser media tests run real Chromium via `configure_browser_env` to reject script-appended autoplay, loop, and controls-less media while publishing conforming script-inserted media.

## Relationships

Registered in the `unit-regression` lane of `mcp/tests/test-evidence-lanes.toml` and as an artifact consumer in `mcp/tests/evidence-lifecycle.toml`. Uses `canvas_browser_test_support`, `canvas_host_test_support`, and `explainer_server_test_support` to exercise `explainer_staging.py`, `explainer_server.py`, `explainer_workspace.py`, `prospective.py`, and `canvas-prospective-load.mjs`.

## Evidence

- Symlinked staging or state directories, escaped reused paths, and outside discard targets raise `PathRefused` directly and surface as `path-held` publish refusals without deleting outside marker files. [1]
- Draft staging, pruning, and identical concurrent renders serialize under the re-entrant task lock without deleting in-flight staging, deadlocking, or failing on concurrent identical renders. [2]
- `_copy_package_folder` unlinks stray regular files at `starters` and `exemplar` before copying while continuing to refuse symlinks. [3]
- A missing shipped kit licence notice refuses publish with `kit-problem` and `kit-file-absent` even when the draft carries the verified shipped kit asset. [4]
- Real Chromium prospective loading refuses script-inserted autoplay, loop, and controls-less media elements while publishing conforming script-inserted media. [5]
