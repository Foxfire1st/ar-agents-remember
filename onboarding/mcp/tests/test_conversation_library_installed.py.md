# mcp/tests/test_conversation_library_installed.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_installed.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Installed-runtime production gates for 260718-CHATS-L2: exercises the REAL seams on machines
where the harnesses are installed — the live Codex app-server gate and library, the locked Pi
helper gate/library, end-to-end Codex and Pi opens through the tracked opener with exact
catalog proof and retirement, and the Claude version-mismatch fail-closed proof.

## Code Commentary

### Logic

Eight opt-in tests, each skipping with an exact reason where its runtime precondition is absent
(CI has no harnesses); none fabricates capability evidence. Codex: the live gate supports
list/read with partial completeness, and a list → read → resolve round-trip runs over the real
0.144.5 app-server. Pi: the live helper gate, the list/read/resolve round-trip, the helper
protocol's malformed-request rejection, and a real end-to-end open (spawn through
opener → tmux → runner → `pi --mode rpc --session <file>`, exact vendor id + bridge epoch
catalog proof, idempotent replay, retirement with no leaked `ar-open-*` sessions). Codex open:
the same end-to-end proof through the landed L0E `resume_thread_id` channel. Claude: installed
2.1.214 vs locked 2.1.211 handshakes `incompatible` and the whole surface stays `unverified`
with the exact reason.

### Conventions

These are the evidence source for `runtime-fixture` capability claims: the gate results they
produce on a qualifying machine are what the fixtures record (shape descriptors only, never
enabling).

### Invariants And Boundaries

- Every test skips honestly where its harness/runtime precondition is absent; no synthetic
  capability evidence is ever produced.
- Open E2Es must retire what they spawn and leave no tmux/catalog leaks.
- Real spawns only through the tracked opener; no test-local process management.

### Todos

None.

## Docs References

No Domain Documentation source is configured. The repository sources and installed-runtime
fixture contract are direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The runtime fixtures recording (never enabling) the gate/open evidence rows this suite produces. | L21-L34 | [codex-0.144.5.json](agents-remember/mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json) |
| The open service whose real spawn/proof/retire arms this suite exercises end-to-end. | L209-L320 | [open_service.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/open_service.py) |
| The doubled gate/port suites whose live counterparts these tests are. | L1-L7 | [test_conversation_library_ports.py](agents-remember/mcp/tests/test_conversation_library_ports.py) |

## Cross-Repo References

No neighboring repository participates in this installed-runtime suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the installed-runtime
  library/open production gate sidecar. Verification is blank until closeout commits and
  stamps the new source.
