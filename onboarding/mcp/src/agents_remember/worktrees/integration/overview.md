# mcp/src/agents_remember/worktrees/integration

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-15T00:56:17+00:00 |
| lastVerifiedCommitHash | `0dd1df9a950d59ac9622e5fb54250e528df08fa5` |
| lastVerifiedCommitDate | 2026-09-16T20:47:18+02:00|
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| governingOverview | `../overview.md` |

## Governing Overview

[worktrees overview](../overview.md)

## IAS Frozen Contract-Activation Serialization Boundary

The per-contract activation record and the sync transaction run under the same repository integration authority
that serializes protected-source movement. Remote refresh is evidence gathered before the lock;
the admitted local source tips, pinned authority refs, contract re-read, selection transition, and
base-pair finalization are proven under authority. No ambient checkout or prior queue row becomes a
second source of truth.

Terminal lifecycle cleanup releases only an exact selected terminal pointer and does so before the
canonical contract identity can be destroyed. Lifecycle/commit evidence remains in the stable
operation journal and Git proof owners; the disposable closeout projection observes readiness only.

## Purpose

The integration-authority package owns branch/ref authority, closeout-door publication and recovery,
and direct landing. Its committed L2 structure groups root-journal
generation/control/worker/location logic under `lifecycle/` and direct-landing execution and recovery
under `direct_landing/`; the remaining integration orchestration stays at this parent route. These
are ownership-preserving package moves, not compatibility copies of the former flattened modules.
The bounded schema-1 `legacy/` bridge this route once carried was deleted as a capability by the
de-entanglement cut (commit `a583beb8`, "delete the legacy operation bridge and its tool surface").
Integration no longer owns a quality gate, a publication fence, an integration-claim transfer, or an
organizational-completion boundary; all four were deleted by the closeout-door cut (commit `fad9808e`).

## Hot Path Summary

Follow `integration_ref_transaction.py` for code/memory ref publication and source-ancestry checks, `direct_landing/` for journaled memory writes, and `closeout/preparation/` for retained private outputs. No route requires a ledger commit or validates cached rows to authorize Git work.

## Detailed Route Context

Normal operation authority is locator -> immutable enclosure-root manifest -> canonical root journal. `lifecycle_operation_location.py` owns path confinement and publication state; `lifecycle_operation_binding.py` owns only the pure canonical identity/digest bytes that publication proves. This route also owns admission-time authoritative reread, generations and controls, exact Git/ref/process evidence, door/successor publication, direct landing, and integration reconciliation. The bounded schema-1 legacy repair route this summary used to list was deleted with the legacy package.

The final size/ownership split places door publication and recovery below `closeout/`, detached
worker launch/state/termination below `lifecycle/worker/`, cancellation mutation below
`lifecycle/control/`, and total journal observation below `lifecycle/observation/`. These packages
separate responsibilities without adding facades or alternate authority: mutation still requires
exact contract/journal/Git/process evidence, while observation remains read-only and task status or
queue state cannot hide retained operations.

Master integration, series closeout, closeout/reopen, and the memory carryover paths consume this
package: branch-backed authority checks (`require_*`), durable lifecycle operation leases, the
Dagger quality gate checkout, and organizational-completion repair.

MCAR exact-pair admission centralizes live code-worktree and memory-worktree identity in
`memory_quality/memory_candidate_pair.py` after the de-entanglement cut relocated it out of
`closeout/` (commit `0b63d6fc`). Configured repository authority remains strict and may
delegate only those duplicate candidate checks to that pair owner. Completed-integration reopen
policy is isolated in `closeout/integration_reopen.py`: it permits memory-only settings closeout
only when the source head is either the recorded base or the exact recorded integrated commit;
unrelated source movement still refuses.

`integration_quality.py` was deleted by the closeout-door cut (commit `fad9808e`). It had zero callers
in `src/` before that cut: the integration-time quality gate was already gone, and the module plus its
two consumers were the last of it. Normal integration therefore runs no acceptance gate of its own —
`integrate.py` contains no quality reference at all. The surviving route member
`integration_quality_checkout.py` still owns the detached exact-commit checkout context manager, and
`certification.py` still owns journal-selected frozen-run certification; both are now consumed outside
the integration path.

The closeout path uses its distinct selected operation state and an explicit continuation port for
current memory observation, Gate-5 execution, and finalization. These source boundaries do not
establish that a production continuation is installed or that the candidate has been accepted.

## Conventions

- The package keeps the `worktrees` layering altitude: it never imports the queue package's
  application layer.
- Authority refusals stay typed (`SprintLinkageError`/`CloseoutQueueError`-family or the
  `AgentsRememberError` family).

## Invariants And Boundaries

- Lifecycle operation identity/lease/store are runtime-authority surfaces (bounded, evictable).
- Integration never falls back to a host quality run; the Dagger graph owns acceptance.
- Frozen run and terminal references are selected by the live operation owner. Resume reopens
  those originals; a result payload, latest report, or another generation cannot substitute for them.
- Exact-pair consumers have one candidate-identity owner; disabling the duplicate configured check
  never disables repository-root, separation, task, or enclosure authority.
- Integration publishes the admitted code and memory-content commits. It proves exact source ancestry, object existence, ownership, substantive cleanliness and ref compare-and-swap. The consumer cache supplies none of those facts.
- Cache-only absence, edits or index conflicts are ignored in memory-domain content observations. Non-cache content differences and conflicts remain refusal conditions.
- The closeout door is journal-owned state (`<worktree_group>/reports/closeout-door.json`, plus the
  operation record's own publication). `WorktreeContract` no longer carries a `closeout_door` field;
  a contract that still carries the key parses, the key is never read, and the next rewrite drops it.
- Integration reports a fact — integrated, checks passed. It never completes a master task document.

## Recovery Proves Actual Git Outputs

Direct landing retains accepted input and proves the actual memory-content commit through journaled mutation evidence, current branch/HEAD, source ancestry and exact substantive content. If no memory content changed, it can reuse the existing memory head without manufacturing attribution or a cache-maintenance commit. If content changed, the one memory-content commit carries the shared `Code-Commit:` trailer.

The writer removes root `memory.md` from the memory index at the final staging/commit boundary, so force-staging the ignored cache after admission cannot include it in the output. Cache refresh is a post-output observation and cannot substitute for or invalidate Git proof. Cancellation and replacement retain their independent journal/worker/ownership checks.

## 260821-CLIVE-L1 Admission, Identity, And Recovery

Closeout integration separates four owners: the contract lifecycle lease serializes filesystem writers; closeout admission stabilizes and normalizes candidate/plan before lifecycle compatibility; candidate identity binds accepted effective input and Git provenance; mutation evidence and recovery projection own crash classification. The typed integrate caller owns integrate retention, authority, and candidate derivation, while lease-bound closeout admission is the sole closeout candidate owner. The shared controller requires the supplied candidate and explicit authority, then separates generation creation/conflict/terminal replacement from recovery/launch/projection; it cannot recapture closeout provenance or infer kind-specific authority from ambient state. For closeout, reconciliation precedes durable journal publication. Worker authority survives every non-terminal phase and may be cleared only after exact termination proof; a failed or denied termination retains the PID and blocks replacement. The store is strict schema 3.0 and relies on model/public fill-only boundaries for impossible leg-set or proven-commit rewrites while retaining transition-specific identity/state/pre-state checks. Duplicates validate against the immutable accepted plan, and generation retention requires commit-proven mutation or exact canonical contract-finalization publication. The disposable queue projection owns no retry, recover, cancel, revise, claim, or commit evidence.

## 260821-CLIVE-L2 Current Architecture

One admitted contract observation enters each public mutation flow; the mutation owner rereads that exact authority under its existing lease/lock. Journal input and proven output are immutable. Retry/recover remain same-generation, revise is safe-cancel plus write-ahead successor, and worker authority survives until termination proof. Direct landing journals memory-content mutation and publication evidence; cache refresh is informational. Terminal cleanup refuses until L5 archive proof. The legacy schema-1 repair route and the pre-locator adoption route it once listed were deleted as capabilities by the de-entanglement cut.

The route decomposition mirrors those boundaries without adding new authority: normal lifecycle state is under `lifecycle/` and direct landing under `direct_landing/`. The `legacy/` package that held the only schema-1 reader no longer exists. Parent-level integration modules coordinate Git/ref publication and organizational repair across those owners.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact integration selection and original-publication readback precede suffix execution. | `prepare_integration_certification`; `_load` | mcp/src/agents_remember/worktrees/integration/certification.py:192-216; mcp/src/agents_remember/worktrees/integration/certification.py:235-296 |
| Completed organizational proof binds original selected references through the operation owner. | `select_completed_integration` | mcp/src/agents_remember/worktrees/integration/certification.py:367-441 |
| Locator-manifest-journal authority and all publication I/O/state transitions. | `LifecycleOperationLocation`; `prepare_enclosure_publication` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py:80-114; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py:181-267 |
| Pure immutable binding, canonical serialization, digests, and bounded conflict evidence. | `EnclosureBindingIdentity`; `enclosure_binding_payload`; `sha256_payload`; `location_conflict`; `byte_conflict` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py:25-48; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py:95-115; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py:130-132; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py:142-152; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_binding.py:155-165 |
| Task-addressed controls consume the central action vocabulary, exact admitted command, current generation and legal-action evidence under the lifecycle lease. | "LifecycleControlAction = Literal["; "class LifecycleControlCommand:"; "def control_operation(" | mcp/src/agents_remember/models/lifecycles/operation_kinds.py:41-41; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:120-120; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:165-165 |
| Direct landing recovery. | `execute_direct_landing`; `execute_or_require_direct_landing_recovery` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:73-115; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:118-175 |
| Public operation projection derives legal controls and recovery surfaces from retained journal evidence. | `operation_projection`; `_projected_operation_result`; `_operation_specific_projected_result` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:145-172; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:582-592; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:661-693 |

## 260821-CLIVE Final Door-To-Journal Architecture

Closeout scheduling intent begins as an immutable door generation published in its own journal at
`<worktree_group>/reports/closeout-door.json`. Public door
commands publish exact task/contract bytes under the short repository-scoped task CAS, then refresh
the disposable projection as a downstream effect. Starting closeout atomically transfers the exact
first-ready waiting door into the stable root operation journal; claim intent is durable before
worker launch. From that point, lifecycle, source-journal identity, commits and memory content,
certification, integration, cancel, retire, supersede, and recovery evidence remain journal-owned
even if task changes invalidate the projection.

The landing and terminal lanes are also source-owned, not queue-owned. `atomic_series_landing.py`
checks current protected-ref collisions across active canonical series without persisting a blocker.
`atomic_series_terminal.py` issues only an ephemeral transaction-bound cleanup/abandon capability.
`terminal_enclosure_archive.py`, `lifecycle_enclosure_terminal.py`, and
`lifecycle_operation_location.py` require an exact bounded external archive, receipt, terminal
locator, and predecessor before the old enclosure root may be removed or a successor published.
Stable operation leases live outside the deletable root.

Recovery is deliberately narrow: an existing claimed generation resumes itself; direct-landing
outputs may be reconstructed only from exact lineage and deterministic bytes. Missing create-time
door intent, present-invalid location state, ambiguous mutation, or guessed successor state requires
developer decision. There is no raw-Git fallback, scan-based recovery, synthetic initial door,
standalone successor-intent WAL, or permanent compatibility reader. The deleted
`lifecycle_successor_control.py` responsibilities now live in task-addressed controls,
journal-door control, atomic terminal replacement, and the terminal enclosure/location transaction.

## 260824-PDLS Final Reconciliation

The accepted PDLS tree keeps lifecycle evidence in the root journal while splitting collision
classification, topology repair, legacy archive proof, queue-evidence parsing, and direct-landing
execution into their named owners. The split reduces repeated validation and fixture coupling; it
does not create a second authority route, queue-owned lifecycle evidence, or a compatibility reader.

## CCR-R18@v1 Observed-Exit Archive Guards

260831-CCR-L18 updated `terminal_enclosure_archive.py` so `_require_archivable_operation` consumes the projection-owned `project_worker_exit(record)` observation for the absent-worker/resolved-termination archive guards. File-level detail lives in that sidecar.


## Integrated IAS Recovery Contract

The closeout child now resumes retained prepared code/memory-content publication before original-head admission. The default application service bundle installs `PreparedCloseoutContinuation`; the service boundary remains explicit and selected journal/certificate identities still govern execution. Protected-source integration, root-journal ownership and Dagger certification boundaries are unchanged by the helper extractions.

## CCR-R12@v5 Current Integration Boundary

Normal integration validates the prepared code/external-memory pair, explicit handover approval,
source identity, and compare-and-swap/ref safety before protected publication. It publishes the
prepared pair through ref/tree movement and records the result without creating a merge commit or
invoking a merge hook. It does not automatically run strict code quality, memory quality, selected
certification, curator coherence, or independent review; full suites are an explicit developer
request. Earlier selected-certificate wording describes retained historical/explicit evidence.

**Reclamation is automatic and unprompted — and it is not integration's (260831-LOCR-L31).** A
successful integration publishes the landed pair through the shared landing writer, records
`integration_status="completed"` with `cleanup="pending"`, and **stops there**. It reclaims nothing,
and the integration result carries no cleanup report: its `cleanup` key is the untouched contract cell
and its summary says the worktrees are reclaimed when the task edge is finalized. Terminal
reclamation belongs to `lifecycle_finalize_task`, which runs the existing terminal cleanup procedure
and shapes the operator report — the inventory of what was removed and what was left in place across
all four target kinds (worktrees, merged local task branches, the reports directory, and the enclosure
root).

**Why it moved.** Reclaiming inside integration completed the enclosure's cleanup cell before
integration returned, so the one guard that routes a landed leaf onward to `lifecycle_finalize_task`
(`next_step.py::_gate_after`, keyed on `contract.cleanup != "completed"`) could never fire. A genuine
landing therefore reported `nextOperation: "done"` while the leaf's task document stayed `planning`
and its master row stayed `inProgress` — silently, on leaves L29 and L30. Keeping the landing and the
reclamation in one function made the edge that finalizes the task unreachable.

Because reclamation now runs after the landing, a cleanup refusal **blocks finalization** rather than
being reported beside a completed landing: the leaf document and its master row are left open over an
enclosure that is still on disk, which is exactly the honest state. A refused or partial integration
still cleans up nothing, and a dry-run finalization reports cleanup's own plan unshaped instead of a
completed-reclamation sentence.

## Source-Moved Recovery Guidance

The integration-resolution handoff's `summary` and `cancel_note` now route a moved
source through `worktree_sync` for the owning contract — settling any retained code or memory
conflict, re-running the targeted test utility after code resolutions — and then a new targeted
closeout. The refusal sentence and protected-ref/door classification are unchanged, and `replay`
remains the carryover vehicle rather than this route's prompt. See
[`integration_resolution_handoff.py`](integration_resolution_handoff.py.md).

## Master Completion Is Undecided

A leaf integrating reports a fact — integrated, checks passed. It may never imply its master is done.
`publish_organizational_master_completion`, which wrote a master task document to `Completed` by
inference from a landed leaf, was deleted by the closeout-door cut (commit `fad9808e`) and
deliberately not replaced. A door-less leaf now yields a genuine absence rather than a reconstructed
completion plan, so the integration path neither computes nor publishes a master completion.

The current truthful state is that **completing a master is a decision that is not reachable in code
today**. It is owed two checks that do not exist yet, and the intended entry point is
`application/worktree_tools.py::lifecycle_finalize_task_tool`, gated on both:

- a reviewer **report must exist** — existence only; it is never read, parsed, hashed or graded;
- an **approval must be recorded**, widened from `tasks/route_review.py`'s `developerApproval` into
  one `{approver role/altitude, tentative | final}` concept, so an orchestrator may approve
  tentatively and the developer's sprint-handover approval is final.

Neither check is built. Master completion is therefore never a side effect of a landing.

The remaining completion machinery in `organizational_completion.py` is largely unreachable after the
cut. `organizational_completion_plan`, `prepare_organizational_master_completion`,
`publish_organizational_master_completion` and `require_published_organizational_master_completion`
all have **zero callers and zero test references**. Only `classify_organizational_master_completion`
is still reached, from `integration_operation_decision.py`, to classify a retained
`publication.organizationalCompletion`. The module is the named site of the gap, not a live inference.
See [`organizational_completion.py`](organizational_completion.py.md).

## Closeout-Door Cut Removals And Relocations

The closeout-door cut (commit `fad9808e`, "Take closeout_door out of the contract and off the
integration path") removed four modules from this route and moved door storage. The door concept
itself survives; only its storage and its integration-time consumers were deleted.

- `closeout_door` left `WorktreeContract` entirely — field, parser, writer and
  `_require_publishable_closeout_door`. A contract that still carries a `closeout_door:` block parses;
  the key is never read and the next rewrite drops it. Door storage **moved** to its own journal.
- `integration_claim_transfer.py` (`transfer_and_publish_integration_claim`) — deleted, not
  relocated. `modules/integrate.py` no longer builds a claim transfer. The compare-and-swap over
  owner/generation identity it performed has no successor on the integration path.
- `integration_publication_fence.py` (`IntegrationDoorAuthorityEvidence`,
  `classify_integration_door_authority`) — deleted, not relocated. The door **reading** it wrapped
  moved to `closeout/door.py::live_closeout_door`; the integration-time authority classifier did not.
- `integration_quality.py` — deleted. It already had zero `src/` callers; the integration-time
  quality gate was gone before this cut.
- `organizational_completion_integration.py` (`preview_integration_boundary`,
  `prepare_integration_publication_intent`, `transfer_integration_claim`, `source_operation_matches`)
  — deleted, not relocated. `modules/integrate.py` no longer builds boundary facts or a publication
  intent.
- `DirectLandingResponse.doorGenerationId` was removed, and all five door reads in
  `worktrees/direct_landing.py` are gone; direct-landing admission is now the request itself plus the
  `directExecutionEnabled` policy gate.

Deliberately **not** claimed: the door plane survives because `worktree_operation_control` is a
second consumer on the public tool surface. Its deletion cannot land alone — `closeout_input_test_support.py`
is an eight-importer hub — and remains a separate, unmade cut.

## De-Entanglement Cut Removals And Relocations

The de-entanglement cut deleted the lock, door, operation and journal planes and the legacy bridge,
and relocated several route members. On this route specifically:

- The `legacy/` package was deleted as a capability (commit `a583beb8`) along with its tool surface
  and the `application/lifecycle/legacy_operation_tool.py` application boundary. There is no
  schema-1 reader and no `worktree_legacy_operation` tool any more.
- The lock plane was deleted (commit `1a0919c1`): `controlplane/task_publication_lock.py` and
  `worktrees/integration/lifecycle/lifecycle_operation_lease.py` are gone. The accepted cost is that
  two concurrent writers of the same task document may lose one write.
- The public closeout-door tool entry point was deleted (commit `6982c6a7`) and the detached
  lifecycle worker was deleted (commit `173bb01e`), moving the record advance into
  `lifecycle/lifecycle_operation_store.py` and putting closeout/integration on the in-process
  synchronous route driven by `worktree_closeout_apply` and `worktree_integrate`.
- `memory_candidate_pair.py`, `future_code_candidate.py` and `memory_census_scope.py` moved to
  `memory_quality/` so the pre-closeout quality service owns its own candidate identity
  (`0b63d6fc`, `be517eec`), and `prepared_certification.py` moved the other way (`deb032fb`).

## Terminal Task State Gates Integration-Branch Retirement

Retiring a series' integration branch now depends on the *master's own task document*, not only on an
enclosure census. `integration_branch_authority.py::_require_series_task_terminal` is that guard,
shared by the cleanup and abandon arms of `require_terminal_worktree`. It exists because
`require_series_children_retired` walks `task_root/enclosures`, and a child that was never started
has no enclosure to walk — so a master whose remaining leaves are all still `planning` reads as fully
retired there. That is how `ar/260831_lifecycle-owned-completion-relay` could have had its branch
retired while most of its leaves had never been created.

The vocabulary is deliberately asymmetric. `worktree_cleanup` still requires `Completed` exactly:
cleanup proves a completion fact. `worktree_abandon` accepts `Completed` **or** `abandoned`, and two
refusals carry the reasoning: an in-progress master cannot be retired through abandon at all, and an
`abandoned` master whose contract already records a landed line — `integration_status` in
`{"completed", "checkpointed"}` (260831-LOCR-L30) — is refused because abandoning asserts that none
of the work was taken. Once part of it landed, finally or at a checkpoint of a still-open master, the
honest terminal route is to mark the never-integrated rows abandoned and complete the master instead.
The refusal message names both states: "this master already landed work into its source branch".
`series_closeout.py::_require_atomic_master_complete` keeps its `!= "Completed"` test for the same
reason and names abandonment distinctly (`atomic-series-closeout-master-abandoned`): an abandoned
master is reclaimed with `worktree_abandon` and is never closed out. And
`organizational_completion.py::require_published_organizational_master_completion` reports
"this organizational master is abandoned, not completed" rather than the generic
not-durably-published message.

## Historical milestone context: 260831-LOCR-L30/L34 Checkpoint Landing On This Route

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

`worktrees/series_closeout.py` gained `publish_series_checkpoint_under_authority`, the non-final
master exit, and `worktrees/modules/integrate.py` gained the `checkpoint_landing_result` route that
reaches it. The route keeps every ref-protecting authority this overview describes — the series
contract binding, the atomic landing authority, the replay/ff source-state gate, the source-lineage
proof and the master-handover gate — and drops only the completion assumptions the final series route
proves (`_require_atomic_master_complete`, `_require_every_atomic_leaf_landed`, and the completed
closeout). It runs no cleanup and records `checkpointed` rather than `completed`, so the master keeps
its worktrees, branches and enclosure. A master that is already `Completed` is refused with
`atomic-series-checkpoint-master-complete`, so a checkpoint can never downgrade a finished integration.
Detail lives on the `series_closeout.py`, `integrate.py`, `landing_record.py`,
`integration_ref_transaction.py` and `integration_branch_authority.py` file cards.

**260831-LOCR-L34 repaired this route's reachability and its fail-open hole.** The L30 form read the
commits to land from the contract's closeout cells — the very completion facts an unfinished master does not
have — and required `closeout_status == "completed"`, so the route was unreachable in both directions.
It now captures its own candidate (`capture_series_checkpoint_refs`: the live code and memory
work-branch tips, with their ledger mapping proved through `exact_series_memory_closeout`, the
exact-mapping reader; the *final* series route may additionally accept the reconciled pair through
`series_memory_closeout`, 260831-LOCR-L36) and publication **requires** that `expected` value,
revalidating it against the live tips immediately before the ref move
(`atomic-series-checkpoint-candidate-moved`). The transaction on
this route carries the route difference as data, and since **260913-LCA-L11** that data is exactly one
fact: `LandingAdmission` holds the checkpoint's own captured candidate, or nothing extra for the final
routes. The L34 form also carried the finished master's ledger **shape** — the leaf-chain prefix, or
the leaf projection form for an unfinished master, selected by `_require_preserved_ledger_history` —
and **all of it is removed**: the developer's ruling of 2026-09-14T08:15+02:00 made the rebuild
outrank the tracked ledger file, so a landing no longer reads the table for what it *should* have
said, only for whether each row it carries is true. `_integrated_ledger_pair` and its source-blob
read are gone with the rule, `LandingAdmission.expected_series_ledger_prefix` and its
`atomic_series_ledger_prefix` producer are gone, and `require_integrated_ledger_mapping` keeps four
promises that were never about the file (the landed pair's mapping, per-row truth through
`_require_true_rows`, the conditional descent from the exact memory source, and the header naming its
own first row). The preview/apply parity invariant this repair came from is inventoried on
[the worktrees route overview](../overview.md) and in
[`memory_quality/overview.md`](../../memory_quality/overview.md); the removal and its cost are
recorded on the worktrees route and on the `integration_ref_transaction.py` card.

## Repo-Internal References

The following current source owns the changed behavior; no external domain source is configured for this slice.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The landing output carrier has only code and memory-content commits. | L63-L67 | [mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py](mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py) |
| Only actual memory ancestry determines this integration proof. | L235-L250 | [mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py](mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py) |
| Direct memory writes exclude the consumer cache. | L175-L236 | [mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py](mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py) |

## Update History

- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Replaced direct recovery ledger proofs and landing row validation with two-output Git authority. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the route's only change
  is inside `closeout/preparation/memory_output.py` (its git call now passes
  `GitRunnerOptions(input_text=…)`). Re-read the overview: it names neither that module nor the
  runner, and its live-door and shared-renderer statements still hold. No wording changed.
  Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  `mcp/src/agents_remember/worktrees/integration/` route changed since the recorded verification
  commit. Re-read the card against the frozen on-disk source and re-checked its claims and cited
  ranges: nothing this card asserts is falsified by the change, so no wording changed. Verification
  metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): a route file moved since
  the recorded verification commit (`closeout/preparation/memory_output.py`). Re-read the route
  card: it makes no claim about that module, and its existing statements about the shared renderer
  and the live door read still hold. No wording changed; verification metadata remains
  closeout-owned.
- 2026-09-14T11:58+02:00 — 260913-LCA-L11 route impact (curator, uncommitted change set on
  `ar/260913-lca-l11-ar`, base `4214d7a1`): corrected this route's checkpoint/landing paragraph, which
  described the L34 shape as current. The ledger-preservation check is **removed** by the developer's
  2026-09-14T08:15+02:00 ruling — it protected the tracked `memory.md`, which is derived state — so
  `LandingAdmission` now carries only the checkpoint's captured candidate,
  `_require_preserved_ledger_history` and `_integrated_ledger_pair` are gone,
  `expected_series_ledger_prefix`/`atomic_series_ledger_prefix` are gone, and the surviving promises
  are the mapping, per-row truth, the conditional source descent and the header. Added the matching
  invariant and recorded the known gap (a same-code-commit row reversal can land unreported) as
  pending a decision on the worktrees route. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.
- 2026-09-13T23:52+02:00 — 260913-LCA-L4 (uncommitted change set on `ar/260913-lca-l4-ar`, base
  `5bb124d4`): corrected the one sentence above that placed the rendering definition in
  `models/closeout/input.py`. Since L4 that method is a delegation to
  `kernel.memory_attribution.render_memory_content_message`, the one writer for all five memory-content
  producers, so this route's direct-landing leg (`_direct_memory_commit`, commit site `:270`, naming
  `operation_input.codeCommit` at `:272`) reaches the shared renderer through the closeout model rather
  than through a route-local or model-local format. Nothing else on this route changed: the trailer is
  still written at creation, before `prove_git_commit` journals the object, and the `memory.md`-only
  ledger commit still carries none. Verification metadata remains closeout-owned; no acceptance claim
  and no verification stamp advanced.
- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): the
  branch-addressed route's memory-content commit is now attributed in the object —
  `_direct_memory_commit` takes the verified `code_commit` and commits
  `effectiveInput.memory_content_message(code_commit)`, one `Code-Commit: <sha>` trailer from the same
  single `models/closeout/input.py` rendering the worktree closeout route uses, while the
  `memory.md`-only ledger commit carries none. Recorded it beside the ordered-authority paragraph
  whose ledger row recovery reads, and rebound the stale direct-landing evidence row (`73-115`;
  `118-175`). Verification metadata remains closeout-owned; no acceptance claim and no verification
  stamp advanced.
- 2026-09-13T17:56+02:00 — 260831-LOCR-L36: corrected the checkpoint-route paragraph. The route is a
  partial **publication** rather than a pause, its capture proves its ledger mapping through
  `exact_series_memory_closeout` (the exact-mapping reader), and the *final* series route may
  additionally accept the reconciled pair a `worktree_sync` produced through `series_memory_closeout`.
  The conserved integration plane is unchanged; what changed is which reader each route may claim.
  Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T14:44+02:00 — Retitled and corrected the serialization-boundary section to the per-contract activation record now that activation is keyed per series contract; the frozen integration plane itself (protected-ref compare-and-swap, ancestry proof, source-state gate, clean-checkout proof, ledger-mapping proof) is unchanged by that re-keying and no change to it is claimed. Content change; `lastVerifiedCommitHash` remains closeout-owned.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:00+00:00 — 260831-LOCR-L34: recorded the checkpoint reachability repair on this route
  — the route had required a completed closeout it also made unreachable, so it could not be entered
  from either side; it now captures its own live candidate refs and revalidates them at publication,
  the route difference travels as `LandingAdmission` data through one transaction, and a paused
  master's ledger is proved as the leaf projection form rather than against the completion census.
  Corrected the section's "two completion assumptions" to include the completed-closeout gate, and
  pointed to the preview/apply parity invariant inventory on the worktrees route overview and in
  `memory_quality/overview.md`. Content change, not a range repoint; verification metadata remains
  closeout-owned and no acceptance claim is made.
- 2026-09-12T19:50+02:00 — 260831-LOCR-L31 route impact: integration no longer reclaims. Replaced the
  "cleanup is automatic on a successful integration" boundary with the landed-and-stop account, and
  recorded **why** the ownership moved: reclaiming inline completed the enclosure's cleanup cell before
  integration returned, so the `next_step.py::_gate_after` guard keyed on `contract.cleanup !=
  "completed"` could never fire — a genuine landing reported `nextOperation: "done"` while the leaf
  document stayed `planning` and its master row stayed `inProgress`, silently on L29 and L30. Recorded
  that the result carries no cleanup report (the `cleanup` key is the untouched contract cell), that
  `lifecycle_finalize_task` owns the terminal procedure and its shape, and that a cleanup refusal now
  blocks finalization instead of being reported beside a completed landing. The retired
  `retry_cleanup` next operation is no longer this route's post-landing projection. Verification
  metadata remains closeout-owned; no route acceptance claim.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: recorded the non-final series exit and the
  checkpoint integration route on this route, and widened the abandon-refusal account from
  `integration_status == "completed"` to `{"completed", "checkpointed"}` with the value behind it.
  Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T23:05:00+00:00: Integration-branch retirement curation: recorded that retiring a series' integration branch now requires the master's own terminal task state through `_require_series_task_terminal`, why the enclosure census cannot see unstarted work, and the deliberate `Completed`-only versus `Completed`-or-`abandoned` asymmetry plus the two named refusals. Content change, not a range repoint.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: "LifecycleControlAction = Literal[", "class LifecycleControlCommand:", "def control_operation(", `_operation_specific_projected_result`, `_projected_operation_result`, `operation_projection` repointed to mcp/src/agents_remember/models/lifecycles/operation_kinds.py:41-41, mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:120-120, mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_controls.py:165-165, mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:145-172, mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:582-592, mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py:661-693. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T15:02+02:00 — Automatic post-integration cleanup at code commit `76ce662a`: recorded in the current integration boundary that a successful integration reclaims its own enclosure through the existing terminal cleanup procedure, that a refused or partial integration cleans up nothing, and that a cleanup failure does not fail the integration — the refusal is reported and the contract's `cleanup` cell holds `cleanup-pending` for a `retry_cleanup`. Verification metadata remains pinned because this is a targeted single-claim repair; source documentation only, no acceptance claim.
- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: retired the deleted `integration_quality.py` composition paragraph and its evidence row, corrected the door from contract-owned to journal-owned (`<worktree_group>/reports/closeout-door.json`), narrowed the cancellation-recovery wording to the contract-owned copy that actually went, recorded the four deleted route members and what moved versus what did not, and added the master-completion-is-undecided gap with its two owed checks. Verification metadata remains pinned because only the cut-affected claims were reconciled; this records source documentation only and makes no acceptance or certification claim.
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: removed the dead `legacy/` route member and its stale evidence row, repaired the `closeout/memory_candidate_pair.py` reference to `memory_quality/memory_candidate_pair.py`, recorded the deleted lock/door/operation/legacy planes and the four relocated members, and dropped the deleted worker/door wording from the recovery and integration-boundary sections. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-10T15:06+02:00 — No content impact: mechanical citation re-derivation of pre-existing stale anchors in this route overview against the current working tree; the cited symbols and route meaning are unchanged.
- 2026-09-10T15:06+02:00 — Source-moved recovery guidance: the integration-resolution handoff now routes through `worktree_sync` plus a new targeted closeout, while the refusal sentence, door/protected-ref classification, and `replay` support are unchanged. Verification metadata remains closeout-owned.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

- 2026-09-09T02:35:47+02:00 — CCR-L38 inherited route reconciliation: re-read this route's purpose, member inventory, route summary, and invariants against frozen candidate code tree `4c6b7bc2362bc03d50fc7a0643f34b591b805d45`; the candidate's changed paths are outside source route `mcp/src/agents_remember/worktrees/integration`, so no route/member/prose/invariant change is required. route-member-count=116; source inspection only; verification metadata remains unchanged pending producer-owned realization. No acceptance or certification claim.

- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.


- 2026-09-06T13:51:59+00:00 — L33 candidate curation: Added journal-selected original certification and suffix-execution ownership; refreshed cited existing lifecycle owner extents while retaining source-pair, publication and recovery boundaries. Reviewed uncommitted source; prior verification commit/date remain unchanged. This is source documentation, not gate or acceptance evidence.




- 2026-09-05T06:21+00:00 — Re-read the reopened affected citation claims against the frozen source, corrected their current wording/ranges, and replaced ambiguous symbols with exact declaration anchors. Verification records this source-backed claim review; it is not a code acceptance or final Gate-5 verdict.

- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: recorded the terminal-archive observed-exit guard change in `terminal_enclosure_archive.py`.


- 2026-08-31T20:30+02:00 — No route topology impact: 260831-DER restores fresh ordinary series
  integration as explicit no-door `not-applicable` authority while retaining exact leaf-door and
  journal recovery boundaries.

- 2026-08-30T06:26+02:00 — MCAR-L03 A005: documented the canonical exact-pair owner, the narrow
  configured-authority delegation, and completed-integration memory-only reopen boundary.

- 2026-08-28T14:15+02:00 — PDLS closeout: verified the direct-landing recovery, lifecycle
  translation, and exact clean-snapshot refactor against the landed candidate. The existing final
  reconciliation remains accurate; no new authority or compatibility path was introduced.

- 2026-08-26T19:27+02:00 — Reconciled the IAS closeout recovery repair: direct landing now proves
  newest-first ledger output while retaining accepted history as an immutable suffix, and cancelled
  closeout replacement uses the current waiting door plus cancellation and worker-exit proof rather
  than requiring a unique historical predecessor row.

- 2026-08-26T14:32+02:00 — Reconciled direct landing, integration proof, and organizational
  completion to valid newest-first same-code memory history.

- 2026-08-26T08:55+02:00 — Finalized the IAS source-pair serialization boundary label against
  the frozen pass-13 candidate.

- 2026-08-25T17:21+02:00 — PDLS final reconciliation recorded the accepted ownership splits and
  preserved the journal/door/queue authority boundary. Verification remains closeout-owned.

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: reconciled the final closeout, control, observation, and worker package splits; moved preserved sidecars and added the cancellation/projection owners. Verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is not Dagger certification.

- 2026-08-24T21:43+02:00 — File-size route refresh: separated pure enclosure binding and digest
  construction from the locator/manifest I/O state machine. No location authority, fallback, or
  compatibility reader moved into the new helper. Verified at source commit `23d35f77`.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: reconciled immutable doors, atomic journal claim transfer, strict terminal archive/successor authority, and removal of successor-intent WAL ownership. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: recorded the `lifecycle/`, `direct_landing/`, and `legacy/` package boundaries, repointed current evidence, and verified the governed route at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: route ownership now records typed integrate versus lease-bound closeout callers, required shared-core values, and separated generation/recovery stages against accepted tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `worktrees/integration`
  route — fourteen modules moved from `worktrees/` (flat). Verified at code commit e5cb139f.
