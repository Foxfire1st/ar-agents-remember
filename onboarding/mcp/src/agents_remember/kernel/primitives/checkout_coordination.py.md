# mcp/src/agents_remember/kernel/primitives/checkout_coordination.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/primitives/checkout_coordination.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:28+02:00 |
| lastVerifiedCommitHash | `dc03c64a91947cee470622c560c516854eec86b5`|
| lastVerifiedCommitDate | 2026-08-30T17:41:53+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation source. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Runtime config asks this checkout policy before selecting the synthetic leaf configuration. | "checkout_coordination.checkout_cli_location()"; `_checkout_runtime_config` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:748-748; mcp/src/agents_remember/kernel/primitives/runtime_config.py:771-800 |
| Durable lock admission authorizes the target before entering the kernel; append and rewrite retain the same guard. | `exclusive_access`; `_prepare_append_target`; `_require_rewrite_access` | mcp/src/agents_remember/controlplane/durable_store.py:319-360; mcp/src/agents_remember/controlplane/durable_store.py:431-433; mcp/src/agents_remember/controlplane/durable_store.py:436-438 |
| MCP establishes trusted mode before `load_config`; pytest establishes explicit test mode before importing application services. | `main`; `begin_pytest_process` | mcp/src/agents_remember/mcp/server.py:77-99; mcp/test_support/agents_remember_test_support/testing/global_state.py:61-66 |


## Cross-Repo References

No separate cross-repository implementation dependency governs this policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-06T00:28+02:00 — Reopened the actual guarded durable-store entry points and recorded host registry ownership as a separate policy composition. No guard change or role declaration was made; preserved the unchanged source stamp.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: re-anchored citation range(s) to current source after the L16 line movement (cited files changed, card source unchanged); verification metadata unchanged.
- 2026-08-13T00:00+02:00 — 260731-EFA-L23 post-closeout worker-authority repair: added the explicit `lifecycle-operation` execution mode for the plane-owned detached task worker. It may use live coordination to claim/finalize its durable operation but receives no MCP/dashboard daemon writer role; ordinary checkout CLI isolation is unchanged. The owner reports 46 focused tests across the two affected suites, Ruff clean, and diff-check clean. Verification remains closeout-owned.
- 2026-08-12T22:24+02:00 — 260731-EFA-L23 async-closeout follow-up: added the exact enclosure `reports/` target for operational artifacts while keeping coordination rows confined to leaf-local `provider-runtime/dev-ar-coordination`; sibling/live escapes remain refused. Verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 citation maintenance: re-anchored the pytest process-declaration evidence after `conftest.py` line movement; the checkout-coordination claim is unchanged.
- 2026-08-10T19:57:55+02:00 — Closeout citation review: retained the three policy claims after
  re-reading the committed candidate and replaced ambiguous identifier anchors with exact,
  uniquely resolved call/signature anchors. Verification metadata remains pinned until closeout.

- 2026-08-10T18:31+02:00 — 260731-EFA-L21: created for checkout-local coordination isolation and central durable-write containment. Verification metadata remains blank until approved closeout commits the code.
