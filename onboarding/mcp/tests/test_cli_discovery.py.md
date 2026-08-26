# test_cli_discovery.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_cli_discovery.py`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-03T09:55+02:00                           |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`       |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Unit tests for `cli/discovery.py` (260703 L1): the upward walk that makes `--config` optional
for the umbrella CLI.

## Code Commentary

`DiscoverConfigTests` builds throwaway directory trees per test (`tempfile.TemporaryDirectory`)
with two helpers: `_settings(path, coordination_root)` writes a **usable** settings JSON (it
creates the `coordinationRoot` directory, because usability requires an existing absolute dir)
and `_mcp_json(directory, config_path)` writes an `.mcp.json` with an `agents-remember` server
entry carrying `--config <path>` args (or none).

Covered behaviors, one test each:

- convention hit (`.claude/mcp/agents-remember-settings.json` found from a deep start dir);
- `.mcp.json` registration hit (recorded `--config` path reused);
- same-directory precedence (convention beats registration);
- nearest-directory-wins across levels (a lower `.mcp.json` beats a higher convention file);
- tolerance sweep in one walk: malformed `.mcp.json`, an entry without `--config`, and a
  foreign-server-only file are all skipped without error;
- a registration pointing at a **missing** file is skipped (usability, not existence of the
  registration, decides);
- the placeholder-template skip: a repo-shaped tree ships the tracked convention template with a
  `<PATH/TO/YOUR/...>` `coordinationRoot`; starting inside it must walk past to the real
  settings above — the regression test for the semantic `_is_usable_settings` probe;
- the miss error names both probed patterns and the resolved origin.

## Invariants And Boundaries

- Tests never touch the real workspace: every tree is a tmp dir, and usable settings always point
  `coordinationRoot` at a directory created inside that tmp tree.
- The template-skip test encodes the repo-checkout reality; if the shipped template's shape
  changes (e.g. placeholders become resolvable paths), this test is the tripwire.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test. | `discover_config` | mcp/src/agents_remember/cli/discovery.py:36-50 |
| The CLI wiring that consumes discovery. | `_resolve_settings` | mcp/src/agents_remember/cli/dashboard.py:212-221 |

## Update History
- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 2 repository-reference citations (2/2 anchored and sourced; scoped citation check clean).

- 2026-07-03T09:55+02:00 — Created for 260703 L1 alongside `cli/discovery.py` (8 tests: hits,
  precedence, nearest-wins, tolerance, template skip, miss error). Verification metadata pinned
  until closeout stamps the code commit.
