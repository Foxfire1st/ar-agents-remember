# mcp/src/agents_remember/drift/onboarding_drift.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/drift/onboarding_drift.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T22:37+02:00                     |
| lastVerifiedCommitHash | `3417d47f1e76d37e9ba6e803c7b28afa4758da9c` |
| lastVerifiedCommitDate | 2026-05-23T23:06:47+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`onboarding_drift.py` is the package-local C-02 drift classifier. It compares
sidecar, overview, inline, and entity-catalog onboarding against the current
source tree and writes temporary drift reports for workflow decisions.

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

### Todos

- The file still has several Radon `C` functions and should be included in the
  Phase 06 package-level analysis.

## Docs References

No external documentation is needed to prove this repository-local drift
classifier.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for the file's local classifier behavior. | n/a | n/a |

## Repo-Internal References

Same-repository source is the direct evidence for the drift classifications and
report routing.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module imports resolver storage/path helpers, defines drift classification constants, and uses `DriftRow` as the shared result shape. | L20-L29; L38-L48; L65-L76 | [onboarding_drift.py](agents-remember-md/mcp/src/agents_remember/drift/onboarding_drift.py) |
| Sidecar, overview, entity-catalog, inline, and source classifiers are separate functions that feed one drift result stream. | L210-L314; L335-L440; L467-L799; L851-L1065 | [onboarding_drift.py](agents-remember-md/mcp/src/agents_remember/drift/onboarding_drift.py) |
| Report path resolution keeps explicit durable-memory report paths out of the memory repo and under coordination temp instead. | L1115-L1195 | [onboarding_drift.py](agents-remember-md/mcp/src/agents_remember/drift/onboarding_drift.py) |

## Cross-Repo References

No meaningful cross-repo boundary is documented here; MCP/controller callers are
same-repository code.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling repository boundary is needed to explain this file. | n/a | n/a |

## Update History

- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
