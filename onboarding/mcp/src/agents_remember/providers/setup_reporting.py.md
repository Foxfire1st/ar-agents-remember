# mcp/src/agents_remember/providers/setup_reporting.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/setup_reporting.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed for this provider setup summary behavior. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Setup finalization computes strict `ok`, recovered `ready`, setup state, failed phases, final status, result counts, and summary output. | `finalize_setup_payload` | mcp/src/agents_remember/providers/setup_reporting.py:45-66 |
| Setup state keeps `ready-with-failed-phases` distinct from `ok`, failed, and failed-unchecked states. | `ok` | mcp/src/agents_remember/providers/setup_reporting.py:69-77 |
| Setup summary files are written under `logs/providers/setup/` as `last-<action>.json`, a timestamped snapshot, and `last-<action>-full.json` (full untrimmed payload), with dry-runs returning paths but writing nothing. | `write_setup_summary` | mcp/src/agents_remember/providers/setup_reporting.py:117-151 |
| Summary payloads omit nested settings internals and include action, readiness, enabled providers, result counts, failed phases, final status, and compacted results. | `compact_result` | mcp/src/agents_remember/providers/setup_reporting.py:100-114 |
| Tests assert dry-run no-write behavior, compact summary files, recovered final status reporting, and omission of raw stdout. | `ProviderSetupTests` | mcp/tests/test_provider_setup.py:25-899 |
| Provider setup delegates final payload augmentation and summary persistence to this module. | `finalize_setup_payload` | mcp/src/agents_remember/providers/provider_setup.py:584-584 |

## Cross-Repo References

No sibling repository boundary is needed to explain this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 5 repository-internal citations for finalization, summary writing/compaction, provider-setup tests, and delegation.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The
  delegation row pointed at `provider_setup.py` L1-L66 (imports and the `ProviderSetupRequest`
  dataclass); the single call is `setup_reporting.finalize_setup_payload(...)` inside
  `_action_payload_from_args` at L562-L588, reached via the module import at L24. Verified by grep
  that L584 is the only `setup_reporting.` call site in that file. No claim text changed.

- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/src/agents_remember/providers/setup_reporting.py` and moved the lines this card cites, so
  the Citations column no longer pointed at the code its rows name. Corrected the ranges
  (L157-L183 → L157-L179). The behaviour described is unchanged — the file's AST is identical to
  the base revision — this is a citation repair only. Verification metadata pinned until closeout
  stamps the L2 commit.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-01T23:40+02:00 — `write_setup_summary` now writes a third artifact, `last-<action>-full.json`, with the full untrimmed provider-setup payload (command stdout/stderr included, `default=str`). `setup_summary_paths` gained a `lastFull` key; all return dicts (success, error, dry-run) report `lastFull`. The compact summary and trimmed tool response were not usable debug artifacts when a provider step failed. Updated Logic, Invariants, and the summary-files Repo-Internal References row.
- 2026-05-28T12:32+02:00: Created after provider setup gained compact setup summaries and separate historical setup state.
