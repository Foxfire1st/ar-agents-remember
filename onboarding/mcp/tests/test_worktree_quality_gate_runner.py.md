# mcp/tests/test_worktree_quality_gate_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_quality_gate_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T20:55+02:00 |
| lastVerifiedCommitHash | `77bc614506b8b50937aed6846523547d36045947` |
| lastVerifiedCommitDate | 2026-08-24T20:41:34+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

Owns the Dagger-only quality command, preview, host-refusal, container memory-cap,
report-replacement, and failure-transport regressions split from the closeout mutation suite.

## Code Commentary

### Logic

`CodeQualityGateTests` proves wrapper applicability and altitude, exact diff-base forwarding,
container-runtime-managed and explicitly capped full Dagger gates, immediate host-execution
refusal, atomic replacement of the one enclosure test report, and bounded failure output.

### Conventions

Checkout and target helpers remain single-owned in `test_worktree_closeout_quality_gate.py` and are
imported here; runner policy and closeout mutation are separate test responsibilities.

### Invariants And Boundaries

- Leaf closeout runs targeted Dagger acceptance; master integration runs full Dagger acceptance.
- Explicit caps report `mode=explicit-cap`; absent caps report
  `mode=container-host-managed`. Both retain container-runtime-managed swap.
- Host quality execution refuses before resolving an interpreter or invoking a wrapper.
- The report path is stable and each completed run replaces its predecessor.
- Missing wrappers and invalid modes fail loudly rather than weakening the gate.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this repository-local runner suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The runner suite covers preview, execution, cap, report, interpreter, and failure contracts. | `CodeQualityGateTests` | mcp/tests/test_worktree_quality_gate_runner.py:35-498 |
| Stable helpers remain in the closeout mutation suite. | `_checkout_with_wrapper`; `_quality_target` | mcp/tests/test_worktree_closeout_quality_gate.py:47-61; mcp/tests/test_worktree_closeout_quality_gate.py:64-70 |

## Cross-Repo References

The runner can certify a consuming repository's checkout when that checkout carries the wrapper.

| Finding | Anchor | Source |
| --- | --- | --- |
| Applicability is determined from the supplied checkout rather than a repository name. | `quality_wrapper_path`; `requires_strict_code_quality` | mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:80-82; mcp/src/agents_remember/worktrees/modules/code_quality_gate.py:119-132 |

## L23 Host-Execution Removal

The former local diagnostic runner, interpreter selection, host environment construction,
systemd/rlimit command planning, and their tests are removed from the acceptance adapter. The
remaining named local entry point is a refusal surface and never resolves or starts a wrapper.

## R39 Runner Policy Proofs

The runner suite separates consumer adapter opt-in from the Agents Remember self-wrapper policy
and requires the latter to refuse when missing. It proves local quality execution always raises
before wrapper resolution, keeps Dagger as the only plan/executor, and removes tests for deleted
host interpreter, environment, subprocess, and memory-cap machinery.

## R43 Builder-Level Dagger Refusal

The runner suite now calls `_gate_command_parts` and `_memory_policy_payload` with a local executor
and requires both to reject it with pinned-Dagger guidance. The missing-wrapper assertion uses the
same `self-owned wrapper` wording as production.

## 260824-PDLS Lifecycle Evidence Proof

Successful clean-quality fakes now return `CleanQualityOutcome` with certifying evidence bound to
the checkout's current `git write-tree`. Gate tests therefore exercise the same typed lifecycle
consumer boundary as production instead of treating any zero-exit subprocess as acceptance.

## Update History

- 2026-08-24T20:55+02:00 — Replaced zero-exit-only fakes with candidate-bound certifying outcomes.

- 2026-08-14T12:13:26+02:00 — R43 curator: recorded builder-level non-Dagger refusal and aligned
  missing-wrapper wording. Verification remains closeout-owned.

- 2026-08-14T11:27+02:00 — R39 curator: reconciled the test card with self-policy, immediate host
  refusal, and the simplified Dagger-only adapter. Verification remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: quality-runner tests require Dagger-only
  execution, explicit mode/diff base, exact candidate materialization, fail-closed status, and no
  host or direct-Docker compatibility path.
- 2026-08-12T20:10+02:00 — L23 curator: documented short native temp-root propagation through the quality runner; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 replaced a platform branch in the test expectation with an equivalent lookup; host-managed and explicit-cap runtime behavior is unchanged.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: added the
  host-managed full command/report proofs and resource-policy payload coverage;
  retained explicit-cap failure proofs. Verification metadata remains pinned
  until closeout stamps L24.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: created from `CodeQualityGateTests` in the
  closeout quality-gate suite; retained shared helpers and separated runner policy from closeout
  mutation while bringing both files below the hard size gate.
