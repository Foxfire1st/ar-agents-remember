# mcp/src/agents_remember/providers/setup_reporting.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/setup_reporting.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T23:40+02:00                     |
| lastVerifiedCommitHash | `8833b31a37deda0d9d2e6895659ab0fe085a8ee9` |
| lastVerifiedCommitDate | 2026-06-01T23:39:39+02:00|
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

`write_setup_summary()` writes three artifacts: `last-<action>.json` and a timestamped snapshot (both using the compact `summary`), and now also `last-<action>-full.json` holding the full, untrimmed provider-setup payload (command stdout/stderr included, serialized with `default=str` to keep `Path` and other non-JSON values). `setup_summary_paths` gained a `lastFull` key; all return dicts (success, error, and dry-run) report `lastFull`. The compact summary's `SUMMARY_KEYS` filter drops command output, and the tool response is trimmed for model context, so neither was a usable debug artifact when a provider step failed. `compact_result()` keeps only diagnostic summary keys, recursively compacts nested payloads/results, and truncates long strings so setup logs do not balloon with raw stdout.

### Invariants And Boundaries

- Setup summaries describe what happened during the last setup action; they
  are not the source of current provider truth.
- A failed phase remains visible even when a final watcher status later reports
  ready.
- The MCP current-state path is owned by `current_state.py`, not this module.
- Dry runs must report intended summary paths without writing files.
- Compact summaries should preserve diagnosis fields while omitting large raw
  output.
- The full artifact (`last-<action>-full.json`) is the authoritative debug copy; it is never trimmed and uses `default=str` serialization.

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
| Setup finalization computes strict `ok`, recovered `ready`, setup state, failed phases, final status, result counts, and summary output. | L45-L66 | [setup_reporting.py](agents-remember/mcp/src/agents_remember/providers/setup_reporting.py) |
| Setup state keeps `ready-with-failed-phases` distinct from `ok`, failed, and failed-unchecked states. | L69-L77 | [setup_reporting.py](agents-remember/mcp/src/agents_remember/providers/setup_reporting.py) |
| Setup summary files are written under `logs/providers/setup/` as `last-<action>.json`, a timestamped snapshot, and `last-<action>-full.json` (full untrimmed payload), with dry-runs returning paths but writing nothing. | L117-L154 | [setup_reporting.py](agents-remember/mcp/src/agents_remember/providers/setup_reporting.py) |
| Summary payloads omit nested settings internals and include action, readiness, enabled providers, result counts, failed phases, final status, and compacted results. | L157-L183 | [setup_reporting.py](agents-remember/mcp/src/agents_remember/providers/setup_reporting.py) |
| Tests assert dry-run no-write behavior, compact summary files, recovered final status reporting, and omission of raw stdout. | L51-L192 | [test_provider_setup.py](agents-remember/mcp/tests/test_provider_setup.py) |
| Provider setup delegates final payload augmentation and summary persistence to this module. | L1-L66 | [provider_setup.py](agents-remember/mcp/src/agents_remember/providers/provider_setup.py) |

## Cross-Repo References

No sibling repository boundary is needed to explain this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-01T23:40+02:00 — `write_setup_summary` now writes a third artifact, `last-<action>-full.json`, with the full untrimmed provider-setup payload (command stdout/stderr included, `default=str`). `setup_summary_paths` gained a `lastFull` key; all return dicts (success, error, dry-run) report `lastFull`. The compact summary and trimmed tool response were not usable debug artifacts when a provider step failed. Updated Logic, Invariants, and the summary-files Repo-Internal References row.
- 2026-05-28T12:32+02:00: Created after provider setup gained compact setup summaries and separate historical setup state.
