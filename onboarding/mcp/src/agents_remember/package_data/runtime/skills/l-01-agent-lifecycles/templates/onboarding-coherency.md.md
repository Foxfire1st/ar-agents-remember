# l-01-agent-lifecycles/templates/onboarding-coherency.md

## Purpose

Packaged runtime copy of the onboarding-versus-code coherence report template. The canonical
template owns the review shape; the skill sync process publishes this exact artifact.

## Code Commentary

### Logic

The report compares current code, existing onboarding/entity intent, and ruled task/design intent.
It inventories changed sidecars, missing onboarding, route overviews/indexes, and drift, and records
only the affected scoped diagnostics requested for the handoff. The author field names the analysis
role or bounded fan-out label, not a runtime sub-agent id.

### Conventions

Changed source sidecars and their nearest governing routes need a substantive current-body update
plus newest-first history, or a specific sanctioned no-impact attestation after review. Missing
onboarding and curator-actionable findings are reported with their exact status before handoff;
routine closeout and integration do not require a full memory-quality certificate.

### Invariants And Boundaries

- Verification hashes and entity fingerprints remain real-commit-derived.
- The report is evidence; it neither stamps metadata nor performs closeout.
- This packaged artifact must remain byte-identical to the canonical template.

### Todos

None recorded.


## CCR-R12@v5 Handoff Boundary

This template records the exact checks and their failed or not-run status as handoff evidence, together with the curator's complete memory-quality result. Closeout and integration consume the prepared code, memory-content, and ledger transaction and carry that completed curation as a prerequisite; full code quality, full tests, certification, and review are explicit requests rather than automatic template gates.

## Evidence

### Repo-Internal References

This bundle copy is written by fan-out sub-agents and consumed by the reviewer's onboarding-vs-code lens and the orchestrator's memory-quality checks.

- Sync-propagated bundle copy of the canonical templates source. [1]
- The adversarial reviewer's onboarding-vs-code lens cites this report as backing evidence, and the reviewer's Outputs section names it among the durable route reports. [2]
- The orchestrator's checks consume this report, written by its own loop or a dispatched role seat while AR mutations stay in the orchestrator main loop; the former no-native-sub-agents rule was retired by MIK-R99/D92 and is kept here only as historical context; the current shared operation block states the seat's own organisation at any size. [3]
- The reviewer's onboarding-vs-code lens pairs `read_ar_files` with `grepai_search`, and the curation exception makes the complete memory-quality operation the reviewer's one non-optional check. [4]

### Cross-Repo References

No sibling repository evidence is needed for this report template.

No meaningful cross-repo references found.
