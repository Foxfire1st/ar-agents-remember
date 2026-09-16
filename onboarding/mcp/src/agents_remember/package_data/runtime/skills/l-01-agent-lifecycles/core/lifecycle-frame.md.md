# core/lifecycle-frame.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/core/lifecycle-frame.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `3054af87fdf0e21e9ec7132a5d62ba0d514600ba` |
| lastVerifiedCommitDate | 2026-09-16T08:23:52+02:00|
| governingOverview      | `../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../overview.md)

## Purpose

The shared **minimal lifecycle frame**: the six signals every session shares, which seats run them,
the opening trust checkpoint, and how every seat meets a provider degradation.

## Code Commentary

### Logic

The signal table maps `lifecycle_start` (fleeting, one per session, no id), `lifecycle_phase` (the
phase axis), `lifecycle_turn_end_notification` (set `awaiting-developer`, return immediately, and the
**next turn's first AR call auto-resumes**), the automatic `worktree_start` promotion to persistent,
`worktree_attach`, the `switch_lifecycle` save gate, and the terminal `lifecycle_end`.

Two rules carry the most weight for every other file: a tool call outside any lifecycle is **dropped,
never misattributed**, and **a spawned role that never touches a mutating AR tool simply never
instantiates a lifecycle** — that is the designed shape, not a gap. `## Which signals a seat runs` maps
each seat class onto that rule, and `## The trust checkpoint` binds the four-step
`context_packet` / report / drift / provider opening detail to the architect and orchestrator only.

`## Provider degradation, as every seat meets it` is the shared response protocol: a
`degradation-alert` pauses provider **starting**, leaf-altitude seats stop starting providers and hold
**no kill authority**, and the orchestrator owns investigation dispatch, the remediation order, and the
stop.

### Conventions

A role file binds whether its seat runs the trust checkpoint; a spawned role never repeats it,
because its spawner compiles the facts into the brief.

### Invariants And Boundaries

- A tool call outside any lifecycle is dropped, never misattributed; `paused` is system-owned.
- A spawned role runs its own lifecycle when it runs one and never adopts its spawner's.
- Seat binding is the dispatch-time catalog binding, not lifecycle adoption.
- A holder of one lifecycle never advances another seat's.
- Leaf-altitude seats never start providers while a degradation-alert is live and hold no kill authority.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The six-signal frame and the dropped-call rule. | `## The Minimal Lifecycle Frame` | skills/l-01-agent-lifecycles/core/lifecycle-frame.md:1-38 |
| The four-step trust checkpoint bound to the architect and orchestrator. | `## The trust checkpoint` | skills/l-01-agent-lifecycles/core/lifecycle-frame.md:40-56 |
| The provider-degradation response protocol every seat meets. | `## Provider degradation, as every seat meets it` | skills/l-01-agent-lifecycles/core/lifecycle-frame.md:57-70 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/core/lifecycle-frame.md` — a file added by the role-instruction corpus consolidation. The canonical source is a shared core block composed into every role capsule (lifecycle-frame).; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
