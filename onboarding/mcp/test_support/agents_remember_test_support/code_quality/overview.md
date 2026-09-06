# Python Quality Verification Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/test_support/agents_remember_test_support/code_quality` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T21:56+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Python verification infrastructure](../overview.md)

## What This Area Is

Repository verification infrastructure for quality planning, exact test selection, Dagger-produced evidence, diagnostic scoring, causal failure reporting and retry reuse. Shipping it alongside source does not make it operational product behavior. Static checks include product and verification inputs; production coverage and CRAP measurement exclude tests and support.

## Hot Path Summary

`quality_plan.py` owns typed configuration and command planning; `check.py` executes/interprets the rails. `profile_selection.py` publishes the selected population and `profile_rails.py` rederives and validates exact scope before execution. `dependency_ownership.py` and `scope.py` establish supported consumers and explicit product/verification ownership. `retry_proof.py`, `retry_coverage.py` and child-environment helpers preserve admitted retry inputs without leaking outer retry/progress controls into candidate tests.

## Operating Model

Targeted scope is derived from source and declared consumers, never guessed from unknown ownership. Missing, ambiguous, dynamic, stale or contradictory ownership remains explicit and refuses targeted admission instead of widening to a full suite. A full population is an explicit selection. Compare canonical POSIX-string populations while preserving duplicate detection; a differently ordered `Path` list is not a new authority.

Coverage and CRAP reports describe the selected production inputs. Their findings are diagnostic, while a broken report tool remains a failure. Retry data may be reused only under its exact admitted candidate, environment, tools, selected population and published artifact identity. Fresh and retained coverage databases remain separate until the owning successful execution merges/publishes them; missing expected artifacts cannot masquerade as known-empty proof.

Causal reports distinguish a proved dependent node from an independent same-file node. Missing causal evidence cannot invent safe suppression or broaden unowned selection. Declared report paths and source applicability govern teardown evidence; a skipped clean-room scenario is explicitly non-applicable, not successful execution. Persisted physical producer bytes, export bindings and immutable report generations are distinct from synthetic test payloads.

## Local Invariants And Traps

Do not reconstruct the deleted host diagnostic analyzer/manifest machinery to permit ordinary pytest: that development loop already exists. Do not add percentage floors, a CRAP exception registry or source-pinning tests to satisfy historical claims. Do not silently grow case budgets or move unit bloat under integration markers. Profile planning, execution and certifying publication stay separate owners.

## File-Level Onboarding Map

Use the generated adjacent route index for existing source/sidecar membership after its owner refreshes it. This overview does not promise one card for a deleted source file or maintain a parallel static inventory.

## Historical Context

The original PDLS/CCR entries explain exact-scope, retry and publication repairs. Their historical exact consumer counts and old coverage enforcement are not current policy. Current source and the diagnostic policy below govern; history is retained for provenance.
## Development And Certification Policy

Ordinary Python development is supported directly through `mcp/.venv/bin/python -m pytest`; four workers run the isolated unit population. `-m integration` selects the small real-boundary population and `-m ""` selects both. Focused file/node execution, including serial debugging, is valid development work and does not acquire certification authority. The repository declares budgets of 1,000 unit and 150 integration parametrized collected cases. Extend or consolidate distinct behavior protection before adding cases; do not restore deleted matrices, private-branch tests or unused fixture machinery because an old milestone names them.

Coverage, including changed-line coverage, is diagnostic only. No percentage floor requires additional tests. Production-only CRAP retains 20 as a review trigger, not a delivery blocker; tests and verification support are excluded. Lint, formatting, typing, structural rules and test failures still enforce. Diagnostic-tool execution errors remain visible failures distinct from metric findings. There is no coverage baseline, score-exception registry or ratchet.

Only genuine Dagger admission and the existing lifecycle owners can issue immutable candidate-bound certifying evidence. A host pytest pass, copied report, green helper result or use of Dagger alone is insufficient. Reuse the existing shared engine and preserve process identity, disposable state, credential isolation, exact candidate and publication ownership. Full-suite execution and whole-master independent review belong to the master aggregation boundary under the current execution policy; this overview does not impose either on every leaf. Focused development evidence remains useful without pretending to be final acceptance.
## Repo-Internal References

These current source and policy ranges establish the development/certification distinction and the existing memory preparation surfaces. A citation is source evidence, not a recorded test execution.

| Finding | Anchor | Source |
| --- | --- | --- |
| Development commands, budgets, diagnostic metrics and isolation. | `# Python test policy and commands` | docs/design/python-pytest-bootstrap.md:1-50 |
| Certifying publication and accepting consumers. | `# Python Test Evidence Authority` | docs/design/python-test-evidence.md:1-65 |
| Exact contract scope, full check and curator worklist publication. | `_resolve_execution`; `_execute_memory_quality`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality/controller.py:295-441 |
| Interactive catalog names missing authority without eligibility. | `_attach_final_full_catalog` | mcp/src/agents_remember/application/memory_quality/controller.py:444-480 |
| Final memory adapter requires the selected four-code-terminal prefix. | `PreparedMemoryCertificationAdapter` | mcp/src/agents_remember/memory_quality/prepared_certification.py:396-437 |
| Finalization consumes original selected fifth-certificate inputs. | `PreparedCloseoutContinuation` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/continuation.py:18-45 |

| Exact profile scope and suite execution. | `_require_exact_scope`; `_paths`; `_run_python_suite`; L92-L214 | [Profile rails](mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:92-214) |
| Plan composition and typed command steps. | `CheckConfig`; `Step`; `quality_steps`; L100-L168 | [Quality plan](mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:100-168) |
| Teardown proof from source applicability and exact result bytes. | `_verify_teardown`; `_verify_started_teardown`; `_write_teardown_proof`; L253-L359 | [Teardown owner](mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:253-359) |

## Docs And Cross-Repo References

No Domain Documentation entries are configured in the resolved memory root. Current local policy and source owners are cited above; no live external system or sibling repository is used to grant authority.

## Update History

- 2026-09-06T21:56+00:00 — Reconciled the governing route against IAS d3610903 and retained source/card evidence. Replaced obsolete host-test prohibitions, coverage floors and deleted-suite claims with the current preparation/development/certification boundaries. Existing history and verification pins remain preserved; this is semantic memory preparation, not acceptance.

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation: Added canonical string scope ordering and exact population guards, refreshed the shifted teardown owner ranges, and retained the actual L32/C97 teardown contract; no later L33 source-applicability behavior is imported.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Reconciled exact ambient-runner ownership, persisted teardown proof and repaired producer/publication boundaries; removed obsolete print-only and missing-producer claims.

- 2026-09-05T07:08+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Removed obsolete safe-full selection behavior; added selector identity, exact rail scope, causal selected-population limit and unproduced teardown-proof boundary. Verification records current source claims, not execution or acceptance.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 registered the five exact, independently observed
  `layers.toml` consumers. The declaration avoids safe-full selection without making metadata
  self-proving or adding a fallback. Verification remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 added source-verified exact consumer ownership for `.codex/config.toml`; the candidate resolves completely without global invalidation or a silent narrow fallback. Verification remains closeout-owned.

- 2026-08-29T19:04+02:00 — Reconciled the projection generator with Python 3.13 named-literal
  schema definitions after the lifecycle-owned fast gate exposed the former inline-only assumption.
  Verification remains closeout-owned.

- 2026-08-28T04:48+02:00 — Split typed plan construction from quality execution and added the
  causal-report safe-continuation owner; unavailable evidence now selects the full population.
- 2026-08-27T19:13+02:00 — Added the explicit all-contexts-affected retry state while retaining
  missing-artifact refusal.
- 2026-08-27T18:33+02:00 — Added the explicit retained/fresh coverage-composition owner and
  outer-wrapper/child-rail environment boundary after the real xdist retry run exposed both
  ownership collisions.
- 2026-08-27T11:08+02:00 — Rehomed the quality producer under verification authority; documented
  explicit package scope, source-derived ownership, persistent Dagger retry, and exact causal
  behavior. Verification remains closeout-owned.
