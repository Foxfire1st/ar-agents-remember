# mcp/tests/test_packaged_assets_and_context_values.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/tests/test_packaged_assets_and_context_values.py`  |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-08-01T14:20+02:00                                  |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`              |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural tests for packaged-asset plumbing and coordination-context value handling.
These units were reachable from the suite only *incidentally*, so their interesting arms had
never been observed: the whole Windows half of the long-path normaliser, the
malformed-settings arms of the crossRepo parser, the prune-to-nothing arm of gate
compaction. Each test asserts a returned value, a file's exact content on disk, or the exact
error text a caller would see.

## Classes

| Class | Unit |
| --- | --- |
| `LongPathTests` | `long_path` prefixes Windows paths with the `\\?\` extended-length marker. |
| `CopyTraversableTreeTests` | `copy_traversable_tree` mirrors a `Traversable` onto disk (a `Path` is one). |
| `CrossRepoEntryToDictTests` | `cross_repo_entry_to_dict` emits four fixed keys plus only the **set** optionals. |
| `ParsedCrossRepoAllowEntryTests` | `parsed_cross_repo_allow_entry` **never raises**: it excludes and explains. |
| `GateStoreCompactTests` | `GateStore.compact` prunes consumed/expired gates, reports records removed, and empties the log without unlinking it. |
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

## The Prune-To-Nothing Arm (260731-EFA-L5 R5)

The current prune-to-nothing arm is cit:([`test_pruning_the_last_gate_empties_the_workspace_log_without_unlinking_it`], mcp/tests/test_packaged_assets_and_context_values.py:419-444). It replaced the earlier delete-the-log assertion: that unlink is exactly what leaf 260731-EFA-L5 removed, because an appender that had already opened the log in `"a"` mode could keep writing into an inode with no remaining links — its snapshot disappeared along with the file, with no torn line and no exception for the caller to notice. The empty case was the most dangerous branch in the store rather than the dullest one.

The claim being proven is unchanged and not weakened. Two snapshots go in, `compact` still
reports removing both, and nothing survives; only the evidence for "nothing survives" moved,
from absence to emptiness — and it is now checked twice over, through the **strict** reader
(which raises rather than skipping, so an empty result cannot be a swallowed parse failure) and
against the raw bytes: `log_path(None).is_file()`, `read_bytes() == b""`, `read(None) == []`.

## Invariants And Boundaries

- `parsed_cross_repo_allow_entry` is total: a malformed entry is excluded with an
  explanation, never an exception into the settings load.
- `cross_repo_entry_to_dict` emits exactly four fixed keys plus set optionals — an unset
  optional must not appear as `null`.
- Gate compaction reports what it removed, including the prune-to-nothing case.
- An emptied gate log stays a file. `assertFalse(path.exists())` is the shape 260731-EFA-L5
  removed and must not come back: absence and emptiness are not the same evidence, and only
  emptiness proves the records left rather than that the file did.
- No docker daemon is contacted.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Packaged-asset plumbing: long-path normalisation and traversable tree copy. | `long_path`, `copy_traversable_tree` | mcp/src/agents_remember/install/assets.py:17-32; mcp/src/agents_remember/install/assets.py:50-62 |
| CrossRepo serialization emits the fixed and set optional fields. | `cross_repo_entry_to_dict` | mcp/src/agents_remember/kernel/coordination_context/serialize.py:42-57 |
| CrossRepo parsing excludes malformed entries with an explanation instead of raising. | `parsed_cross_repo_allow_entry` | mcp/src/agents_remember/kernel/coordination_context/setting_values.py:86-103 |
| Gate storage supplies the strict read and compaction path under test. | `GateStore` | mcp/src/agents_remember/controlplane/store.py:96-325 |
| Gate compaction uses the store rewrite seam. | `_replace` | mcp/src/agents_remember/controlplane/store.py:316-325 |
| The shared rewrite never unlinks an empty destination. | `rewrite_lines` | mcp/src/agents_remember/controlplane/durable_store.py:448-455 |
| The suite that measures what the unlink was costing, across all six control-plane logs and against the leaf's base commit. | `test_no_record_is_lost_when_a_compaction_empties_and_unlinks_the_log` | mcp/tests/test_controlplane_store_durability.py:140-153 |
| The provider lifecycle entry points the fan-out drives. | `run_grepai_lifecycle`, `run_cgc_lifecycle` | mcp/src/agents_remember/providers/lifecycle_service.py:50-94; mcp/src/agents_remember/providers/lifecycle_service.py:97-137 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:12:00+02:00 — 260731-EFA-L6-W3-B01 curator: curated 8 Repo-Internal table citations and 1 prose citation with exact asset, context, gate-store, durability-suite, provider-lifecycle, and current prune-arm anchors. Verification metadata remains unchanged for closeout.

- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator: the prune-to-nothing arm changed its evidence
  and the card gained a section for it. The earlier delete-the-workspace-log test became
  `test_pruning_the_last_gate_empties_the_workspace_log_without_unlinking_it`, replacing
  `assertFalse(self.store.log_path(None).exists())` with
  `is_file()` + `read_bytes() == b""` alongside the unchanged `read(None) == []` and
  `removed == 2`. The unlink it used to assert is the defect the leaf removed (R5): `_replace`
  called `path.unlink(missing_ok=True)` on an empty kept set, so an appender already holding the
  log open in `"a"` mode wrote into an inode with no remaining links and lost its snapshot with
  no torn line and no exception. The claim is not weakened — the same two snapshots go in and
  the same nothing survives; the evidence moved from absence to emptiness and is now checked
  twice, through the **strict** reader (so an empty result cannot be a swallowed parse failure)
  and against the raw bytes. Updated the Purpose sentence that promised "a file that exists (or
  no longer does) on disk", the `GateStoreCompactTests` row in the class table, added an
  invariant that `assertFalse(path.exists())` must not come back, and added three Repo-Internal
  rows (the compaction and strict read under test, the never-unlinking `rewrite_lines` behind
  them, and the durability suite that measured the cost). This card carries no line citations in
  its reference table, so nothing needed re-anchoring there. Verification metadata pinned until
  closeout stamps the L5 commit.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  packaged-asset / context-value suite. Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
