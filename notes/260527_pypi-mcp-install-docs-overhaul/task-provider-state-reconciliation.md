# Task: Provider State Reconciliation And Recovery

**Status:** source implementation complete; installed MCP retest pending
**Parent Task:** `260527_pypi-mcp-install-docs-overhaul`
**Repo:** agents-remember-md
**Type:** Provider | State | Reporting | Tests
**Created:** 2026-05-28T11:32
**Series Role:** follow-up 02, split out from provider workflow compatibility after setup reporting grew large

---

## Objective

Create a durable provider state model that reports current provider runtime truth: container state, watcher state, uptime, and indexing state.

The setup summary files own what happened during the last setup attempt. MCP/provider status should show what is true now.

---

## Requirements

- Introduce a first-class provider state artifact for the current provider instance, separate from one-shot setup summaries.
- Track current state per provider and per owned resource/container, including GrepAI backend/embedder/watcher and CodeGraphContext backend plus per-repo watchers.
- Track whether each container/resource is up or down, how long it has been up when available, whether each watcher is up, and the current indexing state.
- Keep setup history in setup summary files only. Do not let an old failed setup result appear as current provider state.
- Let later status checks reconcile current health. If live providers are healthy, current state is ready even if the last setup summary recorded failed phases.
- Keep strict setup `ok` semantics in the setup command and setup summary. Current provider state should use runtime labels such as `ready`, `degraded`, `failed`, `stale`, or `unknown`.
- Make `provider_status`, watcher status, and context packets surface current provider/runtime facts only. They may point users to setup summaries for history, but their main state must be current truth.
- Record enough current detail to debug individual providers and containers without requiring the original huge setup JSON payload.
- Keep operator-facing provider state under the coordination-root log/status tree, consistent with `logs/providers/...`; do not store provider state in `providers/logs/...`.
- Avoid destructive reconciliation. A status check may update the provider state artifact, but it must not stop, restart, remove, or mutate containers.
- Ensure worktree and benchmark provider instances write/read their own state, not the workspace provider state.
- Add tests for setup failure followed by healthy status, per-container state visibility, watcher up/down state, indexing state, stale status handling, and workflow-local provider instances.

---

## Implementation Steps

### S1 - Current State Audit

- [x] Map every current provider state surface.
  - [x] Audit GrepAI runtime state files, CGC state files, provider setup summaries, `provider_status`, watcher status, and context packet provider reporting.
  - [x] Identify which surfaces are runtime-private versus operator-facing.
  - [x] Record which current payload fields are required for per-container state, uptime, watcher state, and indexing state.

### S2 - State Schema

- [x] Define the durable provider state schema.
  - [x] Include instance identity, scope, coordination root, settings file, provider enablement, current status, per-resource status, uptime, watcher state, indexing state, and timestamps.
  - [ ] Define current-state transitions for stale status.
  - [x] Decide the exact state artifact path under `logs/providers/...`.

### S3 - Reconciliation Writer

- [x] Implement state writes from non-mutating status checks.
  - [x] Ensure `provider_setup` continues writing setup summaries, not current provider state history.
  - [x] Update current status from `provider_status` or watcher status without mutating containers.
  - [x] Make current state become ready when live providers are ready, regardless of failed phases preserved in setup summaries.

### S4 - Reporting Surfaces

- [x] Update user-facing provider status payloads.
  - [x] Surface current provider state, current per-container/resource state, watcher up/down state, uptime, and indexing state.
  - [x] Keep setup-history fields out of current status except for an optional setup summary path/hint.
  - [x] Make context packets report ready/degraded/failed current state clearly.
  - [x] Keep command-level `ok` distinct from current provider readiness.

### S5 - Tests And Retest

- [x] Add unit tests for reconciliation behavior.
  - [x] Setup failure followed by healthy watcher status reports current state as ready without echoing old setup failure as current state.
  - [x] Failed child provider/container remains visible in current provider state.
  - [x] Watcher up/down and indexing state are visible in current provider state.
  - [x] Worktree and benchmark provider instances do not read or overwrite workspace provider state.
  - [ ] Stale status timeout behavior is explicitly modeled and tested.
- [ ] Retest main provider prepare/status after the source changes are installed or published.
  - [ ] Verify a later healthy status reports current state as ready.
  - [ ] Verify a future `ok=false` setup records enough detail to diagnose the failed phase.

---

## Implementation Notes

- Added `providers/current_state.py` as the owner for current runtime provider state projection and persistence.
- Current state is written to `logs/providers/status/<scope>/<instance>/current.json`.
- `provider_status`, context packets with providers enabled, and MCP watcher status now write/read current state derived from live watcher status.
- Current state records GrepAI backend/embedder/watcher resources and CGC FalkorDB plus per-repo watcher resources.
- Docker-derived resource summaries include container state, running flag, health, start time, and uptime seconds.
- Disabled configured providers are reported as `disabled` and do not make enabled provider readiness fail.
- CGC watcher all-status now includes backend status, and the aggregate `ok` fails when the shared FalkorDB backend is unhealthy.
- Setup summaries remain separate under the setup-reporting path and are not copied into current state.
- Stale timeout behavior is intentionally still open because the current user-facing status surfaces perform live non-mutating reconciliation instead of reading old state as truth.

## Verification

- `source .venv/bin/activate && ruff check mcp/src/agents_remember/providers/current_state.py mcp/src/agents_remember/providers/lifecycle/docker_runtime.py mcp/src/agents_remember/providers/lifecycle/watchers.py mcp/src/agents_remember/providers/status.py mcp/src/agents_remember/controllers/skill_tools.py mcp/src/agents_remember/providers/cgc/lifecycle/installation.py mcp/tests/test_provider_current_state.py mcp/tests/test_tools.py mcp/tests/test_context_packet.py`
- `source .venv/bin/activate && python -m pytest mcp/tests/test_provider_current_state.py mcp/tests/test_provider_lifecycle.py mcp/tests/test_context_packet.py mcp/tests/test_tools.py mcp/tests/test_install_runtime.py -q`
- `source .venv/bin/activate && python -m agents_remember.code_quality.check` passed with 234 tests passed, 3 skipped. CRAP threshold findings remain report-only existing findings.

---

## Proposed Code Examples

### E1 - Provider State Artifact Shape

Distinct change covered: current provider state must report the live runtime, not setup history.

Why this example is included: it shows the MCP/status-facing shape the user should see when asking whether providers are currently usable.

```json
{
  "version": 1,
  "instance": {
    "id": "projects",
    "scope": "workspace",
    "coordinationRoot": "/workspace/ar-coordination"
  },
  "state": "ready",
  "ok": true,
  "checkedAt": "2026-05-28T11:45:00+02:00",
  "summary": "All configured providers are currently usable."
}
```

### E2 - Per-Resource State

Distinct change covered: users need to see container state, watcher state, uptime, and indexing state instead of only a top-level boolean.

Why this example is included: it is the missing layer between `ok=false` and actionable provider troubleshooting.

```json
{
  "providers": {
    "grepai-memory": {
      "state": "ready",
      "watcherUp": true,
      "indexingState": "idle",
      "resources": {
        "postgres": {"containerState": "running", "uptimeSeconds": 7220, "containerName": "ar-grepai-postgres-projects"},
        "ollama": {"containerState": "running", "uptimeSeconds": 7218, "containerName": "ar-grepai-ollama-projects"},
        "watcher": {"containerState": "running", "uptimeSeconds": 7190, "containerName": "ar-grepai-watcher-projects"}
      }
    },
    "codegraphcontext-code": {
      "state": "degraded",
      "indexingState": "repo-refreshing",
      "resources": {
        "falkordb": {"containerState": "running", "uptimeSeconds": 7225, "containerName": "ar-cgc-falkordb-projects"},
        "watchers": {
          "agents-remember-md": {"watcherUp": true, "indexingState": "idle"},
          "device-management": {"watcherUp": false, "indexingState": "unknown"}
        }
      }
    }
  }
}
```

---

## Decision Log

| Date-Time | Decision | Rationale |
| --- | --- | --- |
| 2026-05-28T11:32 | Split provider state reconciliation into its own task. | The provider workflow compatibility task already covers isolation, warm-start, and central logging; durable state reconciliation is a separate layer and should not be buried in that task. |
| 2026-05-28T11:32 | Keep setup reporting and current provider state separate. | Setup summaries preserve command history, while provider state needs to represent current usability after later health checks and recovery. |
| 2026-05-28T11:45 | MCP/provider status must show current runtime truth only. | Setup summaries answer what happened during setup; MCP status answers what is currently up, down, watching, and indexing. |
| 2026-05-28T12:25 | Store current state under `logs/providers/status/<scope>/<instance>/current.json`. | The status tree is operator-facing and instance-scoped, while setup summaries stay in the setup-reporting tree. |
| 2026-05-28T12:25 | Keep stale-state timeout as a follow-up. | Current MCP status performs a fresh non-mutating runtime check, so stale behavior only applies to future artifact-read surfaces. |

---

## Open Questions

- What stale-status timeout should mark current provider state as stale?

---

## References

- [Provider workflow compatibility task](/home/mohamedreadone/Projects/ar-coordination/tasks/agents-remember-md/260527_pypi-mcp-install-docs-overhaul/task-provider-workflow-compatibility.md)
- [Parent findings](/home/mohamedreadone/Projects/ar-coordination/tasks/agents-remember-md/260527_pypi-mcp-install-docs-overhaul/findings.md)
- [Provider setup service](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py)
- [Provider setup reporting](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/setup_reporting.py)
- [Provider status packet](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/status.py)
- [Watcher lifecycle orchestration](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/lifecycle/watchers.py)
