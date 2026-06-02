# mcp/README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/README.md`                            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T16:35+02:00                     |
| lastVerifiedCommitHash | `dc25f5a63de359926985c925096aad9019968bf4` |
| lastVerifiedCommitDate | 2026-06-02T18:31:01+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`mcp/README.md` is the PyPI-facing README for the installable
`agents-remember-mcp` package and the de-facto pre-MCP bootstrap doc. It opens
with an agent-driven Quickstart, then documents requirements, install/run
(uvx-first), a starter settings block, harness registration, the first setup MCP
calls, and the high-level tool surface.

## Code Commentary

### Logic

The README is self-contained for the bootstrap so it works from the rendered
PyPI page without a source checkout. It leads with a three-step "ask your agent
to" Quickstart — (1) wire the MCP via
`uvx agents-remember-mcp --config <abs settings.json>` + author the settings +
restart; (2) `runtime_install` then `skills_install`; (3) run the
`c-13-install-and-onboard` skill — then gives `uvx` as the primary install/run
path (pip as alternative), an inline minimal starter `settings.json`, the harness
registration JSON (using `uvx`), the first setup MCP calls, and the tool surface.
Project-doc links are absolute GitHub URLs so they resolve from PyPI.

Beyond the Quickstart the README now carries the operational detail a first-run
needs: a **Settings file location** rule (place the settings file under the
harness registration folder in an `mcp/` subdirectory, because `skills_install`
infers its skill target from the sibling `skills/` of that `mcp` parent, with a
per-harness path table), an **Install Order And First Operations** section
spelling out the strict scaffolding → skills → providers ordering, the
`runnerIntegrityFailed` fast-fail if providers run before `runtime_install`, and
the `runtime_install` flags (`install_provider_deps`, `no_cache` to force a
from-scratch image rebuild), a per-harness setup-pages table, a
**skill-install** note (`skills_install` copies one flat folder per skill at
`<skill-root>/<name>/` — there is no layout option), an upgrade callout that
`timeoutCaps.providerSeconds` was renamed to `providerSetupSeconds` (old key
rejected with `ConfigError`; `providerSetupSeconds` caps only image build /
dependency install; `0` means unlimited), and a **Troubleshooting** section
(uvx index lag, `degraded` providers / Ollama recovery, and the git-identity
placeholder for memory/worktree commits). The settings guidance now also states the **workspace-first default**: `coordinationRoot` defaults to `<workspace>/ar-coordination/` and the settings file goes under `<workspace>/<harness-folder>/mcp/` — inside the workspace, never the user's home directory.

### Invariants And Boundaries

- Keep this README focused on the MCP package and its bootstrap, not the whole
  product manual.
- Keep it self-contained for pip/PyPI readers: inline the starter settings and
  use absolute GitHub URLs (no source-checkout-relative `../` links that 404 on
  the PyPI page).
- Keep the run command aligned with `agents_remember.mcp.server.main()`, which
  requires `--config`; both `uvx agents-remember-mcp` and the pip console command
  invoke it.
- Keep requirements practical and package-level: Python 3.11+, uv/pip, an
  MCP-capable harness, Git, and Docker (plus Ollama for the grepai embedder) only
  when provider tools are enabled.
- Keep the Settings file location guidance accurate: `skills_install` only finds
  a skill target when the settings file's parent directory is named `mcp`, so the
  README must keep telling users to place it under the harness registration folder
  (e.g. `.claude/mcp/`, `.codex/mcp/`), not loose in the workspace root.
- Keep the skill-install note correct: `skills_install` copies one flat folder
  per skill (`<skill-root>/<name>/`, matching the skill's lowercase `name`) and
  has **no layout option** (the `tree`/`flat` `layout` input was removed in
  2.0.0). For harnesses whose skill root isn't the inferred
  `<harness-root>/skills/`, set `harnessSkillRoot`. Drift here (reintroducing a
  `layout=` arg) silently breaks skill-install docs.
- Keep the install-order rationale intact: scaffolding → skills → providers.
  `runtime_install` builds provider images (step 2); indexing only *starts* in
  step 3, so "providers last" means indexing, not image builds.
- Keep the benchmark-safety callout intact: `codex_benchmark_prepare`/
  `codex_benchmark_run` are opt-in, refused unless settings set
  `"benchmarksEnabled": true`; a real run (`dry_run=false`) clones third-party
  repos and runs the Codex CLI, and `codex_sandbox` defaults to Codex's `default`
  sandbox with `danger-full-access` reserved for trusted local runs (full host
  access). The README must keep warning that benchmark execution runs untrusted
  code.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The run command requires an absolute `--config` path and rejects coordinator `system/settings.json`; `uvx agents-remember-mcp` and the pip console script both call `server.main()`. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py); [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| The PyPI package declares the `agents-remember-mcp` console script and uses this README as project metadata. | [pyproject.toml](agents-remember-md/mcp/pyproject.toml) |
| The Quickstart hands post-scaffolding setup off to the `c-13-install-and-onboard` skill install-and-onboard skill. | [`c-13-install-and-onboard` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md) |
| The tool surface the README summarizes is exposed by the server/payload layer and catalogued in the tool reference. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py); [mcp-tools.md](agents-remember-md/docs/reference/mcp-tools.md) |
| The `providerSeconds` → `providerSetupSeconds` rename and the fail-loud `ConfigError` on the old key are enforced in MCP config. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| The `runtime_install` flags the README documents (`install_provider_deps`, `no_cache`) and the runner-integrity manifest behind `runnerIntegrityFailed` are owned by the install/runtime layer. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |

## Update History

- 2026-06-02T16:35+02:00: Second batch (install-location defaults) — documented the workspace-first settings default: `coordinationRoot` at `<workspace>/ar-coordination/` and the settings file under `<workspace>/<harness-folder>/mcp/`, inside the workspace and never the user's home directory. fix/skill-ref-naming-and-grepai-status branch; verification pinned until closeout.
- 2026-06-02T11:00+02:00: Removed the stale `tree`/`flat` skill-layout language after confirming `skills_install` has no `layout` arg (removed in 2.0.0) — it copies one flat folder per skill at `<skill-root>/<name>/`. Updated the Logic note and the skill-install invariant; `README.md`, `docs/getting-started.md`, `docs/reference/mcp-tools.md`, and the per-harness install pages were corrected in the same pass (docs/** are outside file-level onboarding). Verification metadata stays pinned until closeout. fix/skills-install-layout-docs branch.
- 2026-05-31T12:30+02:00 — Captured the README's new benchmark-safety callout (1.0.0 review remediation): `codex_benchmark_prepare`/`codex_benchmark_run` are opt-in behind `benchmarksEnabled: true`, real runs run untrusted code, and `codex_sandbox` defaults to `default` with `danger-full-access` opt-in.
- 2026-05-30T21:22+02:00: Verified against `57944df` after the 0.9.0–0.9.4 run. Documented the README sections added since `412342847` — Settings file location (the `mcp`-parent rule that lets `skills_install` infer its target), Install Order And First Operations (scaffolding → skills → providers, `runnerIntegrityFailed`, `install_provider_deps`/`no_cache`), the `tree` vs `flat` skill-layout note, the `providerSeconds` → `providerSetupSeconds` rename, and Troubleshooting — and added matching invariants and references.
- 2026-05-29T14:15+02:00: Rewrote the README as a self-contained, uvx-first bootstrap — added the 3-step "ask your agent to" Quickstart (hands off to `c-13-install-and-onboard` skill), inlined a starter `settings.json`, switched project-doc links to absolute GitHub URLs, and linked the MCP tool reference. Metadata pending closeout refresh.
- 2026-05-28T15:52+02:00: Updated after the MCP package README added the canonical source checkout link.
- 2026-05-28T15:43+02:00: Created after the MCP package gained a dedicated README and `pyproject.toml` started using it as package metadata. Verification metadata remains pinned until closeout commits the source change.
