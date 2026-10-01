# mcp/src/agents_remember/kernel/primitives/checkout_coordination.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

Own the one fail-closed policy that distinguishes trusted MCP/dashboard execution,
the plane-owned lifecycle-operation worker, explicit pytest execution, unpublished
linked-worktree CLI execution, and refused primary-checkout CLI execution. It derives
the checkout from the imported package
path rather than `cwd` or caller-provided environment, so a one-shot command cannot
select the deployed coordinator merely by changing directory or passing live settings.

## Code Commentary

### Logic

`resolve_checkout_location(source_path)` walks ancestors of the loaded package and
accepts only an Agents Remember repository shape. A `.git` file means a linked
worktree; a `.git` directory means the primary checkout. For a linked checkout,
`CheckoutLocation.coordination_root` is exactly
`<checkout-parent>/provider-runtime/dev-ar-coordination` and
`synthetic_config_path` is its non-authoritative sibling marker.
`CheckoutLocation.reports_root` is the enclosure's exact sibling `reports/`
directory: operational and test artifacts live there, outside coordination
authority state.

`declare_execution_mode` owns the process-singleton mode (`mcp`, `dashboard`,
`lifecycle-operation`, or `test`). `declare_lifecycle_operation_process` is the
narrow declaration for the detached task worker: it admits live coordination authority
needed to claim its durable operation and finalize the task edge without assigning the
long-lived `mcp` or `dashboard` daemon writer role. `checkout_cli_location` returns no special context for one of those declared
modes or for an installed wheel. An undeclared linked checkout receives its leaf
location; an undeclared primary checkout raises `CheckoutCoordinationError` because it
has no disposable leaf enclosure.

`require_durable_write_target` resolves the candidate and permits exactly two
task-local descendants: the disposable coordination root for inbox/gate/lifecycle
rows, and the enclosure `reports/` root for operational artifacts. Everything else
is refused. The exception text names those responsibilities separately rather than
calling report files coordination rows. `exclusive_access`, `append_line`, and
`rewrite_lines` call the guard, so an escape fails before parent or lockfile creation
and a manual runtime-config construction cannot bypass the normal synthetic config
route. This is not a second coordinator or a live-state fallback: no coordination
authority is copied into or resolved from `reports/`.

The host Dagger registry is a separate resource owner. Its lock mechanics use `kernel.file_lock` directly and its admission policy lives in `AuthorityRegistry`; this checkout policy does not gain a host-registry path exception or a fabricated trusted execution mode.

### Conventions

Resolve the imported package location and actual execution declaration; caller cwd and ambient role-like values are not authority.

### Invariants And Boundaries

- Detection follows the imported package checkout, never `cwd`, a CLI flag, or an
  environment override.
- The dummy root is created lazily by the operation that needs it; no live state is
  copied and the provider-runtime teardown already owns its enclosing directory.
- Enclosure reports are the only non-coordination durable target allowed to
  unpublished checkout code. They remain self-overwriting task artifacts and do not
  contain inbox, gate, lifecycle, or observer authority rows.
- Trusted daemon declaration precedes authority loading. Pytest declares `test`
  explicitly in `conftest.py`; it is not inferred from process names or environment.
- Only the detached plane-owned lifecycle worker declares `lifecycle-operation`.
  The mode does not claim MCP/dashboard daemon ownership and is not a general checkout
  CLI escape hatch.
- This protects supported Agents Remember paths from accidental writes. Arbitrary
  hostile Python or shell filesystem access remains outside an in-process policy.

### Todos

None identified in this bounded containment review.

## Evidence

### Docs References

No external Domain Documentation source is configured.

No configured domain documentation source.

### Repo-Internal References

- Runtime config asks this checkout policy before selecting the synthetic leaf configuration. [1]
- Durable lock admission authorizes the target before entering the kernel; append and rewrite retain the same guard. [2]
- MCP establishes trusted mode before `load_config`; pytest establishes explicit test mode before importing application services. [3]


### Cross-Repo References

No separate cross-repository implementation dependency governs this policy.

No cross-repository evidence is required.
