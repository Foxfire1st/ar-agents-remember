# mcp/src/agents_remember/memory/knowledge/family_view.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The **Family projection**: what one family revision's recorded composition, owning route and
explanatory context *are*, reported from the canonical rows.

**It reports and never traverses.** The projection has no reached set, follows no edge, and fills no
gap. A missing composition link, a missing owning route and a missing explanatory context are all
reported as **absent**; nothing here infers a relationship from a display label, a folder or path
ancestry, a prefix, a symbol, a shared member, a shared anchor or a prose sentence. A revision whose
members all live under one route's path and which records no owning route is reported
**ungoverned**, not governed by that route.

## Code Commentary

### Logic

- `family_revision_view` — the one entry point. It reads the stored links, the recorded owning route
  (or the explicit ungoverned state) and the authored context, and returns them with their
  provenance.
- `FamilyRevisionView` — the value. Each link carries its **direction** and the **policy version it
  was declared under**, because a link reported without that version would be unreadable against
  another version of the same policy.
- The three reads it uses are the projection's own lookups in `read_queries.py`
  (`fetch_composition_rows`, `fetch_owning_routes_for_revisions`, `fetch_contexts_for_revisions`),
  ordered through the order-column registrations that module declares. The projection holds no
  statement of its own.

### Conventions

- **Derived output, not a second authority.** The view is regenerable at will from the canonical rows
  and writes nothing; every statement it runs is a `SELECT` on the caller's connection. Reading it
  twice changes nothing.
- **Only stored facts, and absences are stated.** There is no computed set of "related families"
  presented as a recorded relationship.
- The one value that could be mistaken for a traversal's result — the declared depth bound — travels
  as *the policy's declared bound*, labelled as a declaration, beside the links it declares.

### Invariants And Boundaries

- **The projection does not traverse.** It carries no reachable set and it never imports
  `composition_traversal.py`; a case asserts both.
- **The composition table is deliberately not consulted for selection anywhere.** The selected set,
  the counts, the ordering, the revision groups, the advertised frontier and the manifest digest are
  unchanged by this leaf, and the retrieval read does not import this module.
- **The projection is not an authority.** It decides no relationship, mints no identity and records
  no status; it presents what is stored.
- **Boundary.** Reading the stored rows is `compositions.py`; walking declared edges under a policy is
  `composition_traversal.py`. This module only presents.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The one projection entry point, which reports the stored links, the route or the explicit ungoverned state, and the recorded context.** [1]
- The projection's value, whose links carry their direction and the policy version they were declared under. [2]
- The ungoverned state's own read, which never fills the gap. [3]
- **The case that drives the projection through the read-only application seam and asserts the recorded link is reported with its policy version.** [4]
- **The same case's second half: a family revision this namespace does not hold is a typed refusal, and the file is byte-identical afterwards.** [5]
- **The case that proves a composition graph leaves the shipped selection exactly as it was.** [6]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
