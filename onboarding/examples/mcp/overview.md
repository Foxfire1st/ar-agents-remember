# examples/mcp Overview

| Field | Value |
| --- | --- |
| sourceRoute | `examples/mcp` |

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

`examples/mcp/` holds the public MCP authority-settings template, `settings.example.json`, and a coding-guidelines example that teams can adapt for a memory repository. The authority template is separate from a memory layer's `system/settings.json`; the guidelines are documentation-shaped example content, not an automatically selected runtime input.

## Hot Path Summary

Start with the JSON configuration example for the repository/profile and runtime settings shape; read the guideline example for source/application ownership. The configured runtime owns parsing and admission, so these illustrative files do not themselves confer execution or lifecycle authority.

## How It Is Built

### Authority settings

The JSON template names one coordination root, one workspace root and the transcript-log root, then declares repository and provider IDs. The `agents-remember` repository entry selects `mcp/certification-profile-v1.json` beside a null `contractPath`; it is a reference to the checked-in profile, not another executor. Configured repository roots derive from `workspaceRoot/<repo-id>`, and external memory derives from `coordinationRoot/memory-repos/ar-<repo-id>`.

The provider entries are empty per-provider settings objects, not an empty providers map. The parser derives the supported providers' runtime and log locations and instance identity; callers do not insert container/data-root/watch configuration into those objects. The retained template and parser vocabulary do not by themselves promise that any provider setup, watcher or backend tool is an available active operation.

`benchmarksEnabled` is false. Dashboard supervision is opt-in in the template (`autoStart: false`, `port: 8765`). Timeout caps use `toolSeconds` and `providerSetupSeconds`; the old `providerSeconds` spelling is refused. The setup cap is distinct from indexing or seed duration, which the parser's refusal explicitly identifies as uncapped.

The retained `providerDegradation` illustration enables the detector and failsafe and sets the memory ratios to 0.8 and 0.92. These conservative settings are parsed by the focused `kernel/primitives/provider_degradation_settings.py` owner; their presence is configuration vocabulary, not a report of live provider health or measurement.

The retirement illustration enables `autoLandOnIntegration`, `autoLandOnFinalize` and `autoCloseCompletedSeats`. The parser accepts the older `autoRetireOnIntegration` and `autoRetireOnFinalize` aliases, while current keys take precedence. Tool-log retention is also illustrated separately by `keepDays`, `maxBytes` and `enclosureMaxBytes`.

### Coding guidelines

`coding-guidelines.example.md` explains source ownership, file/function-size pressure, responsibility separation and refactor discipline. The current layer heading is Application entry point, with the matching anti-pattern wording; the earlier Controller terminology is not a separate live layer. Teams can adapt the document as their memory layer's coding-guidelines body.

## Invariants And Boundaries

- The template carries no `orchestration` block and no `memorySettingsIncludes` key. Agentic choices, including gate delegation, have their standard user-settings home. The runtime parser's warning-bearing, one-cycle gate-delegation fallback is not an instruction to add another orchestration block to this example.
- Paths shown in the template are placeholders to replace with authority-approved absolute roots, not facts about the executing workspace.
- A certification-profile reference selects declared policy; a template is neither certifying execution nor acceptance evidence.
- Report-gated completed-seat cleanup is subordinate to a successful completion edge. It targets the exact task's Worker/Reviewer/Curator roles only, requires the exact session's durable report before retirement and excludes Manager/Orchestrator owners. Disabling auto-close selects the landed/archive path; setting a template flag is not proof that any seat was actually closed.
- Parser configuration, provider health, dashboard supervision and Git/seat effects are different owners. An example's defaults must not be represented as observed deployment state.

## Evidence

- The public JSON example contains the repository/profile reference, empty per-provider objects and the named default illustrations. [1]
- The guideline example separates source responsibilities and uses Application entry point terminology. [2]
- External memory roots derive from the coordination root and reject the removed repository-local layout. [3]
- Supported provider entries derive runtime/log roots and reject unsupported per-provider fields. [4]
- Retirement parsing preserves the two legacy aliases with current-key precedence. [5]
- Gate delegation's standard settings home outranks the warning-bearing authority fallback. [6]
- The old provider timeout spelling refuses and explains the separate uncapped indexing/seed boundary. [7]
- Degradation settings retain explicit enable/failsafe switches and parsed threshold vocabulary. [8]
- Completion cleanup is report-gated for the finite leaf-role set and has a separate landed/archive branch. [9]
