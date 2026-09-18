# mcp/src/agents_remember/memory/migration/parse.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/migration/parse.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The migration's parser, and the only place a legacy Markdown artifact becomes structure: `parse_artifact`
reads one artifact into the declared front-matter table it carries, the ATX headings it writes with the
line each starts at, the corpus's own `cit:(...)` citation marks, and the references those two sources
declare, and returns a `ParsedArtifact` whose `outcome` is one of the census's declared values. **It
reports structure, and it classifies nothing** — its own docstring states that an artifact's semantic
category, the truth of a claim it makes, whether a reference resolves and whether a card is any good are
all somebody else's read, so there is no keyword test, no scoring, no heading-to-topic mapping and no
branch whose condition is a statement about meaning. **It never raises for a bad artifact either**: a
shape it has not been told about is reported `unsupported` with the content it could not read, text that
is not the text of any UTF-8 sequence is `unreadable` with the offending byte spelled out, and the one
form it refuses is a declared entry in its own format list rather than an omission, because a format
merely missing from a list is indistinguishable from a format nobody considered. The one correctness
detail the module is built around is where the metadata table **stops**: reading continues only while a
row is a two-cell row whose key is a name of `RECOGNIZED_FRONT_MATTER_KEYS`, so the evidence inventory a
card writes below its front matter cannot become declarations the card never made. Every stored text is a
bounded prefix of the artifact's own words, unmodified and unelided, because a truncation marker would be
this parser writing text into a field whose meaning is what the artifact itself said.

## Code Commentary

### Logic

**What is read, stated as a boundary rather than as an intention.** The module docstring is the contract,
and it is written as a list of refusals: no keyword test, no scoring, no heading-to-topic mapping, no
branch conditioned on meaning. What is actually read is enumerated just as tightly — a declared
front-matter table, ATX headings, fenced regions and the corpus's own citation mark — and the vocabulary
an outcome may take is the census's, not this module's. `parse_artifact` is the single entry point that
produces an observation, and it branches exactly three ways: text that cannot be UTF-8 is reported
`unreadable`, text with no declared table is reported `unsupported`, and everything else is reported
`parsed` with its declarations, sections, citation keys and references attached.

**Four outcomes bound by name, from a vocabulary this module does not own.** The four state names are
unpacked from `CENSUS_PARSE_OUTCOMES` at import, and the unpacking is deliberately a guard: a vocabulary
that stopped carrying exactly those four states fails at import instead of letting a mismatched name
reach a written row. The binding is what lets every path below name a state symbolically rather than
spell one as a literal. The fourth binding, `OUTCOME_UNPARSED`, is never used by any path in the shipped
candidate — this parser produces `parsed`, `unsupported` and `unreadable` only — so the declared
vocabulary is wider than the set of outcomes this module can reach.

**Four declared formats, each carrying the observed structure that decides it.** `SUPPORTED_FORMATS` is
the parser's own boundary, and every entry is a `SupportedFormat` naming the format, the `doc_type`
values it covers and a `reason` written as the structure the corpus actually shows, because a format
admitted on a guess cannot be re-checked later. The reasons carry the measured population at the
migration baseline: 2071 artifacts declare a two-column table whose first key is a front-matter name, of
which 1984 declare `file-level-onboarding` and 85 declare a route-tier overview, while 41 declare no
readable front matter at all; the refused form's own reason names 38 artifacts that carry the
`| Field | Value |` header under a key outside the front-matter vocabulary and 3 that carry no such table
at all. The four
declared names are `markdown-metadata-table/v1`, `file-level-onboarding-card/v1`,
`route-local-overview/v1` and `generated-bootstrap-artifact/v1`, and `declared_formats()` returns the
tuple unchanged so a reader of an outcome can name the format the outcome was decided against.

**The table stops at its own end, and that is the module's measured failure mode.** `_read_metadata_table`
finds the first line matching the recognized header, requires the two-column separator row immediately
below it, and then continues only while a row has exactly two cells and its first cell is a member of
`_RECOGNIZED_KEYS`. It breaks at the first key outside that set or the first line that is not a table row
at all, and a table with no recognized row returns `None`. The docstring names the reason as a measured
failure of this corpus rather than a hypothetical: reading every `|`-row that follows the header turns a
card's `Finding | Anchor | Source` evidence inventory into front-matter rows the card never declared. The
same rule is what makes an artifact whose first key is already outside the vocabulary reportable as
`unsupported` rather than half-read.

**A heading is read where it is written, and a fence is not a place a heading is written.** `_read_sections`
builds one `Section` per heading, and each section's `body` runs from the line after its heading to the
next heading of any level, so a document's lines belong to at most one section and a parent's text is
never duplicated into its children's. `_heading_positions` is where the fence matters: it toggles a
`fenced` flag on every fence opener or closer and refuses to match a heading while fenced, because a line
beginning with `#` inside a fenced block is a comment the artifact is showing — reading it as a heading
would name a section the artifact does not have and hand a citation an enclosing location that is really
a line of source code. `_title` then returns the text of the first level-one heading, or `None`.

**A citation key is delimited by the artifact's own quoting, not by parenthesis depth.** `CITATION_MARK`
is the two-character-plus-paren mark `cit:(`, and `_citation_occurrences` walks the text by `str.find`,
keeping the 1-based line count in step with the cursor, and reports every complete mark in written order.
`_body_end` decides where the body closes: it walks characters tracking whether it is inside a
double-quoted string or a backtick code span, honours a backslash escape inside a double-quoted anchor,
and returns the first `)` written outside that quoting. The docstring states why depth counting is wrong
for this corpus — an anchor quotes the source text it is about, and that text may carry an unbalanced
parenthesis such as a quoted call signature, so a depth count runs past the real close and swallows the
citations that follow. The walk is bounded by `PROSE_MAX_LENGTH` plus one character, so a mark that never
closes stays cheap, and a body that does not close within that width is not reported at all.
`parse_artifact` then deduplicates the keys in written order through `dict.fromkeys`.

**References are read out, and resolution is somebody else's question.** `_references` builds the
declared half from `REFERENCE_FIELD_NAMES` in declaration order, skipping any field whose value is blank
because a blank value is not a reference the artifact made, and the written half from every citation mark
with its line. `ArtifactReference` carries the verbatim text, the line, and a `field_or_section` that
says only where the text was read from — a declared field's name, or the heading of the section the mark
appeared in — and its docstring is explicit that this is not a kind, a target or a verdict.
`_enclosing_heading` returns the empty string for content written above the artifact's first heading
rather than naming the nearest heading anyway, because that would place a citation inside a section the
artifact does not put it in.

**A bad artifact is an outcome with evidence, never an exception.** `parse_artifact` checks
`_is_utf8_text` first, which asks whether the text encodes back to UTF-8 and reports `unreadable` when it
does not; `_utf8_safe` then rewrites any lone surrogate with `errors="backslashreplace"` so the stored
evidence still says what was there, since a value carrying a lone surrogate is not serializable evidence
and a record that cannot be written is a worse report than one that spells the byte out. `_unread` builds
the row for both non-parsed outcomes and sets every read product empty — no front matter, no title, no
sections, no citation keys, no references — because an artifact that was not parsed produced none of them.
An artifact with no content at all reports `NOTHING_OBSERVED` instead of an empty extension, which is the
one value here that is not the artifact's own text and is a statement about the observation rather than
about meaning.

**Bounded storage, and the bound is not interpretation.** `_bounded` is a plain prefix slice with no
marker, and it is applied at each storage point: the heading text at `LABEL_MAX_LENGTH`, a section body,
a citation body and an unparsed remainder at `PROSE_MAX_LENGTH`. `_unwrapped` removes the table's
code-span quoting from a declared value and nothing else, and only when the value is exactly one code
span — both ends backticked with no backtick between them — because stripping the outer characters of a
value quoting two spans would edit the declaration the artifact made rather than remove the table's
quoting from it.

**Two vocabulary projections over one declared field, and a default that is not a refusal.**
`FORMAT_BY_DOC_TYPE` and `ARTIFACT_KIND_BY_DOC_TYPE` both read the artifact's declared `doc_type`, and
both are lookups rather than inferences: an artifact that declares a `doc_type` neither projection names
is still an artifact using the metadata-table form, so `classify_declared_format` defaults to
`METADATA_TABLE_FORMAT`, while `_artifact_kind` defaults to `ARTIFACT_KIND_OTHER`. The module's own
comment states the asymmetry's reason — the vocabulary of `doc_type` values grows, the shape of a
two-column declaration table does not — and two import-time guards close the gap between the
projections and the schemas they must land in: every artifact kind named must be a member of
`CENSUS_ARTIFACT_KINDS`, and every reference field must be a field of the module's own table vocabulary.
The declared format list's `doc_type` string also names `repo-entity-catalog`, which neither projection
names, so such an artifact is read as the metadata-table form and recorded as `other`.

### Conventions

This module declares no model of its own and imports none: `SupportedFormat`, `FrontMatter`, `Section`,
`ArtifactReference` and `ParsedArtifact` are frozen dataclasses with no framework base, and the only
shared vocabulary it consumes is the census's four parse outcomes from `schema_v9.py` and the two width
bounds `PROSE_MAX_LENGTH` and `LABEL_MAX_LENGTH` from `models/knowledge/base.py`. Every declaration that
must agree is a single module-level constant: the citation mark, the three format names, the refused
format's name, the front-matter vocabulary with its frozenset view, the three reference field names, both
`doc_type` projections, the four line patterns and the one observation note. The regexes are compiled once
at import and matched without flags; the header pattern admits the padded spelling the corpus writes,
and the heading pattern drops an ATX closing sequence. Module-private helpers carry a leading underscore
and there is no `__all__`, so the module's public surface is whatever a caller chooses to import — in the
shipped candidate that is `CITATION_MARK`, `declared_formats` and `parse_artifact`, plus the dataclasses.

### Invariants And Boundaries

- **Nothing here is a statement about meaning.** No keyword test, no score, no heading-to-topic map and
  no branch conditioned on prose exist in the file; the only classifications are lookups over a declared
  `doc_type` field, and the artifact's semantic category is left to the modules that own it.
- **No bad artifact raises.** Every input yields a `ParsedArtifact`: an undecodable text is `unreadable`,
  a text with no declared table is `unsupported`, and a sweep over a corpus therefore reports every
  artifact it met instead of stopping at the first bad one.
- **The metadata table is its own bound.** A row is front matter while its key is a recognized
  front-matter name, so the tables a card writes below its front matter are never read as declarations,
  and an unrecognized first key reports the artifact `unsupported` rather than half-read.
- **A non-parsed outcome carries its evidence.** `unparsed_content` always holds observed content —
  `NOTHING_OBSERVED` when the artifact had none — and every other read product is empty for that
  outcome, because reporting a title or a section beside content that was not read is a claim the parser
  cannot support.
- **Written location and written order are preserved.** `FrontMatter.keys_in_order` is the written order
  beside the mapping, a section's `line` is the 1-based line of its heading, a reference's `line` is
  where it was written, and content above the first heading is reported as belonging to no section.
- **The stored value is the artifact's own prefix.** `_bounded` truncates without a marker, and
  `_unwrapped` removes code-span quoting only when the value is a single span, so no stored field carries
  text this module wrote.
- **Fenced regions are quoted text.** A `#` line inside a fence is not a heading, so a fenced block can
  neither invent a section nor become a citation's enclosing location.
- **Four outcomes are declared and three are reachable.** `OUTCOME_UNPARSED` is bound at import and
  produced by no path here, so the census vocabulary is wider than this parser's outcome set.
- **One declared classifier has no caller.** `classify_declared_format` is a public function that no
  module or test in the shipped candidate calls, so the declared-format read it performs is available but
  unused.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The parser reads the same corpus the inventory and the mapping registry read, and it answers to vocabularies
that live in the knowledge schema and the census payload models rather than here. The rows below cite the
observation it returns, the four declared formats and their measured reasons, the table-stop rule and the
citation reader that implement its contract, the two guards that keep its projections inside the closed
vocabularies, and the two declared names the shipped candidate never reaches.

| Finding | Anchor | Source |
| --- | --- | --- |
| The parser's own statement of its contract: what it observes, why it classifies nothing, and why a bad artifact is an outcome rather than an exception. | `ParsedArtifact` | mcp/src/agents_remember/memory/migration/parse.py:1-31; mcp/src/agents_remember/memory/migration/parse.py:235-253 |
| The four outcomes bound by name from the census's own vocabulary, with the unpacking itself as the guard against a moved vocabulary. | `CENSUS_PARSE_OUTCOMES`; `OUTCOME_PARSED` | mcp/src/agents_remember/memory/migration/parse.py:49-54; mcp/src/agents_remember/memory/knowledge/schema_v9.py:78-83 |
| The four declared formats, each carrying the observed structure that decides it and the measured corpus population behind it. | `SUPPORTED_FORMATS`; `SupportedFormat` | mcp/src/agents_remember/memory/migration/parse.py:144-187; mcp/src/agents_remember/memory/migration/parse.py:132-141 |
| The one form this parser refuses, declared as an entry with a reason instead of omitted, so the refusal is a recorded decision. | `UNSUPPORTED_FORMAT` | mcp/src/agents_remember/memory/migration/parse.py:61-64; mcp/src/agents_remember/memory/migration/parse.py:176-186 |
| The declared front-matter vocabulary read as the table's own bound as well as its meaning. | `RECOGNIZED_FRONT_MATTER_KEYS`; `_RECOGNIZED_KEYS` | mcp/src/agents_remember/memory/migration/parse.py:66-81; mcp/src/agents_remember/memory/migration/parse.py:328-336 |
| The table read that continues only while a key is recognized and breaks at the first row that is not, which is what keeps a card's evidence inventory out of its front matter. | `_read_metadata_table` | mcp/src/agents_remember/memory/migration/parse.py:316-336 |
| The `doc_type` to format projection with its metadata-table default, so an unnamed declaration stays in the form the parser reads. | `FORMAT_BY_DOC_TYPE`; `classify_declared_format` | mcp/src/agents_remember/memory/migration/parse.py:88-96; mcp/src/agents_remember/memory/migration/parse.py:267-280 |
| The `doc_type` to artifact-kind projection with its `other` default, and the import-time guard that keeps every named kind inside the census's closed vocabulary. | `ARTIFACT_KIND_BY_DOC_TYPE`; `ARTIFACT_KIND_OTHER` | mcp/src/agents_remember/memory/migration/parse.py:98-115; mcp/src/agents_remember/memory/migration/parse.py:487-497 |
| The heading read that refuses to match inside a fenced block, so quoted source text cannot name a section. | `_heading_positions`; `_FENCE` | mcp/src/agents_remember/memory/migration/parse.py:366-383; mcp/src/agents_remember/memory/migration/parse.py:117-123 |
| The citation mark and the closing-quote walk that delimits a body by the artifact's own quoting rather than by parenthesis depth, bounded to the storable width. | `CITATION_MARK`; `_citation_occurrences`; `_body_end` | mcp/src/agents_remember/memory/migration/parse.py:42-44; mcp/src/agents_remember/memory/migration/parse.py:386-408; mcp/src/agents_remember/memory/migration/parse.py:411-438 |
| The declared fields whose values are references the artifact makes, and the reference assembly that reports them beside every written citation, with the empty location used for content written above the first heading. | `REFERENCE_FIELD_NAMES`; `_references`; `_enclosing_heading` | mcp/src/agents_remember/memory/migration/parse.py:83-86; mcp/src/agents_remember/memory/migration/parse.py:441-468; mcp/src/agents_remember/memory/migration/parse.py:471-484 |
| The non-parsed row that carries the observed content, its empty read products and the note used when there was no content to carry. | `_unread`; `NOTHING_OBSERVED` | mcp/src/agents_remember/memory/migration/parse.py:500-519; mcp/src/agents_remember/memory/migration/parse.py:125-128 |
| The UTF-8 observation and the escaped rewrite that keeps a lone surrogate out of a stored field. | `_is_utf8_text`; `_utf8_safe` | mcp/src/agents_remember/memory/migration/parse.py:522-541 |
| Bounded storage at each write point, with the two widths the shared base declares and a prefix that carries no truncation marker. | `_bounded`; `_read_sections`; `PROSE_MAX_LENGTH`; `LABEL_MAX_LENGTH` | mcp/src/agents_remember/memory/migration/parse.py:592-600; mcp/src/agents_remember/memory/migration/parse.py:339-354; mcp/src/agents_remember/models/knowledge/base.py:20-25 |
| The outcome vocabulary the parser's states must be members of, and the payload guard that refuses a non-parsed outcome with no evidence. | `CensusParseOutcome`; `_require_unparsed_content_with_a_failed_parse` | mcp/src/agents_remember/models/knowledge/census.py:63-65; mcp/src/agents_remember/models/knowledge/census.py:174-190 |
| The declared-format classifier and the fourth outcome binding: both are declared in the shipped candidate and reached by no caller. | `classify_declared_format`; `OUTCOME_UNPARSED` | mcp/src/agents_remember/memory/migration/parse.py:267-280; mcp/src/agents_remember/memory/migration/parse.py:49-54 |
| The one consumer of this module in the candidate: the migration test module imports the citation mark, the declared-format reader and the parser, and asserts the outcomes and the citation keys they produce. | `declared_formats`; `parse_artifact` | mcp/tests/test_migration_census.py:26-30; mcp/tests/test_migration_census.py:178-183 |
| The inventory module declares the same `doc_type` to artifact-kind projection independently, so the projection exists twice in this package with identical content. | `ARTIFACT_KIND_BY_DOC_TYPE` | mcp/src/agents_remember/memory/migration/inventory.py:322-352; mcp/src/agents_remember/memory/migration/inventory.py:325-329 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The parser reads one text value it is handed
and returns a value built from that text, every vocabulary it consults is an imported repository-local
constant, and nothing here opens a path, reads a remote or reaches another repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the migration's parser. It records the module's whole contract as the file states it: structure reported and nothing classified, every artifact getting one of the census's four outcomes, and no bad artifact raising. Those mechanisms are all cited here too — the four declared formats with the measured corpus population each reason names, the front-matter vocabulary that is also the metadata table's own stopping rule, the fenced-region heading read, the quote-aware citation delimiters bounded to the storable width, the two `doc_type` projections with the two import-time guards that keep them inside the closed vocabularies, and the unelided bounded prefixes every stored value is cut to. It also records two declared-but-unreached names, `OUTCOME_UNPARSED` and `classify_declared_format`, and the identical artifact-kind projection the inventory module declares independently. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
