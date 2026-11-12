# mcp/test_support/agents_remember_test_support/code_quality/file_size.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Enforce the repository's File Size Budget standard: every file at or above the 1,200-line hard limit is a finding carrying the band it violates (hard-limit-exceeded, architectural-failure at 2,000+, emergency-cleanup at 4,000+; under-limit is the healthy case). Counting matches `wc -l` (newline characters). The module runs enforced by default (non-zero exit on any finding) and in `--report` mode (same output, exit 0) so the wrapper can keep the check wired and visible while the tree is unarmed.

## Code Commentary

- `line_count(path)` — `wc -l`-compatible counting.
- `band_for(line_count)` — the standard's band label for a file.
- `measure(paths)` — every measured file at or above the hard limit, sorted by path; raises `OSError` on an unreadable file.
- `render(finding)` / `scope_line(paths)` — the band-naming output lines.
- `build_parser()` / `main(argv)` — CLI with `--project-root` and `--report`; no paths supplied refuses to certify an empty measurement (fail-closed).
- The wrapper wires this as the enforcing `file-size` step; the arming boolean `file_size_armed` in `pyproject.toml` is read through `code_quality/scope.py`, and `scope.size_paths` = index-known Python plus `dashboard/src` TypeScript/TSX.
- Since 260731-EFA-L7 (FIX-3) the rail is armed: `band_for(1199)` → `under-limit`, `band_for(1200)` → `hard-limit-exceeded`, `band_for(2000)` → `architectural-failure`, `band_for(4000)` → `emergency-cleanup` are pinned by `mcp/tests/test_file_size_detector.py`.

## Invariants And Boundaries

- The detector is read-only and fail-closed: an empty measurement is refused, an unreadable file exits 1, and the arming key is type-checked before the run.
- The card mirrors the source file one-to-one at `mcp/test_support/agents_remember_test_support/code_quality/file_size.py`.

## Evidence

### Repo-Internal References

- The project-owned wrapper's file-size rail selects enforcing or report-only behavior from explicit configuration. [1]
- The arming boolean and measured scope. [2]
- The band-boundary and wiring suite. [3]
