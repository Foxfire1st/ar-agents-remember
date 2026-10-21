# mcp/src/agents_remember/memory_quality/style/citations/test_case_ranges.py

## Governing Overview

[memory quality overview](../../overview.md)

## Purpose

**Which case a line range is, and why a range is no case at all (MIK-R194 rule 2).** A proof may name an
`it.each` case, a `for` table, a computed title or a title bound twice by the exact lines the case
occupies. This module answers whether a range is one case that runs and that no name reaches, and
otherwise names the reason in the writer's words. It reads the syntax nodes `grammars.py` parses: that
direction is fixed, because `grammars` imports `test_cases`, and nothing here may be reachable from it.

## Code Commentary

### Logic

- **`case_at(path, nodes, start, end, reaches=None)`** picks the cases out of the walked nodes and
  answers the one whose `span_of` equals the range exactly. Any other range is refused, naming the
  cases it overlaps.
- **Admission, in order.** `_admitted_or_refused` asks `blocking_reason` first: a `.skip`, `.todo`,
  `.skipIf`, `.runIf` or `.fails` on the case or on any enclosing suite refuses it and names that
  modifier, with no line-range offer, because a case that does not run proves nothing. It then takes
  the case's `pairing_titles` and asks `_reached_name`: a title a name really reaches makes the case a
  definition, refused with the `path::title` to write instead. Only then is a `CaseExtent` returned.
- **`CaseExtent`** carries the fields of the module's own extent — start, end, kind, declaration,
  test case — and the titles the evidence pairs with. The range fields mirror `extents.Extent` rather
  than importing it, because `extents` imports `grammars`.
- **The name question.** `_reached_name` asks the caller's resolver for each title when there is one.
  Without a resolver it falls back to `_names_only`, which counts test calls and so cannot see a
  declaration that takes the same name: a title bound twice names neither case, and the range is then
  the only proof.
- **The refusals.** `_refusal` is one sentence — the lines, the path, and one reason. `_no_extent`
  names the cases the range overlaps as `a-b, …` or says no test case overlaps it. `not_a_case_file`
  refuses a file that is no test file and names the `path::<name>` form.
- **False-positive boundaries.** Only the OUTERMOST matching call is a case, because the inner call of
  `it.each([...])('title', body)` holds the parameters and not the title and the body. A member outside
  the known modifiers (`test.describe`, `test.step`, `test.setTimeout`) makes the call no case, a bare
  parameter table registers no test, and a parse error is no case.

### Conventions

- The extent is measured with the case module's `span_of`, never re-derived here, so a range that this
  module admits is a range the rest of the citation surface measures the same way.
- Refusal texts are the writer's; this module authors no report text of its own beyond the reason.

## Invariants And Boundaries

- **A range is one exact extent.** Lines that sit inside a case, or span two cases, are refused with
  the overlapping extents named, never admitted loosely.
- **Only the outermost call is a case.** A nested table call, an unknown member and a parse error are
  no case, so their own line is never a case's extent.
- **A case that does not run is never offered a range**, even though its lines are a real extent.
- **A case a name reaches is always told to name it.** The range route exists only for the case no
  name reaches, so it never competes with the plain `path::title` proof.
- The fallback naming test counts test calls only; a caller with a snapshot passes the real resolver
  so an ordinary declaration of the same name also keeps the range open.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- A file that is no test file is refused with the name form to use instead. [1]
- The range is admitted only for the case whose extent equals it exactly, and refused otherwise. [2]
- A case whose own modifier, or an enclosing suite's, stops it from running is refused with that modifier named. [3]
- A case a name reaches is refused as a definition, with the `path::title` to write instead. [4]
- An admitted case reports its extent fields and the titles its evidence pairs with. [5]
- A range that is no case's extent names the extents it overlaps, or says none overlaps it. [6]
- The refusal sentence names the lines, the path and one reason. [7]
- Only the outermost call rooted at it or test, holding its own body, is a case. [8]
