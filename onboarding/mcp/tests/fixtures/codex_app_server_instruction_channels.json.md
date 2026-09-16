# mcp/tests/fixtures/codex_app_server_instruction_channels.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/codex_app_server_instruction_channels.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T14:15+02:00 |
| lastVerifiedCommitHash | `34f818a190c35238dca33552d586ea2ace5d9e06` |
| lastVerifiedCommitDate | 2026-09-16T14:33:47+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l5-ar` uncommitted source; base `c1dbebf883f22710b71d40a66ec92c1ac134918f` |
| governingOverview | `../overview.md` |

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

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The per-request instruction fields are recorded, with `turn/start` deliberately empty. | `"instructionFields"` | mcp/tests/fixtures/codex_app_server_instruction_channels.json:5-19 |
| The thread-open response's own observation field is recorded. | `"threadOpenResponseInstructionFields"` | mcp/tests/fixtures/codex_app_server_instruction_channels.json:20-22 |
| The fixture supplies the case that pins the delivered instruction parameter. | `test_instruction_channel_is_the_schema_supported_thread_open_field` | mcp/tests/test_codex_capsule_delivery.py:296-315 |

## Cross-Repo References

Generated from the external Codex CLI app-server schema.

| Finding | Anchor | Source |
| --- | --- | --- |
| Generation provenance and the pinned version are recorded in the fixture itself. | `cliVersion`; `schemaBundleDigest` | mcp/tests/fixtures/codex_app_server_instruction_channels.json:3-4 |

## Update History

- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: created onboarding for the installed-schema
  instruction-channel fixture, recording that it is the independent side of the wire comparison, the
  `turn/start` absence the lifetime design rests on, the expiry contract, and the regeneration path.
  `governingOverview` is `../overview.md` (the route-local `mcp/tests/overview.md` the census names as
  this source's nearest governing route) rather than the grandparent the sibling
  `codex_app_server_0_144_3.json.md` card points at. Verification metadata stays pinned to the last
  committed source (`c1dbebf8`).
