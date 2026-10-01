# mcp/src/agents_remember/memory/knowledge/evidence_refusals.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The digest-versus-bytes refusal, the one comparison of a recorded value against the world outside the database. [1]
- The root-escape refusal: the path is confined by construction, so an escaping resolution indicts the root. [2]
- The accepted-origin refusal for a supporting record, naming its own table. [3]
- The shared spelling helper these factories build through, which is the only thing they import from it. [4]
- The shipped code vocabulary these three stay inside. [5]
- The shared module had already grown its own batch-scoped factory — spelled through the same `refusal` helper — which is why this file's three failures are spelled beside their own record group instead. [6]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
