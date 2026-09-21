# mcp/src/agents_remember/application/review_comparison_freeze.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_comparison_freeze.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T22:40:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l11`, uncommitted; base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75` |
| lastVerifiedCommitHash | `a8d2431926d6b130012ca81ed2e85b14721c0615` |
| lastVerifiedCommitDate | 2026-09-21T22:51:46+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The act that produces a durable comparison generation**, and the reclamation of an attempt that did
not become one. `review_comparison_generation` owns *what* a generation is and
`review_comparison_reopen` owns resolving one; this module owns the production path between them:
**resolve → compose → freeze**, a hidden stage → validation → seal → **one rename**, a sweep for the
stages a killed freeze left behind, and reclaim-on-failure.

Its governing property is that it **composes owners and re-implements none of them**: the source
endpoints and the capture identity come from the review's own resolution (R01), both knowledge halves
are copied by the storage snapshot owner (`freeze_closed_snapshot`), the inventory / comparison identity
/ record collections are the values the review composition already produced, and the retention of code
objects and snapshots belongs to `review_comparison_retention` — "the only thing in this package that
writes a ref".

Two entries, one difference:

- `freeze_review_comparison` (`:232-276`) is the **production entry**. It calls `resolve_review_candidate`
  and then `compose_review` exactly as the review surface does — including the composition's own
  pre-publication recheck that refuses a candidate whose captured endpoint moved — and freezes only what
  that composition actually bound. A refused composition freezes nothing and returns its refusal
  unchanged, so a generation is never published for a comparison the surface declined to make.
- `freeze_comparison_generation` (`:279-309`) takes the already-composed values as a
  `ComparisonGenerationRequest` and is the operation a test or a future caller can drive directly.

**The freeze is deliberately not wired to any route or read path** — see *Invariants And Boundaries*.

## Code Commentary

### Logic

**Publication is one rename of a fully validated directory.** `_stage` (`:647-661`) creates one hidden
sibling of the destination — same filesystem, so the publish is a same-filesystem rename, and a
discovery pass listing generations never sees a stage — named `.{pid}-{uuid}.stage` so two concurrent
freezes cannot share one and a stage a killed process left can be told from a live one. `_publish`
(`:327-351`) retains both knowledge halves into the stage, assembles the field set, seals it with
`assemble_manifest`, and only then calls `atomic_replace(staged.directory, final)`. Everything
referenced has been read back inside the stage before that rename; a generation therefore exists or it
does not.

**A published generation is never overwritten, and an exact retry converges.** If the destination
already exists, `_reuse_or_refuse` (`:354-386`) reads the published record: the same `binding_digest`
returns that record unchanged with `reused=True` (immutability is a property of bytes, not of
intention), while a different binding under an occupied id is refused — "an immutable generation is
never overwritten to describe a different comparison". The id is derived from the bindings, so an
occupied id holding the same binding *is* this generation.

**Every failure path reclaims the ephemeral state, and the refusal survives it.** `_reclaim`
(`:420-431`) removes the stage and releases a pin **this call** created, in that order, because a
cleanup failure must not replace the refusal that says why the freeze stopped. `_release_quietly`
(`:717-732`) suppresses its own errors for the same reason and is given `staged.created_pin`, which is
`None` when the ref already existed — an existing pin belongs to a generation that is already published,
and reclaiming it here would delete a record this call did not make.

**A hard failure is reclaimed exactly like a refusal.** `freeze_comparison_generation` wraps `_publish`
in `except (KnowledgeStorageError, OSError)` as well as its own `_FreezeRefused` (`:302-309`), so a
failure raised *outside* the operation's control flow — an unreadable record at the destination, a
filesystem that refuses the rename — goes through `_storage_refusal` (`:406-417`) and leaves no stage and
no unpublished pin behind.

**The stale-stage sweep reclaims only from the dead.** `_sweep_stale_stages` (`:664-684`) runs at every
freeze start inside the leaf's generation root — the directory the record itself names as
`temporary_storage_scope` — and removes only hidden entries ending in `.stage`. `_issuer_alive`
(`:687-708`) answers from the pid in the name via `os.kill(pid, 0)`: a name with no parsable pid, this
process, a permission error or any other `OSError` all count as **live**, so a concurrent freeze never
has its work removed from under it and the sweep never removes something it cannot attribute to a dead
freeze. Removal failures are suppressed; a stage this call cannot remove is reported by the next.

**The field set is assembled from the owners' own values, dumped through their own models.**
`_manifest_payload` (`:437-470`) builds the payload with `_json` (`:473-477`), which calls
`model_dump(mode="json")` when the value has one — because the seal is a digest over the *stored*
encoding, and handing the models themselves to the sealer would digest whatever the encoder happened to
do with them. Per binding:

- `_scope_binding` (`:480-494`) digests **R02's own inventory payload verbatim** and carries the owner's
  `listed_total` as `changed_path_count`; `_selector_id` (`:497-510`) reads the seed's own declared
  identity field (`invariant_id`, `family_id`) so a revision seed — which selects one revision of an
  identity — yields no identity this scope claims to have selected.
- `_record_binding` (`:513-544`) records counts and one digest over the three collections, and states in
  its `detail` that "whether an owner published none or could not be read is R14's fact, and this record
  asserts neither". `current` is deliberately **not** digested (it is a caller measurement keyed by
  tuples with no canonical JSON spelling); `current_measured` records that a measurement was supplied.
- `_policy_stamps` (`:599-611`) emits five stamps, every one a constant its owner publishes:
  `DIFF_POLICY_VERSION` (or the comparison's own `policy_version`), `KNOWLEDGE_REVIEW_SURFACE_VERSION`,
  `ORIGIN_VERSION`, `GENERATION_VERSION` and this record's own `COMPARISON_GENERATION_VERSION`.
- `_lineage` (`:614-623`) names the predecessor by id *and* manifest digest, the comparison's own
  binding digest, and `_receipt_digest` (`:626-641`) — the candidate dataset's admission receipt digest
  when one is beside it. A receipt that exists but cannot be read yields `None` rather than an error:
  the receipt is the *candidate's* record, this feature neither owns nor depends on it, and refusing a
  freeze over a file nothing in the comparison reads would make an unrelated file the gate.

**A citation is read and digested while freezing, and one that escapes the task root is refused.**
`_evidence_reference` (`:555-587`) resolves the caller's task-relative path through `_confined`
(`:590-596`), which refuses an absolute path or any `..` part, then reads the bytes and records their
digest and length. That is what makes the citation checkable at reopen rather than merely recorded; a
path that does not resolve or does not read is a refusal, not a citation nobody can follow.

**The options value exists because four caller-known facts travel together.** `ComparisonFreezeOptions`
(`:146-163`) carries the record collections, the cited artifacts, the halves the caller has established
carry no recorded generation (`historical_absence`), and the generation this one supersedes (`parent`).
One frozen default, `EMPTY_FREEZE_OPTIONS` (`:163`), is a module-level value rather than a per-call
default, because a default built per call would rebuild the tuple it holds.

### Conventions

`__all__` publishes `EMPTY_FREEZE_OPTIONS`, the two input dataclasses, the request, the outcome and the
two entry points. All five are **frozen dataclasses**, not pydantic models: they are values passed
between this operation and its callers, while the manifest it publishes is the stored wire shape. The
internal control flow is one private exception, `_FreezeRefused` (`:224-229`), carrying the
`ReviewRefusal` that stopped the freeze; every public outcome is a returned
`ComparisonGenerationFreeze` whose `state` is `"published"` or `"refused"`. The three refusal codes
(`_ABSENT`, `_UNRESOLVED`, `_REFUSED`, `:127-129`) are the **shipped** comparison vocabulary reused
rather than widened. `_now()` (`:741-744`) is the module's one clock read.

### Invariants And Boundaries

- **Nothing is published until every referenced byte has been read back inside the stage.** The rename is
  the last act, and it is one act.
- **A partial capture is unpublished and reclaimable**: the stage is removed on every failure path and a
  pin this call created is released again.
- **A pin this call did not create is never released here.**
- **An occupied generation id is converged on or refused, never overwritten.**
- **The temporary-storage scope of a generation is the one leaf directory the record names**, and the
  sweep never leaves it, never touches a non-stage entry, and never removes a stage whose owner may be
  alive.
- **A refused composition publishes nothing.** The production entry returns the surface's own refusal
  unchanged rather than inventing a second reason.
- **No second capture path and no second snapshot path.** The capture identity is carried verbatim from
  the resolution, and the snapshot bytes come from `freeze_closed_snapshot`.
- **Boundary: the freeze is deliberately not wired to any route or read path.** Nothing in this leaf
  calls it from a serving surface, an HTTP route, the dashboard or a closeout path; it is the operation
  a caller invokes, and wiring it at closeout is ICR-R21's obligation. A reader must not infer from the
  absence of callers that the operation is dead code — the production entry is complete and measured,
  and its consumer is a later leaf.
- **Boundary: the freeze does not reclaim a published generation.** Releasing a pin and discarding a
  retained snapshot belong to `review_comparison_reclamation`, and this module neither calls it nor
  reaches for a ref or a snapshot of a generation that is already published.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the module's own docstring and functions, in the four owners it
composes, and in the cases that drive the production entry against a real enclosure. Three details a
reader should carry: the publish is **one rename** of a directory whose every referenced byte was read
back first; the stage name carries the creating **pid**, which is what makes "reclaim only from the dead"
possible; and a receipt the comparison does not read is never allowed to gate a durable generation.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the composition rule and of the one-rename publication. | `freeze_closed_snapshot`; `review_comparison_retention` | mcp/src/agents_remember/application/review_comparison_freeze.py:1-42 |
| The published surface and the three shipped refusal codes it reuses. | `__all__`; `_ABSENT`; `_UNRESOLVED`; `_REFUSED` | mcp/src/agents_remember/application/review_comparison_freeze.py:113-129 |
| **The four caller-known facts that travel together, and the one empty contribution.** | `ComparisonEvidenceInput`; `ComparisonFreezeOptions`; `EMPTY_FREEZE_OPTIONS` | mcp/src/agents_remember/application/review_comparison_freeze.py:132-163 |
| **Everything one freeze binds, as values other owners produced**, including the declared historical absences and the predecessor. | `ComparisonGenerationRequest` | mcp/src/agents_remember/application/review_comparison_freeze.py:166-184 |
| **The outcome: a published record, or the refusal that stopped it, with `reused` separating the two ways a freeze succeeds.** | `ComparisonGenerationFreeze`; `published` | mcp/src/agents_remember/application/review_comparison_freeze.py:187-207 |
| The staging directory and the pin *this call* created, kept apart because an existing pin belongs to an already-published generation. | `_Staged`; `_FreezeRefused` | mcp/src/agents_remember/application/review_comparison_freeze.py:210-229 |
| **The production entry: resolve exactly as the surface does, compose exactly as the surface does, freeze only what was bound.** | `freeze_review_comparison` | mcp/src/agents_remember/application/review_comparison_freeze.py:232-276 |
| **The operation itself, and its two reclaim paths — its own refusal and a hard failure raised outside its control flow.** | `freeze_comparison_generation` | mcp/src/agents_remember/application/review_comparison_freeze.py:279-309 |
| The refusal for a comparison with no task artifact plane to survive in. | `_no_task_root_refusal` | mcp/src/agents_remember/application/review_comparison_freeze.py:312-324 |
| **Stage, seal, and publish by one rename.** | `_publish` | mcp/src/agents_remember/application/review_comparison_freeze.py:327-351 |
| **Convergence on an already-published record, and the refusal to overwrite one with a different binding.** | `_reuse_or_refuse` | mcp/src/agents_remember/application/review_comparison_freeze.py:354-386 |
| The knowledge halves, retained through the retention owner, with its refusal stopping the freeze. | `_retained_knowledge` | mcp/src/agents_remember/application/review_comparison_freeze.py:389-403 |
| The refusal for a failure the freeze could not classify, whose next action states that nothing was published. | `_storage_refusal`; `_reclaim` | mcp/src/agents_remember/application/review_comparison_freeze.py:406-431 |
| **The field set assembled from the owners' own values, each nested value dumped through its owner's model.** | `_manifest_payload`; `_json` | mcp/src/agents_remember/application/review_comparison_freeze.py:437-477 |
| **The scope: R02's inventory payload digested verbatim, and a selector identity read from the seed's own declared field.** | `_scope_binding`; `_selector_id` | mcp/src/agents_remember/application/review_comparison_freeze.py:480-510 |
| **The record binding, which asserts what the composition supplied and explicitly not what an owner published (R14's fact).** | `_record_binding` | mcp/src/agents_remember/application/review_comparison_freeze.py:513-544 |
| **A citation read and digested while freezing, and the task-root confinement that refuses one that escapes.** | `_evidence_references`; `_evidence_reference`; `_confined` | mcp/src/agents_remember/application/review_comparison_freeze.py:547-596 |
| **Every policy stamp as a constant its owner publishes.** | `_policy_stamps` | mcp/src/agents_remember/application/review_comparison_freeze.py:599-611 |
| **The lineage, and the candidate receipt digest that is `None` rather than fatal when unreadable.** | `_lineage`; `_receipt_digest` | mcp/src/agents_remember/application/review_comparison_freeze.py:614-641 |
| **The one hidden stage, the sweep that runs before it, and the pid-based liveness question that makes "reclaim only from the dead" possible.** | `_stage`; `_sweep_stale_stages`; `_issuer_alive` | mcp/src/agents_remember/application/review_comparison_freeze.py:647-708 |
| The two quiet cleanups: one stage removal and one pin release, neither of which may replace the refusal. | `_discard_stage`; `_release_quietly`; `_refused`; `_now` | mcp/src/agents_remember/application/review_comparison_freeze.py:711-744 |
| The owners it composes rather than re-implements. | `resolve_review_candidate`; `compose_review`; `ReviewCandidateResolution` | mcp/src/agents_remember/application/review_candidate_resolution.py:135-200; mcp/src/agents_remember/application/knowledge_review.py:377-454; mcp/src/agents_remember/application/review_candidate_resolution.py:103-132 |
| The retention owner this module hands the code pin and the two snapshots to. | `retain_comparison_source`; `retain_knowledge_sides` | mcp/src/agents_remember/application/review_comparison_retention.py:131-165; mcp/src/agents_remember/application/review_comparison_retention.py:315-341 |
| The record the freeze seals, and the `assemble_manifest` that seals and derives the id in one call. | `ComparisonGenerationManifest`; `assemble_manifest` | mcp/src/agents_remember/application/review_comparison_generation.py:376-469; mcp/src/agents_remember/application/review_comparison_generation.py:557-580 |
| The storage snapshot owner the two knowledge halves are copied through. | `freeze_closed_snapshot` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:92-160 |
| The record-collection inputs the caller supplies and the empty value the freeze defaults to. | `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/review_record_rendering.py:60-77 |
| **The production-composition case: a refused freeze publishes nothing, leaves no hidden stage, releases the pin it created, and the same leaf freezes afterwards.** | `test_a_refused_freeze_publishes_nothing_and_reclaims_its_stage_and_pin` | mcp/tests/test_knowledge_review_comparison_generation.py:675-708 |
| **The case that separates a stage a dead freeze left from a live one, driven through a real child process.** | `test_a_stage_a_dead_freeze_left_behind_is_reclaimed_and_a_live_one_is_not`; `_stage_left_by_a_dead_process` | mcp/tests/test_knowledge_review_comparison_generation.py:1030-1059; mcp/tests/test_knowledge_review_comparison_generation.py:1173-1194 |
| **The end-to-end journey the packet names: freeze, `git gc --prune=now` measured against a control object, remove the worktree, reopen in a child process.** | `test_a_frozen_comparison_reopens_the_exact_content_after_restart_and_reclamation`; `_reopen_in_a_new_process`; `_write_control_object` | mcp/tests/test_knowledge_review_comparison_generation.py:336-387; mcp/tests/test_knowledge_review_comparison_generation.py:279-315; mcp/tests/test_knowledge_review_comparison_generation.py:236-241 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The task artifact root it publishes into is
under the coordination root, which is outside both the code and the memory repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **one inherited citation defect repaired — it is not this leaf's own.** The row carrying the module's own statement of the composition rule cited `review_comparison_freeze.py:1-42` with an Anchor cell reading `*(module docstring)*`, which is italic prose rather than an anchor: nothing in the row said what those lines were supposed to contain, so the range could not be checked at all. The defect predates this leaf (the row was written by 260921-ICR-L11) and is repaired here only because this leaf's curation pass owns the gate finding. The Anchor cell now names two real identifiers that occur **literally inside the cited range** — `freeze_closed_snapshot` at line 12 and `review_comparison_retention` at line 18, the two owners the docstring's composition rule names — which is what makes the claim ("the module's own statement of the composition rule and of the one-rename publication") checkable. The Finding wording, the cited range and every other row are unchanged; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are deliberately **not** advanced, because nothing in this leaf is committed and the governed closeout owns the real stamp.
- 2026-09-21T19:31:00+02:00 — 260921-ICR-L11 curator (uncommitted change set on `ar/260921-icr-l11`, base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`): created this one-to-one card for the module this leaf introduced as **the act that produces a durable comparison generation** under ICR-R11@v1. It records the properties a reader has to act on rather than the function list: publication is **one rename of a fully validated directory**, so a generation exists or it does not and no partial capture can be resolved; an already-published generation is converged on (same binding digest → the published record with `reused=True`) or refused, never overwritten; every failure path removes the stage and releases **only** the pin this call created, because an existing pin belongs to a record this call did not make; and a hard failure raised outside the operation's own control flow is reclaimed exactly like a refusal, so a rename `OSError` cannot leak a complete-looking `.stage`. The card also records the sweep: stages are named for the creating pid, the sweep runs inside the one leaf directory the record names as its temporary storage scope, and every unattributable or possibly-live name counts as live — "reclaim only from the dead". Two stated boundaries are carried as boundaries and not as defects: the freeze is **deliberately not wired to any route or read path** (ICR-R21 wires it at closeout), and reclaiming a *published* generation belongs to `review_comparison_reclamation`, which this module never calls. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`, this leaf's recorded base — because every construct cited here exists only in this leaf's uncommitted candidate; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the real stamp once the code commit exists.
