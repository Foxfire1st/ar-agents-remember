# mcp/src/agents_remember/worktrees/modules/leaf_ref_start.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/worktrees/modules/leaf_ref_start.py` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-01T09:14+02:00                                      |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`                  |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[worktrees/modules overview](overview.md)

## Purpose

`leaf_ref_start.py` adapts the shared task-tree leaf-ref resolver to the `worktree_start` command result
surface. It keeps the policy out of `start.py` and gives start-contract construction a small helper for
canonical doc-id resolution.

## Code Commentary

`resolve_start_leaf_doc_id(context, args)` resolves `args.leaf_id or args.worktree_name` within the
current repository and requested task/parent-task scope, returning only the canonical task doc id for
contract persistence. `invalid_leaf_ref_result(error)` maps resolver failures to exit code 2 with
`state`, `summary`, `expected`, and `candidates` fields so callers get the expected
`<repo>/<master-folder>/<doc-id>` form and candidate set. Its `state` is
`error.status`, which since 260731-EFA-L4 is typed `leaf_refs.LeafRefStatus` — the same two-member
`Literal` `models.terminal` folds into its own status unions — rather than a bare `str`.

### The second refusal: `invalid_contract_request_result` (260731-EFA-L4)

`invalid_contract_request_result(error: ContractError)` is the sibling adapter for the *other* bad
start argument: a `workflow_kind` or `memory_mode` the persisted contract vocabulary does not hold.
Both arrive at the `worktree_start` MCP signature as free `str` and are narrowed by
`worktree_contract._task_vocabulary` before anything is written; that narrowing raises
`ContractError`, and nothing between here and the `@server.tool()` handler catches one. This maps it
to exit code 2 with just two fields:

```python
{"state": "invalid-request", "summary": f"worktree_start refused: {error}"}
```

There is no `expected` or `candidates` key — the legal set is already interpolated into the
`ContractError` message by `_task_vocabulary` (`f"workflow_kind must be one of
{sorted(VALID_WORKFLOW_KINDS)}"`), so `summary` carries it. The refusal is *returned*, not raised, so
a mistyped argument reads as a blocked start rather than a traceback.

The asymmetry with the contract READ path is deliberate and belongs to
`worktree_contract`: a contract *file* holding an unknown token degrades to the declared fallback and
is quarantined, while a *caller asking for* one is refused before it can be written down.

## Invariants And Boundaries

- This module is start-specific glue; the resolver owns matching, ambiguity, and candidate policy.
- The helper returns doc ids because worktree contracts persist doc ids, while terminal catalogs persist
  qualified ids.
- Both refusal builders return a `WorktreeCommandResult` rather than raising. `worktree_start`'s
  handler has no `except` for either `LeafRefResolutionError` or `ContractError`, so anything that
  escapes this module reaches the MCP client as a traceback.
- The three `state` values this module can emit — `leaf-ref-not-found`, `leaf-ref-ambiguous`,
  `invalid-request` — are all bad-argument refusals raised before any worktree, branch or contract
  write.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared resolver and `LeafRefResolutionError` payload facts, plus the `LeafRefStatus` alias `error.status` is typed as. | `LeafRefStatus`, `LeafRefResolutionError`, `resolve_leaf_ref` | mcp/src/agents_remember/worktrees/leaf_refs.py:30-30; mcp/src/agents_remember/worktrees/leaf_refs.py:45-72; mcp/src/agents_remember/worktrees/leaf_refs.py:94-147 |
| Start contract builder that calls these helpers. | `build_start_contract` | mcp/src/agents_remember/worktrees/modules/start_contract.py:187-206 |
| `ContractError`, `_task_vocabulary` and the six-cell vocabulary the second refusal reports on. | `ContractError`, `_task_vocabulary`, `ContractCells` | mcp/src/agents_remember/worktrees/worktree_contract.py:92-93; mcp/src/agents_remember/worktrees/worktree_contract.py:162-179; mcp/src/agents_remember/worktrees/worktree_contract.py:182-197 |

## Update History

- 2026-08-03T03:59:59+02:00 — Curated 6 citation findings (3 table rows, 3 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-08-01T09:14+02:00 — 260731-EFA-L4 curator: the card described only two functions; the module
  now has three. Documented `invalid_contract_request_result(error: ContractError)` — the refusal
  for a `workflow_kind`/`memory_mode` outside the contract vocabulary, emitting
  `{"state": "invalid-request", "summary": f"worktree_start refused: {error}"}` with no `expected`
  or `candidates` key because `_task_vocabulary` already interpolates the legal set into the
  message — and the new `from agents_remember.worktrees.worktree_contract import ContractError`
  that backs it. Also recorded that `invalid_leaf_ref_result`'s `state` is now the typed
  `LeafRefStatus` rather than a bare `str`, and added the invariants that both builders return
  rather than raise (the `worktree_start` handler catches neither error) and that all three emitted
  states are pre-write argument refusals. Added the `worktree_contract.py` reference row.
  Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: created as the worktree-start adapter for canonical leaf-ref
  resolution and refusal payloads. Verification metadata pinned until closeout stamps the
  260707-HFX-L4 commit.
