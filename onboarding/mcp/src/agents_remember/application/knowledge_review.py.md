# mcp/src/agents_remember/application/knowledge_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T18:05+02:00 |
| lastVerifiedCommitHash |  `47570cd827428c171613c8cb01e01f0b1cb26f73`|
| lastVerifiedCommitDate |  2026-09-20T01:58:41+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l22` uncommitted source; base `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

The Intent Reviewer's thin adapter over the shipped read, diff and view operations. It **selects
nothing**: it resolves which candidate a task context names, calls the operations, and assembles
their results into the typed payload `models/knowledge/review.py` declares. R07's selection policy,
R08's comparison result, `Route` as the recorded scope axis and L20's review matrix are consumed
exactly as their owners publish them — no scope is computed, no frontier is widened, no reference is
re-resolved and no row is re-diffed here.

**Why the composition lives here and not in `serving/`.** `layers.toml` ranks `serving` below
`application`, so a serving module may not import the application operations this adapter composes.
The dashboard reaches it the way it reaches the launch-capsule compiler: through a port on
`ServingCollaborators` that the composition root wires in `cli/dashboard.py`. The HTTP shim therefore
does transport only.

**The candidate is resolved from canonical task context, never from a path.** A caller names a
repository, a master and a leaf id. The leaf's enclosure contract is located from the recorded task
root, and the two datasets the comparison is between are derived from that contract's own recorded
worktree group. The current `HEAD`, a guessed worktree path and a browser-supplied path are all
unavailable as fallbacks, because none of them is reachable from this module's inputs.

**Every absence is a state.** An unresolvable author, a missing operand, an absent assessment
collection and a comparison the shipped operation refused each produce a named field or a typed
refusal — never a blank a reader could take for a measured zero, and never a favourable default.

## Code Commentary

### Logic

**`resolve_review_candidate` screens the three selectors, then locates the leaf's own contract.**
Each of `repository_id`, `master` and `leaf_id` must be a single path segment: a value that is empty,
contains `/` or `\`, or starts with `.` is refused as `candidate_unresolved` naming the segment, the
offending input and the next action, so no selector can traverse out of the task tree. `_leaf_contract`
then globs `<coordination_root>/tasks/<repository>/<master>/enclosures/*/series-contract.md`, loads
each through the shipped `load_contract`, skips a contract whose `repo_name` differs or whose cleanup
is `abandoned`, and returns the one whose `parent_task_name`/`task_name` matches the master and whose
`slugify(leaf_id)` matches. A contract that does not resolve is refused as `candidate_unresolved`; a
contract with no live `code_worktree` is refused as `candidate_not_live` and the refusal says the
landed leaf's committed change-set is **not this surface**, so a review is never offered for work that
has already landed.

**The two datasets live under one disposable root and are named by two directory constants.**
`REVIEW_CANDIDATE_RELATIVE_ROOT` is `provider-runtime/dev-ar-coordination/knowledge` — inside the
leaf's disposable local root, the one root the checkout-coordination contract declares a linked task
worktree may hold undeclared state under — so a review reads no candidate out of the live coordination
tree and writes beside none. `_BASELINE_DIRECTORY` and `_CANDIDATE_DIRECTORY` name the two halves, and
both databases take their name from the shipped `CANDIDATE_DATABASE_NAME`. The resolution carries two
code roots and two tree ids; `baseline_code_tree_id` is the contract's `code_base_commit` or `None`,
and `candidate_code_tree_id` is deliberately `None`, because the candidate is the live uncommitted
working tree and has no exact tree id.

**`read_knowledge_review` is the whole public operation and it resolves before it composes.** It calls
`resolve_review_candidate`, returns `_refused(...)` immediately when that yields a `ReviewRefusal`, and
otherwise delegates to `compose_review`. The `contract` is carried on the resolution so a caller that
also needs the recorded task facts reads them from the same resolution rather than resolving twice.

**`compose_review` refuses an absent candidate dataset before it compares anything.** A
`candidate_database` that is not a file produces `candidate_dataset_absent` with the instruction to
author the candidate's knowledge in the leaf's disposable root and reopen — the surface substitutes no
other dataset. Only then does it call `_compare`, and a comparison that is not `state == "page"`, or
that carries no page or no binding, is turned into a `comparison_refused` result through
`_comparison_refusal`, which carries the shipped refusal's own `code`, `detail` and `next_action`
through verbatim rather than inventing a summary.

**The review matrix is read from the candidate through L20's operation, not recomputed.**
`read_knowledge_view` is handed the candidate database, the diff side opened by `open_diff_side` over
the same database and code root, and a `ViewRequest(view="review_matrix", record_kinds=REVIEW_MATRIX_KINDS)`.
A view that is not `state == "view"` becomes `comparison_refused` with the view's own detail appended,
so the surface never renders a pane from a partial matrix. `REVIEW_MATRIX_KINDS` is the *input* the
view is asked for — the five record kinds — rather than a selection policy of this leaf's; the view
applies its own registered traversal over them.

**The five subjects the payload states are assembled from the matrix rows and the supplied records,
and the two authored/mechanical collections never mix.** `_knowledge_pane` renders identities, both
sides' exact statements and conditions, the retained-revision groups, every field transition the
comparison reported, the authored records (`AUTHORED_EFFECT_KINDS`), the detection signals, the
assessment displays and one unresolved-author reference per authored row. `_source_pane` renders the
realization items as selected locations, the five published remaining counts, the expansion reference
and command, the attributed/unattributed changed paths, and one unresolved attribution row per item the
other side's selection did not reach. `_evidence_pane` renders the evidence links, the observations and
the assessments, with `evidence_state` and `assessment_state` computed from the collections themselves.

**Staleness and submission are two statements of one fact, and the payload model enforces it.**
`_staleness` returns `current` when there is no `previous_binding_digest` or it equals the comparison's
own `binding_digest`, and `stale` otherwise — retaining the previous digest as a *labelled previous
input* together with the moved axis. `_submission` returns `disabled_stale` exactly when stale and
`unavailable` otherwise, and in both cases publishes `PROPOSED_ASSESSMENT_DISPOSITIONS` rather than a
control of this module's own. `KnowledgeReviewPayload`'s validator refuses the payload where the two
disagree, so "an assessment is never submitted against a comparison that has moved" is a property of
the value.

**Five counts are published, and a count that has no meaning says so instead of reporting zero.**
`locations_remaining` and `records_present_outside_selection` are measured from the page;
`references_unresolved` is the page's own `suppressed_total`; and
`changed_paths_outside_selection` and `unattributed_changed_paths` carry `value=None` with a stated
reason when the comparison published no source expansion, because "not measured here" and "measured as
none" are different facts. `ReviewRemainingCount`'s validator refuses an unexplained absent count and
refuses a measured count that also carries a not-applicable reason.

**`review_records_for` reads the published assessment collection and treats absence as an empty
collection, not an error.** It resolves the candidate, returns `EMPTY_REVIEW_RECORDS` when the
resolution refuses or carries no contract, loads the curator-coherence authority through the shipped
`load_curator_coherence_authority`, and returns `EMPTY_REVIEW_RECORDS` for a `CuratorCoherenceError`,
`OSError` or `ValueError` rather than failing. No `current` measurement is supplied, so
`_subject_states` reports every stored assessment `stale` — the shipped projection refuses to promote
an unmeasured assessment to current and this surface does not improve on that by guessing.

### Conventions

The module holds no vocabulary of its own: every value it returns is a shipped type — the review
models from `models/knowledge/review.py`, the diff models and `VerificationObservationPayload`, the
detection payload and the read models. `ReviewSurfaceRequest` is imported for re-export and named in
`__all__` beside `read_knowledge_review`, `compose_review`, `resolve_review_candidate`,
`review_records_for`, `ReviewRecordInputs`, `ReviewCandidateResolution`, `EMPTY_REVIEW_RECORDS`,
`REVIEW_CANDIDATE_RELATIVE_ROOT` and `REVIEW_MATRIX_KINDS`. `ReviewRecordInputs` and
`ReviewCandidateResolution` are frozen dataclasses rather than pydantic models, because they carry
live paths and a loaded contract rather than a wire shape. `_refused` is the single builder of a
refused result and `refusal(...)` the single builder of a refusal value, so no code path in this
module raises out of `read_knowledge_review`. The private helpers are deliberately one-purpose:
`_selector_record_id` reads `kind` off the seed through `getattr` and returns `None` for any seed kind
that is not an identity, so a non-identity selector addresses no identity item rather than a guessed
one.

### Invariants And Boundaries

- **The adapter selects nothing.** The comparison, the item identities, the counts, the field
  transitions and the revision groups are the shipped operations' own values; the module adds no
  ordering, no ranking, no filter and no re-diff.
- **No path is accepted from a caller.** The candidate dataset is derived from the located enclosure
  contract's recorded worktree group; `HEAD`, a guessed worktree and a browser-supplied path are all
  unreachable from the module's inputs.
- **A side with no exact tree is a supported state.** `candidate_code_tree_id` is `None` by
  construction and `baseline_code_tree_id` is `None` when the contract records no base commit; neither
  is a prompt to substitute a working tree.
- **Unassessed is the absence of a value.** No `current` measurement means every stored assessment is
  displayed `stale`; a candidate with no published assessment displays `unassessed` rather than a
  clearance.
- **An unresolved reference is displayed, never dropped and never made anonymous.** `_unresolved_author`
  names the record and states that the matrix publishes no author; the evidence pane names the coverage
  the matrix does not publish; the source pane names every item held by only one snapshot.
- **The module defines no record kind and stores nothing.** It opens the candidate read-only through
  the shipped operations and writes no file; `REVIEW_CANDIDATE_RELATIVE_ROOT` is a location it *reads*.
- **Rank is the reason for the port.** `serving/review.py` takes this module's `read_knowledge_review`
  as a port supplied by the composition root, because a serving module may not import it.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the adapter's own docstring and
functions, the shipped comparison and view operations it calls, the contract loader that locates the
candidate, the models module that declares the payload, and the test module that drives the whole
surface. One detail a reader should carry: the two path constants under `REVIEW_CANDIDATE_RELATIVE_ROOT`
are this surface's own recorded decision for this increment, and the candidate half is what the
comparison's `after` side reads.

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter's own statement of what it selects (nothing), why the composition sits at this tier rather than in `serving/`, and how the candidate is resolved from task context rather than from a path. | `resolve_review_candidate` | mcp/src/agents_remember/application/knowledge_review.py:1-26; mcp/src/agents_remember/application/knowledge_review.py:182-227 |
| The published adapter surface: the two entry points, the two dataclasses, the two constants and the re-exported request model. | `__all__` | mcp/src/agents_remember/application/knowledge_review.py:92-103 |
| The disposable candidate root and the two directory names it composes: both datasets inside the leaf's disposable local root, so a review reads no candidate out of the live coordination tree. | `REVIEW_CANDIDATE_RELATIVE_ROOT`; `CANDIDATE_DATABASE_NAME` | mcp/src/agents_remember/application/knowledge_review.py:105-114; mcp/src/agents_remember/models/knowledge/snapshot.py:45-58 |
| The record kinds the review matrix is asked for — an input to L20's view rather than a selection policy of this module's — and the authored kinds the knowledge pane separates from the mechanical signals. | `REVIEW_MATRIX_KINDS`; `AUTHORED_EFFECT_KINDS` | mcp/src/agents_remember/application/knowledge_review.py:116-131 |
| The record input set, its frozen shape and its single module-level empty value. | `ReviewRecordInputs`; `EMPTY_REVIEW_RECORDS` | mcp/src/agents_remember/application/knowledge_review.py:138-156 |
| The resolution value: the two datasets, the two code roots, the two tree ids and the carried contract. | `ReviewCandidateResolution` | mcp/src/agents_remember/application/knowledge_review.py:159-179 |
| The one contract locator: the recorded task root, the globbed enclosures, the `repo_name`/`cleanup` skips and the leaf-id slug match. | `_leaf_contract`; `slugify`; `load_contract` | mcp/src/agents_remember/application/knowledge_review.py:230-250; mcp/src/agents_remember/tasks/task_paths.py:20-35; mcp/src/agents_remember/worktrees/task_resolver.py:20-50; mcp/src/agents_remember/worktrees/worktree_contract.py:430-450 |
| **The whole public operation: resolve, then compose, with a refused resolution returned as a refused result before any comparison runs.** | `read_knowledge_review` | mcp/src/agents_remember/application/knowledge_review.py:253-281 |
| **The composition: the absent-dataset refusal, the comparison, the matrix read through the shipped view operation, and the three panes with staleness and submission.** | `compose_review`; `read_knowledge_view`; `ViewRequest` | mcp/src/agents_remember/application/knowledge_review.py:284-365; mcp/src/agents_remember/application/knowledge_views.py:78-104; mcp/src/agents_remember/models/knowledge/view.py:1060-1094 |
| The shipped comparison call over the two already-resolved sides, with the probe passed through and no side or selector added. | `_compare`; `diff_knowledge_scope` | mcp/src/agents_remember/application/knowledge_review.py:368-399; mcp/src/agents_remember/application/knowledge_diff.py:190-230 |
| The comparison identity carried verbatim, and the limits/omissions/side-absences carried as counted facts. | `_comparison_identity`; `_limitations` | mcp/src/agents_remember/application/knowledge_review.py:424-440; mcp/src/agents_remember/application/knowledge_review.py:443-458 |
| **Staleness and submission as two statements of one fact, and the payload validator that refuses a payload where they disagree.** | `_staleness`; `_submission`; `KnowledgeReviewPayload` | mcp/src/agents_remember/application/knowledge_review.py:461-476; mcp/src/agents_remember/application/knowledge_review.py:479-506; mcp/src/agents_remember/models/knowledge/review.py:490-528 |
| The three panes: identities and authored records never rendered as mechanical facts, the selected locations and the five published remaining counts, and the evidence pane's two independent absence states. | `_knowledge_pane`; `_source_pane`; `_evidence_pane` | mcp/src/agents_remember/application/knowledge_review.py:512-545; mcp/src/agents_remember/application/knowledge_review.py:548-609; mcp/src/agents_remember/application/knowledge_review.py:612-648 |
| The per-subject assessment projection that reports an unmeasured assessment stale rather than promoting it to current. | `_subject_states`; `assessment_state_for` | mcp/src/agents_remember/application/knowledge_review.py:654-673; mcp/src/agents_remember/models/lifecycles/review_assessment.py:430-460 |
| The assessment display, and the observation displayed exactly with no sufficiency field. | `_assessment_display`; `_observation` | mcp/src/agents_remember/application/knowledge_review.py:695-709; mcp/src/agents_remember/application/knowledge_review.py:712-730 |
| **The reviewed subject chosen by the selector that named it: a sibling's item is never substituted, and a subject the comparison holds on both sides is preferred.** | `_identity_item`; `_selector_record_id` | mcp/src/agents_remember/application/knowledge_review.py:733-759; mcp/src/agents_remember/application/knowledge_review.py:762-770 |
| The selected source location with its recorded role kept `None` rather than guessed, and the change state derived from the comparison's own observation. | `_location`; `_change_state` | mcp/src/agents_remember/application/knowledge_review.py:911-934; mcp/src/agents_remember/application/knowledge_review.py:944-950 |
| The one refusal builder, and the published assessment collection read from the curator authority's own publication with an absent authority treated as empty rather than as an error. | `refusal`; `review_records_for`; `load_curator_coherence_authority` | mcp/src/agents_remember/application/knowledge_review.py:962-976; mcp/src/agents_remember/application/knowledge_review.py:979-1004; mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:235-260 |
| **The case that proves the surface stores nothing: the two datasets' row counts are identical across a full render.** | `test_the_surface_stores_nothing_so_deleting_every_rendering_loses_no_canonical_information` | mcp/tests/test_knowledge_review_surface.py:440-452 |
| **The case that proves the adapter selects nothing: the comparison identity, item identities and counts are the shipped operation's own, compared value for value.** | `test_the_adapter_selects_nothing_because_the_shipped_comparison_is_the_comparison_rendered` | mcp/tests/test_knowledge_review_surface.py:453-504 |
| The case that proves the candidate is resolved from task context and never from a browser-chosen path, and the case that proves an absent dataset refuses by name. | `test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`; `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one` | mcp/tests/test_knowledge_review_surface.py:734-749; mcp/tests/test_knowledge_review_surface.py:729-742 |
| The case that proves the stale rule in both directions, which were two cases until they were merged: a stale comparison keeps its previous input and disables submission, and a current comparison whose submission claims staleness is unconstructible rather than merely unlikely. | `test_the_stale_rule_holds_in_both_directions` | mcp/tests/test_knowledge_review_surface.py:569-590 |
| The composition root that wires this adapter into the serving port. | `review_port`; `read_knowledge_review` | mcp/src/agents_remember/cli/dashboard.py:76-98 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The adapter reads one coordination root's
task tree and one candidate's disposable datasets, and carries no identity that ranges beyond the
repository namespace the request names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-19T22:38+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): **re-read each claim below against the construct its range now covers, corrected the wording where the construct had moved, re-derived every range from the construct's real extent in the file the claim cites, and only then left the card's stamp to closeout.** No `Generated citation repair` bullet is written: these are curator edits, not a mechanical projection. `knowledge_review.py.md:208` — re-read: the two cases the claim names were merged into one, and its own docstring says so ('One rule, two directions, and they were two cases until they were merged'). The rule is unchanged, so the claim's SUBJECT survives; only the anchor and range are wrong.

- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `knowledge_review.py.md:207` (`test_the_candidate_is_resolved_from_task_context_and_never_from_a_browser_chosen_path`, `test_an_absent_candidate_dataset_refuses_by_name_rather_than_substituting_one`).
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's application adapter. It records the four things a reader of this route needs: the adapter **selects nothing** and composes only R08's `diff_knowledge_scope` and L20's `read_knowledge_view(review_matrix)`; the composition sits at the application tier because `layers.toml` ranks `serving` below `application`, so the HTTP shim reaches it through a port the composition root wires; the candidate is resolved from canonical task context and never from a caller-supplied path; and every absence is a named state or a typed refusal rather than a favourable default. It also records the two published facts the panes are built on — the five remaining counts, where an unmeasurable quantity states its reason instead of reporting a zero, and the stale/submission coupling the payload model enforces structurally. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
