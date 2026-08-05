# mcp/src/agents_remember/providers/lifecycle/state_files.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/state_files.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`state_files.py` owns JSON state file reads and writes for provider lifecycle
modules.

## Code Commentary

### Logic

The module returns an empty dict for absent JSON state files and writes
deterministic, sorted, indented JSON with a trailing newline.

### Invariants And Boundaries

- State file helpers do not interpret provider state.
- Callers own schema decisions and error handling around loaded data.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| CGC and GrepAI lifecycle modules use these helpers for provider state and image locks. | `CgcBackendContext` | mcp/src/agents_remember/providers/cgc/lifecycle/backend.py:53-70 |
| Provider settings reads reuse the JSON loader. | `cgc_settings_from_file` | mcp/src/agents_remember/providers/lifecycle/provider_settings.py:33-41 |

## Update History
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 2 citation claims; scoped result 0 findings.

- 2026-05-25T21:14+02:00: Created from the JSON state portion of the former shared lifecycle common module.
