# dashboard/src/data/setClient.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setClient.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md`                                   |

## Governing Overview

[data overview](overview.md)

## Purpose

The sole live-session set-control I/O driver: exact-session snapshot reads, model/effort POSTs,
serialized pair changes, effort cycling, acknowledgment, and promotion/drift observation.

## Code Commentary

### Logic

- `refreshSessionSnapshot` single-flights GETs by session, mirrors either the whole snapshot or
  the verbatim classified error, and resolves queued/unknown pendings by readback.
- `sendSet` POSTs the exact model/effort route, treats every valid SetResult as evidence, and
  keeps route failures separate. `applySetResult` appends all evidence, supersede-guards the
  current pending, moves effective values only from echo evidence, and performs one automatic
  readback for `unknown`.
- Pair changes serialize model evidence before effort. Route termination records unknown
  effectiveness; SetResult-backed refusal preserves the stronger evidence wording.
- The refcounted promotion watcher re-GETs focused turn-ended sessions, queued/unknown background
  sessions at turn end, and sessions that gain focus.

### Conventions

Pure policy stays in `setAcceptance.ts`, `pairChange.ts`, and `sessionCapabilities.ts`; this module
only sequences I/O and store writes. Announcements are emitted only for the focused session.

### Invariants And Boundaries

No request or in-flight state moves an effective marker. HTTP failures never become SetResults,
and an older response never clears a newer request's pending state.

### Todos

- Reviewer sev-4 observation 5: a `turn-ended` transition that occurs entirely between observed
  session-store snapshots cannot trigger the promotion watcher.
- Reviewer sev-4 observation 8: the automatic unknown readback can join an already in-flight
  exact-session GET rather than force a later post-result GET.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact snapshot, set, pair, cycling, acknowledgment, and watcher orchestration. | `refreshSessionSnapshot`, `sendSet`, `startPairChangeFlow`, `acknowledgeSetAttention`, `cycleEffortRequested`, `startSetPromotionWatcher` | dashboard/src/data/setClient.ts:72-119; dashboard/src/data/setClient.ts:228-274; dashboard/src/data/setClient.ts:375-383; dashboard/src/data/setClient.ts:386-391; dashboard/src/data/setClient.ts:405-426; dashboard/src/data/setClient.ts:450-497 |
| Full I/O and transition regression matrix. | "sendSet — wire + honesty table application", "refreshSessionSnapshot (R1/F16)", "serialized pair change (R5)", "cycleEffortRequested (R7)", "startSetPromotionWatcher (R4 + v3 drift delta)" | dashboard/src/data/setClient.test.ts:64-697 |
| Acceptance and readback policy. | `reduceSetResult`, `resolvePendingsByReadback` | dashboard/src/data/setAcceptance.ts:101-153; dashboard/src/data/setAcceptance.ts:204-232 |
| Pair serialization machine. | `startPairChange`, `applyPairStepResult`, `applyPairReadback` | dashboard/src/data/pairChange.ts:50-52; dashboard/src/data/pairChange.ts:58-111; dashboard/src/data/pairChange.ts:156-196 |
| Store state and mutation boundary. | `SessionCockpitState`, `sessionCockpitStore` | dashboard/src/data/sessionCockpitStore.ts:209-268; dashboard/src/data/sessionCockpitStore.ts:588-601 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## FEUI-L8 Reviewed Candidate Delta

Adds a dev-scenario generation around exact-session snapshot single-flight state. Retired requests may resolve to their caller but cannot write into a successor scenario that reuses the session id.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T03:59:59+02:00 — Curated 10 citation claims (5 table rows, 5 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R1–R8 through fix round 3 and final
  reviewer PASS. Sev-4 observations 5 and 8 remain recorded. Verification metadata is pinned to
  the contract base until the uncommitted code lands.
