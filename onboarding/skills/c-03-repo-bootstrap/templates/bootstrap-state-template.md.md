# skills/c-03-repo-bootstrap/templates/bootstrap-state-template.md

## Governing Overview

[Repository overview](../../../overview.md)

## Purpose

This template defines the persistent bootstrap state file that allows `c-03-repo-bootstrap` skill runs to pause and resume across sessions, including existing-memory slice maintenance and the closeout boundary.

This authored `skills/` template defines an artifact format; the packaged runtime source is a byte-identical distribution twin in this bounded inspection, not an independent contract owner. The document below describes placeholders and expected information, not the state of a bootstrap run.

## Code Commentary

### Logic

The template tracks run metadata, onboarding root, source inventory gate status, phase status, areas, governing routes, slice maintenance, waves, decisions, parking lot items, blockers, deferred files, closeout boundary status, and the next recommended action.

The header uses `sourceInventoryStatus` (pending / presented / accepted / corrected / blocked), distinct from the ledger gate field. Phase rows run from Phase 0 setup/source intake through scout, area deep-dives, root overview, coverage plan, governing route map, route-overview waves, docs/boundary evidence, file-onboarding waves, curator reviews and Phase 5 handoff. Area rows track scouting, deep-diving, brief, root overview, coverage and route map. Governing-route rows include planned, created, refreshed, moved, cleanup-planned, removed, retired, deferred and blocked with confidence. Slice-maintenance rows distinguish source change, existing memory, action and status. Waves separate curator result from human review; decisions record date, context and source; the parking lot explicitly uses LOW confidence. Blockers name owner and unblocking action, deferred files name a revisit trigger, and closeout rows distinguish handoff presentation from a closeout request.

### Conventions

Preserved workflow guidance, checked by the parent against the canonical bootstrap skill; it describes the procedure, not completed execution:

> `bootstrap/STATE.md` is read first and updated last in each bootstrap session. It is state and coordination memory for the bootstrap, not file-level onboarding, and it records whether closeout has merely been requested after handoff.

### Invariants And Boundaries

Preserved advisory boundary from the incoming card:

> The state file must preserve decisions, blockers, and low-confidence parking-lot items rather than promoting them into durable facts.

All phase statuses, `done` area values and `complete` wave rows are exemplar vocabulary in a template, not observed task progress or review outcomes. The `Closeout Boundary` explicitly says closeout is separate from automated bootstrap and records only whether closeout was requested. No placeholder or filled state row itself grants closeout or publication authority.

The source header still literally offers `topology | external / mixed` at line 13. This is inherited template vocabulary, not evidence that mixed topology is currently supported; the governing overview states that only external topology is supported. The inherited choice is disclosed rather than silently rewritten.

### Historical And Verification Limits

The incoming card carried this unfinished verification instruction:

> Fill verification metadata after the source file is committed.

It is retained as a historical Todo, not an assertion that verification metadata is missing now, an authority grant, or a request to hand-write mechanical sidecar fields. This comparison supplies no executed bootstrap, source approval, test result, completed wave, closeout, publication or acceptance.

The old card also attributed a workflow requirement to the packaged `c-03-repo-bootstrap` skill: 

> `c-03-repo-bootstrap` skill requires every bootstrap to maintain `bootstrap/STATE.md` from this template.

The attribution is preserved and checked against the current canonical bootstrap skill. The separate skill citation below supports the procedural requirement; the template alone proves only its artifact format.

### Docs References

The incoming card recorded the following repository-local documentation assessment:

> No external documentation is needed for this repository-local template.

> No relevant external documentation found.

These are inherited assessments, not a fresh external documentation search. The present evidence is the inspected local template.

### Cross-Repo References

The incoming card recorded:

> No sibling repository evidence is needed for this template.

> No meaningful cross-repo references found.

These are preserved scope assessments, not a fresh sibling-repository inspection. Any cross-repo fields in the template describe recorded context, not permission to write another repository.

## Evidence

### Repo-Internal References

The citation rows below preserve the incoming template-evidence meanings while retargeting them to the canonical authored source and narrowing ranges to the information described. They prove the shape of a template, not execution or acceptance of its values. Inherited cross-file skill claims remain qualified above.

- The state template records bootstrap mode, memory root, onboarding root, branch, topology, source inventory status, and phase status across the full `c-03-repo-bootstrap` skill lifecycle. [1]
- The state template tracks areas, governing routes, slice maintenance, waves, decisions, parking lot items, blockers, deferred files, closeout boundary status, and next action. [2]
- Wave examples, curator result and human review fields are distinct from decisions, LOW-confidence questions and blockers. [3]
- Deferred-file triggers, separate closeout request and one recommended next step complete the state format. [4]
- Every bootstrap maintains bootstrap/STATE.md, reads it first and updates it last, using this template. [5]
