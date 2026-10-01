# mcp/src/agents_remember/providers/setup_reporting.py

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

## Evidence

### Docs References

No external documentation is needed for this local setup reporting module.

No relevant external documentation is needed for this provider setup summary behavior.

### Repo-Internal References

- Setup finalization computes strict `ok`, recovered `ready`, setup state, failed phases, final status, result counts, and summary output. [1]
- Setup state keeps `ready-with-failed-phases` distinct from `ok`, failed, and failed-unchecked states. [2]
- Setup summary files are written under `logs/providers/setup/` as `last-<action>.json`, a timestamped snapshot, and `last-<action>-full.json` (full untrimmed payload), with dry-runs returning paths but writing nothing. [3]
- Summary payloads omit nested settings internals and include action, readiness, enabled providers, result counts, failed phases, final status, and compacted results. [4]

| Provider setup delegates final payload augmentation and summary persistence to this module. | `finalize_setup_payload` | mcp/src/agents_remember/providers/provider_setup.py:584-584 |

### Cross-Repo References

No sibling repository boundary is needed to explain this file.

No meaningful cross-repo references found.
