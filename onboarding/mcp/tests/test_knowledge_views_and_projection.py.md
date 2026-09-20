# mcp/tests/test_knowledge_views_and_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_views_and_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T15:30+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80` |
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted change set; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

**The 39 `unit-regression` cases that pin `KS-R20@v1` §1, §2, §3, §5 and §6 as behaviour: the closed
view set, the classification, the bounded response, the vault-safety writer, and the mounted surface's
own refusals.** §1 is the closed set of five view names, asserted as a literal and in order — the one
assertion that cannot be satisfied by iterating the constant it checks. §2 is the classification — the
two-member provenance class with its author/rule separation, the closed and versioned mechanical-rule
registry that admits exactly one rule per ordering input, the four admitted ordering inputs, and the
declared tiebreak rule every ordered position must name. §3 is the bounding — the two-way honesty rule
between `rows_remaining` and a continuation, the continuation refused when it is presented against a
snapshot other than the one that minted it, and the quantity that states `not_applicable` with a reason
instead of reporting a zero. §5 is the vault safety — confinement, the case collision, the unchanged
test in its two halves, the externally edited file, the explicit per-path authorization as the only
overwrite route, the symlink that is never followed, the interrupted publication, the absent sweep, and
the manifest that refuses to be unreadable or doubly owned. §6 is the mounted surface — one case per
registered `knowledge_*` operation family, each asserting that family's own refusal path rather than the
roster's shape, plus one case asserting the five mounted names are exactly the five these cases drive.
Most cases run without a database: the view vocabulary, the closed rule registry, the ordering pass and
the projection writer are pure functions of their inputs, which is also why a renderer that opened a
store would not typecheck against the declared reader port. The eight §6 cases are the exception: they
drive the **registered** handlers through a real `FastMCP` server, five of them over a dataset this
build creates, and that is their point — a roster row is not coverage.

## Code Commentary

### Logic

**The module is local builders, then the cases in clause order under a section comment each, and almost all
of it can run without a database because nothing it measures has one inside it.** `SNAPSHOT` is one
`KnowledgeReadSnapshot` over fixed digests; `_completeness` scopes a completeness statement to that
snapshot's logical digest under the recorded graph and traversal policy; `_output` builds one
`RenderedOutput` carrying a stable identity, the renderer version and its bytes; `_profile` builds the
local destination profile the writer takes. Nothing above the destination section touches a filesystem, and
the ten destination cases inside it take pytest's `tmp_path` and a real vault root. The docstring states the
reason those vocabulary cases need no store: the view vocabulary, the closed rule registry, the ordering pass and
the projection writer are pure functions of their inputs, so the classification rule can be tested without
a store — and a renderer that opened one would not typecheck against `KnowledgeViewReader`, which carries
no path, no connection and no candidate tree. The same docstring names the four cases that carry the leaf;
two of them, the ordering differential and the classification completeness scan, are the sibling
acceptance module's cases, so this card names them where its own docstring does.

**§2's cases close the class at two members, refuse every mixture, and then measure the registry that keeps
a determination mechanical.** `test_the_class_set_is_closed_at_two_members` asserts the class tuple equals
`("authored", "mechanical")`, because a third member would be the unclassifiable value the packet forbids
wearing a name. `test_an_authored_classification_carries_its_author_and_cannot_cite_a_rule` builds an
authored provenance, asserts its author reference, and then refuses a `Provenance` that holds the authored
record *and* a `rule_id`; `test_a_mechanical_classification_names_its_rule_and_has_no_author` is the
mirror, refusing a mechanical class that carries an authored record, and
`test_a_class_without_its_evidence_is_refused_rather_than_defaulted` refuses both classes built with
neither evidence, so a value with no author and no rule can never be emitted as classified.
`test_an_unregistered_rule_cannot_produce_a_classification` raises `MechanicalRuleNotRegistered` for a rule
id no renderer registered and again for a registered id presented at the wrong version.
`test_the_registry_admits_one_rule_per_ordering_input` collects the ordering input of every rule whose
determination is `ordering`, asserts the set equals `ORDERING_INPUTS`, pins the registry version at 1, and
requires every registered rule to declare at least one value it reads — the closure runs in the direction
that matters, since an admitted input with no rule would be an ordering nobody could reproduce.
`test_no_registered_rule_reads_a_name_a_path_or_a_score` sweeps every rule's declared reads against the
eight forbidden tokens and puts the rule and the read into its failure message, so a rule that started
reading a symbol's spelling, a path's depth or a score is reported whether or not any payload would expose
it.

**Ordering has one admission gate and one reproducibility obligation, and both are refused rather than
defaulted.** `test_an_unadmitted_ordering_input_is_refused_rather_than_defaulted` asks
`require_admitted_ordering_input` for a fifth input and gets a `ViewRefusal` whose code is
`unadmitted_ordering_input` and whose observed value is the request itself, while an admitted input answers
`None`; there is no fallback order and no rows.
`test_every_admitted_position_names_the_declared_tiebreak_rule` builds a position and finds
`ordering.declared-tiebreak` on it, with the authored provenance of the position kept separate from the
mechanical rule that placed it. `test_a_position_cannot_name_an_unregistered_rule` is the negative: an
inline comparator cannot acquire a position by naming a rule the registry does not carry, because the
position's own validator consults the registry.

**§3's cases make the bounding statement one fact with two refusals.** A payload with three rows remaining
and no continuation is refused by `test_a_payload_with_rows_remaining_must_carry_a_continuation`, and a
complete page that nevertheless carries a token is refused by
`test_a_complete_payload_must_not_carry_a_continuation`; reading the same comparison in both directions is
what makes each refusal mean something, since either half alone is satisfiable by a writer that is wrong in
the other. `test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named` shows the
token accepted against its own snapshot and refused against a copy whose logical digest moved, with
`expected` and `observed` naming the two digests — the view does not silently re-resolve and the caller
receives no page. `test_a_quantity_with_no_meaning_for_a_view_says_so_instead_of_reporting_zero` asserts
the `not_applicable` state, the absent value and the non-blank reason for a quantity the view does not
measure, keeps `rows_returned` at a real zero beside it, and refuses a stated absence that carries a value,
because a zero there would read as a measurement.

**Two shape obligations are asserted over the serialized record rather than described in prose.**
`test_the_curation_queue_keeps_a_work_item_free_of_any_curator_judgement` dumps a `MachineWorkItem` and
asserts the body holds no `disposition`, no `rationale` and no `author_ref`, then builds the queue row and
finds its `disposition` still `None`: requirement 1.6 is a shape obligation, and the two attributions live
in two records.
`test_a_no_consequence_statement_is_refused_without_the_class_that_produced_it` builds a mechanical
statement, asserts it names no stored claim, and then refuses one carrying a `claim_ref`;
`test_an_authored_no_consequence_statement_names_the_stored_claim_it_is` is the other half — the authored
determination names the stored claim and carries its author.

**The confinement and collision vocabulary is measured without a filesystem, and then the writer is
measured over a real temporary destination.**
`test_a_path_that_is_not_purely_destination_relative_is_refused` hands six offending spellings — an
absolute path, a parent escape, an interior `..`, a doubled separator, a path inside the staging directory
and the empty string — to `require_confined_relative_path` and requires `destination_escape` for each while
a plainly relative path answers `None`, naming the offending spelling in its assertion message.
`test_a_case_collision_names_both_paths_and_both_records` detects two outputs whose destinations differ
only by case, asserts one collision naming the canonical form and both stable identities, and asserts that
a single output produces none. From there the cases take `tmp_path`:
`test_the_first_projection_writes_a_generation_one_manifest` asserts the `projected` state, generation one,
and the five recorded values every later unchanged test reads — path, identity, source snapshot, renderer
version and a sha256 digest. `test_an_unchanged_orphan_is_removed_and_a_modified_one_is_retained` is
requirement 5.6's two halves in one run: the path must be in the prior manifest *and* the bytes on disk
must still match it, so a dropped file nobody edited is removed while a dropped file the user edited is
retained with the reason `edited-since-last-projection`, and the outcome states say `removed` and
`retained-with-reason`. `test_an_externally_edited_output_is_reported_and_never_overwritten` keeps the
user's bytes, reports the single `modified` discrepancy, completes the rest of the plan, and shows that the
prior digest survives in the manifest so a third run detects the same edit again rather than adopting it as
its own. `test_an_explicit_per_path_authorization_is_the_only_route_to_an_overwrite` edits two outputs,
authorizes one path, and finds the authorized path rewritten, the other still holding the user's bytes, and
the two manifest entries carrying the per-path authorization flag.

**The writer's refusals all happen before a byte is published, and the destination is never swept.**
`test_an_escaping_path_refuses_the_whole_plan_and_writes_nothing` gets a `refused` report whose code is
`destination_escape` and whose `resolved_root` is the real path of the destination root, and asserts the
good output's directory and the manifest were never created.
`test_a_collision_refuses_the_whole_plan_before_either_output_is_written` gets `destination_collision`,
finds the colliding record named in the refusal, and finds nothing written.
`test_a_symlinked_destination_entry_is_not_followed_and_the_rest_continues` plants a real symlink to a
directory outside the root, projects one output through it and one elsewhere, and asserts the outside
directory gained nothing while the other output published and the linked path is reported.
`test_an_interruption_leaves_the_destination_exactly_as_it_was` drives the writer's own
`ProjectionHooks(before_publish=...)` seam to raise between staging and the first rename, then compares a
full byte-for-byte tree snapshot of the destination against the prior one; the packet's Open Truth Gap
recorded that whether this checkpoint was deterministically inducible was unverified, and this case is the
answer, with no sleep, no thread and no signal.
`test_the_destination_is_never_swept_and_unlisted_files_are_untouched` puts a user directory in the
destination, projects an empty plan after one generation, and finds the user's file intact, the retired
output gone, and the outcomes naming only the path the manifest knew.
`test_an_unreadable_manifest_refuses_rather_than_treating_the_destination_as_unowned` writes non-JSON into
the manifest, gets `manifest_unreadable`, and asserts nothing was written;
`test_the_manifest_refuses_two_owners_for_one_path` hands the same `ManagedOutput` twice to a
`ProjectionManifest` and requires the refusal, because a duplicate path could not answer "does the
substrate own this file".

**§1.1 is asserted as a literal, and §6 is asserted by driving the mount.**
`test_the_five_view_names_are_the_closed_ordered_set` writes the five names out
(`source_context`, `invariant`, `family`, `review_matrix`, `curation_queue`), requires `tuple(VIEW_PURPOSES)`
to equal them and the five payload classes' own `view` defaults to follow in the same order, so a sixth
view, a rename, a reorder, or a name admitted by the `ViewName` literal union but missing from the published
purposes map goes red — the one assertion the view-looping cases cannot make, because they iterate the
constant they would be checking. The eight §6 cases mount the knowledge family alone on a real `FastMCP`
server (`register_knowledge_tools` with a stub config whose only read fact is a workspace root) and pin one
refusal per operation family, each decided before a page is built: an ordering input outside the four
admitted ones (`unadmitted_ordering_input`), a sixth view (`unknown_view`, refused from the name alone
against a path that does not exist), a continuation minted for another walk (`continuation_unreadable`,
against a real current-generation dataset), a record kind with no admitted write (`registration_absent`), a
comparison whose before side is absent (`selected_input_unavailable`, naming the path it could not read), an
integrity report over a namespace with no recorded detection run (`compatible is None` with a stated
limitation rather than a zero), a projection with no view named (`unresolved_projection_input`, whose
destination is never created), and the mount's own membership — the five tool names, each of which this
module's own source must call by name.

### Conventions

- **Lane and marker.** `mcp/tests/test-evidence-lanes.toml` files this module under `unit-regression`, and
  the module declares no module-level `pytestmark`: its cases are selected by the project default
  (`-m "not integration"`) rather than by an integration marker of their own. The eight §6 cases carry
  `@pytest.mark.anyio` and a module-local `anyio_backend` fixture pinned to `asyncio`, which is how they
  await the registered handlers in-process. The lane stays the unit one because they build their own dataset
  under `tmp_path`, start no subprocess and reach no network — and because the integration lane is at exactly
  **400 / 400** against `integration_case_budget = 400`, measured in this change set by seat W1's
  worktree-bound collect-only run, so it cannot take a new case at all.
- **The fixture is pytest's `tmp_path`, and the shared read-scope fixture belongs to the sibling module.**
  The ten destination cases take `tmp_path` and build their vault root under it; this module does not
  import `read_scope_test_support.build_read_scope_fixture` or its `ReadScopeFixture` at all — that shared
  real-dataset fixture is what `test_knowledge_projection_vault_safety.py` consumes, and the case-level
  vocabulary here is the three local builders.
- **The modules under test are imported by their public names.** `ManagedProjectionWriter` and
  `ProjectionHooks` come from `agents_remember.memory.knowledge.managed_projection`; the class set, the
  registry, the ordering inputs, the provenance builders and `MechanicalRuleNotRegistered` come from
  `agents_remember.models.knowledge.classification`; the manifest vocabulary plus
  `detect_destination_collisions` and `require_confined_relative_path` come from
  `agents_remember.models.knowledge.projection_manifest`; the view vocabulary and its helpers come from
  `agents_remember.models.knowledge.view`. No case reaches a private name.
- **No parametrisation.** The six offending paths are a tuple iterated inside one case and each is named in
  its assertion message, and the two bounding directions are two named cases rather than one parametrised
  pair, so a failure says which spelling or which direction failed.
- **Nothing is mocked.** There is no `monkeypatch`, no patched module and no substitute store: the only
  "real" inputs are a temporary directory, a real `os.symlink`, real manifest bytes on disk, and the
  writer's own declared `ProjectionHooks` seam for the interruption. The vault-safety case that must fail
  mid-publication raises from that hook instead of sleeping, spawning a thread or sending a signal. The §6
  cases add one stub, `_RegistrationConfig`, and it stands in only for the registration-time runtime config
  (`register_knowledge_tools` reads `workspace_root` and nothing else), so the registered handlers, the
  server and the dataset they are driven against are all real and nothing under test is replaced.
- **Assertions name the thing they are about.** The forbidden-read sweep reports `(rule.rule_id, read)`,
  the path case reports the offending path, the no-database reason is stated in the module docstring, and
  the manifest cases compare whole dictionaries (`retained`, `states`, `authorized`) rather than probing
  single keys, so a discrepancy in any entry is visible.

### Invariants And Boundaries

- **Two classes, and no third.** The class tuple is asserted as exactly two members, both mixed forms are
  refused, and a class with no evidence is refused rather than defaulted.
- **A mechanical determination is a registry entry.** Nothing produces a classification from a rule the
  registry does not carry, at either the builder or the position validator, and no registered rule reads a
  name, a path, a depth, an extension or a score.
- **Ordering is admitted or refused, never defaulted.** A fifth ordering input yields a typed refusal with
  no rows, and every position names the registered declared tiebreak that placed it.
- **Bounding is one statement with two refusals.** Rows remaining and a continuation must agree in both
  directions, and a continuation is valid only against the snapshot that minted it.
- **Absence is stated, never zero.** A quantity without meaning for a view carries `not_applicable`, no
  value and a reason, and a stated absence carrying a value is refused.
- **The manifest is the only authority on ownership.** An unreadable manifest refuses instead of treating
  the destination as unowned, a duplicate path is refused, and an unlisted file is not the substrate's to
  remove.
- **Publication is atomic from the destination's point of view.** An interruption between staging and the
  first rename leaves the destination byte-identical, and the escaping-path and collision refusals are
  taken over the whole plan before anything is staged.
- **An external edit is reported, preserved and never adopted.** The prior digest survives in the manifest,
  so the same edit is detected on the next run, and the only route to an overwrite is an explicit per-path
  authorization.
- **The storeless cases do not reach the application seam; the §6 group does, deliberately.** No
  vocabulary, classification, ordering, bounding or writer case calls `read_knowledge_view` or
  `project_knowledge`, opens a store or runs a renderer end to end — they measure the declared vocabulary
  and the writer, and the real-dataset acceptance run is the sibling module's job. The eight §6 cases are
  the exception and exist because of it: they drive the **registered** handlers through a real `FastMCP`
  server, so one case per family measures the family's own refusal path rather than its roster row.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring fixes the clause group, the reason the cases need no database, and names the leaf's four load-bearing cases — two of which are the sibling acceptance module's. | "Most cases run without a database." | mcp/tests/test_knowledge_views_and_projection.py:1-11; mcp/src/agents_remember/models/knowledge/view.py:862-881 |
| **One snapshot constant and three local builders — a completeness statement, a rendered output and a destination profile — are the whole vocabulary every case is written against.** | `SNAPSHOT` | mcp/tests/test_knowledge_views_and_projection.py:68-105 |
| The provenance class set is closed at exactly two members, derived from the vocabulary literal rather than restated. | `test_the_class_set_is_closed_at_two_members` | mcp/tests/test_knowledge_views_and_projection.py:126-129; mcp/src/agents_remember/models/knowledge/classification.py:71-76 |
| **An authored determination carries its author and cannot cite a rule, a mechanical one names its rule and has no author, and a class with no evidence at all is refused rather than defaulted.** | `test_an_authored_classification_carries_its_author_and_cannot_cite_a_rule` | mcp/tests/test_knowledge_views_and_projection.py:119-157; mcp/src/agents_remember/models/knowledge/classification.py:319-386 |
| A rule the registry does not carry cannot produce a classification, at either the provenance builder or the registry lookup, and the identity requires both the id and the version. | `test_a_classification_needs_its_evidence_and_a_rule_the_registry_holds` | mcp/tests/test_knowledge_views_and_projection.py:164-180; mcp/src/agents_remember/models/knowledge/classification.py:105-111; mcp/src/agents_remember/models/knowledge/classification.py:272-292 |
| **The registry admits exactly one ordering rule per admitted input, is versioned, and no registered rule reads a name, a path, a depth, an extension or a score.** | `test_no_registered_rule_reads_a_name_a_path_or_a_score` | mcp/tests/test_knowledge_views_and_projection.py:191-197; mcp/src/agents_remember/models/knowledge/classification.py:94-95; mcp/src/agents_remember/models/knowledge/classification.py:114-156; mcp/src/agents_remember/models/knowledge/classification.py:168-266 |
| **An ordering input outside the four admitted ones is refused by name with no fallback order, and every admitted position names the registered declared tiebreak rather than an inline comparator.** | `test_an_unadmitted_ordering_input_is_refused_rather_than_defaulted` | mcp/tests/test_knowledge_views_and_projection.py:192-223; mcp/src/agents_remember/models/knowledge/view.py:445-495; mcp/src/agents_remember/models/knowledge/view.py:498-522 |
| **The bounding-honesty rule is one statement measured in both directions: rows remaining requires a continuation, and a complete page must carry none.** | `test_incompleteness_and_its_continuation_must_agree` | mcp/tests/test_knowledge_views_and_projection.py:245-274; mcp/src/agents_remember/models/knowledge/view.py:728-772 |
| A continuation presented against another snapshot is refused with both logical digests named, and the caller receives no page. | `test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named` | mcp/tests/test_knowledge_views_and_projection.py:275-285; mcp/src/agents_remember/models/knowledge/view.py:366-414; mcp/src/agents_remember/application/knowledge_views.py:106-138 |
| **A quantity with no meaning for a view states that in a reason instead of reporting a zero, and a stated absence that carries a value is refused.** | `test_a_quantity_with_no_meaning_for_a_view_says_so_instead_of_reporting_zero` | mcp/tests/test_knowledge_views_and_projection.py:275-291; mcp/src/agents_remember/models/knowledge/view.py:211-242; mcp/src/agents_remember/models/knowledge/view.py:273-331 |
| The curation queue's work item has no field for a disposition, a rationale or an author, and the row's own disposition stays absent until a curator authors one. | `test_the_curation_queue_keeps_a_work_item_free_of_any_curator_judgement` | mcp/tests/test_knowledge_views_and_projection.py:294-313; mcp/src/agents_remember/models/knowledge/view.py:656-668; mcp/src/agents_remember/models/knowledge/view.py:686-692 |
| **A mechanical no-consequence statement is refused when it carries a stored claim it did not author, and an authored one names the stored claim, its author and its rationale.** | `test_a_no_consequence_statement_is_refused_without_the_class_that_produced_it` | mcp/tests/test_knowledge_views_and_projection.py:316-345; mcp/src/agents_remember/models/knowledge/view.py:525-549 |
| A path that is not purely destination-relative is refused syntactically before any real-path resolution, and a case collision names both paths and both stable identities without inventing a suffix. | `test_a_case_collision_names_both_paths_and_both_records` | mcp/tests/test_knowledge_views_and_projection.py:383-395; mcp/src/agents_remember/models/knowledge/projection_manifest.py:448-488; mcp/src/agents_remember/models/knowledge/projection_manifest.py:491-516 |
| **The first projection writes a generation-one manifest recording path, identity, snapshot, renderer version and digest; a dropped output nobody edited is removed while an edited one is retained with its reason; an externally edited output is reported and never overwritten; and the per-path authorization is the only overwrite route.** | `test_the_first_projection_writes_a_generation_one_manifest` | mcp/tests/test_knowledge_views_and_projection.py:390-516; mcp/src/agents_remember/models/knowledge/projection_manifest.py:211-229; mcp/src/agents_remember/models/knowledge/projection_manifest.py:252-328; mcp/src/agents_remember/memory/knowledge/managed_projection.py:271-288; mcp/src/agents_remember/memory/knowledge/managed_projection.py:550-622 |
| **An escaping path and a collision each refuse the whole plan before anything is written, a symlinked destination entry is not followed while the remaining outputs continue, an interruption between staging and the first rename leaves the destination byte-identical, and the destination is never swept.** | `test_an_escaping_path_refuses_the_whole_plan_and_writes_nothing` | mcp/tests/test_knowledge_views_and_projection.py:519-618; mcp/src/agents_remember/memory/knowledge/managed_projection.py:325-379; mcp/src/agents_remember/memory/knowledge/managed_projection.py:383-432; mcp/src/agents_remember/memory/knowledge/managed_projection.py:480-548 |
| An unreadable manifest refuses rather than treating the destination as unowned, and the manifest itself refuses two owners for one path. | `test_the_manifest_refuses_two_owners_for_one_path` | mcp/tests/test_knowledge_views_and_projection.py:678-692; mcp/src/agents_remember/models/knowledge/projection_manifest.py:252-328; mcp/src/agents_remember/memory/knowledge/managed_projection.py:292-323 |

## Cross-Repo References

No cross-repository behavior is exercised in this file. Its inputs are this repository's own declared
shapes plus a temporary directory the case creates and owns; nothing it asserts reaches a second
repository, a network, a durable store or a Git object.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T01:25+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared both enforced citation rows this card carried (`citation_anchor_absent_from_range`), by renaming the dead anchor cells to the surviving constructs the previous pass had already identified and range-corrected.** The two named tests exist nowhere in the tree: `test_an_unregistered_rule_cannot_produce_a_classification` is now the foreign-rule direction of `test_a_classification_needs_its_evidence_and_a_rule_the_registry_holds` at `:164` — its own docstring says *"Two directions of one rule … Requirement 2.2 with its own contrapositive, merged because both measure whether a classification can exist without the input it is defined by: an unregistered rule cannot produce one, and a class whose evidence is missing cannot be emitted as classified either"* — and its cited range `:164-180` is that merged case's own extent (`:183` starts the next case). `test_a_payload_with_rows_remaining_must_carry_a_continuation` is now `test_incompleteness_and_its_continuation_must_agree` at `:245`, whose docstring says *"One statement about one pair of fields, so one case: a bounded response never presents its first page as the whole scope, and a page that says it is complete never carries the token that says it is not"*; its cited range `:245-274` already held that construct. Only the two Anchor cells changed: both Finding texts, the four code-side ranges (`classification.py:105-111`, `:272-292`, `view.py:728-772`) and every other row are untouched, and no citation was dropped. One residual is recorded rather than repaired: the `### Logic` prose at `:68` and `:91` still names the two pre-merge cases, because this pass's mandate is the claim's Anchor cell and body prose is not a citation row — the owning curator can align that prose with the surviving constructs. The two rows are now current; reviewed against the working candidate `ar/260915-ks-l30-ar`, no commit exists for these bytes and the commit stamp is not advanced.
- 2026-09-20T01:01:54+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): the card's 2 enforced citation rows (citation_anchor_absent_from_range ×2) both named tests that exist nowhere in the tree, and both facts are still measured — the source says so itself. `test_an_unregistered_rule_cannot_produce_a_classification` is now the first direction of `test_a_classification_needs_its_evidence_and_a_rule_the_registry_holds` ("Requirement 2.2 with its own contrapositive, merged because both measure whether a classification can exist without the input it is defined by"), so its node range moved from `mcp/tests/test_knowledge_views_and_projection.py:173-179` to `:164-180`, the merged node's own extent. `test_a_payload_with_rows_remaining_must_carry_a_continuation` is now `test_incompleteness_and_its_continuation_must_agree` ("Requirement 3.3 in both directions ... so one case"), so its node range moved from `:231-259` to `:245-274`. Both rows' dead anchor cells were left exactly as they stand — re-wording a claim is outside this residue pass — so these two rows are reported, not claimed clear. No claim wording, anchor or other range was changed; the code-side ranges (`classification.py:105-111`, `:272-292`, `view.py:728-772`) were left untouched, and no verification stamp was advanced.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `test_the_class_set_is_closed_at_two_members` repointed to mcp/tests/test_knowledge_views_and_projection.py:126-129. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `test_an_unregistered_rule_cannot_produce_a_classification` repointed to mcp/tests/test_knowledge_views_and_projection.py:173-179. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `test_no_registered_rule_reads_a_name_a_path_or_a_score` repointed to mcp/tests/test_knowledge_views_and_projection.py:191-197. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `test_a_continuation_presented_against_another_snapshot_is_refused_with_both_named` repointed to mcp/tests/test_knowledge_views_and_projection.py:275-285. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `test_a_case_collision_names_both_paths_and_both_records` repointed to mcp/tests/test_knowledge_views_and_projection.py:383-395. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `test_the_manifest_refuses_two_owners_for_one_path` repointed to mcp/tests/test_knowledge_views_and_projection.py:678-692. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:27+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): corrected this card against a source that now pins **§1 and §6** as well as §2/§3/§5 — **39 unit-regression cases, not 30**. Nine cases are new in this change set: the §1.1 literal that asserts the five view names and their order (the module's only assertion that cannot be satisfied by iterating `VIEW_NAMES`), and eight §6 cases that drive the **registered** `knowledge_*` handlers through a real `FastMCP` server — one refusal per operation family (`unadmitted_ordering_input`, `unknown_view`, `continuation_unreadable`, `registration_absent`, `selected_input_unavailable`, an integrity report with `compatible is None`, `unresolved_projection_input`) plus one that asserts the five mounted names are exactly the five the module calls. Four body claims were false and are corrected: the Purpose's clause set and case count; the `### Logic` claim that the module runs without a database because nothing it measures has one inside it; the `### Conventions` claims that the module declares no marker of its own (the §6 cases carry `@pytest.mark.anyio`) and that nothing is stubbed (they use a `_RegistrationConfig` stub for the registration-time config only, with the handlers, the server and the dataset left real); and the `### Invariants And Boundaries` claim that nothing here reaches the application seam. The §6 group is unit-lane by construction — its dataset is built in-process under `tmp_path`, with no subprocess and no network — and the integration lane is at 400/400 in this change set (seat W1's measurement, not this pass's), so an integration row was not available. Item 25's typing fix in this module (the `report.manifest is not None` assertion before its `outputs` are read) is recorded in the same edit. Verification metadata is unchanged and closeout owns the stamp; the `reviewedWorkingCandidate` row now names this leaf's candidate. **This entry claims no pyright count** — the gate's form is the broad whole-project run and this pass ran no pyright — **and no execution result**: no case was run in this pass.
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): created this one-to-one card for the `KS-R20@v1` §2/§3/§5 unit suite. It records the thirty cases in clause order: the two-member class set with both provenance refusals and the no-evidence refusal, the closed versioned registry with one rule per admitted ordering input and no rule reading a name, a path or a score, the ordering admission gate beside the declared tiebreak every position must name, the two bounding-honesty directions, the continuation refused against another snapshot with both digests named, the quantity that states its own not-applicability, the two payload shape obligations of requirement 1.6 and 2.3, and the eleven cases of the vault-safety writer section, ten of them over a real temporary destination — the generation-one manifest, the unchanged orphan removed beside an edited one retained, the externally edited output reported and preserved, the per-path authorization as the only overwrite route, the whole-plan refusals for an escaping path and a collision, the symlink that is not followed, the interruption that leaves the destination byte-identical, the absent sweep, the unreadable manifest and the duplicate owner. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
