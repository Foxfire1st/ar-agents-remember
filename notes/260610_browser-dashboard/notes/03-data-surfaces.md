# 03 — Observable Data Surfaces Inventory

| Field | Value |
| --- | --- |
| Topic | Every artifact the system produces today that a dashboard could read, plus the gaps |
| Status | Inventory (verified 2026-06-10 against MCP 2.7.0 @ `ab7e21b`; **delta re-verified 2026-06-12 against 2.9.0 @ `610b856`**: tools 37→36 (+`worktree_sync`, −`direct_closeout_*`), contract still v1 + new `sync_log` field, `worktree_start` response shape and `setup-progress.json` contract unchanged) |
| Sources | Recon agent over live `ar-coordination/` tree + source + onboarding; raw detail in `raw/recon-workflow-output.json` → `dataSurfaces` |

## Surfaces That Exist Today

| # | Surface | Path (pattern) | Producer / trigger | Dashboard value |
| --- | --- | --- | --- | --- |
| 1 | Provider current-state snapshot | `logs/providers/status/<scope>/<instance>/current.json` | `current_state.py` via `provider_status` / `context_packet(include_providers)` / `provider_watchers` — **call-triggered, stale between calls** | Provider tiles, per-container uptime/health, per-repo watcher + indexing state |
| 2 | Provider setup summaries | `logs/providers/setup/{<UTC>-<action>.json, last-<action>[-full].json}` | `setup_reporting.py` at end of every setup run | Setup history, phase failure rates, seed-vs-reindex outcomes |
| 3 | Worktree setup progress (2.7.0) | `<worktreeGroup>/provider-runtime/setup-progress.json` | `setup_progress.py` on daemon thread; 15s heartbeat, stale > 90s; `currentPhase`, `completedPhases[]`, `seedFallback`, `retryArgs` | **The boot-sequence data.** Live phase widget; docstring: "any dashboard can observe this file" |
| 4 | Worktree provider-state | `<worktreeGroup>/provider-runtime/provider-state.json` | written on successful isolated setup | Inventory of live isolated stacks; join key to Docker compose projects |
| 5 | Worktree group layout | `worktrees/<repo>/<group>-ar/{code, memory-<name>, provider-runtime}` | worktree_start / cleanup / abandon | Active vs stale groups (3 of 4 looked uncleaned at recon), disk, pairing |
| 6 | Worktree contract | `tasks/<repo>/<task>/contract.md` (YAML front matter `ar-worktree-contract/v1`) | `worktree_contract.py`; mutated at each contract state transition ("lifecycle" is now reserved for note 01's entity) | Per-task kanban: started → approved → closed out → integrated → cleaned; approval audit; since 2.9.0 also a `sync_log` (one entry per mid-task base sync) |
| 7 | Task files + registry | `tasks/<repo>/<YYMMDD>_<name>/task.md`, `tasks/index.md` | hand-written by sessions | Open-task board, decision-log feed (markdown parsing required) |
| 8 | Memory ledger | `memory-repos/ar-<repo>/memory.md` (`ar-memory-ledger/v1` + table) | closeout/baseline/carryover tools, one row per closeout | Memory↔code currency, closeout frequency over time (~95 rows) |
| 9 | Drift reports | `temp/drift-reports/<token>/<repo>_<branch>_drift-report.md` | drift_check / memory_quality_check; **same-name overwrite, no history** | Drift gauge + classification breakdown (last run: 330 up-to-date / 1 disabled) |
| 10 | Route indexes | 18× `onboarding/**/overview.index.json` | `route_index_refresh` | Coverage charts (root: 878 files in scope), route tree map |
| 11 | Onboarding sidecars | `onboarding/**/<file>.md` metadata (`lastVerifiedCommitHash/Date`) | c-05 during closeouts | lastVerified age histogram over 330+ units, stalest-docs leaderboard |
| 12 | Tool reports | `temp/tool-reports/<tool>/<UTC>-<label>.json` (keep-last-5, 7 days) | `tool_reports.py` for verbose tools | Recent heavy-ops drill-down (bounded window) |
| 13 | MCP read-only tools (37 total at 2.7.0; 36 at 2.9.0 — +`worktree_sync`, −`direct_closeout_*`) | stdio server; e.g. `context_packet`, `worktree_status` (designated poll target: phase, dirty flags, providers block), `provider_status`, `drift_check`, `cgc_*`, `grepai_*` | FastMCP; every response token-stamped via `_tool_payload` | The poll API; per-call token cost already present in every payload |
| 14 | Watcher log roots | `logs/providers/{grepai,codegraphcontext}/...` | **reserved but empty** — watchers log to Docker stdout only (`docker logs <containerName>` via names in current.json) | Would be indexing-activity tail; today requires docker shell-out |

Also: `sessions/` (issue #43) does **not** exist yet. `logs/mcp/` exists, empty.

## The Gaps (what a dashboard wants that nothing emits)

1. **No tool-call event stream** — which tools ran, when, args, duration. Without
   this, "activity" is invisible. (Natural emit point: `_tool_payload`.)
2. **No token-spend persistence** — every payload is stamped, nothing aggregates.
   The "fuel gauge" needs a time series.
3. **No session/lifecycle record** — note 01; the central gap.
4. **No health history** — current.json is one overwritten snapshot, call-triggered;
   no heartbeat when idle, no uptime series.
5. **No drift trend** — reports overwrite per repo+branch.
6. **No indexing throughput/lag numbers** — `watchers.lastRefresh` null, SetupProgress
   `metrics{itemsDone,itemsTotal,percent}` reserved but unpopulated.
7. **Setup phase timings not rolled up** — setup-progress.json dies with the worktree group.
8. **No machine-readable task registry** — `tasks/index.md` is hand-maintained markdown.
9. **No push channel** — everything is poll-a-file/poll-a-tool. (A "file ping
   transport" idea was explicitly deferred in the issue-54 task decisions.)
10. **No stale-worktree detection** — integration-complete-but-uncleaned groups
    must be inferred from contract + dir existence.
11. **No retrieval-latency persistence** — grepai/cgc responses embed
    durationSeconds; dropped on the floor.
12. **No cross-repo rollup** — context_packet is per-repo, on demand, unpersisted.

## Reading For The Design Task

The v1-vs-v2 split from the recon still holds even with the "plan for 3.0"
posture (note 04): surfaces 1–13 can power a *read-only* first light without any
MCP change, which keeps the visual track unblocked while the lifecycle/event
architecture (notes 01–02) is designed properly. The gaps list is effectively
the requirements backlog for the 3.0 observability work.
