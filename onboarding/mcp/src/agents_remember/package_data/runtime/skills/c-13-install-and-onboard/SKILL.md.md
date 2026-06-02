# c-13-install-and-onboard/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T16:35+02:00                     |
| lastVerifiedCommitHash | `700ed5e9cc4549276226b6662eb8c9ff90739ee0` |
| lastVerifiedCommitDate | 2026-06-02T18:28:34+02:00|

## Purpose

`c-13-install-and-onboard` skill is the post-scaffolding install orchestration skill. After the MCP does the
deterministic scaffolding (`runtime_install`, `skills_install`), `c-13-install-and-onboard` skill leads the
model + developer through the remaining setup until the project is operational.

## Code Commentary

### Logic

The skill defines a Stage 0 preflight (verify prerequisites — MCP reachable and
the harness restarted, scaffolding present, settings sane, `jq` for the hook,
Docker/Ollama for providers, topology consistency — with a plain-language fix per
failure so a non-expert is never left with a silent half-install) plus a
four-stage sequence: (1) install a context-injecting
start-of-session/chat hook for the harness, or place the coordinator directive in
the harness's always-on instructions file when no injecting hook exists; (2) ask
whether to scaffold a new memory repo or adopt an existing one; (3) hand off to
`c-03-repo-bootstrap` only when a new memory repo was scaffolded; (4) configure
providers (start/refresh watchers) so they actually index the code and memory,
since `runtime_install` builds the runtimes but they index nothing until pointed
at repos. It carries the directive text and a per-harness routing table
(Claude Code / Codex / Pi / OpenClaw / Antigravity inject; Cursor / Copilot /
Hermes use their native instructions file). When a context-injecting start hook
is installed, Stage 1 now tells the developer it activates on the **next**
session (harnesses load and often snapshot session hooks at startup), so a
restart is required and it must be confirmed on the next session — a distinct
restart from the post-`skills_install` one.

The skill opens with an **Install Locations — Workspace-First Defaults** section: every artifact
(coordination root, skills, MCP settings, harness settings, hooks) has an explicit default rooted at
the `<workspace>` the harness was opened in — never the user's home directory — with `ar-coordination/`
the one harness-agnostic constant and the rest translated into each harness's own folder conventions,
each shown as an accept-or-override prompt before anything is written. These defaults govern
`coordinationRoot`/`workspaceRoot` in the MCP settings, the `install_root` for `skills_install`, and the
Stage 1 hook/settings paths. The injected directive was shortened to a blunt MANDATORY-FIRST-ACTION
block that forbids any repository work until `ar-coordination/AGENTS.md` and its `l-01` procedure are
read.

### Conventions

Model-driven by design: there is no MCP tool and no hardcoded per-harness
installer — a capable harness writes the right config in the right place. The
skill delegates memory init to the `c-00-initialize-memory-repo` skill, bootstrap to the `c-03-repo-bootstrap` skill, baseline adoption to
the `c-10-adopt-memory-baseline` skill, and context resolution to the `c-08-ar-coordination-context-resolver` skill.

### Invariants And Boundaries

- It must not scaffold a memory repo without asking, and must not assume a start
  hook is supported without checking the harness.
- It must not fabricate a harness hook format; when a format is unconfirmed it
  falls back to the instructions file and says so.
- It orchestrates and reports; it does not reimplement the skills it delegates to.

### Todos

Confirm the Antigravity hook format from current docs so Stage 1 can install a
real hook there instead of falling back to its instructions file. Wire `c-13-install-and-onboard` skill into
the install docs / coordinator routing once the flow stabilizes.

### Docs References

The Claude Code hook pattern is documented in the install guide.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Claude Code SessionStart hook worked example (directive file + settings.json merge). | n/a | [docs/install/claude-code.md](agents-remember-md/docs/install/claude-code.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Stage 2/3 delegate memory init and bootstrap to these skills. | L88-L116 | [`c-00-initialize-memory-repo` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-00-initialize-memory-repo/SKILL.md) |
| Existing-memory adoption is delegated to baseline adoption. | L97-L101 | [`c-10-adopt-memory-baseline` SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/c-10-adopt-memory-baseline/SKILL.md) |
| Stage 4 starts/refreshes provider watchers and verifies indexing. | L118-L139 | [provider_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/provider_tools.py) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-02T16:35+02:00: Second batch (install-location defaults) — documented the new workspace-first **Install Locations** section (explicit per-target defaults rooted at `<workspace>`, never the home directory; accept-or-override prompts; `ar-coordination/` the one constant) and the shortened MANDATORY-FIRST-ACTION directive. fix/skill-ref-naming-and-grepai-status branch; verification pinned until closeout.
- 2026-06-02T04:25+02:00: Replaced the "chat / W-02 light / W-01 heavy" routing line with L-01's build-mode (read-only exit / chat build / W-02 light task) after W-01 retirement. L-01 series, Sub-task B/S6, mcp 1.1.0.
- 2026-05-30T21:51+02:00: Documented the hook-activation restart guidance added in the 0.9.x run — a freshly installed context-injecting start hook activates only on the next session, a distinct restart from the post-`skills_install` one. Verified against `57944df`.
- 2026-05-29T20:25+02:00: Reviewed for the act-by-default `dry_run` flip — `c-13-install-and-onboard` skill install/provider guidance now models preview-first (`dry_run=true`) then the real run for `runtime_install`/`skills_install`/`provider_watchers`.
- 2026-05-29T13:22+02:00: Created with the `c-13-install-and-onboard` skill install-and-onboard orchestration skill (replaces the reverted scripted start_hook_install MCP tool with a model-driven skill stage). Metadata pending closeout refresh.
