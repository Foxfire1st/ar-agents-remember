# mcp/src/agents_remember/kernel/coordination_context/settings.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

Selects which settings file of a memory or coordination root is parsed, and re-exports the parser helpers
that the public resolver facade offers.

## Code Commentary

`parse_coordination_settings(settings_path)` returns `(StorageSettings, CrossRepoSettings)`.

1. The JSON sibling of the given path (`path_settings_path_for`, the same name with `.json`) is probed
   first. When it exists it is the only file parsed (`parse_json_settings`); the Markdown file is not opened.
2. Otherwise, a missing Markdown file gives the default storage and cross-repository settings.
3. Otherwise every fenced YAML block of the Markdown file is parsed (`parse_settings_block`). The last
   block that sets storage wins; cross-repository settings are taken from the last block that has an
   allow list.

Both probes use `observed_exists` and the Markdown text is read with `observed_text`. Inside a recording
block the run therefore leaves one row for each file it looked at: `absent` for a missing JSON sibling,
`absent` for a missing Markdown file, and the SHA-256 of the bytes read for the file that was parsed. A
result kept with these rows is recomputed when a JSON sibling appears, when the parsed file changes or when
it disappears. A failed read is recorded as `unreadable (...)` and raised. Outside a recording block nothing
is recorded and the answers are the same. The text is decoded as UTF-8 with `\r\n` and `\r` turned into
`\n`.

## Evidence

- The JSON sibling first, then the default, then the fenced Markdown blocks, all through the recorder. [4]
- The absent JSON sibling and the consumed Markdown bytes are recorded; a JSON file that appears is a change. [5]
- A settings file changed and restored while a worklist child reads it is seen with the bytes actually parsed. [6]
