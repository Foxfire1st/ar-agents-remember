# README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `README.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-12T18:57+02:00                     |
| lastVerifiedCommitHash | `d2f8072bb43a197c193b99405056e720adc34b1b` |
| lastVerifiedCommitDate | 2026-05-12T19:22:12+02:00|

## Purpose

`README.md` is the public-facing explanation of Agents Remember. It explains one-to-one onboarding, setup, harness skill installation, storage modes, shared roots, resolver and drift-check roles, and the repository's skill layout.

## Code Commentary

### Logic

The README introduces the memory model first, then explains setup, harness skill installation, storage decisions, shared workspace behavior, active coordination context resolution, chat/worktree closeout behavior, and the available skill families. Its early "What This Looks Like" section shows the default repo-local onboarding sidecar and points to this repo's inspectable shared-memory layer as an example, while `memory.md` is explained as the code-commit to memory-commit ledger. It teaches `ar-memory/` for durable internal memory, `ar-coordination/` for local coordination, names C-09 `direct-closeout` as the approved current-checkout commit sequence for small shared-memory chat-mode edits, and lists C-10 as the adoption path that turns existing shared-memory onboarding into the first ledgered `memory.md` baseline after drift review.

The setup flow now separates three paths that users often conflate: the real `agents-remember-md` checkout, the harness-visible skills folder, and the `ar-coordination` root. Harnesses that require skills in a dedicated folder use `scripts/install-skills.sh --install-root <skills-folder>` to create symlinks back to the canonical `skills/` tree. Recursive scanners such as Codex and Claude Code use the namespace tree layout, while stricter direct-folder scanners such as Hermes.md, Pi.dev, OpenClaw, Windsurf, and Cursor compatibility installs use `--layout flat` so the visible folder names match lowercase skill frontmatter names without copying canonical source files. Shared-mode coordination can live outside both the workspace and the checkout by setting `AR_COORDINATION_ROOT` in the checkout's `.env`.

### Conventions

The README distinguishes source files, onboarding files, generated maintenance artifacts, task workflow artifacts, shared memory repos, harness skill-install locations, and the `memory.md` ledger. It names Codex `.agents/skills`, Claude Code `.claude/skills`, Hermes `~/.hermes/skills`, Pi `.pi/skills`, OpenClaw `<workspace>/skills` and `~/.openclaw/skills`, Cursor `.cursor/skills`, and Windsurf `.windsurf/skills` locations separately, treats C-08 as the resolver, uses `code_repository_name`/`code_repository_root` for resolver inputs, and treats C-02 as the drift classifier.

### Invariants And Boundaries

The README is explanatory, not an implementation source. When it disagrees with helper scripts, current script behavior should be verified before changing operational assumptions. It must not imply that users should copy individual Agents Remember skill folders; preserving the canonical skill tree through tree or flat symlinks is part of the install contract.

### Todos

Second-wave documentation should add richer walkthroughs for real C-09 start/closeout usage after the first production worktree task is run. Refresh verification metadata after the README install-guidance change is committed.

### Docs References

External domain documentation is only needed when the README makes harness-specific discovery claims.

| Finding                                                                                                                                                 | Citations | Source Path                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------- |
| Claude Code documents project and personal skill locations, plugin skills, extra directories via `--add-dir`, live skill changes, and nested discovery. | L155-L189 | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Hermes documents `.hermes.md`/`HERMES.md`, `AGENTS.md`, and `CLAUDE.md` context discovery plus `AGENTS.md` progressive subdirectory loading. | L58-L75; L136-L154 | [Hermes Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files) |
| Hermes documents external skill directories through `skills.external_dirs`, and its skill format uses YAML frontmatter with a lowercase `name`. | L283-L300; L389-L401 | [Hermes Skills](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md) |
| Pi documents `AGENTS.md` startup context and skill locations including `.pi/skills`, `.agents/skills`, global Pi skills, settings paths, and recursive `SKILL.md` directory discovery. | L132-L147; L104-L120 | [Pi Quickstart](https://pi.dev/docs/latest/quickstart), [Pi Skills](https://pi.dev/docs/latest/skills) |
| Pi documents Agent Skills compatibility and requires lowercase skill names that match parent directories. | L87-L89; L195-L200 | [Pi Skills](https://pi.dev/docs/latest/skills) |
| OpenClaw documents workspace `AGENTS.md` as injected operating instructions, workspace `skills/` as a standard workspace file, and skill precedence between workspace, managed, and bundled locations. | L200-L242; L882-L903 | [OpenClaw Agent Workspace](https://openclawlab.com/en/docs/concepts/agent-workspace/), [OpenClaw Skills](https://openclawlab.com/en/docs/tools/skills/) |
| Cursor documents Agent Skills, recursive skill-root walking, `.agents/skills` and `.cursor/skills` project roots, user-wide roots, slash invocation, and the requirement that `name` match the containing folder. | L1-L14 | [Cursor Agent Skills](https://cursor.com/docs/skills.md) |
| Windsurf documents workspace/global skill folders, automatic and `@skill-name` invocation, `.agents/skills` compatibility scanning, and Claude skill scanning when Claude config reading is enabled. | L123-L215 | [Windsurf Skills](https://docs.windsurf.com/windsurf/cascade/skills) |
| Windsurf documents `AGENTS.md` as location-scoped rules that are discovered throughout the workspace and parent directories up to the git root. | L120-L173 | [Windsurf AGENTS.md](https://docs.windsurf.com/windsurf/cascade/agents-md) |

## Repo-Internal References

The README establishes the conceptual map future tasks will repeatedly cite.

| Finding                                                                                                                                                                                                                                            | Citations | Source Path                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------- |
| One-to-one onboarding means source files have matching onboarding files.                                                                                                                                                                           | L89       | [README.md](agents-remember-md/README.md) |
| The working shared-memory example links to the inspectable memory repo, shows the memory repo layout, and explains the `memory.md` code-to-memory ledger concept.                                                                                   | L43-L73   | [README.md](agents-remember-md/README.md) |
| The quickstart now states that the checkout can live outside the code workspace, and the installer section explains namespace tree symlinks versus flat direct skill symlinks.                                                                                  | L104-L171 | [README.md](agents-remember-md/README.md) |
| C-00 creates memory and coordination scaffolds, while C-03 owns initial repo onboarding.                                                                                                                                                           | L175-L203 | [README.md](agents-remember-md/README.md) |
| Storage mode and path rules are separate concepts.                                                                                                                                                                                                 | L207-L220 | [README.md](agents-remember-md/README.md) |
| Inline storage reuses the same file-level onboarding model, and the general wire-up flow now includes installing skills into a dedicated harness folder when required.                                                                              | L243-L256 | [README.md](agents-remember-md/README.md) |
| The Codex section explains that `AGENTS.md` and `/` skill discovery are separate, and it documents workspace-local, external-checkout, and user-wide `install-skills.sh` calls.                                                                     | L262-L296 | [README.md](agents-remember-md/README.md) |
| The Claude Code section separates `CLAUDE.md` instruction loading from native skill discovery, and documents `.claude/skills`, `~/.claude/skills`, external checkouts, and nested discovery through the namespace symlink.                           | L300-L338 | [README.md](agents-remember-md/README.md) |
| The Hermes.md section documents context-file choices, local and shared skill-folder installs, and `external_dirs` configuration using the flat symlink layout. | L342-L379 | [README.md](agents-remember-md/README.md) |
| The Pi.dev section documents `AGENTS.md`, `.pi/skills`, `.agents/skills`, and global Pi skill installs using the flat symlink layout. | L381-L418 | [README.md](agents-remember-md/README.md) |
| The OpenClaw section documents workspace `AGENTS.md`, workspace `skills`, global `~/.openclaw/skills`, and extra dirs while using the flat symlink layout. | L420-L451 | [README.md](agents-remember-md/README.md) |
| The Cursor section separates instructions from native Agent Skills, documents project/user skill roots, slash invocation, recursive walking, and the flat symlink layout needed for lowercase parent folder compatibility.                           | L453-L495 | [README.md](agents-remember-md/README.md) |
| Copilot and Windsurf guidance now describes using `install-skills.sh --install-root <skills-folder>` when a harness cannot discover skills directly from the checkout; Windsurf uses the flat symlink layout and `@skill-name` invocation.          | L499-L559 | [README.md](agents-remember-md/README.md) |
| The three modes section notes that small chat-mode shared-memory edits can use C-09 `direct-closeout` for code-first onboarding metadata refresh and ledger sequencing, while larger or parallel work should use C-09 worktrees.                    | L561-L571 | [README.md](agents-remember-md/README.md) |
| Shared coordination guidance now separates skill installation from `AR_COORDINATION_ROOT` and shows a layout where the checkout, `ar-coordination`, and workspace all live in different roots.                                                      | L603-L632 | [README.md](agents-remember-md/README.md) |
| C-08 resolves the active context from `code_repository_name` or `code_repository_root`, returns `coordination_root` and `memory_root`, and C-02 classifies stale onboarding.                                                                        | L714-L720 | [README.md](agents-remember-md/README.md) |
| The repository contains core skills, workflows, the skill installer script, roadmap material, and system examples.                                                                                                                                  | L724-L744 | [README.md](agents-remember-md/README.md) |
| The README lists C-09 as the helper for worktree-backed tasks and direct closeout of approved current-checkout edits, and C-10 as the helper for converting existing shared-memory onboarding into the first ledgered baseline after drift review. | L737-L738 | [README.md](agents-remember-md/README.md) |

## Cross-Repo References

The README explains shared workspace use, but this file-level onboarding does not rely on sibling repository internals.

| Finding                                                                                                                                  | Citations | Source Path                               |
| ---------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------- |
| Shared memory uses one memory repo per selected code repo while the coordinator owns tasks, notes, memory-repo checkouts, and worktrees. | L603-L710 | [README.md](agents-remember-md/README.md) |

## Update History

- 2026-05-12T18:57+02:00: Updated after the README added Hermes.md, Pi.dev, and OpenClaw install instructions after the Claude Code section.
- 2026-05-12T18:51+02:00: Refreshed metadata and current README references after the install-skills guidance and harness-specific skill setup sections were added in the working tree.
- 2026-05-12T18:22+02:00: Updated after the README gained Cursor and Windsurf native skill instructions and split installer guidance into tree versus flat symlink layouts.
- 2026-05-12T18:08+02:00: Updated after the Claude Code README instructions were corrected to use `.claude/skills` / `~/.claude/skills` native discovery with the existing namespace symlink.
- 2026-05-12T17:53+02:00: Updated after the README gained harness-specific skill installation guidance, external-checkout examples, and explicit `AR_COORDINATION_ROOT` separation from skill installation.
- 2026-05-12T11:30: Updated after the shared-memory example wording focused on the inspectable memory repo rather than repeating the code repository link.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the resolver overview adopted `code_repository_name`, `code_repository_root`, and `coordination_root` terminology.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the public repository overview.
- 2026-05-09T21:59: Updated for ar-memory/ar-coordination split, C-09, and resolver contract changes.
- 2026-05-10T03:01: Updated after the README added C-09 direct-closeout as the lightweight current-checkout path for approved shared-memory micro edits.
- 2026-05-10T02:20: Updated after the README added a working shared-memory repo example and links to the code and memory repositories.
- 2026-05-09T22:46: Updated for the C-10 adoption skill entry.
