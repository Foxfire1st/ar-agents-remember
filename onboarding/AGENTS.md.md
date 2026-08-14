# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `AGENTS.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T16:10+02:00 |
| lastVerifiedCommitHash | `a89a6fc88d9330eb2749c87b3dcc3f6c4e46c4bd` |
| lastVerifiedCommitDate | 2026-08-14T12:44:51+02:00|

## Purpose

`AGENTS.md` is the repo-root operating contract for agents working on the
`agents-remember` source checkout. It now explicitly distinguishes this
source package from the installed coordination runtime and tells agents who
arrive through a workspace-level pointer to follow the installed
`ar-coordination/AGENTS.md` instead when they are working on a sibling
repository. It also points store, queue, append-only-log, and loop-over-store
changes at the resolved memory layer's stability/reclamation coding doctrine
before implementation.

## Code Commentary

### Logic

The current launcher contract is sprint-local rather than global. A developer-opened free chat
launches an architect seat that is bound to one qualified `repo/sprint/leaf` context; that
architect then launches the sprint's orchestrator, and the orchestrator launches managers inside
the same repository+sprint provenance. Named command seats do not fall back to a workspace-wide
architect or orchestrator identity. The dashboard and notifier can therefore host concurrent
sprints without cross-sprint custody, routing, or wake ownership.

The file starts by declaring that `agents-remember` is source package code,
not the live runtime after installation. It gives a fallback handoff for the
case where a workspace root includes this file while the actual target is a
sibling repository, then scopes normal resolver input for this checkout to
`code_repository_name = agents-remember`.

A `Start Here — Route By Role` section now sits where Task Format Routing used
to: sessions route by role through the `l-01-agent-lifecycles` skill — a spawned
agent (the `AR_SPAWN_ROLE` env var, or a role brief as first message) follows
its brief as its session start, and a developer-facing session is the
**architect**, running `skills/l-01-agent-lifecycles/roles/architect.md`
on the request → trust-checkpoint → reframe-research → decide → build → close
phase axis. The job type is a lens during reframe-research, and the build
decision at `decide` has two shapes — a research-only exit (no worktree, no task
file) or a durable `w-02-light-task-workflow` skill task; chat is never a build
route, so small code work takes the minimal artifact and larger work escalates
to a master + light sub-task series. The `tasks/AGENTS.md` collaboration
doctrine applies in the architect lifecycle's reframe-research phase.
The HFX-L6 role split keeps spawned roles on their briefs while making the
owner/developer-facing seat the architect; the backend orchestrator is no
longer the normal developer-facing lifecycle.
The memory section also carries a `Memory Retrieval Strategies` list — Semantics
(GrepAI), Relationship (cgc), and Intent (onboarding plus bounded source
confirmation) — that points to the same `c-04-retrieval-strategy-router` skill router.

The build-mode decision is the only task-format call; the former standalone
chat workflow is retired, and the chat build itself is retired with the
lifecycle convergence — every code change lives under an approved task
document. The memory section
keeps the `c-08-ar-coordination-context-resolver` skill, `context_packet` MCP tool, then `c-02-memory-quality-control` skill memory quality control gate and
points agents at the resolved memory layer's settings, tools, sources, and
optional coding guidelines rather than pretending the source checkout has active
root-level `system/` settings. Provider authority is stated directly as MCP
settings.

The source-layout section now records root `skills/` as the canonical skill
source tree and `scripts/sync-skills.py` as the repo helper that copies canonical
skills into the MCP package-data tree and every harness starter package. It also
records root `agents-md-files/`, `benchmarks/`, `providers/`, and `system/` as
canonical runtime asset folders and routes their MCP package-data refresh
through `scripts/sync-runtime.py`. It also records `scripts/harness/` as the single
source for the eight self-hosted harness starter packages (`.claude/`, `.codex/`,
`.cursor/`, `.github-vscode/` with `.vscode/`, `.hermes/`, `.openclaw/`, `.pi/`,
`.agents/`), refreshed with `python3 scripts/sync-harness.py`, and points at that
directory's `README.md` for which differences between harnesses are genuine requirements
and which files the generator does not manage. The MCP package-data skill and runtime
asset trees and the harness starter trees are explicitly generated, so agents should edit
root canonical folders first and run the relevant sync helper instead of editing
generated copies by hand — each generated harness file says so in a header comment, while
files a starter package owns alone (`.codex/config.toml`, `.cursor/hooks.json`) are edited
in place. The boundaries section keeps root instructions scoped to source-checkout
work, keeps installed coordinator instructions under `runtime/agents-md-files/`,
repeats the "edit root skills" rule, and adds the matching
runtime-asset and harness sync boundaries.

### Code Quality Instructions — Rewritten By 260731-EFA-L2

The code-quality section no longer says "run Ruff, Pyright, and Radon". It names the gate
command and what it does:

```text
python -m agents_remember.code_quality.check
```

The file states that this command is the accepting wrapper and takes **no path arguments**,
because its scope is
`git ls-files '*.py'` and narrowing what a gate certifies is how a gate stops meaning
anything. The pinned Dagger graph runs it exactly once at leaf closeout in targeted mode and
exactly once at master integration in full mode. Host hooks and GitHub PR validation are
deterministic non-test rails and cannot satisfy acceptance.

**Known gap in the source file, not in this card:** the wrapper also enforces the
changed-lines coverage floor (`diff_coverage.py`, the last and binding step), and this
paragraph of `AGENTS.md` does not mention it. `CONTRIBUTING.md` does. An agent reading only
`AGENTS.md` will not learn that a changed line with no test fails the gate.

A dedicated paragraph is the leaf's own correction of a policy it briefly held:
`C901` plus `PLR0911`/`PLR0912`/`PLR0915` are **enforced by ruff like every other rule**,
with no baseline. It records that arming them surfaced 67 offenders, that those were parked
in `quality/complexity-baseline.txt` behind a shrink-only ratchet for exactly one day before
the developer overruled it, that all 67 were refactored instead, and that **the file, the
module that read it and the gate step that ran it are deleted**. It then tells agents how to
clear a finding — extract a cohesive helper: a dispatch table for an if/elif ladder, a
guard-clause prologue split from the body, a parse step separated from a decide step — and
how never to: `# noqa`, a per-file ignore, or widening a limit in `pyproject.toml`.

A separate sentence states the policy in general: **"Nothing in this gate is exempt from
anything. There is no baseline, ratchet, allowlist or grandfather file anywhere in it, and
none may be added: a finding is fixed, never recorded."** CRAP gets the same treatment —
`cc**2 * (1 - branch_coverage)**3 + cc` against the branch data Coverage.py emits under
`[tool.coverage.run] branch = true`, with the reader refusing a statement-only report, and
the threshold as the whole policy.

A second paragraph is the leaf's correction of this file's own prior claim:
**"Radon does not enforce anything."** `radon cc` and `radon mi` exit 0 whatever they
find — the file cites `radon cc mcp/src/agents_remember -s -n B --order SCORE` reporting
141 blocks at grade C or worse and still exiting 0 — so no Radon invocation can fail a
gate. Radon is a report for refactor scouting, and it remains load-bearing in exactly one
place that is not a gate: `code_quality/crap_calculator.py` imports
`radon.complexity.cc_visit` for the complexity term of the CRAP score. The section closes
by telling agents to record Radon rows in the code-quality report template as
`reported`, never as `passed`.

HFX2-L8's stability/reclamation cross-reference survives unchanged: before adding or
editing any store, loop-over-a-store, queue, or append-only log, agents must read the
memory layer's `system/coding-guidelines.md` "Stability, Bounded Resources, and
Reclamation" section. This is a doctrine read requirement, not a new gate or runtime
behavior.

### Conventions

Workflow names remain stable contracts. C-* skills are core support skills, and
W-* skills are task workflows. Active runtime and memory settings are always
resolved through `c-08-ar-coordination-context-resolver` skill; provider readiness is checked through MCP when that
server and providers are configured; source templates and example defaults are
not treated as the user's live runtime configuration.

### Invariants And Boundaries

This file should not be used as the installed coordinator entrypoint. Installed
coordinator instructions belong in `runtime/agents-md-files/` as package-owned
templates and in the live `ar-coordination/` tree after runtime installation.
User-specific behavior and repo policy belong in the resolved memory layer.
Worktree, closeout, integration, push, cleanup, and protected-branch movement
remain approval-gated. Implementation approval and commit approval are separate
gates; agents must stop after checks or closeout dry-runs until the developer
explicitly approves real commits or lifecycle mutations. The workflow-before-code
warning now says this explicitly: do not randomly commit — use the `c-12-closeout` skill closeout
procedure (`direct_closeout_preview`/`apply`) instead.

### Todos

Refresh verification metadata after this `AGENTS.md` source update is committed.

### Docs References

No external domain documentation is needed to prove this repository-local agent
contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found; same-repository workflow files are the direct evidence. | n/a | n/a |

## Repo-Internal References

The active repo behavior depends on the source-checkout scope, installed-runtime
handoff, workflow routing, resolver gate, and source-layout boundaries in this
file.

| Finding | Anchor | Source |
| --- | --- | --- |
| The file identifies `agents-remember` as the source package and points sibling-repo work to the installed `ar-coordination/AGENTS.md`. | `# Agents Remember Source Checkout Instructions` | AGENTS.md:1-198 |
| The repo routes sessions by role through the `l-01-agent-lifecycles` skill: spawned agents follow their briefs, a developer session runs the architect lifecycle, and the build decision at `decide` is a research-only exit or a durable `w-02-light-task-workflow` skill task (chat is never a build route); the standalone chat workflow and the chat build are retired. | `## Start Here — Route By Role` | AGENTS.md:16-50 |
| Memory rules require `c-08-ar-coordination-context-resolver` skill, then a configured-provider readiness check, then `c-02-memory-quality-control` skill memory quality control, and route agents to the resolved memory layer, including `system/tools.md` for repo-specific code quality checks, instead of a root-level source checkout `system/` folder. | `## Memory And Onboarding` | AGENTS.md:49-98 |
| Boundaries state that implementation approval is not commit approval; agents must stop after checks or closeout dry-runs before real commits, closeout apply, integration, push, or cleanup. | `## Boundaries` | AGENTS.md:125-145 |
| Source-layout and boundary notes make root `skills/` canonical, identify `scripts/sync-skills.py` as the helper that refreshes generated MCP/harness skill copies, and keep installed coordinator instructions separate from user-owned memory and runtime configuration. | `## Source Layout` | AGENTS.md:99-124 |
| Source-layout and boundary notes make root `agents-md-files/`, `benchmarks/`, `providers/`, and `system/` canonical runtime asset folders, identify `scripts/sync-runtime.py` as the helper that refreshes generated MCP package-data copies, and tell agents not to edit generated runtime asset copies directly. | `## Source Layout` | AGENTS.md:99-124 |
| Code-quality routing names `python -m agents_remember.code_quality.check` as the gate, states that it takes no path arguments because its scope is `git ls-files '*.py'`, lists four enforcing steps plus mandatory CRAP, states that nothing in the gate is exempt and no baseline or allowlist may be added, tells agents how to clear a complexity finding by extraction, states that Radon reports and cannot fail a gate while remaining CRAP's complexity engine, and requires the Stability/Reclamation doctrine before store, loop-over-store, queue, or append-only-log changes. | `## Code Quality Instructions` | AGENTS.md:146-198 |
| Source-layout and boundary notes make `scripts/harness/` the single source for the eight self-hosted harness starter packages, route their refresh through `scripts/sync-harness.py`, and separate generated starter files from the per-harness files a starter package owns alone. | `## Source Layout` | AGENTS.md:99-124 |
| The gate command this file names, with the enforcing/report split it describes. | `run_quality_check` | mcp/src/agents_remember/code_quality/check.py:420-469 |
| The `diff-coverage` step this file omits. | `run_diff_coverage` | mcp/src/agents_remember/code_quality/post_coverage.py:121-170 |
| The binding coverage floor `AGENTS.md` does not mention; `CONTRIBUTING.md` is the document that does. | `DiffCoverage`; `measure` | mcp/src/agents_remember/code_quality/diff_coverage.py:56-77; mcp/src/agents_remember/code_quality/diff_coverage.py:289-317 |
| The report template this file says must record Radon rows as `reported`. | `## Tool Results` | system/defaults/examples/memory-repo/code-quality-report-template.md:18-39 |

## Cross-Repo References

The workspace root may include this file as a pointer, but this file now
delegates sibling-repository work to the installed runtime instructions.

| Finding | Anchor | Source |
| --- | --- | --- |
| No sibling repository citation is required; the cross-repo behavior is a handoff instruction in this file. | n/a | n/a |

## L23 Final Candidate Disposition

The source instructions now make the pinned Dagger graph the sole acceptance authority. Python,
Vitest, and Playwright startup requires the graph's matching nonce and in-container attestation;
direct host execution is diagnostic and cannot satisfy leaf closeout or master integration.

## R39 Acceptance Cadence

The source instructions now make lifecycle altitude the sole acceptance owner: targeted Dagger
runs once at leaf closeout and full Dagger runs once at master integration. Leaf integration,
push, pull request, tag, and publish do not rerun acceptance; pull requests retain deterministic
non-test checks only. Python, Vitest, Playwright, and the direct wrapper refuse outside the matching
nonce-attested Dagger graph.

## Update History

- 2026-08-14T11:25+02:00 — R39 curator: reconciled the root instructions with the exact-once
  leaf/master cadence and PR-only non-test validation. Verification remains closeout-owned.
- 2026-08-14T09:37+02:00 — Reopened L23 cadence: recorded exact targeted-at-leaf-closeout and
  full-at-master-integration ownership; leaf integration and GitHub PR validation do not rerun it.
- 2026-08-14T06:30+02:00 — L23 final candidate review: source instructions now make the pinned
  Dagger graph the sole acceptance path and require Python, Vitest, and Playwright to refuse startup
  without its nonce and in-container attestation. Verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded the free-chat launcher and sprint-qualified
  architect → orchestrator → manager chain, including the removal of global named-seat fallback.
  Verification metadata remains pinned until closeout stamps the code commit.

- 2026-08-02T16:46+02:00 — 260731-EFA-L6 curator W1-B03: repaired 11 citation rows with exact anchors and source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 final state. **Retired this card's mid-leaf claim
  that `AGENTS.md` documents a shrink-only complexity baseline and five enforcing steps.**
  The source file now says the opposite: nothing in the gate is exempt, the baseline and its
  gate step are deleted, the four complexity codes are enforced by `ruff` directly, and a
  finding is cleared by extraction. Recorded the four enforcing steps the file actually
  names, and recorded honestly that the file **omits the `diff-coverage` step** that the
  wrapper also enforces. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 gate honesty (mid-leaf). **Retired this card's claim that
  agents should "run Ruff, Pyright, and Radon after Python code changes"** — the file now
  names one gate command, states it takes no path arguments because its scope is
  `git ls-files '*.py'`, and says plainly that Radon does not enforce anything while
  remaining CRAP's complexity engine. Added the shrink-only complexity baseline paragraph
  (both failing directions, the `--write` discipline, the hazard it does not cover) and
  the `scripts/harness/` source-layout and boundary entries for the generated harness
  starter trees. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.

- 2026-07-09T10:40+02:00 — 260707-HFX2-L8 stability/reclamation doctrine: documented the new
  Code Quality Instructions MUST-READ sentence that points store, loop-over-store, queue, and
  append-only-log changes at the resolved memory layer's "Stability, Bounded Resources, and
  Reclamation" doctrine. Verification metadata pinned until closeout stamps the HFX2-L8 commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: the repo-root
  session-start contract now routes developer-facing sessions to the architect lifecycle
  (`roles/architect.md`) and points the plan gate at the architect, while spawned role
  sessions still follow their briefs. Verification metadata pinned until closeout stamps
  the HFX-L6 commit.

- 2026-07-06T12:05+02:00 — 260703-L10 (one-vocabulary sweep): the `Start Here` section became `Route By Role` — sessions route through the unified `l-01-agent-lifecycles` skill (spawned agents follow briefs; a developer session is the orchestrator on the request → trust-checkpoint → reframe-research → decide → build → close axis), the dead `orient → ground → frame → decide` axis and the retired skill name are gone, the chat build is removed from the build modes (chat is never a build route; research-only exit or `w-02-light-task-workflow` task), and the IMPORTANT block names the orchestrator lifecycle's plan gate. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-06-11T14:07+02:00: No content impact: re-verified against merged main `c2c2dcb` after the upstream doc-link/typo merges (PRs #69-#73) and the repository rename from `agents-remember-md` to `agents-remember`; card content already matched the source.
- 2026-06-08T11:53+02:00: Updated source-layout onboarding for canonical root runtime asset folders (`agents-md-files/`, `benchmarks/`, `providers/`, `system/`) and `scripts/sync-runtime.py`, including the generated package-data boundary. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-03T18:58+02:00: Updated source-layout onboarding for the root-level canonical `skills/` tree and `scripts/sync-skills.py` sync helper. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-02T03:45+02:00: Rewired the root checkout contract to route every session into `l-01-session-job-lifecycle`: replaced Task Format Routing and the separate `Frame Before You Choose a Format` section with a `Start Here — Enter the Job Lifecycle` section whose only task-format call is L-01's build-mode step (read-only exit / chat build / durable W-02); the standalone W-03 chat workflow is retired and absorbed into L-01's chat build. Part of the L-01 lifecycle reshape (mcp 1.1.0). Verification metadata re-verified at closeout.
- 2026-06-01T11:18+02:00: Documented the new `Frame Before You Choose a Format` section ahead of Task Format Routing (the `tasks/AGENTS.md` collaboration doctrine applies up front and routes evidence to `c-04-retrieval-strategy-router` skill) and the added `Memory Retrieval Strategies` list pointing to `c-04-retrieval-strategy-router` skill. Verification metadata stays pinned; Repo-Internal Reference line ranges will be re-verified at closeout.
- 2026-05-29T20:25+02:00: Updated after the workflow-before-code warning was made explicit ("do not randomly commit; use the `c-12-closeout` skill closeout procedure").
- 2026-05-28T19:52+02:00: Updated after source-checkout code quality guidance added Pyright beside Ruff and Radon.
- 2026-05-24T04:34+02:00: Updated after source-checkout instructions renamed `c-02-memory-quality-control` skill to memory quality control and made commit approval separate from implementation approval.
- 2026-05-23T21:31+02:00: Made source-checkout code quality guidance explicit about Ruff and Radon after Python implementation work.
- 2026-05-23T21:25+02:00: Simplified provider-authority wording and added source-checkout code-quality routing to resolved memory-layer tools and coding guidelines.
- 2026-05-23T14:20+02:00: Updated source-layout onboarding after `installer/` and `runtime/scripts/` were removed from the source package.
- 2026-05-23T13:46+02:00: Updated provider readiness guidance to use `context_packet` MCP tool instead of deleted source lifecycle scripts or coordinator `system/settings.json`.
- 2026-05-21T04:09+02:00: Added the configured-provider readiness check after `c-08-ar-coordination-context-resolver` skill and before `c-02-memory-quality-control` skill for source-checkout work.
- 2026-05-15T04:12+02:00: Reframed the root `AGENTS.md` onboarding around the source checkout contract and the installed-runtime handoff.
- 2026-05-15T00:38+02:00: Refreshed after coordinator and memory-layer settings guidance was folded into the repo-root contract during the `AGENTS.md` template reshuffle. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T18:51+02:00: Refreshed after AGENTS.md emphasized the workflow-before-code warning and separated it from the memory section.
- 2026-05-12T11:30: Updated after AGENTS.md was shortened to the three workflow formats, workflow-before-code rule, and `c-08-ar-coordination-context-resolver` skill resolver contract.
- 2026-05-11T19:52: Corrected escaped workflow wildcard wording introduced during the verification refresh.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the memory system rules switched fallback resolver language to `code_repository_name` and `code_repository_root`.
- 2026-05-10T03:01: Updated after chat-mode closeout guidance routed approved micro edits through `c-09-git-worktree-manager` skill `direct-closeout`.
- 2026-05-09T22:57: Refreshed against commit `bb95b99` and tightened references around the six-gate onboarding workflow.
- 2026-05-09T21:59: Updated for split memory/coordination terminology and `c-09-git-worktree-manager` skill worktree context.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the agent operating contract.
