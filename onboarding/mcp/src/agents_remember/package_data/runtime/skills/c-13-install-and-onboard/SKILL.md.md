# c-13-install-and-onboard/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-09T12:04+02:00                     |
| lastVerifiedCommitHash | `04f78993c54ef6f98773b0208e66e97d19686be8` |
| lastVerifiedCommitDate | 2026-07-09T12:35:59+02:00|

## Purpose

`c-13-install-and-onboard` skill is the post-wiring setup orchestration skill.
After the developer copies and renders a harness starter package, wires the MCP
server, and restarts the harness once, this skill verifies/runs
`runtime_install`, interviews the developer on the agentic orchestration
settings (260703-L13), sets up or adopts memory, bootstraps onboarding when
needed, and configures providers.

## Code Commentary

### Logic

L13 review follow-up (L13R-2): Stage 2's gate-delegation item now states GLOBAL file only — the loader refuses it repo-locally, so the interview can never imply a per-repo gate posture.

260703-L16: Stage 2 item 4 grew from "harness preference" to the full knob interview — per-role
`orchestration.roles` AND per-level `orchestration.rolesPerLevel` (leaf|master|portfolio tiered
economics), harness values as builtin ids OR developer-defined `orchestration.harnesses` entries,
the per-harness dispatch-time effort validation (claude's flag set + session-level `ultracode`),
and the never-validated free-form escape hatch (`launchArgs`/`sessionCommands`/`promptKeywords`,
recorded in spawn provenance) — pointing at `docs/reference/harnesses.md` as the spawn-surface
manual. HFX2-L10 clarifies the interview's authority boundary: ordinary spawning seats cannot pass
`harness`/`model`/`effort`, direct launch/session spend controls, or harness-native spend/endpoint
env keys directly; settings are the spend surface.

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

The five-stage sequence is now: (1) run or verify `runtime_install()` so the
coordinator scaffold exists (it also seeds the global agentic settings file
copy-if-missing); (2) the AGENTIC-SETTINGS INTERVIEW (new with 260703-L13,
between the old Stages 1 and 2): walk the developer through the four knob
families — gate delegation posture (with the explicit boot-snapshot
restart note), loop defaults, concurrency caps, and harness preference
(registry ids claude/codex/pi) — and edit
`<coordinationRoot>/system/settings.json` with their answers, leaving skipped
families at the seeded defaults; repo-local `<repo>/system/settings.json`
overrides are offered only on request, never created unprompted; (3) ask
whether to scaffold a new memory repo or use an existing one, unless memory
already resolves cleanly; (4) hand off to `c-03-repo-bootstrap` only when a
new memory repo was scaffolded; (5) configure providers (start/refresh
watchers) so they actually index the configured code and memory. Stage 0's
settings-sane check also reports whether the global agentic settings file
exists, and the report result gains an agentic-settings line (interviewed vs
seeded defaults, with the file path). `skills_install()` is explicitly not part
of package-based first-run setup because starter packages already include
harness-discoverable skills; it remains only a maintenance/manual option. The
report result similarly avoids any hook-restart instruction because hooks are
copied before this skill runs.

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
| Stage 2 interviews the developer on the agentic settings families and writes the global file seeded by `runtime_install`. | L125-L165 | [`c-13-install-and-onboard` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md) |
| Stage 3/4 delegate memory init, existing-memory adoption, and bootstrap to the existing skills rather than reimplementing them. | L167-L194 | [`c-13-install-and-onboard` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md) |
| Stage 5 starts/refreshes provider watchers and verifies indexing. | L196-L216 | [provider_tools.py](agents-remember/mcp/src/agents_remember/controllers/provider_tools.py) |
| The install-side seeding the interview builds on (copy-if-missing global file). | seed_agentic_settings | [runtime.py](agents-remember/mcp/src/agents_remember/install/runtime.py) |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 (spawn settings authority): Stage 2's knob interview now
  says `orchestration.spawn.harness` is the fallback when no role/level knob supplies a harness and
  that ordinary spawned seats cannot pass harness/model/effort, launch/session spend controls, or
  harness-native spend/endpoint env keys directly. Sync-propagated bundle copy of the canonical
  skill. Verification metadata pinned until closeout stamps the 260707-HFX2-L10 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): Stage 2 item 4 now interviews the
  full knob surface (roles + rolesPerLevel, orchestration.harnesses extensibility, per-harness
  effort vocabularies, the free-form escape hatch) and references the `docs/reference/harnesses.md`
  manual. Sync-propagated bundle copy of the canonical skill. Verification metadata pinned until
  closeout stamps the L16 commit.

- 2026-07-06T23:45+02:00 — L13 adversarial-review follow-up (L13R-2): Stage 2 gate-delegation item marked global-layer only. Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T22:54+02:00 — 260703-L13 (settings unification): the agentic-settings interview
  joins as Stage 2 (gate delegation posture, loop defaults, concurrency caps, harness
  preference; global file at `<coordinationRoot>/system/settings.json`, repo-local overrides
  on request only), the later stages renumber 3/4/5, Stage 0's settings check reports the
  global file, and the report gains the agentic-settings line. Sync-propagated bundle copy of
  the canonical `skills/c-13-install-and-onboard/SKILL.md`. Verification metadata pinned
  until closeout stamps the L13 commit.

- 2026-06-06T18:42+02:00: Updated after c-13 clarified that rendering can use the convenience script or manual path/repository/hook-command placeholder replacement. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T18:19+02:00: Updated after c-13 clarified the copied package renderer contract: one explicit `--repo` list and inferred workspace root. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T16:45+02:00: Updated after c-13 switched its prerequisite from manual placeholder replacement to running the copied package's `render-starter` script, and after its preflight language corrected the legacy `jq` misconception. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-03T18:58+02:00: Reframed the install-and-onboard skill around package-first setup: starter packages own skills/hooks/rules/instructions/MCP templates; this skill runs after one harness restart, verifies/runs `runtime_install`, sets up/adopts memory, bootstraps when needed, and configures providers without calling `skills_install` or installing hooks. Verification metadata stays pinned until closeout.
- 2026-06-02T16:35+02:00: Second batch (install-location defaults) — documented the new workspace-first **Install Locations** section (explicit per-target defaults rooted at `<workspace>`, never the home directory; accept-or-override prompts; `ar-coordination/` the one constant) and the shortened MANDATORY-FIRST-ACTION directive. fix/skill-ref-naming-and-grepai-status branch; verification pinned until closeout.
- 2026-06-02T04:25+02:00: Replaced the "chat / W-02 light / W-01 heavy" routing line with L-01's build-mode (read-only exit / chat build / W-02 light task) after W-01 retirement. L-01 series, Sub-task B/S6, mcp 1.1.0.
- 2026-05-30T21:51+02:00: Documented the hook-activation restart guidance added in the 0.9.x run — a freshly installed context-injecting start hook activates only on the next session, a distinct restart from the post-`skills_install` one. Verified against `57944df`.
- 2026-05-29T20:25+02:00: Reviewed for the act-by-default `dry_run` flip — `c-13-install-and-onboard` skill install/provider guidance now models preview-first (`dry_run=true`) then the real run for `runtime_install`/`skills_install`/`provider_watchers`.
- 2026-05-29T13:22+02:00: Created with the `c-13-install-and-onboard` skill install-and-onboard orchestration skill (replaces the reverted scripted start_hook_install MCP tool with a model-driven skill stage). Metadata pending closeout refresh.
