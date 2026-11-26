# mcp/src/agents_remember/application/knowledge_reader/marks.py

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Read weakness anchors and derive dependent movement at the selected code tree, while sharing one open-weakness count over an already-open knowledge index.

## Code Commentary

weakness_list reads valid typed records in id order, filters folder/kind/open state and optionally observes anchors through the shared currentness owner. A stale anchor remains a readable marked row. Observations are cached within the read; invalid records are skipped as validator findings. open_weakness_counts delegates to open_weakness_counts_in, which counts only open records with a path at the supplied index and omits zero-count paths.

For a closed weakness, `weakness_list` obtains the `closed` display from `weakness_closure.closure_document`. [6] That returned copy preserves an explicit closing commit or derives it from the closure's memory-history origin; pending or unavailable attribution is disclosed as `commitNote`, without changing the stored record. [6]

dependent_movement walks recorded links in order: record revision mismatch/missing record, whole-file absence or an unexcepted blob change, or anchor-content movement produces a moved row. Any moved link gives stale, including any additional unverifiable rows; only unverifiable links with none moved gives unverifiable, otherwise current. This state is derived and never stored. For a whole-file link, a changed blob stays current when its only changes substitute the product's complete confirmed version token with its complete selected version token. Product identity comes from `project.version` in `mcp/pyproject.toml` at the dependent's exact confirmation revision and the selected code tree, rather than the runtime version resolver or working files. A token may remain unchanged; a changed token must exactly match the old-to-new product substitution, preserving a leading `v` or `V`, and all other bytes must remain unchanged. An epoch, extra release component, or pre, post, dev or local part belongs to the complete token, so an embedded matching product substring does not excuse a different version. Missing old or selected version provenance excuses no changed blob. Text-only comparison cannot distinguish a dependency whose complete old and new version tokens equal the product's from an own-product substitution; this is the recorded weakness of the rule.

File attribution names the newest path commit only when its value matches the observed blob/absence, including deletion. Anchor attribution follows bounded newest-first path commits and requires the observed anchor transition, so an unrelated constant edit is not called the mover. Selected commit provenance is exact, or HEAD only when its whole tree matches; dirty/unpaired/historical trees without that provenance do not borrow later HEAD history. Unknown attribution names its reason.

dependent_list supports folder, stale-only and standing-on-code filters and emits each moved link. dependent_counts counts documents per distinct anchor/file path. Record-link movement is a memory revision fact, not a code commit. dependent_state_at returns absent for no dependent, unverifiable for invalid/read-failed data and otherwise the derived state.

`dependent_list` and `dependent_detail` project open deferrals through `derive_deferrals`, `infer_reading_leaf`, and `load_task_facts`, marking deferred dependents with `state: "deferred"` (while preserving `stalenessState` and `deferred: True` and surfacing them under `staleOnly=True`); `dependent_state_at` returns `"deferred"` when deferrals are open, and `dependent_state` accepts an optional pre-opened `code` tree.

## Invariants And Boundaries

No function writes a record or stores derived staleness. Card counts carry quantities, not weakness sentences or dependent text. The new index-taking helper performs the same validated open-record count as the ordinary selection reader and lets focused cards reuse the bound after index already open.

## Evidence



- Weakness lists and the shared open-index count retain validation/filtering and omit zero paths. [1]




- Mixed moved/unverifiable links follow explicit stale-first precedence. [2]


- Whole-file product-version substitutions use exact confirmation/selected metadata and complete token boundaries; equal dependency/product token pairs remain indistinguishable. The regression cases exercise both dependent reading and landing computation.


- Attribution checks the observed file/anchor transition rather than unrelated path edits. [3]


- Only exact committed provenance can select history for attribution. [4]

- Dependent filters, per-path counts and single-record failure labels remain derived. [5]


- Closed weakness rows use the shared closure display without changing the stored record. [6]
