# mcp/src/agents_remember/providers/cgc/lifecycle/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`cgc.py` is the CodeGraphContext lifecycle export facade. It groups the split
CGC implementation modules behind one import surface for `providers.lifecycle`.

## Code Commentary

### Logic

The module re-exports CGC backend, core settings/layout, runner, installation,
process-control, refresh, and query lifecycle functions. It intentionally
contains no behavior beyond those exports.

### Invariants And Boundaries

- Keep this module import-only.
- Put CGC implementation in the focused `cgc_*` modules.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The parent lifecycle facade imports this CGC facade. | "agents_remember.providers.cgc.lifecycle" | mcp/src/agents_remember/providers/lifecycle/__init__.py:11-11 |
| The CGC core module in the exported surface. | `cgc_uses_settings` | mcp/src/agents_remember/providers/cgc/lifecycle/core.py:30-34 |
| The CGC backend module in the exported surface. | `cgc_primary_backend_context` | mcp/src/agents_remember/providers/cgc/lifecycle/backend.py:110-119 |
| The CGC runner module in the exported surface. | `cgc_runner_image_build` | mcp/src/agents_remember/providers/cgc/lifecycle/runner.py:37-74 |
| The CGC installation module in the exported surface. | `cgc_install` | mcp/src/agents_remember/providers/cgc/lifecycle/installation.py:152-180 |
| The CGC process-control module in the exported surface. | `cgc_start` | mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py:175-201 |
| The CGC refresh module in the exported surface. | `cgc_refresh` | mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py:106-143 |
| The CGC query module in the exported surface. | `cgc_run` | mcp/src/agents_remember/providers/cgc/lifecycle/query.py:87-107 |

## Update History

- 2026-08-03T02:47:40+02:00 — W3-B01 curator: curated 8 Repo-Internal table citations with exact parent-facade and seven lifecycle-module anchors, expanding the aggregate row into source-local citations. The original exported-surface wording omitted the current `compose` module also listed by the facade; that semantic Tier-3 discrepancy is inventoried rather than silently expanded. Verification metadata remains unchanged for closeout.
- 2026-05-26T12:51+02:00: Updated after exporting the CGC Docker runner lifecycle helpers.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created as the CodeGraphContext lifecycle export facade.
