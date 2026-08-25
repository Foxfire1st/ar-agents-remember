# mcp/src/agents_remember/testing/causal_failures.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/causal_failures.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns the pytest-side causal-failure artifact, graph-proven blocked-node handling, and exact
reproduction metadata for independent/process-sensitive failures.

## Code Commentary

### Logic

Collection loads the owner-preflight artifact and skips only tests whose file has a declared/import
edge to the failed owner. Every item receives a failure class and retry semantics. Session finish
adds blocked nodes and independent failures to the same JSON and Markdown payload.

### Conventions

Process sensitivity is derived from owned imports (async, socket, process, threading), not guessed
from exception text. Workers report observations; the controller alone publishes the artifact.

### Invariants And Boundaries

- Incomplete ownership causes no blanket suppression.
- Independent failures execute and remain separately visible.
- Seed, worker, duration, start/finish time, and process families survive reporting.
- The artifact is always non-accepting; a causal skip cannot mint evidence.

### Todos

None.

## Docs References

No external domain documentation defines this repository diagnostic format.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Collection blocks only exact file edges and records retry metadata. | `pytest_collection_modifyitems` | mcp/src/agents_remember/testing/causal_failures.py:71-112 |
| Runtime failures and final artifacts preserve independent evidence. | `runtime_failure_record` | mcp/src/agents_remember/testing/causal_failures.py:114-226 |
| Focused proof covers incomplete ownership and process-sensitive reproduction. | `test_incomplete_ownership_never_becomes_blanket_suppression` | mcp/tests/test_causal_failure_localization.py:127-196 |

## Cross-Repo References

No adjacent repository owns this failure record.

## Update History

- 2026-08-25T01:56+02:00 — Created for causal failure localization without hiding independent
  evidence.
