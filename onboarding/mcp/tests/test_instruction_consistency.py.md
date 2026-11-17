# mcp/tests/test_instruction_consistency.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves that every instruction and documentation text the product ships names only commands, tools, `task_doc` operations and paths that exist, and that each consistency rule fails on a planted counterexample instead of passing by sampling.

## Code Commentary

The checker lives in `agents_remember_test_support.testing.instruction_consistency`; this module drives it. The module-scoped `registry` fixture loads the registered CLI commands, MCP tools and knowledge names, and `_complete_mentions` builds a clean synthetic corpus that mentions every knowledge name outside the checker's set `UNDOCUMENTED_COMMANDS`.

- **Whole corpus.** Every text file under `skills/` and `docs/`, the root `README.md` and the registered tool descriptions must pass with no finding.
- **Mutations on each carrier.** An unregistered command or sub-command, an unregistered tool (in prose, a call, a table or an unclosed call), a missing `task_doc` operation, a missing path and every retired term are each reported, with a line number, on a skill detail, an architecture document, the README and a tool description alike.
- **Presence both ways.** Removing any knowledge name from skills or from the reference docs is reported as undocumented, and a misspelled `explainer_control` is an unregistered tool. A migration command that serves only an earlier installation must have no documentation row; the refusal of a row that names one is asserted in `test_role_instruction_corpus.py`.
- **Exemptions stay narrow.** The conversion marker exempts a retired term on its own line only and never an unregistered command. Protocol names, statuses, schema fields, function calls and sidecar paths in prose are not mistaken for files or commands.
- **Historical records.** The frozen budget files under `skills/l-01-agent-lifecycles/` are authenticated by their recorded hashes. The checker compares each supplied surface with its owner and rejects duplicate JSON keys. Historical fields in the current budget and retired digest-map bindings use the owner-specific masking rules; history-shaped fields elsewhere still report absent paths. The current budget record names no absent path outside a marked historical sub-record. Exactly one renewal sub-record is nonhistorical and contains only `authority`.

## Evidence

- The registry of commands, tools and knowledge names is loaded once. [1]


- The whole shipped corpus and registered descriptions pass. [3]
- Each reference-kind mutation fails on each required carrier. [4]


- The conversion exemption is explicit and confined to its line. [6]
- Protocol and diagnostic names are not files or commands. [7]
- Authenticated historical paths are not current existence claims, and changed or moved history is. [9]
- History-like fields do not hide active missing paths. [10]


- A duplicate history key cannot borrow the owner's fingerprint. [13]

- The current budget record names no absent path. [11]

- Exactly one renewal sub-record is nonhistorical and contains only its authority; historical sub-records carry no current field. [12]

- A changed frozen owner fails its existing hash authentication. [14]

- The clean synthetic corpus mentions every knowledge name outside the set `UNDOCUMENTED_COMMANDS`. [2]

- Knowledge-name presence is checked both ways and a broken tool name fails. [5]

- A migration command of an earlier installation needs no documentation row; the refusal of a row that names one is asserted in test_role_instruction_corpus.py. [8]
