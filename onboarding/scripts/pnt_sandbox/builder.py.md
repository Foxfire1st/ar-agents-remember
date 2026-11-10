# scripts/pnt_sandbox/builder.py

## Governing Overview

[overview](../../overview.md)

## Purpose and current source account

Repeatable build creates the disposable repository/origin, publishes corpus through the selected build tools and preserves existing repository/task/memory/Paseo state. Settings and Eve application/launcher inputs are deliberately regenerated; layout version 5 gives the sandbox its own user configuration. Unmarked populated directories and unfinished reset state refuse. The marker's state transition is whole-file replace.

The corpus request names its sandbox and that sandbox's `hostPort`, produced from the build's own layout, so the helper that runs the corpus admits only the sandbox's own Paseo host. The corpus runs before the build writes the sandbox's `paseoRuntime` settings, which is the one no-host phase the helper admits.

## Evidence

The current preparation owner is sandbox settings_expectation through Operations.render_settings; the host block is written to the sandbox MCP authority, separately from developer user settings.

- The built-state recognition. [2]

- The current builder writes host facts to MCP authority and consumes preparedSettingsPath from the sandbox-owned preparer. [4]

- The scoped current source carries the module/document behavior described above. [1]

- The corpus request carries the sandbox and its Paseo port from the layout, and the bootstrap order is unchanged. [3]
