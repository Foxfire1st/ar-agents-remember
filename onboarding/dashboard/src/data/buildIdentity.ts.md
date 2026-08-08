# dashboard/src/data/buildIdentity.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/buildIdentity.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T12:43+02:00 |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`|
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

This module is the browser-side build-identity seam. It exposes the dashboard fingerprint embedded
by Vite at bundle time and compares it with the optional fingerprint reported by the serving
process, allowing the shell to distinguish a matching client/server pair from a stale loaded page.

## Code Commentary

### Logic

`CLIENT_DASHBOARD_BUILD` is the compile-time `__AR_DASHBOARD_BUILD__` value. The pure
`clientMatchesServingBuild` helper returns `null` when an older server omits `dashboardBuild`, and
otherwise returns exact string equality. It diagnoses identity only: reload remains an explicit
operator action owned by the cockpit, never an automatic loop in this data module.

### Conventions

The compile-time constant is exposed through one named export, and comparison stays pure so UI
tests can exercise identity without rebuilding or mutating browser state.

### Invariants And Boundaries

- An absent server fingerprint is unknown compatibility, not a mismatch.
- Exact fingerprint equality is the only positive match signal.
- This module does not fetch state, mutate browser location, or infer identity from commit hashes.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

### 2026-07-24 Curator Delta

`servingCommitLabel` now appends `*` when the serving checkout was dirty at boot. The compact label
keeps the stamp readable while the cockpit tooltip supplies the explicit dirty explanation; an absent
commit still falls back to version identity rather than inventing a hash.

## Docs References

No relevant documentation was found after checking the configured sources; current claims are
proven by repository source and direct consumers.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external or domain documentation is configured for this repository-local seam. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Declares the optional server fingerprint consumed by the comparator. | `ServingBuild` | dashboard/src/types/projection.ts:388-394 |
| Renders the comparison and owns the explicit reload action. | `ServingBuildStamp` | dashboard/src/cockpit/Cockpit.tsx:923-953 |
| Embeds the fingerprint into the compiled client. | `__AR_DASHBOARD_BUILD__` | dashboard/vite.config.ts:65-65 |

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local seam.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | — | — |

## Update History
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 6 citations (citation_anchor_missing=3, citation_prose_not_in_cit_form=0, citation_source_malformed=3); final scoped citation check clean.
- 2026-07-24T13:17:50Z — Documented dirty serving-build labels and their compact/tooltip split.
  Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T12:43+02:00 — FEUI-L9R: created the one-to-one card for the candidate build-identity
  module; verification metadata stays blank until the code candidate is committed and closeout can
  stamp it.
