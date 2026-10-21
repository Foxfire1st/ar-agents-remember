# mcp/src/agents_remember/application/knowledge_writer/repoint.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The judged route between two refusals a `still_rejected` row used to loop through: a `reconsider_on`
link whose base target has no image at C, and the same link refused as re-authored once a leaf moved it
by hand.** A leaf may delete the symbol a decision's `reconsider_on` link names (MIK-R194 problem 2).
Left as it is, the link cannot be mapped to C; re-authored by hand, it is refused as re-authored.
`RepointRowAuthoring` (rules 4 to 7) admits a `repoint` list on that row — one item per fired link,
`{link, path, locator}`, naming where the code that `reconsider_when` is about now lives at C — and
writes the decision with the re-pointed links, its revision raised once in the leaf. Nothing here
derives a target, answers an item or writes a rejection: a re-point exists only because a curator wrote
one in a hand-off, and a fired link with no row still reaches the curator's worklist and blocks
closeout (rule 8, D430).

## Code Commentary

### Logic

- **`repointed_links(document, index, context, repoints)`** judges each item and returns
  `RepointOutcome(links, problems, judged, items)`. An admitted item replaces that link's `target`; a
  refused one adds `links.<i>: why`, as the refresh's own refusals do. The links left alone are handed
  to `refreshed_links` with the re-pointed positions removed from the answered item's fired facts, so
  every other fired link refreshes exactly as today. `judged` is true when an item was admitted or the
  refresh newly judged a link.
- **Admission (`_admission`).** The item must name a link that fired on the answered item, its trigger
  must be one of `REPOINTABLE` (`anchor`, `anchor_stale`, `refresh_not_current`), the link must still be
  a `reconsider_on` link of the answered alternative (else "recompute the worklist"), and a
  `refresh_not_current` item must be answered by naming that item in the row's `items`.
- **One item (`_item`).** The fired base target must be known with its path, or the row must `raise`
  instead; the new target is resolved at C by the caller's resolver (`_resolved`), so a target that
  does not resolve at C refuses the item. An anchor-triggered item is admitted when the link still
  stands at its base target or already names this same re-point; a link whose base target still maps to
  C keeps its refresh ("remove its repoint"); any other current target is "restore its base target in
  `records`, or `raise`".
- **`refresh_not_current` (`_refresh_refusal`).** Such an item fired because the link no longer holds
  the target an earlier refresh wrote, so only that target — or the identical re-point a rerun would
  write — may be replaced. A link still at its base target is "recompute the worklist"; any other
  target means another answer stands between them, and overwriting it would discard a judgment someone
  else made (rule 4d).
- **Continuity is exact.** `_same_target` compares a stored link with a fired fact through
  `link_target_key` (`<path>@<blob>#<content>`), and `_earlier_refresh` reads the earlier refresh from
  the item's `entry.anchor`; `_already` compares path, locator and content with what resolves at C, so
  a rerun of the same re-point writes the same bytes.
- **`RepointRowAuthoring(HistoryRowAuthoring)` overrides only `_reconsideration_row`.** With no
  `repoint` it writes the inherited row and notes the route when the answered item fired on a refresh
  that no longer stands; with one it refuses a `raise` ("a raise leaves the links as they are and asks
  the developer"), then uses the inherited `_common_row`, `_answered_item` and `_place_record`.
  `_judge_repoints` reads the decision from the subject, takes the item's fired facts, the base record
  and C, runs `repointed_links`, names every refusal, and places the record once; `_place_repoint`
  returns without a bump when the produced links are already the stored ones; `_stored_repoint_row`
  validates the stored shape through `ReconsiderationRow` before the row is written.
- **The report (`_note_repoints`).** Each re-point is reported with its link, both paths and the row's
  reason; `_describe` spells the locator it replaced and the one it wrote (a symbol, a line range, or
  the whole file).

### Conventions

- Every refusal reads `links.<i>: why`; the row-level ones are prefixed "the still_rejected re-point is
  refused: ".
- The module imports the writer's public link helpers (`fired_target`, `link_at`, `refreshed_target`,
  `Answer`, `CodeAtC`) instead of re-implementing them, so a re-point judges a link exactly as the
  refresh does.

## Invariants And Boundaries

- **A re-point's target comes only from the curator's hand-off.** `repointed_links` admits items and
  refuses them; nothing here derives a target, answers an item, keeps a rejection or authors one, and a
  fired link with no row still reaches the worklist and blocks closeout (rule 8, D430).
- **An item is admitted only where it can answer the link's own trigger.** For `anchor` and `anchor_stale` the
  fired base target must have no image at C and the leaf's link must still be the base target or already this
  same re-point; for `refresh_not_current` the row must name the item, and the link must hold the earlier
  refresh this item fired on, or this same re-point. For those two triggers a link that still maps is
  refreshed as today and its `repoint` is refused; a trigger outside `REPOINTABLE` is "leave it to the
  refresh".
- **A rerun of the same re-point writes the same bytes.** A link that already names the item's target
  is admitted, `_place_repoint` sees the produced links equal to the stored ones, and nothing is bumped.
- **`raise` carries no `repoint`.** The override refuses it by name; a raise leaves the links as they
  are and its question says where the code lives.
- This module judges links and places the decision. It does not compute a worklist, decide what fired,
  write a task-document question or undo an earlier refresh (`refresh_restoration` owns that).

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or
landing result. No Domain Documentation source is configured for this slice; no external-system
guarantee is inferred.

## Evidence

- `repointed_links` re-points the named fired links, refreshes every other fired link as today, and returns the links, the refusals, whether anything was judged and the row's stored items. [1]
- An item is admitted only for a link that fired on the answered item with `anchor`, `anchor_stale` or `refresh_not_current`, and that is still a `reconsider_on` link of the answered alternative; a `refresh_not_current` item must be named in the row's `items`. [2]
- An anchor-triggered item is admitted when the link stands at the fired base target or already names this re-point; a link that still maps to C keeps its refresh, and any other current target is refused. [3]
- A `refresh_not_current` item may replace only the earlier refresh it fired on, or the identical re-point a rerun writes; any other current target refuses with "recompute the worklist, or `raise`". [4]
- The new target is resolved at C, and a link that already names that path, locator and content changes nothing on a rerun. [5]
- `RepointRowAuthoring` overrides only `_reconsideration_row`: with no `repoint` the inherited row is written and the refresh route is noted, and a `raise` carrying `repoint` is refused by name. [6]
- The decision is placed once with the re-pointed links, and a rerun that produces the stored links bumps nothing. [7]
- Each re-point is reported with its link, both paths and the row's reason. [8]
