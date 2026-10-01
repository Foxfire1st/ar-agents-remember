# mcp/src/agents_remember/memory/knowledge/citations.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The authored citation-binding write path: the binding's own rows, and every refusal between them.
One authored act lives here — record that this citation key, in this exact revision of this prose
document, denotes this knowledge record at this locator.

## Code Commentary

### Logic

The module carries the shipped pair of entry points, exactly as the facet and detection writes do:
`author_citation_binding` owns the candidate lock and one `BEGIN IMMEDIATE` transaction and returns a
typed `CitationBindingResult`; `apply_citation_binding` writes inside a caller's open transaction and
raises `KnowledgeRefused`, so a batch path rolls the whole batch back. That split is what makes "a
refused binding write leaves the dataset exactly as it was" a property of the transaction boundary
rather than a promise about statement order. `_apply_binding_write` and `_write_binding_rows` write the
envelope row, the sealed revision and the binding row together, so a binding whose sealed revision is
missing cannot exist.

`_validated_payload` routes the payload through `validate_record_payload` at the one envelope seam, so
an unregistered kind, a schema inadmissible for its kind, a payload that omits a required fact and a
payload carrying an undeclared field are all the same shipped `invalid_payload` refusal, raised before
any row exists.

`require_target_reference` is the reference check: the target record must be stored in this namespace,
a named revision must be a revision *of that record*, and the record's **recorded kind must be the
kind the reference declares** — a wrong-kind reference is refused at this boundary. `_require_governing_route`
refuses a named route that is not authored here, while `None` is the explicit **ungoverned** state.
`require_binding_generation` is the gate: a dataset whose recorded generation predates
`REQUIRED_BINDING_GENERATION` is refused with the observed generation as a fact, never migrated,
widened or written through.

`binding_row` derives the canonical column tuple, `local_key_text` renders the recorded key (or
`None` for a form this increment does not read), `binding_row_digest` is the row's own digest over its
*recorded* columns, and `load_binding_ids` is the ordered identity listing the read path uses.

### Invariants And Boundaries

- **The binding is authored, not inferred.** Nothing here derives a target from a path prefix, a
  folder name, a symbol string, a display label or a prose mention, and nothing searches for a nearest
  plausible record. A wrong-kind reference is a *write* refusal, which is why the read path's
  `target_kind_mismatch` can only arise from a store changed after the write.
- **Scope is never inferred.** `governing_route_id` is a parameter and is never derived from the
  document path, the target's path, the key's written source or the repository root.
- **Every reference is checked before the row it belongs to**, so a dangling reference is refused
  rather than stored and the read path never has to guess what an absent reference meant.
- **A rewritten key is a different key**, which is why the key is recorded as form plus exact text and
  the `UNIQUE` constraint makes "one owner revision records one key once" a table fact.
- This module writes no Markdown, re-parses no corpus and imports nothing from
  `memory_quality/style/citations/**`: the one citation authority stays where it is.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The two entry points and the transaction split that makes a refused write leave nothing behind.** [1]
- **The one payload decision point, and the reference check that refuses a wrong-kind or absent target before any row exists.** [2]
- **The governing-route check: a named route that is not authored here is refused, and `None` is the explicit ungoverned state.** [3]
- **The generation gate: a dataset that predates the binding table is refused with the observed generation as a fact.** [4]
- The row codec, the canonical key text and the row digest over the recorded columns. [5]
- The ordered binding identities the read path enumerates. [6]
- The one envelope seam this write path validates through, and the registry its decision reads. [7]
- The revision-row helper the sealed revision is written with, and the draft it takes. [8]
- The two operation members this write path and its read partner register. [9]
- **The boundary cases that measure the write refusals: a wrong-kind target, a target the namespace does not hold, and a dangling governing route beside an accepted ungoverned binding.** [10]
- The boundary case that proves the store itself refuses two bindings claiming one key in one owner revision. [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file. A binding records a fact about one memory
document and one knowledge record in the same namespace.

No meaningful cross-repo references found.
