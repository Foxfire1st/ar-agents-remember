# mcp/src/agents_remember/providers/cgc/lifecycle/query.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/query.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`query.py` owns bounded native `cgc run` commands and explicit CGC visualizer
lifecycle commands.

## Code Commentary

### Logic

The module strips native args after `--`, rejects `visualize` through bounded
`run`, checks status before live commands, executes bounded native commands
inside the CGC Docker runner with captured output, builds Dockerized visualizer
server commands, validates ports, and runs visualizer foreground commands only
after durable namespace checks. The visualizer `--repo` argument is the layout's
driveless container path (`container_code_repo_root`), so it is valid inside the
Linux runner on Windows hosts.

`cgc_run_status_result` (the `cgc run` pre-flight) now gates on `cgc_backend_status` (FalkorDB running + data mount + network + ping) instead of `cgc_status` (which also requires the watcher container to be running). A one-shot `cgc run` — such as the seed's `bundle import` or a graph query — needs only the FalkorDB backend; gating on the full provider status blocked the seed because worktree watchers start last (OQ7), causing the import to never run and the seed to fall back to a full re-index. Queries issued with the worktree fully up are unaffected by this change. The visualize path (`cgc_visualize_status_result`) still gates on the full `cgc_status`.

### Invariants And Boundaries

- `cgc run` is only for bounded native commands and must reject visualizer
  server startup.
- `cgc visualize` is the explicit long-running server command and requires a
  durable process namespace.
- Watcher start/stop behavior lives in `process_control.py`.
- Query and visualizer execution must use the Docker runner image, not a host
  `cgc` executable.
- Command/dry-result helpers take a concrete `CgcRuntimeLayout` (imported from
  `agents_remember.providers.context`), not an untyped `Any` layout.
- `cgc_run_status_result` gates on `cgc_backend_status` (backend only); `cgc_visualize_status_result` gates on the full `cgc_status` (backend + watcher).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| CGC status checks are provided by the installation module. | "def cgc_status" | mcp/src/agents_remember/providers/cgc/lifecycle/installation.py:317-317 |
| `cgc_backend_status` (backend-only readiness) is provided by the backend module. | `cgc_backend_status` | mcp/src/agents_remember/providers/cgc/lifecycle/backend.py:194-237 |
| Docker command construction is provided by the runner module. | `cgc_runner_image_build` | mcp/src/agents_remember/providers/cgc/lifecycle/runner.py:37-74 |
| Provider lifecycle tests cover visualizer rejection, dry-run visualize command construction, and bounded `cgc run`; the `cgc run` test now stubs `cgc_backend_status`. | `test_run_rejects_visualizer_server` | mcp/tests/test_provider_lifecycle.py:1030-1056 |

## Update History
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 3 citation claims; scoped result 0 findings.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/providers/cgc/lifecycle/query.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-01T23:40+02:00 — `cgc_run_status_result` now gates on `cgc_backend_status` (FalkorDB backend only) instead of `cgc_status` (full provider including watcher). Fixes OQ7-caused seed failure: worktree watchers start last, so gating `bundle import` on the watcher caused the import to never run and the seed to fall back to a full re-index. The visualize path still uses `cgc_status`. Added `cgc_backend_status` import from `backend.py`. Updated Logic, Invariants, and Repo-Internal References.
- 2026-05-31T12:50+02:00 — `cgc_run_command`, `cgc_run_dry_result`, `cgc_visualize_command`, and `cgc_visualize_dry_result` now type their `layout` param as `CgcRuntimeLayout` (newly imported from `agents_remember.providers.context`) instead of `Any`; added an Invariants note recording the concrete layout type (1.0.0 review remediation).
- 2026-05-29T07:19+02:00: Updated after the visualizer `--repo` argument switched to the driveless container path (`container_code_repo_root`) for Windows-host support.
- 2026-05-26T12:51+02:00: Updated after bounded CGC run and visualizer commands moved into the Docker runner.
- 2026-05-25T21:14+02:00: Split from `process.py` so bounded query and visualizer behavior is separate from watcher process control and refresh.
