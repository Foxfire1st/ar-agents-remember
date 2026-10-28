# Python Quality Verification Overview

| Field | Value |

| --- | --- |
| sourceRoute | `mcp/test_support/agents_remember_test_support/code_quality` |


## Governing Overview

[Python verification infrastructure](../overview.md)

## What This Area Is

Repository verification infrastructure for quality planning, exact test selection, Dagger-produced evidence, diagnostic scoring, causal failure reporting and retry reuse. Shipping it alongside source does not make it operational product behavior. Static checks include product and verification inputs; production coverage and CRAP measurement exclude tests and support.

## Hot Path Summary

`projection_types.py` renders the dashboard projection contract from the Python wire schemas. It folds the served projection's additional definitions into generated TypeScript and compares that supplemental definition set exactly with its declared renames. A new supplemental definition therefore requires updating that declaration and regenerating the output. Refinements TypeScript cannot enforce structurally, including numeric bounds, lengths and patterns, remain documented beside the affected property. Unsupported schema keywords or shapes refuse generation.

Its named vocabularies now concern attention severity, lane and item class, plus process fact state and process health.

> Retained earlier card wording; superseded by the current account above:
> Its named vocabularies now concern attention severity/lane and process fact/health only.
 Task stage/activity/eventAt, task counts and entry membership are rendered from the current Python schema like other model fields; the generator no longer reconstructs a session-state partition, lifecycle-count extension, lifecycle metrics factory or `SubTaskRow` union. Task presentation vocabulary remains a consumer concern, not a second lifecycle model synthesized by this generator.

`quality_plan.py` owns typed configuration and command planning; `check.py` executes and interprets the rails. `profile_selection.py` derives the selected population, and `profile_rails.py` rederives and validates exact scope before execution. `dependency_ownership.py` and `scope.py` establish supported consumers and explicit product/verification ownership. `catalog_selection.py` reads both catalog versions through the shared reader `parse_catalog`; invalid catalog input remains an explicit selection refusal. `retry_proof.py`, `retry_coverage.py` and the child-environment helper preserve admitted retry inputs and remove outer retry/progress controls from candidate-test environments.

## Construction And Ownership

The plan separates command construction from execution. Its steps distinguish enforcing subprocesses from report-only steps. Profile rails compare the published selector payload with a fresh repository-owned derivation and compare executable scope fields with canonical POSIX-string populations. A differently ordered `Path` list is not a new authority.

The source-derived consumer graph combines imports and qualifying literal references. A path string can therefore establish an edge without an import; the deciding predicates distinguish exact paths from basename and fixture references that need additional read evidence. The evidence catalog's consumer census and the ambient role runner's repository-declared selection consumers are separate authorities. `REPOSITORY_TEST_INPUT_CONSUMERS` overrides the catalog for selection where a repository declaration exists, and the selected declaration must match observed consumers. Neither authority substitutes for the other.

The lifecycle loader checks both canonical catalog form and agreement with the source-derived consumer graph. These are separate refusals: canonical catalog bytes do not establish consumer completeness.

`record_integrity.py` compares records that can drift apart: leaf-document status against enclosure closeout/integration cells; master-row status against the status derived from the leaf document; register arrows against declared leaf IDs; and declared prose figures against their source at the stated revision. Each result names its subject and authority populations alongside findings. Register comparison and figure comparison join the combined run only when their inputs are supplied. The helper exposes a CLI as well as callable comparisons; it is not a quality-plan gate.

For master rows, `derived_master_status` requires a `Completed` document and a nonempty set of steps all marked `done` before returning `Completed`; completing steps alone is insufficient. Contracts without matching leaf documents are counted rather than judged. The register's free-form prose census remains outside the stated comparison contract: its bucket rule is undeclared.

`instrument_discipline.py` makes measurement admissibility explicit. A count requires positive and negative witnesses and must use the positive pattern the probe proved. A captured window reports the boundary that closed it, including the line cap. Artifact checks refuse crash-adjacent pass claims, absent run evidence, nonzero exits without result evidence, and clean claims with no stated way to fail. Producer identity requires an existing script, command and revision. Reproduction compares bytes, uses a temporary scratch directory, and returns `matches=False` for a nonzero producer exit or a missing output artifact.

The record-integrity and instrument-discipline tests import these helpers and are listed in the `architecture-fitness` lane. Record-integrity source is 1,110 lines; its test source is 1,140 lines and contains 37 test-function definitions. These are source measurements, not executed or collected-case evidence. Historical record controls look for `AR_COORDINATION_ROOT`, otherwise try a repository-relative coordination root, and skip when required records are unavailable. Their historical prose inputs are pinned to Git revision `e116e5ee`.

## Invariants And Boundaries

Targeted scope is derived from source and declared consumers. Missing, ambiguous, stale or contradictory ownership remains explicit rather than silently widening admission to a full suite. Full population selection is explicit. Keep duplicate detection when comparing canonical populations; sorting must not erase contradictory declarations.

Coverage and CRAP reports describe selected production inputs. Metric findings are diagnostic; broken report tools remain failures. Retry reuse depends on admitted inputs, compatible selection, environment/tool identity and artifact digests. Fresh and retained coverage databases remain separate until a passing delta execution merges and publishes them. Missing expected artifacts cannot masquerade as known-empty proof. The merge owner removes the public artifact pair on a read, merge, analysis or publication failure.

Missing or inconsistent causal evidence fails preflight and runs the already selected pytest population without suppression. It does not license broader unowned selection. The standing distinction between a proved dependent node and an independent same-file node remains part of the causal-report contract; its detailed producer predicates were not independently verified in this bounded account.

Historical teardown proof used frozen source applicability and exact report bytes: a non-applicable scenario required no summary and recorded zero starts, while an applicable scenario required two fresh passing replications and matching candidate/selection identity and teardown checkpoints. That adapter was removed with the old orchestration in MIK L113 and is not a current rail. Physical producer bytes, export bindings and immutable report generations remain distinct from synthetic test payloads.

> Retained earlier card wording; superseded by the current account above:
> Teardown proof uses frozen source applicability and exact report bytes. A non-applicable scenario must have no summary, and its proof explicitly records zero starts and non-applicability. An applicable scenario requires two passing fresh replications, matching candidate/selection identity and passing teardown checkpoints. Physical producer bytes, export bindings and immutable report generations remain distinct from synthetic test payloads.


The final memory adapter requires exactly four selected code terminals before certification. It compares published result bytes with the producer bytes before selecting the terminal. Finalization requires five selected terminals and consumes the original fifth certificate's semantic inputs and references; it refuses absent certificate authority rather than inventing a replacement.

The memory-quality controller revalidates contract scope, executes the requested checks and attaches the curator checklist when publication is requested. `_bounded_quality_response` now retains complete computed finding populations in the whole result; `_answered_quality_response` adds status/reason fields from `quality_result_answer`, while the MCP payload builder uses that answer projection for delivery. These source changes establish no execution or acceptance. The checklist includes route-index, onboarding and knowledge-review inputs, plus the informational `without_proof` population. Its interactive final catalog names missing certification authorities without claiming eligibility.

Do not reconstruct the deleted host diagnostic analyzer/manifest machinery to permit ordinary pytest: the development loop already exists. Do not add percentage floors, a CRAP exception registry or source-pinning tests to satisfy historical claims. Do not silently grow case budgets or move unit bloat under integration markers. Profile planning, execution and certifying publication stay separate owners.

## Development And Certification Policy

Ordinary Python development is supported directly through `mcp/.venv/bin/python -m pytest`; four workers run by default. `-m integration` selects the small real-boundary population and `-m ""` selects both. Focused file/node execution, including serial debugging, is valid development work and does not acquire certification authority. These commands require a Git checkout because population enumeration uses tracked files.

The root configuration and current test-policy document both declare 10,000 unit and 2,000 integration parametrized collected cases. The unit ceiling has been raised three times since D226's 4,000 — to 5,000, to 6,000 by L54 and to 10,000 by L193's D460 — and the unit ceiling remains 10000 and D579 raises integration to 2000; guard behavior is unchanged. The earlier 1,000/150-versus-4,000/1,000 discrepancy remains a historical source-pair observation, not a present disagreement. Preserve the standing requirement to extend or consolidate distinct behavior protection before adding cases, and to justify budget growth explicitly. Do not restore deleted matrices, private-branch tests or unused fixture machinery because an old milestone names them.

Coverage, including changed-production coverage, is diagnostic only. No percentage floor requires additional tests. Production-only CRAP retains 20 as a review trigger, not a delivery blocker; tests and verification support are excluded. Lint, formatting, typing, structural rules and test failures still enforce. Diagnostic-tool execution errors remain visible failures distinct from metric findings. There is no coverage baseline, score-exception registry or ratchet.

Only genuine Dagger admission and the existing lifecycle owners can issue immutable candidate-bound certifying evidence. A host pytest pass, copied report, green helper result or use of Dagger alone is insufficient. Reuse the shared engine and preserve process identity, disposable state, credential isolation, exact candidate and publication ownership. Focused development evidence remains useful without implying final acceptance. The standing full-suite and whole-master independent-review boundary is retained, but its current execution-policy authority was not verified in this bounded account.

## Navigation And Historical Limits

Use the generated adjacent route index for existing source/sidecar membership after its owner refreshes it. This overview does not promise a card for a deleted source file or maintain a parallel static inventory.

Historical PDLS/CCR accounts explain exact-scope, retry and publication repairs; historical consumer counts and coverage enforcement are not current policy. The former fourth/fifth helper descriptions are historical additions, not a current module inventory. The instrument's recorded plural-`findings` regex fault, the register prose-census limitation and the terminal pass's citation-shift example remain historical cautions rather than claims that today's instruments are faultless.

The earlier account names citation-binding tests as a worked example of literal edges in both registries, asserts byte-identical route sources between `7b1db4e0` and `5e4eb651`, and describes appended registry rows shifting subsequent citation ranges. Those historical assertions were not re-established against their original Git objects here. The standing preference for citation identities that survive line movement remains; the historical end-of-file append convention does not override the current canonical catalog ordering requirement.

No lifecycle/status metadata in this overview grants execution or acceptance authority. No test execution or current task status is established by this source review; missing lifecycle authority remains an uncertainty.

**L184.** The projection-type checker knows the served provider limit, including its exact reset datetimes.























> Retained earlier citation wording: - Helper test imports, source figures, historical Git pin and conditional record availability.












## Evidence

- Helper test imports, source figures, historical Git pin and conditional record availability.

## Retirements

- Retired at the fifth freeze d59c3493: mcp/tests/test-evidence-lanes.toml:1-635 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a06d2ffcfae2c277f2ae19330c17d09c616b77e8. Retired means the anchor no longer stands, not that the cited subject was deleted.

- The current root policy is 10000 unit and 2000 integration selected cases. Collection rejects a lane above its declared ceiling; the raise changes headroom and preserves the guard. [12]

- The current root policy is 10000 unit and 2000 integration selected cases. Collection rejects a lane above its declared ceiling; the raise changes headroom and preserves the guard. [1]

- Certifying publication and accepting consumers. [2]

- Exact profile scope and suite execution. [13]

- Plan composition and typed command steps. [14]

- Both catalog versions use the shared parser; retain the original deciding range. [16]

- Catalog narrowing preserves removed consumers; parser errors remain named refusals. [17]

- Profile selection declares full mode explicitly and retains incomplete targeted inputs. [19]

- Repository declarations override catalog consumers and must match observed import/literal consumers. [20]

- Literal edges use deciding path/read predicates; standalone prose strings are excluded. [21]

- Canonical form and source-derived consumer completeness are separate catalog checks. [22]

- Record comparisons state both populations; completion requires document status and completed steps; optional comparisons require inputs. [23]

- Instrument admissibility and byte-exact producer reproduction. [24]

- Retry artifacts retain admitted identity, digest checks and passing-delta merge ownership. [26]

- Child environments remove outer invocation controls through the executing caller. [27]

- Missing causal authority fails preflight without suppressing the selected population. [28]

- The current root policy is 10000 unit and 2000 integration selected cases. Collection rejects a lane above its declared ceiling; the raise changes headroom and preserves the guard. [29]

- Projection generation validates schema vocabulary and exact supplemental definitions. [18]

- The retained named vocabularies are attention severity, lane and item class, plus process fact state and process health; the removed session state and phase vocabularies are not among them. [30]

- Ordinary schema interfaces are rendered without a lifecycle-count extension or injected metrics factory/legacy subtask union. [31]

- Exact contract scope, the full check and curator worklist publication, including the informational without-proof list.  Anchor: `_execute_memory_quality` `_answered_quality_response` `_attach_curator_checklist` [10]

- Interactive catalog names missing authority without eligibility. [11]

Retired at the fifth freeze d59c3493: mcp/tests/test-evidence-lanes.toml:1-635 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a06d2ffcfae2c277f2ae19330c17d09c616b77e8. Retired means the anchor no longer stands, not that the cited subject was deleted [25]
