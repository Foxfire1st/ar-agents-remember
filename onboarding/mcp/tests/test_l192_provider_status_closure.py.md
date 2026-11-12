# mcp/tests/test_l192_provider_status_closure.py

## Current operative account — MIK-R199

- The module docstring fixes the subject and its residue: the detailed provider-status / start-only closure is gone, and the same file asserts what that removal must not take with it — legacy settings reporting, the stop/cleanup route, the settings writer and the independent metrics/degradation surface. It also records the shape the negative assertions are written against: the summary used to take `include_providers`/`detail_limit`/`target_repo_id` and reach a live watcher status read.
- `test_the_detailed_status_closure_is_not_reachable_from_the_surviving_entry_point` derives its expectation from the shipped signature instead of a literal list: `inspect.signature(provider_status.provider_summary_packet)` must name exactly `config`, a fixed tuple of former helpers (`_watchers_status`, `_provider_summary_items`, `_provider_summary_item`, `_provider_recovery_actions`, `_provider_indexing_targets`, `ProviderStatusProjection`) must be absent from the module, and `include_providers` must not occur in its source at all.
- The summary that survives is pinned as a non-reporting projection. A runtime whose provider map holds a provider key still reports `configured` and `enabled` true with `state` `skipped`, empty `items`, `indexing` and `recoveryActions`, and no `ok` key — the case's own reason is that a skipped summary states no health it did not read. A runtime with an empty provider map reports `configured` and `enabled` false and the same `skipped` state.
- `test_no_surviving_action_asks_a_watcher_to_start_or_report_status` holds the action vocabulary rather than the call sites: the admitted watcher-service actions are exactly `stop` and `shutdown-all`, each provider's entry in `watcher_lifecycle.WATCHER_PROVIDER_ACTIONS` admits only those, `run_watchers_lifecycle` raises `ValueError` matching "unsupported watcher service action" for `start` and for `status`, and a fixed tuple of former status/start symbols (`watcher_cgc_status_results`, `watcher_cgc_backend_status`, `cgc_start_all`, `cgc_status`, `cgc_backend_status`, `cgc_all_layouts_from_settings`) is absent from `providers.lifecycle.watchers`.
- `test_the_retained_stop_settings_and_safety_callers_are_still_present` asserts that the CLI module's `run_configured_watchers`, `write_lifecycle_settings`, and `providers.metrics`' `ProviderMetricsStore` and `sample_provider_containers` are still there, under a comment naming them as the stop/cleanup route, the legacy-key settings writer and the independent safety surface.
- The closing case asserts the status-only projection module is not importable at all (`importlib.util.find_spec` returns `None`), that the CLI watcher entry point carries no `__wrapped__`, then drives a dry-run `stop` against the generated settings path inside a temporary coordination root and requires `provider` `watchers`, `action` `stop`, `ok` true and an empty `results`, with the comment that the generated settings declare no provider to stop. The cgc runner image build and status callables are asserted callable in the same case, so the image's layout ownership is not collateral.

### Source and authority bounds

- Source inspection: `mcp/tests/test_l192_provider_status_closure.py:1-15`.
- Source inspection: `mcp/tests/test_l192_provider_status_closure.py:43-57`.
- Source inspection: `mcp/tests/test_l192_provider_status_closure.py:60-81`.
- Source inspection: `mcp/tests/test_l192_provider_status_closure.py:84-90`.
- Source inspection: `mcp/tests/test_l192_provider_status_closure.py:93-127`.
- Source inspection: `mcp/tests/test_l192_provider_status_closure.py:130-165`.

The claims above are what the file asserts and the modules it names; the file carries no result of its own.

## Evidence

- The surviving summary's parameter list is read from the live signature and required to be `config` alone. [1]
- The former detail helpers and `include_providers` are required absent from `agents_remember.providers.status`. [2]
- A configured key still reports configured but as a skipped projection that states no health and no `ok`. [3]
- The stop/cleanup route, the settings writer and the metrics store are asserted present rather than assumed. [4]
- The watcher service admits only stop/shutdown-all and refuses `start` and `status` with `ValueError`. [5]
- The status-only projection module is required unimportable while the stop route and the cgc image owner survive. [6]
