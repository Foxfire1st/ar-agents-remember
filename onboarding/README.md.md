# README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `README.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-19T01:50+02:00 |
| lastVerifiedCommitHash | `cbea101871743715b485f221d00f21f28d0d8835` |
| lastVerifiedCommitDate | 2026-06-13T18:54:16+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`README.md` is the public front door for Agents Remember. It gives a concise product-level explanation, a high-signal Core Features section, a short quickstart, links to harness-specific install pages, optional benchmark guidance, and a compact repository/runtime map. The concentrated feature tour now lives in `docs/features.md`; detailed setup, concepts, workflows, benchmark methodology, guides, and reference material live under `docs/`.

## Code Commentary

### Logic

The README's `<h3>` headline now frames Agents Remember in two parts — git-verified records of what coding agents know, and a control plane for what they do — sharpening the earlier single-line "durable, git-verified repo memory" framing toward the records-plus-control-plane positioning. Below it, the README uses `## Core Features` as the fast product pitch. It frames Agents Remember as project memory coding agents can verify and act on, shows the source-file to onboarding-unit mapping, and names the user-facing features a skimming reader needs in the first thirty seconds: path-addressed memory, Git-proven freshness, optional semantic/code-graph discovery that finds but does not decide, memory that lands with code through external-memory ledgers and dual worktrees, repo-owned `system/` behavior, and harness-ready first-run packages. The previous `## Core Model` section carried the same conceptual spine but was less effective as a public feature pitch.

The previous MCP-installs-skills first-run model was replaced with package-first
harness setup. The root page now keeps one short, harness-agnostic three-step
quickstart that the agent drives: (1) copy the harness-native starter package
from the repo and render the copied package. The `render-starter` script is a
convenience that infers the workspace root from the copied harness folder, takes
one explicit `--repo` list such as `--repo my-app shared-lib`, and fills path,
repository, and hook-command placeholders; the docs also allow manual
placeholder replacement. The package provides skills, hooks, rules,
instructions, MCP settings templates, and rendered hook commands; (2) wire the
published
`agents-remember-mcp` package with `uvx agents-remember-mcp@latest --config
<abs>/agents-remember-settings.json`, then restart the harness once so it loads
the MCP server and native package files; (3) invoke `c-13-install-and-onboard`,
which runs or verifies `runtime_install()`, asks scaffold-new vs existing memory,
bootstraps onboarding when needed, and starts provider indexing when enabled.
`skills_install()` remains documented as maintenance/manual, not the normal
first-run path. Harness-specific setup links point to dedicated pages under
`docs/install/`, and detailed first-run setup lives in `docs/getting-started.md`.

The README distinguishes the source checkout from the installed runtime. The
source checkout exposes root `skills/` as the canonical skill source tree and
`scripts/sync-skills.py` as the helper that refreshes MCP package-data and
harness package skill copies. It also exposes root `agents-md-files/`,
`benchmarks/`, `providers/`, and `system/` as canonical runtime asset source
folders and `scripts/sync-runtime.py` as the helper that refreshes MCP
package-data copies only. The installed `ar-coordination/` runtime owns
installed instructions, skills, optional benchmark package content, local
coordination artifacts, external memory repos, worktrees, and temp files. The
Repository Layout section states the installed runtime defaults to
`<workspace>/ar-coordination/` — inside the workspace, never the user's home
directory — and points at the `c-13-install-and-onboard` skill, which presents
that and every other install path as a workspace-first accept-or-override
default.

A `## What It Looks Like In Practice` mini-transcript sits between Core Features and the Live Demo: it shows a source file's by-path onboarding note, the task-start `context_packet`/`memory_quality_check` calls, and the read-onboarding-then-propose-then-refresh loop — a concrete picture of the by-path loop for skimming readers.

A short `## Live Demo` section sits between Core Features and Requirements. It states that Agents Remember runs on itself and links the project's own published memory repo (`Foxfire1st/ar-agents-remember`) as a live, inspectable example of the by-path onboarding layer. It surfaces the dogfooding message higher on the page than the existing Contributing-section mention, which still owns the operational instruction to clone that memory and use it while contributing.

### Conventions

- Keep the README short enough to scan.
- Use the README to orient and route, not to carry full setup matrices or reference material.
- Use `docs/` for user-facing docs, `benchmarks/` for optional benchmark fixtures, `AGENTS.md` and installed runtime templates for agent behavior, and onboarding for durable repository knowledge.
- Keep public language focused on the current intended install model: copy a harness starter package, wire the MCP server, run/verify `runtime_install()` through `c-13-install-and-onboard`, and store memory in either repo-local `ar-memory/` or selected external memory repos.
- Avoid presenting the public README as a source-package explanation or compatibility guide for old alpha layouts.

### Invariants And Boundaries

The README is explanatory, not the implementation source of truth. Runtime behavior belongs to MCP tools, package services, and skills. If README guidance disagrees with helper behavior, verify helper behavior before changing operational assumptions.

`docs/**` is currently excluded from file-level onboarding by this repository's path rules, so this README onboarding is the durable file-level companion for the public documentation front door. Repo-level overview onboarding should carry broad documentation-structure context when the docs tree changes.

### Todos

- If `docs/**` becomes eligible in path rules later, create focused file-level onboarding for high-value docs pages instead of overloading this README onboarding.

### Docs References

The README itself no longer depends on external harness docs for detailed setup claims; those claims live in the dedicated install pages.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external documentation is needed to prove the root README's current structure; it is a same-repository public overview and link hub. | n/a | n/a |

## Repo-Internal References

The README routes readers into the split documentation tree and gives the current runtime/source layout.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The README now has a `## Core Features` section that replaces `## Core Model`; it shows the source-file to onboarding-unit mapping, pitches path-addressed memory, Git-proven freshness, optional semantic/code-graph discovery, external-memory ledgers and dual worktrees, repo-owned `system/` behavior, and harness-ready first-run packages, then links to `docs/features.md`. | L32-L48 | [README.md](agents-remember/README.md) |
| The README shows a `## What It Looks Like In Practice` mini-transcript: a source file's by-path onboarding note, the task-start `context_packet`/`memory_quality_check` calls, and the read-then-propose-then-refresh loop. | L50-L66 | [README.md](agents-remember/README.md) |
| The README has a `## Live Demo` section stating Agents Remember runs on itself and linking the project's own published memory repo (`Foxfire1st/ar-agents-remember`) as a live, inspectable by-path onboarding example. | L68-L73 | [README.md](agents-remember/README.md) |
| The quickstart is a short, harness-agnostic three-step agent-driven flow: copy the harness starter package, render it either with the convenience `render-starter` script or manual placeholder replacement, wire the MCP server with `uvx`, restart once, then invoke `c-13-install-and-onboard`; `skills_install()` is maintenance/manual because the package already carries the initial skills and harness files. | L89-L121 | [README.md](agents-remember/README.md) |
| The README routes readers first to the new Features tour, then to setup, concepts, workflows, benchmark methodology, guides, settings, and skills documentation under `docs/`. | L123-L135 | [README.md](agents-remember/README.md) |
| The README keeps the source checkout layout distinct from the installed runtime layout, exposes root `skills/` as canonical, identifies `scripts/sync-skills.py` as the helper that refreshes generated skill copies, exposes root `agents-md-files/`, `benchmarks/`, `providers/`, and `system/` as canonical runtime assets, identifies `scripts/sync-runtime.py` as the package-data-only runtime asset helper, and notes the workspace-first `<workspace>/ar-coordination/` default. | L137-L177 | [README.md](agents-remember/README.md) |
| The README's Status section is a two-paragraph current-state + direction statement: paragraph one states the current version (`2.9.0`), the core-path maturity, the Stability deferral, the GitHub Releases routing (the repository's canonical changelog — this repo keeps no `CHANGELOG.md`, and Status no longer narrates per-release summaries), and the harness-maturity note; paragraph two states where the journey is going (observable, steerable sessions: machine-readable lifecycle entity, durable approval gates, a projection layer, the browser cockpit #2/#43, and the up-to-3.0 posture) — the only public place that states direction. | L199-L203 | [README.md](agents-remember/README.md) |
| The Stability section is the semver promise: skill IDs, MCP tool names and their inputs/outputs, the `ar-coordination/`/`ar-memory/` layout, and the settings schema do not change without a major version bump; internals/provider internals/prompt wording may change in minor releases. | L183-L185 | [README.md](agents-remember/README.md) |
| The Contributing section points contributors at CONTRIBUTING.md, restates the core rules, and tells contributors to download/clone the project's own published memory (Foxfire1st/ar-agents-remember) and use it as the active Agents Remember memory for their checkout while contributing (dogfooding the by-path onboarding loop). | L187-L191 | [README.md](agents-remember/README.md) |
| The docs index now includes `docs/features.md` as the concentrated product tour alongside getting-started, concepts, workflows, install guides, guides, and reference pages. | L1-L46 | [docs/README.md](agents-remember/docs/README.md) |
| `docs/features.md` carries the full feature tour, including the new table of contents plus harness-native setup and operational guardrails for MCP authority, baseline adoption, branch carryover, cross-repo gates, benchmarks, and source quality tooling. | L1-L471 | [docs/features.md](agents-remember/docs/features.md) |

## Cross-Repo References

The README describes external memory in general terms, but this file-level onboarding does not rely on sibling repository internals.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found for the README itself. | n/a | n/a |

## Update History

- 2026-06-19T01:50+02:00 — Updated the Logic section for the README headline revision (PR #85 / `b9d7314`): the `<h3>` tagline changed from "Durable, git-verified repo memory for coding agents." to "Git-verified records for what your coding agents know. A control plane for what they do.", sharpening the public positioning toward records-plus-control-plane. Advanced verification metadata to merged `main` `cbea101`.
- 2026-06-12T19:06+02:00 — No content impact: Status section version string bumped to 2.9.1 (issue #83 closeout committed-range fix release); the README structure and guidance this sidecar describes are unchanged.
- 2026-06-12T12:05+02:00 — Rewrote the Status section from the per-release narrative chain (2.0.0→2.8.0, grown into a de-facto changelog) into a two-paragraph current-state + direction statement: version `2.9.0` with the core-path maturity, Stability deferral, GitHub Releases routing (the repository's canonical changelog), and harness-maturity notes, plus a "where the journey is going" paragraph (observable, steerable sessions: machine-readable lifecycle entity, durable gates, projection layer, browser cockpit #2/#43, the 3.0 posture) — making Status the one public place that states direction. The 2.9.0 release content (worktree-only closeout, GitHub #62) moves to the mcp-v2.9.0 GitHub Release notes instead of the README. Updated the stale Status body row (previously pinned at 2.5.2). Verification metadata stays pinned until closeout commits the source change.
- 2026-06-11T14:07+02:00: No content impact: re-verified against merged main `c2c2dcb` after the upstream doc-link/typo merges (PRs #69-#73) and the repository rename from `agents-remember-md` to `agents-remember`; card content already matched the source.
- 2026-06-10T10:26+02:00 — No content impact: Status section bumped to 2.8.0 with the GitHub #54 release sentence (lifecycle-long stale-base prevention: include_freshness, stale-base preflight, memory_main_advance, worktree_sync); the README structure this sidecar describes is unchanged.
- 2026-06-10T08:15+02:00 — Status section bumped to 2.7.0 with the release sentence: background worktree provider setup observability (#53) and container-form CGC seed argv on Windows (#58).
- 2026-06-10T06:05+02:00 — No content impact: Status section bumped to 2.6.0 with the memory-integrity release sentence (carryover overview candidates, closeout body/history gates, no-impact markers; GitHub #56); the sidecar's description of the README remains accurate.
- 2026-06-10T05:45+02:00 — Status section bumped to 2.5.2 with the carryover response compaction sentence (GitHub #52).
- 2026-06-10T05:30+02:00 — Status section bumped to 2.5.1 with the tool-reliability release sentence (protocol-pipe hygiene, stall-based wedge detection, GrepAI indexing parity, single runner-image derivation, tool-report compaction with keep-5/7-day retention).
- 2026-06-09T22:10+02:00 — Status section bumped to 2.5.0 with the CGC durability/readiness release sentence (FalkorDB host-path persistence, graph-content readiness states, degraded-packet propagation, `indexing` summary list, watcher self-heal, orphan cleanup).
- 2026-06-09T15:39+02:00: Bumped the Status section to `2.4.2` and documented it as the patch packaging the consolidated `l-01-session-job-lifecycle` skill, where the complete lifecycle spine now lives in `SKILL.md` instead of a separate `lifecycle.md` companion. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-08T12:22+02:00: Bumped the Status section to `2.4.1` and documented
  it as the patch for runtime asset packaging/source sync plus skipped-provider
  context-packet provider validation. Verification metadata stays pinned until
  closeout commits the source change.
- 2026-06-08T11:53+02:00: Updated repository-layout onboarding for canonical root runtime asset folders and `scripts/sync-runtime.py`, including the pre-commit/pre-push generated-copy checks. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-08T08:33+02:00: Bumped the Status section to `2.4.0` and documented it as the release for harness-local starter renderers, Python hook command rendering, and manual placeholder-replacement docs that remove the legacy Claude Code `jq` misconception. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T18:42+02:00: Refined setup memory so renderers are framed as optional convenience scripts for placeholder replacement; manual replacement is an explicit supported path. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T18:19+02:00: Refined the renderer setup memory after the CLI contract dropped the separate workspace-root flag; copied harness packages now infer the workspace root from their folder and accept one `--repo` list. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T16:45+02:00: Updated the quickstart memory after starter packages gained harness-local `render-starter` scripts; setup now says copy the package, render paths/repositories/hook commands before MCP wiring, then wire MCP and restart. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T12:28+02:00: Replaced README `## Core Model` memory with a faster `## Core Features` pitch and added the public `docs/features.md` link; updated references to the new features page and docs index entry. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-04T23:15+02:00: Updated the `2.3.3` Status note to include Docker-safe provider setup naming for dotted worktree names alongside the runtime reinstall watcher rebind patch. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-04T18:52+02:00: Bumped the Status section to `2.3.2` and documented it as the patch that packages the refreshed runtime skills with the C-09 worktree intent approval gate and integration checkout prerequisite reminder. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-03T19:25+02:00: Bumped the Status section to `2.3.1` and documented it as the patch that corrects the PyPI/MCP package README to the 2.3.0 package-first setup flow. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-03T18:58+02:00: Updated for the 2.3.0 starter-package release: package-first quickstart, one-restart first-run path, root `skills/` canonical source tree, `scripts/sync-skills.py`, and Status-section version bump. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-03T04:25+02:00: Bumped the Status-section version reference to `2.2.0` (mcp 2.2.0 — lifecycle collaboration loop and C-09 source-branch contract refresh; a minor backward-compatible release on the 2.0.0 reshape). Verification metadata pinned until closeout. chore/release-mcp-2.2.0 branch.
- 2026-06-02T18:35+02:00: Bumped the Status-section version reference to `2.1.0` (mcp 2.1.0 — workspace-first install defaults, skill-name/MCP-tool reference convention, grepai-status + quality-gate fixes; a minor backward-compatible release on the 2.0.0 reshape). Verification metadata pinned until closeout. chore/release-mcp-2.1.0 branch.
- 2026-06-02T16:35+02:00: Second batch (install-location defaults) — the Repository Layout section gained a workspace-first note (installed runtime defaults to `<workspace>/ar-coordination/`, inside the workspace and never the home directory; the `c-13-install-and-onboard` skill shows each install path as an accept-or-override default). Realigned the post-Layout row ranges by +3 (layout end L105-L139, status L141-L143, stability L145-L147, contributing L149-L153). fix/skill-ref-naming-and-grepai-status branch; verification pinned until closeout.
- 2026-06-02T11:30+02:00: Added a `## What It Looks Like In Practice` mini-transcript between Core Model and Live Demo (by-path note + task-start `context_packet`/`memory_quality_check` + read/propose/refresh loop). Added its Repo-Internal References row (L36-L52) and realigned every post-insertion row range by +18 (live-demo L54-L59, quickstart L72-L90, documentation L92-L103, layout L105-L136, status L138-L140, stability L142-L144, contributing L146-L150). Part of the HN-launch doc pass that also touched `docs/getting-started.md`, `docs/workflows.md`, `docs/README.md`, and a new `docs/release-checklist.md` (all outside file-level onboarding). Verification metadata stays pinned until closeout. docs/hn-launch-hardening branch.
- 2026-06-02T10:10+02:00: Added a `## Live Demo: This Repo Uses Agents Remember` section between Core Model and Requirements — it states Agents Remember runs on itself and links the project's own published memory repo (`Foxfire1st/ar-agents-remember`) as a live, inspectable onboarding example, surfacing the dogfooding message higher on the page than the existing Contributing mention. Added a Live Demo Repo-Internal References row (L36-L41) and realigned every post-insertion row range by +7 (quickstart L54-L72, documentation L74-L85, layout L87-L118, status L120-L122, stability L124-L126, contributing L128-L132). Verification metadata stays pinned until closeout commits the source change. docs/readme-live-demo branch.
- 2026-06-02T05:10+02:00: Bumped the Status section to `2.0.0` and flagged it as a major, breaking release (the L-01 lifecycle reshape: retired W-03/W-01, flat skills, removed skill IDs + the `skills_install` `layout` input + heavy `workflow_kind` values). L-01 series, release, mcp 2.0.0.
- 2026-06-02T05:00+02:00: Updated the README's workflow language for the `l-01-session-job-lifecycle` skill reshape — "normal work starts in chat mode" became the `l-01-session-job-lifecycle` skill session job lifecycle, and the Workflows doc link now names the `l-01-session-job-lifecycle` skill build modes (read-only / chat build / `w-02-light-task-workflow` skill). The `docs/**` workflow/skills/layout/install pages were rewritten in the same pass but stay outside file-level onboarding. `l-01-session-job-lifecycle` skill series, docs pass, mcp 2.0.0.
- 2026-06-02T03:30+02:00: Bumped the Status-section version reference to `1.0.2` (mcp 1.0.2 — `system/git-workflow.md` + PR-gated landing doctrine). Verification metadata pinned until closeout.
- 2026-06-01T13:30+02:00: Bumped the Status-section version reference to `1.0.1` (mcp 1.0.1). Verification metadata pinned until closeout.
- 2026-05-31T12:40+02:00 — Added a new `## Stability` section (the 1.0.0 semver public-contract promise: skill IDs, MCP tool names/inputs/outputs, the `ar-coordination/`/`ar-memory/` layout, and the settings schema) and reconciled the Status section to defer to it instead of warning that those contracts may evolve. Added a Contributing line linking the project's own published memory layer (Foxfire1st/ar-agents-remember) as a downloadable example. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-31T12:30+02:00 — Bumped the Status-section reference from `0.9.6` (pre-1.0) to `1.0.0` and updated the stability caveat to "may still evolve across minor releases" (1.0.0 review remediation). Verification metadata stays pinned until closeout commits the source change.
- 2026-05-31T01:06+02:00: Bumped the Status-section version reference to `0.9.6` for the `w-02-light-task-workflow` skill design-section change (MCP 0.9.6). Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T22:29+02:00: Bumped the Status-section version reference to `0.9.5` for the S6 token-counter release. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T21:22+02:00: Refreshed for the 0.9.0–0.9.4 run and verified against `57944df`. Rewrote the Logic quickstart description to the current short three-step, agent-driven flow that hands onboarding to `c-13-install-and-onboard` and frames the three harness restarts; corrected the stale Repo-Internal References (the quickstart row had described an older `c-00-initialize-memory-repo` skill / `c-03-repo-bootstrap` skill / `include_benchmarks` / `.codex` flow) and realigned all README line ranges to the 119-line source; cleared the resolved verification-refresh Todo.
- 2026-05-29T21:00+02:00: Updated after the Quickstart stopped telling users to clone this repo (Agents Remember runs from the published `agents-remember-mcp` package via `uvx`) and switched the `runtime_install`/`skills_install` examples to the act-by-default form.
- 2026-05-29T20:30+02:00: Verified the sidecar body against the committed re-spined `README.md` (TLDR, the three retrieval substrates, quickstart, install pages, source/runtime layout) and advanced verification metadata to the landed commit `01f503d`.
- 2026-05-29T17:30+02:00: Re-spined the README front door — added a TLDR framing repo knowledge as first-class infrastructure, replaced the sidecar-only "path-derived, no vector store / hidden service" positioning with the three retrieval substrates (by path / by meaning / by relationship), and removed the sidecar-era infographic embed. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` moved Codex setup to `.codex` and removed the source `.env` resolver path.
- 2026-05-24T09:38+02:00: Updated after the public quickstart switched Codex MCP registration and skill exposure examples from `.agents` to `.codex`.
- 2026-05-24T04:34+02:00: Updated after public docs renamed `c-02-memory-quality-control` skill to memory quality control.
- 2026-05-23T14:20+02:00: Updated after the public quickstart switched from deleted installer scripts to `runtime_install` MCP tool and copy-only `skills_install`.
- 2026-05-23T13:46+02:00: Updated repository layout after provider lifecycle, provider setup, and benchmark runner behavior moved into `mcp/` and the source `scripts/` route was removed.
- 2026-05-23T05:32+02:00: Updated after the quickstart stopped presenting source-installer provider dependency install and moved provider dependency operations behind MCP settings.
- 2026-05-21T02:14+02:00: Updated quickstart notes after reinstall began installing enabled provider dependencies by default and documented `--skip-provider-deps`.
- 2026-05-15T17:32+02:00: Clarified benchmark package wording after source-side empty workspace folders were removed in favor of generated workspaces. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-15T15:50+02:00: Updated after the README added optional benchmark install guidance, benchmark methodology routing, and benchmark package/runtime layout entries. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-15T12:05+02:00: Refreshed after the README was rewritten as a concise public front door and detailed setup/reference material moved into `docs/`. Verification metadata remains pinned to the last committed source state until the docs rewrite is committed.
- 2026-05-14T21:38+02:00: Updated after README settings examples gained the standard path-rule exclusion baseline for generated/vendor/build/local artifacts. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-13T13:38: Updated after the README replaced top-level system examples with folder-shaped coordinator/global and memory-repo-specific scaffold examples.
- 2026-05-12T18:57+02:00: Updated after the README added Hermes.md, Pi.dev, and OpenClaw install instructions after the Claude Code section.
- 2026-05-12T18:51+02:00: Refreshed metadata and current README references after the install-skills guidance and harness-specific skill setup sections were added in the working tree.
- 2026-05-12T18:22+02:00: Updated after the README gained Cursor and Windsurf native skill instructions and split installer guidance into tree versus flat symlink layouts.
- 2026-05-12T18:08+02:00: Updated after the Claude Code README instructions were corrected to use `.claude/skills` / `~/.claude/skills` native discovery with the existing namespace symlink.
- 2026-05-12T17:53+02:00: Updated after the README gained harness-specific skill installation guidance, external-checkout examples, and explicit `AR_COORDINATION_ROOT` separation from skill installation.
- 2026-05-12T11:30: Updated after the external-memory example wording focused on the inspectable memory repo rather than repeating the code repository link.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the resolver overview adopted `code_repository_name`, `code_repository_root`, and `coordination_root` terminology.
- 2026-05-10T03:01: Updated after the README added `c-09-git-worktree-manager` skill direct-closeout as the lightweight current-checkout path for approved external-memory micro edits.
- 2026-05-10T02:20: Updated after the README added a working external-memory repo example and links to the code and memory repositories.
- 2026-05-09T22:46: Updated for the `c-10-adopt-memory-baseline` skill adoption skill entry.
- 2026-05-09T21:59: Updated for ar-memory/ar-coordination split, `c-09-git-worktree-manager` skill, and resolver contract changes.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the public repository overview.
