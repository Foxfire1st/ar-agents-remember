# mcp/tests/checkpoint_landing_test_support.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/tests/checkpoint_landing_test_support.py`              |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

The shared world builders for the checkpoint-landing boundary proof: one real temporary Git
master/leaf series topology — contracts, branches, code and memory commits, and ledger rows —
plus the small readers and mutations a landing case needs to aim itself at it.

**This module adds no behaviour, and it is the second half of one size-rail move.** Its builders
were the fixture half of `test_checkpoint_landing_end_to_end.py`; they were extracted verbatim so
that the case module keeps only its twenty cases, and the two modules that import them now do so
by name. It is declared as a `shared-support` artifact in `mcp/tests/evidence-lifecycle.toml`
(`:342-361`), owner `checkpoint-landing-test-port`, introduced by `260913-LCA-L12`, with the
`exact` consumer scope the three modules below define. No builder weakens a production authority:
every one drives the repository's own helpers or the registered public operation.

## Code Commentary

### Logic

`close_out_leaf` records a leaf closeout **from real commits** authored in the leaf's own two
worktrees, because the ordinary integrate route's entry gate requires a closed-out contract and
the ledger-divergence cases need a live leaf. `accumulate_master_line` authors the state a paused
master is actually in — code and memory content landed, the mapping in the master's ledger, the
super branch still behind — using the repository's own ledger helpers so the projection the
landing re-proves is the real one. Around those two, the module supplies the pieces a case
composes: `rev`, `memory_repository`, `payload_text`, `branch_checkout`, `commit_code`,
`commit_memory_content`, `commit_ledger_mapping`, `git_that_conflicts`, `advance_source_line`,
`absorb_source_into_master_line`, `rewrite_master_ledger`, `interleave_leaf_ledger`,
`write_divergent_ledger`, `hand_edit_ledger`, `hand_edit_ledger_in_place`, `closeout_messages`,
`checkpoint`, `ledger_at`, `ledger_mapping`, `master_status` and `set_master_status`.

`checkpoint` deliberately drives the **public** operation
(`worktree_tools.worktree_checkpoint_landing_tool` with `strategy="ff-only"`) rather than any inner
helper, which is what lets the case module assert the boundary instead of a seam.

### Conventions

One flat module of small builders, no classes and no fixtures of its own; a case composes what it
needs. Builders that must fail do so through `git_that_conflicts`/`git` rather than by fabricating
state, and every ledger the module writes is written with the production helpers.

### Invariants And Boundaries

- The world is real: temporary repositories, real branches, real commits, real ledger rows. No
  builder mocks a Git surface or synthesizes a ledger the projection could not have read.
- `checkpoint` and `close_out_leaf` reach production owners; a support module that re-implemented
  either would be a parallel implementation of the thing under test.
- The three consumers are the whole consumer set (`consumer_scope = "exact"` in the catalog):
  `test_checkpoint_landing_end_to_end.py`, `test_cross_master_concurrency.py` and
  `test_lifecycle_playthrough_end_to_end.py`. This module is **not** a test module itself, so it
  carries no `test-evidence-lanes.toml` lane row; its membership is accounted through its
  consumers' lane rows.
- Scenario-specific differences stay in the case module; a builder grows only when a second
  consumer needs the same step.

### Todos

None recorded beyond the catalog's own permanence rationale.

## Docs References

The configured Domain Documentation registry is empty for this memory root; no external
documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required for this repository-owned test world. | "def close_out_leaf(" | mcp/tests/checkpoint_landing_test_support.py:66-101 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two builders the boundary proof is built on: a leaf closed out from real commits, and one accumulated master line authored with the repository's own ledger helpers. | "def close_out_leaf("; "def accumulate_master_line(" | mcp/tests/checkpoint_landing_test_support.py:66-101; mcp/tests/checkpoint_landing_test_support.py:104-120 |
| The public checkpoint entry point the cases drive instead of an inner helper. | "def checkpoint(" | mcp/tests/checkpoint_landing_test_support.py:345-353 |
| The ledger-table readers and mutations: what one commit carries, what one leaf pair maps, and the in-place hand edit a divergence case needs. | "def ledger_at("; "def ledger_mapping("; "def hand_edit_ledger_in_place(" | mcp/tests/checkpoint_landing_test_support.py:356-359; mcp/tests/checkpoint_landing_test_support.py:362-368; mcp/tests/checkpoint_landing_test_support.py:324-336 |
| The declared artifact row that gives this module its `shared-support` identity, its owner, its three exact consumers and its replacement contract. | "path = \"mcp/tests/checkpoint_landing_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:343-343 |
| The case module this world was extracted from, which now imports the builders by name and keeps only its twenty cases. | "from checkpoint_landing_test_support import (" | mcp/tests/test_checkpoint_landing_end_to_end.py:50-71 |
| The two other consumers, which reuse the same builders rather than growing their own. | "from checkpoint_landing_test_support import ("; "from checkpoint_landing_test_support import close_out_leaf" | mcp/tests/test_cross_master_concurrency.py:68-73; mcp/tests/test_lifecycle_playthrough_end_to_end.py:44-44 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | "def checkpoint(" | mcp/tests/checkpoint_landing_test_support.py:345-353 |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator: created the one-to-one sidecar for this new
  shared-support module. It holds the checkpoint-landing world builders extracted from
  `test_checkpoint_landing_end_to_end.py`, and the card records that provenance plainly: the move
  exists to clear a duplicated fixture and a size rail, not to add behaviour, so nothing here
  changes what the cases prove. Records the catalog's declared facts — `shared-support`, owner
  `checkpoint-landing-test-port`, introduced by `260913-LCA-L12`, `exact` consumer scope — the
  three consumers and their import sites, and why this module carries no lane row of its own.
  Verification metadata remains closeout-owned; no verification stamp advanced and no acceptance
  claim is made.
