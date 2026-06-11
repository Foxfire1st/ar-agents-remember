# Validation Pass 01: PyPI MCP Install And Workflow Integrity

**Task:** `260527_pypi-mcp-install-docs-overhaul`
**Started:** 2026-05-27T13:02
**Scope:** S1-S3 only: install/runtime/provider/memory/chat/light/worktree validation.

---

## Ground Rules

- Test workflows end to end before writing documentation.
- Record every defect or friction point in `findings.md`.
- Do not fix implementation defects during this pass unless the developer approves after findings review.
- Do not rewrite public docs during this pass.
- Correction after review: workflow integrity must be proven through real MCP tool calls from the harness/server path. Direct Python payload calls and CLI commands are only supporting evidence.

---

## Method Correction

This pass mixed three validation methods and originally over-stated several results:

| Method | What it proves | What it does not prove |
| --- | --- | --- |
| Real MCP tool call from the active conversation | Harness-visible MCP behavior for the configured current workspace | PyPI package behavior in the isolated install workspace unless that server is the one being used |
| Codex CLI commands such as `codex mcp add/list/get` | Harness registration file shape and server registration metadata | Tool visibility or tool execution through the model |
| Direct Python calls such as `*_payload(...)` or provider/worktree APIs | Package imports, controller behavior, and local source-level bugs | End-to-end MCP transport, harness process context, restart behavior, or model-mediated use |

The isolated PyPI workflow evidence below should be treated as package/API smoke evidence unless the row explicitly says it was invoked through MCP.

---

## Environment Baseline

Host tools observed during the pass:

| Requirement | Result |
| --- | --- |
| Python | `python3 --version` -> Python 3.12.3 |
| pip | `python3 -m pip --version` -> pip 24.0 |
| Git | `git --version` -> 2.43.0 |
| Docker | `docker --version` -> 29.4.2 |
| Docker Compose | `docker compose version` -> v5.1.3 |
| Codex | `codex --version` -> codex-cli 0.130.0 |
| uv | `uv --version` -> 0.11.8 |
| pipx | `pipx --version` -> 1.4.3 |

Package environment:

- Clean venv: `/tmp/ar-pypi-validate-venv`.
- Installed package: `agents-remember-mcp==0.1.0`.
- Installed dependency resolver selected `mcp==1.27.1`.
- Entrypoints verified: `agents-remember-mcp --help` and `python -m agents_remember.mcp --help`.

---

## Integrity Matrix

| Path | Evidence | Result | Docs consequence |
| --- | --- | --- | --- |
| Task-start context/drift | `context_packet(repo_id="agents-remember", include_providers=true)` and `drift_check(repo_id="agents-remember", detail_limit=50)` | pass: providers healthy, drift actionableCount=0 | Existing onboarding can be used as validation context. |
| PyPI install and tool list | Clean venv install plus direct `server_info_payload` | package smoke pass: 34 public tools reported by package code | Retest `server_info` through MCP before using as end-to-end proof. |
| Codex MCP registration | Isolated `HOME=/tmp/ar-codex-home codex mcp add/list/get` | pass for registration; visibility validation is docs-only | Docs need explicit restart/reload and “ask the model to call `server_info`” validation. See F-005. |
| Runtime scaffold install | Direct `runtime_install_payload(dry_run=true/false, include_benchmarks=false, install_provider_deps=false)` | package/API pass: runtime copied packaged coordinator/provider/skill files and wrote provider manifest | Retest through MCP before documenting as happy path. See F-008. |
| Skills install | Direct `skills_install_payload(layout=tree, dry_run=false, overwrite=true)` and tree/flat dry-runs with `overwrite=true` | package/API pass for install/refresh with overwrite; reinstall without overwrite errors | Retest through MCP; docs need first install vs refresh wording. See F-007 and F-008. |
| New external memory init | Direct `memory_init_payload(dry_run=true/false)` | package/API blocked: scaffold lacks `system/settings.json`; transient `master` branch before baseline | Retest through MCP after deciding fix path. See F-001, F-006, and F-008. |
| Baseline adoption for new external memory | Direct `memory_baseline_status_payload`, `memory_baseline_adopt_payload(dry_run=true/false)` | package/API pass after memory init: ledger created and memory branch ended on `main` | Retest through MCP before documenting. See F-008. |
| Existing external memory from Git | Local `git clone` of code repo and matching external memory repo into a new workspace | pass: context resolved external memory and baseline status `already-ledgered` | Docs can cover installing/cloning existing external memory, with drift caveats. |
| Repo-local `ar-memory/` from Git | Isolated repo with committed `ar-memory/` and no external memory, using direct payload calls | package/API blocked: resolver says internal, payload context/drift/quality force external | Retest through MCP after fixing/triaging. See F-002 and F-008. |
| Provider setup/status/watch | Direct `provider_status_payload`, `provider_watchers_payload(start/refresh, dry_run=true)`, `grepai_search_payload(dry_run=true)`, `cgc_symbol_search_payload(dry_run=true)` | package/API partial: dry-run planning and stopped-status reporting pass; true MCP watcher start is not yet validated | Validate the real MCP tool path first. See F-004 and F-008. |
| Provider integration tests | New `mcp/tests/test_pypi_workflow_integrity.py` | partial: GrepAI/CGC setup success/failure tests pass; defect expectation tests fail | Keep tests as executable repros for fix discussion. |
| Chat/direct closeout | Isolated code repo + external memory with README onboarding sidecar; direct `direct_closeout_preview_payload` then `direct_closeout_apply_payload` | package/API pass: preview requested commit approval; apply created code, memory-content, and ledger commits | Retest through MCP/model path before documenting chat closeout. See F-008. |
| Light/worktree lifecycle | Direct `worktree_start(skip_provider_setup=true)`, worktree closeout preview/apply, integrate dry-run/apply, cleanup | package/API partial: worktree and memory worktrees copied/closed/integrated; cleanup leaves provider runtime if present | Retest through MCP/model path; worktree docs need cleanup fix. See F-003 and F-008. |
| Worktree provider isolation | Direct `worktree_start(dry_run=true)` provider payload | package/API pass for planned CGC isolation: roots target code worktree and runtimeRoot under `worktree_group/provider-runtime`; GrepAI is skipped for worktree setup | Retest through MCP before documenting provider isolation. See F-008. |

---

## Validation Notes

### Package And Harness

- PyPI install initially failed inside the restricted sandbox due DNS, then succeeded with approved network escalation.
- The direct Python MCP stdio inspection timed out at `session.initialize`, but a minimal FastMCP test server timed out the same way. This is treated as a validation-method issue, not an Agents Remember product finding.
- Codex registration writes expected config:

```toml
[mcp_servers.agents-remember]
command = "/tmp/ar-pypi-validate-venv/bin/agents-remember-mcp"
args = ["--config", "/tmp/ar-pypi-workspace/.codex/mcp/settings.json"]
```

### Provider Results

- Provider status before start is clear: both providers are configured and stopped.
- Dry-run `provider_watchers(start)` plans GrepAI Postgres/Ollama/watcher and CGC FalkorDB/watcher Docker Compose commands.
- Dry-run `provider_watchers(refresh)` plans both GrepAI refresh and CGC refresh-all.
- Direct local `provider_watchers(start, dry_run=false)` from the Codex command sandbox returns the durable-namespace error. This was not a true harness MCP tool invocation, so it must not be treated as proof that MCP watcher start fails or requires a host-terminal workaround.

### Workflow Results

- New external memory path works only after baseline adoption. Before adoption, there is no ledger for worktree/direct closeout.
- Chat/direct closeout passes once the changed source has a matching onboarding sidecar. Without that, preview marks onboarding metadata as missing and apply would block.
- Worktree start with provider setup skipped created independent code and memory worktrees from the ledgered external memory.
- Worktree provider setup dry-run creates independent CGC settings under the worktree group and does not point CGC roots at the global source repo.
- Worktree cleanup removes code/memory worktrees and merged branches, but leaves worktree provider runtime state behind while still reporting cleanup completed.

### Test Results

Focused validation command:

```text
.venv/bin/python -m unittest mcp.tests.test_pypi_workflow_integrity -v
```

Result:

- 2 passing tests: GrepAI/CGC provider prepare dry-run success and CGC seed failure without refresh fallback.
- 3 failing tests matching confirmed findings: missing `system/settings.json`, repo-local `ar-memory/` ignored by `context_packet`, and provider runtime not removed during worktree cleanup.
