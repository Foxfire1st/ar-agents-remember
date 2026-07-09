# dashboard/src/data/sessionGroups.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessionGroups.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-09T13:36:16+02:00                        |
| lastVerifiedCommitHash | `c392985424896e9f392507295a23c4902d0c0696`                                    |
| lastVerifiedCommitDate | 2026-07-09T14:31:11+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The pure **G1 command-tree derivation** for the Chats pane (260703-L14): `groupSessions({sessions,
taskDocuments, enclosures})` turns the flat hosted-session list into the grouped sidebar model —
the sprint's command deck on top, one collapsible group per claimed master, landed work rolled into
one archive — so a 20–30-chat orchestrated run reads at a glance while a flat run derives **zero
groups** and the sidebar renders exactly as before. Store-free and side-effect-free by design: the
component layer (`panels/SessionList.tsx`) renders the returned `GroupedSessions` verbatim, and all
the joins are unit-tested here rather than through the DOM.

## Code Commentary

### Logic

Known semantics (review L14R-5): a master named by TWO orchestration docs nests under the first in projection order — accepted first-wins behavior until the L15 pilot pins the orchestrates naming convention.

Membership is decided per session, in precedence order:

1. **Command deck** (`kind:"command"`, gold `orchestration` tier) — exists ONLY when an
   orchestration task exists (a `kind:"master"` doc with non-empty `orchestrates`; the D3 ruling).
   A session joins it by command-role spawn provenance (`spawnRole` ∈ architect / orchestrator /
   strategist / manager — the `COMMAND_ROLES` set, from the AR_SPAWN_ROLE recorded on the catalog row) OR by a
   leaf claim resolving INTO the orchestration task itself: its own qualified leaf key
   (`qualifiedLeafKey(orchestrationDoc)`) or any leaf in the orchestration task's folder — that
   second arm is how the developer-facing architect chat lands on the deck. Label:
   `{orchestration doc title} · command deck`.
2. **Master groups** (`master:{folder}`) — sessions whose qualified leaf key
   (`repo/master/leaf-id`, parsed by `leafKeySegments`) resolves to a **live** enclosure:
   `enclosureForLeafKey` matches `basename(taskRoot)` to the master segment, `leafId`
   case-insensitively (enclosure ids are slugified lowercase, doc ids authored uppercase — the same
   normalization the tasks tab uses), and `repoName` when the enclosure carries one; liveness is the
   shared `hasLiveWorktree` selector. The group takes the purple `management` tier + `nested: true`
   (one 22px indent step) ONLY when that master is commanded by an orchestration doc
   (`orchestratorParentKey` over `masterCommandNames`, or a raw folder match when no master doc is
   projected) — mirroring the tasks-tab grammar exactly. Label: master doc title, folder fallback;
   ordered by master `createdAt` then folder.
3. **Landed archive** (`kind:"landed"`, `defaultCollapsed: true`, unmarked — no tier) — sessions
   whose catalog status is explicitly `landed` always join the archive, even if their old enclosure
   is still projected. Legacy `exited` rows no longer join this archive; they stay ungrouped so the
   archive contains only rows the landed-cleanup endpoint can close.
4. **Ungrouped** — sessions with no leaf claim (and no deck membership) return in `ungrouped` and
   keep today's flat placement below the groups.

`countLabel` is precomputed per group — `"{n} chat(s) · {live} live"` with live derived from the
existing session state (`status ?? "running" === "running"`), the live suffix omitted at 0, and the
archive reading `"· archived"` instead. Only non-empty groups are emitted.

### Invariants And Boundaries

- **D3**: no orchestration task ⇒ no command deck, ever — command-role sessions then fall through
  the claim/ungrouped rules, and a claim-less flat run yields `{groups: [], ungrouped: sessions}`
  (the SessionList's unchanged-flat-list contract).
- Pure derivation over projected truth + the session registry: no persistence, no collapse state
  (collapse is UI-local in `SessionList`), no filesystem reads, and it never re-derives liveness
  from cleanup states — `hasLiveWorktree` is the only liveness rule.
- A running row with a missing enclosure is not inferred as landed anymore; it stays ungrouped unless
  the catalog says `status:"landed"`. This prevents projection gaps from prematurely archiving live
  chats.
- Legacy `exited` rows are not inferred as landed either; cleanup is intentionally aligned with the
  explicit `status:"landed"` backend recheck.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The orchestration-command helpers (isOrchestrationDoc / masterCommandNames / orchestratorParentKey) shared with the tasks tab. | L14 helper block | [taskHierarchy.ts](taskHierarchy.ts) |
| `qualifiedLeafKey` — the durable `repo/master/leaf-id` claim key this grouping parses. | `qualifiedLeafKey` | [taskIdentity.ts](taskIdentity.ts) |
| `hasLiveWorktree` — the shared live-vs-landed rule (L11 worktree truth). | L24-L28 | [selectors.ts](selectors.ts) |
| The `OpenSession` shape incl. the L14 `spawnRole` provenance field. | `OpenSession` | [sessions.ts](sessions.ts) |
| The component that renders this model (collapsible groups + flat remainder). | grouped branch | [SessionList.tsx](../panels/SessionList.tsx) |
| The Chats view that derives and threads the model. | `groupSessions` call | [Chats.tsx](../panels/Chats.tsx) |
| The membership/scale unit suite incl. the 30-chat fixture. | all cases | [sessionGroups.test.ts](sessionGroups.test.ts) |

## Update History

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
