# mcp/src/agents_remember/application/knowledge_proofs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_proofs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash | `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate | 2026-09-29T18:13:06+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R28@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`28_first-class-test-proofs.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The two readings and their consumers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's statement of its two consumers and the no-pass boundary. | "nothing here states whether the test passes" | mcp/src/agents_remember/application/knowledge_proofs.py:1-22 |
| The index is opened only for the two proof views. | `tree_view_proofs`; `_PROOF_VIEWS` | mcp/src/agents_remember/application/knowledge_proofs.py:57-57; mcp/src/agents_remember/application/knowledge_proofs.py:69-87 |
| A view's proofs: one invariant, or every family member; `None` for an unknown subject. | `view_proofs`; `_proof_document` | mcp/src/agents_remember/application/knowledge_proofs.py:90-116; mcp/src/agents_remember/application/knowledge_proofs.py:119-127 |
| The row and coverage shapes. | `UnprovenInvariant`; `ProofCoverage` | mcp/src/agents_remember/application/knowledge_proofs.py:130-145; mcp/src/agents_remember/application/knowledge_proofs.py:148-154 |
| The list: `None` unconverted, a problem rather than an exception, partial index named. | `invariants_without_proof` | mcp/src/agents_remember/application/knowledge_proofs.py:157-190 |
| The cached or throwaway index. | `_unproven`; `KnowledgeIndexCache` | mcp/src/agents_remember/application/knowledge_proofs.py:193-203 |
| The tests the migrated evidence names. | `_evidence_tests`; `tests_named_in` | mcp/src/agents_remember/application/knowledge_proofs.py:206-213 |
| The view consumer. | `_read_result`; `tree_view_proofs` | mcp/src/agents_remember/mcp/tools/knowledge.py:361-445 |
| The checklist consumer. | `_without_proof`; `invariants_without_proof` | mcp/src/agents_remember/application/memory_quality/controller.py:695-706 |
| The index lookups it reads. | `proofs_of`; `invariants_without_proof` | mcp/src/agents_remember/memory/knowledge_index/query.py:260-268; mcp/src/agents_remember/memory/knowledge_index/query.py:270-282 |
| Migrated evidence is listed, then a curator pass writes the proof and the list empties. | `test_migrated_evidence_is_listed_then_turned_into_a_proof_by_a_curator_pass` | mcp/tests/test_knowledge_proofs.py:429-466 |
| The cache is reused, and an unreadable cache is reported, not raised. | `test_the_list_reuses_the_cached_index_and_reports_an_unreadable_one` | mcp/tests/test_knowledge_proofs.py:469-485 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads one memory tree, addressed explicitly by its
caller, and the coordination index cache.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R08 moved lines in `controller.py`, `knowledge.py`, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). No claim, anchor or source file of this card changed.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): created this card for the new file MIK-R28 adds. It records the architect rulings of 2026-09-29: the optional `proofs` field on `knowledge_read` is accepted, the "without proof" list is checklist-only and informational, and rule 3 and the stale-proof clause move to L08 and L03 (Todos). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
