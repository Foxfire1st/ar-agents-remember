# core/launcher.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The **ambient launcher** block: routing condition 3's own obligations, authored here so the role
registry holds only real roles and no file under `roles/` describes this mode.

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
enumerating `roles/` sees exactly the seats that are roles, and the launcher is not one of them.

### Conventions

Keep this block free of any seat identity: it describes a routing condition, and adding it to `roles/`
would silently create a role that does not exist.

### Invariants And Boundaries

- The launcher is never the architect and never becomes one.
- Exactly one `dispatch_agent` call; `dispatched` and `dispatch-queued` are both durable.
- The launcher never submits caller identity and never handles a session id.
- A plane refusal never falls back to ambient.
- The role registry holds exactly the roles the corpus publishes and the launcher has no entry under
  `roles/`. Since 260915-CAPS-L13 that registry is **ten** roles — the ninth seat plus the
  `bootstrap` free agent — and this block's reason for existing is unchanged by that addition: the
  launcher is a routing condition, not an eleventh member.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

- What the launcher is, and the ruling that it is a launcher rather than a role seat. [1]
- The one-call contract for ordinary role-shaped work. [2]
- The bounded task-seat-takeover exception. [3]
- The launcher's prohibition list. [4]
- The structural reason this block is authored outside `roles/`. [5]
- The manifest declares the launcher entry under the ambient-launcher routing condition whose instruction source is this file. [6]
- The shipped check asserts the launcher is not a role and that `ambient-launcher` is a routing condition. [7]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
