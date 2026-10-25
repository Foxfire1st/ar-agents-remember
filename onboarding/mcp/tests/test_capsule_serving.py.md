# mcp/tests/test_capsule_serving.py

## Governing Overview

[tests overview](overview.md)

## Purpose

Focused behaviour cases for the capsule operation and the SEP-2640 skill surface: admission, manifest authority, re-read versus refusal on moved bytes, and the skill-serving guarantees. The module holds 16 collected cases over a synthetic corpus; the shipped-surface, protocol-exchange and guard cases moved whole to `test_capsule_serving_surface.py`, which imports this module's worlds and helpers so each definition lives once.

## Code Commentary

`World` is the fixture: a disposable coordination root with an external-memory contract plus leaf and master task documents, and a synthetic skills corpus whose bytes the cases can predict. `_contract_text` writes that contract with `memory_mode: external` and a memory ledger. The 16 cases pin the admission guarantees (routed blocks carry the fixture's own bytes, no write to the read tree, no role acquisition by string change, unknown roles and escaping paths refused, manifest decides the source set, moved bytes re-read versus refused), the skill-serving guarantees (origin and revision kept, changed bodies refused, no tool grant from frontmatter, tool surface unchanged by resource reads, same-named skills from two servers distinct, discovery registry distinct from the visible catalog, bodies never composed into the instruction stream, non-conforming directories recorded not served). No case here carries an integration marker; the real-process exchange lives in the surface module.

## Current audience, delivery and evidence contract

The synthetic manifest now declares `audience: all` for each operation. Its unsectioned operation text remains intentionally whole-body input; the new audience/manifest-edge modules, not this compatibility fixture, protect section selection and malformed markers.

## Evidence


- Fixture world with external contract and synthetic corpus [14]

- Contract text is external-memory with a ledger [15]
- Capsule carries routed blocks with the fixture's own bytes [16]
- Moved task bytes are re-read versus refused as separate behaviours [17]

- Non-conforming skill directory is recorded, never served [18]

- Shipped-surface, exchange and guard cases moved to the surface module [19]


- The only source change gives every synthetic operation an explicit audience=all, matching the extended manifest schema without changing expected synthetic operation bodies. All existing no-read-tree-write, role acquisition, task-digest, skill-reference/tool-boundary and resource registry cases remain. [20]
