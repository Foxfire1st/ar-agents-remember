# mcp/src/agents_remember/memory/knowledge/schema_generations.py

## Governing Overview


[memory route overview](../overview.md)

## Purpose


Declares and fingerprints the single schema used by disposable knowledge indexes.

## Code Commentary


CURRENT_GENERATION composes the retained table declarations into the current version-9 schema. The structure manifest and pinned fingerprint prevent an accidental schema change under the same identity. `generation_for_name` admits only that current schema; `generation_of_database` refuses a different user_version or structure. The former nine-generation runtime registry, per-generation constants, ancestry selector and declared-column helper are retired. Conversion of legacy memory is owned separately, not a read-time schema fallback.

- `SchemaGeneration` is a frozen record of everything a generation must be able to answer about
  itself: `schema_name`, `user_version`, the ordered `tables` manifest, per-table `columns`,
  `primary_keys` and `json_columns`, the required-SQLite-feature tuple `features`, `table_ddl`,
  `index_ddl`, `triggers`, and `fingerprint`. The key and typed-JSON registries are part of the
  pinned structure rather than derivations: the encoder orders each table's rows by its key tuple and
  decodes its typed-JSON columns, and **neither is recoverable from the DDL** — generation 1's DDL
  never spells `json_valid`, and a key tuple is declared data the encoder checks against the column
  list rather than reads out of DDL text.

- `structure_manifest` and `structure_fingerprint` are functions **of a record**, not of the build.
  That is what lets generation 1's recorded data be recomputed against its constant instead of
  against the code that produced it, and it is the one fingerprint definition in the package.

- `generation_for_name` is a name-to-record resolution for a caller that has already selected, not
  dispatch, and it refuses an unknown name rather than approximating one.

- `index_name` derives an index's name by splitting its `CREATE INDEX` statement. It validates
  nothing: a malformed statement yields a wrong name silently, which is acceptable only because the
  caller passes the module's own DDL constants.

## Evidence


### Repo-Internal References

- `structure_manifest` owns the current boundary described above. [37]
- `require_pinned_schema_unchanged` owns the current boundary described above. [38]
- `generation_for_name` owns the current boundary described above. [39]
- `generation_of_database` owns the current boundary described above. [40]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

- The frozen generation record and the eleven fields a generation must answer for itself; the key and typed-JSON registries are part of the pinned structure, not derivable from DDL. [41]
- The only place a build's own generation decides anything, and it decides only what a created store declares. [42]
- The one fingerprint definition, now a function of a record rather than of the running build. [43]
- Open-path dispatch by version alone, and the hard refusal of an unregistered version. [44]
- **The schema name generation 9 declares — `ar-knowledge-sqlite/v9`, the name a created store now carries.** [45]
- Generation 1's declared tables, columns, keys, JSON columns, DDL, triggers and features — the declarations this module delegates to and never restates. [46]
- The open path that calls this module's dispatch and the creation path that declares a generation. [47]
- The encoder that takes the selected generation instead of reading build globals. [48]

### Cross-Repo References

No cross-repository behavior is implemented in this file. A generation is a property of a dataset,
and a dataset's identity deliberately excludes Git commits, ledger rows and checkout locations.

No meaningful cross-repo references found.
