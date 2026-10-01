# mcp/src/agents_remember/application/task_docs/task_ref.py

## Governing Overview

[application layer route overview](overview.md)

## Purpose

One frozen dataclass, `TaskRef`: **how an MCP caller points at one existing task.** Three read-side
application entry points — `worktree_attach`, `worktree_status`, and `resolve_context` — share this
locator shape. The dataclass names the bundle once; it does not itself decide resolver precedence or
automatically widen the published MCP signatures.

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

- Frozen and behaviourless. Keep resolution logic in `application/worktree_tools.py` /
  `git_worktree_manager`.
- This is an application-boundary type. The MCP tool declarations in `mcp/registration/` keep their
  locators **flat** in the published signature and construct a `TaskRef` in the body — typing a tool
  parameter as `TaskRef` would republish the tool as a nested object and break every client.
- Adding a field here widens three tools at once; that is the point, but it is also the cost.

## Evidence

### Repo-Internal References

- Attach consumes the supplied TaskRef. [1]
- Status consumes the supplied TaskRef. [2]
- The facade projects TaskRef locators into the resolver namespace. [3]
- `resolve_context_tool` takes a `TaskRef`. [4]
- Context resolution accepts the common task locators. [5]
- Attach accepts the common task reference. [6]
- Status accepts the common task reference. [7]
- The frozen task reference carries repo and optional task/contract/leaf/parent locators; precedence remains resolver-owned. [8]
