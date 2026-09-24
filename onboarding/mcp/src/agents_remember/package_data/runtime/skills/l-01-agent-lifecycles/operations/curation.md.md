# operations/curation.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/curation.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-21T18:09+02:00 |
| lastVerifiedCommitHash | `86639933d61528387ce106dbd4d7a334bd468671` |
| lastVerifiedCommitDate | 2026-09-24T18:51:31+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The leaf coherence pass — reconciling intended, current, and implemented meaning and writing the affected onboarding.

Every operation block shares one five-part shape — who carries it, required inputs, normal workflow, authority gates, failure handling, and handoff/exit — which is what makes a long procedure separately loadable instead of padding every role file.

## Code Commentary

### Logic

`## Who carries it, and their job` separates two disjoint jobs in one table: the curator reconciles and
writes memory, the manager compiles the brief and owns the transaction. `## Normal workflow` step 5 is the complete curation check set rather than a named scoped check: the
curator runs the full `memory_quality_check` operation for the leaf, repairs or escalates every
curator-actionable finding with its exact returned code, and re-runs it after every repair until
`curatorActionableCount=0` and the **raw** `qualityChecklistStatus=ready-for-closeout`, publishing the `curator_coherence`
authority when the **combined** `checklistStatus` is rewritten to `coherence-required` — which happens
**only when the coherence record is then missing or stale**, the coherence gate. On the success path,
where the record is already current, the combined field is **not rewritten** and keeps its incoming
`ready-for-closeout` value with `closeoutReady=true`. **Field-name
correction (`D35`, made by 260915-CAPS-L10):** the sentence above previously named
`checklistStatus=ready-for-closeout` as the loop's termination condition; read
the raw field to end the loop and the combined field to decide the coherence gate
(`application/memory_quality/controller.py:664`, `:671`, `:678`, `:685-687`).

**Warrant corrected by `CAPS-R19` (leaf `260915-CAPS-L19`).** The `D35` correction above originally rested
on the sentence *"`ready-for-closeout` is never a value of the combined field."* That absolute claim is
**literally false**, and `CAPS-R19`'s revision note records it as superseded by the three-path model now
stated here. The field-name correction it supported still holds; only its stated warrant was wrong.
**Attribution is complementary and both halves hold:** `260915-CAPS-L10`'s curator corrected the
**onboarding cards** that carried the wrong form, while `CAPS-R19` corrected the **shipped sources** — the
five loop-gate carriers, their nine generated copies, and the guard registry's own docstring — and brought
`docs/reference/mcp-tools.md` into both the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`.
`## Authority gates` states the same rule
from the other side: the completed curation is the prerequisite the transaction carries, and a subset
result never stands in for the full operation.

`## Required inputs` states the
three fed inputs (the landed change set with counters and paths pulled from the leaf contract's recorded
range; the leaf task doc with its approved requirement-corpus ruling and version-addressed packets; and
`notes/` with the builder turn report plus the candidate-bound route-review verdict only when review was
requested) and records the rule that none of them is inferred from transcript memory. Since
`260921-ICR-L20` (`ICR-R20@v1`) that section also names the repository's **published dataset** — the one
declared location the ordinary read route selects, which the knowledge hand-off is published to and the
next task's planner reads. The block also
carries the curator's own prohibitions — never runs the closeout preview, never repairs transaction
conflicts, never decides whether a leaf lands — and the routing rule that rejects overview-dumping and
task-log-dumping alike.

**The authoring step this leaf added is a procedure step, not a new authority.** `## Normal workflow`
gained a third numbered step that routes the reconciliation's *requirement-shaped items* — authored
knowledge, not onboarding prose — through the real writer with the ordinary route's invocation
(`agents-remember knowledge-ingest … --baseline … --publish --commit --json`), and states the discipline
the whole route exists for: **consume the report, not the exit status.** Every entry appears in exactly
one of `committed` / `rulings` / `refused` with its own reason, `publicationRoute` names the destination
selected or that none was, `publishedIdentity` reports what an independent read of that location found
(`confirmed` / `mismatch` / `unavailable`), and a refused publication establishes nothing. `## Authority
gates` gained the matching rule from the other side — the batch and its publication keep their existing
owners, `--commit` is the knowledge-batch write word and not a Git action or an acceptance, and the
mounted `knowledge_change` tool refuses every kind and only names the real entry point — and `## Failure
handling` gained the one that keeps a partial hand-off visible: a run whose entries split across
`committed` and `refused`, or whose publication the owner refused, names each outcome and manufactures no
full completion, with an exact retry as the recovery. `## Handoff / exit` now carries the published
dataset identity as well, because it is what the next task's planner reads.

### Conventions

The strict 1-to-1 source mapping, governing-overview links, and metadata rules live in the `c-05-create-or-update-onboarding-files` skill, not here.

### Invariants And Boundaries

- An operation block holds procedure only; a rule that applies across roles belongs in `core/`.
- A role file names the operation it selects; it does not restate the procedure.
- The operation vocabulary is closed at eight names, so an unknown operation is an explicit error rather than a silent fallback.
- Authority gates and failure handling stay inside this block, not in the role that triggers it.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The operation block's declared purpose, source path, and applicable roles. | `"operations"`; `"purpose"`; `"applies_to_roles"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-1; skills/l-01-agent-lifecycles/composition-manifest.json:45-45; skills/l-01-agent-lifecycles/composition-manifest.json:47-47; skills/l-01-agent-lifecycles/composition-manifest.json:63-63; skills/l-01-agent-lifecycles/composition-manifest.json:73-73; skills/l-01-agent-lifecycles/composition-manifest.json:80-80; skills/l-01-agent-lifecycles/composition-manifest.json:90-90; skills/l-01-agent-lifecycles/composition-manifest.json:98-98; skills/l-01-agent-lifecycles/composition-manifest.json:107-107; skills/l-01-agent-lifecycles/composition-manifest.json:115-115; skills/l-01-agent-lifecycles/composition-manifest.json:128-128; skills/l-01-agent-lifecycles/composition-manifest.json:185-185; skills/l-01-agent-lifecycles/composition-manifest.json:223-223; skills/l-01-agent-lifecycles/composition-manifest.json:261-261; skills/l-01-agent-lifecycles/composition-manifest.json:289-289; skills/l-01-agent-lifecycles/composition-manifest.json:324-324; skills/l-01-agent-lifecycles/composition-manifest.json:366-366; skills/l-01-agent-lifecycles/composition-manifest.json:397-397; skills/l-01-agent-lifecycles/composition-manifest.json:429-429; skills/l-01-agent-lifecycles/composition-manifest.json:463-463; skills/l-01-agent-lifecycles/composition-manifest.json:489-489; skills/l-01-agent-lifecycles/composition-manifest.json:512-512; skills/l-01-agent-lifecycles/composition-manifest.json:539-539; skills/l-01-agent-lifecycles/composition-manifest.json:48-48; skills/l-01-agent-lifecycles/composition-manifest.json:64-64; skills/l-01-agent-lifecycles/composition-manifest.json:74-74; skills/l-01-agent-lifecycles/composition-manifest.json:81-81; skills/l-01-agent-lifecycles/composition-manifest.json:91-91; skills/l-01-agent-lifecycles/composition-manifest.json:99-99; skills/l-01-agent-lifecycles/composition-manifest.json:108-108; skills/l-01-agent-lifecycles/composition-manifest.json:116-116; skills/l-01-agent-lifecycles/composition-manifest.json:129-129; skills/l-01-agent-lifecycles/composition-manifest.json:138-138; skills/l-01-agent-lifecycles/composition-manifest.json:142-142; skills/l-01-agent-lifecycles/composition-manifest.json:146-146; skills/l-01-agent-lifecycles/composition-manifest.json:150-150; skills/l-01-agent-lifecycles/composition-manifest.json:154-154; skills/l-01-agent-lifecycles/composition-manifest.json:158-158; skills/l-01-agent-lifecycles/composition-manifest.json:49-49; skills/l-01-agent-lifecycles/composition-manifest.json:65-65; skills/l-01-agent-lifecycles/composition-manifest.json:75-75; skills/l-01-agent-lifecycles/composition-manifest.json:82-82; skills/l-01-agent-lifecycles/composition-manifest.json:92-92; skills/l-01-agent-lifecycles/composition-manifest.json:100-100; skills/l-01-agent-lifecycles/composition-manifest.json:109-109; skills/l-01-agent-lifecycles/composition-manifest.json:117-117; skills/l-01-agent-lifecycles/composition-manifest.json:130-130 |
| The manifest keeps the operation vocabulary at exactly these eight names. | `OPERATION_KEYS`; `test_manifest_resolves_every_role_and_operation_source` | mcp/tests/test_role_instruction_corpus.py:56-64; mcp/tests/test_role_instruction_corpus.py:199-225; mcp/tests/test_role_instruction_corpus.py:66-66; mcp/tests/test_role_instruction_corpus.py:177-177; mcp/tests/test_role_instruction_corpus.py:180-180; mcp/tests/test_role_instruction_corpus.py:253-253 |
| The canonical source of this block. | `# Operation` | skills/l-01-agent-lifecycles/operations/curation.md:1-1 |
| **The authoring step this leaf added to the block: the real invocation, the report fields to consume, and the rule that a partial hand-off stays partial.** | "Route the durable knowledge through the real writer, and publish it."; "Consume the report, not the exit status"; "A partial or refused knowledge hand-off stays partial." | skills/l-01-agent-lifecycles/operations/curation.md:60-71; skills/l-01-agent-lifecycles/operations/curation.md:141-160 |
| **The authority gate that keeps the batch and its publication with their existing owners, and the published dataset the required-inputs section now names.** | "The knowledge batch and its publication keep their existing owners."; "repository's published dataset" | skills/l-01-agent-lifecycles/operations/curation.md:105-124; skills/l-01-agent-lifecycles/operations/curation.md:33-34 |
| The handoff paragraph that now carries the published identity, and the write plane it names. | "knowledge hand-off result"; `ingest_curator_list` | skills/l-01-agent-lifecycles/operations/curation.md:155-174; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1082-1215 |
| The publication owner whose result the step reads back, and the declared location it publishes to. | `declared_publication_location`; `published_identity_read_back` | mcp/src/agents_remember/application/knowledge_publication_route.py:115-132; mcp/src/agents_remember/application/knowledge_publication_route.py:202-250 |
| This card documents the **generated packaged copy**; the canonical source it mirrors is the root `skills/` tree, and the copy is produced by `scripts/sync-skills.py` and never hand-edited. | `# Operation` | skills/l-01-agent-lifecycles/operations/curation.md:1-1; scripts/sync-skills.py:1-60 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260921-ICR-L28 The Curator's Family Plane And External Sources Join The Reconciliation Pass

`260921-ICR-L28` (`ICR-R28@v2`) adds one numbered step to the canonical `operations/curation.md` and
therefore to this packaged copy: the pass now **examines family coverage and authors it as part of the
same list**, and declares every external source it inspected. Three of its rules are the ones a curator
is most likely to get wrong, and each is stated as a distinction rather than a preference:

- an obligation the pass did not examine is left **without** either key, so the run reports it as
  **unexamined** rather than as family-free — the two are different facts and lead to opposite actions;
- nothing is grouped by directory, route, label or shared anchor, so a family exists only where the
  curator declared one, and `basis` is required wherever the curator decides;
- a member or membership change **prompts a fresh look** at the affected recorded guarantee, with a
  successor revision authored only where that is justified and the earlier revision and its memberships
  preserved exactly as recorded.

**The external-source rule is stated where it is most easily got wrong**: an external document is
declared with its document identity, its version or retrieval time, the digest of what was inspected
when one was taken, and the location read; the run retains it in a bounded manifest and binds the
authored records' origin references to it, so a document is **never** misrepresented as a repository
path with a Git blob. The pass then reads both planes back from the report — `family` and `sources`,
each with its own state — and carries that coverage into the handoff, because a plane whose state is
not `recorded` measured nothing and its null counts are not zeroes.

**This copy is generated.** The step was written in `skills/l-01-agent-lifecycles/operations/curation.md`
and propagated here by `scripts/sync-skills.py`; nothing in this file is edited by hand.

## 260921-ICR-L27 The Repository-Foundation Entry Gets Its Own Section And Its Own Carrier

`260921-ICR-L27` (`ICR-R27@v1`) adds *The repository-foundation entry — the curator's work, before a leaf
exists* to this operation: curation's second, bounded entry, selected when the scope is the repository's
foundation rather than one leaf's delta, with `c-14-knowledge-bootstrap` as its procedure. The ownership
is identical on both entries — the reconciliation and the authored knowledge belong to this seat, and
there is still exactly one admitted writer and one declared published location — so the section's
comparison table separates them by **carrier, scope, required inputs, writer entry, onboarding and
missing inputs** rather than by owner.

The carrier row is the load-bearing one, and `260921-ICR-L32` changed what it says: the leaf entry is
this seat opened on the leaf's task document; the foundation entry is **a taskless curator session**,
which the developer's 2026-09-24 ruling admitted to the taskless seat roles and which authors under this
role's own rules — and it can also be reached through the taskless **bootstrap** seat for the
read-and-report step, or an instructed session holding the procedure for a taskless run. Every other role
is still refused (`400 task-binding-required`, "named role scope is required"). The writer row names both
entries and the enclosure the taskless one refuses (`enclosure_in_scope`, so a bootstrap can never
publish onto a task's line), and the section keeps the rule that **neither entry substitutes for the
other** and that no leaf, worktree, enclosure or task document is ever fabricated to give the foundation
entry an argument list.

> **Seat-policy note at L27's bytes (dated 2026-09-24).** This records the policy of the candidate that curation read: code base `06ed70cfcde7e3860ee5b53435727e7512e4335c` plus that leaf's working-tree delta, where `TASKLESS_SEAT_ROLES` was `{"chat", "terminal", "bootstrap"}` and a document-less `curator` session was refused `task-binding-required`. That was true of those bytes and is **superseded** — whether `curator` joined the set was then a product decision under revision, and it was taken in `260921-ICR-L32`. The carrier instructions and their ten generated copies changed first and this memory followed them.
>
> **Seat-policy note at these bytes (L32 curation, dated 2026-09-24T17:20+02:00).** At the bytes this curation read — code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus this leaf's working-tree delta — `TASKLESS_SEAT_ROLES` is `{"chat", "terminal", "bootstrap", "curator"}`: a document-less `curator` session is **admitted** and receives the curator capsule, while every other role is still refused `task-binding-required`. Read the sentences above as the policy **at these bytes**, not as a permanent property of the product.

Two smaller edits carry the same facts outward: the operation's opening states that it carries the
repository's first or resumed foundation as the same authoring work with a different admission and scope,
and the authority gate now names both writers (`knowledge-ingest` on the leaf entry,
`knowledge-bootstrap` on the repository-foundation entry) while keeping the batch and its publication
with their existing owners. The exit paragraph adds that on the foundation entry the same facts come from
the bootstrap report, with the areas a partial run did not reach named as not reached.

**This card describes a generated copy**, propagated from
`skills/l-01-agent-lifecycles/operations/curation.md` by `scripts/sync-skills.py` into this package-owned
copy and the eight harness starter packages.

## Update History
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the comparison table's carrier row changes with the policy.** The carrier row now names a taskless curator session (the developer's 2026-09-24 ruling) as the foundation entry's author and the bootstrap seat as its read-and-report half, where it previously said a taskless curator seat does not exist; the L27 note is retained as true at its own bytes and a second dated note states the policy at these bytes. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T12:44:00+02:00 — 260921-ICR-L27 curator (uncommitted change set on `ar/260921-icr-l27-ar`, code base `06ed70cfcde7e3860ee5b53435727e7512e4335c`): **body update: the repository-foundation entry section.** The new section with its six-row comparison table, the carrier row that states a taskless curator seat does not exist, the writer row with `enclosure_in_scope`, the opening sentence about the second bounded entry, the authority gate naming both writers, and the exit paragraph that carries the bootstrap report's facts and the areas a partial run did not reach. **Citation accounting:** the rows this card carries were re-read against this candidate — including the `## Handoff / exit` heading, whose live line was re-derived rather than carried forward — so no range was produced by adding a delta to an old number. No verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **body update: the packaged copy carries the canonical operation's new step.** The pass now examines family coverage and authors it as part of the same list — a deliberate `no_family` outcome with its basis, an unexamined obligation left without either key so the report names it unexamined, nothing grouped by directory/route/label/shared anchor, and a member change prompting a fresh look at the affected guarantee — and declares every inspected external source so the run retains it in a bounded manifest rather than as a repository path with a Git blob. Written in `skills/l-01-agent-lifecycles/operations/curation.md` and propagated by `scripts/sync-skills.py`. **Citation accounting:** the ranges this card carries into the files this leaf's change set moved were re-derived against the candidate's own bytes rather than shifted by a remembered delta. No claim and no row was dropped, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.

- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **body update for the authoring step this leaf added to the operation block, in the canonical source and therefore in this generated copy.** `skills/l-01-agent-lifecycles/operations/curation.md` is 161 lines where it measured 144 in this card's last reading; `## Normal workflow` gained a third numbered step (the real ingest invocation, `--baseline`, `--publish --commit --json`, and "consume the report, not the exit status"), `## Required inputs` gained the repository's published dataset, `## Authority gates` gained the paragraph keeping the batch and publication with their existing owners, `## Failure handling` gained the rule that a partial or refused hand-off stays partial and visible, and `## Handoff / exit` gained the published dataset identity. **Citation accounting:** the `## Handoff / exit` row this card already carried was re-derived `:121-128` → `:151-151` from the heading's own post-edit line rather than shifted, the new rows were read from the block's own lines, and `# Operation` `:1-1` — the one row that was already correct — was re-verified rather than assumed. This card documents the **generated packaged copy**: the canonical source is the root `skills/` tree, `scripts/sync-skills.py` produces the copy (the leaf ran it and its `--check`, both clean), and no harness skill root was installed. No verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-17T14:15+02:00 — 260915-CAPS-L19 curator: **Field-name warrant corrected — `ready-for-closeout` read as *never* a value of the combined `checklistStatus`.** That absolute sentence was written by 260915-CAPS-L10's curator as the warrant for this card's `D35` correction, and `CAPS-R19` (`260915-CAPS-L19`) measures it **literally false** (`application/memory_quality/controller.py:685-687` leaves the combined field at its incoming `ready-for-closeout` value on the success path, with `closeoutReady=true`). The card now states the three-path model instead: the raw `qualityChecklistStatus` is the repair loop's gate; the combined `checklistStatus` is rewritten to `coherence-required` **only when the coherence record is then missing or stale**; and `closeoutReady` becomes true only once that validation passes. Corrected under `CAPS-R19`'s revision note (2026-09-17T13:55), which is the authority for this change. The field-name correction itself stands and attribution is complementary — `260915-CAPS-L10` corrected the onboarding cards, `CAPS-R19` corrected the shipped sources (the five loop-gate carriers, their nine generated copies, the guard registry's docstring) and brought `docs/reference/mcp-tools.md` into the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`. The earlier entries below are left exactly as written: they record what L10 did, and this entry is the correction of their warrant. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-17T13:45+02:00 — 260915-CAPS-L10 curator: **corrected a landed defect (`D35`) in the Logic section.** The complete-curation sentence named `checklistStatus=ready-for-closeout` as the loop's termination condition; `ready-for-closeout` is never a value of the combined field. It now names the **raw** `qualityChecklistStatus` as the loop's gate and the **combined** `checklistStatus=coherence-required` as the point at which the `curator_coherence` authority is published, matching `application/memory_quality/controller.py:664,671,678,687`. The 2026-09-17T12:28+02:00 entry below is left as written: it records what CAPS-L18 did, and this entry is the correction of that wording. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. Added the changed `## Normal workflow` step 5 and `## Authority gates` rule to Logic: the complete curation check set, its `curatorActionableCount=0` / `checklistStatus=ready-for-closeout` termination condition, and the coherence authority published when the checklist requires it.
- 2026-09-16T22:19+02:00 — **No content impact:** 260915-CAPS-L16 curator. The canonical source gained
  one pronoun — the curator's exit says terminal/finalizer evidence attests only that **this** turn
  ended — and this card's Logic describes the curator/manager job split and the three fed inputs, not
  the completion-truth wording, so nothing in the body asserts the sentence that moved. Reviewed
  against the change set and deliberately left as written rather than reworded to match a one-word
  diff. **Repaired in the same pass (D16):** this card's `governingOverview` field and link pointed five
  levels up, at `onboarding/mcp/src/agents_remember/overview.md`, which does not exist — the card's own
  link text says "MCP package overview", which from `operations/` is **seven** levels up. Both now
  resolve to `onboarding/mcp/overview.md`. Verification metadata moves to this leaf's synced base
  `8997e184`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/operations/curation.md` — a file added by the role-instruction corpus consolidation. The canonical source is an operation-scoped procedure block extracted from interleaved role prose (curation).; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
