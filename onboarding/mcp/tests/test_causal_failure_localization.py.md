# mcp/tests/test_causal_failure_localization.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_causal_failure_localization.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T14:18+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Proves that causal preflight failures suppress only source-derived exact dependent nodes while
independent nodes—including nodes in the same file—continue, and that machine/human failure
evidence preserves distinct repair families and exact retry inputs.

## Code Commentary

### Logic

The suite exercises the real lifecycle-owner preflight, derives three exact dependent nodes through
one shared helper, forces that owner to fail, and verifies the complete blocked-node payload. A
synthetic pytest collection proves one selected exact node is marked while a same-file independent
node remains runnable. The report round-trip checks machine/human parity. Runtime-profile forcing
separately covers async, process, multiprocessing, subprocess, socket, timeout, and environment
errors and retains worker, seed, process topology, duration, failure family, and retry semantics.
The source-derivation fixture also covers a directly imported owner class followed by an attribute
call, preventing that real dependency form from escaping the exact-node graph.

### Conventions

Named constants hold full pytest node IDs so file-level suppression cannot accidentally satisfy
the assertions. The controlled environment flag is used only by the non-accepting Dagger causal
evidence route.

### Invariants And Boundaries

- Dependency authority is source-derived; observer imports and unrelated reverse importers do not
  become causal dependents.
- Suppression is exact-node, never whole-file or whole-suite.
- Specific runtime exceptions cannot silently fall through to the environment/OSError family.
- Causal artifacts are non-accepting and cannot grant a green result.
- Unclassified failures must be classified before retry instead of receiving guessed semantics.

### Todos

None.

## Docs References

No Domain Documentation source is configured; causality is a repository-owned verification
contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is needed for this exact-node forcing suite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Source derivation yields the three exact dependent contracts and excludes same-file and unrelated observers. | `test_source_derivation_excludes_observer_and_independent_nodes` | mcp/tests/test_causal_failure_localization.py:146-167 |
| A failed owner blocks only source-proved exact nodes during collection. | `test_failed_owner_blocks_only_source_proved_exact_nodes`; `test_collection_suppresses_one_exact_node_not_its_file` | mcp/tests/test_causal_failure_localization.py:169-202 |
| Machine/human reports share one payload and runtime failures retain reproducible worker, seed, process-topology, timing, family, and retry inputs. | `test_machine_and_human_artifacts_render_from_one_payload`; `test_observed_runtime_failures_retain_exact_retry_inputs` | mcp/tests/test_causal_failure_localization.py:204-257 |
| Explicit forcing covers async, multiprocessing, subprocess, process, socket, timeout, and environment families without umbrella fallthrough. | `test_runtime_failure_families_have_distinct_repair_owners` | mcp/tests/test_causal_failure_localization.py:278-292 |
| The dependency derivation implementation owns the source walk and exact-node contract. | `derive_causal_nodes`; `_derive_causal_nodes` | mcp/test_support/agents_remember_test_support/testing/causal_dependency.py:41-98 |

## Cross-Repo References

No meaningful cross-repository boundary applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No sibling repository or external service participates. | — | — |

## Update History

- 2026-08-28T14:18+02:00 — Reconciled causal-localization test symbols and ranges against the
  committed PDLS candidate; the documented proof behavior is unchanged.

- 2026-08-28T11:32+02:00 — Added direct imported-owner-class attribute-call forcing to the causal
  dependency proof.

- 2026-08-28T10:03:40+02:00 — Expanded the source-derived cascade to three dependent contracts and
  added forcing for every distinct runtime family plus process-topology retention.
- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: created the missing sidecar for source-derived
  exact-node causality, safe independent continuation, and reproducible failure evidence.
