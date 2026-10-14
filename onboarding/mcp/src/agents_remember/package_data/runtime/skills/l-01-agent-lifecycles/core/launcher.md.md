# core/launcher.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Describe the developer-facing chat without a role. It answers research inline and hands managed work to a distinct host agent; it never becomes the Architect.

## Code Commentary

The current source has no spawn-role or plane identity selector. The launcher has no binding, worktree or lifecycle. It resolves the sprint and writes the developer’s request into its canonical document before one `role_start` call. An Architect start carries neither a brief nor a document reference; the developer is told where the request lives and speaks with the agent in the dashboard. Launch settings supply the choices. `role_message` from this unbound chat is refused, and a refused start never falls back to another tool.

An explicit developer-named role and task selects the bounded takeover route through the same `role_start`; no incumbent is privately replaced and no exact-id attachment is improvised. After a start the launcher stops local role work. The launcher remains outside `roles/`, because it is not a role seat.

The earlier `dispatch_agent`, queued-brief, plane-identity and conversation-switch account is historical only. It supplies no current call, restored route or independent acceptance. Retained corpus composition metadata is not proof of what a native launched agent receives.

## Evidence

- An unbound free chat answers research inline without becoming a role. [1]
- Managed work is written into the sprint before one parentless Architect start without a brief or document reference. [2]
- Only an explicitly developer-named role and task takes the bounded takeover route. [3]
- No other start or message route and no local work after start is permitted. [4]
- The launcher remains outside roles because it is not a role seat. [5]



- The manifest retains ambient-launcher metadata outside the role registry; this is not the native routing-condition set. [6]

- The source assertions exclude launcher from roles, retain ambient metadata and separately check the two native routing conditions; this is not an executed PASS. [7]

## Historical account — not operative

# core/launcher.md

### Governing Overview

[MCP package overview](../../../../../../../overview.md)

### Purpose

The **ambient launcher** block: routing condition 3's own obligations, authored here so the role
registry holds only real roles and no file under `roles/` describes this mode.

### Code Commentary

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

### Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

- What the launcher is, and the ruling that it is a launcher rather than a role seat. \[1]
- The one-call contract for ordinary role-shaped work. \[2]
- The bounded task-seat-takeover exception. \[3]
- The launcher's prohibition list. \[4]
- The structural reason this block is authored outside `roles/`. \[5]
- The manifest declares the launcher entry under the ambient-launcher routing condition whose instruction source is this file. \[6]
- The shipped check asserts the launcher is not a role and that `ambient-launcher` is a routing condition. \[7]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
