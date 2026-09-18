# mcp/src/agents_remember/memory/migration/inventory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/migration/inventory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The scope inventory: one row per in-scope source artifact, whether or not it has a card. The inventory is
taken over the **scope** — the code repository's tracked file set at a frozen baseline — and never over the
onboarding tree being examined, and that direction is the whole reason the module exists: a corpus-derived
list can only enumerate the sources that already have a card, so the sources with **no onboarding** are
exactly the ones it cannot see, and those are the files a coverage question is asked about. A missing card
is therefore a recorded row carrying `inventory_state="absent"` rather than an omission, and the same rule
runs the other way, so a card whose declared source is gone still gets a row and stays visible in the
count. Each row's route is **derived from the scope's own repository layout and recorded**: it is the
longest declared route directory that is a whole-segment prefix of the source path, matched through the
shipped route normalisation, so `mcp/src/x.py` belongs to route `mcp` while `mcpfoo/x.py` belongs to none —
a bare string prefix would silently file the second under the first. **A bad artifact is a row, not an
exception**: an unreadable file or non-UTF-8 content is recorded against the artifact's own path with the
matching outcome and the observed content that could not be parsed, bounded to the prose width, because a
silent skip and a clean read are indistinguishable in a count.

## Code Commentary

### Logic

**The list is the scope, not the corpus.** The module docstring states both directions of the mapping as
one rule: an in-scope source with no card is a row, and a card whose declared source is out of scope is a
row. `_scope_rows` walks the scope entries and yields either a card row or an absent row per entry, while
`_unclaimed_rows` walks the markdown cards actually observed under the derived routes and yields a row for
each card that no scope entry accounts for. `_card_path_of` is what keeps one artifact to one row: it
computes the card path an entry's source declares syntactically, with no filesystem probe, and the
`claimed` set built from those paths decides which observed cards are already someone's row.

**A route is derived from the layout and recorded, never read out of a card.** `DEFAULT_ROUTE_DIRECTORIES`
declares the eight top-level directories that carry a route in the source tree, and the comment states why
it is declared once rather than inline at each call site: a top-level directory the list does not name
belongs to no route, which is a fact a caller should see rather than have guessed for it. `_route_segments`
normalises each declared route through `_normalized_segments` and sorts the segment tuples by length
descending, so the longest declared route wins; `_route_for_segments` then compares whole segments, which
is what makes `mcpfoo/x.py` belong to no route rather than to `mcp`. A source that matches no declared
route returns the empty string from that helper — it is in scope and has no recorded route, which the
docstring calls a fact about the repository's route coverage rather than a reason to drop the row.

**What the scope is asked about is either what was observed or what the convention declares.**
`_route_directories` maps the observed onboarding paths through `_route_candidate` and returns the sorted
set of routes they name, falling back to `DEFAULT_ROUTE_DIRECTORIES` when the observation is empty, because
an empty observation means no tree was listed rather than that the repository has no routes. When paths
*were* observed, only the routes they name are asked about, so a route directory that does not exist is
never reported as empty coverage. `_route_candidate` is deliberately permissive about how a route arrives
— a corpus spelling with the `onboarding` segment, a bare `mcp`, a card path under its route, or the
absolute directory a caller listed — and strict about the name: it strips everything up to and including
the `CORPUS_DIRECTORY` segment and accepts the first remaining segment only when it is a declared route
directory.

**The declared `doc_type` is the authority for an artifact's kind.** `artifact_kind_of` reads one declared
field and looks it up in `ARTIFACT_KIND_BY_DOC_TYPE`; the path is consulted only when the artifact declares
no `doc_type` at all, and then only to give the row a kind — `overview.md` becomes the route-tier overview
kind, any other `.md` becomes the file-level kind, and anything else is `other`. The docstring states the
reason as the inference this record group exists to avoid: a filename-derived kind and a declared kind
disagree exactly where a corpus is being reorganised. `_declared_doc_type` is the structural read behind
that authority: it finds the recognized header row, scans from the row after the separator, returns `None`
as soon as a line is not a two-cell table row, and returns the `doc_type` row's value with surrounding
whitespace and code-span quoting removed. `_cells` supplies the row reading, and returns no cells at all
for a separator row so a dashed row cannot be read as a cell value.

**A raised read failure is a state a row carries, and the state a reader reports is checked.**
`_read_artifact` is the default reader and stays the smallest thing that satisfies the seam: it decodes
UTF-8 and reports `parsed`, and it does not catch its own failures. `_examine_artifact` is where a failure
becomes data — it catches `OSError` and `UnicodeDecodeError`, records `unreadable`, and carries the
failure's own text as evidence through `_failure_evidence`, which falls back to
`UNREADABLE_CONTENT_FALLBACK` when the failure reported no text. Because the reader is an injected seam,
its reported state is an input rather than a fact of this module: `_require_known_read_state` raises
`ValueError` for a state outside `CENSUS_PARSE_OUTCOMES`, since recording an undeclared state would report
an artifact a reader actually read as one that could not be read at all. `_inventory_state` then derives
`unreadable` or `present` from that one state, and an artifact read as text stays `present` whether or not
its content yielded anything a parser understood.

**A row that did not parse must say what was not parsed, and it is bounded.** `_unparsed_content` is the
one place that decides what a non-parsing outcome has to report: the parsed state reports nothing, and
every other state reports the observed content through `_bounded_observed_content`, which returns
`EMPTY_ARTIFACT_CONTENT` for empty text and otherwise the first `MAX_UNPARSED_LENGTH` characters. The cap
is the prose width the shared base declares rather than a number invented here, and the comment gives the
reason: the remainder is stored in a durable record, and a record that could absorb an arbitrarily large
file would let a single unreadable artifact decide how large the census is. The scope rows are built by
`_card_row`, `_absent_row` and `_unclaimed_row`, and each states its own answer to the fields it does not
have — an absent row names the source and leaves the artifact path empty, while an unclaimed row derives
the source from the card path by the corpus's one documented `.md` suffix rule and records
`POSIX_CURRENT_DIRECTORY` as its route when the path names no route.

**Two entry points, one of them taking the caller's card-path rule.** `resolve_scope` takes the source
paths and the observed onboarding paths, derives the routes from the observation, and drops two things: a
source whose declared card path is not a repository-relative path, and a source outside every declared
route, because a scope entry has to name a route the corpus can be asked about. It returns entries sorted
by source path, using `_card_path_for` to fall back to the plain `.md` suffix when the caller's mapping
returns nothing. `build_inventory` takes the frozen baseline, the scope, the onboarding root and an
optional reader, bundles them into `_ReadingContext` — the comment says the bundle exists partly because a
small argument list is what keeps the row builders inside the repository's function budget — and returns
the `ScopeInventory` for that baseline, with the scope rows followed by the unclaimed rows and the
baseline's own `key()` travelling beside them.

**The vocabularies this module records are closed at import.** Six module-level assertions state that each
value this module can write is a member of the schema's own tuple: the absent kind against
`CENSUS_ARTIFACT_KINDS`, the three inventory states against `CENSUS_INVENTORY_STATES`, and the two parse
outcomes against `CENSUS_PARSE_OUTCOMES`. The comment's reason is that a vocabulary which gained a value in
the schema would otherwise become a value this module records without ever being able to write it, and the
`ReadState` literal mirrors the schema's parse-outcome tuple value for value so that the two cannot move
apart silently.

### Conventions

The module declares its own shapes as frozen dataclasses and imports no payload model: `ScopeEntry`,
`InventoryRow` and `ScopeInventory` are the public ones, and `_ArtifactPath`, `_CardExamination` and
`_ReadingContext` are module-private values that carry an observation about one path, one read and one
whole inventory pass respectively. Paths are handled as POSIX strings with `posixpath` rather than as
platform paths, because a row's path is a repository-relative report label and not a filesystem index.
Every seam is a callable rather than a subclass: `read_artifact` defaults to `_read_artifact` and returns
a `(text, state)` pair, and `card_path_for_source` is a required keyword-only argument to `resolve_scope`
rather than a rule this module assumes. Counts are `collections.Counter` over the rows, exposed as three
properties — `counts_by_state`, `counts_by_route` and `rows_without_onboarding` — and the route axis is
documented as deliberately not the knowledge substrate's route axis, because a substrate route slice keys
on a stored route and on explicit governing-route associations while this row records where a file was
observed to live. Module-private helpers carry a leading underscore and there is no `__all__`.

### Invariants And Boundaries

- **The list is the scope, never the corpus.** Rows are produced from the in-scope source set, so an
  absent row exists for every source with no card and a card left behind by a deleted file still gets a
  row; a list derived from the corpus could not show either.
- **One artifact to one row.** The `claimed` set of syntactically declared card paths decides which
  observed cards are already an entry's row, and only the cards no entry accounts for are reported again.
- **A route is recorded, not inferred from content.** No route is read out of a card's prose; it comes
  from the declared route directories, is matched on whole path segments and is stored in the shipped
  normalisation with no trailing separator.
- **A source outside every route is dropped from the scope, and an unclaimed card without a route records
  the current-directory spelling.** The scope entry has to name a route the corpus can be asked about,
  while an observed card that belongs to none still gets a row with `.` as its route and an empty observed
  route.
- **No bad artifact raises.** A file that cannot be decoded or read becomes a row carrying `unreadable`
  and the bounded evidence of what could not be read, so a run never stops on one artifact.
- **A row whose outcome is not a parse carries evidence.** `_unparsed_content` reports the observed
  content for every state except `parsed`, and empty content is reported as the stated read-outcome fact
  rather than as an empty string.
- **The declared `doc_type` outranks the filename.** The path decides a kind only for an artifact that
  declares no `doc_type`, and a filename-derived disagreement never overrides a declaration.
- **A reader may only report a declared state.** `_require_known_read_state` refuses anything outside
  `CENSUS_PARSE_OUTCOMES` rather than guessing an outcome for a state this inventory has no vocabulary
  for.
- **The module writes nothing.** Every product is an immutable value; there is no store handle, no write
  path and no mutation of the onboarding tree, which is read only through the injected reader.
- **One declared policy name is never read.** `INVENTORY_POLICY_VERSION` is declared so a count can name
  the rule that produced it, and no module or test in the shipped candidate reads it.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The inventory answers a scope question the census asks and produces the row shape the census payload
models declare; the baseline it groups by and the route convention it records come from elsewhere in this
package. The rows below cite the two entry points, the route derivation and the path confinement behind
it, the declared-`doc_type` authority with the structural read that supplies it, the failure path that
turns a bad artifact into a row, the vocabulary closes, and the payload shape these values have to answer
to.

| Finding | Anchor | Source |
| --- | --- | --- |
| The inventory's own statement of its direction: one row per in-scope source, absent rows for the sources a corpus-derived list cannot see, and rows for cards whose source is gone. | `ScopeInventory`; `rows_without_onboarding` | mcp/src/agents_remember/memory/migration/inventory.py:1-29; mcp/src/agents_remember/memory/migration/inventory.py:149-176 |
| The row a source with no card produces: its own absent kind, absent state and absent outcome, with the source named and the artifact path left empty. | `_absent_row`; `ABSENT_INVENTORY_STATE`; `ABSENT_PARSE_OUTCOME` | mcp/src/agents_remember/memory/migration/inventory.py:522-536; mcp/src/agents_remember/memory/migration/inventory.py:73-84 |
| The declared route directories — eight top-level routes — and the stated consequence that an unnamed top-level directory belongs to no route. | `DEFAULT_ROUTE_DIRECTORIES` | mcp/src/agents_remember/memory/migration/inventory.py:53-66 |
| The confinement rule the route match runs over: an absolute, backslash, empty-segment or traversal spelling is not a repository-relative path, and the match itself is on whole path segments, longest declared prefix first, with the empty string for a source that matches no declared route. | `_normalized_segments`; `_route_segments`; `_route_for_segments` | mcp/src/agents_remember/memory/migration/inventory.py:215-227; mcp/src/agents_remember/memory/migration/inventory.py:230-255 |
| The route read that accepts the corpus spelling, a bare route name, a card path or an absolute directory, and rejects any name outside the declared directories — and the routes this scope is then asked about, which are the observed ones or the declared convention when no tree was listed. | `_route_candidate`; `CORPUS_DIRECTORY`; `_route_directories` | mcp/src/agents_remember/memory/migration/inventory.py:287-319; mcp/src/agents_remember/memory/migration/inventory.py:68-71 |
| The declared `doc_type` as the authority for an artifact's kind, with the path consulted only for an artifact that declares none. | `artifact_kind_of`; `ARTIFACT_KIND_BY_DOC_TYPE` | mcp/src/agents_remember/memory/migration/inventory.py:322-352 |
| The structural `doc_type` read: the recognized header row, then the `doc_type` row, stopping at the first line that leaves the table, with separator rows read as no cells. | `_declared_doc_type`; `_METADATA_HEADER`; `_DOC_TYPE_ROW`; `_cells` | mcp/src/agents_remember/memory/migration/inventory.py:408-438; mcp/src/agents_remember/memory/migration/inventory.py:441-450 |
| The default reader that decodes and reports, and the examination that turns a raised read failure into a recorded state with its evidence. | `_read_artifact`; `_examine_artifact` | mcp/src/agents_remember/memory/migration/inventory.py:361-369; mcp/src/agents_remember/memory/migration/inventory.py:453-473 |
| The reader seam: the state a reader reports is checked against the declared parse-outcome vocabulary and refused rather than guessed when it is outside it, and a read failure's own text becomes the evidence a row carries, with a stated fallback when the failure reported none. | `_require_known_read_state`; `ReadState`; `_failure_evidence`; `UNREADABLE_CONTENT_FALLBACK` | mcp/src/agents_remember/memory/migration/inventory.py:91-98; mcp/src/agents_remember/memory/migration/inventory.py:392-405; mcp/src/agents_remember/memory/migration/inventory.py:384-389; mcp/src/agents_remember/memory/migration/inventory.py:105-109 |
| What a row reports for a read that was not a parse: the remainder it must carry, capped at the prose width rather than trusted to be small, and the present-or-unreadable state derived from that one reader state, so a successful read stays a present artifact whatever its parse yielded. | `_unparsed_content`; `_bounded_observed_content`; `MAX_UNPARSED_LENGTH`; `EMPTY_ARTIFACT_CONTENT`; `_inventory_state`; `UNREADABLE_INVENTORY_STATE` | mcp/src/agents_remember/memory/migration/inventory.py:476-485; mcp/src/agents_remember/memory/migration/inventory.py:372-381; mcp/src/agents_remember/memory/migration/inventory.py:86-89; mcp/src/agents_remember/memory/migration/inventory.py:105-109; mcp/src/agents_remember/memory/migration/inventory.py:488-500 |
| The unclaimed direction: the claimed set that keeps one artifact to one row, the cards observed under the derived routes, and the row a card with no source left produces, whose source is recovered by the `.md` suffix rule and whose route falls back to the current-directory spelling. | `_unclaimed_rows`; `_card_path_of`; `_observed_cards`; `_unclaimed_row`; `_declared_source_of`; `POSIX_CURRENT_DIRECTORY` | mcp/src/agents_remember/memory/migration/inventory.py:606-619; mcp/src/agents_remember/memory/migration/inventory.py:567-576; mcp/src/agents_remember/memory/migration/inventory.py:579-590; mcp/src/agents_remember/memory/migration/inventory.py:539-564; mcp/src/agents_remember/memory/migration/inventory.py:111-113 |
| The card row builder that pairs one in-scope source with the card found at its declared card path, and states its own route and kind observations. | `_card_row` | mcp/src/agents_remember/memory/migration/inventory.py:503-519 |
| The scope entry point: the two spellings it drops, the caller-supplied card-path rule and the source-path ordering it returns. | `resolve_scope`; `ScopeEntry`; `_card_path_for` | mcp/src/agents_remember/memory/migration/inventory.py:622-647; mcp/src/agents_remember/memory/migration/inventory.py:125-130; mcp/src/agents_remember/memory/migration/inventory.py:267-271 |
| The inventory entry point and the reading context it bundles, with the baseline pair travelling beside the rows so two baselines are two cohorts. | `build_inventory`; `_ReadingContext`; `FrozenBaseline`; `key` | mcp/src/agents_remember/memory/migration/inventory.py:650-673; mcp/src/agents_remember/memory/migration/inventory.py:200-212; mcp/src/agents_remember/memory/migration/baseline.py:84-87 |
| The six import-time closes that keep every value this module records a member of the schema's closed vocabularies. | `CENSUS_ARTIFACT_KINDS`; `CENSUS_INVENTORY_STATES`; `CENSUS_PARSE_OUTCOMES` | mcp/src/agents_remember/memory/migration/inventory.py:115-122; mcp/src/agents_remember/memory/knowledge/schema_v9.py:73-84 |
| The census payload shape these rows answer — a non-empty artifact path, which the absent row leaves empty, and the guard that requires a non-parsed outcome to carry evidence — and the fact that no module in the shipped candidate converts an inventory row into that payload. | `CensusInventoryRowPayload`; `_require_unparsed_content_with_a_failed_parse` | mcp/src/agents_remember/models/knowledge/census.py:147-190 |
| The only consumer of the inventory in the shipped candidate: the migration test module drives `resolve_scope` and `build_inventory` over a temporary corpus and asserts the absent row and the unreadable row. | `resolve_scope`; `build_inventory` | mcp/tests/test_migration_census.py:205-216; mcp/tests/test_migration_census.py:224-250 |
| The same `doc_type` to artifact-kind projection is declared independently in the parser module, so the projection exists twice in this package with identical content. | `ARTIFACT_KIND_BY_DOC_TYPE` | mcp/src/agents_remember/memory/migration/inventory.py:322-352; mcp/src/agents_remember/memory/migration/parse.py:98-107 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every path it handles is repository-relative
text, the only filesystem it touches is the onboarding root it is handed, and its one external input is a
Git tree id that arrives inside a `FrozenBaseline` value rather than through a Git invocation of its own.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the scope inventory. It records the direction that is the module's whole reason to exist: rows from the scope, so the sources with no card and the cards whose source is gone both stay visible. The mechanisms it cites are the eight declared route directories, the whole-segment match that keeps `mcpfoo` out of route `mcp`, the four spellings `_route_candidate` accepts, the three row builders, the declared-`doc_type` authority with its structural read, the failure path that turns a raised `OSError` or `UnicodeDecodeError` into an `unreadable` row with bounded evidence, the six import-time closes over the schema's closed vocabularies, and the two entry points with the baseline pair travelling beside the rows. It also records the deliberate absences and the recorded facts: no write path, a policy version constant no caller reads, an absent row whose empty artifact path a non-empty census payload field would refuse, and the identical `doc_type` projection the parser module declares independently. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
