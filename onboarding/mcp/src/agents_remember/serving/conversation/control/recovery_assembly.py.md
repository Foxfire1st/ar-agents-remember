# mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py

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

cit:([`recovery_text`], mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:40-47) resolves the recovered body: the substrate `WithdrawalRecovery` payload first,
then the submit journal entry, else honest empty. cit:([`recovery_digest`], mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:50-61) computes the
authority-parity digest (via `payload_digest`, matching `EMPTY_DIGEST` L37 when empty).
cit:([`recovery_payload`], mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:64-77) assembles the `WithdrawalRecovery` wire product (text, digest,
`submittedDraftRevision`, attachment recovery refs). cit:([`recover_attachment_refs`], mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:80-93) mints one
`AttachmentRecoveryRef` per recoverable asset via cit:([`attachment_recovery_ref`], mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:96-123) — the opaque
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

## Evidence

### Docs References

No Domain Documentation source is configured; the recovery contract is repository-owned.

No configured domain documentation was available.

### Repo-Internal References

The substrate recovery payload is the first content source; the journal is the fallback; the ref mint
and digest transform are the sibling authorities.

- The assembly's source priority reads the substrate `WithdrawalRecovery` payload first. [1]
- The submit journal entry used as recovery source of last resort. [2]
- The attachment recovery-ref assembly mints one ref per recoverable asset through its ref-mint call. [3]
- `recovery_digest` reuses the authority-parity payload digest so recovery matches the submit's idempotence digest. [4]
- The lifecycle policy that consumes this assembly: `_build_withdrawn_record` calls `recovery_text`, `recovery_digest`, `recover_attachment_refs`, and `recovery_payload`. [5]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.

## 260731-EFA-L2 Current Delta

`recover_attachment_refs` and `attachment_recovery_ref` now take one `ControlScope` (service,
authorization, session id and the **verified** bridge epoch) instead of the four parallel
arguments, and mint through `RefBinding` / `RefTarget`. The recovery payload, expiry handling and
digest behaviour are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
