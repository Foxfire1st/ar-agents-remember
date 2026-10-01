# Python Quality Verification Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/test_support/agents_remember_test_support/code_quality` |

## Governing Overview

[Python verification infrastructure](../overview.md)

## 260918-TSIP-L2 Record-Integrity Comparisons

This route gained a **fifth** verification-helper module, `record_integrity.py` (**1110 lines**),
beside `citations.py`, `structural_limits.py`, `scope.py` and L1's `instrument_discipline.py`. Like
its sibling it is a helper library and not a gate: no quality-plan step, no registry entry. It is the
only module in this route that reads the **task and memory records** rather than the code.

What it owns is the drift shape this master is about — a document that was true when written and
silently stopped being true. Each of its four comparisons reads a declared value out of one artifact
and the authoritative value out of another, and reports the rows where they disagree while naming both
sides and the number of rows compared:

- a leaf document's `status` against its own enclosure contract's `closeout`/`integration` cells;
- a master's `subTasks[].status` row against the status the shipped rule derives from the leaf
  document beside it — `Completed` requires the document to be `Completed`, never merely every step
  marked, which is `D42`'s fix restated as `derived_master_status`;
- a register row's `→ L<n>` arrow against the leaf ids the owning master actually declares;
- a **figure written in prose** — a line count or a case count — against the source it describes, at
  the revision the prose names. This is the comparison the memory layer's own checks cannot make:
  `range_resolution` looks only inside cited ranges and `claim_reopen` only at cited claims, so a
  number written as prose is invisible to both. It is recorded as `T45`, and on the previous leaf it
  was found by grepping the tree rather than by running the checker.

Two properties are the route's business rather than the module's. **Every comparison states the two
populations it compared** beside its findings, because "0 disagreements" without them is a zero nobody
can license — the rule L1's `instrument_discipline.py` enforces for a text probe, applied to a record.
And **every unanswerable question refuses by name** instead of returning a zero: no coordination root,
a root carrying no `tasks/` tree, a base commit that does not resolve, a source outside any Git tree,
and a claim whose shape is not `PATTERN:SHAPE:SOURCE:DOCUMENT[:DOCUMENT...]`.

What it deliberately does **not** do is stated on its own card rather than smoothed here: the
register's prose census has no honest check, because finding the census means parsing free-form
Markdown and its bucket rule is undeclared; and the contracts with no matching leaf document are
counted rather than judged.

Its contract suite is `mcp/tests/test_record_integrity.py` (**1140 lines, 37 cases** — 1000 lines when
it was delivered, and the case count has not moved since), registered in
the `architecture-fitness` lane of `mcp/tests/test-evidence-lanes.toml` because the module imports
this package and executes nothing over a real boundary. Fourteen of those cases read the real record
and **skip** without `AR_COORDINATION_ROOT`, and the `T45` documents are read **by Git object** at
`e116e5ee` rather than from a working tree that moves under the test.

## 260918-TSIP-L1 Instrument-Discipline Helpers

This route gained **the fourth** verification-helper module, `instrument_discipline.py`, beside
`citations.py`, `structural_limits.py` and `scope.py` — **the route's fifth** is
`record_integrity.py`, recorded in the section above. It is a helper library, not a gate: it exposes
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
## The Two Registries A New Test Module's Path Literals Reach

`dependency_ownership.py` owns the source-derived test-consumer graph, and one fact about it is load-bearing
enough to state here rather than leave in a card: **a path *string* in a test is a dependency edge, and it is
derived twice for two different consumers.** The evidence **census** is served by
`mcp/tests/evidence-lifecycle.toml`'s `consumers` lists, while the **selection** graph for the ambient role
runner is served by `REPOSITORY_TEST_INPUT_CONSUMERS[AMBIENT_ROLE_RUNNER_PATH]`, and that constant
**overrides** the catalog for selection rather than restating it. Both derivations therefore have to be
satisfied — one does not stand in for the other. `260915-KS-L18` is a worked example: its two
citation-binding test modules each quote a real corpus key that the e2e generator's run report is written
about, which registered them in **both** registries without a single import creating the edge.

## Development And Certification Policy

Ordinary Python development is supported directly through `mcp/.venv/bin/python -m pytest`; four workers run the isolated unit population. `-m integration` selects the small real-boundary population and `-m ""` selects both. Focused file/node execution, including serial debugging, is valid development work and does not acquire certification authority. The repository declares budgets of 1,000 unit and 150 integration parametrized collected cases. Extend or consolidate distinct behavior protection before adding cases; do not restore deleted matrices, private-branch tests or unused fixture machinery because an old milestone names them.

Coverage, including changed-line coverage, is diagnostic only. No percentage floor requires additional tests. Production-only CRAP retains 20 as a review trigger, not a delivery blocker; tests and verification support are excluded. Lint, formatting, typing, structural rules and test failures still enforce. Diagnostic-tool execution errors remain visible failures distinct from metric findings. There is no coverage baseline, score-exception registry or ratchet.

Only genuine Dagger admission and the existing lifecycle owners can issue immutable candidate-bound certifying evidence. A host pytest pass, copied report, green helper result or use of Dagger alone is insufficient. Reuse the existing shared engine and preserve process identity, disposable state, credential isolation, exact candidate and publication ownership. Full-suite execution and whole-master independent review belong to the master aggregation boundary under the current execution policy; this overview does not impose either on every leaf. Focused development evidence remains useful without pretending to be final acceptance.
## Evidence

### Repo-Internal References

These current source and policy ranges establish the development/certification distinction and the existing memory preparation surfaces. A citation is source evidence, not a recorded test execution.

- Development commands, budgets, diagnostic metrics and isolation. [1]
- Certifying publication and accepting consumers. [2]
- Exact contract scope, the full check, and the curator worklist publication, which on a converted tree also carries the informational "without proof" list. [3]
- Interactive catalog names missing authority without eligibility. [4]
- Final memory adapter requires the selected four-code-terminal prefix. [5]
- Finalization consumes original selected fifth-certificate inputs. [6]

| Exact profile scope and suite execution. | `_require_exact_scope`; `_paths`; `_run_python_suite`; L92-L214 | [Profile rails](mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:92-214) |
| Plan composition and typed command steps. | `CheckConfig`; `Step`; `quality_steps`; L100-L168 | [Quality plan](mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:100-168) |
| Teardown proof from source applicability and exact result bytes. | `_verify_teardown`; `_verify_started_teardown`; `_write_teardown_proof`; L253-L359 | [Teardown owner](mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:253-359) |

### Docs And Cross-Repo References

No Domain Documentation entries are configured in the resolved memory root. Current local policy and source owners are cited above; no live external system or sibling repository is used to grant authority.

## Terminal-Pass Verification (`260915-KS-L23`, code `5e4eb651`)

This route's **own sources are byte-identical** between its previous verification commit `7b1db4e0` and the
terminal leaf's landing `5e4eb651` (`git diff 7b1db4e0..5e4eb651 -- mcp/test_support/agents_remember_test_support/code_quality/`
is empty), so every technical claim in the body above still holds unchanged. What the terminal pass **did** change is
this route's *consumers*, and three of those changes are things a reader of the quality machinery needs:

- **The two gates are two.** The byte-pin guard and the consumer-completeness oracle were named as one thing in
  places and are in fact separate derivations that must both be consulted; the terminal leaf's item 13 recorded them
  as two gates in the oracle's own module docstring (`testing/evidence_lifecycle.py:1-19`) and added a case that
  reddens the oracle while the pinned catalogue's bytes and populations stay provably untouched.
- **The collected-case budget is declared once, at the repository root.** The never-effective `default=1100` /
  `default=300` declarations in `mcp/tests/conftest.py` are removed (item 12); the enforced pair lives in the
  repository root `pyproject.toml` `[tool.pytest.ini_options]` at `:278-279` and is currently **4000 unit / 1000 integration**. A
  budget the parser declares and the repository does not enforce is worse than no declaration, because a reader
  believes it.
- **A registry row is a line, not an identity.** `mcp/tests/evidence-lifecycle.toml` gained appended `consumers` rows
  in this pass, and because a registry is a file of many blocks, appending to the end of **one block in the middle of
  the file** moves every line below it by one — which is why the citation ranges this card carries were re-projected
  in the same pass and why the class is recorded as D-36. The durable cure is a citation form that does not need a
  line range; until then the convention is to add at the end of the file.
