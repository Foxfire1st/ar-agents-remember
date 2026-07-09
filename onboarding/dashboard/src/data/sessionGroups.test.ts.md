# dashboard/src/data/sessionGroups.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionGroups.test.ts`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-07T21:17+02:00                           |
| lastVerifiedCommitHash | `c392985424896e9f392507295a23c4902d0c0696`       |
| lastVerifiedCommitDate | 2026-07-09T14:31:11+02:00|
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

1. **Deck membership** — command-role provenance (backend orchestrator/strategist/manager
   `spawnRole`) plus the developer-facing architect chat claiming the orchestration task's own
   qualified leaf all land on the deck
   (label `{sprint title} · command deck`, gold tier, `4 chats · 4 live`); a worker with a master
   leaf claim does NOT (role provenance is the deck gate) and its master group is `management` +
   `nested` because the sprint names it.
2. **Uncommanded master** — a leaf claim groups under its master with no tier and no indent when
   no orchestration doc names it.
3. **D3 flat-run regression** — with NO orchestration task, a manager-role session and a plain one
   derive zero groups (all ungrouped): the sidebar's unchanged-flat contract.
4. **Archive roll-up (HFX2-L11 round-2 F4 narrowed)** — only a `status:"landed"` claim rolls into
   the `landed` archive group (unmarked, `defaultCollapsed`, label `"landed archive"`,
   `1 chat · archived`); a legacy `status:"exited"` claim and a claim on an absent master with no
   status both route to the pre-existing `ungrouped` bucket instead. Before L11, `exited`/absent
   rows were folded into the archive too — that let sessions the backend's landed-cleanup endpoint
   can't actually close pile up in the group the cleanup button targets, so the derivation now only
   ever admits genuinely `landed` rows.
5. **Case-insensitive leaf join** — an uppercase doc-id claim matches the slugified lowercase
   enclosure `leafId`.
6. **30-chat scale fixture** — 4 deck + 6 + 7 master + 13 `status:"landed"` sessions collapse into
   exactly four groups in deck→masters→landed order with per-group counts (`4 chats · 2 live`,
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

- 2026-07-09T14:05+02:00 — HFX2-L11 (landed chat archive, round 2 F4 fix): `status:"landed"` rows
  route into the new collapsed "landed archive" group; legacy `status:"exited"`/absent-enclosure rows
  no longer fold into that group (round-1 behavior) and instead route to the pre-existing `ungrouped`
  ("Open sessions") bucket, so the landed-archive group only ever contains rows the backend
  landed-cleanup endpoint can actually close. Asserts `ungrouped == ["legacy-exited","active-absent"]`
  style expectations. Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-07T21:17+02:00 — 260707-HFX-L6 review remediation: deck membership tests now
  expect the developer-facing architect chat plus backend orchestrator/strategist/manager command
  seats on the deck, and the at-scale fixture uses an architect command session. Verification
  metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-06T23:56:18+02:00 — 260703-L14 (visual hierarchy + chat grouping): created — deck
  membership by role provenance + orchestration claim, uncommanded-master grouping, the D3
  flat-run zero-group regression, landed/absent archive roll-up, the case-insensitive leaf join,
  and the 30-chat scale fixture. Verification metadata pinned until closeout stamps the L14 commit.
