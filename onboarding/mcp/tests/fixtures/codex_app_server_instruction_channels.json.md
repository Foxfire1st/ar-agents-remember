# mcp/tests/fixtures/codex_app_server_instruction_channels.json

## Governing Overview

[mcp/tests overview](../overview.md)

## Purpose

**The independent side of the capsule-delivery wire comparison.** `260915-CAPS-L5` added it: it records
which instruction-bearing fields the **installed** `codex-cli 0.151.0` app-server schema exposes per
request, so the case that pins `developerInstructions` reads the vendor's own answer instead of the
module under test's opinion of it.

| Field | Meaning |
| --- | --- |
| `cliVersion` | the installed CLI the schema was generated from — `codex-cli 0.151.0` |
| `schemaBundleDigest` | the generated bundle's digest (`sha256:5d2d6d4e…c678`) |
| `instructionFields` | instruction fields per request type: `thread/start`, `thread/resume` and `thread/fork` each expose `baseInstructions` + `developerInstructions`; **`turn/start` exposes none** |
| `threadOpenResponseInstructionFields` | `instructionSources` — the host's own list of loaded instruction documents on the thread-open response |

The `turn/start` empty list is the fact the whole lifetime design rests on: with no turn-level
instruction field, an ordinary user message cannot re-apply the role corpus, so a changed revision
needs a supported thread-open boundary or an explicit refusal.

## Code Commentary

The fixture was generated with `codex app-server generate-json-schema --out <DIR>` against the
installed CLI, and its `_note` records that it is read by the test and **never imported from the
module under test** — the comparison is between two independent sources, not a tautology.

### Conventions

Pinned to one CLI version. Regeneration is the only edit path: regenerate the schema, update
`cliVersion` and `schemaBundleDigest`. The repository's older `codex_app_server_0_144_3.json` fixture
remains evidence about **that** schema; it is not the contract for this one.

### Invariants And Boundaries

- The fixture is an *expiry* artifact: the next installed app-server version change invalidates it.
- A version mismatch is **reported** by the live case's guard, never silently tolerated.
- It proves the schema surface only; it is not proof that a live thread applied anything.

### Todos

Regenerate on the next pinned-CLI change.

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved source registry.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The per-request instruction fields are recorded, with `turn/start` deliberately empty. [1]
- The thread-open response's own observation field is recorded. [2]
- The fixture supplies the case that pins the delivered instruction parameter. [3]

### Cross-Repo References

Generated from the external Codex CLI app-server schema.

- Generation provenance and the pinned version are recorded in the fixture itself. [4]
