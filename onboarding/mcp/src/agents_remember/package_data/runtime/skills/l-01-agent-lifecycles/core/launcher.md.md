# core/launcher.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/core/launcher.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `3054af87fdf0e21e9ec7132a5d62ba0d514600ba` |
| lastVerifiedCommitDate | 2026-09-16T08:23:52+02:00|
| governingOverview      | `../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../overview.md)

## Purpose

The **ambient launcher** block: routing condition 3's own obligations, authored here so the role
registry stays exactly nine roles and no file under `roles/` describes this mode.

## Code Commentary

### Logic

The launcher is the developer-facing **free chat** — a launcher, not a role seat (ruled 2026-07-09). It
has no plane identity, no worktree, and no lifecycle of its own. Research-only questions are answered
inline with no role taken, and the launcher **never becomes the architect**.

`## Ordinary role-shaped work — the one call` is the operative contract: resolve the canonical target
sprint and its canonical sprint document, compile **one complete brief** from
`../templates/architect-brief.md`, call `dispatch_agent(task_document_ref=…, role="architect",
brief=…)` **once**, and on `dispatched` or `dispatch-queued` switch the developer conversation to the
canonical `(sprint document, architect)` chat and stop role work. Both results mean the brief is durable,
so a second brief is never sent. `## Task-seat takeover — the bounded exception` routes an explicit
developer-declared takeover to the named role's canonical document instead, and records the structural
blocker when the altitude cannot be matched.

`## What the launcher must not do` is the prohibition list — no role or hat, no session/lifecycle/agent
id, no fabricated caller identity, no spend knobs in the brief, no local work after a durable dispatch
result. `## Why it is authored here rather than in roles/` records the structural reason: a reader
enumerating `roles/` sees exactly the nine seats.

### Conventions

Keep this block free of any seat identity: it describes a routing condition, and adding it to `roles/`
would silently create a tenth role.

### Invariants And Boundaries

- The launcher is never the architect and never becomes one.
- Exactly one `dispatch_agent` call; `dispatched` and `dispatch-queued` are both durable.
- The launcher never submits caller identity and never handles a session id.
- A plane refusal never falls back to ambient.
- The role registry stays at nine roles; the launcher has no entry under `roles/`.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The one-call contract for ordinary role-shaped work. | `## Ordinary role-shaped work — the one call` | skills/l-01-agent-lifecycles/core/launcher.md:20-43 |
| The bounded task-seat-takeover exception. | `## Task-seat takeover — the bounded exception` | skills/l-01-agent-lifecycles/core/launcher.md:45-56 |
| The launcher's prohibition list. | `## What the launcher must not do` | skills/l-01-agent-lifecycles/core/launcher.md:58-65 |
| The manifest declares the launcher a non-role with this instruction source. | `"is_role": false`; `"instruction_source": "core/launcher.md"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1 |
| The shipped check asserts the launcher is not a role and that `ambient-launcher` is a routing condition. | `test_manifest_resolves_every_role_and_operation_source` | mcp/tests/test_role_instruction_corpus.py:199-225 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/core/launcher.md` — a file added by the role-instruction corpus consolidation. The canonical source is a shared core block composed into every role capsule (launcher).; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
