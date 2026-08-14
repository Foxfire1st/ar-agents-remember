# dashboard/src/data/setChips.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setChips.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Pure shared presentation model for acceptance, pair, and route chips, queued composer hints, and
unacknowledged set attention.

## Code Commentary

### Logic

`deriveSetChips` orders pair state first, then per-kind pending and latest-unacknowledged ledger
evidence, then route errors. Route-terminated pairs use `routeErrorStep` to say effectiveness is
unknown; evidence-backed unsupported pairs keep the designed abort/refusal copy. The same models
feed the header, inspector-adjacent surfaces, and background toasts.

### Conventions

Every acceptance chip carries the acceptance word in `text`; tone never carries meaning alone.
Only 503 route errors are retryable.

### Invariants And Boundaries

Pending requested values never move effective markers. Clamp copy keeps both values; pair progress
spins only while an actual step remains active.

### Todos

- Reviewer sev-4 observation 4: a superseded `unknown` ledger entry can say a readback kept the
  prior value even though no readback resolved that superseded request.
- Reviewer sev-4 observation 7: an identical-value re-request temporarily hides the persistent
  clamp chip while the new in-flight chip is shown; attention remains held.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Chip ordering, copy selection, composer hint, and attention gate. | `deriveSetChips`; `queuedComposerHint`; `hasUnackedSetAttention` | dashboard/src/data/setChips.ts:192-229; dashboard/src/data/setChips.ts:232-238; dashboard/src/data/setChips.ts:241-245 |
| Full chip/pair/route/hint matrix. | "a 503 route error renders alarm with retry; other route errors carry no retry"; "true for unacked ledger entries and finished failed pairs; false otherwise" | dashboard/src/data/setChips.test.ts:158-189; dashboard/src/data/setChips.test.ts:217-232 |
| Copy source consumed by every chip. | `setWaitingCopy`; `setRouteErrorCopy` | dashboard/src/data/setControlsCopy.ts:19-21; dashboard/src/data/setControlsCopy.ts:60-74 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 3 repo-internal citation rows and preserved verification metadata.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R2/R5/R6 through fix round 3. Final PASS
  confirmed route failures no longer borrow SetResult certainty; sev-4 observations 4 and 7 remain
  recorded. Base verification metadata is temporary until code commit.
