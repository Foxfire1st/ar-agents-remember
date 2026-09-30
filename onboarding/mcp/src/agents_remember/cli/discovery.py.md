# mcp/src/agents_remember/cli/discovery.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/cli/discovery.py`   |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated | 2026-09-30T12:15:39+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`   |
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview      | `../../../../overview.md`                     |

## Governing Overview

[overview.md](../../../../overview.md)

## Purpose

`cli/discovery.py` makes `--config` optional for the umbrella CLI: when the flag is omitted,
`discover_config()` finds the trusted MCP settings JSON by walking upward from the current
directory, so `agents-remember dashboard` runs flag-free from anywhere under the workspace.
It exists so the CLI and the harness always boot from the same settings file without the user
retyping an absolute path (260703 L1).

## Code Commentary

`discover_config(start=None)` resolves the origin (default `Path.cwd()`) and walks
`(origin, *origin.parents)`. At each level it probes, in order:

1. the settings convention `SETTINGS_CONVENTION` = `.claude/mcp/agents-remember-settings.json`,
2. an `.mcp.json` (`MCP_REGISTRATION`) whose `mcpServers`/`agents-remember` entry records a
   `--config` argument — `_config_from_mcp_registration` extracts the value following the first
   `--config` token in the entry's `args` list, reusing the harness's own registration verbatim.

The nearest directory wins and the first USABLE candidate ends the walk. Usability is the
semantic probe `_is_usable_settings`: the file must parse as a JSON object whose
`coordinationRoot` is a non-empty string naming an **existing absolute directory**. A miss raises
`ConfigDiscoveryError` with one message naming both probed patterns and the walk origin.

`_config_from_mcp_registration` is total over hostile input: missing file, unreadable bytes,
malformed JSON, non-dict shapes, foreign server entries, or a `--config` flag without a value all
return `None` (the walk continues) — discovery must never crash on someone else's `.mcp.json`.
Since 260731-EFA-L2 it is one line —
`_nested_object(_json_object(mcp_json), "mcpServers", _SERVER_NAME)` then `_config_argument(...)` —
over three named helpers that carry that totality explicitly:

- `_json_object(path)` — the file's top-level JSON object; `None` when absent, unreadable, or not
  an object. **Foreign and malformed files are someone else's**, so discovery skips them silently
  rather than crashing the walk. `_is_usable_settings` reuses it, which is why the two probes now
  tolerate exactly the same hostile input by construction.
- `_nested_object(container, *keys)` — follows `keys` down nested JSON objects, returning `None` at
  the first missing or non-object step.
- `_config_argument(arguments)` — the value following `--config` in a recorded argv list, if it
  carries one.

## Invariants And Boundaries

- **An explicit `--config` always bypasses discovery** — callers only invoke `discover_config()`
  when the flag is absent (see `cli/dashboard.py`).
- **The semantic probe is load-bearing, not cosmetic:** the repository ships a tracked placeholder
  template at the convention path (`.claude/mcp/agents-remember-settings.json` with
  `<PATH/TO/YOUR/...>` placeholders), so running from inside a source checkout must walk PAST it
  to the workspace's real settings. A purely syntactic "file exists" probe would shadow the real
  settings with the template.
- Per-level precedence is convention **before** `.mcp.json` registration; across levels,
  nearest-directory-wins beats both.
- The registration probe never validates the recorded path itself beyond usability — a registered
  `--config` pointing at a missing or template file is skipped silently and the walk continues.
- Discovery returns the settings **path**; validation/parsing into `McpRuntimeConfig` stays with
  `mcp.config.load_config` (no duplicate config semantics here).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The CLI consumer: `--config` optional, discovery fallback + `ConfigDiscoveryError` reporting. | "config_path = args.config or discover_config()"; "except (ConfigDiscoveryError, ConfigError) as error:" | mcp/src/agents_remember/cli/dashboard.py:319-319; mcp/src/agents_remember/cli/dashboard.py:321-321 |
| The CLI consumer: `--config` optional, discovery fallback + `ConfigDiscoveryError` reporting. | "config_path = args.config or discover_config()"; "except (ConfigDiscoveryError, ConfigError) as error:" | mcp/src/agents_remember/cli/dashboard.py:319-319; mcp/src/agents_remember/cli/dashboard.py:321-321 |
| The settings loader the discovered path feeds (`load_config`). | `load_config` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:159-167 |
| Unit tests: convention/registration hits, precedence, nearest-wins, malformed tolerance, template skip, miss error. | "class DiscoverConfigTests(unittest.TestCase):" | mcp/tests/test_cli_discovery.py:42-89 |

## Update History
- 2026-09-30T12:15:39+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`): No content impact: this card's own source is unchanged. MIK-R29 grew `mcp/src/agents_remember/cli/dashboard.py` (the reader import and the `knowledge_reader_port` binding), so the citation rows into it that moved were re-pointed by the installed fixer's normalisation or by the exact base-to-staged line shift; every re-pointed row was checked to hold its anchors in the new range, and no claim was reworded. No verification stamp was advanced.
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): No content impact: this card's source is unchanged. Rows citing lines that MIK-R25 moved in `dashboard.py` were re-pointed, by the installed fixer (its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; each such row was byte-identical to memory HEAD. No verification stamp was advanced.
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/src/agents_remember/cli/dashboard.py`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the one enforced citation row was re-read and re-derived because this leaf's line shifts moved the constructs it names.** The row's two anchors live in `cli/dashboard.py`, which this leaf's +16-line insertion pushed down: `config_path = args.config or discover_config()` is now at 283 (was 267) and `except (ConfigDiscoveryError, ConfigError) as error:` at 285 (was 269). Both ranges were re-derived from the candidate (`267-267` → `283-283`; `269-269` → `285-285`) and both anchors were verified to occur literally at those lines. The claim wording, the other two rows, the anchors themselves and the two verification rows are unchanged — this is a citation-only repair, and `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are deliberately **not** advanced, because nothing in this leaf is committed and the governed closeout owns the real stamp.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `load_config` repointed to mcp/src/agents_remember/kernel/primitives/runtime_config.py:159-167. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `DiscoverConfigTests`; "test_miss_raises_with_both_patterns_and_the_origin" repointed to mcp/tests/test_cli_discovery.py:42-89; mcp/tests/test_cli_discovery.py:80-80. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-03T02:56:49+02:00 — W3-B04 curator: curated 2 table citations (2 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0911` armed with no
  exemptions): `_config_from_mcp_registration` was rebuilt on the new `_json_object`,
  `_nested_object` and `_config_argument` helpers, and `_is_usable_settings` now reuses
  `_json_object` — so both probes tolerate the same hostile input by construction. Discovery
  results and the `ConfigDiscoveryError` message are unchanged. Verification metadata pinned until
  closeout stamps the L2 commit.
- 2026-07-03T09:55+02:00 — Created for 260703 L1 (dashboard config auto-discovery): upward walk with
  convention-then-registration probing, nearest-wins, the `_is_usable_settings` semantic probe (the
  tracked placeholder template must never shadow real settings), and the both-patterns miss error.
  Verification metadata pinned until closeout stamps the code commit.
