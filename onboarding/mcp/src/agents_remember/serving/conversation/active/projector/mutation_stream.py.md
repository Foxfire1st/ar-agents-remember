# mcp/src/agents_remember/serving/conversation/active/projector/mutation_stream.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/mutation_stream.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Owns canonical projection mutation, event cursor minting, bounded retention, and subscriber
fan-out.

## Code Commentary

### Logic

`ProjectionMutationStream` applies mapper outputs to one `ProjectionStore`, translates store
mutations into public mutations, and mints the sequence/cursor/event-id chain. It retains at most
1,000 envelopes and gives each subscriber a 256-entry queue. A full queue is removed from normal
fan-out and receives one retained `retention-overflow` gap followed by the close sentinel; the
shared stream continues for healthy consumers.

### Conventions

Only this component increments event sequence or writes subscriber queues. Reset is for a rebuild;
release additionally discards the heavy projection while preserving the retired shell's identity.

### Invariants And Boundaries

- Event sequences and cursor predecessor links are gap-free and generation-scoped.
- A slow subscriber cannot block or terminate other subscribers.
- Overflow and explicit gaps are public mutations, retained before delivery.
- Raw mapper output never bypasses the canonical store.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Canonical item/revision behavior. | [store.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/store.py) |
| Gap and overflow regressions. | [test_conversation_active_service.py](agents-remember/mcp/tests/test_conversation_active_service.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/conversation/active/projector/mutation_stream.py` since the L2
  base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s) with
  no token change whatsoever. Checked by parsing both revisions and comparing the abstract syntax
  trees (identical) and the comment tokens (identical), so no symbol, signature, default,
  decorator, control-flow branch, docstring, or assertion this card describes has moved, and every
  claim this card makes about its own source still holds.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the mutation-stream
  sidecar and recorded its explicit retention and subscriber bounds. Verification metadata
  remains blank until commit.
