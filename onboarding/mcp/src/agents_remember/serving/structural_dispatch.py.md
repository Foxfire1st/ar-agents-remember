# mcp/src/agents_remember/serving/structural_dispatch.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/structural_dispatch.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T23:19+02:00 |
| lastVerifiedCommitHash | `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate | 2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Provides cross-process per-seat dispatch serialization and durable pinned-brief evidence reads.

## Code Commentary

### Logic

`exclusive_structural_dispatch_lock` hashes repository, task path, and role into one of 4,096 stable
stripes. A reclaimed process-local keyed lock composes threads, while `fcntl.flock` holds the
stripe's lazily created zero-length runtime file across spawn plus brief publication.
`pinned_dispatch_brief` finds the one exact brief for the private current occupant. The viability
and status helpers translate durable inbox state into a convergent structural result.

### Conventions

The lock identity is canonical structural identity. The hashed stripe and its runtime file are
private mechanics, not a public seat address or recovery record.

### Invariants And Boundaries

- Different canonical seats normally remain concurrent; there is no repository- or process-global lock.
- Process death releases the whole-file stripe lock; catalog and inbox evidence, not the lock
  artifact, drive recovery.
- The 4,096-stripe namespace fixes the filesystem upper bound; the process lock map contains only
  live holders/waiters and reclaims the key after they drain.
- A hash collision may serialize unrelated seats but cannot merge their durable state. Stripe files
  remain until runtime/coordination teardown because unlinking a live file could split lock generations.
- Only lock path/open/acquisition failures become `StructuralDispatchLockError`; downstream
  transaction I/O retains its own failure family. There is no fallback that would provide false
  cross-process safety.
- More than one exact-pinned brief for one generation is ambiguous and fails closed.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| One bounded process-plus-POSIX lock path linearizes only the addressed seat transaction. | `exclusive_structural_dispatch_lock` | mcp/src/agents_remember/serving/structural_dispatch.py:56-88 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pinned-brief lookup binds the inbox row to document, role, and private occupant. | `pinned_dispatch_brief` | mcp/src/agents_remember/serving/structural_dispatch.py:91-112 |
| Viability and status are derived from durable inbox state. | `dispatch_brief_viable`; `dispatch_brief_status` | mcp/src/agents_remember/serving/structural_dispatch.py:115-118; mcp/src/agents_remember/serving/structural_dispatch.py:121-129 |

## Cross-Repo References

No cross-repository dependency governs this unit.

## Update History

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — No content impact: final ARSPAWN-L2 review confirmed the bounded
  4,096-stripe serializer, live-file non-unlink rule, reclaimed process map, and narrow error
  translation already match this card. Verification remains closeout-owned.

- 2026-08-25T20:58+02:00 — ARSPAWN-L2 failure-family hardening: only lock path/open/acquisition
  failures now become `StructuralDispatchLockError`; failures raised by the protected transaction
  retain their owning subsystem's meaning. Verification remains closeout-owned.

- 2026-08-25T20:39+02:00 — ARSPAWN-L2 boundedness pass: replaced one-file-per-seat locking with
  reclaimed process-local keyed locks plus a fixed 4,096-file hash-stripe namespace. Each stripe
  uses a whole-file POSIX lock; live files are reclaimed only with runtime teardown so lock
  generations cannot split. Verification remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: created for per-canonical-seat serialization and
  durable dispatch evidence. Verification remains closeout-owned.
