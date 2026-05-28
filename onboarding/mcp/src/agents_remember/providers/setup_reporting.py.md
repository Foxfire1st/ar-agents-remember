# mcp/src/agents_remember/providers/setup_reporting.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/setup_reporting.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T12:32+02:00                     |
| lastVerifiedCommitHash | `3f09b75461760479b443f1b04b180772724e7a24` |
| lastVerifiedCommitDate | 2026-05-28T15:10:01+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`setup_reporting.py` turns provider setup command results into compact,
diagnosable historical setup summaries under `logs/providers/setup/`.

## Code Commentary

### Logic

`finalize_setup_payload()` is called by provider setup after lifecycle phases
finish. It keeps top-level `ok` strict over the phase results, derives a
separate `ready` value from the final watcher status when available, records a
human-readable setup `state`, stores compact failed phases, stores the final
watcher status, counts results, and writes a setup summary.

`write_setup_summary()` writes both `last-<action>.json` and a timestamped
snapshot unless the request is a dry run. `compact_result()` keeps only
diagnostic summary keys, recursively compacts nested payloads/results, and
truncates long strings so setup logs do not balloon with raw stdout.

### Invariants And Boundaries

- Setup summaries describe what happened during the last setup action; they
  are not the source of current provider truth.
- A failed phase remains visible even when a final watcher status later reports
  ready.
- The MCP current-state path is owned by `current_state.py`, not this module.
- Dry runs must report intended summary paths without writing files.
- Compact summaries should preserve diagnosis fields while omitting large raw
  output.

### Todos

None.

## Docs References

No external documentation is needed for this local setup reporting module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for this provider setup summary behavior. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Setup finalization computes strict `ok`, recovered `ready`, setup state, failed phases, final status, result counts, and summary output. | L45-L66 | [setup_reporting.py](agents-remember-md/mcp/src/agents_remember/providers/setup_reporting.py) |
| Setup state keeps `ready-with-failed-phases` distinct from `ok`, failed, and failed-unchecked states. | L69-L77 | [setup_reporting.py](agents-remember-md/mcp/src/agents_remember/providers/setup_reporting.py) |
| Setup summary files are written under `logs/providers/setup/` as a `last-<action>.json` file plus a timestamped snapshot, with dry-runs returning paths but writing nothing. | L117-L154 | [setup_reporting.py](agents-remember-md/mcp/src/agents_remember/providers/setup_reporting.py) |
| Summary payloads omit nested settings internals and include action, readiness, enabled providers, result counts, failed phases, final status, and compacted results. | L157-L183 | [setup_reporting.py](agents-remember-md/mcp/src/agents_remember/providers/setup_reporting.py) |
| Tests assert dry-run no-write behavior, compact summary files, recovered final status reporting, and omission of raw stdout. | L51-L192 | [test_provider_setup.py](agents-remember-md/mcp/tests/test_provider_setup.py) |
| Provider setup delegates final payload augmentation and summary persistence to this module. | L1-L66 | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |

## Cross-Repo References

No sibling repository boundary is needed to explain this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-28T12:32+02:00: Created after provider setup gained compact setup summaries and separate historical setup state.
