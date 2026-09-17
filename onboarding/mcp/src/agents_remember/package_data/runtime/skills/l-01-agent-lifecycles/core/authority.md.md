# core/authority.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/core/authority.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../overview.md)

## Purpose

The shared **seat authority** block: the rules that apply to every seat in the corpus. A role file
states its own seat's side of a rule and never restates the whole of it; this file is authored once and
composed into every capsule.

## Code Commentary

### Logic

`## One lifecycle per agent type` fixes the corpus's structural premise: each agent type runs its own
self-contained lifecycle, no role is defined by reference to another role's, and **authority is
structural, never textual** — a seat's address is its task document plus its role name, and the control
plane owns occupant identity, readiness, and the pinned brief.

`## Seat binding` is the altitude table (sprint / master / leaf / portfolio artifact), the rule that the
session↔seat association is the dispatch-time catalog binding rather than lifecycle adoption, the
hat-collapse rule (sanctioned only for the owner/developer-facing architect seat), and role-seat
immutability in dashboard-owned sessions.

`## Dispatch is one structural transaction` gives the six control-plane steps, the two disjoint caller
kinds (plane-hosted seat vs ambient launcher) with their authority and forbidden shortcuts, the
consumption rules for `dispatched` / `dispatch-queued` / `source-lineage-stale`, and the rule that the
model never handles runtime occupant, session, lifecycle, branch, or commit identifiers.

`## Developer-declared task-seat takeover`, `## Escalation ladder` (**worker → manager → orchestrator →
architect → developer**; a system-specialist escalates to the orchestrator; no rung skipped), `##
Developer clarification triage`, `## Delegated series authority`, `## Minimal decision-item relay`,
`## Notify-and-stop is safe by design` (including the **watcher ban**), and `## Change authority`
complete the block.

### Conventions

Change this file only in the canonical tree; it is a shared source, so a role-local restatement is
drift rather than emphasis. When a rule here changes, the role files that name it keep their own
one-line consequence and need no rewrite.

### Invariants And Boundaries

- No role is defined by reference to another role's lifecycle.
- A spawned role never adopts its spawner's lifecycle and never wears another role's hat.
- A malformed, stale, or unauthorized plane identity is a refusal and never falls back to ambient.
- No role watches, polls, nudges, or timer-loops on its own initiative.
- A question escalates only one rung at a time; no rung is skipped.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The seat-binding altitude table and the structural (non-textual) authority rule. | `## Seat binding` | skills/l-01-agent-lifecycles/core/authority.md:16-36 |
| The six-step dispatch transaction and the two disjoint caller kinds. | `## Dispatch is one structural transaction` | skills/l-01-agent-lifecycles/core/authority.md:56-113 |
| The escalation ladder and the quo-vadis developer-worthy test. | `## Escalation ladder` | skills/l-01-agent-lifecycles/core/authority.md:118-128 |
| The watcher ban and the passive liveness duty. | `## Notify-and-stop is safe by design` | skills/l-01-agent-lifecycles/core/authority.md:187-201 |
| Every role's `**Inherits:**` line names this block, which is how the corpus composes it without duplication. | `**Inherits:**` | mcp/tests/test_role_instruction_corpus.py:227-289 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T12:55+02:00 — 260915-CAPS-L14 curator: **D3 dead governing-overview link repaired.** This card's `governingOverview` was one directory level short, so it resolved to a path that does not exist instead of the `mcp/` route overview. The card directory sits seven levels below `onboarding/`, so seven `../` steps reach `onboarding/` and the correct target is `../../../../../../../overview.md` (→ `onboarding/mcp/overview.md`). Reversed here: `../../../../../overview.md` (which resolved to the nonexistent `mcp/src/agents_remember/overview.md`) or `../../../../../../overview.md` (→ the nonexistent `mcp/src/overview.md`) → **`../../../../../../../overview.md`**. The body's own `[mcp/overview.md](…)` link was re-pointed with it. No prose, anchor, range or verification stamp was otherwise changed.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/core/authority.md` — a file added by the role-instruction corpus consolidation. The canonical source is a shared core block composed into every role capsule (authority).; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
