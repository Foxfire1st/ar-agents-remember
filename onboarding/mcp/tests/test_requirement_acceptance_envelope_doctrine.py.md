# mcp/tests/test_requirement_acceptance_envelope_doctrine.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_requirement_acceptance_envelope_doctrine.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:42:13+00:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Focused architecture-fitness proof that the canonical worker, reviewer, manager, and light-task
sources structurally require the M38 per-requirement acceptance envelope. It prevents a later prose
cleanup or template refactor from silently returning to aggregate “requirements addressed” claims.

## Code Commentary

### Logic

`_text` normalizes Markdown whitespace and `_assert_terms` reports the exact canonical file and
missing contractual phrases. Five tests partition the contract: one complete leaf-primary
worker/brief/report envelope and Checks shape; independent reviewer/verdict adjudication; manager
preservation of primary ownership plus adjacent context; packet supersession and master-versus-leaf
gate boundaries; and explicit separation of the durable-evidence hold point.

The M39 extension also makes each acceptance block prove that the worker and reviewer inspected
the same approved, version-addressed packet and its durable corpus ruling; an unapproved packet is
structurally non-passable even when the remaining evidence fields are populated.

The suite reads canonical `skills/` sources rather than installed copies. Byte-identity of installed
and harness projections remains the separate sync-script contract, so this test proves doctrine
shape without creating a second projection validator.

### Conventions

- Keep assertions on stable structural phrases and headings, not complete prose snapshots.
- Add a term only when omission would materially weaken the acceptance contract.
- Register this module explicitly in the evidence-lane manifest.

### Invariants And Boundaries

- Every worker field demanded by M38 is represented for the leaf-owned primary revision.
- Every verdict variant must contain the per-ID adjudication section.
- Dependency and preservation requirements remain checked context and cannot be claimed closed by
  the leaf-primary envelope.
- Manager dispatch must keep the independent reviewer distinct from both builder and plan author.
- The test does not claim behavioral review independence; it proves the templates make the required
  evidence and disposition fields unavoidable.
- Durable-evidence promotion remains a separately asserted concern.

## Docs References

No external documentation governs this repository-owned lifecycle contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Worker role, brief, and report require one complete primary envelope plus explicit Checks. | `test_worker_role_brief_and_report_require_one_complete_primary_block` | mcp/tests/test_requirement_acceptance_envelope_doctrine.py:22-56 |
| Reviewer role and verdict require independent per-ID accepted/rejected adjudication. | `test_reviewer_role_and_verdict_require_independent_adjudication_per_id` | mcp/tests/test_requirement_acceptance_envelope_doctrine.py:57-77 |
| Manager and task sources preserve primary ownership while keeping adjacent requirements contextual. | `test_manager_and_task_workflow_preserve_primary_ownership_and_adjacent_context` | mcp/tests/test_requirement_acceptance_envelope_doctrine.py:82-112 |
| Packet supersession and leaf/master gate boundaries remain explicit. | `test_packet_supersession_and_leaf_gate_boundaries_are_explicit` | mcp/tests/test_requirement_acceptance_envelope_doctrine.py:115-126 |
| Durable-evidence promotion is structurally separate. | `test_durable_evidence_hold_point_is_explicitly_separate` | mcp/tests/test_requirement_acceptance_envelope_doctrine.py:132-146 |
| The manifest classifies this proof explicitly as architecture fitness. | "mcp/tests/test_requirement_acceptance_envelope_doctrine.py" | mcp/tests/test-evidence-lanes.toml:542-542 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| The test reads only this repository's canonical doctrine. | — | — |

## Update History

- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the cited evidence-lane member and its declared classification and corrected its incoming range. Existing source verification provenance is retained.
- 2026-09-05T06:24:16+00:00: Generated citation repair: "mcp/tests/test_requirement_acceptance_envelope_doctrine.py" repointed to mcp/tests/test-evidence-lanes.toml:539-539. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T17:15+02:00 — No content impact: re-anchored the unchanged architecture-fitness row
  to mcp/tests/test-evidence-lanes.toml:513-513 (committed tree `ce7f10b5`) after intermediate
  lane registrations and the L20 standalone terminal rail-failure registration shifted the
  manifest. Requirement-envelope proof and lane ownership are unchanged.

- 2026-09-01T08:13+02:00 — No content impact: re-anchored the unchanged architecture-fitness row
  after the three final CCR-R01 coverage companions shifted the manifest. Requirement-envelope
  proof and lane ownership are unchanged.

- 2026-09-01T05:22+02:00 — No content impact: re-anchored the unchanged architecture-fitness row
  after six CCR-R01 unit-regression declarations shifted the manifest. Requirement-envelope proof
  and lane ownership are unchanged.

- 2026-09-01T04:34+02:00 — No content impact: repaired the architecture-fitness manifest citation
  after two certification suites entered `unit-regression`; the acceptance-envelope proof is
  unchanged.

- 2026-08-31T20:30+02:00 — No content impact: repointed the architecture-fitness manifest row
  after an earlier unit-regression entry was inserted. Requirement-envelope proof is unchanged.

- 2026-08-29T07:35+02:00 — Repaired the exact evidence-manifest citation after the future-code
  integration-lane row shifted the architecture-fitness block; the acceptance-envelope contract
  and its source test are unchanged.

- 2026-08-28T14:18+02:00 — Reconciled requirement-ownership test names and ranges against the
  committed PDLS candidate; each leaf still owns one complete primary requirement block.

- 2026-08-28T11:51+02:00 — Added forcing for one-primary worker output and reviewer independence
  from the plan author.

- 2026-08-28T11:32+02:00 — Narrowed leaf closure proof to its one owned primary revision, retained
  dependency/preservation checks as context, and added packet-supersession and gate-boundary forcing.

- 2026-08-27T14:04+02:00 — Extended the acceptance-envelope proof with approved
  version-addressed packet inspection and packet-local durable corpus-ruling evidence.
- 2026-08-27T13:32+02:00 — Extended the structural envelope proof from stable IDs to exact stable
  ID + version pairs and matching canonical packet inspection under M39@v1. Verification remains
  closeout-owned.

- 2026-08-27T12:43+02:00 — M38: created the focused structural proof sidecar. Verification
  metadata remains empty until governed closeout stamps the PDLS code commit.
