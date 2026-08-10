# mcp/src/agents_remember/models/terminal_catalog.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/models/terminal_catalog.py`         |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-08T14:38+02:00                                      |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                  |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[models overview](overview.md)

## Purpose

`models/terminal_catalog.py` owns the terminal-catalog row vocabulary that 260731-EFA-L9 moved
out of `serving/terminal_catalog.py` (R8: the conversation tree's nine `terminal_catalog` imports
had to go): `TerminalCatalogEntry` and its literals, the migration-safe JSON parsing/serialization
helpers, the liveness-hysteresis copiers, seat-role migration, and the liveness configuration.
The durable store itself (`TerminalCatalog`, locking, compaction) stays in
`serving/terminal_catalog.py`.

## Code Commentary

### Logic

`TerminalCatalogEntry` (cit:(["class TerminalCatalogEntry"], mcp/src/agents_remember/models/terminal_catalog.py:68-68)) is the immutable row model: browser-visible session id
and label, launch kind, harness/lifecycle ids, cwd, tmux session, command argv, status
(`running`/`exited`/`landed`/`terminated`), the durable leaf-identity key, spawned-by provenance
(`spawned_by_session`/`spawned_by_lifecycle`/`spawn_role` plus the free-form launch provenance),
liveness probe state, control metadata, and the multiplexed pending-interactions column.
`from_json`/`to_json` translate between Python snake_case and the dashboard API's camelCase with
`None`-filtered optional fields, so legacy rows read back as `None` without a schema bump.

The pure parsers are shared with the conversation tree and stay dependency-light: `_optional_str`,
`_optional_path`, `_optional_list`, `_optional_object`, `_optional_object_list`,
`_optional_non_negative_int`, `_present_fields`, `_liveness_evidence`, `_turn_state`,
`_control_state`, `_control_activity`, `_control_acceptance`, and `_status`
(cit:(["def _optional_object_list("], mcp/src/agents_remember/models/terminal_catalog.py:593-600)). The read helpers fail closed on shape: a malformed
multiplexed pending-interaction list degrades the whole field to `None` rather than persisting a
partial set.

The liveness copiers own the hysteresis math: `with_liveness_success` self-heals a false `exited`
mark, `with_liveness_failure` records evidence-dependent thresholds
(`pane-gone` marks fast with a zero window; `tmux-command-failed` needs the full threshold across
the minimum window), and a `terminated` row is never revived. `migrated_seat_role` remains the
sole authority for deriving legacy `seatRole` from persisted role, `spawn_role`, and terminal
kind (cit:(["def migrated_seat_role("], mcp/src/agents_remember/models/terminal_catalog.py:688-694)).
`DEFAULT_LIVENESS_HYSTERESIS` (cit:(["DEFAULT_LIVENESS_HYSTERESIS = TerminalCatalogLivenessConfig()"], mcp/src/agents_remember/models/terminal_catalog.py:723-723)) carries the sweep
configuration defaults.

### Conventions

- Models-only module: no file I/O, locking, or store behavior here; the store imports the row
  vocabulary from this module.
- Optional JSON fields stay migration-safe (`None` means absent on legacy rows); filtering is
  strictly on `None`, so empty tuples/strings remain present.

### Invariants And Boundaries

- `seatRole` remains required on the wire; `spawn_role` is immutable origin provenance;
  `livenessFailures` is truth-gated; `exitEvidence` is exited-only.
- The old `serving/terminal_catalog.py` row definitions are gone; no forwarding shim exists, and
  conversation modules must import the vocabulary from here (layering rail enforced).

### Todos

No known follow-up in this file.

## Docs References

No external/domain documentation is configured; this is an internal wire/row contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The store consumes the row vocabulary and liveness config from this module. | `TerminalCatalogEntry` | mcp/src/agents_remember/models/terminal_catalog.py:44-474 |
| The baseline test pins the moved catalog-row helpers and serialization samples. | `test_serialization_samples_match_baseline` | mcp/tests/test_model_split_baseline.py:211-211 |

## Cross-Repo References

No cross-repository implementation governs this contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the row-vocabulary move from
  `serving/terminal_catalog.py`; preserved the entry/liveness/parsing knowledge from the old
  serving card and left store behavior to the serving card. Verification metadata pinned until
  closeout stamps the L9 code commit.
