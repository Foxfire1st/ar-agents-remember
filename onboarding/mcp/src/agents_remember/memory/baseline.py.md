# mcp/src/agents_remember/memory/baseline.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory/baseline.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-13T23:52+02:00 |
| lastVerifiedCommitHash | `52875e7a8695fc7b67bff21ebb07a67268213967` |
| lastVerifiedCommitDate | 2026-09-14T00:06:58+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`baseline.py` is the package-local `c-10-adopt-memory-baseline` skill implementation for inspecting and
adopting an existing external-memory onboarding baseline. The memory commit it creates when adopting is
attributed: since 260913-LCA-L4 it carries the `Code-Commit:` trailer naming the code source-branch
commit the initial ledger row maps.

## Code Commentary

### Logic

The module exposes `BaselineRequest`, `baseline_status()`, and
`baseline_adopt()` as service entry points for MCP application entry points. The CLI
commands now adapt parsed arguments into that request shape, print the returned
payload, and return the service return code. The thin argparse-to-context
adapter is `resolve_baseline_context(args)` (renamed from the package-generic
`resolve_context`); it delegates to `resolve_request_context(request_from_args(args))`.
`resolve_request_context` passes the request's `topology` and `coordination_root` to the resolver
inside a `CoordinationHints(...)` (260731-EFA-L2) — the resolver no longer accepts
`requested_topology=` / `coordination_root=` as individual keywords. `code_repository_name`,
`workspace_root` and `code_repository_root` are still passed directly.

### Attribution At The Commit Seam (260913-LCA-L4)

Baseline adoption writes the first mapping a repository's memory has, and it takes a commit message
from nobody: its adopt subject is a hard-coded string built from the code repository's name. Before L4
that subject was the whole message, so the memory commit pair — the only memory commit a fresh baseline
has — carried no attribution and the projected ledger would simply have no first row.

In `adopt_initial_baseline` (`:169-232`) the code commit is now resolved **once** and used twice
(`:204-221`):

```python
code_source_commit = branch_commit(context.code_repository_root, source_branch)
require_git(context.memory_root, ["add", *existing_paths])
memory_content_commit = commit_if_dirty(
    context.memory_root,
    render_memory_content_message(
        f"[adopt-{context.code_repository_name}-memory-baseline] Adopt external memory content",
        code_source_commit,
    ),
)
ledger = create_initial_ledger(
    context.code_repository_name,
    code_source_commit,
    memory_content_commit,
)
```

Two independent resolutions of "the code source-branch commit" is exactly how a trailer and its ledger
row come to disagree, so hoisting it is the point rather than a tidy-up. The trailer is rendered by
`kernel.memory_attribution.render_memory_content_message` — the package's one writer, so this route does
not own a format — and it names `branch_commit(code_repository_root, source_branch)`, the same value
`create_initial_ledger` maps. The adoption still requires external topology, still blocks on actionable
drift unless it is explicitly accepted, and still refuses in the same places; only the memory-content
message gained the trailer.

The `memory.md`-only ledger commit (`:224`) is deliberately left unattributed: it names no code commit,
and a second trailered commit for one code commit would project a duplicate row.

### Invariants And Boundaries

- Adoption requires external topology.
- Actionable drift blocks adoption unless explicitly accepted.
- This module is invoked through typed MCP payloads, not through a coordinator
  runtime script path.
- MCP application entry points should call `baseline_status()` and `baseline_adopt()`
  directly rather than invoking `main(argv)` and parsing stdout.
- Baseline status imports drift classifiers from the `memory_quality.integrity`
  package; the old top-level `drift` package is no longer present.
- `baseline_adopt`'s `dry_run` defaults to `False` (act-by-default); `dry_run=true`
  previews the adoption plan without committing.
- The adopting memory commit is attributed to the code source-branch commit, and the initial ledger row
  maps that same resolved value — one resolution, so the trailer cannot disagree with the ledger. The
  attribution is rendered by `kernel.memory_attribution.render_memory_content_message`, never by a
  route-local format, and the `memory.md`-only ledger commit stays unattributed by rule.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `memory_baseline_status` and `memory_baseline_adopt` call this module. | `memory_baseline_status_tool`; `memory_baseline_adopt_tool` | mcp/src/agents_remember/application/memory_tools.py:353-361; mcp/src/agents_remember/application/memory_tools.py:363-379 |
| Ledger parsing and writing live in the kernel. | `load_ledger`; `write_ledger` | mcp/src/agents_remember/kernel/memory_ledger.py:202-205; mcp/src/agents_remember/kernel/memory_ledger.py:216-238 |
| The adopting memory commit is attributed to the code source-branch commit through the kernel's one renderer, and that same resolved value is what `create_initial_ledger` maps. | `render_memory_content_message`; `code_source_commit`; `create_initial_ledger` | mcp/src/agents_remember/memory/baseline.py:208-221; mcp/src/agents_remember/kernel/memory_attribution.py:72-97 |
| The end-to-end case that drives the public `memory_baseline_adopt` on a real disposable repository and asserts both documented git readers see the trailer, and that the ledger commit sees none. | `test_baseline_attributes_its_memory_content_commit_to_the_code_source_branch` | mcp/tests/test_memory_attribution_producers.py:289-345 |

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History
- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): baseline adoption became one of the five memory-content producers, and it was the
  one whose commit message is nobody's argument — its hard-coded adopt subject was the whole message, so
  a fresh baseline's only memory commit carried no attribution and the projected ledger had no first
  row. Recorded that the code source-branch commit is now resolved once (`:208`) and used twice — the
  renderer call (`:210-216`) and `create_initial_ledger` (`:217-221`) — that the trailer is rendered by
  `kernel.memory_attribution.render_memory_content_message` rather than by a route-local format, that the
  `memory.md`-only ledger commit (`:224`) stays unattributed by rule, and the public end-to-end case that
  proves both documented git readers see the trailer. Rebound the stale `memory_baseline_status_tool`
  range (353-360 → 353-361). Verification metadata remains closeout-owned; no acceptance claim and no
  verification stamp advanced.

- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `load_ledger`, `write_ledger` repointed to mcp/src/agents_remember/kernel/memory_ledger.py:202-205, mcp/src/agents_remember/kernel/memory_ledger.py:216-238. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: regenerated the memory-tool ranges
  via the scoped fixer; exact non-fixing check returns zero findings.

- 2026-08-02T20:43+02:00 — W2-B08: anchored 2 baseline reference claims and repointed the MCP call-site reference from the removed `application/skill_tools.py` to `application/memory_tools.py`; ranges remain generated by the scoped fixer. Verification metadata stays pinned until closeout.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2: call-site update for the resolver's new signature —
  `resolve_request_context` now wraps `topology`/`coordination_root` in a `CoordinationHints`.
  Behaviour unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-05-31T12:50+02:00 — Renamed the argparse adapter `resolve_context` to `resolve_baseline_context` in the source; noted the new name in Logic (behavior-preserving, thin delegate to `resolve_request_context(request_from_args(args))`) (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Typed drift rows as `list[drift.DriftRow]`, normalized `topology` to `Literal['internal','external'] | None` at the argparse boundary, and added a ledger-path guard in `baseline_adopt`; behavior-preserving (commit `0549b28`).
- 2026-05-24T02:47+02:00: Updated after drift imports moved under `memory_quality.integrity`.
- 2026-05-24T00:35+02:00: Updated after adding request/service entry points for MCP controllers.
- 2026-05-23T13:09+02:00: Copied into the MCP package and patched to package imports.
