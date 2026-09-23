# mcp/src/agents_remember/application/review_pagination.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_pagination.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T00:15:00+02:00 |
| lastVerifiedCommitHash | `4c000b11c5243e4a8e77c08e87984fff00c1d94b` |
| lastVerifiedCommitDate | 2026-09-23T20:33:15+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[mcp/src/agents_remember/application route overview](overview.md)

## Purpose

The review surface's **page arithmetic** for `ICR-R10@v1`: how one bounded collection's page is
*stated* on the review surface. Two collections are composed into one review — the **knowledge
comparison**, whose page is the shipped comparison's own window of its before/after union, and the
**review matrix records**, whose page is the shipped view's own window of its selection — and this
module owns the one thing that is neither owner's: the page value the response publishes.

The two ownership boundaries the module exists to hold are stated in its own docstring:

- **It mints no cursor and re-derives no binding.** The continuation a page publishes is the owner's
  own opaque token carried verbatim — the comparison's `knowledge-diff-cursor/v1` for the knowledge
  collection, the view's snapshot-bound continuation for the records collection. That is what keeps
  one pagination authority rather than two, and it is why the collections are *named* rather than
  uniform: a cursor presented to the other walk is refused by that owner rather than served as a slice
  of it.
- **The counts are the owner's own.** `total`, `returned` and `remaining` are read off the
  comparison's `KnowledgeDiffCounts` and the view's `ViewCounts` exactly as those owners published
  them; nothing here subtracts two of them to invent the third.

A cursor that no longer binds is a **reset, not a fallback**: the owner's own typed rejection is mapped
onto the surface's single `comparison_page_reset` refusal carrying the owner's expected/observed
identities, and the page served beside it is the *current* comparison's first page rather than a window
stitched from two generations.

## Code Commentary

### Logic

**`MOVED_SNAPSHOT_CODES` is exactly one code — the owners' binding mismatch.** The comparison's own
binding mismatch and the view's own snapshot mismatch are both spelled `continuation_binding_mismatch`,
and that alone is mapped onto the new-generation action. Everything else keeps the owner's own next
action and is reported as `comparison_page_unreadable`, because telling a reader to open a new
comparison when nothing moved would be a false statement about what happened.

**The two directions are told apart by asking the owner's own decoder, not by reading refusal text.**
`comparison_reset` calls `continue_diff_from_cursor` on the presented token: a token the comparison's
decoder reads back *is* one of its cursors, so a refusal on it is a binding mismatch and earns the
new-generation action; a token it does not read back was never this collection's, so the caller's
mistake is about *which walk* the token belongs to and the owner's own remedy travels through instead.

**`records_page_refusal` names the token the reader actually sent.** The view's own snapshot refusal
names its *view* as the offending input — true of the walk, useless to the reader — so the presented
cursor is named instead: it is the value the reader sent and the value they must discard. A view
refusal for a reason that is not about the cursor at all (an unreadable snapshot, an ambiguous row set)
is published as `comparison_refused` with the owner's own words, because none of those is a statement
about a page.

**`comparison_page` and `records_page` publish the pair of numbers the owners actually measured, and
declare what `total` counts.** The comparison measures its whole selection, so its total is the
selection's own size on every page and `returned` is cumulative over the walk. The view measures its
remainder from where the *walk* stands, so its `total` is `returned + remaining` — the size of the
selection this walk still covers — and `records_page` checks the rows it returned against the bound the
caller asked for, because a page that reports a bound it did not apply is how a narrow window comes to
read as the whole selection.

**`reset_comparison_page` is the packet's failure behavior made one value.** A cursor for a moved
snapshot is refused with the explicit new-generation action, and the page that travels with the refusal
is the first page of the comparison that is there now — the last coherent page of this generation —
rather than no page, an empty page, or a window taken at a position from the generation that moved. The
refused cursor stays named on the refusal's own `offending_input`/`expected`/`observed` identities, and
`continued_from` is `None` because a reset page followed nothing.

**`RecordsPagePosition` is one value rather than four arguments** because the four describe one thing —
the page's own position in its walk. A caller that could pass three of them could state a page whose
scope, cursor and bound disagreed with each other.

### Conventions

- One responsibility per module: this is the page arithmetic beside the review adapter, and the adapter
  delegates to it rather than repeating it.
- The page vocabulary (`ReviewCollectionPage`, `REVIEW_PAGE_RESET_NEXT_ACTION`,
  `MAXIMUM_REVIEW_PAGE_SIZE`, the two page refusal codes) lives in
  `models/knowledge/review.py`, where the surface's other published shapes live.
- The owners' words travel through unchanged where the owner's own reason is the answer; the surface's
  own action is substituted only where the surface is stating a fact the owner cannot (a page whose
  generation moved).

### Invariants And Boundaries

- **No second pagination authority.** No cursor type, no binding digest and no re-derivation of an
  owner's counts is created here — the codecs stay with the comparison and the view.
- **A page with a remainder cannot exist without its cursor.** That is enforced by
  `ReviewCollectionPage._require_one_walk` at construction, not by a rendering convention.
- **A refused cursor is never re-resolved** against the generation that is there now; the reset page is
  a *new* first page, labelled `state="reset"` with the refusal beside it.
- Untouched: the shipped entry read stays a catalogue that fetches no record page, and the page size is
  admitted by the route (see `serving/review.py`), not by this module.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

`ICR-R10@v1`'s scope clause says the new internal module belongs beside its reuse/extension owners and
must not duplicate their implementation; this card records which half of the responsibility landed
where.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what it owns, of the one cursor authority it reuses, and of the reset rule.** | `MOVED_SNAPSHOT_CODES`; `RecordsPagePosition` | mcp/src/agents_remember/application/review_pagination.py:1-29; mcp/src/agents_remember/application/review_pagination.py:68-88 |
| **The one moved-snapshot code: the owners' own binding mismatch, and the two directions told apart by the owner's decoder.** | `MOVED_SNAPSHOT_CODES`; `comparison_reset` | mcp/src/agents_remember/application/review_pagination.py:59-73; mcp/src/agents_remember/application/review_pagination.py:91-124 |
| The refusal for a cursor that is not this collection's cursor at all, keeping the owner's own words and remedy. | `unreadable_page_refusal` | mcp/src/agents_remember/application/review_pagination.py:127-149 |
| **The matrix refusal: the binding mismatch takes the surface's action, every other view refusal keeps the owner's, and the presented token is named rather than the view.** | `records_page_refusal` | mcp/src/agents_remember/application/review_pagination.py:152-199 |
| The four fields of one page's position in its walk, as one value. | `RecordsPagePosition` | mcp/src/agents_remember/application/review_pagination.py:76-88 |
| **The comparison window stated as the surface's page: `total_basis="selection"`, cumulative `returned`.** | `comparison_page` | mcp/src/agents_remember/application/review_pagination.py:202-230 |
| **The view window stated as the surface's page: `total_basis="walk"`, and the returned rows checked against the bound the caller asked for.** | `records_page`; `RecordsPagePosition` | mcp/src/agents_remember/application/review_pagination.py:233-269; mcp/src/agents_remember/application/review_pagination.py:76-88 |
| **The reset page: the current comparison's first page served beside the refusal, with the refused cursor named on the refusal.** | `reset_comparison_page` | mcp/src/agents_remember/application/review_pagination.py:272-305 |
| The one reader of a view quantity, so a page can never publish an unmeasured count. | `_counted` | mcp/src/agents_remember/application/review_pagination.py:308-314 |
| **The published page value this module builds, with the constructor check that refuses a remainder without a cursor.** | `ReviewCollectionPage`; `_require_one_walk` | mcp/src/agents_remember/models/knowledge/review.py:465-465 |
| The surface's own new-generation action and the maximum page size the request model admits. | `REVIEW_PAGE_RESET_NEXT_ACTION`; `MAXIMUM_REVIEW_PAGE_SIZE` | mcp/src/agents_remember/models/knowledge/review.py:192-196; mcp/src/agents_remember/models/knowledge/review.py:181-185 |
| The two collections named once, because their cursors are different documents. | `ReviewPagedCollection` | mcp/src/agents_remember/models/knowledge/review.py:169-169 |
| The two page refusal codes on the closed refusal-code union. | `comparison_page_reset`; `comparison_page_unreadable` | mcp/src/agents_remember/models/knowledge/review.py:157-158 |
| The one consumer: the adapter offers a request's cursor to the collection it names and states the page this module returns. | `compose_review` | mcp/src/agents_remember/application/knowledge_review.py:321-479 |
| **The route that admits the page size in its own vocabulary before the request model sees it.** | `_admitted_paging`; `paged_review_request` | mcp/src/agents_remember/serving/review.py:517-517; mcp/src/agents_remember/serving/review.py:293-357 |
| The client that renders these pages without ever constructing a cursor. | `carriedPage`; `pageBounds` | dashboard/src/data/review.ts:548-569; dashboard/src/data/review.ts:578-580 |

## Cross-Repo References

No cross-repository behavior is exercised in this file. Both owners are this repository's own store
readers, and every count on a page is measured inside the same process.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T00:15:00+02:00 — 260921-ICR-L10 curator: **created.** The module is new in this leaf
  (`ICR-R10@v1`, complete bounded pagination) and this is its one-to-one card. It records the two
  ownership boundaries a later reader would otherwise have to rediscover from the diff — the cursor is
  always the owner's own opaque token and is never minted or re-bound here, and the three counts are
  read off the owners rather than derived — plus the one distinction the fix rounds turned into code:
  the moved-generation reset is the owners' single binding-mismatch code, told apart from a foreign
  cursor by asking the owner's own decoder rather than by reading refusal text. **Stamp accounting:**
  the verification pair names the **production line at this leaf's base**
  `dcf35a0e0fc06bccdafd22390b7588b0aea811bc` (2026-09-22T20:08:58+02:00); everything this card
  describes is **uncommitted** working-tree bytes in the `ar/260921-icr-l10` worktree, so no commit
  contains them and closeout owns the real stamp.
