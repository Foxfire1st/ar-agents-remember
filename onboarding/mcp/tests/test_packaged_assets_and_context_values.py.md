# mcp/tests/test_packaged_assets_and_context_values.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/tests/test_packaged_assets_and_context_values.py`  |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-31T15:32+02:00                                  |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`              |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural tests for packaged-asset plumbing and coordination-context value handling.
These units were reachable from the suite only *incidentally*, so their interesting arms had
never been observed: the whole Windows half of the long-path normaliser, the
malformed-settings arms of the crossRepo parser, the prune-to-nothing arm of gate
compaction. Each test asserts a returned value, a file that exists (or no longer does) on
disk, or the exact error text a caller would see.

## Classes

| Class | Unit |
| --- | --- |
| `LongPathTests` | `long_path` prefixes Windows paths with the `\\?\` extended-length marker. |
| `CopyTraversableTreeTests` | `copy_traversable_tree` mirrors a `Traversable` onto disk (a `Path` is one). |
| `CrossRepoEntryToDictTests` | `cross_repo_entry_to_dict` emits four fixed keys plus only the **set** optionals. |
| `ParsedCrossRepoAllowEntryTests` | `parsed_cross_repo_allow_entry` **never raises**: it excludes and explains. |
| `GateStoreCompactTests` | `GateStore.compact` prunes consumed/expired gates and reports records removed. |
| `RangeTextTests` | `range_text` renders a benchmark metric column as a value or a low–high span. |
| `ProviderInvalidateIndexesTests` | `_provider_invalidate_indexes` — the destructive full-rebuild fan-out. |

## Two Testing Details That Must Not Be "Simplified"

**Windows semantics on POSIX.** Every Windows arm of `long_path` returns before it is
reached on POSIX, so `sys.platform` is patched **on the module under test**. Windows *string*
semantics — backslash separators, drive letters, UNC roots — come from `PureWindowsPath`
inputs, because a `PosixPath` treats a backslash as an ordinary filename character, which
would make the assertions fiction. `PureWindowsPath` has no `resolve`, so it is used only on
the `resolve=False` arms, which never call it.

**The destructive fan-out.** In `ProviderInvalidateIndexesTests` only the **two lifecycle
entry points** are patched — they shell out to docker. `_RecordingLifecycleRunner` stands in
for that process boundary. The dispatch, the per-provider action names, the temporary
settings file and the `ok` fold are the **real code under test**.

## Invariants And Boundaries

- `parsed_cross_repo_allow_entry` is total: a malformed entry is excluded with an
  explanation, never an exception into the settings load.
- `cross_repo_entry_to_dict` emits exactly four fixed keys plus set optionals — an unset
  optional must not appear as `null`.
- Gate compaction reports what it removed, including the prune-to-nothing case.
- No docker daemon is contacted.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Packaged-asset plumbing: long-path normalisation and traversable tree copy. | [package_data/](agents-remember/mcp/src/agents_remember/package_data/) |
| Coordination-context crossRepo parsing and gate storage. | [agents_remember/](agents-remember/mcp/src/agents_remember/) |
| The provider lifecycle entry points the fan-out drives. | [providers/](agents-remember/mcp/src/agents_remember/providers/) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  packaged-asset / context-value suite. Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
