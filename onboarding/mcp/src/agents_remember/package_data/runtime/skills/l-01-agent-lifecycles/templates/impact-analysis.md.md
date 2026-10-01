# l-01-agent-lifecycles/templates/impact-analysis.md

## Purpose

Packaged runtime copy of the bounded impact-analysis report template. The canonical template owns
the report contract; the sync process publishes this exact artifact.

## Code Commentary

### Logic

The report records scope, evidence, affected surfaces, risks, and conclusions for an orchestrator or
reviewer. Its author is an analysis role or bounded fan-out label, not a runtime sub-agent id.

### Conventions

Keep findings evidence-backed and label the analytical responsibility rather than transport
identity. Edit the canonical template and synchronize.

### Invariants And Boundaries

- The report carries analysis, not mutation authority.
- Runtime occupant identifiers are not durable authorship identity.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.

## Evidence

### Repo-Internal References

This bundle copy is written by fan-out sub-agents and consumed by the orchestrator's integrity bulwark and the reviewer's completion lens.

- Sync-propagated bundle copy of the canonical templates source. [1]
- The orchestrator's portfolio integrity bulwark consumes this report, written by its own loop or a dispatched seat while AR mutations stay in the orchestrator main loop. [2]
- The frame's artifact-obligation doctrine keeps AR mutations in the main loop while sub-agents write templated reports. [3]

### Cross-Repo References

No sibling repository evidence is needed for this report template.

No meaningful cross-repo references found.
