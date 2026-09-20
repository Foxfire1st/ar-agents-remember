# mcp/tests/test_workflow_chain_guidance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_workflow_chain_guidance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T00:08+0200 |
| lastVerifiedCommitHash | `4346e6979a9bb628bd07bd83957917e1b157f32b`|
| lastVerifiedCommitDate | 2026-09-20T15:23:19+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l8-ar` uncommitted source (new file, **1442 lines / 12 cases**, sha256 `2225c95ba8624286c770ea1060dd3235d5e0a9a2851ec4db830819e0c800b3e1`); base `d9214edf` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

Working candidate verification: this file is new in `260918-TSIP-L8` and **no commit carries its
bytes**, so `lastVerifiedCommitHash` names the base the leaf was cut from rather than a commit that
contains this source; it does not claim the uncommitted content was verified at that commit. The
`reviewedWorkingCandidate` row names the exact candidate and its digest, and the governed closeout
owns the real stamp. Every claim below was read against that candidate, and every cited range was
re-read from the candidate's own bytes rather than carried from a report.

## Purpose

The AR workflow as **one ordered path**, kept true by a test run rather than by a document. A trace
that lives in a task root is not a landing, so the workflow statement this leaf owns is re-derived at
every revision: the operations run in order through the registered entry points, each response's
guidance is checked against **the caller's own contract**, and every step the guidance recommends is
**called** rather than read.

The defect class it exists for is `T44`/`T108` — *a machine-readable next action that does not work*.
Every unit test of the guidance passed while the guidance was internally consistent and externally
unusable, because nothing walked the chain and followed its own advice. Three properties are asserted
over populations **derived at run time**: the hops come from executing the chain, the guidance
channels come from each response the chain produced, and the arguments a recommendation supplies are
read from the product's own guidance state machine over the contract on disk. The only literal
sequences in the module are `WORKFLOW_OPERATIONS` — which *is* the workflow statement, and is
asserted against what the walk observed — and value fixtures for arguments a recommendation leaves to
the caller.

It also carries the module-level statement of three register findings it does **not** repair:
`T108` (a recommendation naming an operation its own argument model refuses), `T109` (the
`nextRequiredArgs` channel that cannot declare what the operational triple omits), and `T87`/`T34`'s
stale-base raiser.

## Code Commentary

### Logic

Twelve cases, one shared disposable world per class, `unittest.TestCase` throughout, no `pytest` marks.

- **The order** (`test_the_chain_runs_in_the_declared_order_through_the_registered_entry_points`,
  `:1038-1053`; `…reaches_every_declared_state_and_the_terminal_contract`, `:1055-1068`;
  `…each_hop_was_the_move_the_previous_response_named`, `:1070-1104`). `WORKFLOW_OPERATIONS`
  (`:98-108`) is nine operations, with `worktree_integrate` and `lifecycle_finalize_task` appearing
  **twice on purpose** — each is a preview followed by its apply, and the preview is the step `T62`
  broke. Case 1 asserts tuple equality against the observed hops, so a skipped or reordered hop
  changes the tuple and reds it; it also asserts every hop is on `PUBLIC_TOOLS` and that no hop lost
  its envelope. Case 2 asserts each operation's own state vocabulary (`EXPECTED_STATES`, `:112-121`)
  plus the terminal `cleanup` cell, and the phase progression (`EXPECTED_PHASES`, `:124-129`) read
  from the product's state machine over the real contract file. Case 3 *derives* the order from the
  guidance rather than asserting it beside it: where a response names a forward move, the next hop
  taken must be that tool, and the case bounds its own derivation (`forward >= 4`, `holds >= 1`).
- **The two guidance channels** (docstring `:35-49`; `_recommendation`, `:615-644`;
  `test_every_guidance_channel_names_the_callers_own_task`, `:1108-1126`). A worktree response carries
  the **operational triple** `nextAction`/`nextTool`/`nextArgs`
  (`mcp/src/agents_remember/models/worktree.py:356-358`), produced from the response's own contract by
  `guidance.py`; and `nextStep`, the **lifecycle overlay** computed at the choke point from the
  process-global ambient lifecycle (`mcp/src/agents_remember/application/next_step.py:260-260`) and
  filtered by `bound_next_step` (`mcp/src/agents_remember/application/tool_response.py:58-58`). They
  are read as two, because a case that inspects only `nextStep` reports "withheld" where the seat in
  fact received the same operational move top-level.
- **The address guard, with its arrangement asserted** (`_sibling_arrangement`, `:799-847`;
  `test_a_concurrent_siblings_guidance_never_reaches_this_task`, `:1128-1162`). `T54` was systematic:
  guidance derived from the process-global lifecycle named a concurrent session's enclosure. The case
  asserts the arrangement **first** — the unguarded guidance MUST name the sibling enclosure
  (`:1142-1151`) — so a green cannot mean the guard was never exercised, and then asserts no channel
  of this task's response names the sibling while the operational channel still names this task's
  move.
- **The derived callability population** (`callability_population`, `:997-1012`; `_as_given_call`,
  `:680-700`; `classify_call`, `:237-251`; `missing_required_args`, `:254-262`;
  `GUIDANCE_STEPS_MISSING_REQUIRED_ARGS`, `:165-167`;
  `test_every_recommended_step_is_callable_with_the_args_its_guidance_supplies`, `:1166-1185`). Each
  hop is called first with **exactly what its own guidance supplied** (plus the arguments that
  guidance itself declares as required), then again with only the fields the tool's own argument model
  named as absent — so the chain can continue, because a check that stopped at the refusal could not
  tell an unusable recommendation from a broken chain. The two failure arms are separated by **model
  identity**, never by wording: the generated `<tool>Arguments` model refusing the call is an unusable
  recommendation, any other raise lost the envelope. The pin is asserted **equal in both directions**,
  so a recurrence and a widening both fail.
- **The operational-triple probe** (`_probe_operational_triples`, `:902-918`; `_call_recommendation`,
  `:888-900`; `RecommendedCall`, `:320-333`;
  `…every_response_that_published_an_operational_triple_was_called_with_it`, `:1187-1237`). Every hop
  that publishes a `nextTool`/`nextArgs` triple is called **verbatim**, and the second producer of the
  same recommendation — `worktree_start(retry_provider_setup=True)` answering `blocked` — is **driven**
  in the same world rather than cited (`_retry_provider_setup_arrangement`, `:920-993`). The
  population is asserted so it cannot silently shrink, and the negative fact is stated rather than left
  implicit: the only operations publishing no triple are the two terminal `lifecycle_finalize_task`
  calls (`:1234-1237`).
- **The classifier's own control** (`test_the_callability_arm_can_actually_fail`, `:1239-1269`).
  `worktree_closeout_apply` called with nothing must be refused by **its own** model with
  `{contract_path, intent_note}`, the one-field-short shape must classify alike (the singular and
  plural refusal spellings), and a call that loses its envelope entirely must classify `raised` —
  otherwise an "answered" classification could be satisfied by a classifier that never refuses.
- **The withhold, counted** (`WITHHELD_GUIDANCE_HOPS`, `:178-183`;
  `…the_guidance_that_could_not_be_validated_is_withheld_and_counted`, `:1271-1292`). A response that
  declares no camelCase address cannot vouch for guidance derived from the process-global lifecycle,
  so the hint is withheld rather than emitted unchecked; the case pins the count by tool and asserts
  non-vacuity (a withheld hop must still publish the same move top-level, which is why the withhold
  costs this chain nothing today).
- **The previews and `T62`'s trigger** (`_walk`, `:769-791`;
  `…every_preview_step_answered_and_the_drift_snapshot_was_actually_read`, `:1296-1336`). The drift
  snapshot is planted at the producer's own path (`drift_snapshot_path`,
  `mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:21-21`) before the cleanup and finalize
  previews; the case asserts it was **present** when they ran, that every preview answered
  (`would-*`/`closed`), that the snapshot **survived** the previews, and that the **real** finalize
  reclaimed it — so the preservation claim is not an artefact of nothing ever touching the file.
- **The stale base and its raiser** (`STALE_BASE_RAISERS`, `:196-196`; `_stale_base_arrangement`,
  `:849-884`; `test_a_stale_base_closes_the_envelope_by_raising_and_is_counted`, `:1338-1367`). The
  arrangement is measured, not described: the sibling enclosure's source branch is advanced the way a
  sibling's landing advances it, `worktree_sync` must answer `would-sync` (or the arm tested nothing),
  and the closing operations are driven in exactly that state. `worktree_closeout_preview` raises
  `SourceLineageRefusal` (`mcp/src/agents_remember/worktrees/modules/closeout_lineage.py:68-68`), so
  the caller loses `ok`, `status` and every recovery key; the remedy (`worktree_sync`) is asserted to
  exist **in the exception text only**. The pin is asserted equal in both directions.
- **The declared-requirement channel, `T109`**
  (`test_the_declared_requirement_channel_is_real_and_its_one_needed_case_is_unreachable`,
  `:1371-1442`). Three measured facts in order: where the channel is reachable the product uses it
  (the `cleanup-pending` phase declares `contract_path` for `lifecycle_finalize_task`, read at the one
  walk moment that phase is live); the phase that declares `intent_note` (`closeout-pending`) is
  **unreachable from the tools' own writers**, because the real apply leaves `approved_for_commit` and
  `closeout_status: completed` in the *same* contract write
  (`mcp/src/agents_remember/worktrees/modules/closeout.py:481-497`); and the declaration is
  nonetheless real, asserted on the contract state that defines it — the real post-apply contract with
  only `closeout_status` rewritten.

### Conventions

One hermetic world per class (`WorkflowWorld`, `:336-569`): a single `TemporaryDirectory`, two real
Git repositories with remote-tracking authority, real task documents, a real server built by
`create_server`, and a real in-memory MCP client session per call (`:402-414`, through
`create_connected_server_and_client_session`). `declare_test_process()` is called on
construction (`:340-340`). No Docker, no network, no writes outside the temporary tree.

Every call goes through the **production entry point** — a registered tool over an MCP session — and
`call` returns a three-way arm (`RAISED ToolError` with the payload, `RAISED <Exception>`, or
`RETURNED` with `structuredContent`), so "did it raise" is itself the measurement.

The lane row is `unit-regression` (`mcp/tests/test-evidence-lanes.toml:201-201`, inside the array
that opens at `:5-5`), which is the lane the default selection collects, so the module is in the unit
population a full run reaches. The registry loader is what makes the row load-bearing: the round-1
worker ran the module **before** its row existed and the loader refused it — *"test files without an
explicit lane"* — and on this candidate the loader plus budget screen read **10 passed** (measured by
this pass, `mcp/tests/test_evidence_lanes.py` + `mcp/tests/test_suite_budget.py`, `-n0`, no override).

### Invariants And Boundaries

- **The pins are the workflow statement's, and they are exact in both directions.**
  `GUIDANCE_STEPS_MISSING_REQUIRED_ARGS` (`:165-167`) carries exactly one entry,
  `worktree_closeout_apply` → `{intent_note}`, which is a **registered residual** rather than a
  tolerated omission: the fix belongs to the tool surface and the module's comment says so. Rule
  stated at `:132-136`: repair it and delete the entry in the same change; never delete the constant,
  never widen it.
- **"Every recommended step is callable" is not what this module proves, and the honest statement is
  narrower.** What it pins is the callability of the recommendations **the walk reaches**, over the
  union of each hop's as-given call and every hop's own operational triple plus the one driven retry
  producer. Three residuals lie outside that producer set and are registered, not repaired:
  **`T127`** — the lifecycle-operation `recommendedAction` channel
  (`mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:450-453`,
  where `:450` is the call and `:452` the `tool=` argument) recommends `worktree_status` with
  `{"contract_path"}` only, on a key that is *not* `nextTool`/`nextArgs`, so the module's probe
  structurally cannot see it; **`T130`** — a fourth `nextTool`/`nextArgs` producer,
  `_projection_without_control` (`mcp/src/agents_remember/application/task_docs/task_unstarted_evidence.py:535-545`),
  whose `RecoveryRoute` tuple (`:48-48`) is unpacked and published as `nextTool`/`nextArgs` by
  `public_payload` (`:68-80`); and **the phase channel's second repaired site** below.
- **The phase channel is pinned at ONE of its two repaired sites.** `guidance.py` carries
  `repo_id=contract.repo_name` on two `worktree_status` recommendations — `:369-369` (the
  `integration_status == "checkpointed"` branch of `_post_integration_phase`, phase
  `worktree-started`) and `:451-451` (`_pre_integration_phase`, the pre-integration step). The walk
  reaches only the second, so a **targeted** removal of `repo_id` at `:369` leaves this module at
  **12 passed**. The successor verification's two-site mutation reds the module, but its red is fully
  explained by `:451-451` alone, and that evidence shape must not be read as covering both. The bytes
  are correct at both sites; this is a coverage boundary, and it is `T114`'s class.
- **The coverage case's population is every hop plus one named producer, not "every response".** Its
  `expected` and `observed` sets are *both* derived from `self.hops` (`:1198-1204`), so it
  structurally cannot notice a triple-bearing response that is not a hop. The successor verification
  measured the gap rather than assuming it: in this fixture the only responses built outside the walk
  publish no triple, so the derivation is safe here — but the honest statement of the population is
  the narrower one.
- **The `A5c` limit is stated in the module rather than left to be discovered.** The phase machine
  declares requirements in four places; the `T109` case pins two (the reachable `cleanup-pending` and
  the defining `closeout-pending`) and the docstring at `:1397-1406` says so. Deleting the
  `carryover-pending` declaration (`guidance.py:321-321`) leaves the module green — green **by
  design**, and reproduced as such by the verification's `A5c` mutation.
- **The module proves the mechanism and pins the populations; it repairs neither.** `T108`'s residual,
  `T109`'s missing field and `T34`'s stale-base raiser are statements this module carries for their
  owners, and the `### Todos` below record the same.
- **Dead code and an unread field, recorded rather than smoothed.** `_apply_half` (`:605-613`) is
  defined and never called, and `Hop.as_given_arm` — the field that carries *whether the guidance was
  followable at all* — is written and read by no assertion; the callability signal that survives into
  a case is `missing_args` alone, which case 6 pins. In case 10's preview predicate the arm
  `hop.state == "closed"` cannot be satisfied by any preview the walk takes (every preview answers
  `would-*`), so it is an assertion arm that cannot fail; case 2's `EXPECTED_STATES` is what would
  catch a preview that actually applied.

### Todos

Verification metadata remains closeout-owned; this card records source inspection only. Owed to
whatever change next touches the module: the three registered residuals above (`T127`, `T130`, the
`guidance.py:369-369` coverage boundary), the dead `_apply_half` and the unread `Hop.as_given_arm`
(either assert them or delete them), and the `nextRequiredArgs` pin `T109` asks for once the tool
surface ships the field.

## Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned contract and assertion facts; no external library behaviour is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The anchors below identify current behaviour of this module; they are not execution evidence and they
make no acceptance claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| The workflow statement: nine operations, with the two preview/apply pairs appearing twice on purpose. | `WORKFLOW_OPERATIONS` | mcp/tests/test_workflow_chain_guidance.py:98-108 |
| Each operation's own state vocabulary, and the terminal cleanup cell. | `EXPECTED_STATES` | mcp/tests/test_workflow_chain_guidance.py:112-121 |
| The phase progression, read from the product's state machine and never restated from a literal. | `EXPECTED_PHASES` | mcp/tests/test_workflow_chain_guidance.py:124-129 |
| The callability pin, with the repair rule stated at the constant. | `GUIDANCE_STEPS_MISSING_REQUIRED_ARGS` | mcp/tests/test_workflow_chain_guidance.py:165-167 |
| The withhold pinned by tool and count, so repairing the producers is a visible edit. | `WITHHELD_GUIDANCE_HOPS` | mcp/tests/test_workflow_chain_guidance.py:178-183 |
| The raisers that escape as an exception instead of a typed refusal (`T34` on `T87`'s state). | `STALE_BASE_RAISERS` | mcp/tests/test_workflow_chain_guidance.py:196-196 |
| Values for arguments a recommendation leaves to the caller — values, never a population. | `FIXTURE_ARGS` | mcp/tests/test_workflow_chain_guidance.py:200-206 |
| The two refusal arms separated by model identity, never by wording. | `classify_call` | mcp/tests/test_workflow_chain_guidance.py:237-251 |
| The fields a tool's own argument model named as required and absent. | `missing_required_args` | mcp/tests/test_workflow_chain_guidance.py:254-262 |
| One operation, what its own guidance supplied, and what came back. | `Hop` | mcp/tests/test_workflow_chain_guidance.py:272-316 |
| One response's own operational triple, and what calling it exactly as published produced. | `RecommendedCall` | mcp/tests/test_workflow_chain_guidance.py:320-333 |
| The disposable world: real repositories, a real server, one session per call. | `WorkflowWorld` | mcp/tests/test_workflow_chain_guidance.py:336-569 |
| Invoking one registered tool exactly as a consumer does, with the raise itself as the arm. | `call` | mcp/tests/test_workflow_chain_guidance.py:402-414 |
| The single walk of the chain, the hops it produced, and the three arrangements. | `WorkflowChainObservation` | mcp/tests/test_workflow_chain_guidance.py:572-1020 |
| What the guidance supplies for a hop, and the arguments it declares as required. | `_recommendation` | mcp/tests/test_workflow_chain_guidance.py:615-644 |
| The first call exactly as given, then again with only what the model named as missing. | `_as_given_call` | mcp/tests/test_workflow_chain_guidance.py:680-700 |
| Execute one recommended step as given, then again with only the arguments it omitted. | `_record` | mcp/tests/test_workflow_chain_guidance.py:702-743 |
| The ordered walk, the sibling arrangement, the retry producer, the stale base, the probe. | `_walk` | mcp/tests/test_workflow_chain_guidance.py:745-797 |
| The `T54` arrangement, asserted before the property so a green cannot mean it tested nothing. | `_sibling_arrangement` | mcp/tests/test_workflow_chain_guidance.py:799-847 |
| The stale base driven through the tools, with `worktree_sync` required to answer `would-sync`. | `_stale_base_arrangement` | mcp/tests/test_workflow_chain_guidance.py:849-884 |
| Every hop's own triple called verbatim, so the channel a case does not call is not a channel it can see. | `_probe_operational_triples` | mcp/tests/test_workflow_chain_guidance.py:902-918 |
| The second producer of the same recommendation, driven in the same world rather than cited. | `_retry_provider_setup_arrangement` | mcp/tests/test_workflow_chain_guidance.py:920-993 |
| The union of the walk's own as-given calls and every probe, asserted equal to the pin. | `callability_population` | mcp/tests/test_workflow_chain_guidance.py:997-1012 |
| The order, asserted against what the run actually did rather than stated beside it. | `test_the_chain_runs_in_the_declared_order_through_the_registered_entry_points` | mcp/tests/test_workflow_chain_guidance.py:1038-1053 |
| The order derived from the guidance, with the derivation's own bound. | `test_each_hop_was_the_move_the_previous_response_named` | mcp/tests/test_workflow_chain_guidance.py:1070-1104 |
| Guidance must name the response's own place, on every channel it uses (`T54`). | `test_every_guidance_channel_names_the_callers_own_task` | mcp/tests/test_workflow_chain_guidance.py:1108-1126 |
| The sibling arrangement asserted first, then the property (`T54`'s arm). | `test_a_concurrent_siblings_guidance_never_reaches_this_task` | mcp/tests/test_workflow_chain_guidance.py:1128-1162 |
| The derived population, asserted equal to the pin over both channels. | `test_every_recommended_step_is_callable_with_the_args_its_guidance_supplies` | mcp/tests/test_workflow_chain_guidance.py:1166-1185 |
| The population of the case above, so it cannot silently shrink — with its own boundary stated. | `test_every_response_that_published_an_operational_triple_was_called_with_it` | mcp/tests/test_workflow_chain_guidance.py:1187-1237 |
| The classifier's control: an unusable recommendation must be seen as one. | `test_the_callability_arm_can_actually_fail` | mcp/tests/test_workflow_chain_guidance.py:1239-1269 |
| The withhold is real, counted, and explained in both directions. | `test_the_guidance_that_could_not_be_validated_is_withheld_and_counted` | mcp/tests/test_workflow_chain_guidance.py:1271-1292 |
| `T62`'s trigger: the snapshot present, every preview answering, preserved, then reclaimed. | `test_every_preview_step_answered_and_the_drift_snapshot_was_actually_read` | mcp/tests/test_workflow_chain_guidance.py:1296-1336 |
| The stale base driven, and the raiser pinned by set equality. | `test_a_stale_base_closes_the_envelope_by_raising_and_is_counted` | mcp/tests/test_workflow_chain_guidance.py:1338-1367 |
| `T109`: the declaring channel asserted where it is defined, and its four-phase population stated. | `test_the_declared_requirement_channel_is_real_and_its_one_needed_case_is_unreachable` | mcp/tests/test_workflow_chain_guidance.py:1371-1442 |
| The lane row that keeps this module in the default selection, inside the array opening at `:5`. | "mcp/tests/test_workflow_chain_guidance.py" | mcp/tests/test-evidence-lanes.toml:201-201 |
| The operational triple's declared home, and the reason it is a channel of the response's own contract. | `nextArgs` | mcp/src/agents_remember/models/worktree.py:356-358 |
| The overlay's model, which can declare what it leaves to the caller and the operational triple cannot. | `nextRequiredArgs` | mcp/src/agents_remember/models/base.py:63-63 |
| The guard that withholds a hint which cannot name the response's own place. | `bound_next_step` | mcp/src/agents_remember/application/tool_response.py:58-58 |
| The process-global ambient lifecycle the overlay is derived from, which is why the guard exists. | `next_step_for` | mcp/src/agents_remember/application/next_step.py:260-260 |
| The producer that writes `approved_for_commit` and `closeout_status: completed` in one contract write. | `_amended_closeout_contract` | mcp/src/agents_remember/worktrees/modules/closeout.py:481-497 |
| The snapshot path the preview's drift collection actually reads, derived from worktree and branch. | `drift_snapshot_path` | mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:21-21 |
| The real reclamation the preservation claim is measured against. | `remove_drift_snapshot` | mcp/src/agents_remember/kernel/primitives/drift_snapshot.py:27-31 |
| The exception a stale base escapes as, carrying the remedy in prose only. | `SourceLineageRefusal` | mcp/src/agents_remember/worktrees/modules/closeout_lineage.py:68-68 |
| The repaired pre-integration recommendation the walk reaches (`guidance.py:451`). | `_pre_integration_phase` | mcp/src/agents_remember/worktrees/modules/guidance.py:375-453 |
| The repaired `checkpointed` recommendation the module does **not** reach (`guidance.py:369`). | `_post_integration_phase` | mcp/src/agents_remember/worktrees/modules/guidance.py:287-369 |
| The declaration `T109` pins where it is defined; it is at `:433`, not the `:432` two reports cite. | `required_args` | mcp/src/agents_remember/worktrees/modules/guidance.py:433-433 |
| The declaration `A5c` shows is not asserted (`carryover-pending`). | `required_args` | mcp/src/agents_remember/worktrees/modules/guidance.py:321-321 |
| The `recommendedAction` residual (`T127`): the call at `:450`, the `tool=` argument at `:452`. | `LifecycleRecommendedAction` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:450-453 |
| The `RecoveryRoute` producer (`T130`) that publishes an uncallable triple as `nextTool`/`nextArgs`. | `_projection_without_control` | mcp/src/agents_remember/application/task_docs/task_unstarted_evidence.py:535-545 |
| The tuple shape `T130` rests on: the value is a tuple element, not a tool-shaped key. | `RecoveryRoute` | mcp/src/agents_remember/application/task_docs/task_unstarted_evidence.py:48-48 |
| Where the tuple becomes the operational triple a seat reads. | `public_payload` | mcp/src/agents_remember/application/task_docs/task_unstarted_evidence.py:68-80 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local contract claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No repository or external-system boundary is proved by this module. | N/A | N/A |

## 260918-TSIP-L8 The Workflow Statement's Own Acceptance Module

This card is created by the leaf's **curator**, not by the worker who wrote the module: a worker
editing the memory tree is the role boundary this master registered as `T105`. The module is **new in
this leaf** — 1442 lines, 12 cases, sha256 `2225c95b…` — and before this card it had no file-level
onboarding at all, which the leaf's own fix round recorded as a handoff (`T120`).

**The trees, both named (`T100`).** Every number this card states was measured on the **leaf memory
worktree** at `877a5a003af6c6a11b488f8cc30ad4b4dfb05fb1` paired with the **leaf code worktree's**
`d9214edf3388ee862f8c8f2ed59cf40af710d8bb` plus this leaf's five uncommitted entries. That pair is
**one behind the master on both axes** — L7's landing is this leaf's code base and L9 has landed since
(`eca18fe6`, memory `f396e830`) — and the scoped `memory_quality_check` **refuses** on it with
`memory-candidate-pair-base-stale` (field `codeBaseCommit`, expected `d9214edf`, observed
`eca18fe6`). The refusal is **not** cleared here: the standing brief forbids syncing for curation and
the closeout syncs.

**What that refusal costs, stated rather than worked around.** The checklist, its attestation and the
census are bound to the pair identity — `controller.py::_curator_candidate_inputs` raises
*"curator publication has no exact code/memory pair identity"* and `census.py::prepare_memory_census`
returns `None` — so **those three artifacts cannot exist at this scope at all**, and this pass reports
no sha256 for them. The measurement they are built from was driven instead through the product's own
root-parameterised entry points, in the controller's own composition order, on two code arms:

```
[A] leaf code worktree  d9214edf + L8's five entries       : 292 / 121 / 3 / 2, report-only 491
[B] clean HEAD          d9214edf, a real clone, full history: 283 / 120 / 3 / 2, report-only 488
```

Arm B reproduces **L7's own frozen pin exactly** (`mcp/tests/test_memory_citation_agreement.py:498-499`
pins `283 / 120` and the `T58` pair `3 / 2`), which is what makes the delta attributable instead of
merely observed. Keyed on row identity rather than on the message (which embeds the line that moves),
the whole delta is this leaf's **code** change set, and it is named:

- **+9 enforced**, every one `citation_anchor_absent_from_range`: `closeout.py.md:438` (1),
  `landing.py.md:26` (2) and `:140` (3), `start.py.md:281` (1), and the lane registry's own card at
  `test-evidence-lanes.toml.md:1499` (1) and `:1551` (1) — the last two from inserting this leaf's row.
- **+3 report-only**, including the single row that moves the `T52` definition pin **120 → 121**:
  `onboarding/mcp/src/agents_remember/worktrees/modules/startup/start_result.py.md:60`, whose anchor's
  definition the round-2 repair to `start_result.py` shifted. That row is why the pin reads 121 on the
  pair this leaf lands, and it is **not** this card's.

The module's live arm is hermetic (`AR_ONBOARDING_ROOT` unset → the population cases `skipTest`), so a
green lane run is not evidence that the pin holds; the re-derivation belongs to the last writer
(`T122`), and this card does not move it.

**That last claim is proved on the pair it lands, and its boundary is stated.** On arm A the card
carries **0 rows in the enforced class, 0 in the report-only class and 0 in the missing-onboarding
class**, and `292 / 121 / 3 / 2` with report-only `491` are **identical before and after** it; the only
movement the card causes anywhere is `missingOnboardingCount` 1 → 0, which is the deliverable itself.
On a **pre-landing** arm the same card carries 36 enforced and 1 report-only row
(`citation_source_vanished` / `citation_anchor_absent_from_range` on this document), because the module
it documents does not exist there — which is precisely why a pin measured on a checkout that does not
contain the module is not evidence about the tree that survives, and why the re-pin is the last
writer's.

**Does a lane someone actually runs reach the module?** Yes: the row is `unit-regression`
(`mcp/tests/test-evidence-lanes.toml:201-201`), the lane the default selection collects, and on this
candidate the registry loader plus the budget screen read **10 passed** (measured by this pass, `-n0`,
no `-o` override; the declared rails are `pyproject.toml:278-279`'s `4000 / 1000`, raised from `3000 / 600` by `260918-TSIP-L13` after this pass measured them). The row is load-bearing —
the round-1 worker ran the module before the row existed and the loader refused it — so a module
cannot enter this tree unreached.

**And the second registry is a known, deliberately unrepaired obligation (`T129`).** Measured with the
product's own consumer-completeness oracle on this leaf's tree, `load_evidence_inventory` reports
**2 findings**, both naming this module's arrival: the node lockfile row
`mcp/tests/fixtures/repository_profiles/node/package-lock.json` is missing
`mcp/tests/test_workflow_chain_guidance.py` as a consumer, alongside the pre-existing
`mcp/tests/tool_refusal_census_support.py` gap that is `T106`'s. Neither is repaired here: the repair
is a code change to `mcp/tests/evidence-lifecycle.toml` and the pin files
(`test_dependency_ownership_ast_helpers.py:44-46`), this pass may not edit any code file, and the
ruling already assigns it to **L10** as a scope addition — which is also the correct sequencing,
because the rows name modules that only exist once L8 and L9 have landed.

## Update History
- 2026-09-20T00:08+0200 — 260918-TSIP-L8 curator (uncommitted change set on `ar/260918-tsip-l8-ar`, memory worktree base `877a5a00`): **created.** The module is new in this leaf (**1442 lines / 12 cases**, sha256 `2225c95b…`) and had no file-level onboarding at all. Recorded the walk and its declared order (`WORKFLOW_OPERATIONS` nine operations with the two preview/apply pairs doubled), the two guidance channels and why they must be read as two, the `T54` sibling arrangement asserted before its property, the derived callability population and the union it is asserted over, the operational-triple probe and the driven retry producer, the withhold pinned by count, the `T62` drift-snapshot presence/preservation/reclamation, the `T87` stale-base arrangement and its raiser, and the `T109` declared-requirement case. It also records the three boundaries the successor verification named **as boundaries** — the phase channel pinned at only `guidance.py:451` (`:369` alone leaves the module green), the coverage case's population derived from `self.hops`, and `A5c` green by design — and the two registered residuals outside its producer set (`T127`, `T130`). It records one citation correction: the `intent_note` declaration is at `guidance.py:433`, not `:432` as the leaf's fix-round report has it. The trees are named with both commits, the scoped quality refusal is quoted rather than cleared, and the `T129` second-registry obligation is measured on this leaf's own tree and handed to L10. **The pin measurement is stated rather than implied**: the card adds 0 rows in every class on the pair it lands (`292 / 121 / 3 / 2`, report-only 491, identical before and after it), the +9 enforced and +3 report-only rows that do move those numbers are this leaf's *code* change set and are named, and the single row behind the `T52` `120 → 121` move is `startup/start_result.py.md:60`. Verification metadata is the recorded base commit, which does not contain this file; the candidate is uncommitted and the governed closeout stamps the real code commit.
