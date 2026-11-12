# mcp/src/agents_remember/cli/settings_provenance.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Builds the line a command-line run prints when it discovered its settings file: the file it used and, when the dashboard daemon of the same coordination root runs with another settings file, that file and the daemon's pid.

## Code Commentary

`discovered_settings_line` starts with `settings discovered: <path>`. It reads the recorded dashboard state under the coordination root and asks the process that answers on that state's host and port for the `--config` it was started with. Only when that file differs from the discovered one and names the same coordination root does the line add `dashboard daemon pid <pid> uses <file> for the same coordination root`. A missing state, no answering dashboard, a dashboard without an observable `--config`, the same file or another coordination root leave the line plain. A failure to observe the dashboard or to read its settings adds `dashboard settings comparison is unknown` with the reason.

The function is read-only: it writes no settings file and no daemon state, and it is called only by `cli/discovery.discover_config`, which prints the line to stderr. An explicit `--config` run prints no provenance line.

## Evidence

- The line names the discovered file, and adds the daemon's other file only for the same coordination root, or the reason the comparison is unknown. [1]
- The answering dashboard's process and its `--config` are observed from the port's socket owner. [2]
- Discovery prints the line to stderr after selecting the user's settings file. [3]
