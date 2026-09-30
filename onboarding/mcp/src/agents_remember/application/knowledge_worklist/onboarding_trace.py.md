# mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**MIK-R30's `onboarding_trace` item kind: its registration, the gate's two memory sides, and its items in
the leaf's one worklist.** The rule itself is `worktrees/modules/onboarding_trace.py`; this module registers
the kind in MIK-R08's registry, resolves K_B and K_C for it (the converted base included), and merges the
gate's items into `knowledge-worklist.json` so the closeout gate (MIK-R09) consumes one list.

## Code Commentary

### Logic

- **Registration (MIK-R30 rule 7).** `ONBOARDING_TRACE_KIND` is `register_item_kind(ItemKind(...))` at
  import: name `onboarding_trace`, subject pattern `^onboarding:\S`, facts `sources`, `markdown`, `sidecar`,
  `countedChange`, owner `MIK-R30`, and `row_lookup=subject_row(ITEM_KIND)`. The row lookup covers the row
  half of the satisfying rule only; `onboarding_item_open` applies both halves. The package `__init__`
  imports this module, so the kind is registered whenever the worklist is.
- **Sides.** `onboarding_trace_sides(TraceSideRequest)` reads K_C from the memory candidate directory and
  K_B from its commit (`knowledge_tree_from_directory`, `knowledge_tree_from_git`). Since MIK-R09 (L09)
  `TraceSideRequest.memory_candidate` may also be a Git tree of the memory repository, the gate's exact candidate,
  which is read with `knowledge_tree_from_git`; the pairing's `memoryCandidate` is then the tree ID:
  - neither converted: `None`, and the caller keeps today's gate;
  - K_B converted and K_C not: an incomplete side, "K_C is unconverted while K_B is converted; the crossing
    sync converts it";
  - K_C marked but without a pinned conversion version: an incomplete side naming that;
  - K_B unconverted, K_C converted: K_B is replaced by its conversion through
    `base_cache.converted_base_files`, which reads or fills the converted-base cache (MIK-R24 rule 7).
  Both sides are then restricted to `onboarding/`, `knowledge/history/` and the layout marker
  (`_onboarding_and_history`). The pairing records `base`, `memoryBase`, `convertedBase` and
  `memoryCandidate`.
- **Storage settings.** `trace_context(contract)` parses the memory worktree's own `system/settings.md`, as
  closeout resolves it, then falls back to `contract_context`, and only with neither to the resolver's
  default `StorageSettings()`, which gates every source (the strictest reading). Since MIK-R09 every settings file
  it reads is recorded through `kernel.recorded_reads.record_read`: the worktree's own file (read, or `absent`, which
  is why the fallback is taken), the context's settings paths, and the coordination fallback
  `system/settings.md`. None lies in a tree, so the mandatory gate's memo re-hashes them before reusing a verdict
  (L09 review R1 notes, ruling 2026-09-30T16:07:55). Outside a recording block nothing changes.
- **One list (ruling Q2).** `worklist_onboarding(document, contract, request)` runs only on a `complete`
  worklist. It computes the gate over the worklist's own B..C `changes[].path` and calls
  `with_onboarding_items`, which appends each item's document (`id`, `kind`, `subject`, `facts`,
  `satisfiedBy`), sorts the whole list by `(kind, subject)`, adds `onboardingTrace` (`openCount`,
  `unnecessaryRows`) and recomputes the digest. Any side failure, or any gate problem, turns the worklist
  `incomplete` with a named reason (K_B for sides, K_C for a gate problem), so the list is never silently
  short.

### Conventions

- `leaf.py` builds the `TraceSideRequest` (`_trace_request`) and exposes `leaf_onboarding_trace_sides`; this
  module does not import `leaf.py`, which avoids an import cycle.

### Invariants And Boundaries

- **`onboarding_trace` items go into the persisted worklist** (architect ruling 2026-09-29T18:49:50 (2)),
  with their satisfaction state, so L09 consumes one list.
- **The converted-base cache is extended to the Markdown the gate compares** (ruling 18:49:50 (4)); see
  `base_cache.py`.
- **Mixed formats give an incomplete side, never a vacuous pass** (ruling 19:23:45 N1): comparing a legacy
  card with its converted counterpart would make every card look changed.
- **Items are sorted by `(kind, subject)`**, L08's items and the gate's together, before the digest (ruling
  19:23:45 N2).
- **A side failure names its error kind** on the `incomplete` worklist (ruling 19:23:45 N4).
- **Unconverted trees keep today's gate.** `onboarding_trace_sides` returns `None` when neither side holds
  the layout marker, and the worklist itself is `None` there.

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R30@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`30_onboarding-refresh-gate-on-history-files.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: registration, sides and the one list. | "its registration, its sides and its worklist items." | mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:1-27 |
| The kind's four registry fields, registered on import. | `ONBOARDING_TRACE_KIND`; `register_item_kind` | mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:76-90 |
| The explicit inputs of the side resolution. | `TraceSideRequest` | mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:93-107 |
| The sides: `None`, the two mixed-format refusals, and the converted base. | `onboarding_trace_sides` | mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:110-166 |
| K_C may be a Git tree, the gate's exact candidate (MIK-R09). | "K_C: the memory working tree, or a Git tree of" | mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:101-102 |
| The storage settings the gate reads; since MIK-R09 each settings file read is recorded. | `trace_context`; "absent: the fallback below is taken because of it" | mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:177-208 |
| The gate's items merged, sorted and digested into the one list. | `with_onboarding_items` | mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:217-248 |
| The worklist step, which names any side failure. | `worklist_onboarding` | mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:251-274 |
| The worklist run that calls it after a complete run, since MIK-R09 inside `worklist_over`. | `worklist_over`; `worklist_onboarding` | mcp/src/agents_remember/application/knowledge_worklist/leaf.py:530-552 |
| The persisted worklist carries the gate's items in order. | `test_the_persisted_worklist_carries_the_onboarding_items_in_its_one_list` | mcp/tests/test_onboarding_trace_gate.py:725-747 |
| Mixed formats are an incomplete side and the persisted worklist is `incomplete`. | `test_mixed_formats_are_an_incomplete_side_never_a_vacuous_pass` | mcp/tests/test_onboarding_trace_gate.py:438-461 |

## Cross-Repo References

The sides are read from the leaf's paired code and memory repositories (the configured pair of one
repository), not from another code repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09.** The Sides bullet records that `TraceSideRequest.memory_candidate` may be a Git tree (the gate's exact candidate), and the Storage-settings bullet that every settings file `trace_context` reads is recorded for the gate's memo (review R1 notes, ruling 16:07:55). One row added and the settings row extended. The worklist-run row into `leaf.py`, whose construct moved and which the fixer could not project, was re-measured: it now cites `worklist_over` (`530-552`), where the call lives since MIK-R09.
- 2026-09-30T17:58:58+00:00: Generated citation repair: `worklist_onboarding` repointed to mcp/src/agents_remember/application/knowledge_worklist/onboarding_trace.py:251-274. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T17:58:58+00:00: Generated citation repair: `test_the_persisted_worklist_carries_the_onboarding_items_in_its_one_list` repointed to mcp/tests/test_onboarding_trace_gate.py:725-747. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; a row citing `leaf.py` lines that MIK-R10 moved were re-pointed by the installed fixer or, where it declined, by the exact line shift over rows byte-identical to memory HEAD. No claim was reworded, so the fixer's bullets are kept. No verification stamp was advanced.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/src/agents_remember/application/knowledge_worklist/leaf.py`, moved by MIK-R11's changes, were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): created this card for the new file MIK-R30 adds, recording the architect rulings of 18:49:50 (2, 4) and 19:23:45 (N1, N2, N4). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
