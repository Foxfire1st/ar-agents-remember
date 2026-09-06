# mcp/src/agents_remember/providers/current_state.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/current_state.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T15:20+02:00     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`current_state.py` projects provider watcher status into the current runtime
truth that MCP callers should read. It writes the latest provider state to
`logs/providers/status/<scope>/<instance>/current.json` under the coordination
root.

## Code Commentary

### Logic

`build_current_provider_state()` captures the check time (or accepts an injected
`checked_at` from the dashboard projector), maps raw watcher status into per-provider
state, computes an aggregate state, and returns a versioned `provider-current-state`
payload. `write_current_provider_state()`
persists that payload beside the central provider status logs. Instance path
selection uses a shared provider scope/id when all configured providers match,
or a deterministic mixed digest when the config combines multiple provider
instances.

The provider mappers keep GrepAI and CGC shapes separate. GrepAI state records
PostgreSQL, Ollama, and watcher resources plus `watcherUp`, indexing state, and
configured repo targets. `grepai_target_repos(config)` derives those targets from
the MCP repository memory roots (`repoId` + memory-root `path`) and
`grepai_current_state()` persists them as `targetRepos` when present. The
readiness/indexing values are still provider-level until GrepAI exposes per-root
health, but the repo coverage itself is explicit and stable. `targetRepos` means
the aggregate GrepAI instance has addressable repo/project targets; it does not
mean the current-state payload has split GrepAI into separate processes. CGC state records
the shared FalkorDB backend plus one watcher resource per repo. Disabled
configured providers are represented explicitly as `disabled` and do not poison
aggregate readiness.

GrepAI readiness is additionally gated on workspace presence.
`grepai_workspace_present()` inspects the watcher's `workspaceStatus` **stdout**
(not just its exit code, because `grepai workspace status` exits 0 even when it
prints "No workspaces configured"). `grepai_current_state()` downgrades a
container-ready GrepAI to `degraded` when no searchable workspace exists, and
`grepai_indexing_state()` reports `noWorkspace` in that case. With a workspace
present, it maps the watcher's `initialScan` log-marker probe (provided by
`grepai/lifecycle/runner.py`) to `indexing` (scan in progress) or `indexed`
(scan complete), falling back to `unknown` only when markers are absent —
parity with the CGC graph probe.

Crash-looping containers are not live: `resource_state()` returns `failed` for
`containerState == "restarting"` (Docker reports Running=true between
restarts), and both the CGC `watcherUp` and GrepAI `watcher_up` derivations
exclude restarting containers.

### Invariants And Boundaries

- This file reports what is true now; it must not embed last-setup history.
- Disabled providers are current state, not failures.
- Current state is refreshed when the agent asks the MCP for provider status or
  a context packet that includes providers, and the dashboard projector can now
  refresh it on cadence with the same timestamp used for projection.
- The file does not start, stop, or repair providers; it normalizes status
  facts produced by lifecycle watchers.
- GrepAI repo coverage is derived from configured repository memory roots and
  persisted as `targetRepos`; consumers should not rediscover that mapping from
  provider names or workspace strings.
- `targetRepos` is coverage/addressing evidence for topology and query routing,
  not per-root health evidence. Keep GrepAI readiness provider-level until the
  provider exposes root-level health.
- GrepAI is only `ready` when its watcher reports a real, searchable workspace;
  container liveness alone is not readiness. A missing/empty workspace is
  `degraded` with `indexingState: noWorkspace`.
- A `restarting` (crash-looping) container must never count as a ready
  watcher — observed during the 2.5.0 rollout, when a crash loop surfaced as
  `running: true` → `ready`.
- `indexing` is healthy-but-busy at every level: it must not degrade
  state/ok; it feeds the compact summary busy list instead.

### Todos

No open file-local todos (the former "replace GrepAI unknown indexing state"
todo is resolved by the `initialScan` marker probe).

## Docs References

No external documentation is needed for this local status projection.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed for this provider state projection. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current state payloads include version, kind, instance, aggregate state, `ok` (`state == "ready"`), check time, settings file, enabled providers, process namespace, and per-provider state. | "def build_current_provider_state("; "def aggregate_state(" | mcp/src/agents_remember/providers/current_state.py:19-34; mcp/src/agents_remember/providers/current_state.py:288-288 |
| Current state files are written under `logs/providers/status/<scope>/<instance>/current.json` by `current_state_path`. | `current_state_path` | mcp/src/agents_remember/providers/current_state.py:52-62 |
| Instance identity uses the shared configured provider scope/id or a deterministic mixed digest through `current_state_instance`. | `current_state_instance` | mcp/src/agents_remember/providers/current_state.py:65-86 |
| GrepAI and CGC status mappers keep provider-specific resources, watcher state, and indexing state separate through `grepai_current_state` and `cgc_current_state`. | `grepai_current_state`; `cgc_current_state` | mcp/src/agents_remember/providers/current_state.py:136-168; mcp/src/agents_remember/providers/current_state.py:179-203 |
| GrepAI target repos are derived from configured repository memory roots and persisted as `targetRepos` in current state. | `targetRepos` | mcp/src/agents_remember/providers/current_state.py:170-170 |
| GrepAI lifecycle settings use the same repository memory-root mapping for roots (`projectId == repoId`) through `_grepai_roots`. | `_grepai_roots` | mcp/src/agents_remember/providers/settings.py:82-91 |
| GrepAI readiness is gated on workspace presence: `grepai_workspace_present` reads the watcher `workspaceStatus` stdout, `grepai_current_state` downgrades to `degraded`, and `grepai_indexing_state` returns `noWorkspace` when absent. | `grepai_workspace_present`; `grepai_current_state`; `grepai_indexing_state` | mcp/src/agents_remember/providers/current_state.py:136-168; mcp/src/agents_remember/providers/current_state.py:302-314; mcp/src/agents_remember/providers/current_state.py:317-333 |
| Container normalization keeps container state, running flag, started-at time, uptime seconds, and health in the current-state payload through `normalize_container_state` and `resource_state`. | `normalize_container_state`; `resource_state` | mcp/src/agents_remember/providers/current_state.py:250-257; mcp/src/agents_remember/providers/current_state.py:260-272 |
| Aggregate state ignores disabled providers and reports ready, degraded, failed, unknown, disabled, or noProviders from current provider facts through `aggregate_state`. | `aggregate_state` | mcp/src/agents_remember/providers/current_state.py:285-299 |
| Provider status writes this current-state payload and returns both the file path and current-state object to MCP callers through `provider_status_packet` and `refresh_current_provider_state`. | `provider_status_packet`; `refresh_current_provider_state` | mcp/src/agents_remember/providers/status.py:53-87; mcp/src/agents_remember/providers/status.py:157-167 |
| Unit tests assert the file path, current truth shape, disabled-provider behavior, workflow-local instance paths, and provider-status integration in `ProviderCurrentStateTests`. | `ProviderCurrentStateTests` | mcp/tests/test_provider_current_state.py:23-171 |

## Cross-Repo References

No sibling repository boundary is needed to explain this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-09-06T22:41:21+00:00: Generated citation repair: `ProviderCurrentStateTests` repointed to mcp/tests/test_provider_current_state.py:23-171. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 9 table citations for current-state paths, provider aggregation, normalization, refresh, and tests; fixer-generated ranges verified.

- 2026-08-01T15:20+02:00 — 260731-EFA-L4 citation repair (no behaviour claim changed). Three ranges in `Repo-Internal References` had drifted off the symbols their findings name and were re-anchored against the current source: the status-mapper row `L85-L198` → **L136-L203** (`grepai_current_state` L136, `grepai_target_repos` L171, `cgc_current_state` L179, its `"watchers"` block closing L203 — the old range began inside `current_state_instance` and stopped mid-mapper); the `targetRepos` row `L101-L105; L132-L172` → **L100-L109; L136-L176** (the grepai branch passing `target_repos=grepai_target_repos(config)` at L108, and `payload["targetRepos"]` at L167); and the workspace-presence row `L132-L164, L298-L329` → **L136-L168; L302-L332** (`degraded` L150, `grepai_workspace_present` L302 reading `workspaceStatus` L311, `grepai_indexing_state` L317 returning `noWorkspace` L321). The card was flagged by the L4 citation sweep as drifting the same way as its two sibling observer cards; every range above was opened and read before being written. Prose unchanged. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/src/agents_remember/providers/current_state.py` and moved the lines this card cites, so the
  Citations column no longer pointed at the code its rows name. Corrected the ranges (L229-L264 →
  L233-L268; L267-L291 → L271-L295). The behaviour described is unchanged — the file's AST is
  identical to the base revision — this is a citation repair only. Verification metadata pinned
  until closeout stamps the L2 commit.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: current-state building/writing now accepts an injected `checked_at` timestamp so projector-owned refreshes and stale-age calculation share one tick time. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:31+02:00 — Clarified that GrepAI `targetRepos` are addressable project targets inside
  the aggregate provider instance, not separate per-repo processes or per-root health. Verification
  metadata will be stamped at closeout.
- 2026-06-23T22:09+02:00 — Task 12 S2 correction: GrepAI current state now persists configured
  repository memory-root targets as `targetRepos`, giving observer projection a stable repo mapping
  for memory-provider satellites. Provider readiness remains provider-level until GrepAI exposes
  per-root health. Verification metadata will be stamped at closeout.
- 2026-06-10T05:30+02:00 — `grepai_indexing_state` maps the watcher's `initialScan` markers to `indexing`/`indexed` (parity with CGC); `resource_state` treats `restarting` containers as failed and CGC/GrepAI watcher-up checks exclude crash loops (a restarting container reported Running=true and looked ready during the 2.5.0 rollout).
- 2026-06-09T22:10+02:00 — `cgc_repo_state()` degrades a ready repo target whose `indexingState` is `empty` or `backend-unreachable` (readiness reflects graph content, not container liveness; `indexing` stays ready), and `cgc_current_state()` degrades the provider when any repo target is not ready — mirroring the existing GrepAI no-workspace degradation pattern.
- 2026-06-02T16:24+02:00: GrepAI readiness gated on workspace presence — `grepai_workspace_present()` reads the watcher `workspaceStatus` stdout; container-ready GrepAI with no searchable workspace is now `degraded` / `indexingState: noWorkspace`.
- 2026-05-28T12:32+02:00: Created after provider status gained a current-state projection separate from setup history.
