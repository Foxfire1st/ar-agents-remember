# mcp/src/agents_remember/worktrees/role_handover_locator.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

One bounded, product-owned directory alias per launch request, so the hand-over artifact can be named by a path whose length does not depend on how deep the report folder is.

## Code Commentary

`locator_root` is the durable root the product owns, `~/projects/.agents-remember/handover-locators`; it sits outside every worktree, enclosure and scratch folder, which are all removed when a task ends. `locator_directory` names one request's alias by the request id and refuses a name that cannot be an id. `is_locator` recognizes a directory directly under that root.

`ensure_locator` makes the alias lead to the report folder: an alias that already leads there is reused without being rewritten, so a repeat and a resume keep one locator; an absent one is created as a directory link, so a lost locator is rebuilt at the same place; and anything else at the name — a link to another folder, a real directory, a file — is refused with `locator_refusal` before a launch writes any of its files. `remove_locator` removes only the alias, and only when it leads inside the folders being reclaimed; an absent name and one that leads outside are reported and left standing, so a report folder is never touched and a foreign target is never unlinked.

The artifact keeps its own name, bytes and write-once mode beside the report. The alias changes only the path the agent is given, never the file's identity, and no link is followed at the artifact's own name.

## Evidence

- The durable root is the product's own folder under the user's projects directory. [1]
- One request id names one alias, and a name that cannot be an id is refused. [2]
- The product recognizes its own locators directly under that root. [3]
- A repeat reuses the alias, a lost one is rebuilt at the recorded folder, and a name that would lead elsewhere is refused. [4]
- Removal deletes only an alias that leads inside the reclaimed folders and reports every other name as it stands. [5]
