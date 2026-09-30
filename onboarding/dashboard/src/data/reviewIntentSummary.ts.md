# dashboard/src/data/reviewIntentSummary.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewIntentSummary.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:18:54+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4` |
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

The client and hook for the changed-intent summary the task entry shows beside its Intent review control
(`ICR-R24@v3`, leaf `260921-ICR-L47`). It is the **one** read the entry makes for the reviewer before the
reviewer is opened; the subject catalogue is the reviewer's own and is not loaded here. The counts are the
comparison owner's (`mcp/src/agents_remember/application/review_intent_summary.py`); this client never
derives a count from change-set line totals or from catalogue size.

## Code Commentary

### Logic

- The wire types mirror the server model: `ReviewIntentSummaryResult` with `state`
  (`counted` | `partial` | `unavailable`), optional `counts` (`ReviewIntentCounts`: `added`,
  `removed`, per-kind `IntentHeadChanges`, `realization_only`, `membership_only`, `unresolved`)
  and optional `refusal`; since MIK-L32 also optional `attribution` (`ReviewLaneSummary` from `./reviewLane`), the
  unexplained-changes lane's file-level count a tree comparison's summary carries (MIK-R32 rule 9).
- `intentReviewSummary` GETs `/api/review/intent/summary?repo&master&leaf` through the shared
  `getReviewJson` decode.
- `summaryRead` maps one answer to the render state `IntentSummaryRead`: `counted`/`partial` with
  counts, or `unavailable` with a `ReviewFailure` (`reviewProblemFromRefusal` for the owner's refusal,
  `unreadableAnswer` for a body that is none of the three shapes). `counts` and `problem` are never
  both present. `attribution`, when the body carries it, is kept on both the counted/partial state and the
  refused `unavailable` state (ruling 2026-09-30T12:19:20 Q6: the count shows even when the intent counts are
  refused); an unreadable body or a failed request carries none.
- `useIntentReviewSummary(repo, master, leaf, facts)` reads once per task context and again only when
  `facts` moves. A sequence number drops a superseded answer, and an answer is only shown under the
  task key it was read for, so a previous leaf's late answer cannot land on the leaf shown now. A thrown
  request becomes `unavailable` via `reviewProblemFromCause`.

### Conventions

Uses the shared review vocabulary (`ReviewFailure`, `ReviewRefusal`) from `./review`, so the entry and
the review surface classify the same codes the same way.

### Invariants And Boundaries

- **Three answers kept apart to the screen:** a measured `+0 −0` is `counted`; `partial` says it
  leaves subjects out; `unavailable` carries no counts.
- **`facts` is the caller's leaf-scoped invalidation value** (built by `panels/detail-panel/changeSetBar.tsx`),
  never the global analytics document.
- Transport only: no catalogue read and no count derivation here.
- **The lane's count arrives on this same response** (MIK-L32): the entry never asks for it more eagerly than for
  the intent counts, and it stays a separate field all the way to the screen (`intentReviewEntry.tsx`).

### Todos

`realization_only` and `membership_only` are carried but not displayed (worker observation O7); showing
them is a presentation choice owned by the later presentation leaves, not current intent.

## Docs References

No Domain Documentation source is configured for this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wire types mirroring the server model. | `ReviewIntentCounts`; `ReviewIntentSummaryResult` | dashboard/src/data/reviewIntentSummary.ts:39-47; dashboard/src/data/reviewIntentSummary.ts:49-58 |
| The route request through the shared decode. | `intentReviewSummary`; `getReviewJson`; "/api/review/intent/summary" | dashboard/src/data/reviewIntentSummary.ts:60-68 |
| The render state and the answer mapping; an unrecognised body is unreadable, never drawn. | `IntentSummaryRead`; `summaryRead`; `unreadableAnswer` | dashboard/src/data/reviewIntentSummary.ts:72-90 |
| The hook: one read per task context and per `facts`, superseded answers dropped. | `useIntentReviewSummary`; `reads.current === seq` | dashboard/src/data/reviewIntentSummary.ts:96-121 |
| The lane's count carried on both answered states (MIK-L32). | "attribution?: ReviewLaneSummary;"; "const attribution = result.attribution ? { attribution: result.attribution } : {};" | dashboard/src/data/reviewIntentSummary.ts:57-57; dashboard/src/data/reviewIntentSummary.ts:79-90 |
| The server model it mirrors. | `ReviewIntentSummaryResult` | mcp/src/agents_remember/models/knowledge/review_intent_summary.py:93-123 |
| The consumer. | `useIntentReviewSummary` | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:131-171 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): **body update for MIK-R32.** Logic records the optional `attribution` (the lane's `ReviewLaneSummary`) and that `summaryRead` keeps it on the counted/partial and refused states (ruling 2026-09-30T12:19:20 Q6); an Invariants bullet records that it arrives on this same response. One row added. The moved rows were re-pointed by the installed fixer's normalisation or by the exact base-to-staged shift. No verification stamp was advanced.
- 2026-09-28T17:06:50+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the changed-intent summary client and hook (`ICR-R24@v3`). The verification pair names the code base; closeout owns the real stamp.
