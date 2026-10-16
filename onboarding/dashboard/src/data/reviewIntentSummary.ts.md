# dashboard/src/data/reviewIntentSummary.ts

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
- `useIntentReviewSummary` loads `/api/review/intent/summary?repo&master&leaf` through the store-owned bounded `intentSummaries` resource and shared `decodeReviewJson` decoder.
- `summaryRead` maps one answer to the render state `IntentSummaryRead`: `counted`/`partial` with
  counts, or `unavailable` with a `ReviewFailure` (`reviewProblemFromRefusal` for the owner's refusal,
  `unreadableAnswer` for a body that is none of the three shapes). `counts` and `problem` are never
  both present. `attribution`, when the body carries it, is kept on both the counted/partial state and the
  refused `unavailable` state (ruling 2026-09-30T12:19:20 Q6: the count shows even when the intent counts are
  refused); an unreadable body or a failed request carries none.
- `useIntentReviewSummary(repo, master, leaf, facts)` reads once per task context and again only when
  `facts` moves. The render key includes repo, master, leaf and facts. Mounted/sequence checks drop superseded completions; `load` and `peek` both receive the same facts identity. A facts move shows loading until that identity has an answer, never retained old-facts counts. A thrown request becomes `unavailable` via `reviewProblemFromCause`.

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

## Evidence

### Docs References

No Domain Documentation source is configured for this module.

No relevant domain documentation was found.

### Repo-Internal References

- The wire types mirroring the server model. [1]
- The render state and the answer mapping; an unrecognised body is unreadable, never drawn. [3]
- The lane's count carried on both answered states (MIK-L32). [5]
- The server model it mirrors. [6]
- The consumer. [7]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.

- [2]
- [4]
- Pending sharing is same-facts only; superseded transport cannot retain or relabel an answer. [8]
