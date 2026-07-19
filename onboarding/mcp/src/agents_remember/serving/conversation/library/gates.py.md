# mcp/src/agents_remember/serving/conversation/library/gates.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/gates.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The live production-path capability gates for the dormant native library: a harness's history
features report `supported` only after a real gate against the installed runtime passes at the
exact locked versions, and any mismatch, missing binary, or failed probe demotes the whole
surface with an exact reason — fail closed and visible, never invented parity.

## Code Commentary

### Logic

`LibraryGateRegistry.history_capabilities` resolves the harness from the L0 registry, resolves
the installed executable, and gates once per installed-executable fingerprint (path + size +
mtime), cached per harness and bounded by construction to the three normalized harnesses; an
executable change re-runs the gate, which is exactly the design's observed-version demotion
rule. The Codex gate runs a real app-server connect + initialize + `thread/list` probe and
requires the observed CLI version to equal `LOCKED_CODEX_RUNTIME_VERSION` (0.144.5). The
Claude/Pi helper gates run `helper_preflight` (node, locked entry, installed locked
dependencies) plus a real native list call through the helper host, whose per-spawn handshake
observes the installed runtime/helper versions. Supported profiles are honest: Codex and Claude
stay `partial` on historical/tool completeness with permanent notes; Pi is fully `supported`
because its append-only entries are the complete session line.

### Conventions

Every `FeatureCapability` carries `runtime-fixture` evidence (observed versions, gate fixture
id, observation time); `unavailable` means the harness/binary is absent, `unverified` means the
gate ran and could not prove the locked configuration, with the exact observed-versus-locked
reason.

### Invariants And Boundaries

- No `supported` without live production-path evidence at the exact locked versions; fixture or
  helper presence alone never enables a capability.
- A failed probe demotes to `unverified` with the probe's typed reason, never `unavailable` and
  never a raw exception.
- The cache key is the executable fingerprint, so a reinstall or upgrade honestly re-gates.

### Todos

Claude stays `unverified` on machines whose installed runtime (2.1.214) differs from the locked
gate version (2.1.211) until a real installed 2.1.211 history passes the replay gate.

## Docs References

No Domain Documentation source is configured for this internal gate registry.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The doubled gate suite covers version match/mismatch, probe failure, missing binaries, and
helper preflight; the installed suite re-proves the same gates live; the helper host owns the
locked version constants the helper gates compare.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Codex version match enables with partial completeness; mismatch and failed probes demote to unverified. | L68-L125 | [test_conversation_library_gates.py](agents-remember/mcp/tests/test_conversation_library_gates.py) |
| Helper success enables Pi fully; helper failure and missing locked dependencies demote to unverified. | L158-L209 | [test_conversation_library_gates.py](agents-remember/mcp/tests/test_conversation_library_gates.py) |
| The locked runtime/helper version constants the helper handshake compares. | L39-L46 | [helper_host.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/helper_host.py) |
| The installed-runtime suite re-proves the Codex and Pi gates on real harnesses with exact skip reasons. | L134-L152; L215-L230 | [test_conversation_library_installed.py](agents-remember/mcp/tests/test_conversation_library_installed.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local gate registry.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the live capability gate registry
  sidecar. Verification is blank until closeout commits and stamps the new source.
