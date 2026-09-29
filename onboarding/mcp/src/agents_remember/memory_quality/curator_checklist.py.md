# mcp/src/agents_remember/memory_quality/curator_checklist.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/curator_checklist.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T01:22:26+02:00 |
| lastVerifiedCommitHash | `7127756cd132d1103cd0a24bc7dc6884ddb663ee` |
| lastVerifiedCommitDate | 2026-09-30T01:41:06+02:00|
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
cit:([`report_path_for`, `split_commit_owned_findings`, `_tracked_onboarding_paths`], mcp/src/agents_remember/memory_quality/curator_checklist.py:86-88; mcp/src/agents_remember/memory_quality/curator_checklist.py:93-95; mcp/src/agents_remember/memory_quality/curator_checklist.py:98-116; mcp/src/agents_remember/memory_quality/curator_checklist.py:215-221; mcp/src/agents_remember/memory_quality/curator_checklist.py:208-214).

`write_curator_checklist` sorts repair rows, missing sidecars, stale indexes, actionable drift
candidates, closeout-owned provenance, and noteworthy report-only rows before it derives the
zeroable curator count. It writes through `atomic_write_text`, so a reader sees the previous
complete checklist or the next complete checklist, never a partial report
cit:([`write_curator_checklist`], mcp/src/agents_remember/memory_quality/curator_checklist.py:132-212).
The renderer preserves the important distinction between a zeroable pre-closeout gate and dirty
source/real-commit evidence that must remain visible until governed closeout supplies a real
commit cit:([`_render`, `_append_drift`], mcp/src/agents_remember/memory_quality/curator_checklist.py:236-306; mcp/src/agents_remember/memory_quality/curator_checklist.py:394-425).

Under CCR-R03@v1 `CuratorChecklist` now carries the exact `code_candidate_tree` and
`memory_candidate_tree`, and the attestation embeds the `memory-quality-attestation/v1` dependency
declaration built from the pair, both trees, and the rendered-report SHA-256 — so the checklist
attestation content-addresses exactly the candidate trees it inspected
cit:([`CuratorChecklist`, `write_curator_checklist`], mcp/src/agents_remember/memory_quality/curator_checklist.py:38-70; mcp/src/agents_remember/memory_quality/curator_checklist.py:132-212).

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The defaulted input and its rows. | `without_proof`; `WithoutProof` | mcp/src/agents_remember/memory_quality/curator_checklist.py:65-65; mcp/src/agents_remember/memory_quality/curator_checklist.py:73-78 |
| The section renders only for a list, as information that moves no count. | `_render`; `_append_without_proof`; "Information, not a gate (MIK-R28 rule 5)" | mcp/src/agents_remember/memory_quality/curator_checklist.py:236-306; mcp/src/agents_remember/memory_quality/curator_checklist.py:354-386 |
| The wire summary is identical with and without the list; an unconverted checklist has no section. | `test_the_checklist_shows_the_list_as_information_that_moves_no_count` | mcp/tests/test_knowledge_proofs.py:398-426 |

## 260928-MIK-L08 The Knowledge-Worklist Section (MIK-R08 Rule 7)

`CuratorChecklist` gained two more **defaulted** inputs, `knowledge_worklist: Mapping[str, Any] | None`
and `knowledge_worklist_path: str | None`: the leaf's persisted `knowledge-worklist/v1` document and where
it lives, handed over by the memory-quality controller. `_render` appends
`memory_quality/knowledge_worklist_section.knowledge_worklist_lines` after the "without proof" section and
before the Completion Rule, and only when a worklist exists.

- **Information, not a count.** The worklist never enters `curator_actionable_count`, the attestation or
  the wire counts; what an open item blocks is the closeout gate's (MIK-R09), live at the cutover.
- **Unchanged bytes for unconverted leaves.** `None` (every unconverted leaf, every production leaf before
  MIK-R37) renders nothing, so today's checklist bytes are unchanged.
- Both L28's `without_proof` and L08's worklist inputs sit on the one dataclass; the sections render in
  that order.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two defaulted worklist inputs and their comment. | `knowledge_worklist`; `knowledge_worklist_path` | mcp/src/agents_remember/memory_quality/curator_checklist.py:69-70 |
| The section renders only for a worklist, after the "without proof" section. | `_render`; `knowledge_worklist_lines` | mcp/src/agents_remember/memory_quality/curator_checklist.py:236-306 |
| The section's lines, whose item table since MIK-R06 also renders `family_route_condition` items through the kind-to-renderer table. | `knowledge_worklist_lines` | mcp/src/agents_remember/memory_quality/knowledge_worklist_section.py:161-209 |

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
| A leaf scope derives the report path from the contract's worktree group; only a full scoped check requests rows and writes the checklist, and since MIK-R28 it also hands the checklist the "without proof" list (`None` for an unconverted tree). | `resolve_leaf_memory_scope`; `_resolve_execution`; `_execute_memory_quality`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_scope.py:145-169; mcp/src/agents_remember/application/memory_quality/controller.py:369-389; mcp/src/agents_remember/application/memory_quality/controller.py:392-466; mcp/src/agents_remember/application/memory_quality/controller.py:516-680 |
| Cleanup removes the reserved reports directory before it attempts to remove the enclosure. | `_removed_directories` | mcp/src/agents_remember/worktrees/modules/cleanup.py:558-593 |
| The checklist writer owns the enclosure report projection; deleted regression fixtures do not supply a current pass. | `write_curator_checklist` | mcp/src/agents_remember/memory_quality/curator_checklist.py:132-212 |
| R03 attestation dependency declaration source. | `memory_quality_attestation_dependencies` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:112-149 |

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
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): **reopened claim re-read and reworded.** The row "The section's lines" (`knowledge_worklist_lines`) was reopened because the function changed structurally (MIK-R06: `family_route_condition` rows; MIK-R11: the Plan column). Its cited range was already stale at the base (`74-121`, from before L11). I re-read the function at `knowledge_worklist_section.py:161-209`, where it is defined; the claim is about that construct, so the range is re-cited there by reading, not by projection, and the claim is reworded to say what the table now renders. The fixer's generated bullet for this row was removed, because the claim was reworded. The fixer also normalised the `without_proof` row to `65-65` (the anchor's line); no claim there changed. No verification stamp was advanced.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): Added the section "260928-MIK-L08 The Knowledge-Worklist Section (MIK-R08 Rule 7)": the defaulted `knowledge_worklist` and `knowledge_worklist_path` inputs, rendered by `knowledge_worklist_lines` after the "without proof" section only when a worklist exists, never counted.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): Added the section "260928-MIK-L28 The "Invariants Without Proof" Section": the defaulted `without_proof` input, `WithoutProof` and `_append_without_proof`, with the architect ruling that the list is checklist-only and informational and never counts toward `curatorActionableCount`. Three cited rows. The reopened row about `_attach_curator_checklist` was re-read against the working tree: it still holds, and it now also states that the controller hands the checklist the list (`None` for an unconverted tree). The body's prose citations and the table rows moved by the new dataclass and section were re-pointed by the installed `memory-citations --fix` and the exact base-to-working line map; I also removed a stale second `_append_drift` range (`:332-363`) that the fixer had left beside the re-pointed `:381-412`. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`controller.py`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.

- 2026-09-27T05:30:43+00:00 — Authored scoped citation maintenance for 1 L41 source-range projection(s) resolved by the frozen source index. Only changed-source ranges were adopted from the preview; unrelated ranges, generated history and verification stamps are preserved.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-18T20:45:18+02:00 — 260915-KS-L23 post-closeout clearance (change set on `ar/260915-ks-l23`, memory base `ce3028e9`, code `5e4eb651`): **re-read the reopened claim at :91 and advanced the verification stamp.** The row's `citation_claim_reopened` finding held that its evidence changed after verification — ``write_curator_checklist`` changed structurally from code commit `9f88a6de572dc15bbed1802cf08b77c1193fb24c` to the working tree — and that only a re-read plus a stamp advance clears it; a citation edit cannot. The wording is retained because it still holds against `5e4eb651`: the function is still declared at :113, still replaces the deterministic checklist and its attestation atomically (the enclosure report projection), and still returns the compact wire summary whose `curatorActionableCount` is `curator_actionable_count(repair, missing, stale)` — commit-owned and report-only findings stay outside the actionable arithmetic. The citation is current: `write_curator_checklist` is declared at :113 inside the cited 113-195. No claim, Anchor cell or range was re-worded or dropped; `lastVerifiedCommitHash` advanced to `5e4eb651be0691e2d2a90ea59bc662f92050db25` and `lastVerifiedCommitDate` to `2026-09-18T20:45:18+02:00` — the committed (code, memory) pair that now carries these bytes.
- 2026-09-18T14:05+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base
  `7b1db4e0`): **re-read this card against the changed source and recorded the one-function change the
  leaf made.** The inline three-term sum became the named `curator_actionable_count` at `:100-110`, with
  `write_curator_checklist`'s single call site calling it at `:134`; the value and the behaviour are
  unchanged, and the body paragraph that quoted the inline expression now states the count by its three
  terms and by the function that defines them, so a successor reading the report-only boundary is not
  pointed at an expression the file no longer carries. Three citation ranges in the body were repointed in
  the same pass, because the new function was inserted above the writer and moved every anchor below it:
  `write_curator_checklist` is now `:113-195`. No claim was deleted or softened, and this card
  now carries a recorded working candidate naming what was actually read: the construct exists only in
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
