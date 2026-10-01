# mcp/src/agents_remember/memory/migration/mappings.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The explicit mapping registry: data a reviewer can read, not an inference at parse time. `KS-R21@v1` §2.1
requires every imported artifact to be imported under an **explicit mapping** naming its source artifact
form, the target record kind and the fields the mapping supplies, and it requires that mapping to be data
that can be inspected and reviewed rather than an inference performed at parse time or a table of
heuristics inside the parser — so the mapping is a value here, selected by an equality test on a
**declared** field of the artifact (its `doc_type` and its format name) and never by a property of the
artifact's prose. Where no entry matches, the outcome is `UNMAPPED`, a named state, and §2.2 forbids the
three things an importer does when it only pretends to be mechanical: it does not construct a best-fit
mapping, it does not choose a target kind by name similarity, and it does not create a record so that the
row looks complete. There is deliberately no scoring function in the module, because a "closest" mapping
would be an inference with a distance metric on it, and `select_mapping` therefore returns `None` rather
than a candidate. Every entry declares the fields it supplies, and the registry declares four entries over
the census's three record kinds, one of which is a wildcard matching any declared doc type so that an
artifact with no declared form still receives an explicit migration disposition instead of vanishing.

## Code Commentary

### Logic

**A mapping is a value, and selection is an equality test over declared fields.** The module docstring
quotes the requirement's own terms and draws the line the rest of the file keeps: the registry is data,
selection is an equality test on the artifact's `doc_type` and format name, and no property of the
artifact's prose takes part. `MAPPINGS` is the whole registry as a tuple, and `ExplicitMapping` is one
entry: a `mapping_id`, the `artifact_format` and `artifact_doc_type` that select it, the `record_kind` it
targets, the `supplied_fields` it fills, the `provenance_fields` it carries into the stored provenance, and
a `rationale` written for a reviewer. The class docstring separates the two field declarations: the
supplied fields are §2.1's declaration and are described as checked against the target payload model's own
required field set, while the provenance fields are the artifact's declared front-matter keys that travel
into the record because the artifact, the location within it and the baseline are supplied by the importer
itself.

**Four entries, three record kinds, and one wildcard.** The registry declares
`file-card-to-inventory-row`, `route-overview-to-inventory-row`, `file-card-to-claim` and
`artifact-to-disposition`. The first two target the inventory row kind — one for a file-level card that
declares the source it documents and the revision it was verified against, one for a route overview that
declares its scope through `sourceRoute` and therefore supplies an observed route path instead of a
declared source path, which the entry's rationale names as what lets a route with no cards be reported.
The third targets the claim kind and supplies only `claim_text` and `claim_location`. The fourth targets
the disposition kind, is the one entry whose `artifact_doc_type` is `*`, and supplies only
`disposition_kind`; its rationale states that every artifact gets a migration disposition, including the
ones deliberately not imported, because non-claim content and historical material must carry an explicit
disposition rather than silently vanishing from the inventory. The record kinds themselves are imported
names — `CENSUS_INVENTORY_ROW_KIND`, `CENSUS_CLAIM_KIND` and `CENSUS_DISPOSITION_KIND` — so a target kind
this module names is a kind the census model already declares.

**Selection has two stated limits.** `select_mapping` first refuses a format the registry does not
declare, returning `None` before any entry is examined; the docstring ties that to the §1.1 rule that an
undeclared format is a finding rather than a silent extension, and says the format test is kept here so
the unmapped state stays reachable. Then it walks `MAPPINGS` in registry order, skips every entry whose
`artifact_format` differs, and returns the first entry whose `artifact_doc_type` is either `"*"` or equal
to the artifact's declared `doc_type`, with a `None` doc type normalised to the empty string first. The
wildcard is the second limit's whole content: it matches any **declared** doc type, and the docstring
calls an artifact that declared none the honest attribution for a piece whose form is unknown.

**Fields a mapping may not supply, and the one authored field each rationale refuses.** The claim entry's
rationale is the module's clearest boundary statement: it supplies only the claim's original text and its
location, and deliberately supplies no claim kind, no applicability and no assessment, because those are a
curator's authored work and a mapping that filled them would be the importer interpreting prose. The
disposition entry makes the same refusal for one field, supplying the disposition's kind and never a
rationale, which the payload model carries as an authored field beside the kind. The registry version is a
separate declaration: `MAPPING_REGISTRY_VERSION` records which registry produced an outcome, on the
docstring's reasoning that a changed registry is a changed mapping and a re-run at a different mapping is a
difference to report rather than a silent second import.

**Unmapped is a named state produced in one place, and absence has its own spelling.**
`UNMAPPED` is a `Literal["unmapped"]` whose value is a member of the closed disposition vocabulary the
census payload already declares, so an unmapped artifact appears in the census's dispositions rather than
in a log line. `NO_MAPPING_ID` is the empty string an unmapped outcome carries, which is what lets a
reader tell "no mapping existed" from "a mapping existed and was named" — an empty identifier is the
absence, never a blank mapping — and `mapping_identity` is the one place that choice is made. The
disposition value itself is returned by `unmapped_disposition`, a function rather than a constant read at
the call site, so that "no mapping exists" is produced in one place and a later reader can see the state is
*chosen* here rather than defaulted there.

**A second access path by target kind.** `mappings_for_kind` returns every entry whose `record_kind` is
the one asked for, in registry order, which is the access path that reaches a mapping whose selector pair
another entry already claims. `DECLARED_FORMATS` is derived from the registry rather than written out — the
sorted set of the entry formats — and it is the gate `select_mapping` tests, so the format vocabulary this
module admits is exactly the vocabulary its own entries use.

### Conventions

The module declares one frozen dataclass and no model of its own: every record kind it targets is an
imported constant from the census payload models, and its two outcome values are typed against the
vocabularies those models close — `UNMAPPED` as a `Literal` whose single value the disposition vocabulary
contains, and `select_mapping`'s `None` return as the absent mapping rather than an empty entry. The
registry is a module-level tuple and the derived format list is computed from it at import, so the two
cannot disagree; the docstring, the dataclass docstring and each entry's `rationale` carry the reasoning a
reviewer needs, and the wildcard's rationale states the one case the selector cannot express through
equality. There is no `__all__`, no scoring, no distance function and no fallback entry: the module's
public surface is the dataclass, the registry, the derived format tuple, the two outcome values and the
four functions.

### Invariants And Boundaries

- **Selection reads declared values only.** The equality test is over `artifact_format` and
  `artifact_doc_type`; no entry, function or default in this file consults the artifact's prose, its path
  or its content.
- **An undeclared format selects nothing.** `select_mapping` returns `None` before examining an entry, so
  a format the parser met but the registry never admitted is `unmapped` rather than matched by the nearest
  entry, and no best-fit, similarity or completeness rule exists to absorb it.
- **One wildcard, and it supplies one field.** `artifact-to-disposition` is the only entry whose
  `artifact_doc_type` is `*`, it matches a doc type the artifact never declared, and it supplies only
  `disposition_kind` — never the disposition's rationale, which is authored.
- **No mapping supplies an authored field.** No entry supplies a claim kind, an applicability or an
  assessment, so the importer this registry drives has no field in which to interpret prose.
- **Target kinds are imported, not spelled.** Every `record_kind` is one of the census model's own kind
  constants, so a kind this registry names cannot drift from the kind the payload registry resolves.
- **The format vocabulary is derived, not restated.** `DECLARED_FORMATS` is computed from `MAPPINGS`, so
  the gate and the entries are one declaration; in the shipped candidate that vocabulary has exactly one
  member, `markdown-metadata-table/v1`.
- **Two entries share a selector pair and selection returns the first.** `file-card-to-inventory-row` and
  `file-card-to-claim` declare the same format and the same `doc_type`, and `select_mapping` returns the
  first match in registry order, so the claim mapping is unreachable through `select_mapping` and reachable
  only through `mappings_for_kind`.
- **The registry's own comment counts three entries while the tuple declares four.** The comment above
  `MAPPINGS` states that "the three entries below are the whole registry" while four `ExplicitMapping`
  values follow; the count that is true of the registry is its three record kinds.
- **The payload-model check the docstring describes is not performed in this module.** No code in the
  shipped candidate compares an entry's `supplied_fields` against the target payload model's required field
  set; the registry assertions the migration test module does make are narrower — the wildcard is the only
  entry matching any doc type, and no entry supplies `claim_kind`, `applicability` or
  `assessment_disposition`.
- **The registry version is recorded and never read.** `MAPPING_REGISTRY_VERSION` is declared so an outcome
  can name the registry that produced it, and no module or test in the shipped candidate reads it.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The registry is the join between the artifacts the parser observed and the record kinds the census payload
models declare, and it is the module that decides which of those records an artifact can become. The rows
below cite the entry shape and what it declares, the four entries and their three record kinds, the
selector and its two limits, the wildcard and the fields every rationale refuses, the named unmapped state
with its one production site, and the recorded facts this candidate leaves in the file.

- The registry's own statement of its status as data: §2.1's explicit mapping, §2.2's three forbidden moves, and the absence of any scoring function. [1]
- The registry itself: four entries, each naming its source form, target record kind, supplied fields, provenance fields and rationale. [2]
- The four mapping identifiers and the three record kinds they target, with the inventory row kind reached by two entries. [3]
- The record kinds imported from the census payload models rather than spelled as literals. [4]
- The selector: an equality test on the declared format and doc type, with an undeclared format refused before any entry is examined. [5]
- The wildcard entry, which matches any declared doc type including none and supplies only the disposition kind. [6]
- The claim mapping's boundary: original text and location supplied, no claim kind, no applicability and no assessment, because those are a curator's authored work. [7]
- The route-overview entry and the reason it supplies an observed route path instead of a declared source path. [8]
- The unmapped state as a value of the closed disposition vocabulary, and the empty identifier that distinguishes no mapping from a named one. [9]
- The one place that produces the unmapped disposition, so the state is chosen rather than defaulted at a call site. [10]
- The second access path, by target record kind, which reaches a mapping whose selector pair another entry already claims. [11]
- The registry version recorded beside every outcome, and the payload field — a disposition's rationale — that the wildcard entry deliberately leaves empty. [12]
- Two entries declare the same format and doc type, and the first match in registry order wins, so the claim mapping cannot be reached through the selector. [13]
- The registry comment that counts three entries where the tuple declares four, and the format vocabulary derived from those entries, which has exactly one member. [14]
- The registry properties the migration test module does assert, and the supplied-field declaration they are asserted against. [15]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The registry is a tuple of values selected by
string equality, every vocabulary it consults is an imported repository-local constant, and nothing here
opens a path, reads a store or reaches another repository.

No meaningful cross-repo references found.
