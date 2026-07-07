# dashboard/src/data/sessionGroups.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionGroups.test.ts`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T23:56:18+02:00                           |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`       |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Unit tests for the pure G1 command-tree derivation (`data/sessionGroups.ts`, 260703-L14). The
grouping is deliberately store-free, so membership, tiering, and the at-scale shape are all pinned
here as data-in/data-out cases — the component suite (`SessionList.test.tsx`) only covers rendering.

## Code Commentary

### Logic

Six cases over small doc/enclosure/session builders (a sprint doc carrying
`orchestrates: ["260706_management-repo"]`, a commanded and a free master, live enclosures):

1. **Deck membership** — command-role provenance (strategist/manager `spawnRole`) plus the
   developer-facing chat claiming the orchestration task's own qualified leaf all land on the deck
   (label `{sprint title} · command deck`, gold tier, `3 chats · 3 live`); a worker with a master
   leaf claim does NOT (role provenance is the deck gate) and its master group is `management` +
   `nested` because the sprint names it.
2. **Uncommanded master** — a leaf claim groups under its master with no tier and no indent when
   no orchestration doc names it.
3. **D3 flat-run regression** — with NO orchestration task, a manager-role session and a plain one
   derive zero groups (all ungrouped): the sidebar's unchanged-flat contract.
4. **Archive roll-up** — a claim on a dead-worktree enclosure and a claim on an absent master both
   roll into one `landed` group (unmarked, `defaultCollapsed`, `2 chats · archived`).
5. **Case-insensitive leaf join** — an uppercase doc-id claim matches the slugified lowercase
   enclosure `leafId`.
6. **30-chat scale fixture** — 4 deck + 6 + 7 master + 13 landed sessions collapse into exactly
   four groups in deck→masters→landed order with per-group counts (`4 chats · 2 live`,
   `6 chats · 2 live`, `7 chats · 1 live`, `13 chats · archived`) and nothing ungrouped — the
   "reads at a glance at 30 chats" requirement as data.

### Invariants And Boundaries

Pure logic tests (no DOM, no store). Fixture builders satisfy the full `TaskDocNode` /
`EnclosureNode` projection shapes so type drift in the mirror surfaces here.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The derivation under test. | — | [sessionGroups.ts](sessionGroups.ts) |
| The component-level rendering/collapse coverage that complements this suite. | L14 describe | [SessionList.test.tsx](../panels/SessionList.test.tsx) |

## Update History

- 2026-07-06T23:56:18+02:00 — 260703-L14 (visual hierarchy + chat grouping): created — deck
  membership by role provenance + orchestration claim, uncommanded-master grouping, the D3
  flat-run zero-group regression, landed/absent archive roll-up, the case-insensitive leaf join,
  and the 30-chat scale fixture. Verification metadata pinned until closeout stamps the L14 commit.
