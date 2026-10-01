# mcp/src/agents_remember/memory_quality/curator_checklist.py

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
cit:([`report_path_for`, `split_commit_owned_findings`, `_tracked_onboarding_paths`], mcp/src/agents_remember/memory_quality/curator_checklist.py:86-88; mcp/src/agents_remember/memory_quality/curator_checklist.py:94-96; mcp/src/agents_remember/memory_quality/curator_checklist.py:99-117; mcp/src/agents_remember/memory_quality/curator_checklist.py:216-222; mcp/src/agents_remember/memory_quality/curator_checklist.py:208-214).

`write_curator_checklist` sorts repair rows, missing sidecars, stale indexes, actionable drift
candidates, closeout-owned provenance, and noteworthy report-only rows before it derives the
zeroable curator count. It writes through `atomic_write_text`, so a reader sees the previous
complete checklist or the next complete checklist, never a partial report
cit:([`write_curator_checklist`], mcp/src/agents_remember/memory_quality/curator_checklist.py:133-213).
The renderer preserves the important distinction between a zeroable pre-closeout gate and dirty
source/real-commit evidence that must remain visible until governed closeout supplies a real
commit cit:([`_render`, `_append_drift`], mcp/src/agents_remember/memory_quality/curator_checklist.py:237-307; mcp/src/agents_remember/memory_quality/curator_checklist.py:395-426).

Under CCR-R03@v1 `CuratorChecklist` now carries the exact `code_candidate_tree` and
`memory_candidate_tree`, and the attestation embeds the `memory-quality-attestation/v1` dependency
declaration built from the pair, both trees, and the rendered-report SHA-256 — so the checklist
attestation content-addresses exactly the candidate trees it inspected
cit:([`CuratorChecklist`, `write_curator_checklist`], mcp/src/agents_remember/memory_quality/curator_checklist.py:38-71; mcp/src/agents_remember/memory_quality/curator_checklist.py:133-213).

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

## 260928-MIK-L28 The "Invariants Without Proof" Section (MIK-R28 Rule 5)

`CuratorChecklist` gained one more **defaulted** input, `without_proof: WithoutProof | None = None`.
`WithoutProof` holds one row per live invariant that no proof entry names (`invariant`, `status`, `path`,
`evidenceTests`) and an optional `problem`. `_render` appends `_append_without_proof`'s section after the
`knowledgeReview` section and before the completion rule, and only when the input is not `None`.

- **Informational, never counted (architect ruling, 2026-09-29).** The section says so in its own text: the
  admission rule (MIK-R27) accepts criteria other than a proving test. It is not an input to
  `curator_actionable_count`, the attestation or the wire summary, for the same reason as the
  `knowledgeReview` section. No count field is added to the strict summary model.
- **Unconverted trees render nothing.** The controller passes `None` for every tree without the layout
  marker, so today's checklist bytes are unchanged before MIK-R37.
- Each row names the tests the invariant's recorded `origin.handoff.evidence` mentions (the migrated
  "Evidence: …" text), so the rule-6 curator pass knows where to start. A `problem` renders as an
  "Incomplete:" line, and an empty list renders `_None._`.

- The defaulted input and its rows. [1]
- The section renders only for a list, as information that moves no count. [2]
- The wire summary is identical with and without the list; an unconverted checklist has no section. [3]

## 260928-MIK-L08 The Knowledge-Worklist Section (MIK-R08 Rule 7)

`CuratorChecklist` gained two more **defaulted** inputs, `knowledge_worklist: Mapping[str, Any] | None`
and `knowledge_worklist_path: str | None`: the leaf's persisted `knowledge-worklist/v1` document and where
it lives, handed over by the memory-quality controller. `_render` appends
`memory_quality/knowledge_worklist_section.knowledge_worklist_lines` after the "without proof" section and
before the Completion Rule, and only when a worklist exists.

- **Information, not a count.** The worklist section never enters `curator_actionable_count`, the attestation or
  the wire counts; what an open item blocks is the closeout gate's (MIK-R09), live at the cutover. **Since MIK-R09
  (L09)** the field comment says how an open item does reach the count: the mandatory gate hands each one to
  `repair_findings` as one `knowledge-gate` finding (the controller's `_with_gate`), so the three-term formula and the
  single checklist are unchanged. The only change to this file is that comment.
- **Unchanged bytes for unconverted leaves.** `None` (every unconverted leaf, every production leaf before
  MIK-R37) renders nothing, so today's checklist bytes are unchanged.
- Both L28's `without_proof` and L08's worklist inputs sit on the one dataclass; the sections render in
  that order.

- The two defaulted worklist inputs and their comment, which since MIK-R09 names the gate's `knowledge-gate` findings. [4]
- The section renders only for a worklist, after the "without proof" section. [5]
- The section's lines, whose item table since MIK-R06 also renders `family_route_condition` items, and since MIK-R09 `onboarding_trace` items, through the kind-to-renderer table; its lead sentence now says the gate counts open items. [6]

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; the checklist contract is
package-owned.

No configured domain documentation could be checked.

### Repo-Internal References

The application layer decides when the report exists, and worktree cleanup owns its lifecycle.

- A leaf scope derives the report path from the contract's worktree group; only a full scoped check requests rows and writes the checklist, and since MIK-R28 it also hands the checklist the "without proof" list (`None` for an unconverted tree). [7]
- Cleanup removes the reserved reports directory before it attempts to remove the enclosure. [8]
- The checklist writer owns the enclosure report projection; deleted regression fixtures do not supply a current pass. [9]
- R03 attestation dependency declaration source. [10]

### Cross-Repo References

No cross-repository implementation owns this package-local report contract.

No meaningful cross-repo references found.

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
