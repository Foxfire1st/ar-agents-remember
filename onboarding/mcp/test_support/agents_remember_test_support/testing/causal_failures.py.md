# mcp/test_support/agents_remember_test_support/testing/causal_failures.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/causal_failures.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T10:16:27+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python test infrastructure overview](overview.md)

## Purpose

Implements pytest-side exact-node causal suppression, observed failure-family classification, and
durable non-accepting causal reports.

## Code Commentary

### Logic

Hooks load and structurally validate the owner-preflight report, classify retry semantics, and
index blocked status by exact pytest node id. Only a collected node that appears in a source-proved
dependency chain receives a skip marker. Other nodes in the same file still execute. Retry family
is derived from the actual observed exception chain—not imports present in the test file—and keeps
async, process, multiprocessing, subprocess, socket, timeout, and residual environment/OSError
owners distinct. The most-specific match wins, so a connection or timeout does not also become a
generic environment failure. Runtime evidence carries the actual serial/xdist process topology,
seed, worker, timing, and retry semantics. Unknown observed assertions stay independent. JSON and
Markdown render from the same bounded payload.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Blocked status requires a failed owner preflight plus a valid owner-to-exact-node chain;
  file membership is never sufficient.
- Independent and same-file sibling nodes remain observable, including process-sensitive failures.
- Each observed exception belongs to one most-specific runtime family; umbrella OSError matching
  cannot erase its socket, timeout, or child-process owner.
- Causal output is explanatory and non-accepting; an invalid causal artifact disables suppression
  and the quality owner runs the complete selected population.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `pytest_collection_modifyitems` | mcp/test_support/agents_remember_test_support/testing/causal_failures.py:82-108 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| Collection blocks only exact node ids present in the validated causal report and records serial/xdist topology for every collected item. | `pytest_collection_modifyitems`; `_process_topology` | mcp/test_support/agents_remember_test_support/testing/causal_failures.py:82-108; mcp/test_support/agents_remember_test_support/testing/causal_failures.py:255-265 |
| Runtime evidence separates observed blocked nodes from independent failures while retaining worker, seed, topology, and timing. | `pytest_runtest_logreport`; `runtime_failure_record`; `_runtime_evidence` | mcp/test_support/agents_remember_test_support/testing/causal_failures.py:129-168; mcp/test_support/agents_remember_test_support/testing/causal_failures.py:185-193 |
| Observed exception chains map each exception to one most-specific async, multiprocessing, subprocess, process, socket, timeout, or environment family. | `execution_profile`; `_OBSERVED_RUNTIME_FAMILIES`; `_observed_runtime_families` | mcp/test_support/agents_remember_test_support/testing/causal_failures.py:196-252 |
| Validation refuses missing owners, unknown exact nodes, conflicting identity, invalid chains, and incomplete runtime evidence. | `_validate_causal_report`; `_validate_blocked_rows`; `_validate_runtime_evidence` | mcp/test_support/agents_remember_test_support/testing/causal_failures.py:389-520 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `CAUSAL_REPORT_OPTION` | mcp/test_support/agents_remember_test_support/testing/causal_failures.py:19-19 |

## Update History

- 2026-08-28T10:03:40+02:00 — Split process, multiprocessing, subprocess, socket, async, timeout,
  and environment/OSError families and added explicit serial/xdist topology to retry evidence.
- 2026-08-28T04:37+02:00 — Derived retry family from observed exception chains and aligned invalid
  causal-artifact recovery with full-population safe mode.
- 2026-08-27T11:14+02:00 — Reconciled exact-node suppression, same-file independent execution,
  runtime failure separation, and non-accepting JSON/Markdown evidence.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
