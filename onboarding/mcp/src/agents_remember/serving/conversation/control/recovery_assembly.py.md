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

`recovery_text` (L40-L47) resolves the recovered body: the substrate `WithdrawalRecovery` payload first,
then the submit journal entry, else honest empty. `recovery_digest` (L50-L61) computes the
authority-parity digest (via `payload_digest`, matching `EMPTY_DIGEST` L37 when empty).
`recovery_payload` (L64-L77) assembles the `WithdrawalRecovery` wire product (text, digest,
`submittedDraftRevision`, attachment recovery refs). `recover_attachment_refs` (L80) mints one
`AttachmentRecoveryRef` per recoverable asset via `attachment_recovery_ref` (L96) — the opaque
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
| The `ar-war1.` recovery-asset brand and the purpose-branded `mint_ref` this assembly calls. | L14; L37-L44; L136-L161 | [refs.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/refs.py) |
| The authority-parity content digest (`payload_digest`) that `recovery_digest` reuses so recovery matches the submit's idempotence digest. | L28-L48 | [previews.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/previews.py) |
| The lifecycle policy that consumes this assembly: `_build_withdrawn_record` calls `recovery_text`, `recovery_digest`, `recover_attachment_refs`, and `recovery_payload`. | L442-L511 | [withdrawals.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/withdrawals.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

`recover_attachment_refs` and `attachment_recovery_ref` now take one `ControlScope` (service,
authorization, session id and the **verified** bridge epoch) instead of the four parallel
arguments, and mint through `RefBinding` / `RefTarget`. The recovery payload, expiry handling and
digest behaviour are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations, all pointing four lines above their function after the signatures were wrapped multi-line: `recovery_text` L36 → L40-L47, `recovery_digest` L46 → L50-L61, `recovery_payload` L60 → L64-L77. `EMPTY_DIGEST` (L37), `recover_attachment_refs` (L80) and `attachment_recovery_ref` (L96) were already correct and are untouched.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations. `refs.py` is 246 lines, so the old L28-L204 was the whole module: narrowed to the `ar-war1.` brand (L14, `_PREFIX_BY_PURPOSE` L37-L44) and `mint_ref` (L136-L161), and split the authority-parity digest out into its real home, `previews.py` `payload_digest` L28-L48. Re-anchored the consuming lifecycle policy to `withdrawals.py` `_build_withdrawn_record` L442-L511 (was L455-L538), verified by the four `recovery_assembly.*` calls at L454, L456, L465, and L490.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `ControlScope` / `RefBinding` / `RefTarget` call shapes; recovery payload unchanged.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the recovery assembly —
  substrate-payload-first content resolution with journal fallback, authority-parity digests, and
  one-use attachment recovery-exchange refs, extracted from `withdrawals.py`. Verification is blank
  because the new source file is uncommitted; closeout owns its first source stamp.
