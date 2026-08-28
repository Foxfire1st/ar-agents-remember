# mcp/tests/test_requirement_compilation_gate_doctrine.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_requirement_compilation_gate_doctrine.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This pure architecture-fitness test structurally pins M39@v1: requirement compilation and cold-read
approval precede task topology, and downstream handoffs remain bound to the same ID/version.

## Logic

The suite reads canonical lifecycle and task-workflow Markdown, normalizes whitespace, and checks
for the compiler gate, every mandatory packet section, cold-read questions, filtered projections,
one-primary-requirement leaf rule, version invalidation/rebriefing, and exact-revision evidence
fields in worker/reviewer templates. It additionally pins immutable version-addressed filenames,
new-file creation for later revisions, and packet-local durable corpus approval inspected by every
downstream seat. Curator briefing is included: it must receive exact approved packets plus the
reviewer's per-revision adjudication and must refuse rejected/worker-blocked delivery as current
intent.

## Invariants And Boundaries

- It verifies required doctrine structure, not semantic implementation conformance by itself.
- Generated projection equality remains owned by `scripts/sync-skills.py --check`.
- A missing or weakened gate term fails loudly; there is no compatibility reader for old templates.

## Update History

- 2026-08-28T11:32+02:00 — Refreshed structural phrases for the one-primary leaf contract; the
  card already described that semantic boundary and required no other body change.

- 2026-08-27T16:27+02:00 — Added structural curator-brief/role proof for exact approved packets,
  independent adjudication, and rejected/blocked fail-closed behavior. Pure run: 8 passed.

- 2026-08-27T14:04+02:00 — Extended M39 proof to immutable version-addressed packet files and
  mandatory approved-state plus durable-ruling checks in manager/worker/reviewer handoffs.
- 2026-08-27T13:32+02:00 — Added focused structural proof for M39@v1. Verification remains
  closeout-owned.
