# mcp/src/agents_remember/serving/conversation/projectors/__init__.py

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

Declares the engine-facing `HarnessProjector` protocol every per-harness projector module
satisfies, binds the three landed harness modules (codex, claude, pi) to it with their
channel-capability flags, and exposes the `PROJECTORS` registry plus `projector_for` lookup the
session factory consumes.

## Code Commentary

### Logic

`HarnessProjector` is a `Protocol` with four channel flags — `harness_id`, `uses_native_pages`,
`uses_transcript_echo`, `eager_native_continuation` — and three mapping entry points
(`map_native_frame`, `map_evidence_frame`, `map_transcript_echo`). `map_evidence_frame` also takes the
optional keyword `parent_thread_id`: the multiplexed-harness demux context (the parent thread's vendor
id) that lets codex/claude mappers route a frame to its sub-agent thread; harnesses without sub-agent
threads (pi, and eve) accept and ignore it.

**Four** private adapter classes bind the module-level mapper functions and declare each harness's
honest channel set: codex pages native threads with lazy continuation and no echo; claude is
stream/replay-only (its `map_native_frame` raises `NotImplementedError`) and consumes the submission
echo; pi pages durable entries with eager native continuation so live items always carry native
identity; and — since the eve product-integration change set — `_EveProjector` declares the **durable
stream as its only evidence surface**, setting `uses_native_pages = False`,
`uses_transcript_echo = False` and `eager_native_continuation = False`, so both other channels fail
closed for a harness that carries neither. `PROJECTORS` maps harness id to the bound projector — now
including `"eve"`, which is what makes "every registered harness id has a projector" true — and
`projector_for` returns `None` for harnesses without a projector so the factory fails closed typed.

### Conventions

Mappers stay pure module-level functions; the adapter classes only bind them as `staticmethod`s
and declare flags — no state, no IO, no engine knowledge. Channels a harness does not have raise
`NotImplementedError` rather than silently no-oping, so an engine wiring mistake is loud.

### Invariants And Boundaries

- The engine reads channel behavior only through these flags; it never special-cases a harness.
- A harness without a registered projector must fail session resolution typed, never default.
- Claude's `map_native_frame` must keep failing closed: claude has no native page by design.
- `parent_thread_id` is keyword-only with a `None` default: non-multiplexed
  harnesses satisfy the protocol without knowing the demux seam exists, and `None` always means
  the parent conversation.
- New harnesses register here and in the capability evidence, nowhere else in the engine.

### Todos

None.

## Evidence

### Docs References

The resolved `Domain Documentation` registry has no entries. The per-harness schema authorities
(the codex app-server v2 generated protocol, the locked claude stream-json fixtures, the locked
Pi RPC documentation) are cited by the individual mapper sidecars.

No configured domain documentation was available for this registry.

### Repo-Internal References

The three mapper modules own the actual frame grammars; the engine in the `active/projector/`
package drives mappers through these flags; the factory in `active/factories.py` resolves
harnesses through `projector_for`.

- The engine's native ingest reads all three channel flags: `uses_native_pages` seeds `native_complete` and gates the dirty-tip refresh, `uses_transcript_echo` arms the echo-zipper eviction guard and diverts frames to the echo buffer, and `eager_native_continuation` picks lazy tip-refresh vs the eager continuation poll. [1]
- The echo projector applies the transcript-echo channel flag. [2]
- The child-history projector applies the native-pages channel flag. [3]
- The rebuild coordinator applies the native-pages channel flag for parent-history re-derivation. [4]
- The session factory resolves the per-harness projector and fails closed when none exists. [5]
- Mapper output types the protocol's entry points return are defined in the shared module. [6]
- The eve projector bound here, and the three flags that make the durable stream its only evidence surface. [7]
- The per-harness mapper module the registration binds. [8]
- The harness union a registered projector's `harness_id` is typed with, widened so eve could register. [9]
- The cases: every registered harness id has a projector, and the eve projector declares stream-only evidence. [10]

### Cross-Repo References

No cross-repository implementation participates in this registry.

No meaningful cross-repo references found.
