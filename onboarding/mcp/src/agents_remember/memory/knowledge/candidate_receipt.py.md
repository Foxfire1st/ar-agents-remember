# mcp/src/agents_remember/memory/knowledge/candidate_receipt.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Own the sealed local candidate receipt: canonical bytes, validated reads, exact admission-binding comparison and reconstruction of the recorded resolution. The receipt identifies the current candidate; ordinary open remains strict, while the separate explicit progression owner may replace its code-tree binding only after validating the exact predecessor.

## Code Commentary

### Logic

resolution_from_receipt reconstructs CandidateResolution from the receipt fields for both first-generation establishment and explicit code progression. Ordinary candidate open still compares the full sealed binding. Controlled code-only progression belongs to candidate_progression and reuses this module only to build, validate and atomically write the admitted receipt.

- `write_candidate_receipt` encodes the receipt through `canonical_json_bytes` rather than a pretty-printed dump,
  so the same receipt always has the same file content and a digest over the file is a digest over the binding
  itself; it publishes through `atomic_write_bytes`, so a reader sees the old receipt or the new one.
- `read_candidate_receipt` validates on read. A read failure, non-UTF-8/ambiguous JSON, and a receipt that does
  not seal itself all raise `KnowledgeStorageError` — a receipt that cannot be read is **not** a candidate this
  package will operate on, and the caller turns that into the `selected_input_unavailable` refusal that names the
  exact path.
- `build_receipt_for_candidate(destination, schema)` derives a receipt from the admitted resolution and the schema
  the database actually carries. It is a thin adapter over `models.knowledge.snapshot.build_candidate_receipt`, so
  there is exactly one constructor of seals.
- `receipt_binding_refusal` performs **three comparisons that answer three different questions**, and the
  distinction is the point:
  1. **against the database** — is the stored namespace the admission's? A database bound elsewhere is not a stale
     receipt but a different knowledge namespace, and answering `candidate_binding_changed` is what keeps a rebind
     from happening by accident;
  2. **against the schema generation** — was this candidate created under the generation this code declares? The
     check is the recorded **fingerprint**, because a database can pass the current table manifest while having
     been written by a different generation's rules;
  3. **against the admission** — were these the lane, the exact code and memory inputs, the snapshot/candidate/task
     references this candidate was admitted with?
- The expected binding is rebuilt through the same constructor a new candidate uses (with the receipt's own
  recorded schema generation, since that has already been verified), so the comparison cannot drift from the value
  a creation would write. `_BINDING_FIELDS` is that compared set, and `_render` names only the differing fields in
  the refusal's `expected`/`observed` so a caller is told what actually differs rather than given two full
  receipts.

### Conventions

- The expected-binding derivation deliberately reuses `build_candidate_receipt` instead of comparing fields by
  hand: a hand-written comparison is a second definition of the binding, and the two would drift.
- Refusals are **values** (`KnowledgeRefusal | None`), while unreadable/unsealable receipts are **defects** raised
  as `KnowledgeStorageError`. The caller decides which refusal vocabulary a defect maps into; this module does not
  invent one.

### Invariants And Boundaries

- **The receipt is content-addressed and validated on read.** A receipt edited in place, or written by a different
  admission, is detected and answered with a typed refusal — the working database is never re-initialized,
  repaired or partially trusted to make a later step succeed.
- **The write is atomic and canonical.** Same receipt, same bytes; the digest over the file is a digest over the
  binding.
- **Schema identity is compared by fingerprint, not by table manifest.** A generation can share a manifest and
  differ in rules.
- **Boundary.** This module owns receipt bytes and the binding comparison. It does not open a database, decide the
  candidate lifecycle, or choose a refusal code for an unreadable file.

### Todos

None recorded for this slice.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The admission-derived field set compared when a candidate is reopened. [1]
- The canonical, atomic receipt write. [2]
- The validating read that turns every failure into a defect naming the path. [3]
- The one adapter that derives a receipt from an admitted destination. [4]
- The three-comparison binding check and its refusal. [5]
- The differing-field rendering used in a refusal's facts. [6]
- The sealed receipt model and its read-time seal validator. [7]
- The canonical encoder and the atomic publisher this module writes through. [8]
- The refusal this module returns for a receipt that is not this admission's. [9]
- The lifecycle caller that reads both candidate inputs before anything else. [10]
- The schema identity the fingerprint comparison is made against. [11]
- The node that proves a candidate the admission cannot verify is refused with its bytes intact. [12]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
