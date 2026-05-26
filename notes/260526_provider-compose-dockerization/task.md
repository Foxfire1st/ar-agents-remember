# Task: Provider Compose Dockerization

**Status:** inProgress
**Repo:** agents-remember-md
**Type:** Code
**Created:** 2026-05-26T14:38

---

## Objective

Move the Agents Remember provider Docker topology for GrepAI and CodeGraphContext out of Python command builders and runtime-generated Dockerfile strings into committed, inspectable Dockerfiles, Docker Compose base files, and override templates/fragments. Python lifecycle code should fill package-owned override templates with validated MCP-derived values at command time, feed that override to `docker compose` from trusted MCP-controlled execution context, and report resulting image/container state.

---

## Reframing

Surface request: implement the previously discussed Docker Compose direction as a light task.

Deeper objective: make the provider stack inspectable and easier to reason about by separating stable infrastructure shape from dynamic local runtime state.

Highest-leverage framing: treat committed Compose assets and override templates/fragments as the stable provider infrastructure contract, trusted MCP-rendered override content as dynamic execution input, and Python as an orchestration/validation layer rather than the Docker spec.

---

## Requirements

- Commit Dockerfiles for the GrepAI runner and CodeGraphContext runner; no runner Dockerfile should be generated from Python strings.
- Commit base Compose YAML for stable GrepAI services: Postgres/pgvector, Ollama, and GrepAI watcher/runner shape.
- Commit base Compose YAML for stable CGC services: FalkorDB backend and CGC runner/watcher shape.
- Render dynamic Compose override YAML from package-owned templates/fragments at command time from trusted MCP code rather than treating a workspace-local generated file as authority.
- Derive the rendered override only from MCP authority settings and existing lifecycle-derived provider settings.
- Keep Docker/Compose shape in committed templates/fragments; Python may validate values and repeat template fragments for dynamic cases such as per-repo CGC watchers.
- Put dynamic values in the rendered override content: coordination root, provider runtime/data/log paths, repo IDs, repo paths, selected host ports, image tags, enabled services, and per-repo CGC watcher services.
- Prefer `docker compose -f <base> -f - up/down/ps/logs/run/exec` or trusted MCP-owned temporary override files over manual `docker run` topology assembly.
- Preserve provider status, image lock/state reporting, health checks, and existing MCP provider authority behavior.
- Treat any persisted rendered override or diagnostic copy as untrusted runtime output, never as hand-edited user config or execution authority.
- Use hashes for tamper/staleness reporting by comparing persisted diagnostic/runtime copies against the server-rendered expected override content.
- Avoid compatibility or fallback layers unless a concrete migration risk is identified and explained before implementation.
- Treat the existing provider onboarding as relevant implementation context for this Docker work, reading it alongside source before editing and refreshing it through C-05 after the implementation changes.

---

## Assumptions And Boundaries

- The existing MCP settings remain the only user-facing provider authority; provider detail fields still must not move into hand-edited settings.
- The future installed MCP server/runtime is expected to live outside the editable workspace; workspace and coordination files are data, not trusted control logic.
- MCP lifecycle tools must not accept arbitrary Compose file paths, service definitions, image names, bind mounts, or Docker args from tool input.
- One-shot provider commands may use `docker compose run --rm` or `docker compose exec` depending on whether they need the long-running watcher container.
- The task includes both GrepAI and CGC; implementing only one provider is not complete.
- This task does not redesign provider query semantics, onboarding generation, or the MCP public tool surface except where command/status payloads must reflect Compose.
- Existing dirty source and drifted provider onboarding are part of the same Docker/provider lifecycle work area. Onboarding is relevant for intent and route context, while source remains the final authority for any section where drift is tied to uncommitted changes.

---

## Implementation Steps

### S1 - Establish Onboarding-Guided Docker Context

- [ ] Build the Docker/provider context map before editing.
  - [ ] Read the relevant GrepAI, CGC, lifecycle, settings, and runtime-layout onboarding sidecars/routes.
  - [ ] Compare drifted onboarding claims against the current dirty source files in the provider Docker area.
  - [ ] Record which onboarding files will need C-05 refresh after implementation.
  - [ ] Verify the plan still covers both providers and all currently touched Docker lifecycle surfaces.

### S2 - Add Source-Controlled Docker And Compose Assets

- [ ] Commit inspectable provider Docker/Compose assets.
  - [ ] Add a GrepAI runner Dockerfile that replaces `grepai_runner_dockerfile()`.
  - [ ] Add a CGC runner Dockerfile and patch asset that replace `cgc_runner_dockerfile()` and generated `patch_cgc.py`.
  - [ ] Add base Compose YAML files for GrepAI and CGC stable services.
  - [ ] Include the new assets in package/runtime installation paths.
  - [ ] Verify the committed files expose service shape, image build context, mounts, networks, commands, and health expectations clearly.

### S3 - Render Runtime Compose Overrides From Templates And MCP-Derived Settings

- [ ] Add a provider Compose renderer/service.
  - [ ] Add package-owned override templates/fragments for GrepAI dynamic values, CGC backend dynamic values, and CGC per-repo watcher services.
  - [ ] Generate GrepAI override YAML for runtime paths, data paths, log paths, selected ports, image tags, network name, workspace mounts, and enabled services.
  - [ ] Generate CGC override YAML for backend paths, selected ports, image tags, network name, and one watcher service per configured repo root.
  - [ ] Feed rendered overrides to Compose through stdin or trusted MCP-owned temporary files, not through authoritative workspace-local generated files.
  - [ ] Optionally persist diagnostic copies and hashes for status/debug output, clearly marking them as non-authoritative.
  - [ ] Validate that generated values come from lifecycle settings derived from MCP authority settings.
  - [ ] Add focused tests for deterministic override rendering.

### S4 - Migrate Lifecycle Operations To Docker Compose

- [ ] Replace manual Docker topology assembly with Compose orchestration.
  - [ ] Replace GrepAI Postgres, Ollama, runner build, watcher start/stop/status, and bounded run paths with Compose operations.
  - [ ] Replace CGC FalkorDB, runner build, per-repo watcher start/stop/status, refresh, query, and visualize paths with Compose operations.
  - [ ] Preserve image lock/state reporting by inspecting images/containers after Compose pull/build/up.
  - [ ] Preserve health checks and readiness checks for Postgres, Ollama, FalkorDB, GrepAI workspace status, and CGC watcher state.
  - [ ] Remove obsolete Dockerfile string generation and manual `docker run` topology builders after the Compose path is complete.

### S5 - Update Tests, Docs, And Onboarding

- [ ] Prove and document the new provider Docker contract.
  - [ ] Update provider lifecycle tests from manual argv expectations to Compose file/render/command expectations.
  - [ ] Update MCP/config tests that assert provider-derived runtime fields or status payloads.
  - [ ] Update user-facing docs or runtime layout docs that describe provider Docker state.
  - [ ] Route durable provider Docker findings and changed source sidecars through C-05 onboarding updates during implementation.
  - [ ] Run the repo-listed Ruff/Radon/pytest checks appropriate for the touched files.

---

## Proposed Code Examples

### E1 - Committed GrepAI Compose Base

Distinct change covered: stable provider topology moves into source-controlled Compose.

Why this example is included: this is the most visible form of the new contract; dynamic paths and ports are intentionally absent from the base file.

```yaml
services:
  postgres:
    image: ${GREPAI_POSTGRES_IMAGE}
    restart: unless-stopped
    environment:
      POSTGRES_USER: grepai
      POSTGRES_PASSWORD: grepai
      POSTGRES_DB: grepai
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U grepai -d grepai"]

  ollama:
    image: ${GREPAI_OLLAMA_IMAGE}
    restart: unless-stopped

  watcher:
    image: ${GREPAI_RUNNER_IMAGE}
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
      ollama:
        condition: service_started
    command: ["watch", "--workspace", "${GREPAI_WORKSPACE}", "--log-dir", "/grepai/logs"]
```

### E2 - Template-Rendered Override Shape

Distinct change covered: runtime-local values are rendered into dynamic Compose override YAML from package-owned templates at command time.

Why this example is included: this is the boundary where MCP-derived settings become concrete Compose input without making a workspace-local generated file authoritative.

```yaml
services:
  postgres:
    ports:
      - "127.0.0.1:51183:5432"
    volumes:
      - "/home/me/ar-coordination/providers/data/grepai/postgres/data:/var/lib/postgresql/data"

  watcher:
    volumes:
      - "/home/me/ar-coordination/providers/runners/grepai:/grepai/runtime"
      - "/home/me/ar-coordination/providers/logs/grepai:/grepai/logs"
    environment:
      HOME: /grepai/runtime/home
      XDG_STATE_HOME: /grepai/runtime/state/xdg
      XDG_CACHE_HOME: /grepai/runtime/cache/xdg
```

### E3 - CGC Per-Repo Watcher Override

Distinct change covered: dynamic per-repo CGC watcher services are rendered from an inspectable fragment in the override while the runner/backend shape remains stable.

Why this example is included: CGC is the main reason the override needs generated service entries rather than only environment substitution.

```yaml
services:
  watcher-agents-remember-md:
    image: agents-remember/codegraphcontext:0.4.10
    restart: unless-stopped
    working_dir: /runtime/agents-remember-md
    volumes:
      - "/home/me/ar-coordination/providers/runners/codegraphcontext/agents-remember-md:/runtime/agents-remember-md"
      - "/home/me/Projects/agents-remember-md:/repo:ro"
    environment:
      FALKORDB_HOST: falkordb
      FALKORDB_GRAPH_NAME: agents_remember_md
    command: ["watch", "/repo"]
```

### E4 - Python Orchestration Boundary

Distinct change covered: lifecycle code renders/validates/calls Compose instead of constructing Docker topology.

Why this example is included: this keeps Python responsible for authority, validation, and reporting while Docker/Compose owns the infrastructure shape.

```python
def start_grepai(args: argparse.Namespace) -> dict[str, Any]:
    settings_path, provider_settings, layout = grepai_layout_from_args(args)
    override = render_grepai_compose_override_from_template(provider_settings, layout)
    result = compose_up(
        base_files=grepai_base_compose_files(),
        override_yaml=override.text,
        services=["postgres", "ollama", "watcher"],
    )
    return grepai_state_from_compose(settings_path, layout, override, result)
```

---

## Decision Log

| Date-Time        | Decision | Rationale |
| ---------------- | -------- | --------- |
| 2026-05-26T14:38 | Use light-task workflow for provider Compose migration. | The change spans both providers and needs a durable plan plus approval, but can still fit a compact implementation plan. |
| 2026-05-26T14:38 | Keep MCP settings as source of truth and generated override YAML as runtime state. | This preserves the existing authority boundary while making Docker topology inspectable. |
| 2026-05-26T14:38 | Treat dirty-source provider onboarding as directional only for planning. | The task-start drift gate found actionable drift tied to dirty provider source files, so source-confirmed evidence should govern this plan. |
| 2026-05-26T14:40 | Treat provider onboarding as relevant context for the Docker migration. | The dirty worktree is concentrated in Docker/provider lifecycle files, so onboarding should guide route intent and then be refreshed through C-05 after source changes. |
| 2026-05-26T15:24 | Render dynamic Compose overrides from package-owned templates/fragments in trusted MCP code. | The MCP is expected to run outside the sandbox, so workspace-local generated YAML should not become an execution authority or prompt-injection surface, and Python should still avoid owning the whole Compose document shape. |
| 2026-05-26T15:33 | Begin implementation from `feature/provider-compose-dockerization`. | Developer approved C-09 worktree-backed implementation and asked that the feature branch be created first and used as the source of the worktrees. |

---

## Open Questions

- Should diagnostic copies of rendered overrides be persisted at all, or should `status` expose only hashes/render summaries unless explicitly requested?
- During implementation, call out any concrete reason to keep a temporary manual Docker fallback before adding it.

---

## References

- Source-confirmed GrepAI Dockerfile string and watcher command builder: `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/runner.py`
- Source-confirmed GrepAI backend/embedder manual Docker run builders: `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py`, `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py`
- Source-confirmed CGC Dockerfile string and command builders: `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py`, `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py`
- MCP authority settings derivation: `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/settings.py`, `/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/mcp/config.py`
- Local inspectable Docker example: `/home/mohamedreadone/Projects/device-management/docker-compose.yaml`, `/home/mohamedreadone/Projects/device-management/docker/`
- Task-start drift report: `/home/mohamedreadone/Projects/ar-coordination/temp/drift-reports/agents-remember-md/agents-remember-md_main_drift-report.md`
