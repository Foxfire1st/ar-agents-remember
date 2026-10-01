# mcp/src/agents_remember/application/knowledge_proofs.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**Test proofs read back as first-class knowledge (MIK-R28 rules 4 to 6).** A test that proves an invariant is
a `proves` entry in the test file's sidecar (MIK-R21), written by the curator writer from the hand-off
(MIK-R12). This module reads those entries back from the derived index (MIK-R23) of one converted memory
tree for two consumers: `knowledge_read`'s `invariant` and `family` views, and the curator checklist's
informational "Invariants without proof" section.

## Code Commentary

### Logic

- **Views (rule 4).** `tree_view_proofs(index_path, tree_key, request)` returns `None` before opening
  anything unless the view is `invariant` or `family` (`_PROOF_VIEWS`). It then opens the index with the
  tree's key (a mismatch raises `IndexMismatchError`, which the tool turns into its ordinary refusal) and
  calls `view_proofs`.
- `view_proofs` maps the view's projected revision UUID back to `<ID>@<revision>` with `index.text_id`. The
  `invariant` view asks `proofs_of` for that one ID; the `family` view asks for every member. Each proof is
  `{id, invariant, path, anchor, facet, sidecar}` (`_proof_document`). A subject the index does not hold
  gives `None` (no proof section), which is distinct from `[]` (a subject with no proof).
- **Without proof (rules 5 and 6).** `invariants_without_proof(memory_root, *, coordination_root=None)`
  returns `None` for an unconverted tree (no layout marker). Otherwise it lists the live invariants no proof
  entry names as `UnprovenInvariant` rows inside a `ProofCoverage`. Beside each row it names the tests the
  invariant's recorded `origin.handoff.evidence` mentions (`_evidence_tests`, through
  `knowledge_writer.handoff.tests_named_in`): the migrated "Evidence: …" text (MIK-R24) that a rule-6
  curator pass turns into proofs through the writer.
- `_unproven` reads the index from the coordination index cache when a coordination root is given (keyed by
  the tree, reused when present); without one it builds a throwaway index in a temporary directory outside
  every working tree. The memory tree is only read.

### Conventions

- Naming a test is textual only; whether it resolves at C is the writer's to establish.
- A partial index sets `problem` to "the index is partial: …", so the list is never read as complete.

### Invariants And Boundaries

- **A proof never claims a pass.** Nothing here states whether a test passes, and a proof is never
  presented as the invariant being satisfied (MIK-R28 exclusions; Doc13). Test execution results are not
  stored.
- **Information, never a gate (architect ruling, 2026-09-29).** The "without proof" list feeds only the
  rendered checklist section; it never counts toward `curatorActionableCount`, the attestation or the wire
  summary. The admission rule (MIK-R27) accepts other criteria.
- **The list never breaks the run that shows it.** `MemoryTreeError`, `IndexMismatchError`, `apsw.Error` and
  `OSError` become `ProofCoverage(unproven=(), index_state="unreadable", problem=…)`.
- **Unconverted trees and database reads are unchanged.** Both entry points answer `None` for them, so
  today's installed runtime output is byte-identical before MIK-R37.

### Todos

- Rule 3 (proofs in change detection) and the stale-proof clause are not built here. By architect ruling
  (2026-09-29, option a) they move to L08 (a changed test body or a deleted test raises a worklist item for
  the proved invariant) and L03 (the stale flag on a proof whose test symbol no longer resolves), which
  carry the proof test cases.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R28@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`28_first-class-test-proofs.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The two readings and their consumers.

- The module's statement of its two consumers and the no-pass boundary. [1]
- The index is opened only for the two proof views. [2]
- A view's proofs: one invariant, or every family member; `None` for an unknown subject. [3]
- The row and coverage shapes. [4]
- The list: `None` unconverted, a problem rather than an exception, partial index named. [5]
- The cached or throwaway index. [6]
- The tests the migrated evidence names. [7]
- The view consumer, since MIK-R02 the per-page extras of a converted tree's read. [8]
- The checklist consumer. [9]
- The index lookups it reads. [10]
- Migrated evidence is listed, then a curator pass writes the proof and the list empties. [11]
- The cache is reused, and an unreadable cache is reported, not raised. [12]

### Cross-Repo References

No meaningful cross-repo references found: the module reads one memory tree, addressed explicitly by its
caller, and the coordination index cache.

No cross-repo boundary is crossed by this file.
