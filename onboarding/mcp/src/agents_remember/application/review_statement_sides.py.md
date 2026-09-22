# mcp/src/agents_remember/application/review_statement_sides.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_statement_sides.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T17:30:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l6`, uncommitted; base `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9` |
| lastVerifiedCommitHash | `f33f58eab87bd4db0eb944999d01808821ef9c3a` |
| lastVerifiedCommitDate | 2026-09-22T11:27:22+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

Pane 1's recorded content, and the one owner of what a statement side *is*. The module reads a
`KnowledgeDiffItem` the shipped comparison already produced and projects it into the vocabulary
`models/knowledge/review.py` declares: **the statement operand each side recorded**
(`side_content`), **the essential conditions each side recorded** (`side_conditions`), and **the
mechanical field rows the comparison itself reported** (`field_changes`, with `field_text` reading
one field's recorded value). It sits between the comparison and the adapter: it selects nothing,
compares nothing, re-reads no snapshot and stores nothing, and
`application/knowledge_review.py` imports and calls it inside `_knowledge_pane`.

**Why the file exists.** ICR-R06@v1's Scope asks a leaf that touches a responsibility inside the
over-review-adapter to move that responsibility out before adding behavior, and the statement-side
contract is that responsibility. The extraction is therefore both a size repair and the place the
one-sided rule lives: the adapter resolves, calls and assembles, and this module owns the projection
the pane's two side values and field roster are built from. The mirror of the same decision on the
client is `dashboard/src/panels/review/KnowledgeStatements.tsx`, which owns how the two sides are
drawn; this module owns what they contain.

## Code Commentary

### Logic

**`side_content(item, side)` has three outcomes and no fourth, and it decides from the item rather
than from any text.** `read_side` returns the item's own payload for that side (`item.before` for
`"before"`, `item.after` for `"after"`, `None` when the item itself is absent). A side the item
holds no payload for is `absent`, carrying the detail `the <side> snapshot selected no record for
the reviewed subject`; a side whose payload exists and published no statement
(`read_item.statement is None`) is `unresolved`, with its own detail saying the operand is
unresolved rather than an empty statement; otherwise the side is `present` and carries the recorded
text itself. An addition is exactly the first outcome on the before side, a removal exactly the
first on the after side — and the two `unresolved`/`absent` cases stay distinguishable, which is
what the packet's Failure And Recovery Behavior requires and what an empty-string operand would
destroy.

**`field_changes(items)` is the comparison's own `changed_fields` and nothing else.** One
`ReviewFieldChange` per `(item, field)`, in the page's order, built from `item.changed_fields` —
the roster is neither widened with fields that did not move nor narrowed by dropping a transition
because one of its two values is absent. A **one-sided record reports no field rows at all**, and
that is the comparison's own rule rather than an omission here: it reports such a record through
that item's coverage, because nine field rows would state nine differences where there is one
absence. This is the module's `field_changes` docstring, and it is measured by the case module
below.

**`field_text(item, name)` reserves `None` for the two real absences, and that reservation is the
whole reason a structured value gets a rendering.** `ReviewFieldChange` declares that `None` on
either value *is* the recorded fact that the field was absent on that side, so only two inputs may
produce it: the side holds no record at all (`item is None`), or the record it holds carries no
value for this field (`getattr(item, name, None) is None`). A `Mapping` value is therefore **not**
reported as `None`: each side carries `structured_value_text` of the value *that side really
holds*, so a present value is never displayed as an absent one and the two sides of a field the
comparison calls *changed* never read as the same text. A tuple field joins into `"; "`-separated
text a reader can compare, and an empty tuple is the empty string it is — a present-but-empty value,
not an absence.

**`structured_value_text(value)` is a labelled, canonical, bounded projection — the pane's own
rendering and never a wire change.** `json.dumps(value, sort_keys=True, separators=(",", ":"),
default=str)` gives one key order and one separator set, so the two sides of a changed field are
directly comparable and every token is the value's own (a non-text leaf renders by its own `str`;
no reference is resolved and no content is invented). The result is bracketed by
`STRUCTURED_VALUE_LEAD` / `STRUCTURED_VALUE_TAIL` so a reader can tell the pane's rendering of a
value from a value an author wrote, and it is bounded by `PROSE_MAX_LENGTH` minus the markers'
width: a projection that does not fit is visibly cut with `…<truncated>` rather than silently
shortened or raised. `provenance` is the shipped field this exists for — it is one of the fields
the comparison projects and compares, and it is structured rather than text.

**The projection is deterministic, and the module's own check depends on that.**
`structured_value_text({"b": 1, "a": 2}) == structured_value_text({"a": 2, "b": 1})` is asserted by
the case module, because a projection whose key order followed insertion order would make two equal
values compare unequal in the pane.

### Conventions

The module imports the shipped vocabulary and re-declares nothing: `ReviewFieldChange`,
`ReviewSideContent` and `PROSE_MAX_LENGTH` are `models/knowledge/review.py`'s and
`models/knowledge/base.py`'s, and `KnowledgeDiffItem` / `ReadItem` are the diff and read models.
`__all__` publishes the seven names the adapter and the case module import —
`STRUCTURED_VALUE_LEAD`, `STRUCTURED_VALUE_TAIL`, `field_changes`, `field_text`, `read_side`,
`side_conditions`, `side_content` — and `STRUCTURED_VALUE_TRUNCATION` is deliberately private
because nothing outside the projection reads it. The names are spelled without a leading
underscore, unlike the private helpers they replace in the adapter, and the adapter **does not
re-export them under their old private spellings**: `_side_content`, `_conditions`, `_read_side`,
`_field_changes` and `_field_text` matched nothing outside the adapter before the move, so there is
no importer to keep resolving and no alias is warranted. `side` is a plain `"before"`/`"after"`
string rather than an enum, matching the vocabulary `ReviewSideContent` is keyed by.

### Invariants And Boundaries

- **A state is read, never inferred from an empty string.** `absent` and `unresolved` answer
  different questions about different snapshots and neither is ever spelled as empty text; a
  present side's `text` is the recorded statement, not a re-typed or trimmed copy.
- **`None` on a field row means absence, and only absence.** The two inputs that produce it are
  "this side holds no record" and "this record carries no value for this field". A structured value
  is projected instead, and a recorded empty tuple is the empty string.
- **The field roster is the comparison's, not this module's.** It is neither widened nor narrowed;
  a one-sided record's empty roster is the comparison's own coverage rule.
- **Nothing is selected, compared, stored or re-read.** The module takes an
  already-composed `KnowledgeDiffItem` (or a sequence of them) and returns values; it opens no
  store, reads no snapshot, and writes nothing.
- **No wire shape is defined here.** Every returned value is a shipped model; the projection's
  markers are pane text carried in a text slot, not a new field, and no transport reads them.
- **Two owners, one rule.** The statement-side *data* contract lives here; the statement-side
  *rendering* contract lives in `KnowledgeStatements.tsx`. Neither re-implements the other, and
  neither re-implements `DiffPane`/`FilePane`.

### Todos

None recorded. Two limits are declared rather than pending, and both are the leaf's own recorded
uncertainties rather than this module's defects: the projection's marker spelling is falsifiable as
reader-facing text (a typed per-side value state would be a contract change and is not made here),
and `binary` is a declared `ReviewSideState` with no producer in this module or anywhere else on the
statement-side path — the renderer's case for it is explicitly a declared-state fixture.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and six
declarations, the two model modules whose contract it reads, the adapter that calls it, and the two
case modules that measure it from the composition side and the renderer side.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of its scope: three projections of a comparison's items, and a selection that reads nothing and stores nothing.** | `side_content`; `field_changes`; `side_conditions` | mcp/src/agents_remember/application/review_statement_sides.py:86-117; mcp/src/agents_remember/application/review_statement_sides.py:120-124; mcp/src/agents_remember/application/review_statement_sides.py:135-155 |
| The published surface: the seven names the adapter and the case module import. | `__all__` | mcp/src/agents_remember/application/review_statement_sides.py:44-53 |
| **The structured-value projection: the lead/tail markers, the truncation marker, and the canonical bounded rendering that keeps a present value out of the absence slot.** | `STRUCTURED_VALUE_LEAD`; `STRUCTURED_VALUE_TAIL`; `STRUCTURED_VALUE_TRUNCATION`; `structured_value_text` | mcp/src/agents_remember/application/review_statement_sides.py:55-83 |
| **The three outcomes and no fourth: `absent` / `unresolved` / `present`+text, each with the detail that says which fact it is.** | `side_content`; `read_side` | mcp/src/agents_remember/application/review_statement_sides.py:86-117; mcp/src/agents_remember/application/review_statement_sides.py:127-132 |
| The conditions a side recorded, empty exactly when that side recorded none. | `side_conditions` | mcp/src/agents_remember/application/review_statement_sides.py:120-124 |
| **The field roster taken from the comparison's own `changed_fields`, one row per field, with the docstring's own reason a one-sided record reports none.** | `field_changes` | mcp/src/agents_remember/application/review_statement_sides.py:135-155 |
| **`None` reserved for the two real absences, the `Mapping` branch that projects instead, and the tuple join that makes a recorded empty a present-but-empty value.** | `field_text` | mcp/src/agents_remember/application/review_statement_sides.py:158-179 |
| The side-state vocabulary and the point the two states are distinct at: `ReviewSideContent` carries `state`, optional `text`, `language` and `detail`, and `ReviewSideState` is the closed four-member literal. | `ReviewSideState`; `ReviewSideContent` | mcp/src/agents_remember/models/knowledge/review.py:124-124; mcp/src/agents_remember/models/knowledge/review.py:128-153 |
| **The contract that makes `None` mean absence, and therefore the reason a structured value is projected rather than nulled.** | `ReviewFieldChange` | mcp/src/agents_remember/models/knowledge/review.py:276-287 |
| The declared prose limit the projection is bounded by. | `PROSE_MAX_LENGTH` | mcp/src/agents_remember/models/knowledge/base.py:24-24 |
| The item this module projects: its two payloads and the `changed_fields` roster the rows come from. | `KnowledgeDiffItem` | mcp/src/agents_remember/models/knowledge/diff.py:318-354 |
| The payload `read_side` returns, with the `statement` and `essential_conditions` fields each projection reads. | `ReadItem` | mcp/src/agents_remember/models/knowledge/read.py:363-401 |
| **The adapter's delegation: the import block and the one call site set inside `_knowledge_pane`, where the four side values and the field roster are assembled.** | `side_content`; `side_conditions`; `field_changes` | mcp/src/agents_remember/application/knowledge_review.py:101-105; mcp/src/agents_remember/application/knowledge_review.py:714-761 |
| **The production composition case: the structured field's two sides are both present, differ, and round-trip back to the stored authorship envelope.** | `test_a_structured_field_value_is_rendered_as_its_own_text_and_never_as_an_absence` | mcp/tests/test_knowledge_review_one_sided_statements.py:320-350 |
| The case that a one-sided record reports its change through coverage and keeps the roster empty. | `test_a_one_sided_record_is_reported_by_its_coverage_and_not_by_a_roster_of_field_rows` | mcp/tests/test_knowledge_review_one_sided_statements.py:353-369 |
| The case that a row keeps the side that recorded a value and names the side that did not. | `test_a_field_row_keeps_the_side_that_recorded_a_value_and_names_the_side_that_did_not` | mcp/tests/test_knowledge_review_one_sided_statements.py:288-317 |
| The renderer that consumes these values and owns how they are drawn. | `KnowledgeStatements` | dashboard/src/panels/review/KnowledgeStatements.tsx:93-118 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The module projects one comparison item's
recorded content and carries no identity that ranges beyond the repository namespace the comparison
was opened under.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-22T09:20:00+02:00 — 260921-ICR-L4 curator (gate repair pass on the merged line): **one enforced row re-cited.** The delegation row cited `knowledge_review.py:90-90`/`672-705`, which the record-owner extraction and attribution wiring moved; it now cites the import block at `:93-96` and `_knowledge_pane` at `:694-727`. Wording unchanged; no stamp advanced.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `side_content`; `field_changes`; `side_conditions` repointed to mcp/src/agents_remember/application/review_statement_sides.py:86-117; mcp/src/agents_remember/application/review_statement_sides.py:135-155; mcp/src/agents_remember/application/review_statement_sides.py:120-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-21T17:30:00+02:00 — 260921-ICR-L6 curator (uncommitted change set on `ar/260921-icr-l6`):
  **created.** The module is new in this leaf and this is its one-to-one card. It records the three
  projections the module owns (statement side, essential conditions, mechanical field rows), the
  three-outcome side contract (`absent` / `unresolved` / `present`) and why a state is read rather
  than inferred from empty text, the `None`-means-absence reservation in `ReviewFieldChange` and the
  labelled canonical bounded `structured_value_text` projection that keeps a present structured value
  out of the absence slot, the comparison's own `changed_fields` roster and its one-sided-record
  rule, and the fact that the moved names are deliberately **not** re-exported under the adapter's
  old private spellings because nothing outside the adapter imported them. **Stamp accounting:** the
  verification pair names production line `7f8dc82829d0dc824d1ab9846c5ec6a6f13f8ba9` — the leaf's
  base, and the last real commit the reading was taken against — because every construct this card
  cites exists only in this leaf's uncommitted candidate and no commit contains the bytes a stamp
  would claim to have verified. `reviewedWorkingCandidate` states what was actually read; closeout
  owns the stamp once the code commit exists.
