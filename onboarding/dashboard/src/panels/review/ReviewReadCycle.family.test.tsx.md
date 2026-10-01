# dashboard/src/panels/review/ReviewReadCycle.family.test.tsx

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Protect exact bounded family continuation through the real client/read hook and mounted review, using complete bodies captured from public authorship and the real HTTP route.

## Code Commentary

### Logic

The capture supplies before and after walks at a fixed page size. The positive flow preserves exact content and claims as those walks advance independently, including identical replay and repeated first pages from another side. Primary statement/evidence and the complete inventory remain their response owners' values.

The negative cases begin with coherent accumulated context. Wrong cursor, comparison, snapshot, subject, namespace, family revision, stale state, immutable content and structured page refusal must fail visibly without installing the rejected response. An unadvertised request cursor receives the same admission check. Whole-review refusal still suppresses the display through the existing outcome rule.

Mounted cases inspect the displayed statement, evidence, sibling rows, inventory, continuation and owner recovery text. The actual family-detail branch distinguishes content-only pages, a fully accumulated roster and unavailable scope. Refresh and changed subject/history reset accumulation; a late superseded response cannot restore an older question. Focus, layout and open-file state survive a legitimate continuation.

### Conventions

Only fetch and the separately tested catalogue hook are isolated. Since L48 `useReviewReadCycle` requires the surface's `ReviewReadCache`, so the hook harnesses (`mountCycle` and the reset case) each construct a fresh cache; a fresh cache per mount means no case is answered from another case's reads. Successful review bodies come from the capture; deliberate corruptions are negative probes. The capture is `familyPaging.captured.json`. **MIK-L31 re-captured it from the current route** (MIK-R31 rule 6, the L44-R1-F5 remainder: L44's producer, first build accepted, one attempt; the receipt's `mik_l31_recapture` entry at the L10-synced tree `18b77329`), so its member sources now carry `locator`, `resolved_ranges` and `locator_state`. Because family order follows the stored identities each build draws afresh, the late-source-expression case now opens the subject inside the capture's own `family_id` explicitly rather than relying on that family being listed first. The module header (lines 22-28, refreshed by a comment-only follow-up) says so, and says why the cases open the walked family by its `family_id`. Source-content requests receive their own explicit test refusal when a case measures selection rather than served bytes. This is mounted component evidence, not installed-browser or whole-product acceptance.

### Invariants And Boundaries

A rejected response is never a successful replacement. Exact identity and complete preserved populations matter; text coincidence and passing merge helpers alone do not establish display safety. The capture is regression evidence, never the repository's live knowledge foundation.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured. These implementation-specific contracts are supported by repository source.

No configured domain source could be checked.

### Repo-Internal References

The cases below exercise the actual read cycle and rendered outcome boundary.

- **The header's provenance paragraph: bodies from the public authorship and real review route; `familyPaging.captured.json` re-captured by MIK-L31 and recorded in the receipt; the walked family opened by its `family_id`.** [1]
- The harness uses the captured HTTP bodies and existing read cycle, with its own fresh read cache. [2]
- Independent exact walks retain content and claims. [3]
- Failed admission retains the coherent display and failure details. [4]
- Unadvertised cursors are checked without weakening whole-review refusal. [5]
- The family-detail branch states loaded, complete and unavailable scope. [6]
- Refresh, changed questions and late responses cannot reuse old context. [7]
- A late source expression becomes reachable beside preserved intent and workspace state; the walked family is opened by the capture's own `family_id`. [8]
- The production owner admits or rejects continuation before retaining data: the read cycle decides when (`familyContinuationRead`), and since L48 the merge it applies lives in `familyWalkMerge.ts`. [9]

### Cross-Repo References

No external repository or live service is exercised by these mounted cases.

No cross-repository reference is required.
