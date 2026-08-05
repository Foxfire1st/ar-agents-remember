# scripts/harness/shared/session-start-directive.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `scripts/harness/shared/session-start-directive.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T06:30+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

The one definition of the session-start directive read from **inside** a workspace. It is
the text every session-start hook prints and the text Cursor's always-applied rule and
Copilot's instructions carry. `scripts/sync-harness.py` composes it into **six** files:
the four `hooks/agents-remember-session-start.md` directives, `.cursor/rules/
agents-remember.mdc`, and `.github-vscode/copilot-instructions.md`.

## Code Commentary

### Logic

The body states the three-condition session routing that `l-01-agent-lifecycles` owns:

1. If `AR_SPAWN_ROLE` is set, **or** the first user message is a role brief from an
   orchestrating agent, the session must **ignore the notice entirely** — the brief is
   the session start.
2. Otherwise the session is the developer-facing one, i.e. the **architect**: read
   `ar-coordination/AGENTS.md`, then run the lifecycle at
   `skills/l-01-agent-lifecycles/roles/architect.md`.
3. The architect's four named obligations are spelled out inline: trust checkpoint before
   relying on memory, `read_ar_files` (paired source + onboarding) until the build
   decision, retrieval-strategy tally as evidence, notify-and-stop at every developer
   hand-off.

### Conventions

- Per-harness framing is **not** in this file. It is declared as `prologue` / `epilogue`
  in `sync-harness.py`'s `Composed` entries: Cursor's `---`/`alwaysApply: true` front
  matter, the `@<PATH/TO/YOUR/PROJECTS_FOLDER>/ar-coordination/AGENTS.md` include line,
  and Copilot's note about where the path resolves.
- The body is stored without a trailing newline concern; `compose()` strips trailing
  newlines from the body before joining prologue, body and epilogue.

### Invariants And Boundaries

- **This body names `ar-coordination/AGENTS.md` relatively**, because every file composed
  from it is read from inside the workspace. The sibling `workspace-directive.md` is the
  same directive for context files mirrored to the workspace root, which carry the
  rendered absolute path instead. Which body a harness takes is a per-harness fact; the
  body itself is not, and that is the whole reason there are two files rather than nine.
- A wording change here lands in all six composed files at once. Editing a composed copy
  directly is caught by `sync-harness.py --check` in both hook tiers and by
  `mcp/tests/test_sync_harness.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The generator that composes this body into six files with per-harness framing. | `generated_files`, `compose` | scripts/sync-harness.py:576-621; scripts/sync-harness.py:631-633 |
| The workspace-root variant of the same directive. | "as workspace instructions" | scripts/harness/shared/workspace-directive.md:9-9 |
| The hook fragments that read this file at run time. | `DIRECTIVE_PATH`, `emit` | scripts/harness/session_start_hook.py:23-23; scripts/harness/session_start_hook.py:57-59 |
| The lifecycle this directive routes a session into. | `# l-01-agent-lifecycles — The Agent Lifecycles` | skills/l-01-agent-lifecycles/SKILL.md:6-416 |

## Update History

- 2026-08-03T03:06:00+02:00 — Curator W3-B02 repaired 4 Repo-Internal citation rows, resolving 8 manifest findings with exact generator, directive, hook, and lifecycle anchors; verification metadata was preserved.
- 2026-07-31T06:30+02:00 — 260731-EFA-L2 promoted this to the single source for six
  copies of the session-start directive (requirement L2-R12). Verification metadata is
  pinned to the leaf's reformat commit until closeout stamps the code commit.
