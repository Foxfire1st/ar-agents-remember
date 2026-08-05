# mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

## Docs References

No Domain Documentation source is configured; the recovery contract is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The substrate recovery payload is the first content source; the journal is the fallback; the ref mint
and digest transform are the sibling authorities.

| Finding | Anchor | Source |
| --- | --- | --- |
| The assembly's source priority reads the substrate `WithdrawalRecovery` payload first. | `recovery_text` | mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:40-47 |
| The submit journal entry used as recovery source of last resort. | `JournalEntry`; `recovery_text` | mcp/src/agents_remember/serving/conversation/control/service.py:144-153; mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:40-47 |
| The attachment recovery-ref assembly mints one ref per recoverable asset through its ref-mint call. | `attachment_recovery_ref` | mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:96-123 |
| `recovery_digest` reuses the authority-parity payload digest so recovery matches the submit's idempotence digest. | `recovery_digest` | mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:50-61 |
| The lifecycle policy that consumes this assembly: `_build_withdrawn_record` calls `recovery_text`, `recovery_digest`, `recover_attachment_refs`, and `recovery_payload`. | `_build_withdrawn_record` | mcp/src/agents_remember/serving/conversation/control/withdrawals.py:442-511 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

`recover_attachment_refs` and `attachment_recovery_ref` now take one `ControlScope` (service,
authorization, session id and the **verified** bridge epoch) instead of the four parallel
arguments, and mint through `RefBinding` / `RefTarget`. The recovery payload, expiry handling and
digest behaviour are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-04T15:32:44+02:00 — 260731-EFA-L6 S18-B08 curator: rebound recovery source priority, attachment-ref assembly, and authority-parity digest reuse to their complete assembly functions.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations, all pointing four lines above their function after the signatures were wrapped multi-line: `recovery_text` L36 → L40-L47, `recovery_digest` L46 → L50-L61, `recovery_payload` L60 → L64-L77. cit:([`EMPTY_DIGEST`], mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:37-37), cit:([`recover_attachment_refs`], mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:80-93) and cit:([`attachment_recovery_ref`], mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py:96-123) were already correct and are untouched.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the cross-file citations by binding the `ar-war1.` brand and ref mint to cit:([`_PREFIX_BY_PURPOSE`, `mint_ref`], mcp/src/agents_remember/serving/conversation/control/refs.py:39-44; mcp/src/agents_remember/serving/conversation/control/refs.py:136-161), the authority-parity digest to cit:([`payload_digest`], mcp/src/agents_remember/serving/conversation/control/previews.py:28-48), and the consuming lifecycle policy to cit:([`_build_withdrawn_record`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:442-511).
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `ControlScope` / `RefBinding` / `RefTarget` call shapes; recovery payload unchanged.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the recovery assembly —
  substrate-payload-first content resolution with journal fallback, authority-parity digests, and
  one-use attachment recovery-exchange refs, extracted from `withdrawals.py`. Verification is blank
  because the new source file is uncommitted; closeout owns its first source stamp.
