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

The closeout-facing prepared-memory certification adapter is currently `application/prepared_certification.py`, outside this directory. Its execution composes affected-closure work and full memory-quality checks against the prepared code view. Its imports obtain future-code and memory-pair services from `worktrees/modules/`; the former account of these services solely under `memory_quality/` is not a current location map. The standing dependency intent remains that pre-closeout memory-quality services can mint and prove their candidate identity without depending on the closeout plane; the import observations here do not establish that this intent is satisfied throughout the repository.

[Certification](certification/overview.md) and [preparation](preparation/overview.md) describe the selected certification and private-output routes. [preparation_selection.py](preparation_selection.py.md) retains selected original objects and command outcomes through the lifecycle store. Selection requires the four original code certificates and, for memory legs, the selected fifth certificate. A command start is recorded before launch, an actual outcome remains recordable after cancellation, and selecting a prepared output grants no task-ref publication. `application/worktree_services.py` registers the prepared-memory certification adapter; private output selection alone supplies neither final memory certification nor approval.

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
- Exact no-content-impact and no-route-impact judgments project into separate onboarding gates. The shared refresh validator composes sidecar and governing-route checks; curator preparation must not treat only one surface as sufficient.
- Malformed canonical authority remains subject to exact prepared predecessor identity. Immutable generation collisions and incomplete generations refuse; durable integrity does not substitute for current readiness.
- Graph-backed consumers use the bound graph-context sprint for their observation rather than mixing its topology with an independently resolved sprint.
- External-memory closeout obtains its accepted pair from current coherence and re-proves apply/recovery pair identity against the exact contract, rather than substituting repository identity.

After its identity and evidence checks, the live coherence validator calls the knowledge gate over the observed code and memory candidate trees. A refusal becomes `curator-coherence-knowledge-gate-refused`, with `memory_quality_check` as the next action. Converted memory without a bound gate refuses. The gate passes the parent memory tip to its registered leaf validator. Unconverted memory is not simply guaranteed the former behavior: the current route consults the cutover lock when the converted gate does not apply. The prepared closeout path explicitly refuses converted memory because it cannot close the leaf history while preserving the exact curator-attested candidate; it separately checks the cutover lock for unconverted memory.

The standing refresh-parity intent is that curator preparation and closeout independently apply the same sidecar and governing-route body/history checks. The shared validator composes both legacy surfaces, and the curator's legacy branch calls it with separate no-impact identities. The prepared closeout legacy branch calls the two component validators separately; both callers instead select onboarding history traces when their trace context is available. These source branches support the applicable-surface intent without establishing unconditional shared-helper parity or successful validation.

The standing recovery contract is to recover retained prepared finalization before fresh original-head admission, allowing the original generation to finish owned publication without rerunning commands or certifying a changed candidate. Preparation certificate and command-retention predicates were confirmed; finalization admission order remains a named uncertainty in this review.

## Lifecycle Context And Uncertainties

The original lifecycle annotation is retained outside operative promises:

**Inert until the cutover.**

No lifecycle authority establishing that annotation's current status was available in the assigned card or sidecar. The source contains active gate and cutover-lock predicates; the annotation must not be read as disabling them.

Historical relocation/deletion commit attribution, the retired ledger writer's repository-wide absence, cleanup/archive exclusion of assessment evidence, queue invalidation behavior, and the selected certification route's reported Gate-5 observations were not established by the bounded current-source witnesses. These remain contextual claims for parent adjudication rather than current guarantees. The original card names `test_the_closeout_validator_refuses_until_the_gate_passes_and_never_runs_ungated`; this review establishes no execution or result for that test.

## File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `door_source.py` | [door_source.py.md](door_source.py.md) | covered |
| `prepared_certification.py` | [prepared_certification.py.md](prepared_certification.py.md) | covered |
| `curator_coherence.py` | [curator_coherence.py.md](curator_coherence.py.md) | covered |
| `curator_coherence_judgments.py` | [curator_coherence_judgments.py.md](curator_coherence_judgments.py.md) | covered |
| `curator_coherence_publication.py` | [curator_coherence_publication.py.md](curator_coherence_publication.py.md) | covered |
| `curator_coherence_render.py` | [curator_coherence_render.py.md](curator_coherence_render.py.md) | covered |
| `integration_reopen.py` | [integration_reopen.py.md](integration_reopen.py.md) | covered |

## Series leaf grant predicate

A series door targeting a canonical leaf reads its current grant, replacing global settings policy. Ordinary enclosed leaf/door behavior remains unchanged; the source predicate does not execute independent review or borrow queue authority.

## Evidence


- The closeout validator's gate over the authority's exact candidate. [1]
- Door source facts use current Git and task authority. [2]
- Coherence observes exact candidates, validates current identities and dependencies, and shares per-record measurement projection. [3]
- Publication derives the input statement, files prepared candidates, binds assessment authorship and verifies generations before pointer replacement; optional file transport preserves the required identities. [4]
- Assessment evidence has a task-root destination and mandatory retained-byte read-back; immutable generation reads verify structured and projected content. [5]
- Preparation selection requires original certificates and retains command starts, outcomes and selected outputs. [6]
- Shared legacy refresh validation composes both surfaces; the curator caller supplies separate no-impact identities and selects traces when available. [7]
- Current knowledge-gate routing includes converted-memory refusal and an unconverted-memory cutover lock. [8]
- Exact accepted and recovered pair identities and source-branch reintegration predicates have shared owners. [9]
- Both coherence assessment projections delegate supplied per-record measurements to the binding owner. [10]
