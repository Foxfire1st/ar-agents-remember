# mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`process_control.py` owns CodeGraphContext watcher container start/stop
lifecycle and all-root start/stop aggregation.

## Code Commentary

### Logic

The module builds dry-run Docker watcher commands, starts the managed FalkorDB
backend when settings-backed roots require it, starts `cgc watch` inside the
CGC runner image, records provider state, removes watcher containers on stop,
marks stopped state, and aggregates start/stop results across configured roots.
Watcher startup renders the Compose override with backend host ports from the
backend start result so repeated settings-backed starts keep the same
FalkorDB/browser port mappings. Every watcher `up` (start, start-all, and
their dry-run plans) passes `--remove-orphans`: the render always lists every
configured watcher service, so Compose removes exactly the watcher containers
of repos that were dropped from MCP settings instead of leaving them running
against the shared backend.

`cgc_index_concurrency(layout_count)` bounds how many repos reindex
simultaneously. Each CGC indexer self-throttles to ~10 in-flight FalkorDB
queries and uses up to ~10 parser threads; reindexing all repos in parallel
(`max_workers=len(layouts)`) would peg the CPU and overrun the shared FalkorDB
query queue on a workspace with many repos. The default cap is
`DEFAULT_CGC_INDEX_CONCURRENCY` (2). The env var `AR_CGC_INDEX_CONCURRENCY`
overrides the cap (non-integer values are silently ignored in favour of the
default). The function returns at least 1 and at most `layout_count`.
`cgc_parallel_layout_action_results` now calls `cgc_index_concurrency` to set
`max_workers` instead of always using `len(layouts)`.

### Invariants And Boundaries

- Long-running watcher start/stop operations require a durable process
  namespace even though Docker owns the actual watcher lifetime.
- Backend lifecycle is delegated to `backend.py`.
- Refresh and bounded query behavior live in sibling lifecycle modules.
- Host PIDs are not a managed CGC contract; watcher state is tracked by Docker
  container name.
- Watcher `up` should render dependency backend ports from the current start
  result when available.
- `--remove-orphans` is safe here only because the render is always complete:
  if a future change renders a partial service set, the flag would delete the
  watchers that were merely omitted.
- The parallel reindex fan-in is capped by `cgc_index_concurrency` (default 2)
  to prevent FalkorDB query queue saturation on large workspaces; override with
  `AR_CGC_INDEX_CONCURRENCY` on machines with more resources.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared process helpers provide durable namespace checks and command execution. | "def process_namespace_status() -> dict[str"; "def run_command(" | mcp/src/agents_remember/providers/lifecycle/command_runner.py:15-15; mcp/src/agents_remember/providers/lifecycle/process_status.py:38-38 |
| CGC backend startup is delegated to the backend module. | "def cgc_backend_start(args: argparse.Namespace) -> dict[str" | mcp/src/agents_remember/providers/cgc/lifecycle/backend.py:390-390 |
| Docker watcher command construction lives in the runner module. | "def cgc_runner_image_build(args: argparse.Namespace" | mcp/src/agents_remember/providers/cgc/lifecycle/runner.py:37-37 |
| `cgc_index_concurrency` is also imported by `refresh.py` to report `indexConcurrency` in the refresh-all result. | "def cgc_refresh_all(args: argparse.Namespace) -> dict[str"; "def cgc_index_concurrency(layout_count: int) -> int:" | mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py:259-259; mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py:175-175 |
| Unit tests protect the cap defaults, env-override, and boundary conditions. | "def test_default_caps_below_repo_count(self) -> None:"; "def test_env_override_raises_cap(self) -> None:"; "def test_bad_override_falls_back_to_default(self) -> None:"; "def test_zero_layouts_returns_one(self) -> None:" | mcp/tests/test_cgc_index_concurrency.py:22-22; mcp/tests/test_cgc_index_concurrency.py:37-37; mcp/tests/test_cgc_index_concurrency.py:41-41; mcp/tests/test_cgc_index_concurrency.py:45-45 |

## Update History

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 5 citation rows with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py` since the L2 base commit is
  the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-10T06:20+02:00 — Body-quality pass: merged the `--remove-orphans` semantics into Logic and added the complete-render precondition to Invariants (documentation only).
- 2026-06-09T22:10+02:00 — All watcher `up` invocations (start, start-all, and their dry-run plans) now pass `--remove-orphans`; the render always contains every configured watcher service, so Compose removes exactly the watcher containers of repos no longer in MCP settings.
- 2026-06-01T00:00+02:00 — Added `cgc_index_concurrency` (default 2, `AR_CGC_INDEX_CONCURRENCY` override) to bound `cgc_parallel_layout_action_results` fan-in and prevent FalkorDB queue saturation; updated Logic, added fan-in Invariant, added cross-references.
- 2026-05-31T12:30+02:00 — Removed already-running watcher detection from start preflight: `cgc_running_process_result` (and its `cgc_watcher_inspect` use / `alreadyRunning` short-circuit) deleted; layout params now typed `CgcRuntimeLayout` (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `cgc_backend_all_error` now accepts `dict | None` with a `None` guard (closes a latent crash when start-all returns a doctor-failure); extracted `_cgc_start_all_live` to reduce `cgc_start_all` complexity; behavior-preserving (commits `0549b28`, `e3dab63`).
- 2026-05-27T00:25+02:00: Updated after watcher startup began reusing
  backend start-result port mappings in its Compose render.
- 2026-05-26T12:51+02:00: Updated after watcher start/stop moved from host PIDs to Docker watcher containers.
- 2026-05-25T21:14+02:00: Split from `process.py` so watcher process control is separate from refresh and bounded query commands.
