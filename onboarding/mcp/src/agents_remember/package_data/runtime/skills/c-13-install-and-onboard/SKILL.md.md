# c-13-install-and-onboard/SKILL.md

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

The installed interview now names `dispatch_agent` as the sole public spawn transaction. A
plane-hosted seat is recognized by injected plane identity and authorized by its current seat plus
direct-child scope; an identity-free ambient launcher is authorized by canonical target-document
resolution plus role altitude. The public request never chooses caller kind or supplies caller
identity. Both modes consume the same settings profile and private creation/readiness/brief/rollback
pipeline, while a plane refusal never retries as ambient. The internal session primitive is not
caller guidance. Ordinary ambient bootstrap targets the sprint architect; only an explicit
developer-declared task-seat takeover targets another named role at its canonical altitude.

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
coordinator scaffold exists and the host step runs; the shared
`<coordinationRoot>/system/settings.json` file belongs to starter/setup (the
renderer writes it when absent) and this step never writes that authority; (2) the AGENTIC-SETTINGS INTERVIEW (new with 260703-L13,
between the old Stages 1 and 2): walk the developer through the four knob
families — gate delegation posture (with the explicit boot-snapshot
restart note), loop defaults, concurrency caps, and harness preference
(registry ids claude/codex/pi) — and edit
`<coordinationRoot>/system/settings.json` with their answers, leaving skipped
families at the built-in absent-knob defaults; repo-local `<repo>/system/settings.json`
overrides are offered only on request, never created unprompted; (3) ask
whether to scaffold a new memory repo or use an existing one, unless memory
already resolves cleanly; (4) hand off to `c-03-repo-bootstrap` only when a
new memory repo was scaffolded; (5) configure providers (start/refresh
watchers) so they actually index the configured code and memory. Stage 0's
settings-sane check also reports whether the shared agentic settings file
exists, and the report result gains an agentic-settings line (interviewed vs
built-in defaults, with the file path). `skills_install()` is explicitly not part
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


## CCR-R12@v5 Transaction Boundary

Repository certification profiles and full code-quality operations are explicit setup requests made only when the developer asks for them. Their absence does not block routine closeout or integration, and they are not curation; this installer only reports configured setup and delegates any requested certification or memory/bootstrap work to its owning workflow, while curation is always complete on every leaf and its result travels with the handoff.

## Evidence

### Docs References

Harness-native setup details now live in the install guides and starter packages.

No external documentation is needed to prove this repository-local skill contract.

### Repo-Internal References

- The skill starts only after the harness package is copied and rendered, MCP is wired, and the harness has restarted once; package files own skills, hooks, rules, instructions, MCP templates, settings templates, and render scripts. [1]
- Stage 0 checks MCP reachability, package presence, settings, runtime state, provider prerequisites when enabled, and topology consistency, but does not install or repair hooks. [2]
- Stage 1 runs/verifies `runtime_install()` and explicitly avoids `skills_install()` during package-based first-run setup. [3]
- Stage 2 interviews the developer on the agentic settings families, writes the seeded global file, and verifies the two caller kinds of the public dispatch transaction. [4]
- Stage 3 (new under CCR-R22@v1, commit `685f83c44055`) authors, validates, and registers one repository-owned Gate 1-4 certification profile per code-committing repository (`repositories.<repo-id>.certificationProfile`) against `docs/reference/repository-certification-profile.md`; Stage 4/5 delegate memory init, existing-memory adoption, and bootstrap to the existing skills; Stage 6 configures providers. [5]
- The `provider_watchers` tool Stage 5 drives: it accepts `status`/`start`/`stop`/`restart`/`invalidate-indexes`/`shutdown-all`, and the `action="refresh"` this SKILL.md still names now raises a `ValueError` directing callers to `restart` (watchers only, indexes preserved) or `invalidate-indexes` (full re-embed). [6]
- The starter/setup renderer that writes the shared coordination settings file when it is absent; the removed install-side seed writer is historical. [7]

### Cross-Repo References

No sibling repository evidence is needed for this skill.

No meaningful cross-repo references found.

## 260921-ICR-L27 Setup Also Reaches The Knowledge Foundation, And It Stops Reporting Ready Without It

`260921-ICR-L27` (`ICR-R27@v1`) makes the **knowledge foundation** a named part of this skill's setup
sequence rather than something a first run silently omits. Stage 5 becomes *Bootstrap, The Knowledge
Foundation, Then The First Baseline* with three parts, and only its onboarding and baseline halves are
conditional on a newly scaffolded memory repo: the knowledge half applies to **both** memory-repo
answers, because an existing memory repo is exactly the case that can have Markdown onboarding and no
knowledge database.

The skill now reads the state first — `memory_init` returns a `knowledge` block naming where the
repository's foundation lives and what a read of that location finds now, and
`agents-remember knowledge-bootstrap --repo <repo_id> --status` reports the same location read-only — and
runs the foundation step when the location is `not-recorded`. An `unusable` location is reported with its
code and path and repaired before anything is written to it, because the writer refuses that destination
by name rather than overwriting it. The report gains the foundation as its own numbered line, and the
closing verdict must state the foundation's state rather than declaring a repository ready without it.

**The seat is named correctly, and that is deliberate.** This skill never names a role the opener will not
admit: a session opened for the curator with no task document is refused (`task-binding-required`), so the
authoring is handed on as `c-14-knowledge-bootstrap` states — the taskless bootstrap seat before a task
exists, or a curator opened on a task document. The skill delegates the foundation to `c-14` and its own
stages never author knowledge records, never invent records to make setup look finished, and never create
a development leaf, worktree or enclosure to give the writer an argument list it does not need.

**This card describes a generated copy**, propagated from `skills/c-13-install-and-onboard/SKILL.md` by
`scripts/sync-skills.py` into this package-owned copy and the eight harness starter packages.

## 260928-MIK-L96 The install brings the host

The installed skill's preflight checks that the shared settings name a host, its runtime stage says that `runtime_install` brings the host and how to read the host part, and its report has a host line and ends with the one start. No step tells the user to run the provision as part of an install; the terminal provision is the explicit transition.

- The package copy of the install skill. [8]
