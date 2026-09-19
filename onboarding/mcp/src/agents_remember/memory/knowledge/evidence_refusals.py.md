# mcp/src/agents_remember/memory/knowledge/evidence_refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/evidence_refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:15+02:00 |
| lastVerifiedCommitHash |  `562cef4ca64de5b11712d5165d24e78c9a035312`|
| lastVerifiedCommitDate |  2026-09-19T17:51:43+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l12` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The supporting records' own refusals: the three failures no earlier record group can reach. Three
factories, one per fact, each emitting a shipped code rather than widening the refusal vocabulary.

## Code Commentary

### Logic

Refusals live beside the record group that owns them rather than in one growing module, for the same reason
the row codecs and the schemas do: a refusal is a statement about *this* contract, and the shared module is
where the code, the facts and the next action are *spelled*, not where every contract's failures accumulate.

**The capacity fact that put these three here.** `memory/knowledge/refusals.py` was at **1196 lines of the
repository's 1200-line hard rail** before this leaf added a line to it, so extending it in place was not
available; splitting by protected property is the remedy the file-size rail itself asks for. This leaf added
no line to that module and its diff is empty, which is why the shared module's size is unchanged. **The next
record-group leaf cannot extend it either** and must put its own refusal factories beside its own record
group, as this one did.

Three failures, and each is a different fact:

- **A digest that does not describe the bytes** (`artifact_digest_mismatch_refusal`, `invalid_reference`).
  This is the one place a *recorded* value is compared against something outside the database, and
  `invalid_reference` is the honest code: the remedy is to correct the digest or the artifact, not to reread
  a row, and nothing stored was read to produce the refusal.
- **A resolution that leaves the declared root** (`artifact_root_escape_refusal`, `invalid_reference`). The
  recorded path is confined by construction — the vocabulary refuses an absolute, drive, UNC, backslash,
  NUL, `..` or pathspec spelling — so a resolution that escapes means the *root* is not the checkout the
  record describes.
- **Accepted origin data in a supporting record** (`evidence_promotion_not_supported_refusal`,
  `promotion_not_supported`). Persisting a claim or an observation endorses nothing, so this record group
  authors proposals and exposes no promotion. The code is the shipped one; the factory is separate because
  the offending record is a supporting record and its own table is what a caller has to look at.

### Conventions

The three factories build through the shared `refusal(...)` helper with `RefusalFacts`, so they carry the
same shape as every other refusal in the package. No new refusal code was introduced by this leaf.

### Invariants And Boundaries

- **A record-group refusal module imports the shared spelling, not the shared accumulator.** Its only
  dependency from `refusals.py` is `RefusalFacts` and `refusal`, so the shared module can be split later
  without this one changing.
- **Every code here is shipped.** `invalid_reference` and `promotion_not_supported` were both already in
  `KnowledgeRefusalCode`; this leaf widened no vocabulary.
- **A digest failure never repairs a record.** The factory reports the observed and expected facts; nothing
  in this module writes, re-pins or deletes a row.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The digest-versus-bytes refusal, the one comparison of a recorded value against the world outside the database. | `artifact_digest_mismatch_refusal` | mcp/src/agents_remember/memory/knowledge/evidence_refusals.py:31-50 |
| The root-escape refusal: the path is confined by construction, so an escaping resolution indicts the root. | `artifact_root_escape_refusal` | mcp/src/agents_remember/memory/knowledge/evidence_refusals.py:57-68 |
| The accepted-origin refusal for a supporting record, naming its own table. | `evidence_promotion_not_supported_refusal` | mcp/src/agents_remember/memory/knowledge/evidence_refusals.py:74-90 |
| The shared spelling helper these factories build through, which is the only thing they import from it. | `refusal`; `RefusalFacts` | mcp/src/agents_remember/memory/knowledge/refusals.py:57-77; mcp/src/agents_remember/memory/knowledge/refusals.py:48-54 |
| The shipped code vocabulary these three stay inside. | "KnowledgeRefusalCode = Literal[" | mcp/src/agents_remember/models/knowledge/result.py:161-161 |
| The shared module had already grown its own batch-scoped factory — spelled through the same `refusal` helper — which is why this file's three failures are spelled beside their own record group instead. | `batch_command_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:791-813 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-19T17:15+02:00 — 260915-KS-L28 curator (uncommitted change set on `ar/260915-ks-l28`, base `497d9e9f`): M1-4 anchor repair, re-read against the code worktree at `e7998504`. The shared-helper row had `refusal` and `RefusalFacts` crossed (each answered with the other's range); it now cites `refusals.py:57-77` for `refusal` and `refusals.py:48-54` for `RefusalFacts`. The capacity row named `refusal` but cited `refusals.py:791-813`, which defines `batch_command_refusal`; the anchor and its finding now name that factory and what its lines actually establish (the capacity measurement itself, 1196 of a 1200-line rail, is prose in Logic and is not a thing a `path:start-end` citation can carry). Every other row was re-checked and stands. No claim was deleted or softened. The stamp is unchanged because `9f88a6de`'s content for this file is byte-identical to `e7998504` (`git diff 9f88a6de HEAD` is empty).- 2026-09-18T12:07:24+00:00: Generated citation repair: "KnowledgeRefusalCode = Literal[" repointed to mcp/src/agents_remember/models/knowledge/result.py:161-161. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:20+02:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): created this one-to-one card for the supporting records' own refusal factories. It records the three distinct facts, the shipped codes they reuse, and the capacity fact that decided their home: the shared refusal module sits at 1196 of its 1200-line rail, so the next record-group leaf must place its factories beside its own group. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
