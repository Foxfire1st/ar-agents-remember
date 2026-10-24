# mcp/src/agents_remember/application/user_settings_init.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Create the one user settings file with a harness per role, only when that destination is absent, and never write, merge, complete or re-mode one that exists.

## Code Commentary

The single write is `orchestration.roles.<role>.harness` in `~/.config/agents-remember/settings.json` under `XDG_CONFIG_HOME`, with model and effort left unset so each harness keeps its own defaults. The host authority is not this file: the `paseoRuntime` block belongs to the installed MCP settings file, and this module never writes it. An existing regular JSON-object destination is read and reported as it stands, including migrated or hand-written settings, without needing a live host. A symlink is refused before the read; unreadable or non-object JSON is refused with the reason and manual recovery, without replacing the destination. No key inside a file is custody of that file, so nothing here completes or merges one. Only an absent destination reaches validation and the one create: `O_CREAT | O_EXCL` at mode 0600, so the kernel refuses a destination that appeared between the preview and the write and refuses a symlink at that path, and the bytes are never readable by another account even for an instant. There is no temporary sibling path and no replacement step, so nothing outside the one destination is opened for writing. Choices are refused by name — no harness chosen, a role this build does not publish, a harness the configured host does not report (the refusal lists the ones it can run), or an unreadable host catalog — and every refusal carries a `code`, a `detail` and a `nextAction` while writing nothing. A read-back failure after a completed create is answered as no read-back rather than raised, so a create that happened is not reported as a failure.

## Evidence

- The one create-or-report decision, with the existing file reported before any choice is validated. [1]
- The exclusive create at 0600 that refuses any destination already present. [2]
- The write-time refusal of a destination the preview saw absent. [3]
- An absent destination is created exclusively with the chosen roles, and the created file is not world readable. [4]
- An existing marked file is reported and kept byte for byte, an unreadable one is refused without a second read, and a destination that appears after the state read is refused. [5]

- Current source account and its stated boundaries. [6]
