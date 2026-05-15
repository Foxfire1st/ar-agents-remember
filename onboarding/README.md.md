# README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `README.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T12:05+02:00                     |
| lastVerifiedCommitHash | `af3e24cadd005d3b79f29dfdc27731019e0dca27` |
| lastVerifiedCommitDate | 2026-05-15T12:35:48+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`README.md` is now the public front door for Agents Remember. It gives a concise product-level explanation, a short quickstart, links to harness-specific install pages, and a compact repository/runtime map. Detailed setup, concepts, workflows, guides, and reference material now live under `docs/`.

## Code Commentary

### Logic

The README opens with the stable positioning statement: Agents Remember is path-derived, git-verified memory for coding agents. It immediately shows the source-file to onboarding-unit mapping so readers understand the product before encountering workflow names or runtime folders.

The previous long README install matrix was moved out of the front page. The root page now keeps one generic quickstart: clone beside target projects, install runtime into `ar-coordination`, expose installed skills with `install-skills.sh`, add workspace instructions that include `ar-coordination/AGENTS.md`, then ask the agent to initialize memory and bootstrap onboarding. Harness-specific setup links point to dedicated pages under `docs/install/`.

The README distinguishes the source checkout from the installed runtime. The source checkout packages `installer/`, `runtime/`, docs, and roadmap notes. The installed `ar-coordination/` runtime owns installed instructions, scripts, skills, local coordination artifacts, external memory repos, worktrees, and temp files.

### Conventions

- Keep the README short enough to scan.
- Use the README to orient and route, not to carry full setup matrices or reference material.
- Use `docs/` for user-facing docs, `AGENTS.md` and installed runtime templates for agent behavior, and onboarding for durable repository knowledge.
- Keep public language focused on the current intended install model: install into `ar-coordination`, expose installed skills to the harness, and store memory in either repo-local `ar-memory/` or selected external memory repos.
- Avoid presenting the public README as a source-package explanation or compatibility guide for old alpha layouts.

### Invariants And Boundaries

The README is explanatory, not the implementation source of truth. Runtime behavior still belongs to the installer, scripts, and skills. If README guidance disagrees with helper behavior, verify helper behavior before changing operational assumptions.

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
| The README presents Agents Remember as path-derived, git-verified memory and shows the source-file to onboarding-unit mapping before the quickstart. | L1-L14 | [README.md](agents-remember-md/README.md) |
| The quickstart installs runtime assets into `ar-coordination`, exposes installed skills, points workspace instructions at `ar-coordination/AGENTS.md`, then uses C-00 and C-03 for memory initialization and onboarding bootstrap. | L32-L73 | [README.md](agents-remember-md/README.md) |
| The README now routes harness-specific setup to dedicated install pages and routes deeper product material to `docs/`. | L75-L99 | [README.md](agents-remember-md/README.md) |
| The README keeps the source checkout layout distinct from the installed runtime layout. | L101-L130 | [README.md](agents-remember-md/README.md) |
| The docs index owns the expanded documentation map for start-here docs, install guides, guides, and reference pages. | L1-L39 | [docs/README.md](agents-remember-md/docs/README.md) |

## Cross-Repo References

The README describes external memory in general terms, but this file-level onboarding does not rely on sibling repository internals.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found for the README itself. | n/a | n/a |

## Update History

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
- 2026-05-09T21:15: Created first file-level onboarding baseline for the public repository overview.
- 2026-05-09T21:59: Updated for ar-memory/ar-coordination split, C-09, and resolver contract changes.
- 2026-05-10T03:01: Updated after the README added C-09 direct-closeout as the lightweight current-checkout path for approved external-memory micro edits.
- 2026-05-10T02:20: Updated after the README added a working external-memory repo example and links to the code and memory repositories.
- 2026-05-09T22:46: Updated for the C-10 adoption skill entry.
