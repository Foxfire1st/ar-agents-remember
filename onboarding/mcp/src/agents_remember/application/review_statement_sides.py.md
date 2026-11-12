# mcp/src/agents_remember/application/review_statement_sides.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Recorded statement-side and field-value projections, plus the selected record's raw origin reader.
`side_content`, `side_conditions` and field helpers consume supplied comparison items; `side_origin`
is the important exception to the old no-store/no-snapshot description: it opens the supplied snapshot
index to read the selected invariant/family record's stored origin.

## Code Commentary

### Logic

`read_side` selects the supplied item's before or after payload; it performs no independent comparison.
`side_content` returns absent for no selected record, unresolved for a selected record with no operand,
and present with the recorded text otherwise. A family revision reads `joint_guarantee`; other selected
records read `statement`. An empty recorded string is not the same as missing text. The current wire
state vocabulary is present/absent/unresolved: the old declared binary state has been removed.

`side_origin(database, item, side)` opens `KnowledgeIndex(database)`, translates the selected projected
record identity to its text ID, reads the appropriate family/invariant record and validates its raw
`origin` as `Origin`. Missing selection, record ID, mapping, record or origin returns None. Index and
validation failures are not caught and converted to absence here. It neither reconstructs origin from
lossy projected authorship nor treats its presence as authenticated acceptance. The production
knowledge pane calls it separately against its baseline and candidate database bindings.

`field_changes` preserves the comparison's own changed-field roster and page order. `field_text`
returns None for a missing record/value, renders mappings through `structured_value_text`, joins tuple
values and otherwise uses their string rendering. An empty tuple renders an empty string, not None.
The comparison owns which transitions and one-sided rows exist; this module does not widen that roster.

Structured-value rendering uses sorted compact JSON, default=str, explicit lead/tail markers and a
visible truncation marker within the declared prose limit. Sorting ordinary JSON-like map keys avoids
insertion-order differences; arbitrary objects rendered by str and truncated output are not a promise
of lossless canonical bytes for every input. The current named structured-value test asserts key-order
equality only: its former fixture-driven two-sided round-trip is explicitly dead in the stored source.

### Conventions

The public exports include `side_origin` beside the retained projections. `side` is a caller-supplied
before/after spelling, not a new validated selector type. Models define the returned wire vocabulary;
`KnowledgeStatements` owns rendering, not this data helper.

### Invariants And Boundaries

Absent, unresolved, present-empty and present-nonempty are different recorded facts. Raw-origin lookup
is a read, not a mutation, revision choice or semantic verdict. Retained fixture assertions are stored
evidence rather than new execution; no obsolete structured-round-trip or binary-state coverage is claimed.

### Todos

Historical extraction and earlier test accounts are retained below with their superseded scope explicit.

## Historical source-epoch account — superseded where different

The quotation preserves original explanatory detail, prior candidates and producer/test observations.
Its outdated population, no-snapshot, state/count and computation-placement claims are **not** active
contracts; the current source account and renewed evidence govern. No historical grade is renewed.

> ## Purpose
>
> Pane 1's recorded content, and the one owner of what a statement side *is*. The module reads a
> `KnowledgeDiffItem` the shipped comparison already produced and projects it into the vocabulary
> `models/knowledge/review.py` declares: **the statement operand each side recorded**
> (`side_content`), **the essential conditions each side recorded** (`side_conditions`), and **the
> mechanical field rows the comparison itself reported** (`field_changes`, with `field_text` reading
> one field's recorded value). It sits between the comparison and the adapter: it selects nothing,
> compares nothing, re-reads no snapshot and stores nothing, and
> `application/knowledge_review.py` imports and calls it inside `_knowledge_pane`.
>
> **Why the file exists.** ICR-R06@v1's Scope asks a leaf that touches a responsibility inside the
> over-review-adapter to move that responsibility out before adding behavior, and the statement-side
> contract is that responsibility. The extraction is therefore both a size repair and the place the
> one-sided rule lives: the adapter resolves, calls and assembles, and this module owns the projection
> the pane's two side values and field roster are built from. The mirror of the same decision on the
> client is `dashboard/src/panels/review/KnowledgeStatements.tsx`, which owns how the two sides are
> drawn; this module owns what they contain.
>
> ## Code Commentary
>
> ### Logic
>
> **`side_content(item, side)` has three outcomes and no fourth, and it decides from the item rather
> than from any text.** `read_side` returns the item's own payload for that side (`item.before` for
> `"before"`, `item.after` for `"after"`, `None` when the item itself is absent). A side the item
> holds no payload for is `absent`, carrying the detail `the <side> snapshot selected no record for
> the reviewed subject`; a side whose payload exists and published no statement
> (`read_item.statement is None`) is `unresolved`, with its own detail saying the operand is
> unresolved rather than an empty statement; otherwise the side is `present` and carries the recorded
> text itself. An addition is exactly the first outcome on the before side, a removal exactly the
> first on the after side — and the two `unresolved`/`absent` cases stay distinguishable, which is
> what the packet's Failure And Recovery Behavior requires and what an empty-string operand would
> destroy.
>
> **`field_changes(items)` is the comparison's own `changed_fields` and nothing else.** One
> `ReviewFieldChange` per `(item, field)`, in the page's order, built from `item.changed_fields` —
> the roster is neither widened with fields that did not move nor narrowed by dropping a transition
> because one of its two values is absent. A **one-sided record reports no field rows at all**, and
> that is the comparison's own rule rather than an omission here: it reports such a record through
> that item's coverage, because nine field rows would state nine differences where there is one
> absence. This is the module's `field_changes` docstring, and it is measured by the case module
> below.
>
> **`field_text(item, name)` reserves `None` for the two real absences, and that reservation is the
> whole reason a structured value gets a rendering.** `ReviewFieldChange` declares that `None` on
> either value *is* the recorded fact that the field was absent on that side, so only two inputs may
> produce it: the side holds no record at all (`item is None`), or the record it holds carries no
> value for this field (`getattr(item, name, None) is None`). A `Mapping` value is therefore **not**
> reported as `None`: each side carries `structured_value_text` of the value *that side really
> holds*, so a present value is never displayed as an absent one and the two sides of a field the
> comparison calls *changed* never read as the same text. A tuple field joins into `"; "`-separated
> text a reader can compare, and an empty tuple is the empty string it is — a present-but-empty value,
> not an absence.
>
> **`structured_value_text(value)` is a labelled, canonical, bounded projection — the pane's own
> rendering and never a wire change.** `json.dumps(value, sort_keys=True, separators=(",", ":"),
> default=str)` gives one key order and one separator set, so the two sides of a changed field are
> directly comparable and every token is the value's own (a non-text leaf renders by its own `str`;
> no reference is resolved and no content is invented). The result is bracketed by
> `STRUCTURED_VALUE_LEAD` / `STRUCTURED_VALUE_TAIL` so a reader can tell the pane's rendering of a
> value from a value an author wrote, and it is bounded by `PROSE_MAX_LENGTH` minus the markers'
> width: a projection that does not fit is visibly cut with `…<truncated>` rather than silently
> shortened or raised. `provenance` is the shipped field this exists for — it is one of the fields
> the comparison projects and compares, and it is structured rather than text.
>
> **The projection is deterministic, and the module's own check depends on that.**
> `structured_value_text({"b": 1, "a": 2}) == structured_value_text({"a": 2, "b": 1})` is asserted by
> the case module, because a projection whose key order followed insertion order would make two equal
> values compare unequal in the pane.
>
> ### Conventions
>
> The module imports the shipped vocabulary and re-declares nothing: `ReviewFieldChange`,
> `ReviewSideContent` and `PROSE_MAX_LENGTH` are `models/knowledge/review.py`'s and
> `models/knowledge/base.py`'s, and `KnowledgeDiffItem` / `ReadItem` are the diff and read models.
> `__all__` publishes the seven names the adapter and the case module import —
> `STRUCTURED_VALUE_LEAD`, `STRUCTURED_VALUE_TAIL`, `field_changes`, `field_text`, `read_side`,
> `side_conditions`, `side_content` — and `STRUCTURED_VALUE_TRUNCATION` is deliberately private
> because nothing outside the projection reads it. The names are spelled without a leading
> underscore, unlike the private helpers they replace in the adapter, and the adapter **does not
> re-export them under their old private spellings**: `_side_content`, `_conditions`, `_read_side`,
> `_field_changes` and `_field_text` matched nothing outside the adapter before the move, so there is
> no importer to keep resolving and no alias is warranted. `side` is a plain `"before"`/`"after"`
> string rather than an enum, matching the vocabulary `ReviewSideContent` is keyed by.
>
> ### Invariants And Boundaries
>
> - **A state is read, never inferred from an empty string.** `absent` and `unresolved` answer
>   different questions about different snapshots and neither is ever spelled as empty text; a
>   present side's `text` is the recorded statement, not a re-typed or trimmed copy.
> - **`None` on a field row means absence, and only absence.** The two inputs that produce it are
>   "this side holds no record" and "this record carries no value for this field". A structured value
>   is projected instead, and a recorded empty tuple is the empty string.
> - **The field roster is the comparison's, not this module's.** It is neither widened nor narrowed;
>   a one-sided record's empty roster is the comparison's own coverage rule.
> - **Nothing is selected, compared, stored or re-read.** The module takes an
>   already-composed `KnowledgeDiffItem` (or a sequence of them) and returns values; it opens no
>   store, reads no snapshot, and writes nothing.
> - **No wire shape is defined here.** Every returned value is a shipped model; the projection's
>   markers are pane text carried in a text slot, not a new field, and no transport reads them.
> - **Two owners, one rule.** The statement-side *data* contract lives here; the statement-side
>   *rendering* contract lives in `KnowledgeStatements.tsx`. Neither re-implements the other, and
>   neither re-implements `DiffPane`/`FilePane`.
>
> ### Todos
>
> None recorded. Two limits are declared rather than pending, and both are the leaf's own recorded
> uncertainties rather than this module's defects: the projection's marker spelling is falsifiable as
> reader-facing text (a typed per-side value state would be a contract change and is not made here),
> and `binary` is a declared `ReviewSideState` with no producer in this module or anywhere else on the
> statement-side path — the renderer's case for it is explicitly a declared-state fixture.

## Evidence

### Docs References

No configured domain-documentation source was available; these implementation claims use the direct
repository sources below, not a source registry or a copied code comment as independent authority.

### Repo-Internal References

- Statement/condition/field projections consume supplied comparison items; the separately added side_origin helper does open the selected snapshot index. [1]
- The declared prose limit the projection is bounded by. [10]
- The item this module projects: its two payloads and the `changed_fields` roster the rows come from. [11]
- ReadItem supplies the selected statement or family joint guarantee and essential conditions. [12]
- The current knowledge pane assembles selected side content/conditions, raw before/after origins and comparison field changes through these helpers. [13]
- The current stored structured-value test asserts key-order equality only; its former fixture-driven two-sided round-trip is explicitly dead, not current proof. [14]
- The stored one-sided composition case asserts no field roster and retains the supplied side conditions; it is not a fresh execution. [15]
- The stored field-row case distinguishes absent acceptance from recorded values and checks the actual field roster; it is not a fresh execution. [16]
- The renderer that consumes these values and owns how they are drawn. [17]
- The public export list includes side_origin beside the retained projection helpers. [2]
- **The structured-value projection: the lead/tail markers, the truncation marker, and the canonical bounded rendering that keeps a present value out of the absence slot.** [3]
- Statement operands distinguish absent/unresolved/present; a family revision uses joint_guarantee while other selected records use statement. [4]
- The conditions a side recorded, empty exactly when that side recorded none. [5]
- **The field roster taken from the comparison's own `changed_fields`, one row per field, with the docstring's own reason a one-sided record reports none.** [6]
- **`None` reserved for the two real absences, the `Mapping` branch that projects instead, and the tuple join that makes a recorded empty a present-but-empty value.** [7]
- Current ReviewSideState has present/absent/unresolved, and its model requires text exactly when present; binary is no longer a declared fourth state. [8]
- **The contract that makes `None` mean absence, and therefore the reason a structured value is projected rather than nulled.** [9]
- Raw side origin comes from the selected record in its supplied snapshot database, validates the stored Origin and is not reconstructed from projected authorship. [18]

### Cross-Repo References

No new cross-repository boundary is introduced by these helpers.
