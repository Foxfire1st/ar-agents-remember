# mcp/tests/test_dispatch_agent_ambient_reviewer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dispatch_agent_ambient_reviewer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T12:00+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves ambient reviewer dispatch derives only unambiguous manager parents, reuses an identical live
generation, and refuses sprint ambiguity before host effects.

## Code Commentary

### Logic

The suite constructs leaf, master, and sprint task topology, seeds the exact current source-lineage
contracts, and calls the public structural dispatch surface with reviewer role. Assertions cover
parent stamps, idempotent reuse, and the typed ambiguous sprint refusal. The fake-host fixture sets
the readiness wait to zero so this ownership suite proves durable queueing rather than spending a
production startup window on an adapter that the fake intentionally does not launch.
The helper-level forcing case separately proves that a leaf with no canonical owning master is a
typed refusal, never a guessed parent.

### Conventions

The tests observe public outcomes and catalog generations rather than calling the parent helper alone.

### Invariants And Boundaries

- Leaf and master manager ownership is exact.
- Same-parent repeats do not create duplicate live seats.
- Sprint dispatch cannot choose architect or orchestrator implicitly.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Leaf/master ownership and reuse are executable contracts. | `test_leaf_and_master_reviewer_get_the_only_unambiguous_manager_parent`; `test_same_parent_repeat_reuses_the_live_reviewer_generation` | mcp/tests/test_dispatch_agent_ambient_reviewer.py:84-94; mcp/tests/test_dispatch_agent_ambient_reviewer.py:96-108 |
| Sprint ambiguity refuses before host effects. | `test_sprint_reviewer_refuses_ambiguous_parent_before_host_effects` | mcp/tests/test_dispatch_agent_ambient_reviewer.py:110-117 |

## Cross-Repo References

No cross-repository implementation dependency governs this suite.

## Update History

- 2026-08-31T13:42+02:00 — A005 closeout repair added the missing-parent leaf-reviewer refusal
  branch required by changed-unit coverage.

- 2026-08-31T12:00+02:00 — A005 repair supplied the required current lineage and bounded fake-host
  readiness wait so the suite reaches reviewer ownership without bypassing production admission.
  Verification remains closeout-owned.

- 2026-08-31T07:35+02:00 — Created for 260821-ARSPAWN-L5 independent-review repair. Verification remains closeout-owned.
