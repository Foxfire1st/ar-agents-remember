# mcp/src/agents_remember/memory/knowledge/schema_v5.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Retained citation_binding appended-table declarations for the derived-index schema. The historical schema_v5 filename names its origin, not a separately openable generation. The one composition keeps the base and all appended declarations in recorded order. [5] [6]

## Code Commentary

### Logic

APPENDED_TABLES and the column/key/JSON/DDL/index/trigger/feature maps contribute citation_binding to the sole _compose pass. The table retains document revision, exact local key, typed target/locator and nullable governing route. Its constraints seal those recorded facts; no generation registry supplies a creation or migration route. [1] [3] [5]

### Invariants And Boundaries

- **Appending is the only sanctioned way to add a table** (`KS-R10@v1` §1.3). Nothing here
  redeclares, reorders, renames, retypes or drops a generation-1..4 table, and no `ALTER TABLE`
  against an earlier generation's table exists anywhere in this package.
- **There is no digest, content address or fingerprint column, and the absence is the point.** The
  owner revision's blob identity is a *reference* to an identity the memory side already records, not
  a second one minted here. Ambiguity is decided by equality over the recorded key text.
- **The local key is stored as a form and its exact text.** `UNIQUE (repository_id,
  owner_document_path, owner_blob_object_id, local_key_form, local_key_text)` makes "one owner
  revision records one key once" a constraint of the table rather than a rule the write path
  remembers.
- **`target_locator_kind` is checked against the shipped union.** The `CHECK` names the union's three
  members and no fourth, so a binding-local locator spelling is inexpressible rather than merely
  unwritten.
- **The governing route is a nullable foreign key on the binding's own row**, resolved against the
  existing `route` entity: at most one governing route per binding is a constraint, a named route
  that does not exist is unrepresentable, and `NULL` is the explicit **ungoverned** state.
- **The recorded facts are sealed by triggers.** Rewriting a key or re-pointing a target in place
  would silently re-bind the row to prose that says something else; generation 5's triggers refuse
  exactly that, while leaving `lifecycle` free because a binding's lifecycle is its owner's.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The one table generation 5 appends, and the registries the composition merges from.** [1]
- The typed-JSON column registry, which is where the binding payload actually travels. [2]
- **The table DDL: the unique key over the recorded key text, and the `CHECK` that names exactly the shipped locator union.** [3]
- The index DDL and the triggers that seal the recorded facts against in-place re-binding. [4]

- The one schema composition appends retained definitions in order. [5]


- Single v9 schema, not an openable generation5. [6]

- The generation-2 `route` table the governing-route foreign key resolves against. [7]

### Cross-Repo References

No cross-repository behavior is implemented in this file. A table declaration is a property of the
dataset, and a dataset's identity excludes Git commits, ledger rows and checkout locations.

No meaningful cross-repo references found.
