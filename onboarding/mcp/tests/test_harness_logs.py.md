# test_harness_logs.py

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_harness_logs.py`        |
| doc_type               | `file-level-onboarding`                 |
| lastUpdated            | 2026-07-10T13:03+02:00                  |
| lastVerifiedCommitHash |                                         `e400ed0ce98752d1b65d00de97c9b84c7ea20814`|
| lastVerifiedCommitDate |                                         2026-07-10T20:04:45+02:00|
| governingOverview      | `../overview.md`                        |

## Governing Overview

[mcp overview](../overview.md)

## Purpose

Pins `HarnessSessionLog` against production-shaped Claude and Codex JSONL records rather than
hand-written pane grammars.

## Code Commentary

### Logic

Temporary Claude fixtures prove cwd-keyed log binding, exclusion-safe id-bearing user messages,
successful `/effort ultracode` command+stdout evidence, and errored command rejection. Codex
fixtures prove date-partitioned message binding only for the matching cwd. A partial final JSONL
append is ignored until completed, while the same log then becomes acceptable when a complete user
record is written.

### Conventions

Fixtures serialize real event keys and content-block shapes with newline-delimited JSON; filesystem
roots and timestamps are injected so no user session history is read.

### Invariants And Boundaries

- Tests use real record schema and cwd boundaries, not terminal-screen vocabulary.
- Command presence alone is insufficient; success requires non-error stdout.
- A different cwd cannot bind merely because the id text matches.

### Todos

Add real-key fixtures when reviewer residual N1's Claude `.`/`_` sanitization is implemented, and
Codex command fixtures only if the product first gains a supported command-evidence contract.

## Docs References

No Domain Documentation entries are configured; these are repository-local parser regressions.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests encode the local Claude/Codex record contracts used by L15. | L15-L122 | [test_harness_logs.py](test_harness_logs.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `HarnessSessionLog` implements the discovery, cwd validation, message extraction, and command evidence under test. | L36-L225 | [../src/agents_remember/serving/harness_logs.py](../src/agents_remember/serving/harness_logs.py.md) |
| Injector tests exercise the parser through the public delivery outcome rather than only at parser unit level. | L5-L166 | [test_injector.py](test_injector.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The fixtures and parser are local to this repository. | — | — |

## Update History

- 2026-07-10T13:03+02:00 — Created for 260707-HFX2-L15 with real-shape Claude/Codex binding,
  command success/error, cwd isolation, and partial-final-append regressions. Verification metadata
  is blank until closeout stamps the eventual L15 code commit.
