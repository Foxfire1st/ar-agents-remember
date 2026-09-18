# mcp/src/agents_remember/memory_quality/curator_checklist.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/curator_checklist.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:05+02:00 |
| lastVerifiedCommitHash | `9f88a6de572dc15bbed1802cf08b77c1193fb24c` |
| lastVerifiedCommitDate | 2026-09-18T14:21:49+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l16` uncommitted staged source; base `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| governingOverview | `overview.md` |

## Governing Overview

[memory quality overview](overview.md)

## Purpose

This module owns the curator's single enclosure-local memory-quality checklist. It turns the full
contract-scoped quality result, current-additions coverage, route-index preview, drift rows, and
report-only evidence into one deterministically ordered Markdown worklist that is atomically
replaced at `reports/curator-memory-quality.md`.

## Code Commentary

### Logic

`report_path_for` derives the reserved path from the worktree group. A full check separates
repairable findings from the one truthful closeout-only class: missing citation provenance on a
new, still-untracked onboarding card. It obtains the tracked set from the memory worktree rather
than treating every missing-provenance row as harmless historical debt
cit:([`report_path_for`, `split_commit_owned_findings`, `_tracked_onboarding_paths`], mcp/src/agents_remember/memory_quality/curator_checklist.py:74-76; mcp/src/agents_remember/memory_quality/curator_checklist.py:79-97; mcp/src/agents_remember/memory_quality/curator_checklist.py:196-202).

`write_curator_checklist` sorts repair rows, missing sidecars, stale indexes, actionable drift
candidates, closeout-owned provenance, and noteworthy report-only rows before it derives the
zeroable curator count. It writes through `atomic_write_text`, so a reader sees the previous
complete checklist or the next complete checklist, never a partial report
cit:([`write_curator_checklist`], mcp/src/agents_remember/memory_quality/curator_checklist.py:113-195).
The renderer preserves the important distinction between a zeroable pre-closeout gate and dirty
source/real-commit evidence that must remain visible until governed closeout supplies a real
commit cit:([`_render`, `_append_drift`], mcp/src/agents_remember/memory_quality/curator_checklist.py:204-266; mcp/src/agents_remember/memory_quality/curator_checklist.py:319-350).

Under CCR-R03@v1 `CuratorChecklist` now carries the exact `code_candidate_tree` and
`memory_candidate_tree`, and the attestation embeds the `memory-quality-attestation/v1` dependency
declaration built from the pair, both trees, and the rendered-report SHA-256 — so the checklist
attestation content-addresses exactly the candidate trees it inspected
cit:([`CuratorChecklist`, `write_curator_checklist`], mcp/src/agents_remember/memory_quality/curator_checklist.py:36-59; mcp/src/agents_remember/memory_quality/curator_checklist.py:113-195).

### Conventions

- The report filename is stable and contains no timestamp; generation time lives inside the file.
- Every list is sorted before rendering so identical inputs produce the same work order.
- Markdown cells collapse whitespace and escape table separators so finding text cannot corrupt
  the checklist layout.
- The attestation's dependency declaration is generated from the exact candidate trees and report
  digest, matching what the coherence observer re-requires.

### Invariants And Boundaries

- The checklist is operational, not onboarding, task state, or commit evidence.
- Only an untracked new card's missing provenance is closeout-owned. A tracked card with the same
  finding remains curator-actionable so historical debt cannot be hidden.
- `curatorActionableCount` is exactly repairable memory findings plus missing onboarding plus stale
  route indexes. Drift/source-change candidates remain explicit but cannot require a fabricated
  pre-commit verification stamp.
- The writer owns no quality classification, onboarding mutation, route-index mutation, or
  cleanup. It renders already-computed results and atomically publishes one file.
- The attestation binds the exact code/memory candidate trees; a changed tree produces a different
  dependency declaration and stales the attestation.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this repository; the checklist contract is
package-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The application layer decides when the report exists, and worktree cleanup owns its lifecycle.

| Finding | Anchor | Source |
| --- | --- | --- |
| A leaf scope derives the report path from the contract's worktree group; only a full scoped check requests rows and writes the checklist. | `resolve_leaf_memory_scope`; `_resolve_execution`; `_execute_memory_quality`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_scope.py:107-131; mcp/src/agents_remember/application/memory_quality/controller.py:317-337; mcp/src/agents_remember/application/memory_quality/controller.py:318-360; mcp/src/agents_remember/application/memory_quality/controller.py:363-441 |
| Cleanup removes the reserved reports directory before it attempts to remove the enclosure. | `_removed_directories` | mcp/src/agents_remember/worktrees/modules/cleanup.py:532-559 |
| The checklist writer owns the enclosure report projection; deleted regression fixtures do not supply a current pass. | `write_curator_checklist` | mcp/src/agents_remember/memory_quality/curator_checklist.py:113-195 |
| R03 attestation dependency declaration source. | `memory_quality_attestation_dependencies` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:91-129 |

## Cross-Repo References

No cross-repository implementation owns this package-local report contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260815-DAG-L3 Structured Readiness Artifact

A full contract-scoped checklist write now atomically emits `curator-memory-quality.json` beside
the Markdown report. The attestation binds schema, checklist status and counts, the exact
source-change candidate rows, onboarding/report paths, and the SHA-256 of the rendered report;
the response exposes `attestationPath`.

## MCAR-L02 Deterministic Attestation Source

The checklist renderer no longer embeds wall-clock time. Identical quality/candidate input now
reproduces identical Markdown and `ar-curator-memory-quality/v1` bytes, so a harmless rerun cannot
stale an accepted coherence generation. Changed findings or candidate tuples still change the
digest and correctly force republishing. The completion text points to the structured coherence
authority rather than a hand-authored report.

## MCAR-L03 Pair-Bound Attestation

The structured memory-quality attestation now carries the full exact pair identity, and its
generated checklist displays the contract and pair digest. The attestation therefore cannot be
reused for another valid checkout or branch pair.

## 260831-CCR-R03 Tree-Bound Attestation

The attestation now also declares the exact code/memory candidate trees it inspected, so changing
either tree stales the checklist attestation (worker handover:
notes/reports/260902-CCR-L03-worker-delivery.md).

## KS-R15@v1 Factual Knowledge-Review Section

A full contract-scoped write now renders one further **factual** section into the same artifact: the
`knowledgeReview` section `KS-R15@v1` §8.2 assigns to this leaf's sibling
`memory_quality/knowledge_review.py`. `CuratorChecklist` gained one **defaulted** input field,
`knowledge_review: tuple[AssessmentSummary, ...] = ()`, so every existing caller is unchanged and the
section renders an explicit "none recorded" state instead of an absent heading;
`_ChecklistSections.knowledge_review` carries the rendered section, and `_render` appends its lines
after the report-only findings and before the completion rule.

**The section is report-only, and this module is where that is enforced.** It is not an input to the
curator count, whose three terms are repairable findings, missing onboarding and stale route indexes
only. A subject whose assessment is unresolved, stale or partial-scope therefore changes the section's
counted limitations and changes nothing about the gate, the status line, or the arithmetic the
attestation binds. The comment beside the new field says so, and the shape of the function is what
makes it true rather than the comment.

## KS-R16@v1 The Actionability Formula Given One Name

`KS-R16@v1` §5.3 requires that the curator's actionability formula gain no fourth term, and the shipped
answer is that the formula now has exactly one definition with a name. The inline
`len(repair) + len(missing) + len(stale)` expression `write_curator_checklist` used to compute is
extracted into `curator_actionable_count(repair, missing, stale)`, and the writer's one call site now
calls it. **The value and the behaviour are unchanged** — the function is the same sum over the same
three terms, and `curator_checklist.py:134` is still the only place the count is derived. What changed is
that a second consumer can *consume* the formula instead of restating it: the family-integrity pipeline's
routing report calls this function, so the report cannot drift from the checklist it reports into, and
"gains no fourth term" is a property of one function rather than a convention each caller re-implements.
The `knowledgeReview` section remains outside it, for the same reason as before.

## Update History
- 2026-09-18T14:05+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base
  `7b1db4e0`): **re-read this card against the changed source and recorded the one-function change the
  leaf made.** The inline three-term sum became the named `curator_actionable_count` at `:100-110`, with
  `write_curator_checklist`'s single call site calling it at `:134`; the value and the behaviour are
  unchanged, and the body paragraph that quoted the inline expression now states the count by its three
  terms and by the function that defines them, so a successor reading the report-only boundary is not
  pointed at an expression the file no longer carries. Three citation ranges in the body were repointed in
  the same pass, because the new function was inserted above the writer and moved every anchor below it:
  `write_curator_checklist` is now `:113-195`. No claim was deleted or softened, and this card
  now carries a `reviewedWorkingCandidate` row naming what was actually read: the construct exists only in
  this leaf's uncommitted candidate, so closeout owns the stamp.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base
  `837961d4`): **re-read this card against the changed source and recorded the factual section the leaf
  added.** `CuratorChecklist` gained the defaulted `knowledge_review` input, `write_curator_checklist`
  renders `knowledge_review_section(...)` into the one artifact through `_ChecklistSections`, and
  `_render` appends the section's lines before the completion rule. The body states the report-only
  boundary where it is enforced — `actionable_count` remains the three-input sum and the section
  returns no count — and every reference row in this card was re-derived from the current file while
  re-reading it, because the leaf's own insertions had moved every anchor below them: `report_path_for`
  is `:74-76`, `split_commit_owned_findings` `:79-97`, `write_curator_checklist` `:100-180`,
  `_tracked_onboarding_paths` `:183-189`, `_render` `:204-266` and `_append_drift` `:319-350`. The
  generated projection bullet this card carried from 2026-09-08 is retired here, so no mechanically
  rewritten range remains recorded as unverified evidence. Verification metadata remains
  closeout-owned; no acceptance or certification claim is made.
- 2026-09-08T14:45:44+00:00: CCR-L24 preparation reviewed `CuratorChecklist` and `write_curator_checklist` against the current source; the candidate-tree attestation wording remains supported and ranges were regenerated. Verification metadata remains pinned pending final pair composition.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored the controller cells of the checklist row (resolve/execute/attach to 295-315/318-360/363-441, duplicate attach cell removed) shifted by the CCR-R08 +57-line controller insertion. Citation-only re-anchor; no content impact.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the candidate-tree fields on the checklist and the tree-bound attestation dependency declaration; prior sorting, atomic-write, and pair-binding prose preserved.

- 2026-08-29T21:46+02:00 — MCAR-L03: bound the curator worklist and structured attestation to the
  exact code/memory pair. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Removed timestamp entropy and redirected candidate disposition to the
  structured coherence authority. Verification remains closeout-owned.

- 2026-08-15T09:10+02:00 — L3 content update: documented the structured curator readiness
  attestation and rendered-report digest; verification remains closeout-owned.

- 2026-08-11T16:54+02:00 — Created for the enclosure-local, atomically overwritten curator
  memory-quality checklist and its repairable-versus-closeout-owned classification boundary.
