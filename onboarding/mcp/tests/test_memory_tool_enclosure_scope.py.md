# mcp/tests/test_memory_tool_enclosure_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_tool_enclosure_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

This suite proves that contract-scoped memory tools use the leaf's exact code and memory worktrees,
while bare calls use the configured official repository. It also proves every invalid enclosure
refuses instead of falling back to another memory tree.

## Code Commentary

### Logic

The fixture creates official code/memory repositories plus linked leaf worktrees and a real leaf
contract. Route-index tests prove writes and dry runs target only the requested tree. Quality and
drift tests prove reads use both named leaf roots. Contract-scoped quality additionally asserts that
the leaf base reaches `DriftCheckContext.unstamped_code_commit`, while the bare official call leaves
that field `None`; this is temporary claim-comparison provenance, not metadata mutation. A full
contract check atomically replaces the human Markdown checklist and publishes its structured JSON
attestation as the only two files in the enclosure-local report directory.

Refusal tests cover foreign-repository contracts, missing memory worktrees, internal-memory leaves,
out-of-root contract paths, and repositories without memory configuration. Every case fails closed.

### Conventions

- Build both official and leaf trees from real Git repositories rather than mocking path identity.
- Compare whole-tree snapshots around route-index operations to prove the non-target stays untouched.
- Patch only the package runner when inspecting the exact drift-context arguments passed by the
  application entry point.

### Invariants And Boundaries

- `contract_path` selects the leaf code and memory trees together.
- A bare call does not inherit the leaf's temporary unstamped provenance.
- No invalid contract may fall back to official memory.
- The tests prove scope/comparison wiring; claim semantics remain owned by `memory_quality`.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the contract is package-internal and proved by the
application source plus this regression suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture constructs distinct official and leaf repositories joined by one enclosure contract. | `_Enclosure`; `_enclosure` | mcp/tests/test_memory_tool_enclosure_scope.py:69-159 |
| Route-index tests prove scoped writes/dry-runs leave the non-target tree untouched. | `RouteIndexRefreshWritesTheNamedTreeTests` | mcp/tests/test_memory_tool_enclosure_scope.py:176-215 |
| Quality tests prove leaf selection, paired Markdown/JSON curator publication, temporary base forwarding, and strict bare-call provenance. | `MemoryQualityCheckReadsTheNamedTreeTests` | mcp/tests/test_memory_tool_enclosure_scope.py:219-289; mcp/tests/test_memory_tool_enclosure_scope.py:291-329 |
| Drift tests measure the named leaf onboarding against the named leaf code. | `DriftCheckReadsTheNamedTreesTests` | mcp/tests/test_memory_tool_enclosure_scope.py:324-342 |
| Invalid enclosures refuse and the helper constructors preserve typed contract/config shapes. | `RefusalTests`; `_replaced`; `_config_without_memory_root` | mcp/tests/test_memory_tool_enclosure_scope.py:348-438; mcp/tests/test_memory_tool_enclosure_scope.py:441-443; mcp/tests/test_memory_tool_enclosure_scope.py:446-449 |

## Cross-Repo References

No cross-repository implementation dependency governs this test.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260821-DAGQC-L2 Extracted Scope Boundary

The enclosure cases now address `resolve_memory_scope` and the typed controller directly. They force
same-repository leaf authority, frozen code/onboarding/base identity, loud refusal when a leaf has no
usable memory tree, and the deliberate absence of an official-memory fallback.

## Update History

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: rebound enclosure tests to the extracted scope/controller APIs and forced canonical leaf identity plus loud no-memory/no-official-fallback behavior. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T11:07+02:00 — L3 content update: the enclosure-local quality fixture now expects
  both the human curator report and its structured JSON attestation, matching the queue evidence
  contract without broadening write scope.
- 2026-08-11T16:54+02:00 — Added full-check proof that one enclosure-local curator report is
  atomically replaced without siblings, plus subset-call non-interference and component-count
  arithmetic.
- 2026-08-11T14:40+02:00 — Replaced the stale symbol inventory with the current enclosure-scope
  contract, added the temporary-base versus bare-call distinction, and regenerated every source range.
- 2026-08-08T17:18+02:00 — Re-verified the suite after the L9 application-model extraction; scope
  and refusal behavior remained unchanged.
- 2026-08-05T00:00+02:00 — Created for the enclosure-scoped memory-tool regression suite.
