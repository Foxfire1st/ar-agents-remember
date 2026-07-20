# mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

R3's recovery assembly: the exact body a successful withdrawal retains. Pure assembly over the
bounded retention record — the substrate's pre-tombstone payload first, this authority's submit
journal as the source of last resort, and the authority-parity content digest — plus the opaque
one-use attachment recovery-exchange refs with full alt provenance. The lifecycle policy lives in
`withdrawals.py`.

## Code Commentary

### Logic

`recovery_text` (L36) resolves the recovered body: the substrate `WithdrawalRecovery` payload first,
then the submit journal entry, else honest empty. `recovery_digest` (L46) computes the
authority-parity digest (via `payload_digest`, matching `EMPTY_DIGEST` L33 when empty).
`recovery_payload` (L60) assembles the `WithdrawalRecovery` wire product (text, digest,
`submittedDraftRevision`, attachment recovery refs). `recover_attachment_refs` (L76) mints one
`AttachmentRecoveryRef` per recoverable asset via `attachment_recovery_ref` (L98) — the opaque
`ar-war1.` exchange identity carrying alt provenance but no content.

### Conventions

Everything here is pure assembly over the retention record; it decides nothing about lease timing or
disposal. Content resolution is substrate-payload-first, journal-of-last-resort, and never
fabricated.

### Invariants And Boundaries

- Recovery content comes from the substrate payload or the journal; without either it is honestly
  empty, never invented.
- The recovery digest is authority-parity (equal to the submit's idempotence digest for the same
  content).
- Attachment recovery refs are opaque one-use exchange identities with alt provenance; they carry no
  bytes.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the recovery contract is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The substrate recovery payload is the first content source; the journal is the fallback; the ref mint
and digest transform are the sibling authorities.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The substrate `WithdrawalRecovery` pre-tombstone payload this assembly reads first. | L1-L120 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The submit journal entry used as recovery source of last resort. | L135-L166 | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/service.py) |
| The `ar-war1.` recovery-asset ref mint and the authority-parity digest. | L28-L204 | [refs.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/refs.py) |
| The lifecycle policy that consumes this assembly. | L455-L538 | [withdrawals.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/withdrawals.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the recovery assembly —
  substrate-payload-first content resolution with journal fallback, authority-parity digests, and
  one-use attachment recovery-exchange refs, extracted from `withdrawals.py`. Verification is blank
  because the new source file is uncommitted; closeout owns its first source stamp.
