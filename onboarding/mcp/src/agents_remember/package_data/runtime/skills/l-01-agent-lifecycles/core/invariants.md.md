# core/invariants.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/core/invariants.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The shared **invariants** block: the facts every role can count on, authored once so a role file
names the invariant it depends on instead of restating the set.

## Code Commentary

### Logic

`## Continuity lives in durable state, never in transcripts` states why short-lived workers and reviewers
are safe and why **every seat writes its artifact of record** — a finding held only in a chat is a bug.
`## The decision surface` routes decision-needing questions to the task doc's `openQuestions` with the
analysis in `notes/`, and keeps backend seats behind the architect relay.

`## Sequencing is decided by the dependency graph, not by habit` sets parallel-by-default up to the
`orchestration.concurrency` cap, requires a named gate / one-writer dependency / explicit ruling for any
sequential exception, and states that build concurrency never grants landing order. `## Observability`
keeps coordination seats as `task_doc` leaves with attached chats. `## The spine: task doc → branch →
worktree` fixes what creates a branch or worktree, that design and portfolio work never touch git, and
that chat is never a build route.

`## Default behavior, and where it is overridden` states the fill-small-blanks default, the one-rung
escalation for a plan delta beyond blank-filling, and that the **spirit test is orchestrator-only**.
`## Knob resolution and capability doctrine` fixes the resolution order (role-file defaults < global
settings < repo-local settings), which rows are settings keys, the deliberate absence of per-harness role
files, and `dispatch_agent` as the harness-independent fan-out. `## Instruction-surface boundaries`
assigns task-collaboration doctrine to `tasks/AGENTS.md`, the task format to
`w-02-light-task-workflow`, repository specifics to the memory layer, and the corpus's own division of
labour to `roles/` / `operations/` / `reference/`.

### Conventions

Keep each invariant to the statement and its consequence; long rationale belongs in
`reference/rationale.md`.

### Invariants And Boundaries

- Continuity lives in the task tree plus written artifacts, never in a transcript.
- Sequential execution is the exception and must name its reason.
- Only the launch-setting rows are settings keys; `dispatch` and `tools` are structural descriptions.
- There are deliberately no per-harness role files.
- The normative path injects `core/` + the role + the current operation, and references rationale rather
  than embedding it.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The task-doc → branch → worktree spine and what may create a branch. | `## The spine: task doc → branch → worktree` | skills/l-01-agent-lifecycles/core/invariants.md:36-51 |
| Knob resolution order, the settings-key rows, and the no-per-harness-files decision. | `## Knob resolution and capability doctrine` | skills/l-01-agent-lifecycles/core/invariants.md:64-81 |
| The instruction-surface boundary that keeps task doctrine, task format, memory specifics, and role duties in separate owners. | `## Instruction-surface boundaries` | skills/l-01-agent-lifecycles/core/invariants.md:83-93 |
| Every role's `**Inherits:**` line names this block. | `**Inherits:**` | mcp/tests/test_role_instruction_corpus.py:227-289 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **dead governing-overview body link repaired, and the field brought into agreement with it.** The field named `../../../../../../../overview.md` — which resolves, but only under the onboarding root rather than against this card's own route — while the body link named `../../../../../overview.md` and resolved card-relative to nothing, so a reader clicking it landed nowhere and the two declarations disagreed. Both now name `../../../../../../../overview.md`, the route-local overview of this card's own directory, so the field and the link agree by construction. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-09-17T12:55+02:00 — 260915-CAPS-L14 curator: **D3 dead governing-overview link repaired.** This card's `governingOverview` was one directory level short, so it resolved to a path that does not exist instead of the `mcp/` route overview. The card directory sits seven levels below `onboarding/`, so seven `../` steps reach `onboarding/` and the correct target is `../../../../../../../overview.md` (→ `onboarding/mcp/overview.md`). Reversed here: `../../../../../overview.md` (which resolved to the nonexistent `mcp/src/agents_remember/overview.md`) or `../../../../../../overview.md` (→ the nonexistent `mcp/src/overview.md`) → **`../../../../../../../overview.md`**. The body's own `[mcp/overview.md](…)` link was re-pointed with it. No prose, anchor, range or verification stamp was otherwise changed.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/core/invariants.md` — a file added by the role-instruction corpus consolidation. The canonical source is a shared core block composed into every role capsule (invariants).; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
