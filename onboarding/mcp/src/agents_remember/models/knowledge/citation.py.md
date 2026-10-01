# mcp/src/agents_remember/models/knowledge/citation.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The `CitationBinding` vocabulary: what a prose citation binds, and every state one binding
observation resolves to. It declares the **prose owner revision**, the **local citation key as
written**, the **typed target reference** and the **locator inside the target's recorded scope**,
together with the closed nine-member state set, the counts validator, the key-form coverage record
and the closure request/result pair.

## Code Commentary

### Logic

`ProseOwnerRevision` is the memory repository, the document's repository-relative confined POSIX
path and the **recorded Git blob identity** of that document — the shipped `GitBlobIdentity`
convention `models/knowledge/source.py` already uses for "these exact recorded bytes", not a digest
scheme invented here. The identity is *referenced and not minted*: it names an object the memory side
already supplies, and the read path addresses that object rather than hashing whatever the file now
contains.

`ProseCitationKey` stores the key in two halves plus the written source, and `TableRowKeyForm` is the
second, recognized form; `KEY_FORMS` declares both and `COVERED_KEY_FORMS` declares only
`prose_cit_body` — so a table-row key is *present and recognized* and resolves to
`uncovered_key_form` rather than being folded into "absent". `render_local_key` is the one rendering
of either form. `WrittenSource` keeps the prose's own `path:start-end`, which is what makes "target
reference and locator" carried rather than lost.

`CitationTargetReference` is a typed identity (record id, declared kind, optional exact revision),
and `CitationBindingPayload` composes the four facts. `BINDING_STATES` is the closed nine-member
vocabulary; four of its members are *literally* members of the shipped `ANCHOR_RESOLUTIONS` and
`SHIPPED_STATE_FACTS` plus `shipped_literal_for` state that mapping once. `models/knowledge/read.py`
deliberately gains **no** member: the extension is one-directional, so an anchor resolution can never
acquire a citation fact.

**What the binding stores is one table plus a column, and the payload's own docstring says so.** This
leaf appends exactly **one** table — `citation_binding` — and the binding's governing route is a
nullable `governing_route_id` **column on that same row**, a real foreign key into the existing `route`
entity, rather than a second per-binding association table beside it; no generation-1 or generation-2
table is altered. The binding's recorded identity, lifecycle and provenance come from the envelope, which
already carries a governing-route association for `knowledge_record`. The vocabulary module states this
because the delivered schema is the authority for it: `schema_v5.py` declares one appended table and a
nullable route column on it, so a reader who took the payload's own prose as the schema would expect a
second table that generation 5 does not have.

`CitationBindingCounts` refuses a report that omits a declared state or whose per-state counts do not
partition the declared selected set — that is the mechanism by which an unresolved key cannot be
dropped from a denominator. `KeyFormCoverage` refuses to leave an uncovered form uncounted, and
`CitationBindingClosureResult` carries limitations and coverage and **no** semantic-completeness
field.

### Invariants And Boundaries

- **Nothing here is a content address, a logical digest or a fingerprint.** `payload_digest` stays on
  the revision aggregate that owns it; a binding is not an identity of the prose it cites. Ambiguity
  ("more than one binding claims one key in one owner revision") is detected by equality over the
  *recorded key text*, which is the fact at issue, not by a computed digest that would have to be
  kept in step with it.
- **The locator is the shipped `SourceLocator` union**, imported rather than reduplicated, so a
  binding-local locator spelling is inexpressible rather than merely unwritten. A recorded locator
  stays readable when no resolver supports it, which is why `unsupported_locator` is a reported state
  and not a write refusal.
- **A rewritten key is a different key.** The key is stored as its parts, not as one flattened
  string, so whether the anchor text, the file or the extent moved stays distinguishable.
- **The state vocabulary is closed and exhaustive.** `BINDING_STATES` names every member; a state
  that cannot be populated today is still a counted member with a zero entry.
- This module holds no store handle and writes nothing: it is the vocabulary the write path, the read
  path and the closure all speak. The **schema** the binding's payload describes is not declared here:
  generation 5's append belongs to `memory/knowledge/schema_v5.py`, which is why the payload docstring
  names the one table and the route column it actually has rather than describing an association table
  this module does not own.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The owner revision as a referenced and not minted identity: repository, confined document path, and the recorded Git blob identity the memory side already supplies.** [1]
- The written source the prose itself carries, and the ordered-range refusal that keeps it readable. [2]
- **Both key forms, the declaration of which form this increment reads, and the one rendering of either.** [3]
- The typed target reference and the authored payload that composes the binding's four facts. [4]
- **The schema the binding's payload describes: generation 5 appends exactly one table, and the governing route is a nullable column on that same row rather than a second association table.** [5]
- **The closed nine-member state vocabulary, the four members that ARE shipped literals, and the one mapping that states which fact each reuses.** [6]
- **The counts validator that refuses a report whose per-state counts do not partition the declared selected set, and the coverage record that refuses to leave an uncovered form uncounted.** [7]
- The observation, the indivisible closure item, the closure request and the result that carries limitations and no semantic-completeness field. [8]
- The shipped source identity this vocabulary references instead of minting a second one. [9]
- The one locator union the binding must use, and the shipped anchor vocabulary the four shared literals come from. [10]
- The declared selection bound the closure's refusal names. [11]
- **The cases that measure the closed vocabulary in both directions, the shipped-literal identity, the counts partition and the uncovered-form state.** [12]

### Cross-Repo References

No cross-repository behavior is implemented in this file. A binding is a fact about a memory
document and a knowledge record, and neither identity space carries a repository boundary.

No meaningful cross-repo references found.
