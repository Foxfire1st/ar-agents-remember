# mcp/src/agents_remember/canvas/parts.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The page's parts and the claims nested in them: one derivation of `data-part` elements, their titles and the claim ids inside each, read by readiness and by per-part staleness alike.

## Code Commentary

- `part_id_problem` states the one bound on a part id — length and the `[a-z0-9-]` spelling — and refuses the reserved whole-page id, so a page, a protocol message and a part map cannot disagree about which ids exist.
- `derive_part_map` walks the page's own document once, resolves nesting to the innermost part that contains a claim, and keeps the order the page opens its parts in rather than the order they close.
- A page with no `data-part` element is one implicit part holding every claim, named `WHOLE_PAGE_PART`, which no page may declare itself.
- `_check_cross_part_claims` reports a claim that two parts both hold, and the walker reports a repeated id, an inadmissible id and a claim outside every part, so the readiness checks read raw material rather than re-parsing the page.

## Evidence

- The reserved whole-page part is the implicit part of a page that declares none, and a page may not declare that id [1]
- One function spells the bound on a part id for readiness, the protocol message and the part map [2]
- A page's parts are derived once from its own document, nesting resolved innermost and order kept as written [3]
- A claim two parts both hold is reported, because every claim belongs to one part only [4]
