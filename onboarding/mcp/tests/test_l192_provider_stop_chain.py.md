# mcp/tests/test_l192_provider_stop_chain.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin which settings document each provider-stop route selects, so a claim that the metrics tick
stops a leftover provider stack can be judged from code rather than from the tick's name.

## Code Commentary

The stop chain has two entry points. The dashboard metrics loop calls
`providers.watcher_service.run_configured_watchers`, which reads the user's authority settings
first (`config.config_path`) and generates a settings document only when no authority file
exists, passing whichever it selected as `--from-settings`. The install route
(`install.provider_watchers.stop_provider_watchers_before_refresh` →
`run_provider_watcher_lifecycle`) serialises `rebind.settings`, which `install.runtime` fills from
`scope.provider_deps.settings`. The cases hold both selections to their source: the generated
document disables `contextProviders` and enables neither retired id, the legacy map still reads an
enabled provider, a stop against the generated document selects no provider, and an install stop
hands the watcher service the authority document instead of the generated one. Two cases then
check which handler is reached: an enabling document reaches the grepai stop action exactly once,
and the generated document reaches none. Every case runs with `dry_run` true and patched
dispatchers, so no container is started.

## Evidence

- The generated lifecycle document carries no enabled context provider.
  `test_generated_lifecycle_settings_disable_context_providers`,
  `test_provider_enabled_disables_retired_ids_on_generated_document`
- A stop against the generated document selects no provider; the install route carries the
  authority settings instead.
  `test_watchers_stop_selects_no_provider_from_generated_settings`,
  `test_install_stop_route_carries_authority_settings_not_generated_document`
- Only an enabling document reaches a stop handler.
  `test_an_enabling_document_invokes_the_real_stop_handler`,
  `test_the_generated_document_invokes_no_stop_handler`
