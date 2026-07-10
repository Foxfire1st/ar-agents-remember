# dashboard/src/data/sessionGroups.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionGroups.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `79b2fd6c4da73c7845406f6c68b947b8bd0e1009`                                    |
| lastVerifiedCommitDate | 2026-07-10T22:22:16+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The pure L16 rail-grouping derivation for the Chats pane. `groupSessions({sessions,
taskDocuments, enclosures})` partitions the flat hosted-session catalog into one box per
repo-qualified sprint claim, the explicit landed archive, an explicit malformed-claim group, and
the claim-less remainder. Grouping no longer depends on a live enclosure, so a valid
`repo/master/leaf-id` claim stays with its sprint through worktree transitions. Store-free and
side-effect-free by design: `panels/SessionList.tsx` owns rendering and collapse only.

## Code Commentary

### 260707-HFX2-L17 Current-Seat Group Classification

Command-deck classification now uses `sessionSeatRole`, so a hand-opened/rebound architect,
orchestrator, strategist, or manager is grouped by current binding identity instead of stale or
missing spawn provenance. Sprint qualification, archive grouping, and malformed-claim handling are
unchanged.

### Logic

Membership is decided per session, in precedence order:

1. **Landed archive** (`kind:"landed"`, `defaultCollapsed: true`, unmarked) — sessions
   whose catalog status is explicitly `landed` always join the archive, even if their old enclosure
   is still projected.
2. **Malformed claim** — a non-empty leaf key with fewer than three path segments enters the
   `error` group labelled `unresolvable session claims`; malformed rows are never silently orphaned.
3. **Repo-qualified sprint** — every valid claim groups by `${repo}/${master}`, independent of
   enclosure presence or liveness. The key is `sprint:${repo}/${master}`; a matching master doc
   supplies title and creation order, otherwise the qualified key is the honest fallback.
4. **Ungrouped** — sessions without a leaf claim remain in the flat remainder. Claim-less command
   roles are not swept into an unrelated deck.

A sprint becomes `kind:"command"` with the gold orchestration tier only when one of its own members
has command-role provenance or claims the orchestration document itself. A commanded master uses
the purple management tier and one indent step. Because `orchestrates` stores bare folder names,
that fallback is guarded by `doc.repository === repo`; same-named masters in another repository
cannot inherit command styling. Sprint groups sort by master `createdAt`, then qualified key.

`countLabel` is precomputed per group — `"{n} chat(s) · {live} live"` with live derived from the
existing session state (`status ?? "running" === "running"`), the live suffix omitted at 0, and the
archive reading `"· archived"` instead. Only non-empty groups are emitted.

### Todos

- Reviewer D-N3: the rail's `commanded` fallback matches bare folder names plus repository, while
  `LifecycleList` also accepts master id/title aliases through `masterCommandNames`. Current task docs
  use folder names, so the surfaces agree on real data; align the name vocabulary if id/title entries
  become supported orchestration input.

### Invariants And Boundaries

- Repo is part of the grouping and command-style key; folder names alone never cross repositories.
- Valid claims survive absent or non-live enclosures; only explicit `status:"landed"` selects the
  landed archive.
- No orchestration task means no command deck. A claim-less flat run still yields zero groups.
- Pure derivation only: no persistence, filesystem reads, liveness derivation, or collapse state.
- `enclosures` remains in the public input for caller compatibility but L16 grouping does not consult it.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The derivation parses qualified claims, repo-guards command styling, emits sprint/archive/error groups, and leaves claim-less rows flat. | L48-L159 | [sessionGroups.ts](sessionGroups.ts) |
| `qualifiedLeafKey` supplies the durable orchestration-document claim used for command-deck membership. | L1-L63 | [taskIdentity.ts](taskIdentity.ts) |
| The renderer consumes these groups and builds a complete spawn-edge forest inside each member set. | L242-L484 | [SessionList.tsx](../panels/SessionList.tsx) |
| The unit suite pins repo isolation, enclosure-independent grouping, malformed-claim surfacing, and the 30-chat shape. | L90-L277 | [sessionGroups.test.ts](sessionGroups.test.ts) |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: made command-deck role classification binding-first;
  no change to L16 sprint grouping or archive semantics.

- 2026-07-10T13:41+02:00 — 260707-HFX2-L16: replaced the global G1 deck/live-enclosure join
  with repo-qualified sprint groups, preserved valid claims without live enclosures, added the
  explicit malformed-claim group, and repo-guarded the bare-folder `orchestrates` fallback.
  Claim-less command roles remain flat; landed membership remains explicit-status-only. Verification
  metadata stays pinned until closeout stamps the eventual L16 code commit.

- 2026-07-09T13:36+02:00 — 260707-HFX2-L11 round 2: stopped folding legacy
  `status:"exited"` rows into the landed archive because the cleanup endpoint closes only rows still
  `status:"landed"`; exited rows now remain ungrouped and individually closable. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L11 commit.

- 2026-07-09T13:07+02:00 — 260707-HFX2-L11 (landed chat archive): landed grouping is now
  catalog-status-backed. `status:"landed"` wins over command/master membership and goes to the
  collapsed archive; legacy `exited` rows with missing/non-live enclosures still archive, but running
  rows with projection gaps remain ungrouped. Verification metadata remains pinned until closeout stamps
  the HFX2-L11 commit.

- 2026-07-07T21:17+02:00 — 260707-HFX-L6 review remediation: command-deck membership now
  includes `architect` spawn-role provenance alongside backend orchestrator/strategist/manager,
  and the orchestration-task claim is described as the developer-facing architect chat rather than
  an orchestrator chat. Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-06T23:59:56+02:00 — L14 review follow-up (L14R-5): first-wins double-command semantics documented. Verification metadata pinned until closeout stamps the L14 commit.

- 2026-07-06T23:56:12+02:00 — 260703-L14 (visual hierarchy + chat grouping): created — the pure G1
  command-tree derivation (deck by role provenance + orchestration claim, master groups by live
  leaf claim, landed/absent archive, ungrouped flat remainder; D3 deck-only-when-orchestrated;
  precomputed countLabels). Verification metadata pinned until closeout stamps the L14 commit.
