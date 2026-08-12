# mcp/tests/test_leaf_ref_resolution.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_leaf_ref_resolution.py`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-12T08:41+02:00 |
| lastVerifiedCommitHash | `df36127113619f4e85522eb615cc20c7eb637405` |
| lastVerifiedCommitDate | 2026-08-12T08:57:17+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tests overview](overview.md)

## Purpose

`test_leaf_ref_resolution.py` pins the shared task-tree leaf-ref resolver introduced by HFX-L4. It is
focused coverage for accepted canonical forms, legacy aliases, no-match reporting, ambiguity reporting,
start-scope task-root consistency, sibling JSON artifact handling, light-task candidate indexing, loud
marker-bearing malformed-doc handling, and HFX2-L8's boot-safety skip for malformed non-task JSON
artifacts. Since 260712-PTS-L1 it also pins the contract read/heal split: walk-free `load_contract`
(zero tasks-tree traversal, legacy ids returned verbatim) and the explicit `heal_contract_leaf_ids`
sweep (read-path-parity mapping, canonical-skip idempotence, dry-run, error tolerance, CLI seam).

## Code Commentary

The temp fixtures write real `TaskDocument` master and subtask JSON/Markdown pairs through
`write_task_doc`, then call `resolve_leaf_ref` directly. The tests prove:

- qualified refs, doc ids, and legacy slug/file stems normalize to one `repo/master/doc-id` identity;
- no-match errors use `leaf-ref-not-found`, include `<repo>/<master-folder>/<doc-id>`, and list a nearby
  candidate;
- ambiguous legacy slugs use `leaf-ref-ambiguous` and list both candidate qualified ids;
- a fully qualified ref outside the caller's requested `task_name` is rejected instead of being attached
  to the wrong start contract;
- a missing optional master `task.json` is skipped, malformed non-task sibling JSON is ignored for boot
  safety, while a malformed schema-marked leaf JSON file raises;
- standalone/light `task.json` docs resolve from their doc id, slug/folder, and enclosure aliases.
- repository inference accepts exactly one active task-directory child while ignoring files and
  the archive directory; zero or multiple active repository directories remain ambiguous.

The 260712-PTS-L1 read/heal-split tests build on a shared `_persisted_legacy_contract` fixture (a leaf
contract persisted with a legacy stem-shaped id — the pre-heal on-disk state) and prove:

- `load_contract` returns a legacy `leaf_id` verbatim — the read path never heals (R1/R5);
- `load_contract` performs ZERO tree traversal (R6a): every walk entry point the old normalization
  dragged in is patched to fail loud — `resolve_leaf_ref`, `resolve_active_task_root`, the
  series-contract iterators, and `Path.glob`/`rglob`/`iterdir` themselves — so any regression that
  re-adds a tasks-tree walk to the read path trips immediately;
- `heal_contract_leaf_ids` maps a legacy stem id exactly like the removed read-time normalization
  (R6b), including still ignoring sibling artifact JSON on the heal walk;
- the heal is idempotent and skips canonical contracts without resolution (R6c): a second sweep
  rewrites nothing and `resolve_leaf_ref` is patched to assert the canonical skip is walk-free;
- an unprovable legacy id survives the heal unchanged with an empty error report;
- `dry_run=True` reports the would-be rewrite without touching the file;
- an unreadable/torn contract lands in `errors` while the sweep continues healing the rest;
- the `heal-leaf-ids` CLI subcommand (R3) is the on-demand seam: `main([...])` returns 0, prints the
  JSON report, and the contract is healed on disk.

## Invariants And Boundaries

- The tests cover resolver policy, not terminal catalog mutation or worktree start side effects.
- Fixtures use real task-doc writes so candidate aliases match production task-tree shape.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Resolver under test. | `resolve_leaf_ref` | mcp/src/agents_remember/worktrees/leaf_refs.py:88-141 |
| Walk-free `load_contract` and the `heal_contract_leaf_ids` sweep under test. | `load_contract`; `heal_contract_leaf_ids` | mcp/src/agents_remember/worktrees/worktree_contract.py:438-471; mcp/src/agents_remember/worktrees/worktree_contract.py:480-555 |
| The `heal-leaf-ids` CLI seam driven end to end via `main`. | `main` | mcp/src/agents_remember/worktrees/modules/cli.py:159-166 |
| Task document writer used to create representative task trees. | `write_task_doc` | mcp/src/agents_remember/tasks/store.py:36-37 |

## Update History

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 added direct empty/single/multiple repository-inference coverage, including file and archive exclusions, clearing `_single_repo_name` CRAP without changing production behavior.
- 2026-08-04T18:51+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the three malformed rows whose
  links pointed at `.md` cards or an overview instead of code — `resolve_leaf_ref` (leaf_refs.py:
  94-149), `load_contract` + `heal_contract_leaf_ids` (worktree_contract.py:438-473; 480-557), and
  `write_task_doc` (tasks/store.py:36-38, replacing the tasks overview link). Claim wording
  unchanged.
- 2026-07-31T16:50+02:00 — No content impact: the two `default_contract(...)` fixtures — the shared
  `_persisted_legacy_contract` helper and the duplicate-slug case — now build the same contract
  from the `ContractTask`, `LeafIdentity`, and `RepoBranchPlan` parameter objects instead of eleven
  loose keywords, with the imports widened to match. This card describes those fixtures by what
  they persist (a leaf contract carrying a legacy stem-shaped `leaf_id`) and never named the
  `default_contract` keywords, so nothing it claims moved. Re-read the file for case changes:
  no test was added, removed, or renamed, so the canonical/alias resolution pins, the
  `leaf-ref-not-found` and `leaf-ref-ambiguous` reporting, the zero-traversal tripwire, the
  heal-parity and idempotence cases, and the `heal-leaf-ids` CLI seam all still match the source.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1: replaced the two read-time-normalization contract tests with
  the read/heal-split suite — legacy ids come back verbatim from `load_contract`, a loud zero-traversal
  tripwire guards the walk-free read path, and `heal_contract_leaf_ids` is pinned for read-path parity,
  canonical-skip idempotence, dry-run reporting, torn-contract tolerance, and the `heal-leaf-ids` CLI
  seam. Verification metadata pinned until closeout stamps the 260712-PTS-L1 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (minimal projection robustness): added a regression for
  malformed sibling JSON without the task-document schema marker being ignored, while schema-marked
  malformed task docs still fail loud. Verification metadata pinned until closeout stamps the
  260707-HFX2-L8 commit.
- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2: added regressions for schema-marked malformed task docs,
  non-task sibling JSON artifacts, live-style contract loading with sibling artifact JSON, unproven
  read-path contract mapping, and standalone/light task-doc candidate aliases. Verification metadata
  pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: created focused resolver coverage for canonical leaf-ref
  validation, normalization, candidate errors, task-scope mismatch refusal, missing optional master docs,
  and malformed-doc loud failures. Verification metadata pinned until closeout stamps the 260707-HFX-L4
  commit.
