# `w-02-light-task-workflow` requirement-packet-template.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/requirement-packet-template.md` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |

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

## Update History

- 2026-08-28T11:32+02:00 — No content impact: synchronized projection payload changed with the
  canonical one-primary requirement doctrine; projection ownership and byte-identity rules remain
  unchanged.

- 2026-08-27T14:04+02:00 — Clarified immutable version-addressed storage, packet-local durable
  corpus approval, and new-file semantic revisions.
- 2026-08-27T13:32+02:00 — M39@v1 initial packet template. Verification remains closeout-owned.
