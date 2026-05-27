# Validation Pass 02: Real MCP Redo

**Task:** `260527_pypi-mcp-install-docs-overhaul`
**Started:** 2026-05-27T14:30
**Scope:** Redo S1-S3 using the PyPI-installed MCP server through a fresh Codex harness session.

---

## Ground Rules

- Use the PyPI-installed `agents-remember-mcp` executable as the MCP server.
- Execute Agents Remember workflow behavior through MCP tool calls from a fresh Codex session.
- Do not use `agents_remember.mcp.tools.*_payload`, provider setup Python APIs, local source imports, or worktree manager Python APIs as workflow evidence.
- CLI commands are allowed only for environment setup, Codex MCP registration, Git fixture setup, and post-run inspection.
- Record every actual MCP tool call observed, its result, and any follow-up filesystem/Git verification.

---

## Harness Setup

- PyPI package installed in clean venv: `/tmp/ar-mcp-real-validate-02/venv`
  - Package: `agents-remember-mcp==0.1.0`
  - Server executable: `/tmp/ar-mcp-real-validate-02/venv/bin/agents-remember-mcp`
- Primary isolated MCP settings: `/tmp/ar-mcp-real-validate-02/.codex/mcp/settings.json`
  - `workspaceRoot`: `/tmp/ar-mcp-real-validate-02/workspace`
  - `coordinationRoot`: `/tmp/ar-mcp-real-validate-02/ar-coordination`
  - repo id: `agents-remember-md`
- Fresh child Codex invocation pattern:
  - `codex exec ... -c 'mcp_servers.agents-remember.command="/tmp/ar-mcp-real-validate-02/venv/bin/agents-remember-mcp"'`
  - `-c 'mcp_servers.agents-remember.args=["--config", "/tmp/ar-mcp-real-validate-02/.codex/mcp/settings.json"]'`
- Initial child `server_info` proof:
  - Transcript: `/tmp/ar-mcp-real-validate-02/server-info.jsonl`
  - Result: `configPath=/tmp/ar-mcp-real-validate-02/.codex/mcp/settings.json`
  - Result: `workspaceRoot=/tmp/ar-mcp-real-validate-02/workspace`
  - Result: `coordinationRoot=/tmp/ar-mcp-real-validate-02/ar-coordination`
- Installed-skill visibility proof:
  - `CODEX_HOME=/tmp/ar-mcp-real-validate-02/.codex codex debug ... prompt-input`
  - Prompt input showed installed Agents Remember skills under `/tmp/ar-mcp-real-validate-02/.codex/skills/agents-remember-md`.
- Additional isolated settings were used for memory-topology fixtures:
  - Existing external memory: `/tmp/ar-mcp-existing-memory-validate/.codex/mcp/settings.json`
  - Repo-local memory: `/tmp/ar-mcp-repolocal-memory-validate/.codex/mcp/settings.json`

---

## MCP Tool Evidence

All Agents Remember workflow operations below were executed by child Codex sessions as MCP tool calls. CLI/shell was used only for fixture setup and post-run inspection.

| Transcript | Tool path covered | Result |
| --- | --- | --- |
| `/tmp/ar-mcp-real-validate-02/server-info.jsonl` | `server_info` | Passed; proved child session used the isolated PyPI MCP config. |
| `/tmp/ar-mcp-real-validate-02/s1-base.jsonl` | `runtime_install`, `skills_install`, `memory_init`, `context_packet`, `memory_baseline_status` | Mixed; `runtime_install` failed before memory root existed, other calls passed. |
| `/tmp/ar-mcp-real-validate-02/runtime-provider.jsonl` | `runtime_install` after memory init, `provider_status`, `provider_watchers` dry-run | Mixed; runtime succeeded after memory init, provider status showed running global/shared state. |
| `/tmp/ar-mcp-real-validate-02/provider-real-status.jsonl` | `provider_status`, `provider_watchers(action="status", dry_run=false)` | Passed non-mutating status; showed GrepAI contamination with unrelated projects. |
| `/tmp/ar-mcp-real-validate-02/baseline-adopt.jsonl` | `memory_baseline_status`, `memory_baseline_adopt` | Passed; new external memory adopted and ledgered. |
| `/tmp/ar-mcp-real-validate-02/chat-closeout.jsonl` | `context_packet`, `direct_closeout_preview`, `direct_closeout_apply` | Mixed; preview passed, apply blocked on missing README sidecar onboarding. |
| `/tmp/ar-mcp-real-validate-02/chat-closeout-onboarding.jsonl` | `direct_closeout_preview`, `direct_closeout_apply` after onboarding | Passed after onboarding metadata was added; preview missed metadata failure first. |
| `/tmp/ar-mcp-real-validate-02/light-task.jsonl` | Installed `w-02` skill use, task file creation, `direct_closeout_preview/apply` | Passed; temp skill visible, task file created, closeout completed. |
| `/tmp/ar-mcp-real-validate-02/worktree.jsonl` | Installed `c-09` skill use, `worktree_start/status/closeout/integrate/cleanup` | Passed for code/memory with provider setup skipped; provider-runtime cleanup not validated. |
| `/tmp/ar-mcp-existing-memory-validate/run.jsonl` | Existing external memory clone + `memory_baseline_adopt` | Passed; existing cloned memory detected and adopted. |
| `/tmp/ar-mcp-repolocal-memory-validate/run-with-onboarding.jsonl` | Repo-local `ar-memory/` context/baseline | Failed; resolver found internal memory but context/baseline routed external. |

---

## Integrity Matrix

| Path | MCP evidence | Result | Docs consequence |
| --- | --- | --- | --- |
| PyPI MCP server visibility | `server_info` from child Codex reports temp config path | pass | Happy-path validation can say “ask the model to call `server_info`.” |
| PyPI skill install visibility in Codex | Temp `CODEX_HOME` prompt input includes installed Agents Remember skills | pass | Docs must still mention restart/new session after skills install. |
| Runtime install before memory init | `runtime_install` failed with missing GrepAI memory root | blocked | Happy path must initialize memory first or implementation must tolerate missing roots. |
| Runtime install after memory init | `runtime_install` dry-run and real install succeeded | pass | Docs can describe this order if product behavior is not changed. |
| New external memory init/adopt | `memory_init`, `memory_baseline_adopt` | pass with caveats | Docs need mention transient `master` warning or fix it. |
| Existing external memory from Git | cloned existing memory, then `context_packet` and `memory_baseline_adopt` | pass | Docs can teach clone/install then adopt baseline. |
| Repo-local `ar-memory/` from Git | `resolve_context` internal, `context_packet` external, baseline failed | blocked | Do not document repo-local restore as happy path until fixed. |
| Provider status | `provider_status`, `provider_watchers(... dry_run=false)` | blocked for mutation | Docs cannot promise isolated provider up/down yet. |
| Chat/direct closeout | README edit plus onboarding, `direct_closeout_preview/apply` | pass with caveats | Docs must make onboarding-before-closeout explicit. |
| Light task | Installed `w-02`, task file, README/onboarding, `direct_closeout_preview/apply` | pass | Docs can describe light task path after noting approval gates. |
| Worktree core lifecycle | Installed `c-09`, `worktree_start`, closeout, integrate, cleanup | pass with providers skipped | Docs can describe code/memory lifecycle, but provider isolation needs fix/limitation. |
| Worktree provider lifecycle/cleanup | dry-run provider preparation only | blocked | Do not promise provider cleanup until isolated provider runtime is safely tested. |

---

## Findings Updates

- Confirmed through MCP: F-001, F-002, F-006, F-009, F-010, F-011, F-012, F-013, F-014, F-015.
- Partially cleared through MCP: F-003 code/memory cleanup works, but provider-runtime cleanup remains untested.
- Reclassified through MCP: F-004 is not the original sandbox-PID issue; it is now blocked by shared provider state.
- Retested/cleared method issue: F-008 pass 02 used actual child Codex MCP tool calls.
