# mcp/src/agents_remember/application/review_comparison_freeze.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_comparison_freeze.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T04:01:40+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` |
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
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

The production entry resolves once and delegates to `freeze_resolved_review`. That shared entry collects normal R14 owner inputs for the exact resolved pair when no explicit bundle was supplied, composes the review, and hands the resulting bindings to `freeze_comparison_generation`. A caller-supplied bundle remains explicit: positive assessments must carry their complete immutable owner artifacts and exact unique assessment-channel provenance. Missing, incompatible or duplicate required provenance refuses before retention or publication; optional low-level currentness is independent.

**The freeze is deliberately not wired to any route, read path or closeout path — but since
`260921-ICR-L34` it does have a production caller**, the CLI subcommand
`agents-remember review-record-comparison`; see *Invariants And Boundaries*.

## Code Commentary

### Logic

Reserved curator owner references are admitted only through validated record inputs. Generic evidence citations cannot impersonate them. A named expected artifact that failed validation refuses capture; a genuinely non-applicable curator plane remains explicit unavailable metadata while otherwise valid source/knowledge capture proceeds. Explicit EMPTY input never silently fetches today's authority.

freeze_resolved_review accepts an already resolved admitted pair, composes it through the same review owner, and passes only that composition to the existing generation freeze. freeze_review_comparison remains the normal resolver entry. The explicit unchanged-knowledge producer uses this seam after its own checks; no second retention implementation is introduced.

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

**The options value carries the caller-known contributions.** `ComparisonFreezeOptions` carries optional owner records, cited artifacts, explicit historical absence and the predecessor. Omitted records ask the existing collection owner for the already resolved pair; explicit recovery alone sets `retain_parent_inputs` to reuse the named historical capture. `EMPTY_FREEZE_OPTIONS` is the shared frozen default.

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
- **A tree comparison is never frozen (MIK-R25).** `_unfreezable` refuses a resolution that carries `trees` or
  `knowledge_unavailable` before anything is staged, so no knowledge dataset copy is created or retained for a
  review of a converted leaf.
- **An occupied generation id is converged on or refused, never overwritten.**
- **The temporary-storage scope of a generation is the one leaf directory the record names**, and the
  sweep never leaves it, never touches a non-stage entry, and never removes a stage whose owner may be
  alive.
- **A refused composition publishes nothing.** The production entry returns the surface's own refusal
  unchanged rather than inventing a second reason.
- **No second capture path and no second snapshot path.** The capture identity is carried verbatim from
  the resolution, and the snapshot bytes come from `freeze_closed_snapshot`.
- **Boundary: the freeze is not wired to any route, read path or closeout path, and it has had a
  shipped production caller since `260921-ICR-L34`.** The caller is the CLI subcommand
  `agents-remember review-record-comparison`
  ([`cli/review_comparison_record.py`](../cli/review_comparison_record.py.md)), which resolves one
  enclosure contract, composes through the surface's own resolution and composition, and publishes only
  what that composition bound. **Superseded in part:** as ICR-L11 wrote it, "nothing in this leaf calls
  it from a serving surface, an HTTP route, the dashboard or a closeout path … and its consumer is a
  later leaf". The first half is still true and is the point — ordinary capture uses a live resolved pair and explicit recovery uses a named retained parent through the same owners. The operation remains an explicit command rather than a read-side mutation. The second half is no longer true: the consumer exists, and
  ICR-R21's own wiring is a different thing (it attaches the *selected generation* to the closeout
  preview and the delivered receipt to closeout apply and integration, and adds the reopen's fourth
  channel, without calling this operation). A reader must still not read the boundary as dead code:
  the production entry is complete and measured by fifteen production-composition cases.
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
| The published surface and the three shipped refusal codes it reuses. | `__all__`; `_ABSENT`; `_UNRESOLVED`; `_REFUSED` | mcp/src/agents_remember/application/review_comparison_freeze.py:118-127; mcp/src/agents_remember/application/review_comparison_freeze.py:133-133; mcp/src/agents_remember/application/review_comparison_freeze.py:134-134; mcp/src/agents_remember/application/review_comparison_freeze.py:135-135 |
| **The caller-known contributions and the shared default that collects actual owner inputs.** | `ComparisonEvidenceInput`; `ComparisonFreezeOptions`; `EMPTY_FREEZE_OPTIONS` | mcp/src/agents_remember/application/review_comparison_freeze.py:138-149; mcp/src/agents_remember/application/review_comparison_freeze.py:152-165; mcp/src/agents_remember/application/review_comparison_freeze.py:169-169 |
| **Everything one freeze binds, as values other owners produced**, including the declared historical absences and the predecessor. | `ComparisonGenerationRequest` | mcp/src/agents_remember/application/review_comparison_freeze.py:172-191 |
| **The outcome: a published record, or the refusal that stopped it, with `reused` separating the two ways a freeze succeeds.** | `ComparisonGenerationFreeze`; `published` | mcp/src/agents_remember/application/review_comparison_freeze.py:194-214 |
| The staging directory and the pin *this call* created, kept apart because an existing pin belongs to an already-published generation. | `_Staged`; `_FreezeRefused` | mcp/src/agents_remember/application/review_comparison_freeze.py:217-228; mcp/src/agents_remember/application/review_comparison_freeze.py:231-236 |
| **The production entry: resolve exactly as the surface does, compose exactly as the surface does, freeze only what was bound.** | `freeze_review_comparison` | mcp/src/agents_remember/application/review_comparison_freeze.py:239-258 |
| **The operation itself, and its two reclaim paths — its own refusal and a hard failure raised outside its control flow.** | `freeze_comparison_generation` | mcp/src/agents_remember/application/review_comparison_freeze.py:319-356 |
| The refusal for a comparison with no task artifact plane to survive in. | `_no_task_root_refusal` | mcp/src/agents_remember/application/review_comparison_freeze.py:423-435 |
| **Stage, seal, and publish by one rename.** | `_publish` | mcp/src/agents_remember/application/review_comparison_freeze.py:438-462 |
| **Convergence on an already-published record, and the refusal to overwrite one with a different binding.** | `_reuse_or_refuse` | mcp/src/agents_remember/application/review_comparison_freeze.py:465-497 |
| The knowledge halves, retained through the retention owner, with its refusal stopping the freeze. | `_retained_knowledge` | mcp/src/agents_remember/application/review_comparison_freeze.py:500-514 |
| The refusal for a failure the freeze could not classify, whose next action states that nothing was published. | `_storage_refusal`; `_reclaim` | mcp/src/agents_remember/application/review_comparison_freeze.py:517-528; mcp/src/agents_remember/application/review_comparison_freeze.py:531-542 |
| **The field set assembled from the owners' own values, each nested value dumped through its owner's model.** | `_manifest_payload`; `_json` | mcp/src/agents_remember/application/review_comparison_freeze.py:548-581; mcp/src/agents_remember/application/review_comparison_freeze.py:584-588 |
| **The scope: R02's inventory payload digested verbatim, and a selector identity read from the seed's own declared field.** | `_scope_binding`; `_selector_id` | mcp/src/agents_remember/application/review_comparison_freeze.py:591-605; mcp/src/agents_remember/application/review_comparison_freeze.py:608-621 |
| **The record binding, which asserts what the composition supplied and explicitly not what an owner published (R14's fact).** | `_record_binding` | mcp/src/agents_remember/application/review_comparison_freeze.py:624-661 |
| **A citation read and digested while freezing, and the task-root confinement that refuses one that escapes.** | `_evidence_references`; `_evidence_reference`; `_confined` | mcp/src/agents_remember/application/review_comparison_freeze.py:664-698; mcp/src/agents_remember/application/review_comparison_freeze.py:701-733; mcp/src/agents_remember/application/review_comparison_freeze.py:736-742 |
| **Every policy stamp as a constant its owner publishes.** | `_policy_stamps` | mcp/src/agents_remember/application/review_comparison_freeze.py:745-757 |
| **The lineage, and the candidate receipt digest that is `None` rather than fatal when unreadable.** | `_lineage`; `_receipt_digest` | mcp/src/agents_remember/application/review_comparison_freeze.py:760-769; mcp/src/agents_remember/application/review_comparison_freeze.py:772-787 |
| **The one hidden stage, the sweep that runs before it, and the pid-based liveness question that makes "reclaim only from the dead" possible.** | `_stage`; `_sweep_stale_stages`; `_issuer_alive` | mcp/src/agents_remember/application/review_comparison_freeze.py:793-807; mcp/src/agents_remember/application/review_comparison_freeze.py:810-830; mcp/src/agents_remember/application/review_comparison_freeze.py:833-854 |
| The two quiet cleanups: one stage removal and one pin release, neither of which may replace the refusal. | `_discard_stage`; `_release_quietly`; `_refused`; `_now` | mcp/src/agents_remember/application/review_comparison_freeze.py:857-860; mcp/src/agents_remember/application/review_comparison_freeze.py:863-878; mcp/src/agents_remember/application/review_comparison_freeze.py:887-890; mcp/src/agents_remember/application/review_comparison_freeze.py:881-884 |
| The owners it composes rather than re-implements. | `resolve_review_candidate`; `compose_review`; `ReviewCandidateResolution` | mcp/src/agents_remember/application/review_candidate_resolution.py:132-177; mcp/src/agents_remember/application/review_candidate_resolution.py:180-242; mcp/src/agents_remember/application/knowledge_review.py:334-574 |
| The retention owner this module hands the code pin and the two snapshots to. | `retain_comparison_source`; `retain_knowledge_sides` | mcp/src/agents_remember/application/review_comparison_retention.py:134-170; mcp/src/agents_remember/application/review_comparison_retention.py:381-407 |
| The record the freeze seals, and the `assemble_manifest` that seals and derives the id in one call. | `ComparisonGenerationManifest`; `assemble_manifest` | mcp/src/agents_remember/application/review_comparison_generation.py:405-498; mcp/src/agents_remember/application/review_comparison_generation.py:586-609 |
| The storage snapshot owner the two knowledge halves are copied through. | `freeze_closed_snapshot` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:92-137 |
| The record-collection inputs the caller supplies and the empty value the freeze defaults to. | `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/review_record_rendering.py:109-141; mcp/src/agents_remember/application/review_record_rendering.py:188-188 |
| **The production-composition case: a refused freeze publishes nothing, leaves no hidden stage, releases the pin it created, and the same leaf freezes afterwards.** | `test_a_refused_freeze_publishes_nothing_and_reclaims_its_stage_and_pin` | mcp/tests/test_knowledge_review_comparison_generation.py:677-710 |
| **The case that separates a stage a dead freeze left from a live one, driven through a real child process.** | `test_a_stage_a_dead_freeze_left_behind_is_reclaimed_and_a_live_one_is_not`; `_stage_left_by_a_dead_process` | mcp/tests/test_knowledge_review_comparison_generation.py:1032-1059; mcp/tests/test_knowledge_review_comparison_generation.py:1175-1196 |
| **The end-to-end journey the packet names: freeze, `git gc --prune=now` measured against a control object, remove the worktree, reopen in a child process.** | `test_a_frozen_comparison_reopens_the_exact_content_after_restart_and_reclamation`; `_reopen_in_a_new_process`; `_write_control_object` | mcp/tests/test_knowledge_review_comparison_generation.py:236-241; mcp/tests/test_knowledge_review_comparison_generation.py:279-315; mcp/tests/test_knowledge_review_comparison_generation.py:336-387 |

| `freeze_resolved_review` owns the behavior described above. | `freeze_resolved_review` | mcp/src/agents_remember/application/review_comparison_freeze.py:255-257 |
| `freeze_review_comparison` owns the behavior described above. | `freeze_review_comparison` | mcp/src/agents_remember/application/review_comparison_freeze.py:233-235 |
| `freeze_comparison_generation` owns the behavior described above. | `freeze_comparison_generation` | mcp/src/agents_remember/application/review_comparison_freeze.py:319-321 |

The following declarations carry the changed boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Ordinary and explicit recovery paths share exact resolved-pair composition. | `freeze_resolved_review` | mcp/src/agents_remember/application/review_comparison_freeze.py:261-316 |
| Complete authentic owner records and channel provenance are checked before publication. | `_record_input_refusal` | mcp/src/agents_remember/application/review_comparison_freeze.py:359-390 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The task artifact root it publishes into is
under the coordination root, which is outside both the code and the memory repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260921-ICR-L34 The Freeze Gets Its Production Caller, And A Placed Baseline Becomes Freezable

`260921-ICR-L34` (D62) is the leaf that made a leaf's review comparison producible at all. Two things
about *this* module are what it changed or established, and both belong on this card.

**The production entry now has a shipped caller.** `freeze_review_comparison` was complete and measured
but had **no caller outside the test suite**, so no leaf could publish a generation and every closed
leaf's review reopened from `history:recorded-source-range`. The caller is the CLI subcommand
`agents-remember review-record-comparison`
([`cli/review_comparison_record.py`](../cli/review_comparison_record.py.md)): it loads one enclosure
contract, composes a `ReviewSurfaceRequest` from that contract's own recorded identities, and calls this
function once, printing the outcome. Ordinary capture still requires the live candidate identity. L41 also permits the CLI to recover from an explicitly named retained parent and original curator digest. The retention owner revalidates that historical capture; closed resolutions continue to carry no live candidate identity.

**The caller is the first shipped caller to supply `parent`, and that is what makes a successor
readable.** `ComparisonFreezeOptions.parent` is documented as a caller-known fact, and the freeze derives
the successor's recorded index from it: a caller that names none publishes an **index 1** generation. A
leaf whose comparison legitimately changed therefore came to hold two index-1 generations with different
bindings, and `review_comparison_reopen` refuses a tied highest index by design — the leaf's own review
could no longer say which comparison it was reading. The CLI now discovers the standing generation
through `read_generation_refs` and names it, so a re-freeze publishes the next index with recorded
lineage rather than a second claim on index 1. Lineage was chosen over reclamation deliberately:
`review_comparison_reclamation` deletes only the *content* a manifest names and never the manifest
itself, so it cannot remove an index-1 identity, and a successor with recorded lineage is the only
owner-provided resolution.

**Carried, and the single most important thing for the next leaf on this route:** the owner still
permits the state it then refuses to read. `freeze_comparison_generation` will publish an index-1
generation for a leaf that already holds a readable one if a caller names no `parent`; the CLI supplies
it, but the next caller can reintroduce exactly the ambiguity. The guard belongs beside
`_reuse_or_refuse` — compute the parentless manifest, and if its generation id is *not* already
published while the leaf holds readable generations, refuse and name the predecessor. It was not added
here because it changes this owner's contract, and the leaf's mandate was to make the route reachable.
A second carried fact, measured by the leaf's adversarial verifier: because `lineage` sits **inside**
the seal (`review_comparison_generation._UNSEALED_FIELDS` names only `binding_digest`, `generation_id`
and `recorded_at`), naming a parent changes the derived id, so `_publish`'s `if final.exists()` reuse
branch is never taken in the ordinary sequence and `reused` is unreachable — every no-op retry appends a
generation with two full retained knowledge snapshots.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The production entry this leaf gave a caller, and the caller itself.** | `freeze_review_comparison`; `run` | mcp/src/agents_remember/application/review_comparison_freeze.py:239-258; mcp/src/agents_remember/cli/review_comparison_record.py:162-202 |
| **The caller options, including explicit predecessor identity and retained-parent recovery control.** | `ComparisonFreezeOptions`; `EMPTY_FREEZE_OPTIONS`; `parent` | mcp/src/agents_remember/application/review_comparison_freeze.py:152-165; mcp/src/agents_remember/application/review_comparison_freeze.py:169-169 |
| **The reuse branch that is never taken in the ordinary sequence, and the seal omissions that make it so.** | `_publish`; `_UNSEALED_FIELDS` | mcp/src/agents_remember/application/review_comparison_freeze.py:438-462; mcp/src/agents_remember/application/review_comparison_generation.py:162-162 |
| The lineage a named predecessor records: the id *and* that generation's manifest digest, so a successor is readable by identity. | `_lineage`; `ComparisonPublicationLineage` | mcp/src/agents_remember/application/review_comparison_freeze.py:760-769; mcp/src/agents_remember/application/review_comparison_generation.py:380-402 |
| Ordinary publication requires a live capture; explicit recovery revalidates the named retained parent capture without inventing a live identity. | `_unresolved_capture`; `_retained_capture` | mcp/src/agents_remember/application/review_comparison_retention.py:173-220; mcp/src/agents_remember/application/review_comparison_retention.py:223-275 |
| The discovery the caller reads to name the predecessor, in a total order by index then id. | `read_generation_refs`; `ComparisonGenerationRef` | mcp/src/agents_remember/application/review_comparison_generation.py:714-722; mcp/src/agents_remember/application/review_comparison_generation.py:725-753 |

## Update History
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): **body updated for MIK-R25.** Added the section "260928-MIK-L25 A Tree Comparison Is Refused Before Anything Is Staged" (`_unfreezable`, `_tree_comparison_refusal`) with two rows and an Invariants bullet. **Already-stale row re-measured:** the `freeze_comparison_generation` declaration row cited `290-292`, which did not hold the declaration even at the base; it now cites `319-321`. The other rows were projected by the installed fixer or re-pointed by exact line shift. No verification stamp was advanced.
- 2026-09-30T01:46:25+00:00: Generated citation repair: `_no_task_root_refusal` repointed to mcp/src/agents_remember/application/review_comparison_freeze.py:423-435. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:46:25+00:00: Generated citation repair: `_publish` repointed to mcp/src/agents_remember/application/review_comparison_freeze.py:438-462. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:46:25+00:00: Generated citation repair: `_retained_knowledge` repointed to mcp/src/agents_remember/application/review_comparison_freeze.py:500-514. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:46:25+00:00: Generated citation repair: `_policy_stamps` repointed to mcp/src/agents_remember/application/review_comparison_freeze.py:745-757. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T01:46:25+00:00: Generated citation repair: `_publish`; `_UNSEALED_FIELDS` repointed to mcp/src/agents_remember/application/review_comparison_freeze.py:438-462; mcp/src/agents_remember/application/review_comparison_generation.py:162-162. No content impact: mechanical anchor-range projection bound to citation source snapshot a85c638de10bc300eb93d4b69fedcbaf6e141873de546e8335d0f51f59402273; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/src/agents_remember/application/knowledge_review.py`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.

- 2026-09-27T05:41:59+00:00 — Reconciled the options claim with omitted-record collection and explicit retained-parent recovery; removed the superseded fixed field counts. Verification remains closeout-owned.

- 2026-09-27T05:31:41+00:00 — Selected the actual value/model declarations for 3 ambiguous source-linked citation(s), including container members and delegated type owners where applicable. The bounded claim is retained; generated history and real stamps remain unchanged.

- 2026-09-27T05:25:19+00:00 — Reconciled the L41 moved record/path owners and explicit retained-parent recovery boundary with current source. Prior generated history and real verification stamps are preserved.

- 2026-09-27T05:23:46+00:00 — Re-resolved 22 source-linked citation claim(s) against the extracted or shifted L41 owners. Each selected symbol uses its current declaration extent; other source references and prior generated history remain unchanged. Verification stamps remain closeout-owned.

- 2026-09-27T04:56:35+00:00 — Reconciled the ordinary resolved-pair record collection, positive owner-input admission, and explicit retained-parent path while preserving atomic publication and failure reclamation. Verification hashes/dates remain closeout-owned.
- 2026-09-26T21:14:55+00:00: Generated citation repair: `__all__`; `_ABSENT`; `_UNRESOLVED`; `_REFUSED` repointed to mcp/src/agents_remember/application/review_comparison_freeze.py:113-122; mcp/src/agents_remember/application/review_comparison_freeze.py:128-128; mcp/src/agents_remember/application/review_comparison_freeze.py:129-129; mcp/src/agents_remember/application/review_comparison_freeze.py:130-130. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:55+00:00: Generated citation repair: `ComparisonEvidenceInput`; `ComparisonFreezeOptions`; `EMPTY_FREEZE_OPTIONS` repointed to mcp/src/agents_remember/application/review_comparison_freeze.py:133-144; mcp/src/agents_remember/application/review_comparison_freeze.py:147-160; mcp/src/agents_remember/application/review_comparison_freeze.py:164-164. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:55+00:00: Generated citation repair: `_policy_stamps` repointed to mcp/src/agents_remember/application/review_comparison_freeze.py:613-625. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:14:55+00:00: Generated citation repair: `_discard_stage`; `_release_quietly`; `_refused`; `_now` repointed to mcp/src/agents_remember/application/review_comparison_freeze.py:725-728; mcp/src/agents_remember/application/review_comparison_freeze.py:731-746; mcp/src/agents_remember/application/review_comparison_freeze.py:749-752; mcp/src/agents_remember/application/review_comparison_freeze.py:755-758. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — Reconciled the changed ownership and current behavior with the source.
- 2026-09-25T22:00:00+02:00 — 260921-ICR-L34 curator (leaf `260921-ICR-L34`, uncommitted change set on `ar/260921-icr-l34-ar`, code base `a9a1a41bba535803421470bd17d858657177cb5f` plus the working-tree delta): **the production entry acquires its first shipped caller, and the "its consumer is a later leaf" boundary is corrected in place.** The caller is the CLI's `review-record-comparison` (D62), which composes through the surface's own resolution and composition and publishes only what that composition bound; it is deliberately not a route, a pane or a closeout path, because the retention owner requires a captured candidate identity and both closed-leaf resolutions pass `None`, so the producer is live-leaf-only by construction. The caller is also the first to supply `parent`, which is what stops a re-freeze from publishing a second index-1 record under a different binding — the ambiguity `review_comparison_reopen` refuses. **Two carried facts are recorded rather than smoothed:** the owner still permits that ambiguity when a caller names no `parent` (the guard belongs beside `_reuse_or_refuse`, and the fix is a contract change this leaf's mandate did not include), and because `lineage` sits inside the seal, `reused` is unreachable in the ordinary sequence and every no-op retry appends a generation. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so no commit carries the corrected body, and the governed closeout owns the real stamp.
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 curator (candidate uncommitted; basis: leaf base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta): **three enforced rows cleared by one row's ranges — two `range_resolution` findings and the reopened `ReviewRecordInputs` claim.** The record-collection row cited `review_record_rendering.py:84-106` and `:172-172`, while `ReviewRecordInputs` is declared at 109 and `EMPTY_REVIEW_RECORDS` at 183: `84-106`→`109-136` and `172-172`→`183-183`. Wording, Findings and Anchors all unchanged. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header's stamp values are untouched, and the governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **one inherited citation defect repaired — it is not this leaf's own.** The row carrying the module's own statement of the composition rule cited `review_comparison_freeze.py:1-42` with an Anchor cell reading `*(module docstring)*`, which is italic prose rather than an anchor: nothing in the row said what those lines were supposed to contain, so the range could not be checked at all. The defect predates this leaf (the row was written by 260921-ICR-L11) and is repaired here only because this leaf's curation pass owns the gate finding. The Anchor cell now names two real identifiers that occur **literally inside the cited range** — `freeze_closed_snapshot` at line 12 and `review_comparison_retention` at line 18, the two owners the docstring's composition rule names — which is what makes the claim ("the module's own statement of the composition rule and of the one-rename publication") checkable. The Finding wording, the cited range and every other row are unchanged; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are deliberately **not** advanced, because nothing in this leaf is committed and the governed closeout owns the real stamp.
- 2026-09-21T22:16+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **the mechanically projected ranges this document was carrying were re-read against the constructs they now name, and the projection records were replaced by this review.** The mechanical anchor-range projection this leaf's citation pass ran wrote ``ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS`` → mcp/src/agents_remember/application/review_record_rendering.py:84-106; mcp/src/agents_remember/application/review_record_rendering.py:111-111 into this document's Update History. This pass read each affected claim against the construct inside the range it now cites — the wording is retained where the construct supports it and the range was left as the projection re-derived it only after that reading — so the ranges are curator-read evidence rather than unreviewed projections, and the projection bullets are superseded by this entry rather than kept beside it. The claims are not otherwise re-worded, no anchor was renamed, no citation was dropped and no verification stamp was advanced: the candidate is uncommitted and the governed closeout's own metadata refresh owns the real stamp.
- 2026-09-21T19:31:00+02:00 — 260921-ICR-L11 curator (uncommitted change set on `ar/260921-icr-l11`, base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`): created this one-to-one card for the module this leaf introduced as **the act that produces a durable comparison generation** under ICR-R11@v1. It records the properties a reader has to act on rather than the function list: publication is **one rename of a fully validated directory**, so a generation exists or it does not and no partial capture can be resolved; an already-published generation is converged on (same binding digest → the published record with `reused=True`) or refused, never overwritten; every failure path removes the stage and releases **only** the pin this call created, because an existing pin belongs to a record this call did not make; and a hard failure raised outside the operation's own control flow is reclaimed exactly like a refusal, so a rename `OSError` cannot leak a complete-looking `.stage`. The card also records the sweep: stages are named for the creating pid, the sweep runs inside the one leaf directory the record names as its temporary storage scope, and every unattributable or possibly-live name counts as live — "reclaim only from the dead". Two stated boundaries are carried as boundaries and not as defects: the freeze is **deliberately not wired to any route or read path** (ICR-R21 wires it at closeout), and reclaiming a *published* generation belongs to `review_comparison_reclamation`, which this module never calls. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`, this leaf's recorded base — because every construct cited here exists only in this leaf's uncommitted candidate; what was actually read is this leaf's uncommitted working tree, and closeout owns the real stamp once the code commit exists.

## 260928-MIK-L25 A Tree Comparison Is Refused Before Anything Is Staged

**MIK-R25: no database copy is created, retained or read for a review.** `freeze_comparison_generation` now asks
`_unfreezable(resolved)` first. A resolution carrying `trees` (a converted leaf's four-tree comparison) or
`knowledge_unavailable` (a legacy comparison) is refused by `_tree_comparison_refusal`: the comparison is four Git
trees, recorded with its pinning refs when it was resolved, so there is nothing to freeze; the next action is to
reopen it from its record under `notes/reports/review-comparisons`, whose refs are deleted when the task is
archived. The old refusal for a hand-assembled pair with no task root is unchanged and comes second. A dataset
comparison of an unconverted leaf freezes exactly as before.

| Finding | Anchor | Source |
| --- | --- | --- |
| A tree or legacy comparison is unfreezable; a pair with no task root keeps its own refusal. | `_unfreezable` | mcp/src/agents_remember/application/review_comparison_freeze.py:393-405 |
| The refusal: recorded by trees, never copied. | `_tree_comparison_refusal` | mcp/src/agents_remember/application/review_comparison_freeze.py:408-420 |
| A tree comparison is never frozen into a dataset generation. | `test_a_tree_comparison_is_never_frozen_into_a_dataset_generation` | mcp/tests/test_review_git_trees.py:689-699 |
