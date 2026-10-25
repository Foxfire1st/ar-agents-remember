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
  It now also carries optional `unexplained_open`, a separately supplied stored-worklist open count,
  not an authored-intent or attribution total.
- `useIntentReviewSummary` loads `/api/review/intent/summary?repo&master&leaf`, including `comparison=<n>` only when one is supplied, through the store-owned bounded `intentSummaries` resource and shared `decodeReviewJson` decoder.
- `summaryRead` maps one answer to the render state `IntentSummaryRead`: `counted`/`partial` with
  counts, or `unavailable` with a `ReviewFailure` (`reviewProblemFromRefusal` for the owner's refusal,
  `unreadableAnswer` for a body that is none of the three shapes). `counts` and `problem` are never
  both present. `attribution`, when the body carries it, is kept on both the counted/partial state and the
  refused `unavailable` state (ruling 2026-09-30T12:19:20 Q6: the count shows even when the intent counts are
  refused); an unreadable body or a failed request carries none. `unexplained_open` is preserved as
  `unexplainedOpen` whenever it is defined, including measured zero, on either counted/partial or
  unavailable. The main `counts` and owner `problem` remain mutually exclusive; this does not
  prohibit independent auxiliary numbers beside an unavailable authored-intent result.
- `useIntentReviewSummary(repo, master, leaf, facts, comparison?, enabled = true)` waits while disabled, then reads for the task, facts and optional numbered comparison. The render key includes repo, master, leaf, facts and comparison (null when absent). Mounted/sequence checks drop superseded completions; `load` and `peek` both receive the same facts identity. A facts move shows loading until that identity has an answer, never retained old-facts counts. A thrown request becomes `unavailable` via `reviewProblemFromCause`.

### Conventions

Uses the shared review vocabulary (`ReviewFailure`, `ReviewRefusal`) from `./review`, so the entry and
the review surface classify the same codes the same way.

### Invariants And Boundaries

- **Three answers kept apart to the screen:** a measured `+0 −0` is `counted`; `partial` says it
  leaves subjects out; `unavailable` carries no authored-intent `counts`. Independent attribution or
  stored-open facts can remain present. The actual consumer renders the owner problem instead of
  authored plus/minus, while its separate open-work element can show a supplied auxiliary count.
- **`facts` is the caller's leaf-scoped invalidation value** (built by `panels/detail-panel/changeSetBar.tsx`),
  never the global analytics document.
- Transport only: no catalogue read and no count derivation here.
- **The lane's count arrives on this same response** (MIK-L32): the entry never asks for it more eagerly than for
  the intent counts, and it stays a separate field all the way to the screen (`intentReviewEntry.tsx`).

### Todos

`realization_only` and `membership_only` are carried but not displayed (worker observation O7); showing
them is a presentation choice owned by the later presentation leaves, not current intent.


## Current Behavior

`useIntentReviewSummary` creates an `AbortController` per effect, passes its signal to the store's summary load (`:126-131`), ignores an `AbortError` instead of mapping it to `unavailable`, and aborts on cleanup (`:136-140`). The mounted/sequence guard still drops a superseded completion. This supersedes 'Mounted/sequence checks drop superseded completions' as the whole account: a task switch now ends the request, not only its late answer. The facts identity remains leaf-scoped; the display key and store URL additionally distinguish the optional comparison number.

## Evidence

### Docs References

No Domain Documentation source is configured for this module.

No relevant domain documentation was found.

### Repo-Internal References



- The client state and mapping separate authored counts from failure while preserving defined auxiliary values on either declared answer state. [3]


- Attribution and defined unexplained_open are copied separately from authored plus/minus, including on the unavailable branch. [5]


- The mirrored server result constrains its declared outcome and optional non-negative stored-open field. [6]



- The consumer distinguishes main authored counts/problem, attribution and separate open-work count, and opens the task-bound review. [7]



- The shared cache shares pending work only for equal facts; supersession is abort-guarded before retained-value replacement or revalidation relabeling. [8]


### Cross-Repo References

No external-system boundary is implemented by this client. The cited server, consumer and store-cache owners are same-repository evidence.

- The component counts and result wire shape retain authored intent, optional attribution and optional stored-open facts. [1]
- The store-owned hook loads and peeks under the same task/facts key and drops superseded mounted completions. [2]
- Same-key retained fallback and mounted/sequence checks belong to the hook, not a second count computation. [4]
