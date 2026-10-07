# mcp/src/agents_remember/kernel/coordination_context/json_settings.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

Parses the machine-readable settings file `settings.json` into storage settings, path rules and
cross-repository settings.

## Code Commentary

- `parse_json_settings(settings_path)` reads the file once with `observed_text` and parses it as JSON.
  Invalid JSON raises `ValueError` naming the file. The root must be an object. When it has an `onboarding`
  key, storage and path rules are read from that object, with the root as fallback for each of them;
  without the key they are read from the root.
- Inside a recording block the read is recorded with the SHA-256 of the bytes read, also when the JSON then
  turns out to be invalid; a missing or unreadable file is recorded as `absent` or `unreadable (...)` and
  the error is raised. Outside a recording block nothing is recorded.
- `parse_json_storage_settings` applies `storage.mode` (or `storage.layout`) and `storage.default`. A mode
  also becomes the default unless a default is given.
- `parse_json_path_rules` accepts one object or a list. `parse_json_path_rule` normalizes `path` (or `repo`)
  and reads `storage`, `include.paths` (default `*`), `exclude.paths`, `include.fileTypes` and
  `exclude.fileTypes`. A value of the wrong type raises `ValueError` with the rule's label.
- `parse_json_cross_repo_settings` reads `crossRepo.allow` through `parse_cross_repo_allow`.

The parser inspects no file other than the one it is given and starts no Git command.

## Evidence

- One recorded read, the JSON error, and the onboarding wrapper with its root fallback. [4]
- Storage mode and default. [5]
- One path rule with its include and exclude lists. [6]
- The cross-repository allow list. [7]
- A JSON settings file is recorded with its bytes, also when it is not valid JSON. [8]
