# mcp/src/agents_remember/kernel/coordination_context/setting_values.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/setting_values.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`setting_values.py` applies the shared `clean_scalar` helper while parsing
mapping, list, boolean, and `crossRepo.allow` values; scalar normalization itself
is owned by that imported helper.

## Code Commentary

### Logic

The module normalizes string/list settings, validates booleans and mappings,
and converts strict v2 cross-repo allow objects into `CrossRepoAllowEntry`
models. Legacy string allow entries are retained only as excluded entries with
an explicit migration reason.

### Invariants And Boundaries

- Value parsing is format-neutral and performs no filesystem or Git checks.
- Cross-repo entries require both `repo` and `expectedBranch` before runtime
  resolution can include them.

## Docs References

No external documentation is needed for these local parsing helpers.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| JSON settings parsing delegates shared value validation to this module. | `clean_scalar` | mcp/src/agents_remember/kernel/coordination_context/json_settings.py:17-130 |
| Cross-repo runtime resolution consumes parsed allow entries. | `CrossRepoAllowEntry` | mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:41-116 |

## Cross-Repo References

No cross-repository evidence is needed for format-neutral value parsing.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04: narrowed ownership to the module's
  format-specific parsing and anchored its JSON and cross-repo consumers.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/kernel/coordination_context/setting_values.py` since the L2 base commit
  is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 9 line(s) with no token
  change whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-05-25T20:57+02:00: Created by extracting shared settings value parsing from the `c-08-ar-coordination-context-resolver` skill resolver.
