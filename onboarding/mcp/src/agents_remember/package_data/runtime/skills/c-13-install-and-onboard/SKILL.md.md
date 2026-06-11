# c-13-install-and-onboard/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-06T18:42+02:00                     |
| lastVerifiedCommitHash | `44012225994debc1bd7e196f87dc5fc314943f4e` |
| lastVerifiedCommitDate | 2026-06-08T09:05:36+02:00|

## Purpose

`c-13-install-and-onboard` skill is the post-wiring setup orchestration skill.
After the developer copies and renders a harness starter package, wires the MCP
server, and restarts the harness once, this skill verifies/runs
`runtime_install`, sets up or adopts memory, bootstraps onboarding when needed,
and configures providers.

## Code Commentary

### Logic

The skill starts with a package-first contract: harness-native files are already
the copied and rendered starter package's responsibility. Rendering can be done
with the package-local `render-starter` convenience script, which uses an
explicit `--repo` list while the copied harness folder supplies the workspace
root, or by manually replacing path, repository, and hook-command placeholders.
Stage 0 preflight
checks that the MCP is reachable, the harness package appears present, settings
paths are sane, runtime state is known, provider prerequisites are understood
when providers are enabled, and memory topology is consistent. It does not check
legacy hook prerequisites such as `jq`, because hook and instruction files are
part of the copied, rendered harness package and this skill no longer installs
them.

The four-stage sequence is now: (1) run or verify `runtime_install()` so the
coordinator scaffold exists; (2) ask whether to scaffold a new memory repo or use
an existing one, unless memory already resolves cleanly; (3) hand off to
`c-03-repo-bootstrap` only when a new memory repo was scaffolded; (4) configure
providers (start/refresh watchers) so they actually index the configured code
and memory. `skills_install()` is explicitly not part of package-based first-run
setup because starter packages already include harness-discoverable skills; it
remains only a maintenance/manual option. The report result similarly avoids any
hook-restart instruction because hooks are copied before this skill runs.

### Conventions

Model-driven by design: there is no MCP tool and no hardcoded per-harness
installer. A capable harness verifies and uses the copied package files rather
than creating them during first-run setup. The
skill delegates memory init to the `c-00-initialize-memory-repo` skill, bootstrap to the `c-03-repo-bootstrap` skill, baseline adoption to
the `c-10-adopt-memory-baseline` skill, and context resolution to the `c-08-ar-coordination-context-resolver` skill.

### Invariants And Boundaries

- It must not scaffold a memory repo without asking unless memory already exists
  and resolves cleanly.
- It must not install, overwrite, or invent harness hooks, rules, instruction
  files, skills, or MCP registration files during first-run setup.
- It must not call `skills_install()` as part of the package-based first-run
  path.
- It orchestrates and reports; it does not reimplement the skills it delegates to.

### Todos

No open file-local todos.

### Docs References

Harness-native setup details now live in the install guides and starter packages.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external documentation is needed to prove this repository-local skill contract. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The skill starts only after the harness package is copied and rendered, MCP is wired, and the harness has restarted once; package files own skills, hooks, rules, instructions, MCP templates, settings templates, and render scripts. | L8-L22; L25-L42 | [`c-13-install-and-onboard` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md) |
| Stage 0 checks MCP reachability, package presence, settings, runtime state, provider prerequisites when enabled, and topology consistency, but does not install or repair hooks. | L63-L95 | [`c-13-install-and-onboard` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md) |
| Stage 1 runs/verifies `runtime_install()` and explicitly avoids `skills_install()` during package-based first-run setup. | L97-L116 | [`c-13-install-and-onboard` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md) |
| Stage 2/3 delegate memory init, existing-memory adoption, and bootstrap to the existing skills rather than reimplementing them. | L118-L145 | [`c-13-install-and-onboard` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md) |
| Stage 4 starts/refreshes provider watchers and verifies indexing. | L147-L167 | [provider_tools.py](agents-remember/mcp/src/agents_remember/controllers/provider_tools.py) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-06T18:42+02:00: Updated after c-13 clarified that rendering can use the convenience script or manual path/repository/hook-command placeholder replacement. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T18:19+02:00: Updated after c-13 clarified the copied package renderer contract: one explicit `--repo` list and inferred workspace root. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T16:45+02:00: Updated after c-13 switched its prerequisite from manual placeholder replacement to running the copied package's `render-starter` script, and after its preflight language corrected the legacy `jq` misconception. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-03T18:58+02:00: Reframed the install-and-onboard skill around package-first setup: starter packages own skills/hooks/rules/instructions/MCP templates; this skill runs after one harness restart, verifies/runs `runtime_install`, sets up/adopts memory, bootstraps when needed, and configures providers without calling `skills_install` or installing hooks. Verification metadata stays pinned until closeout.
- 2026-06-02T16:35+02:00: Second batch (install-location defaults) — documented the new workspace-first **Install Locations** section (explicit per-target defaults rooted at `<workspace>`, never the home directory; accept-or-override prompts; `ar-coordination/` the one constant) and the shortened MANDATORY-FIRST-ACTION directive. fix/skill-ref-naming-and-grepai-status branch; verification pinned until closeout.
- 2026-06-02T04:25+02:00: Replaced the "chat / W-02 light / W-01 heavy" routing line with L-01's build-mode (read-only exit / chat build / W-02 light task) after W-01 retirement. L-01 series, Sub-task B/S6, mcp 1.1.0.
- 2026-05-30T21:51+02:00: Documented the hook-activation restart guidance added in the 0.9.x run — a freshly installed context-injecting start hook activates only on the next session, a distinct restart from the post-`skills_install` one. Verified against `57944df`.
- 2026-05-29T20:25+02:00: Reviewed for the act-by-default `dry_run` flip — `c-13-install-and-onboard` skill install/provider guidance now models preview-first (`dry_run=true`) then the real run for `runtime_install`/`skills_install`/`provider_watchers`.
- 2026-05-29T13:22+02:00: Created with the `c-13-install-and-onboard` skill install-and-onboard orchestration skill (replaces the reverted scripted start_hook_install MCP tool with a model-driven skill stage). Metadata pending closeout refresh.
