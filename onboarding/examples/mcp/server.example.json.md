# examples/mcp/server.example.json

## Governing Overview

[overview](overview.md)

## Purpose

The one common tool-server registration example: the command and arguments that every harness adapts to start the Agents Remember MCP server.

## Code Commentary

The file declares only `command` (`uvx`) and `args`: `--managed-python`, `--python 3.14`, `--refresh-package agents-remember-mcp`, then the package command `agents-remember-mcp@latest`, then `--config` with the authority settings file at `<ABSOLUTE_USER_CONFIG_FOLDER>/agents-remember/agents-remember-settings.json`. uvx reads its own options first (`--managed-python` and `--python 3.14` ensure uv uses a managed Python 3.14 rather than a system 3.14, and `--refresh-package` takes the next argument as a package name), so the refresh names `agents-remember-mcp`, the `@latest` spec is the command that starts the server, and `--config` reaches that command rather than uvx; the round-9 form `--refresh-package agents-remember-mcp@latest --config …` left uvx no command and made it reject `--config`. The settings file is the settings home the server's CLI discovery reads; the placeholder must become an absolute path, because a JSON argument array does not expand `~`.

Each harness wraps this declaration in its own configuration envelope, which its install guide names; the example carries no harness-specific keys. A source checkout registers its locally built wheel with `uvx --managed-python --python 3.14 --from <wheel>` instead of the published package, as the READMEs show. Registering the server copies no skills or settings: the server serves the packaged skills as MCP resources.

## Evidence

- The example declares `uvx` with `--managed-python`, `--python 3.14`, `--refresh-package agents-remember-mcp`, the package command `agents-remember-mcp@latest`, and a user-config `--config` path passed to that command. [1]

- The tool-server settings file lives beside the user's role settings. [2]
