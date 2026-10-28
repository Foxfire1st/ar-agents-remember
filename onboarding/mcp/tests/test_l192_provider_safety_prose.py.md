# mcp/tests/test_l192_provider_safety_prose.py

## Current operative account — MIK-R199

- The module docstring states the defect the file is written against: a document that says the periodic tick stops a leftover provider stack is wrong, because the tick calls `run_configured_watchers`, which builds the generated lifecycle settings, and that document declares no providers — so `provider_enabled` answers False for each retired id and `watcher_provider_results` calls no provider stop handler. The install-time route reads the authority settings document instead, which still parses legacy provider keys.
- The expected prose is derived from the modules the loop runs rather than from literals the author could drift away from: `CADENCE` is rendered from `metrics.DEFAULT_SAMPLE_INTERVAL_SECONDS`, the loop's stages are matched by word stems (`sampl`, `record`, `evaluat`, `stop`, `compact`) so a tense change in prose is not a failure, and a tuple of continuity markers names the acceptable ways to say the loop is not scoped to an install or a cleanup. The documents under test are `docs/reference/settings-json.md` and `docs/reference/runtime-layout.md`.
- Paragraph handling is explicit: `_paragraphs` splits on blank lines and flattens whitespace; `_loop_paragraphs` keeps only paragraphs that carry both the cadence and `failsafeenabled`; `_loop_paragraph` requires the loop to be stated in a single paragraph per document and reports the missing case in terms of the lifespan's `_metrics_loop`. `_store_home` derives the observer home from `ProviderDegradationStore` and `ProviderMetricsStore` against the same root, asserts they agree, and returns that home relative to the coordination root, so the prose must name the path the stores actually write.
- `test_the_retained_loop_is_still_the_independent_stop_caller` is the source half: `_metrics_loop`'s own source must still sample (`sample_provider_containers`), record (`metrics_store.record`), evaluate (`evaluate_provider_degradation`), compact (`metrics_store.compact`) and sleep on `asyncio.sleep(DEFAULT_SAMPLE_INTERVAL_SECONDS)`; the stop must be supplied by that loop through `run_configured_watchers` with `action="stop"`; `stop_provider_stacks` must have no default in `evaluate_provider_degradation`; the detector must read `settings.fail_safe_enabled` and call `_run_critical_failsafe`; and `_serving_lifespan` must create the metrics task unconditionally, so the prose cannot be made true by switching the loop off.
- `test_failsafe_key_is_the_documented_gate` binds the documented key to the field: the parsed default of `fail_safe_enabled` is true and `parse_provider_degradation_settings` follows `failSafeEnabled` true and false.
- `test_the_document_states_the_periodic_sample_degrade_stop_loop` is parametrised per document with the stages that document must describe, and requires the gate key, the derived cadence, the derived store home, a continuity marker, and the phrases "not a revival" and "starts nothing"; the settings reference additionally has to name the metrics store's log file name.
- `test_the_stop_reads_the_authority_settings_not_the_generated_document` binds the amendment to the code: `run_configured_watchers`' source must contain `config.config_path`, an `is_file()` check and the `write_lifecycle_settings()` fallback. It then shows the asymmetry the tests rely on — the generated document reports `contextProviders.enabled` false with no providers, and `provider_enabled` is false for `grepai-memory` and `codegraphcontext-code`, while a legacy document naming an enabled `grepai-memory` answers true, and `watcher_provider_results` with a bare namespace and action `stop` returns an empty list.
- `test_the_install_route_reads_the_authority_document_not_the_generated_one` binds the contrast to the install modules: `stop_provider_watchers_before_refresh` asks for `action="stop"`, `run_provider_watcher_lifecycle` writes `write_temp_provider_settings(rebind.settings)`, `ProviderWatcherRebind` still carries a `settings` field, and the install runtime takes that document from `scope.provider_deps.settings`.
- `test_each_document_states_which_document_each_stop_reader_can_select_from` requires both documents to carry the consequence and not only the callback: the generated document shown as `"enabled": false, "providers": {}`, the statement that it declares no provider, one of the phrases "selects nothing" or "selects no provider", the words "generated" and "not what a stop reads" kept apart, the authority settings file and `contextProviders` named as what the install-time stop reads instead, `runtime_install` and `providers-remove` still named as routes, and the cadence and `failsafeenabled` still present.

### Source and authority bounds

- Source inspection: `mcp/tests/test_l192_provider_safety_prose.py:1-18`.
- Source inspection: `mcp/tests/test_l192_provider_safety_prose.py:42-74`.
- Source inspection: `mcp/tests/test_l192_provider_safety_prose.py:77-112`.
- Source inspection: `mcp/tests/test_l192_provider_safety_prose.py:115-147`.
- Source inspection: `mcp/tests/test_l192_provider_safety_prose.py:150-157`.
- Source inspection: `mcp/tests/test_l192_provider_safety_prose.py:160-202`.
- Source inspection: `mcp/tests/test_l192_provider_safety_prose.py:205-233`.
- Source inspection: `mcp/tests/test_l192_provider_safety_prose.py:236-249`.
- Source inspection: `mcp/tests/test_l192_provider_safety_prose.py:252-283`.

The document text this file constrains lives outside it; the card states what the file requires of that text, not what the text says.

## Evidence

- The prose tests are written against the chain, not the callback: the tick's generated settings declare no provider while the install route reads the authority document. [1]
- The expected cadence and stage vocabulary are derived from the metrics module and matched by stems. [2]
- Each document must state the loop in a single paragraph carrying the cadence and the failsafe gate. [3]
- The observer home the prose must name is read from the degradation and metrics stores, which are required to agree. [4]
- The safety loop is required to sample, record, evaluate, compact, sleep on the default interval and supply its own stop, with an unconditional start and a non-defaulted stopper. 
- The documented `failSafeEnabled` key is bound to `fail_safe_enabled`. [6]
- The stop's settings source is bound to the authority path with the generated document as fallback, and the generated document is shown to select no provider. [7]
- Both documents must state which settings document each stop reader can select from and keep naming the install and cleanup routes. [8]

- Retired at the fifth freeze d59c3493: mcp/tests/test_l192_provider_safety_prose.py::test_the_retained_loop_is_still_the_independent_stop_caller - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
