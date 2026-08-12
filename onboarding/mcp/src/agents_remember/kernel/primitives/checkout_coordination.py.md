# mcp/src/agents_remember/kernel/primitives/checkout_coordination.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/primitives/checkout_coordination.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T08:41+02:00 |
| lastVerifiedCommitHash |  `df36127113619f4e85522eb615cc20c7eb637405`|
| lastVerifiedCommitDate |  2026-08-12T08:57:17+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

Own the one fail-closed policy that distinguishes trusted MCP/dashboard execution,
explicit pytest execution, unpublished linked-worktree CLI execution, and refused
primary-checkout CLI execution. It derives the checkout from the imported package
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

`declare_execution_mode` owns the process-singleton mode (`mcp`, `dashboard`, or
`test`). `checkout_cli_location` returns no special context for one of those declared
modes or for an installed wheel. An undeclared linked checkout receives its leaf
location; an undeclared primary checkout raises `CheckoutCoordinationError` because it
has no disposable leaf enclosure.

`require_durable_write_target` resolves both the candidate target and the leaf-local
root, then refuses a target outside that root. `exclusive_access`, `append_line`, and
`rewrite_lines` call it, so an escape fails before parent or lockfile creation and a
manual runtime-config construction cannot bypass the normal synthetic config route.

### Invariants And Boundaries

- Detection follows the imported package checkout, never `cwd`, a CLI flag, or an
  environment override.
- The dummy root is created lazily by the operation that needs it; no live state is
  copied and the provider-runtime teardown already owns its enclosing directory.
- Trusted daemon declaration precedes authority loading. Pytest declares `test`
  explicitly in `conftest.py`; it is not inferred from process names or environment.
- This protects supported Agents Remember paths from accidental writes. Arbitrary
  hostile Python or shell filesystem access remains outside an in-process policy.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Runtime config selects the synthetic leaf config before reading the supplied authority file. | `checkout_cli_location`; `_checkout_runtime_config` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:149-157; mcp/src/agents_remember/kernel/primitives/runtime_config.py:653-706 |
| Durable-store lock, append, and rewrite paths all enforce this target policy. | "path = _checked_lock_path_for(log_path)"; "def _prepare_append_target(log_path: Path) -> None:"; "def _require_rewrite_access(log_path: Path, store: str) -> None:" | mcp/src/agents_remember/controlplane/durable_store.py:427-427; mcp/src/agents_remember/controlplane/durable_store.py:506-506; mcp/src/agents_remember/controlplane/durable_store.py:511-511 |
| MCP establishes trusted mode before `load_config`; pytest establishes explicit test mode before importing application services. | "server_startup.declare_mcp_process()"; "declare_test_process()" | mcp/src/agents_remember/mcp/server.py:60-65; mcp/tests/conftest.py:37-40 |

## Update History

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 citation maintenance: re-anchored the pytest process-declaration evidence after `conftest.py` line movement; the checkout-coordination claim is unchanged.
- 2026-08-10T19:57:55+02:00 — Closeout citation review: retained the three policy claims after
  re-reading the committed candidate and replaced ambiguous identifier anchors with exact,
  uniquely resolved call/signature anchors. Verification metadata remains pinned until closeout.

- 2026-08-10T18:31+02:00 — 260731-EFA-L21: created for checkout-local coordination isolation and central durable-write containment. Verification metadata remains blank until approved closeout commits the code.
