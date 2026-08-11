# mcp/src/agents_remember/mcp/tools/read_files.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/mcp/tools/read_files.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-02T01:05+02:00                           |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                     |

## Purpose

`read_files.py` is the thin payload builder for the `read_ar_files` tool
(slice 07): it forwards to the application entry point and returns the result through the
shared token choke point.

## Code Commentary

`read_ar_files_payload(config, repo_id, files, refresh=False)` calls
`read_ar_files_tool` (the application entry point, where all resolution lives) and wraps its
dict in `_tool_payload("read_ar_files", ...)`, so the response is validated
against its registered model and the token fields are stamped at the one choke
point. The module holds no logic of its own — the batch-read, path-confinement,
onboarding-lookup, front-door-dedup, and `read.packet` behavior all live in the
application entry point.

## Invariants And Boundaries

- The payload module stays a thin facade: validation and token stamping happen in
  `_tool_payload`; domain behavior belongs to the application entry point.
- Token fields are stamped by `_tool_payload`, never set here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application entry point that does the actual resolution. | `read_ar_files_tool` | mcp/src/agents_remember/application/read_files.py:77-133 |
| The shared choke point that validates the response and stamps tokens. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:70-72 |
| The strict response model `read_ar_files` validates against. | `ReadArFilesResponse` | mcp/src/agents_remember/models/read_files.py:50-63 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 3 repository-internal references for the read-files application, token choke point, and response model; final scoped result 0 (checker-clean).

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-22T22:33+02:00 — Created for slice 07: the thin `read_ar_files_payload` wrapper over the controller and `_tool_payload`. Verification metadata pinned until closeout stamps the slice-07 code commit.
