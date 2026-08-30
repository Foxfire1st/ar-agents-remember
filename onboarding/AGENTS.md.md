# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `AGENTS.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-30T12:34+02:00 |
| lastVerifiedCommitHash | `f9f92ca793811b6cb738d7e302dfecdf8636e96e`|
| lastVerifiedCommitDate | 2026-08-30T14:26:46+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[agents-remember root overview](overview.md)

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

The current launcher contract is sprint-local rather than global. For ordinary role-shaped work, a
developer-opened free chat resolves the durable sprint and first leaf, compiles the canonical
architect brief, and calls `dispatch_agent` once on the sprint document with role `architect`.
An explicit developer-declared task-seat takeover instead targets the named role on that role's
canonical task document. Absence of plane identity
selects ambient target-document/role-altitude authority; the exact brief is durable before the
launcher hands over. The hosted architect then uses the same public tool under plane identity and
direct-child scope. A plane refusal never falls back to ambient, and neither caller handles the
internal session primitive or a runtime occupant id. The dashboard and notifier can host concurrent
sprints without cross-sprint custody, routing, or wake ownership.

The file starts by declaring that `agents-remember` is source package code,
not the live runtime after installation. It gives a fallback handoff for the
case where a workspace root includes this file while the actual target is a
sibling repository, then scopes normal resolver input for this checkout to
`code_repository_name = agents-remember`.

A `Start Here — Route By Role` section now sits where Task Format Routing used
to: sessions route by role through the `l-01-agent-lifecycles` skill — a spawned
agent (the `AR_SPAWN_ROLE` env var, or a role brief as first message) follows
its brief as its session start, while a developer-facing session is free chat.
Research stays inline; role-shaped work is handed to a separately hosted,
sprint-bound **architect** through the canonical one-call dispatch transaction.
The architect runs the request → trust-checkpoint → reframe-research → decide → build → close
phase axis. The job type is a lens during reframe-research, and the build
decision at `decide` has two shapes — a research-only exit (no worktree, no task
file) or a durable `w-02-light-task-workflow` skill task; chat is never a build
route, so small code work takes the minimal artifact and larger work escalates
to a master + light sub-task series. The `tasks/AGENTS.md` collaboration
doctrine applies in the architect lifecycle's reframe-research phase.
The HFX-L6 role split keeps spawned roles on their briefs while making the
sprint-bound architect the developer-facing owner after launcher handoff; the
launcher itself is not a global role seat and the backend orchestrator is never
the normal developer-facing lifecycle.
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

### Code Quality Instructions — Current Acceptance Boundary

The source now routes Python investigation and acceptance through the pinned Dagger module. Leaf
closeout owns one targeted acceptance run and master
integration owns one full run; other lifecycle and publication steps do not rerun it. The
exported `clean-quality-results.json` is the single authoritative result, while host hooks
and GitHub pull requests stay deterministic non-test rails.

Host Python, Playwright, and the changed-lines coverage CLI have no supported execution path.
Candidate A's direct Python wrapper was deleted and has no compatibility replacement. Direct
targeted Vitest unit/component runs are the deliberate exception:
they are supported as fast diagnostics, but never create acceptance, changed-lines coverage,
or lifecycle evidence. CRAP plus changed-lines coverage score only the Dagger run's
branch-coverage artifact.

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
| The file identifies `agents-remember` as the source package and points sibling-repo work to the installed `ar-coordination/AGENTS.md`. | `# Agents Remember Source Checkout Instructions` | AGENTS.md:1-215 |
| The repo routes sessions by role through `l-01-agent-lifecycles`: spawned agents follow their briefs, while free chat compiles one architect brief and calls `dispatch_agent` once on the sprint document before handoff. | `## Start Here — Route By Role` | AGENTS.md:16-28 |
| Memory rules require `c-08-ar-coordination-context-resolver` skill, then a configured-provider readiness check, then `c-02-memory-quality-control` skill memory quality control, and route agents to the resolved memory layer, including `system/tools.md` for repo-specific code quality checks, instead of a root-level source checkout `system/` folder. | `## Memory And Onboarding` | AGENTS.md:49-98 |
| Boundaries state that implementation approval is not commit approval; agents must stop after checks or closeout dry-runs before real commits, closeout apply, integration, push, or cleanup. | `## Boundaries` | AGENTS.md:125-145 |
| Source-layout and boundary notes make root `skills/` canonical, identify `scripts/sync-skills.py` as the helper that refreshes generated MCP/harness skill copies, and keep installed coordinator instructions separate from user-owned memory and runtime configuration. | `## Source Layout` | AGENTS.md:99-124 |
| Source-layout and boundary notes make root `agents-md-files/`, `benchmarks/`, `providers/`, and `system/` canonical runtime asset folders, identify `scripts/sync-runtime.py` as the helper that refreshes generated MCP package-data copies, and tell agents not to edit generated runtime asset copies directly. | `## Source Layout` | AGENTS.md:99-124 |
| Code-quality routing reserves Python investigation and acceptance for the pinned Dagger module, names the one targeted/full cadence, records Candidate A's wrapper retirement, and permits direct targeted Vitest only as non-certifying diagnostic feedback. | `## Code Quality Instructions` | AGENTS.md:146-215 |
| The same section derives Python scope from the index, names enforcing/reporting rails, forbids baselines and exemptions, and routes exact commands plus stability doctrine through the resolved memory layer. | `## Code Quality Instructions` | AGENTS.md:146-215 |
| Source-layout and boundary notes make `scripts/harness/` the single source for the eight self-hosted harness starter packages, route their refresh through `scripts/sync-harness.py`, and separate generated starter files from the per-harness files a starter package owns alone. | `## Source Layout` | AGENTS.md:99-124 |
| The gate command this file names, with the enforcing/report split it describes. | `run_quality_check` | mcp/test_support/agents_remember_test_support/code_quality/check.py:148-198 |
| The changed-lines step named by the current acceptance boundary. | `run_diff_coverage` | mcp/test_support/agents_remember_test_support/code_quality/post_coverage.py:121-170 |
| The report template this file says must record Radon rows as `reported`. | `## Tool Results` | system/defaults/examples/memory-repo/code-quality-report-template.md:18-39 |

## Cross-Repo References

The workspace root may include this file as a pointer, but this file now
delegates sibling-repository work to the installed runtime instructions.

| Finding | Anchor | Source |
| --- | --- | --- |
| No sibling repository citation is required; the cross-repo behavior is a handoff instruction in this file. | n/a | n/a |

## L23 Final Candidate Disposition

The source instructions make the pinned Dagger graph the sole acceptance authority. Python,
Playwright, changed-lines coverage, and direct-wrapper execution require its matching nonce and
in-container attestation. Direct targeted Vitest is supported diagnostic feedback only and cannot
satisfy leaf closeout, master integration, changed-lines coverage, or lifecycle evidence.

## R39 Acceptance Cadence

The source instructions now make lifecycle altitude the sole acceptance owner: targeted Dagger
runs once at leaf closeout and full Dagger runs once at master integration. Leaf integration,
push, pull request, tag, and publish do not rerun acceptance; pull requests retain deterministic
non-test checks only. Python, Playwright, changed-lines coverage, and the direct wrapper refuse
outside the matching nonce-attested Dagger graph; targeted direct Vitest remains diagnostic-only.

## 260824-PDLS — Python Evidence Rule

The root operating contract now makes the pinned Dagger graph the only supported Python execution
environment for investigation and acceptance. Candidate A's host command, sealed manifest, static
closure analyzer, and self-proof were removed after exact-candidate measurement showed that the
route was slower than the equivalent warm Dagger micro-route while carrying substantial extra
maintenance surface. Direct targeted Vitest remains supported diagnostic feedback; Python has no
host compatibility or fallback path.

## 2026-08-26 Python Evidence-System Doctrine Reconciliation

The repository instruction now requires agents changing test evidence, fixtures, support,
selection, retry, cadence, or causal reporting to read
`docs/design/python-evidence-system.md`. That design document is the governing contract for the
separation between internal canonical product truth, independent external conformance, scheduled
stress/cadence evidence, and lifecycle-eligible durable evidence. The instruction prevents a
locally convenient test or report from silently becoming acceptance authority.

## Update History

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 reconciled the root routing contract to one public
  `dispatch_agent` call, separated ordinary architect bootstrap from explicit named-role takeover,
  retained process-derived ambient-versus-plane authority, and kept plane failures fail-closed.
  Verification remains closeout-owned.

- 2026-08-28T10:03:40+02:00 — Corrected the current code-quality section and citations so they no
  longer advertise the retired Candidate-A Python wrapper.

- 2026-08-28T05:10+02:00 — Reconciled Candidate A retirement: no Python host wrapper, classifier,
  manifest, or compatibility route remains; Dagger owns Python investigation and acceptance.
- 2026-08-26T10:44:52+02:00 — Reconciled the new Python evidence-system doctrine pointer and its acceptance-authority boundary after reviewing the `AGENTS.md` source delta; verification metadata remains closeout-owned.
- 2026-08-24T21:23+02:00 — 260824-PDLS aligned the agent contract with the exact-node diagnostic
  and Dagger evidence firewall.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: reconciled the deliberate
  direct-targeted Vitest diagnostic route with the guarded Python, Playwright, changed-lines,
  wrapper, and acceptance rails; added the governing root-overview link and removed the resolved
  changed-lines documentation-gap claim. Dagger acceptance remains pending and closeout-owned.
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
