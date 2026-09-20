# core/launcher.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/core/launcher.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80` |
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| governingOverview      | `../../../../../../../overview.md` |

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

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| What the launcher is, and the ruling that it is a launcher rather than a role seat. | `## What it is` | skills/l-01-agent-lifecycles/core/launcher.md:8-19 |
| The one-call contract for ordinary role-shaped work. | `## Ordinary role-shaped work — the one call` | skills/l-01-agent-lifecycles/core/launcher.md:20-40 |
| The bounded task-seat-takeover exception. | `## Task-seat takeover — the bounded exception` | skills/l-01-agent-lifecycles/core/launcher.md:41-51 |
| The launcher's prohibition list. | `## What the launcher must not do` | skills/l-01-agent-lifecycles/core/launcher.md:52-60 |
| The structural reason this block is authored outside `roles/`. | "Why it is authored here rather than in" | skills/l-01-agent-lifecycles/core/launcher.md:61-66 |
| The manifest declares the launcher entry under the ambient-launcher routing condition whose instruction source is this file. | `routing_condition` | skills/l-01-agent-lifecycles/composition-manifest.json:507-507 |
| The shipped check asserts the launcher is not a role and that `ambient-launcher` is a routing condition. | `test_manifest_resolves_every_role_and_operation_source` | mcp/tests/test_role_instruction_corpus.py:248-300 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-09-19T22:28:52+00:00: Generated citation repair: `routing_condition` repointed to skills/l-01-agent-lifecycles/composition-manifest.json:507-507. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **dead governing-overview body link repaired, and the field brought into agreement with it.** The field named `../../../../../../../overview.md` — which resolves, but only under the onboarding root rather than against this card's own route — while the body link named `../../../../../overview.md` and resolved card-relative to nothing, so a reader clicking it landed nowhere and the two declarations disagreed. Both now name `../../../../../../../overview.md`, the route-local overview of this card's own directory, so the field and the link agree by construction. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-09-17T12:55+02:00 — 260915-CAPS-L14 curator: **D3 dead governing-overview link repaired.** This card's `governingOverview` was one directory level short, so it resolved to a path that does not exist instead of the `mcp/` route overview. The card directory sits seven levels below `onboarding/`, so seven `../` steps reach `onboarding/` and the correct target is `../../../../../../../overview.md` (→ `onboarding/mcp/overview.md`). Reversed here: `../../../../../overview.md` (which resolved to the nonexistent `mcp/src/agents_remember/overview.md`) or `../../../../../../overview.md` (→ the nonexistent `mcp/src/overview.md`) → **`../../../../../../../overview.md`**. The body's own `[mcp/overview.md](…)` link was re-pointed with it. No prose, anchor, range or verification stamp was otherwise changed.

- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: **body corrected for the corpus's tenth role**
  (`CAPS-R13@v1`). The Purpose said the block is authored here "so the role registry stays exactly nine
  roles", and the Invariants said "the role registry stays at nine roles" — both are stale: the
  registry is now ten, and this block's reason for existing is that the launcher is not a member of it,
  not that the count is nine. The Conventions sentence ("would silently create a tenth role") was
  corrected to "a role that does not exist" for the same reason. **The Repo-Internal section had lost
  its `| Finding | Anchor | Source |` header row**, so its rows rendered as prose; the header and
  delimiter are restored, the four section ranges were re-derived against the 66-line block (they were
  measured against an older revision and began at L20, which is the second heading rather than the
  first), and two stale citations were repaired — the manifest row cited `:1-1` for a `launcher` block
  that lives at `:486-503`, and the corpus-test row cited `:199-225` for a case that now starts at
  `:248`. Verification metadata is left at the leaf base commit because the source is uncommitted —
  the governed closeout stamps the real code commit.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/core/launcher.md` — a file added by the role-instruction corpus consolidation. The canonical source is a shared core block composed into every role capsule (launcher).; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
