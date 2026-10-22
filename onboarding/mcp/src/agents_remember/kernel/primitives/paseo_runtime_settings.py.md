# mcp/src/agents_remember/kernel/primitives/paseo_runtime_settings.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Defines strict optional authority for one install prefix, home, listen endpoint, providers and embed, plus an optional retired version key that never selects the release.

## Code Commentary

A present block must carry the five operational facts (`installPrefix`, `home`, `listen`, `providers`, `embed`) and accepts an optional `version` that never selects the release; providers/embed may be empty but cannot be malformed. The parser rejects nonabsolute paths, malformed listen/ports and unknown keys, and any provided `version` that differs from the packaged contract produces one notice rather than a refusal or a selection. Embed origins must already match the exact browser-canonical spelling; noncanonical spelling is refused, not silently normalized. Frame URLs are validated without credentials/query/fragment, and duplicate canonical origins refuse. An absent block remains None and require_paseo_runtime names no runtime configured.


**L184 — MIK-R192 extra arguments, not a usage read.** This primitive parses the settings map and refuses `extraArgs` in the host provider's own configured options and in any entry that extends that provider; it is settings parsing and a configured-argument refusal, not a reader of the host's usage report, and nothing here decides a limit. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

- Frozen implementation of parse_paseo_runtime_settings supporting the stated file behavior. [1]
- Frozen implementation of _embed_entry supporting the stated file behavior. [3]
- Exercises absent, valid empty providers/embed, missing and unknown runtime fields and rejects malformed block shapes. [4]
- Runs all three commands without the block and checks named refusal, exit two and no process operation. [5]
- Checks a mismatched install is replaced and a failed staged installation preserves the preceding install and daemon. [6]

## 260928-MIK-L96 Five facts and an optional version

A present `paseoRuntime` block now requires the five operational facts (`installPrefix`, `home`, `listen`, `providers`, `embed`); the `version` key is optional and no longer the pin. A block whose version names another version, or no exact version, loads, the packaged contract's version is used, and one notice names the key, the settings file and both versions. A block outside the five-plus-version set is still refused at parse time, an absent block is still the named no-host state, and the block now also reports the settings file it came from.

- The parser with the five facts and optional version. [7]
- The named no-host state and its refusal. [8]
