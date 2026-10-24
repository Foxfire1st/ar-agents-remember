# mcp/tests/test_l192_safety_stop_authority_settings.py

## Current operative account — MIK-R199

- The docstring states the rule and the defect it measures: live periodic safety — sample, record, degradation, stop — stays, and empty or revoked launch settings never authorize suppressing safety. The safety tick's stop had been built from `lifecycle_settings_from_config()`, which by design emits no providers, so the stop selected nothing whatever the sample found. The ruling it cites puts the stop on the user's authority settings through the same reader and shape the install's old-watcher stop uses: stop only, no new reader, no new key, generated documents still empty.
- `_authority_settings(root, *, legacy_entry)` writes a real authority document into `.codex/mcp/settings.json` — version, coordination root, workspace root, a repository entry, an empty `providers` block and a `providerDegradation` block with degrade and critical ratios — and returns `load_config(path)` with the path. When `legacy_entry` is set it adds a `contextProviders` block enabling `grepai-memory`. Its docstring records why that is not an invented authority: reading the legacy block for a stop grants none of the install/prepare/seed/start/query/watch authority the block governs, and no new key is introduced.
- `_critical_samples` writes samples into the metrics store at the authority document's coordination root, each carrying a grepai container sample above the document's critical memory ratio, so the transition is reached against ratios the authority document itself declares rather than a threshold patched into the test.
- `_RecordStop` is a context manager that swaps `watchers.grepai_run` for a handler recording the action it was called with and returning an ok provider result, restoring the original on exit. The observable under test is therefore whether the stop handler ran at all, not whether containers moved.
- `_run_tick` calls `evaluate_provider_degradation` with `stop_provider_stacks=partial(run_configured_watchers, action="stop", dry_run=True)` — the stop is supplied by the caller, matching the production signature in which the stopper has no default, and the call goes through the same watcher service the other stop routes use.
- The first case is the positive: with the legacy authority entry and a critical sample, the result state is `critical`, the recorded actions equal the grepai stop action taken from `watchers.WATCHER_PROVIDER_ACTIONS["grepai"]["stop"]`, the failsafe event reports `enabled` true, and the selected providers in that event's result are exactly `["grepai"]`. The docstring notes this is the case that fails before the amendment, where the tick's stop wrote an empty generated document and nothing was recorded although the authority settings enabled a provider.
- The second case is the control: with the same sample and no authority entry, the state is still `critical`, the failsafe is still enabled, no stop handler ran, and the event's result carries an empty provider list — the stop selects none and reports nothing new.

### Source and authority bounds

- Source inspection: `mcp/tests/test_l192_safety_stop_authority_settings.py:1-14`.
- Source inspection: `mcp/tests/test_l192_safety_stop_authority_settings.py:37-67`.
- Source inspection: `mcp/tests/test_l192_safety_stop_authority_settings.py:70-93`.
- Source inspection: `mcp/tests/test_l192_safety_stop_authority_settings.py:96-119`.
- Source inspection: `mcp/tests/test_l192_safety_stop_authority_settings.py:122-142`.
- Source inspection: `mcp/tests/test_l192_safety_stop_authority_settings.py:145-158`.

The detector and watcher service this file drives live outside it; the card states the fixture shape and what the file asserts of them.

## Evidence

- The document under test is a user authority settings file, and its legacy provider block is read for a stop without granting the authority that block governs. [1]
- Degradation samples are written above the critical ratio the authority document itself declares. [2]
- The stop handler is patched and restored, so the recorded action is the observable rather than container state. [3]
- The tick is driven with the watcher service's own stop as its injected stopper. [4]
- With a legacy authority entry and a critical sample, the safety stop selects that provider and the failsafe event names it. [5]
- With no authority entry, a critical sample still fires the failsafe but no stop handler runs and no provider is reported. [6]
