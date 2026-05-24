# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T02:47+02:00                     |
| lastVerifiedCommitHash | `b25d52f2b445554bb64115db2f27fd156954bcf3` |
| lastVerifiedCommitDate | 2026-05-24T02:36:33+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`drift.py` is the package-local C-02 drift classifier. It compares sidecar,
overview, inline, and entity-catalog onboarding against the current source tree
and writes temporary drift reports for workflow decisions.

## Code Commentary

### Logic

The module defines `DriftRow` as the common result record, discovers sidecar and
inline onboarding, classifies source and onboarding pairs, validates overview
metadata, recomputes entity-catalog `git-blob-set-v1` fingerprints, and renders
text, JSON, CSV, and Markdown report outputs. `main()` is the CLI/dev facade;
MCP tools call package-level summary/controller code that reuses these
classifiers.

### Conventions

Report paths are resolved back to the coordination temp area when callers point
at durable memory. Git subprocesses use `stdin=subprocess.DEVNULL` so they
cannot consume MCP stdio transport input.

### Invariants And Boundaries

- C-02 detects and reports drift; it must not rewrite onboarding.
- Durable memory repo paths are not valid locations for temporary drift reports.
- Entity fingerprints are deterministic Git blob-set hashes over curated
  evidence paths.
- The module now lives under `memory_quality.integrity` rather than a top-level
  `drift` package.

### Todos

- The file still has several Radon `C` functions and should be included in the
  Phase 06 package-level analysis.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Summary generation imports this module and delegates row classification to it. | [summary.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |
| Memory quality wraps this classifier through the drift summary check. | [check.py](agents-remember-md/mcp/src/agents_remember/memory_quality/check.py) |

## Update History

- 2026-05-24T02:47+02:00: Moved from the top-level `drift` package into `memory_quality.integrity.onboarding_drift_check`.
- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
