# mcp/src/agents_remember/mcp/tools/read_files.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/mcp/tools/read_files.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-22T22:33+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                     |

## Purpose

`read_files.py` is the thin payload builder for the `read_ar_files` tool
(slice 07): it forwards to the controller and returns the result through the
shared token choke point.

## Code Commentary

`read_ar_files_payload(config, repo_id, files, refresh=False)` calls
`read_ar_files_tool` (the controller, where all resolution lives) and wraps its
dict in `_tool_payload("read_ar_files", ...)`, so the response is validated
against its registered model and the token fields are stamped at the one choke
point. The module holds no logic of its own — the batch-read, path-confinement,
onboarding-lookup, front-door-dedup, and `read.packet` behavior all live in the
controller.

## Invariants And Boundaries

- The payload module stays a thin facade: validation and token stamping happen in
  `_tool_payload`; domain behavior belongs to the controller.
- Token fields are stamped by `_tool_payload`, never set here.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The controller that does the actual resolution. | [controllers/read_files.py](agents-remember/mcp/src/agents_remember/controllers/read_files.py) |
| The shared choke point that validates the response and stamps tokens. | [base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| The strict response model `read_ar_files` validates against. | [models/read_files.py](agents-remember/mcp/src/agents_remember/models/read_files.py) |

## Update History

- 2026-06-22T22:33+02:00 — Created for slice 07: the thin `read_ar_files_payload` wrapper over the controller and `_tool_payload`. Verification metadata pinned until closeout stamps the slice-07 code commit.
