# mcp/src/agents_remember/controllers/task_ref.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/controllers/task_ref.py`         |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-07-31T15:31+02:00                                    |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                             |

## Governing Overview

[controllers route overview](overview.md)

## Purpose

One frozen dataclass, `TaskRef`: **how an MCP caller points at one existing task.** Every read-side
task tool — `worktree_attach`, `worktree_status`, `resolve_context` — takes the same bundle of
identifiers and hands it to the same resolver, so the bundle is named once instead of being spelled
out five arguments at a time in four places.

## Code Commentary

### Logic

```python
@dataclass(frozen=True)
class TaskRef:
    repo_id: str
    task_name: str | None = None
    contract_path: str | None = None
    leaf_id: str | None = None
    parent_task: str | None = None
```

`repo_id` is required — a task always belongs to a repo. The rest are locators, and a caller
supplies **whichever one it happens to hold**: the task name, the on-disk contract path, or the leaf
id (optionally with its parent task, for a nested task tree).

The docstring is explicit about what this type deliberately does not own: resolution order and
precedence between the locators belong to the worktree resolver, not to this reference. `TaskRef`
only carries what the caller knows. That is why it has no validation, no "exactly one of" rule and
no methods — adding any would move a resolver decision into a value object that three different
tools share.

### Invariants And Boundaries

- Frozen and behaviourless. Keep resolution logic in `controllers/worktree_tools.py` /
  `git_worktree_manager`.
- This is a controller-boundary type. The MCP tool declarations in `mcp/registration/` keep their
  locators **flat** in the published signature and construct a `TaskRef` in the body — typing a tool
  parameter as `TaskRef` would republish the tool as a nested object and break every client.
- Adding a field here widens three tools at once; that is the point, but it is also the cost.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `worktree_attach_tool` / `worktree_status_tool` take a `TaskRef` and resolve it through `_task_ref_namespace`. | [worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py) |
| `resolve_context_tool` takes a `TaskRef`. | [coordination_tools.py](agents-remember/mcp/src/agents_remember/controllers/coordination_tools.py) |
| The three tool declarations that build one from flat MCP arguments. | [registration overview](../mcp/registration/overview.md) |
| The locator packing is asserted against a live server. | [test_mcp_registration_wiring.py](agents-remember/mcp/tests/test_mcp_registration_wiring.py) |

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the file. Introduced when the
  five-locator keyword list on `resolve_context_tool`, `worktree_attach_tool` and
  `worktree_status_tool` was replaced by one shared reference. Verification metadata pinned to the
  pre-change commit until closeout stamps the L2 code commit.
