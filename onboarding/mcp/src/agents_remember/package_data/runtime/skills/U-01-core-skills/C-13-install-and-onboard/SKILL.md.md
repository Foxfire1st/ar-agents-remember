# C-13-install-and-onboard/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-13-install-and-onboard/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T13:22+02:00                     |
| lastVerifiedCommitHash | `421e27200a2fcd1156732c83de1af94fc08250bc` |
| lastVerifiedCommitDate | 2026-05-29T14:12:49+02:00|

## Purpose

C-13 is the post-scaffolding install orchestration skill. After the MCP does the
deterministic scaffolding (`runtime_install`, `skills_install`), C-13 leads the
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
`C-03-repo-bootstrap` only when a new memory repo was scaffolded; (4) configure
providers (start/refresh watchers) so they actually index the code and memory,
since `runtime_install` builds the runtimes but they index nothing until pointed
at repos. It carries the directive text and a per-harness routing table
(Claude Code / Codex / Pi / OpenClaw / Antigravity inject; Cursor / Copilot /
Hermes use their native instructions file).

### Conventions

Model-driven by design: there is no MCP tool and no hardcoded per-harness
installer — a capable harness writes the right config in the right place. The
skill delegates memory init to `C-00`, bootstrap to `C-03`, baseline adoption to
`C-10`, and context resolution to `C-08`.

### Invariants And Boundaries

- It must not scaffold a memory repo without asking, and must not assume a start
  hook is supported without checking the harness.
- It must not fabricate a harness hook format; when a format is unconfirmed it
  falls back to the instructions file and says so.
- It orchestrates and reports; it does not reimplement the skills it delegates to.

### Todos

Confirm the Antigravity hook format from current docs so Stage 1 can install a
real hook there instead of falling back to its instructions file. Wire C-13 into
the install docs / coordinator routing once the flow stabilizes.

### Docs References

The Claude Code hook pattern is documented in the install guide.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Claude Code SessionStart hook worked example (directive file + settings.json merge). | n/a | [docs/install/claude-code.md](agents-remember-md/docs/install/claude-code.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Stage 2/3 delegate memory init and bootstrap to these skills. | L88-L116 | [C-00 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-00-initialize-memory-repo/SKILL.md) |
| Existing-memory adoption is delegated to baseline adoption. | L97-L101 | [C-10 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/U-01-core-skills/C-10-adopt-memory-baseline/SKILL.md) |
| Stage 4 starts/refreshes provider watchers and verifies indexing. | L118-L139 | [provider_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/provider_tools.py) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-29T13:22+02:00: Created with the C-13 install-and-onboard orchestration skill (replaces the reverted scripted start_hook_install MCP tool with a model-driven skill stage). Metadata pending closeout refresh.
