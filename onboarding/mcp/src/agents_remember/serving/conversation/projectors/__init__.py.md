# mcp/src/agents_remember/serving/conversation/projectors/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `41b2fd6452ee572799fa10c4f9c820ab549ec3d2`|
| lastVerifiedCommitDate | 2026-07-19T19:12:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

Declares the engine-facing `HarnessProjector` protocol every per-harness projector module
satisfies, binds the three landed harness modules (codex, claude, pi) to it with their
channel-capability flags, and exposes the `PROJECTORS` registry plus `projector_for` lookup the
session factory consumes.

## Code Commentary

### Logic

`HarnessProjector` (L24-L51) is a `Protocol` with four channel flags — `harness_id`,
`uses_native_pages`, `uses_transcript_echo`, `eager_native_continuation` — and three mapping
entry points (`map_native_frame`, `map_evidence_frame`, `map_transcript_echo`). Three private
adapter classes (L54-L109) bind the module-level mapper functions and declare each harness's
honest channel set: codex pages native threads with lazy continuation and no echo; claude is
stream/replay-only (its `map_native_frame` raises `NotImplementedError`) and consumes the
submission echo; pi pages durable entries with eager native continuation so live items always
carry native identity. `PROJECTORS` (L112-L116) maps harness id to the bound projector;
`projector_for` (L119-L120) returns `None` for harnesses without a projector so the factory
fails closed typed.

### Conventions

Mappers stay pure module-level functions; the adapter classes only bind them as `staticmethod`s
and declare flags — no state, no IO, no engine knowledge. Channels a harness does not have raise
`NotImplementedError` rather than silently no-oping, so an engine wiring mistake is loud.

### Invariants And Boundaries

- The engine reads channel behavior only through these flags; it never special-cases a harness.
- A harness without a registered projector must fail session resolution typed, never default.
- Claude's `map_native_frame` must keep failing closed: claude has no native page by design.
- New harnesses register here and in the capability evidence, nowhere else in the engine.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. The per-harness schema authorities
(the codex app-server v2 generated protocol, the locked claude stream-json fixtures, the locked
Pi RPC documentation) are cited by the individual mapper sidecars.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this registry. | — | — |

## Repo-Internal References

The three mapper modules own the actual frame grammars; the engine in `active/projector.py`
drives mappers through these flags; the factory in `active/factories.py` resolves harnesses
through `projector_for`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The engine consumes channel flags to choose hydration, echo-zipper, and continuation behavior. | L176-L181; L306-L310 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |
| The session factory resolves the per-harness projector and fails closed when none exists. | L90-L94 | [factories.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/factories.py) |
| Mapper output types the protocol's entry points return are defined in the shared module. | L55-L94 | [common.py](agents-remember/mcp/src/agents_remember/serving/conversation/projectors/common.py) |

## Cross-Repo References

No cross-repository implementation participates in this registry.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the projector
  protocol/registry — channel flags, three per-harness bindings, fail-closed lookup. Verification
  is blank because the new source file is uncommitted; closeout owns its first source stamp.
