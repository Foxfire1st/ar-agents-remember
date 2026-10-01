# `w-02-light-task-workflow` requirement-packet-template.md

## Purpose

This installed template is the canonical shape for one independently falsifiable requirement
revision before task decomposition.

## Logic

The packet records stable identity/version, normative behavior, problem/rationale, scope and
exclusions, preservation and failure/recovery boundaries, examples and forbidden overreach,
material diagrams, deliverable/verification evidence classes, authority/provenance, dependencies,
truth gaps, a transcript-free cold-read record, and revision/invalidation history.

## Invariants And Boundaries

- The packet is canonical and immutable after approval; task documents link its
  `<stable-id>-<version>-<slug>.md` address and never rewrite its contract.
- Approval binds one exact ID + version.
- Every approved packet records the durable corpus ruling. Semantic change increments version,
  creates a new version-addressed file, and invalidates only affected acceptance.
- Expected evidence is specified before implementation but does not pre-approve later artifacts.
- This runtime copy is generated from root `skills/` by `scripts/sync-skills.py`.
