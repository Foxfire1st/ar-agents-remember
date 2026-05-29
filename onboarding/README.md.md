# README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `README.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T20:30+02:00                     |
| lastVerifiedCommitHash | `f3d57f6a9cf48a314ec7c9c6c8cb11d5e0eeb893` |
| lastVerifiedCommitDate | 2026-05-29T20:39:01+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`README.md` is now the public front door for Agents Remember. It gives a concise product-level explanation, a short quickstart, links to harness-specific install pages, optional benchmark guidance, and a compact repository/runtime map. Detailed setup, concepts, workflows, benchmark methodology, guides, and reference material now live under `docs/`.

## Code Commentary

### Logic

The README opens with a TLDR that frames Agents Remember as durable, git-verified repo knowledge made first-class infrastructure, then shows the source-file to onboarding-unit mapping and the three substrates agents use to reach memory — by path (the file's own note), by meaning (semantic search), and by relationship (the code graph) — with by-path notes as the core and the other two as opt-in providers. The earlier sidecar-only "path-derived memory, no vector store / hidden service" positioning and the sidecar-era infographic embed were removed; that anti-retrieval framing predated the semantic-search and code-graph providers and no longer described the product.

The previous long README install matrix was moved out of the front page. The root page now keeps one generic quickstart: run the published `agents-remember-mcp` package via `uvx` (no repo clone) with an `ar-coordination/` workspace beside the target projects, configure the MCP server, request `runtime_install()` for `ar-coordination` (it applies by default now), note that reinstall reconciles package-owned runtime scaffold files while provider dependencies are MCP-owned, optionally add benchmark fixtures with `include_benchmarks=true`, expose packaged skills with `skills_install`, add workspace instructions that include `ar-coordination/AGENTS.md`, then ask the agent to initialize memory and bootstrap onboarding. For Codex, the quickstart now uses `.codex/mcp` and `.codex/skills` as the normal harness registration and skill exposure folders. Harness-specific setup links point to dedicated pages under `docs/install/`.

The README distinguishes the source checkout from the installed runtime. The source checkout packages `mcp/`, `runtime/`, optional benchmark package source, docs, and roadmap notes. The installed `ar-coordination/` runtime owns installed instructions, skills, optional benchmark package content, local coordination artifacts, external memory repos, worktrees, and temp files.

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

- After these documentation changes are committed, refresh verification metadata to the new README source commit.
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
| The README's TLDR frames durable git-verified repo knowledge as infrastructure, shows the source-file to onboarding-unit mapping, and names the three retrieval substrates (by path / by meaning / by relationship), with meaning and relationship as opt-in providers. | L1-L20 | [README.md](agents-remember-md/README.md) |
| The quickstart installs runtime assets into `ar-coordination` through MCP `runtime_install`, states that provider dependencies are MCP-owned, optionally installs benchmarks with `include_benchmarks=true`, exposes packaged skills through `skills_install`, uses `.codex/mcp` to infer `.codex/skills` for Codex, points workspace instructions at `ar-coordination/AGENTS.md`, then uses C-00 and C-03 for memory initialization and onboarding bootstrap. | L32-L82 | [README.md](agents-remember-md/README.md) |
| The README now routes harness-specific setup to dedicated install pages and routes deeper product material, including benchmark methodology, to `docs/`. | L81-L106 | [README.md](agents-remember-md/README.md) |
| The README keeps the source checkout layout distinct from the installed runtime layout and includes optional benchmark package locations in both trees. | L108-L140 | [README.md](agents-remember-md/README.md) |
| The docs index owns the expanded documentation map for start-here docs, install guides, guides, and reference pages. | L1-L39 | [docs/README.md](agents-remember-md/docs/README.md) |

## Cross-Repo References

The README describes external memory in general terms, but this file-level onboarding does not rely on sibling repository internals.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found for the README itself. | n/a | n/a |

## Update History

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
