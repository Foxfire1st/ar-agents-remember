# examples/mcp Overview

| Field | Value |
| --- | --- |
| sourceRoute | `examples/mcp` |

## Governing Overview

[overview](../../overview.md)

## Purpose

`examples/mcp/` holds the public MCP authority-settings template, `settings.example.json`, the one common tool-server registration example, `server.example.json`, and a coding-guidelines example that teams can adapt for a memory repository. The authority template is separate from a memory layer's `system/settings.json`; the guidelines are documentation-shaped example content, not an automatically selected runtime input.

## Hot Path Summary

Start with `settings.example.json` for the repository/profile and runtime settings shape and `server.example.json` for the server command each harness registers; read the guideline example for source/application ownership. The configured runtime owns parsing and admission, so these illustrative files do not themselves confer execution or lifecycle authority.

## How It Is Built

### Authority settings

The JSON template names one coordination root, one workspace root and the transcript-log root, then declares repository IDs. The `agents-remember` repository entry selects `mcp/certification-profile-v1.json` beside a null `contractPath`; it is a reference to the checked-in profile, not another executor. Configured repository roots derive from `workspaceRoot/<repo-id>`, and external memory derives from `coordinationRoot/memory-repos/ar-<repo-id>`.

The example carries no `providers` or `providerDegradation` block; `runtime_config.py` lists `retirement`, `providers` and `providerDegradation` in `UNUSED_SETTINGS_SECTIONS` so older files still load while reporting those keys as unused.

`benchmarksEnabled` is false. Dashboard supervision is opt-in in the template (`autoStart: false`, `port: 8765`). Timeout caps illustrate `toolSeconds` only; `parse_timeout_caps` admits only `toolSeconds`, ignores retired `providerSetupSeconds` (reporting it as unused), and rejects unknown keys.

The retirement illustration enables `autoLandOnIntegration`, `autoLandOnFinalize` and `autoCloseCompletedSeats`. `runtime_config.py` lists `retirement` in `UNUSED_SETTINGS_SECTIONS` so the section loads unread and is reported in `unused_settings_keys`. Tool-log retention is also illustrated separately by `keepDays`, `maxBytes` and `enclosureMaxBytes`.

### Server registration

`server.example.json` is the single command/arguments declaration that each harness adapts inside its own configuration envelope, as the install guides describe: `uvx --managed-python --python 3.14 --refresh-package agents-remember-mcp agents-remember-mcp@latest` (selecting uv-managed Python 3.14, then the refresh option with the package name, then the `@latest` command) with `--config` passed to that command, naming the authority settings file at `<ABSOLUTE_USER_CONFIG_FOLDER>/agents-remember/agents-remember-settings.json`. The placeholder must become an absolute path, because a JSON argument array does not expand `~`. The example carries no harness-specific keys and installs nothing.

### Coding guidelines

`coding-guidelines.example.md` explains source ownership, file/function-size pressure, responsibility separation and refactor discipline. The current layer heading is Application entry point, with the matching anti-pattern wording; the earlier Controller terminology is not a separate live layer. Teams can adapt the document as their memory layer's coding-guidelines body.

## Invariants And Boundaries

- Canonical lifecycle finalization records its actual completion edge/contract facts; the retired automatic Worker/Reviewer/Curator closeout cleanup and auto-close/landed opt-out are not current settings or effects. Explicit receipt-tracked native retirement remains a separately authorized operation, not an automatic template consequence.

## Evidence

- The public JSON example contains the coordination/workspace/transcript roots, repository/profile reference, timeoutCaps.toolSeconds, benchmarksEnabled, dashboard, retirement and toolLog illustrations, with no providers or providerDegradation blocks. [1]

- The guideline example separates source responsibilities and uses Application entry point terminology. [2]
- External memory roots derive from the coordination root and reject the removed repository-local layout. [3]
- Gate delegation's standard settings home outranks the warning-bearing authority fallback. [6]


- parse_timeout_caps admits only toolSeconds, silently skips retired providerSetupSeconds (reported by unused_settings_keys), and rejects any other key as an unsupported timeout cap. [7]



- The common registration example runs `uvx` with the published package and an absolute user-config settings path. [9]
