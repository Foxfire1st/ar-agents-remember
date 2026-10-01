# mcp/tests/test_knowledge_citation_boundaries.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

The citation-binding boundary cases: 15 cases that drive a **real** memory repository, a real
SQLite store at generation 5 and a real Git object store, because each of them exists to catch a
fallback that only a real store can expose.

## Code Commentary

### Logic

`_MemoryRepository` builds a real Git repository holding the corpus documents the cases bind against;
`_BindingCase` builds a real knowledge store at the required generation and authors a real terminology
facet to bind to, so every binding in this module points at a record that exists rather than at a
fixture identity. That last detail is load-bearing: the envelope's `knowledge_record` is a different
identity space from generation 1's revision tables, and a case that bound to an invariant revision id
was correctly refused with `missing_expected_row`.

The cases divide into three groups.

**The resolution cases.** `test_a_binding_recorded_against_a_real_document_revision_resolves_to_it`
binds against a measured corpus key and asserts the whole item travels — kind, lifecycle, authority
home. `test_an_owner_revision_the_object_store_cannot_obtain_is_reported_as_unavailable` is the
fallback catcher: the document **is** on disk at the recorded path and the resolver still reports
unavailable, so a working-tree fallback would fail the case.
`test_a_rewritten_document_leaves_the_binding_stale_and_never_re_bound` really rewrites the document
and asserts the binding still reports the *recorded* revision, with `counts.stale == 1`.

**The write-boundary cases.** A wrong-kind target is refused with `invalid_reference`, the expected and
observed kinds named, and **nothing written**; a target the namespace does not hold is refused; a
dangling governing route is refused while an ungoverned binding stores and is reported as `None`; two
bindings claiming one key in one owner revision are refused by the store itself; and a generation-4
dataset is refused the binding table rather than widened.

**The retention cases.** Publication is proven to read back `matched` against the real file, `missing`
against a removed one and `mismatched` against an altered one, with the destination asserted outside
the enclosure and the archive by construction — `../escape.md`, `sub/dir.md`, `..`, `""` and
`a\b.md` are all rejected.

### Invariants And Boundaries

- Every case opens a real store and most of them build a real Git repository, so the module is
  registered in the **integration** lane. `_uncovered_key_case` writes the complete row pair (envelope,
  sealed revision, binding row) rather than the binding row alone, because a binding whose sealed
  revision is missing is a store defect that raises — reporting it as "the target is missing" would
  answer a question about the store with a claim about the binding.
- The module-local helpers are test source and are deliberately **not** registered in the governed
  test-input inventory.
- The corpus keys the cases quote are quoted as corpus data. Quoting a real path in a test is a
  dependency edge in two registries — the evidence census and the selection graph — which is why this
  module's path literals are registrations rather than decoration.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The real Git memory repository the resolution cases bind against, and the real store the write cases run on, each cited at its own declaration.** [1]
- **A binding against a real measured corpus revision, with kind, lifecycle and authority home travelling with the item.** [2]
- **The rewritten-document case: the binding keeps its recorded revision and is never silently re-bound, with the stale count measured.** [3]
- **The fallback catcher: the document is on disk at the recorded path and the resolver still reports unavailable.** [4]
- The write refusals: a wrong-kind target with the kinds named and nothing written, a target the namespace does not hold, and a dangling governing route beside an accepted ungoverned binding. [5]
- **The store itself refusing two bindings that claim one key in one owner revision.** [6]
- The dataset's own declared tables holding the binding rows, and a generation-4 dataset refused the binding table rather than widened. [7]
- **The retention cases: a published artifact reads back matched, a missing destination is blocked, changed bytes are mismatched, and the destination is outside the enclosure and the archive by construction.** [8]
- **The uncovered form produced on a real store by a directly written row pair, counted in a denominator of two and asserted distinct from the recorded-blob mismatch.** [9]
- The integration lane row this module occupies. [10]
- The integration lane row this module occupies. [11]
- The integration lane row this module occupies. [12]

### Cross-Repo References

No cross-repository behavior is exercised in this file. The memory repository the cases build is a
temporary Git repository local to each case.

No meaningful cross-repo references found.
