# Closeout Integration Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout` |

## Governing Overview

[Integration overview](../overview.md)

## What This Area Is

This area binds closeout-door publication and curator-coherence authority to exact task, code and memory candidates. It reconstructs candidate sources, retains evidence, and projects recovery and reintegration needs. Disposable scheduling evidence, candidate acceptance evidence and durable operation-journal evidence have separate owners.

## Hot Path Summary

Door dependency identity binds the task, code and memory candidates and their review, memory, admission and scheduling provenance. Coherence validates the exact candidate pair, task intent, quality attestation and declared evidence dependencies. Recovery projects durable outputs from operation-record mutation evidence; queue state does not supply commit proof.

## Construction And Ownership

`curator_coherence.py` observes the exact code/memory/task/attestation candidate and validates current authority. `curator_coherence_publication.py` publishes content-addressed record/report generations and replaces the canonical authority pointer. Prepare separately files the candidate set and its reading projection under the enclosure reports directory, returning counts, a candidate-list digest and their locations. Validated status/publication answers return counts and record/report locations rather than enumerating the recorded collections. `curator_coherence_judgments.py` requires exactly one agent-owned judgment per source candidate and binds its evidence bytes. `curator_coherence_render.py` generates the human projection; structured records remain the authority.

`curator_coherence_paths.py` owns the task-root namespace, and `curator_coherence_records.py` reads exact immutable generations and verifies their record, report, attestation and retained evidence. Historical generation integrity is distinct from live readiness: the live validator additionally checks current candidate identity, dependencies and original judgment evidence. Publication reads the newly written generation before replacing the canonical pointer.

`door_source.py` resolves the candidate task and constructs a generation from current candidate evidence, topology, semantic task intent and provenance. For graph-backed candidates, door reconstruction and coherence observation pass the already resolved authored graph to the shared graph context and use its bound sprint snapshot. `door.py` connects a claimed door to its exact operation identity; `initial_door_recovery.py` classifies a canonical closeout record missing its create-time door intent. `recovery_projection.py` derives recovery commits from authoritative mutation evidence and refuses contradictions. `integration_reopen.py` reports whether prospective or completed closeout outputs require reintegration, including source-branch ancestry checks for completed outputs.

`task_intent_identity.py` resolves contract-owned task intent and compares it with the live door. `task_intent_legacy_census.py` separately counts current legacy containers; immutable historical generations are excluded from that census. Coherence requires a digest-bearing intent and exact declared direct dependencies rather than topology alone.

The prepared-memory certification application adapter was removed with its affected-execution and continuation composition. The surviving memory-quality controller measures admitted candidates and publishes readiness; the cutover owner supplies unconverted refusal/conversion guidance. Ordinary closeout separately gates the exact converted candidate and output before publication. These owners do not claim to mint the removed prepared-memory certification result. The standing dependency intent remains that pre-closeout preparation must have its own candidate authority; retirement of the old adapter is not proof of a replacement producer.

[Certification](certification/overview.md) and [preparation](preparation/overview.md) retain selected immutable-object and private-output machinery; their presence is not current default prepared-closeout execution. `preparation_selection.py` reopens exact selected intents/outputs, checks their owning operation and logical refs, and requires original command history where a write-enabled selected output is present. The default service factory binds neither a prepared-memory producer nor a continuation. Explicit core finalization still checks exact five-certificate/current-memory authority; private output selection supplies neither that certificate nor approval.

## Publication And Assessment Evidence

The prepare response obtains its publication-input statement from the request model's declaration. It names one agent-owned judgment per candidate and all nine required publication members. `semantic_requirement_revision` and `delivery_attempt` are caller-supplied identities that prepare does not derive. The statement reads the declaration at call time, so an added member appears without a second edit to the summary. Assessments are optional publication content beside judgments and do not replace the judgment coverage obligation. Publish may receive both collections through an absolute `judgments_file` path instead of inline lists. `curator_judgments_file.py` reads one regular-file descriptor within its byte budget, parses the payload and validates each collection with the inline entry models and count bounds. Explicitly supplying either inline list alongside the file, even an empty list, refuses publication; a file-based answer carries the SHA-256 of the bytes read. This optional transport adds no tenth required publication member.

Assessment publication stamps authorship from the admitted caller and rebuilds examined inputs from the same observation as the coherence record. `curator_assessment_evidence.py` publishes cited bytes under `<task_root>/notes/reports/evidence/<assessment_id>/<filename>` and reads each recorded destination back, checking its retained identity. Historical reads use publisher-recorded assessment destinations and retained judgment custody. A failed write or read-back blocks publication with the destination and observed failure; it is not reported as survival or redirected to another store.

Both collection and subject assessment projections use the shared binding classifier through one `_measured_state` path. Missing or empty measurements produce `not-measured`, not evidence of movement. Supplied measurements classify each record against its own declared inputs: disagreement is `stale`, missing coverage is `not-measured`, and complete agreeing coverage is `current`. A subject without an assessment is `none-recorded`; lack of measurement grants no clearance.

Coherence authority is validated before closeout. Once closeout completed, retained authority status/validate answer closed-out with recorded pair and digest, without comparing the live post-closeout tree. That historical response is neither fresh readiness nor integration acceptance; a missing authority stays absent.

## Invariants And Boundaries

- Door publication and claims bind entry identity; durable operation evidence owns running, recovery and terminal facts. A claimed door's operation identity is immutable.
- Recovery remains candidate-bound. Conflicting reported commits and commit-proven mutation evidence refuse rather than silently selecting an output.
- One canonical structured authority selects one immutable coherence generation per leaf. Generated Markdown is checked against that record; historical prose is not an authority-selection mechanism.
- Current coherence binds the exact candidate pair, task document, code and memory trees, semantic intent, attestation and source-candidate set. Missing or stale intent and mismatching dependencies refuse current use and direct republication.
- Current converted onboarding traces require the applicable source-bound card and governing-route judgments over the same candidate. The former sidecar/governing-route refresh composer is removed; curator preparation must satisfy the surviving converted trace gate rather than treating either surface alone as sufficient.
- Malformed canonical authority remains subject to exact prepared predecessor identity. Immutable generation collisions and incomplete generations refuse; durable integrity does not substitute for current readiness.
- Graph-backed consumers use the bound graph-context sprint for their observation rather than mixing its topology with an independently resolved sprint.
- External-memory closeout obtains its accepted pair from current coherence and re-proves apply/recovery pair identity against the exact contract, rather than substituting repository identity.

After its identity and evidence checks, the live coherence validator calls the knowledge gate over the observed code and memory candidate trees. A refusal becomes `curator-coherence-knowledge-gate-refused`, with `memory_quality_check` as the next action. Converted memory without a bound gate refuses. The gate passes the parent memory tip to its registered leaf validator. Ordinary legacy-format candidate/official input is independently refused with central conversion guidance by `curator_coherence._require_knowledge_gate`; unreadable Git/object probes remain named gate errors, never inferred unconverted state. Converted candidates keep the exact existing worklist and validator judgment. The removed prepared closeout path is no alternate converted-memory refusal route; ordinary closeout judges and closes the exact converted memory output through its current owners.

The surviving controller and closeout independently use their converted knowledge/trace and exact-output validation owners. The former legacy sidecar/body-history refresh consumers and prepared closeout component calls were removed. Their standing intent of truthful source-bound onboarding is not transferred to a nonexistent legacy helper or to a claimed shared-helper parity; current candidate equality and trace/gate obligations remain separately stated.

The standing recovery contract is to recover retained prepared finalization before fresh original-head admission, allowing the original generation to finish owned publication without rerunning commands or certifying a changed candidate. Preparation certificate and command-retention predicates were confirmed; finalization admission order remains a named uncertainty in this review.

## Lifecycle Context And Uncertainties

The original lifecycle annotation is retained outside operative promises:

**Inert until the cutover.**

No lifecycle authority establishing that annotation's current status was available in the assigned card or sidecar. The source contains active gate and unconditional legacy-format refusal predicates; the annotation is historical and must not be read as disabling them.

Historical relocation/deletion commit attribution, the retired ledger writer's repository-wide absence, cleanup/archive exclusion of assessment evidence, queue invalidation behavior, and the selected certification route's reported Gate-5 observations were not established by the bounded current-source witnesses. These remain contextual claims for parent adjudication rather than current guarantees. The original card names `test_the_closeout_validator_refuses_until_the_gate_passes_and_never_runs_ungated`; this review establishes no execution or result for that test.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `door_source.py` | [door_source.py.md](door_source.py.md) | covered |
| `curator_coherence.py` | [curator_coherence.py.md](curator_coherence.py.md) | covered |
| `curator_coherence_judgments.py` | [curator_coherence_judgments.py.md](curator_coherence_judgments.py.md) | covered |
| `curator_coherence_publication.py` | [curator_coherence_publication.py.md](curator_coherence_publication.py.md) | covered |
| `curator_coherence_render.py` | [curator_coherence_render.py.md](curator_coherence_render.py.md) | covered |
| `integration_reopen.py` | [integration_reopen.py.md](integration_reopen.py.md) | covered |

## Series leaf grant predicate

A series door targeting a canonical leaf reads its current grant, replacing global settings policy. Ordinary enclosed leaf/door behavior remains unchanged; the source predicate does not execute independent review or borrow queue authority.

## Clean-sync review provenance

The closeout door first allows the recorded candidate tree itself. For a different tree, it calls clean_sync_keeps_route_review: the plane-stamped baseCommit must be an ancestor of the current base; the reviewed and incoming changed-path sets must be disjoint; and the current-base-to-candidate after-image map must equal the recorded-base-to-reviewed map exactly. Map identity includes each raw pathname byte sequence, blob and mode. An absent stamp supplies no exception. The door preserves the existing review record digest as its fingerprint and still checks task intent, evidence bytes and dependencies. This exception belongs to the door; `require_current_route_review` only validates the stored review's intent, evidence and dependencies and returns its recorded tree — the door is what compares that recorded tree with the candidate.

## Evidence

- The door accepts either its exact recorded tree or the bounded clean-sync relation. [11]




- The closeout validator's gate over the authority's exact candidate. [1]

- Door source facts use current Git and task authority. [2]
- Coherence observes exact candidates, validates current identities and dependencies, and shares per-record measurement projection. [3]

- Publication derives the input statement, files prepared candidates, binds assessment authorship and verifies generations before pointer replacement; optional file transport preserves the required identities. [4]

- Assessment evidence has a task-root destination and mandatory retained-byte read-back; immutable generation reads verify structured and projected content. [5]

- Preparation selection requires original certificates and retains command starts, outcomes and selected outputs. [6]




- Converted leaf closeout evaluates its exact candidate through the mandatory invariant gate and refuses an unbound gate; unconverted memory uses the central cutover refusal. No removed prepared-certification adapter is an alternate route. [8]

- Exact accepted and recovered pair identities and source-branch reintegration predicates have shared owners. [9]
- Both coherence assessment projections delegate supplied per-record measurements to the binding owner. [10]

- The curator checklist supplies scope, its worklist-backed `_OnboardingGateInputs` and response to the onboarding refresh gate; that gate dispatches converted history-file traces. It accepts no separate no-impact identities. [7]
