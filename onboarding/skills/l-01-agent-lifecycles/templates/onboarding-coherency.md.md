# skills/l-01-agent-lifecycles/templates/onboarding-coherency.md

## Governing Overview

[overview](../overview.md)

## Purpose

The canonical onboarding-coherency template is the report the Reviewer uses to compare affected onboarding with code, using the Curator's supplied handoff and curation-check result; the Curator, Orchestrator and developer can inspect its findings and readiness. It records affected sidecar, overview, index and entity changes together with the complete curation-check result supplied by the curation operation; drift suites remain separate developer-requested operations. The packaged runtime file is a distribution twin, not another authoring authority.

## Code Commentary

### Logic

The report inventories changed source sidecars, new files missing onboarding, the complete check set, governing overview changes and handoff readiness. Its fields describe recipient, analysis role or helper label identifying the assigned routes, reviewed change scope and written time; the author label is not a runtime occupant-ID field. The owning curation operation reconciles existing intent, ruled change and implemented reality rather than substituting a list of diagnostics for that comparison.

For each changed source file and its nearest governing overview the report records the current trace row (`updated` or `no_impact`, read from `reference/curator/card-formats-and-citations.md#keep-current-card-content`), its reason and unresolved findings; new files report onboarding under the resolved storage policy. Route/repository overviews reflect the change set, including moved, added and deleted slices. Record the actual affected-path checks and their statuses rather than inventing metadata or future commit-derived fingerprints.

### Checks And Handoff

The shape records full `memory_quality_check`, conditional `curator_coherence`, affected-onboarding checks, `git diff --check`, other named checks and requested drift suites. Each carries its scope/command/result and pass, failed, blocked or not-run status as applicable. It also records whether the ledger maps code HEAD, whether governing overviews reflect touched routes/slices, readiness for closeout and whether failed/not-run checks were reported without a full-green claim. These are report fields, not evidence that the checks ran, a ledger is current or closeout is ready.

The complete curation operation is not optional or replaceable by a subset. Its owning operation requires intake and repair-loop full checks, repair or exact-code blocked escalation of every curator-actionable finding, raw quality readiness, and coherence publication/validation when required. This is completed curation evidence and its existing prerequisite, not authority granted by the report to run closeout or integrate. Full code quality, full test suites, certification, review and drift authorization remain distinct from merely filling curation status fields.

### Invariants And Boundaries

The report carries evidence; it neither stamps metadata nor performs closeout. Do not invent future code hashes or advance fingerprints to uncommitted source. Curation reconciles and writes admitted memory, while the transaction owner retains acceptance and publication. Template recipient fields do not dispatch a role or override its assignment.

The current Reviewer source names impact-analysis and onboarding-coherency as durable route reports. Its baseline curation exception states that the Curator always runs complete memory quality; it does not make a reviewer-authored subset equivalent or assign that authoring operation to the Reviewer.

Router doctrine permits harness helpers within the assignment, gives them no AR seat or independent-review authority and retains exactly one Curator writer. An explicitly requested independent review remains separate from the author's helpers.

### Documentation Scope

The template holds no TODO and needs no sibling-repository evidence for this report shape. The report's formatting and check placeholders do not certify whole-repository coherence, provider availability, executed verification or acceptance.

## Evidence

- The Reviewer compares affected onboarding with code using the Curator's handoff and the complete curation-check result from the curation operation. [1]

- Changed files report their current trace row and reason, new files their onboarding, and governing overviews reflect the change; the report decides nothing. [2]

- The report shape contains analytical author and affected scope, changed-sidecar and new-file inventories. [3]

- Check statuses, conditional coherence, drift and ledger fields describe what must be reported, not successful execution. [4]

- Overview and handoff fields require explicit gaps and forbid full-green overclaiming. [5]

- Curator reconciliation and memory authoring do not own Git publication or landing. [8]

- Future hashes/uncommitted fingerprints are forbidden; handoff evidence and required coherence retain their own boundary. [9]

- Helpers are not AR seats or independent review; Curator authoring retains one writer. [12]

- Reviewer doctrine assigns the normal authoring full-MQC exception to the Curator, not a reviewer subset. [10]

- Reviewer outputs include both durable route-report templates. [11]

- Curation reconciles current intent, ruled intent and implemented reality and verifies every card sentence against code; each invariant is ingested within its Curator-authored semantic scope, while grouping and entity edits require their own justification. [6]

- The curation owner runs changed sidecar/overview/entity checks, memory-worktree diff check and full memory quality; every actionable finding is repaired or escalated with its returned code, conditional coherence is completed before closeout, and independent fact-checking checks every changed statement and history row. [7]
