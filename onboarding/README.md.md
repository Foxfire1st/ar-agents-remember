# README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `README.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T11:30+02:00                     |
| lastVerifiedCommitHash | `f70e0108910088af1df622ffd12d16271845cf51` |
| lastVerifiedCommitDate | 2026-06-02T13:52:16+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`README.md` is now the public front door for Agents Remember. It gives a concise product-level explanation, a short quickstart, links to harness-specific install pages, optional benchmark guidance, and a compact repository/runtime map. Detailed setup, concepts, workflows, benchmark methodology, guides, and reference material now live under `docs/`.

## Code Commentary

### Logic

The README opens with a TLDR that frames Agents Remember as durable, git-verified repo knowledge made first-class infrastructure, then shows the source-file to onboarding-unit mapping and the three substrates agents use to reach memory — by path (the file's own note), by meaning (semantic search), and by relationship (the code graph) — with by-path notes as the core and the other two as opt-in providers. The earlier sidecar-only "path-derived memory, no vector store / hidden service" positioning and the sidecar-era infographic embed were removed; that anti-retrieval framing predated the semantic-search and code-graph providers and no longer described the product.

The previous long README install matrix was moved out of the front page. The root page now keeps one short, harness-agnostic three-step quickstart that the agent drives: (1) wire the MCP server by running the published `agents-remember-mcp` package via `uvx --config <abs>/agents-remember-settings.json` (no repo clone), then restart the harness so it loads the server; (2) run `runtime_install` then `skills_install` (scaffolding, skills, and provider images when enabled), then restart so the harness discovers the new skills; (3) run the `C-13-install-and-onboard` skill, which pre-checks setup, installs the start hook (or places the directive), sets up the memory repo (asking scaffold-new vs use-existing), bootstraps onboarding, and starts providers indexing — then restart once more so a newly installed session hook activates. The README frames those three restarts (load server, discover skills, activate hook) as the only hands-on steps. Harness-specific setup links point to dedicated pages under `docs/install/`, and detailed first-run setup lives in `docs/getting-started.md`.

The README distinguishes the source checkout from the installed runtime. The source checkout packages `mcp/`, `runtime/`, optional benchmark package source, docs, and roadmap notes. The installed `ar-coordination/` runtime owns installed instructions, skills, optional benchmark package content, local coordination artifacts, external memory repos, worktrees, and temp files.

A `## What It Looks Like In Practice` mini-transcript sits between Core Model and the Live Demo: it shows a source file's by-path onboarding note, the task-start `context_packet`/`memory_quality_check` calls, and the read-onboarding-then-propose-then-refresh loop — a concrete picture of the by-path loop for skimming readers.

A short `## Live Demo: This Repo Uses Agents Remember` section sits between Core Model and Requirements. It states that Agents Remember runs on itself and links the project's own published memory repo (`Foxfire1st/ar-agents-remember-md`) as a live, inspectable example of the by-path onboarding layer. It surfaces the dogfooding message higher on the page than the existing Contributing-section mention, which still owns the operational instruction to clone that memory and use it while contributing.

### Conventions

- Keep the README short enough to scan.
- Use the README to orient and route, not to carry full setup matrices or reference material.
- Use `docs/` for user-facing docs, `benchmarks/` for optional benchmark fixtures, `AGENTS.md` and installed runtime templates for agent behavior, and onboarding for durable repository knowledge.
- Keep public language focused on the current intended install model: install into `ar-coordination`, expose installed skills to the harness, and store memory in either repo-local `ar-memory/` or selected external memory repos.
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
| The README's TLDR frames durable git-verified repo knowledge as infrastructure, shows the source-file to onboarding-unit mapping, and names the three retrieval substrates (by path / by meaning / by relationship), with meaning and relationship as opt-in providers. | L1-L18 | [README.md](agents-remember-md/README.md) |
| The README shows a `## What It Looks Like In Practice` mini-transcript: a source file's by-path onboarding note, the task-start `context_packet`/`memory_quality_check` calls, and the read-then-propose-then-refresh loop. | L36-L52 | [README.md](agents-remember-md/README.md) |
| The README adds a `## Live Demo: This Repo Uses Agents Remember` section stating Agents Remember runs on itself and linking the project's own published memory repo (`Foxfire1st/ar-agents-remember-md`) as a live, inspectable by-path onboarding example. | L54-L59 | [README.md](agents-remember-md/README.md) |
| The quickstart is a short, harness-agnostic three-step agent-driven flow — (1) wire the MCP server via `uvx`, (2) run `runtime_install` then `skills_install`, (3) run the `C-13-install-and-onboard` skill (which sets up the memory repo, installs the start hook, bootstraps onboarding, and starts provider indexing) — framed around three harness restarts (load server, discover skills, activate hook). | L72-L90 | [README.md](agents-remember-md/README.md) |
| The README routes harness-specific setup to dedicated install pages and routes deeper product material, including benchmark methodology, to `docs/`. | L92-L103 | [README.md](agents-remember-md/README.md) |
| The README keeps the source checkout layout distinct from the installed runtime layout and includes optional benchmark package locations in both trees. | L105-L136 | [README.md](agents-remember-md/README.md) |
| The README's Status section pins the project at `2.0.0` (a major, breaking lifecycle-reshape release) and defers the public-contract promise to the Stability section, noting those contracts change only on a major bump while internals/providers may still evolve across minors. | L138-L140 | [README.md](agents-remember-md/README.md) |
| The Stability section is the semver promise: skill IDs, MCP tool names and their inputs/outputs, the `ar-coordination/`/`ar-memory/` layout, and the settings schema do not change without a major version bump; internals/provider internals/prompt wording may change in minor releases. | L142-L144 | [README.md](agents-remember-md/README.md) |
| The Contributing section points contributors at CONTRIBUTING.md, restates the core rules, and tells contributors to download/clone the project's own published memory (Foxfire1st/ar-agents-remember-md) and use it as the active Agents Remember memory for their checkout while contributing (dogfooding the by-path onboarding loop). | L146-L150 | [README.md](agents-remember-md/README.md) |
| The docs index owns the expanded documentation map for start-here docs, install guides, guides, and reference pages. | L1-L44 | [docs/README.md](agents-remember-md/docs/README.md) |

## Cross-Repo References

The README describes external memory in general terms, but this file-level onboarding does not rely on sibling repository internals.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found for the README itself. | n/a | n/a |

## Update History

- 2026-06-02T11:30+02:00: Added a `## What It Looks Like In Practice` mini-transcript between Core Model and Live Demo (by-path note + task-start `context_packet`/`memory_quality_check` + read/propose/refresh loop). Added its Repo-Internal References row (L36-L52) and realigned every post-insertion row range by +18 (live-demo L54-L59, quickstart L72-L90, documentation L92-L103, layout L105-L136, status L138-L140, stability L142-L144, contributing L146-L150). Part of the HN-launch doc pass that also touched `docs/getting-started.md`, `docs/workflows.md`, `docs/README.md`, and a new `docs/release-checklist.md` (all outside file-level onboarding). Verification metadata stays pinned until closeout. docs/hn-launch-hardening branch.
- 2026-06-02T10:10+02:00: Added a `## Live Demo: This Repo Uses Agents Remember` section between Core Model and Requirements — it states Agents Remember runs on itself and links the project's own published memory repo (`Foxfire1st/ar-agents-remember-md`) as a live, inspectable onboarding example, surfacing the dogfooding message higher on the page than the existing Contributing mention. Added a Live Demo Repo-Internal References row (L36-L41) and realigned every post-insertion row range by +7 (quickstart L54-L72, documentation L74-L85, layout L87-L118, status L120-L122, stability L124-L126, contributing L128-L132). Verification metadata stays pinned until closeout commits the source change. docs/readme-live-demo branch.
- 2026-06-02T05:10+02:00: Bumped the Status section to `2.0.0` and flagged it as a major, breaking release (the L-01 lifecycle reshape: retired W-03/W-01, flat skills, removed skill IDs + the `skills_install` `layout` input + heavy `workflow_kind` values). L-01 series, release, mcp 2.0.0.
- 2026-06-02T05:00+02:00: Updated the README's workflow language for the L-01 reshape — "normal work starts in chat mode" became the L-01 session job lifecycle, and the Workflows doc link now names the L-01 build modes (read-only / chat build / W-02). The `docs/**` workflow/skills/layout/install pages were rewritten in the same pass but stay outside file-level onboarding. L-01 series, docs pass, mcp 2.0.0.
- 2026-06-02T03:30+02:00: Bumped the Status-section version reference to `1.0.2` (mcp 1.0.2 — `system/git-workflow.md` + PR-gated landing doctrine). Verification metadata pinned until closeout.
- 2026-06-01T13:30+02:00: Bumped the Status-section version reference to `1.0.1` (mcp 1.0.1). Verification metadata pinned until closeout.
- 2026-05-31T12:40+02:00 — Added a new `## Stability` section (the 1.0.0 semver public-contract promise: skill IDs, MCP tool names/inputs/outputs, the `ar-coordination/`/`ar-memory/` layout, and the settings schema) and reconciled the Status section to defer to it instead of warning that those contracts may evolve. Added a Contributing line linking the project's own published memory layer (Foxfire1st/ar-agents-remember-md) as a downloadable example. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-31T12:30+02:00 — Bumped the Status-section reference from `0.9.6` (pre-1.0) to `1.0.0` and updated the stability caveat to "may still evolve across minor releases" (1.0.0 review remediation). Verification metadata stays pinned until closeout commits the source change.
- 2026-05-31T01:06+02:00: Bumped the Status-section version reference to `0.9.6` for the W-02 design-section change (MCP 0.9.6). Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T22:29+02:00: Bumped the Status-section version reference to `0.9.5` for the S6 token-counter release. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T21:22+02:00: Refreshed for the 0.9.0–0.9.4 run and verified against `57944df`. Rewrote the Logic quickstart description to the current short three-step, agent-driven flow that hands onboarding to `C-13-install-and-onboard` and frames the three harness restarts; corrected the stale Repo-Internal References (the quickstart row had described an older `C-00`/`C-03`/`include_benchmarks`/`.codex` flow) and realigned all README line ranges to the 119-line source; cleared the resolved verification-refresh Todo.
- 2026-05-29T21:00+02:00: Updated after the Quickstart stopped telling users to clone this repo (Agents Remember runs from the published `agents-remember-mcp` package via `uvx`) and switched the `runtime_install`/`skills_install` examples to the act-by-default form.
- 2026-05-29T20:30+02:00: Verified the sidecar body against the committed re-spined `README.md` (TLDR, the three retrieval substrates, quickstart, install pages, source/runtime layout) and advanced verification metadata to the landed commit `01f503d`.
- 2026-05-29T17:30+02:00: Re-spined the README front door — added a TLDR framing repo knowledge as first-class infrastructure, replaced the sidecar-only "path-derived, no vector store / hidden service" positioning with the three retrieval substrates (by path / by meaning / by relationship), and removed the sidecar-era infographic embed. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` moved Codex setup to `.codex` and removed the source `.env` resolver path.
- 2026-05-24T09:38+02:00: Updated after the public quickstart switched Codex MCP registration and skill exposure examples from `.agents` to `.codex`.
- 2026-05-24T04:34+02:00: Updated after public docs renamed C-02 to memory quality control.
- 2026-05-23T14:20+02:00: Updated after the public quickstart switched from deleted installer scripts to MCP `runtime_install` and copy-only `skills_install`.
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
- 2026-05-10T03:01: Updated after the README added C-09 direct-closeout as the lightweight current-checkout path for approved external-memory micro edits.
- 2026-05-10T02:20: Updated after the README added a working external-memory repo example and links to the code and memory repositories.
- 2026-05-09T22:46: Updated for the C-10 adoption skill entry.
- 2026-05-09T21:59: Updated for ar-memory/ar-coordination split, C-09, and resolver contract changes.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the public repository overview.
