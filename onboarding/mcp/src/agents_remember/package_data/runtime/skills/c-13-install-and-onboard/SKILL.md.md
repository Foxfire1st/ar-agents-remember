# c-13-install-and-onboard/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-11T15:20+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../../../../../overview.md`            |

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

`c-13-install-and-onboard` skill is the post-wiring setup orchestration skill.
After the developer copies and renders a harness starter package, wires the MCP
server, and restarts the harness once, this skill verifies/runs
`runtime_install`, interviews the developer on the agentic orchestration
settings (260703-L13), sets up or adopts memory, bootstraps onboarding when
needed, and configures providers.

## Code Commentary

### 260714-ACPUI-L2 Native Launch Interview

Stage 2 no longer teaches a static builtin model/effort vocabulary or maps a normalized effort to
a pasted command. A native role entry must provide a complete harness/model/effort selection from
the adapter's token-free per-install/account advertisement, with effort chosen from the selected
model and Pi using the exact provider-qualified model key. The native adapter validates and applies
that selection through its launch channel before work begins. `launchArgs`, `sessionCommands`, and
`promptKeywords` remain an explicit user-authored escape hatch and are never synthesized from the
normalized selection.

### Logic

L13 review follow-up (L13R-2): Stage 2's gate-delegation item now states GLOBAL file only — the loader refuses it repo-locally, so the interview can never imply a per-repo gate posture.

260703-L16 originally grew Stage 2 item 4 from "harness preference" to the full knob interview — per-role
`orchestration.roles` AND per-level `orchestration.rolesPerLevel` (leaf|master|portfolio tiered
economics), harness values as builtin ids OR developer-defined `orchestration.harnesses` entries,
and the never-validated free-form escape hatch (`launchArgs`/`sessionCommands`/`promptKeywords`,
recorded in spawn provenance). ACPUI-L2 supersedes that original static-vocabulary description for
builtins with dynamic model-gated advertise plus native launch application, while settings-defined
non-native mappings stay explicit. The interview points at `docs/reference/harnesses.md` as the
spawn-surface manual. HFX2-L10 clarifies the authority boundary: ordinary spawning seats cannot pass
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

## Docs References

Harness-native setup details now live in the install guides and starter packages.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is needed to prove this repository-local skill contract. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The skill starts only after the harness package is copied and rendered, MCP is wired, and the harness has restarted once; package files own skills, hooks, rules, instructions, MCP templates, settings templates, and render scripts. | `# c-13-install-and-onboard Install And Onboard` | mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md:6-273 |
| Stage 0 checks MCP reachability, package presence, settings, runtime state, provider prerequisites when enabled, and topology consistency, but does not install or repair hooks. | `## Stage 0 - Preflight` | mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md:67-103 |
| Stage 1 runs/verifies `runtime_install()` and explicitly avoids `skills_install()` during package-based first-run setup. | `## Stage 1 - Runtime Scaffold`, `runtime_install`, `skills_install` | mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md:104-123 |
| Stage 2 interviews the developer on the agentic settings families and writes the global file seeded by `runtime_install`. | `runtime_install` | mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md:125-165 |
| Stage 3/4 delegate memory init, existing-memory adoption, and bootstrap to the existing skills rather than reimplementing them. | `## Stage 3 - Memory Repo: Ask Scaffold Vs Existing`, `## Stage 4 - Bootstrap` | mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md:187-215 |
| The `provider_watchers` tool Stage 5 drives: it accepts `status`/`start`/`stop`/`restart`/`invalidate-indexes`/`shutdown-all`, and the `action="refresh"` this SKILL.md still names now raises a `ValueError` directing callers to `restart` (watchers only, indexes preserved) or `invalidate-indexes` (full re-embed). | "def provider_watchers_tool("; "if action == \"refresh\":"; "if action not in {\"status\", \"start\", \"stop\", \"restart\", \"invalidate-indexes\", \"shutdown-all\"}:"; "if action in {\"start\", \"restart\", \"invalidate-indexes\"}:" | mcp/src/agents_remember/application/provider_tools.py:50-73 |
| The install-side seeding the interview builds on (copy-if-missing global file). | `seed_agentic_settings` | mcp/src/agents_remember/install/runtime.py:164-180 |

## Cross-Repo References

No sibling repository evidence is needed for this skill.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-11T15:20+02:00 — Re-anchored provider-watcher vocabulary and the removed `refresh`
  behavior to the exact declaration and validation branches.
- 2026-08-03T03:59:59+02:00 — Curated 13 citation findings (6 table rows, 1 prose citation, 6 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation and rewrote
  its claim. The row's `L196-L216` were SKILL.md stage-heading line numbers carried onto a
  `provider_tools.py` link, so they never pointed at that file's material; the row now cites
  `provider_watchers_tool` at `provider_tools.py` L47-L86. Reading it showed the claim was also
  false: the tool no longer accepts `action="refresh"` (it raises and points at `restart` /
  `invalidate-indexes`), while this SKILL.md's Stage 5 still instructs `refresh`: cit:([`## Stage 5 - Configure Providers To Index`], mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md:216-240). The
  row now states the tool's real action vocabulary and names that drift instead of asserting a
  refresh path that fails.

- 2026-07-15T23:16+02:00 — 260714-ACPUI-L2 curator: updated the packaged installer interview to
  require complete dynamically advertised native selections, exact Pi provider identity, and
  native launch application; removed the obsolete static Claude/paste teaching while preserving
  explicitly user-authored free-form commands. Added and final-audited the nearest MCP governing
  overview backlink. Verification metadata remains pinned until closeout stamps the L2 code commit.

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
