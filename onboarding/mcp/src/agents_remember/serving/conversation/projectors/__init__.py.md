# mcp/src/agents_remember/serving/conversation/projectors/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:34 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

cit:([`HarnessProjector`], mcp/src/agents_remember/serving/conversation/projectors/__init__.py:24-52) is a `Protocol` with four channel flags — `harness_id`,
`uses_native_pages`, `uses_transcript_echo`, `eager_native_continuation` — and three mapping
entry points (`map_native_frame`, `map_evidence_frame`, `map_transcript_echo`).
cit:(["def map_evidence_frame("], mcp/src/agents_remember/serving/conversation/projectors/__init__.py:39-45) also takes the optional keyword
  `parent_thread_id`: the multiplexed-harness demux context (the parent thread's vendor id) that
lets codex/claude mappers route a frame to its sub-agent thread; harnesses without sub-agent
threads (pi) accept and ignore it. cit:([`parent_thread_id`], mcp/src/agents_remember/serving/conversation/projectors/__init__.py:46-46) Three private adapter classes bind the module-level mapper
functions and declare each harness's
honest channel set: codex pages native threads with lazy continuation and no echo; claude is
stream/replay-only (its `map_native_frame` raises `NotImplementedError`) and consumes the
submission echo; pi pages durable entries with eager native continuation so live items always
carry native identity. cit:([`_CodexProjector`, `_ClaudeProjector`, `_PiProjector`], mcp/src/agents_remember/serving/conversation/projectors/__init__.py:55-72; mcp/src/agents_remember/serving/conversation/projectors/__init__.py:75-90; mcp/src/agents_remember/serving/conversation/projectors/__init__.py:93-110) cit:([`PROJECTORS`], mcp/src/agents_remember/serving/conversation/projectors/__init__.py:113-117) maps harness id to the bound projector;
cit:([`projector_for`], mcp/src/agents_remember/serving/conversation/projectors/__init__.py:122-123) returns `None` for harnesses without a projector so the factory
  fails closed typed.

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

## Docs References

The resolved `Domain Documentation` registry has no entries. The per-harness schema authorities
(the codex app-server v2 generated protocol, the locked claude stream-json fixtures, the locked
Pi RPC documentation) are cited by the individual mapper sidecars.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this registry. | — | — |

## Repo-Internal References

The three mapper modules own the actual frame grammars; the engine in the `active/projector/`
package drives mappers through these flags; the factory in `active/factories.py` resolves
harnesses through `projector_for`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The engine's native ingest reads all three channel flags: `uses_native_pages` seeds `native_complete` and gates the dirty-tip refresh, `uses_transcript_echo` arms the echo-zipper eviction guard and diverts frames to the echo buffer, and `eager_native_continuation` picks lazy tip-refresh vs the eager continuation poll. | `NativeEvidenceIngestion` | mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:44-268 |
| The echo projector applies the transcript-echo channel flag. | `EchoIngestion` | mcp/src/agents_remember/serving/conversation/active/projector/echo_ingestion.py:35-187 |
| The child-history projector applies the native-pages channel flag. | `ChildHistoryProjection` | mcp/src/agents_remember/serving/conversation/active/projector/child_history.py:25-173 |
| The rebuild coordinator applies the native-pages channel flag for parent-history re-derivation. | `RebuildCoordinator` | mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py:63-192 |
| The session factory resolves the per-harness projector and fails closed when none exists. | `build_identity` | mcp/src/agents_remember/serving/conversation/active/factories.py:79-105 |
| Mapper output types the protocol's entry points return are defined in the shared module. | `MappedItem` | mcp/src/agents_remember/serving/conversation/projectors/common.py:56-60 |

## Cross-Repo References

No cross-repository implementation participates in this registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 6 repository-reference citations (6/6 anchored and sourced; scoped citation check clean).

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the channel-flag citation, broken when
  `active/projector.py` became the `active/projector/` package (commit `3a8ff70`). Grepped all
  three flag names across the package and read every hit: `native_ingestion.py` L60 (`native_complete
  = not mapper.uses_native_pages`), L106-L113 (`refresh_native_tip` short-circuit), L131-L138
  (the `uses_transcript_echo` + hydrated eviction guard raising `ZipperEvidenceEvicted`), L148-L157
  (`_consume_frame` diverting to the echo buffer, then the lazy live-turn record) and L244-L246
  (`poll_native_continuation`'s eager gate); plus `echo_ingestion.py` L64-L66, `child_history.py`
  L67-L73 and `rebuild_coordinator.py` L159-L161. Split into two rows and made the claim name which
  flag drives which behavior, since the old one-line summary no longer mapped to one file. Also
  corrected the paragraph above the table, which still named the retired `active/projector.py`.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/conversation/projectors/__init__.py` since the L2 base commit
  is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 1 line(s) with no token
  change whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds. Noted while checking: the references table also
  cites line ranges inside `factories.py`; those ranges shifted because this task edited those
  files, so treat the cited numbers as approximate and the linked cards as authoritative.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-26T15:34 — 260718-CHATS-L7: `map_evidence_frame` gained the optional keyword-only
  `parent_thread_id` parameter — the multiplexed demux context for harnesses with
  sub-agent threads (codex/claude); pi accepts and ignores it. Sidecar: documented the seam and
  cit:([`parent_thread_id`], mcp/src/agents_remember/serving/conversation/projectors/__init__.py:46-46)
  its `None`-means-parent invariant; refreshed all line citations (protocol L24-L52, adapters
  L55-L110, registry L113-L117, lookup L120-L121) and re-pointed the projector.py flag-
  consumption citations, which the L7 multiplexed-projection rewrite had displaced
  (L176-L181/L306-L310 → L414; L556-L586; L670-L671; L945-L947). Uncommitted; closeout
  re-stamps verification.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the projector
  protocol/registry — channel flags, three per-harness bindings, fail-closed lookup. Verification
  is blank because the new source file is uncommitted; closeout owns its first source stamp.
