# Python Quality Verification Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/test_support/agents_remember_test_support/code_quality` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-18T12:32+02:00 |
| lastVerifiedCommitHash | `d9becade1a373f2272501f7451746ccc259ca9ac` |
| lastVerifiedCommitDate | 2026-09-18T12:33:45+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Python verification infrastructure](../overview.md)

## 260918-TSIP-L1 Instrument-Discipline Helpers

This route gained a fourth verification-helper module, `instrument_discipline.py`, beside
`citations.py`, `structural_limits.py` and `scope.py`. It is a helper library, not a gate: it exposes
no CLI, no registry entry and no plan step, and the quality plan does not invoke it.

What it owns is narrower and older than this route's other helpers. Each of its four surfaces makes
one *measurement admissibility* condition mechanical, so an inadmissible measurement cannot be
stated at all — and after this leaf's independent review those conditions are strictly stronger than
the first revision shipped. As the repaired source now states them:

- a count or a zero is returned only after the pattern reproduced a positive witness, refused a
  negative one, **and is the pattern the probe actually proved**: a proved probe licenses the shape
  it proved and nothing else;
- a captured window ends at its unit boundary and reports which boundary closed it, **the line cap
  included**, so a capped capture is never shaped like a complete one and the lines it left unread
  stay visible;
- a pass claim printed after a crash marker is refused as not attributable to a run that completed;
  an artifact with **no recorded run** — no exit status recorded as one, and no producer transcript —
  is refused; a run that **exited non-zero and reported no result** is refused as a crash, because
  that is the shape a crash takes when it leaves no traceback; and a clean result with no stated way
  to fail is refused as vacuous, where the evidence that the check can fail must be a **non-zero**
  result rather than the presence of the word `finding` in a disclaimer;
- a record must name a producer that exists in the package, with a command and a revision, before the
  producer is accepted as the artifact's source; reproduction is then byte-exact, writes its scratch
  output **outside the directory holding the evidence it is checking**, and answers `matches=False`
  rather than raising when the producer exits non-zero or writes nothing.

That places it in the route as *instrument* evidence rather than product evidence. Its contract test
is `mcp/tests/test_instrument_discipline.py`, registered in the `architecture-fitness` lane of
`mcp/tests/test-evidence-lanes.toml`; the test imports this package and executes nothing over a real
boundary, which is why the structural-invariant lane is the behaviour-preserving one for it and
`unit-regression` is not. The route's own rule that coverage and CRAP are diagnostic applies
unchanged here: the helper exists to make a number trustworthy, not to raise a metric, and it is
excluded from production measurement like its siblings.

Because this module is where the previous master's instrument faults became checks, its card carries
the one fault the check committed against itself — a `\b` that cannot match the plural `findings`,
which the shipped unit cases passed with. That is recorded on the file card and is deliberately not
smoothed here: a route that presented its own instrument as faultless would be the class this route
just shipped a guard against.

## What This Area Is

Repository verification infrastructure for quality planning, exact test selection, Dagger-produced evidence, diagnostic scoring, causal failure reporting and retry reuse. Shipping it alongside source does not make it operational product behavior. Static checks include product and verification inputs; production coverage and CRAP measurement exclude tests and support.

## Hot Path Summary

`projection_types.py` renders the dashboard projection contract from the Python wire schemas: it folds
the served projection's own definitions into the generated TypeScript and compares that definition set
EXACTLY, so extending `ServedWorkspaceProjection` forces a declaration here plus a regeneration of
`dashboard/src/types/projection.ts`. Its keyword vocabulary is closed and fails closed: a refinement
TypeScript cannot enforce structurally (a `minimum`/`maximum`, a length, a pattern) is emitted beside
the affected property, and an undeclared keyword refuses generation instead of disappearing from
either contract.

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
| Interactive catalog names missing authority without eligibility. | `_attach_final_full_catalog` | mcp/src/agents_remember/application/memory_quality/controller.py:550-586 |
| Final memory adapter requires the selected four-code-terminal prefix. | "class PreparedMemoryCertificationAdapter:" | mcp/src/agents_remember/application/prepared_certification.py:749-813 |
| Finalization consumes original selected fifth-certificate inputs. | `PreparedCloseoutContinuation` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/continuation.py:18-45 |

| Exact profile scope and suite execution. | `_require_exact_scope`; `_paths`; `_run_python_suite`; L92-L214 | [Profile rails](mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:92-214) |
| Plan composition and typed command steps. | `CheckConfig`; `Step`; `quality_steps`; L100-L168 | [Quality plan](mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:100-168) |
| Teardown proof from source applicability and exact result bytes. | `_verify_teardown`; `_verify_started_teardown`; `_write_teardown_proof`; L253-L359 | [Teardown owner](mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:253-359) |

## Docs And Cross-Repo References

No Domain Documentation entries are configured in the resolved memory root. Current local policy and source owners are cited above; no live external system or sibling repository is used to grant authority.

## Update History
- 2026-09-18T12:32+02:00 — 260918-TSIP-L1 curator, **second pass** (uncommitted change set on
  `ar/260918-tsip-l1-ar`, base `f0313143`): this route's governor changed under it again. The leaf's
  independent review returned three blocking findings and the fix worker revised
  `instrument_discipline.py` **361 → 432 lines**, so the section above was **corrected rather than
  annotated**: it now states the repaired contract — the pattern-licence binding in `counted_pattern`,
  the `line cap` closer in `capture_bounded_window`, the narrow recorded-exit rule and the fourth
  refusal in `check_artifact_refusal`, the non-zero-result vacuity rule, and reproduction that writes
  into a scratch directory and answers `matches=False` instead of raising. This route carries no
  counts or line numbers for that module, so nothing here had gone stale *numerically*; what had gone
  stale was the strength of the contract it described, which a reader would have taken as the shipped
  one. `lastUpdated` advances with this body edit; `lastVerifiedCommitHash`/`lastVerifiedCommitDate`
  are deliberately unchanged because the candidate is uncommitted and the governed closeout owns the
  real code and memory commits.

- 2026-09-18T11:46+02:00 — 260918-TSIP-L1 curator (uncommitted change set on `ar/260918-tsip-l1-ar`,
  base `f0313143`): this route's governed sources changed, so a body section was **added rather than
  annotated** — `## 260918-TSIP-L1 Instrument-Discipline Helpers`, recording that the route gained a
  fourth verification-helper module beside `citations.py`, `structural_limits.py` and `scope.py`. The
  section states what the module owns (four measurement-admissibility conditions, each refusing
  rather than returning an unlicensed number), why it lands in this route as *instrument* evidence
  rather than product evidence, and why its contract test is registered in the
  `architecture-fitness` lane. It also carries the module's own first-draft fault rather than
  smoothing it. The loader was re-run at this candidate and is silent — `pytest
  tests/test_evidence_lanes.py tests/test_suite_budget.py -q` → **4 passed in 0.54 s**. Verification
  metadata remains closeout-owned: `lastUpdated` tracks this body edit, and
  `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are deliberately unchanged because the candidate
  is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`, base
  `99534dc5`, `projection_types.py` +30/−11): this route's generator changed, so a body section was
  added rather than an annotation. `projection_types.py` now states the current contract: the served
  projection's definitions are folded into the generated TypeScript and compared EXACTLY, so extending
  `ServedWorkspaceProjection` forces a declaration here plus a regeneration; and its keyword vocabulary
  is closed and fails closed, emitting an unenforceable refinement beside the affected property while
  refusing an undeclared keyword. The leaf's own change was the `maximum` refinement (so the observer
  health record's 32-bit counters state their ceiling) and the `TerminalObserverHealth` declaration;
  detail lives in the file card. Verification metadata remains closeout-owned; no stamp advanced.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/test_support/agents_remember_test_support/code_quality` carries local unstaged changes not
  represented in HEAD. Re-read the card against the frozen on-disk source and re-checked its claims
  and cited ranges: nothing this card asserts is falsified by the change, so no wording changed.
  Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: repointed the `PreparedMemoryCertificationAdapter` citation to `mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py:721-785`, where commit `deb032fb` moved the adapter out of `memory_quality/`. Citation path only; the cited claim is unchanged and verification metadata remains pinned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `PreparedMemoryCertificationAdapter` repointed to mcp/src/agents_remember/memory_quality/prepared_certification.py:721-785. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:45:44+00:00: CCR-L24 preparation reviewed `PreparedMemoryCertificationAdapter` and `_attach_final_full_catalog` against the current code candidate; wording retained and ranges regenerated. Verification metadata remains pinned pending final pair composition.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `_attach_final_full_catalog` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:499-535. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:39:58+00:00: Generated citation repair: `PreparedMemoryCertificationAdapter` repointed to mcp/src/agents_remember/memory_quality/prepared_certification.py:479-542. No content impact: mechanical anchor-range projection bound to citation source snapshot 5911742cfcc7a53db92b36b80bac02ee49a67204b190c0311a81bcc2e388ad59; claim bytes unchanged; generated by ccr-r10@v1.

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
