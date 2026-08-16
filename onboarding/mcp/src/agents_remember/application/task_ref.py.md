# mcp/src/agents_remember/application/task_ref.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/application/task_ref.py`         |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-08-02T01:05+02:00                                    |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a`                |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview      | `overview.md`                                             |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `worktree_attach_tool` / `worktree_status_tool` take a `TaskRef` and resolve it through `_task_ref_namespace`. | `worktree_attach_tool`; `worktree_status_tool`; `_task_ref_namespace` | mcp/src/agents_remember/application/worktree_tools.py:258-267; mcp/src/agents_remember/application/worktree_tools.py:270-278; mcp/src/agents_remember/application/worktree_tools.py:281-294 |
| `resolve_context_tool` takes a `TaskRef`. | `resolve_context_tool` | mcp/src/agents_remember/application/coordination_tools.py:20-50 |
| The three tool declarations expose `TaskRef` arguments. | `resolve_context_tool`; `worktree_attach_tool`; `worktree_status_tool` | mcp/src/agents_remember/application/coordination_tools.py:24-59; mcp/src/agents_remember/application/worktree_tools.py:255-264; mcp/src/agents_remember/application/worktree_tools.py:267-275 |
| The locator packing is asserted against a live server. | `test_resolve_context_packs_the_locators_into_a_task_ref` | mcp/tests/test_mcp_registration_wiring_tests_1.py:65-90 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: corrected the shared-locator cardinality and
  separated dataclass scope from resolver/signature plumbing; duplicate source references were removed.

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 4 citation items; scoped citation check now passes.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the file. Introduced when the
  five-locator keyword list on `resolve_context_tool`, `worktree_attach_tool` and
  `worktree_status_tool` was replaced by one shared reference. Verification metadata pinned to the
  pre-change commit until closeout stamps the L2 code commit.
