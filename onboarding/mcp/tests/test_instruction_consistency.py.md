# mcp/tests/test_instruction_consistency.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves that every instruction and documentation text the product ships names only commands, tools, `task_doc` operations and paths that exist, and that each consistency rule fails on a planted counterexample instead of passing by sampling.

## Code Commentary

The checker lives in `agents_remember_test_support.testing.instruction_consistency`; this module drives it. The module-scoped `registry` fixture loads the registered CLI commands, MCP tools and knowledge names, and `_complete_mentions` builds a clean synthetic corpus that mentions every knowledge name and each migration command at its documentation owner.

- **Whole corpus.** Every text file under `skills/` and `docs/`, the root `README.md` and the registered tool descriptions must pass with no finding.
- **Mutations on each carrier.** An unregistered command or sub-command, an unregistered tool (in prose, a call, a table or an unclosed call), a missing `task_doc` operation, a missing path and every retired term are each reported, with a line number, on a skill detail, an architecture document, the README and a tool description alike.
- **Presence both ways.** Removing any knowledge name from skills or from the reference docs is reported as undocumented, and a misspelled `explainer_control` is an unregistered tool. Each migration command must stay documented at its exact owner document.
- **Exemptions stay narrow.** The conversion marker exempts a retired term on its own line only and never an unregistered command. Protocol names, statuses, schema fields, function calls and sidecar paths in prose are not mistaken for files or commands.
- **Historical records.** The frozen budget and digest-map files under `skills/l-01-agent-lifecycles/` are authenticated by content: their historical paths are not existence claims, but changed bytes, a duplicate JSON key or the same history in another file loses the exemption, and history-shaped fields elsewhere still report absent paths. The current budget record names no absent path outside a marked historical sub-record, and exactly one renewal sub-record claims to be current.

## Evidence

- The registry of commands, tools and knowledge names is loaded once. [1]
- The clean synthetic corpus mentions every knowledge name and migration-command owner. [2]
- The whole shipped corpus and registered descriptions pass. [3]
- Each reference-kind mutation fails on each required carrier. [4]
- Knowledge-name presence is checked both ways and a broken tool name fails. [5]
- The conversion exemption is explicit and confined to its line. [6]
- Protocol and diagnostic names are not files or commands. [7]
- A migration command requires its exact documentation owner. [8]
- Authenticated historical paths are not current existence claims, and changed or moved history is. [9]
- History-like fields do not hide active missing paths. [10]
- The current budget record names no absent path. [11]
- Exactly one renewal sub-record claims current. [12]
- A duplicate history key cannot borrow the owner's fingerprint. [13]
- A changed frozen owner fails its existing hash authentication. [14]
