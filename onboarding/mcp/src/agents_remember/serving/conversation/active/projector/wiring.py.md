# mcp/src/agents_remember/serving/conversation/active/projector/wiring.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/wiring.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-31 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[projector overview](overview.md)

## Purpose

Holds the two bundles every component of one session's projection is built from. New at
260731-EFA-L2.

An active-session projection is a small component graph — native-evidence ingestion, echo ingestion,
child-history hydration, interaction projection, a rebuild coordinator — and all of it projects
**exactly one session at exactly one bridge epoch**. That invariant is what these two objects make
structural: every component receives the same spine and the same readers, so no component can end up
ingesting one session's evidence into another session's stream.

## Code Commentary

### `BridgeReaders` — the whole read surface, chosen as a set

A frozen dataclass of five callables, each defaulting to the real control-bridge read:

| field | default |
| --- | --- |
| `evidence` | `read_control_evidence` |
| `native_page` | `read_control_native_page` |
| `transcript` | `read_control_transcript` |
| `provenance` | `read_submission_provenance` |
| `snapshot` | `read_control_snapshot` |

`LIVE_BRIDGE_READERS = BridgeReaders()` is the production value — every one of them goes to the real
control bridge.

They are **one substitution**. A test (or replay harness) that fakes the evidence reader while
leaving the transcript reader live is reading two different sessions and will happily project the
interleaving. Substitute the set, never a single field.

### `SessionProjectionSpine` — the machinery one session's components share

A frozen dataclass carrying everything the ingestion components of ONE projection must agree on:

- `identity: ActiveConversationRef` and `entry: ControlledSession` — *what* is being projected.
- `mapper: HarnessProjector` — how that harness's shapes are read.
- `stream: ProjectionMutationStream` — the single place mutations are published.
- `agents: AgentAuthority` and `refs: ProjectionEvidenceRefs` — the identity and reference minting
  every component must agree on.
- `apply_lock: asyncio.Lock` — serializes them.
- `clock: Callable[[], str]` — stamps them.

Two derived properties keep the rooting rules in one place: `parent_thread_id` (the vendor
conversation this projection is rooted at, which child threads hang off — i.e.
`identity.vendor_conversation_id`) and `bridge_epoch` (`identity.bridge_epoch`).

Handing each component the same spine is what makes "one projection"
checkable rather than a convention repeated across five parameter lists.

### Invariants And Boundaries

- One spine per projection. A component constructed with a different spine — or with a spine whose
  identity/epoch does not match its siblings' — breaks the invariant this module exists to encode.
- `BridgeReaders` is substituted whole. Partial substitution is the failure mode the docstring calls
  out by name.
- Type-only imports (`ActiveConversationRef`, `HarnessProjector`, `ControlledSession`,
  `AgentAuthority`, `ProjectionMutationStream`, `ProjectionEvidenceRefs`) live under
  `TYPE_CHECKING`; this module holds no behaviour beyond the two properties.

## Docs References

No domain documentation source is configured for this repository.

## Repo-Internal References

- [facade.py](facade.py.md) assembles the spine and readers and hands them to the components.
- [native_ingestion.py](native_ingestion.py.md), [echo_ingestion.py](echo_ingestion.py.md),
  [child_history.py](child_history.py.md), [rebuild_coordinator.py](rebuild_coordinator.py.md) each
  take the spine instead of re-listing its fields.
- [harness_control_client.py](../../../harness_control_client.py.md) owns the five live reads.

## Cross-Repo References

No meaningful cross-repo references.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: created for the new module. Verification metadata stays
  pinned to the pre-commit source history until closeout.
