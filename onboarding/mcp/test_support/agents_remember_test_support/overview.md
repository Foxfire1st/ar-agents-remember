# Agents Remember Python Verification Infrastructure Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/test_support/agents_remember_test_support` |

## Governing Overview

[MCP overview](../../overview.md)

## What This Area Is

Development and repository-verification infrastructure for Python tests, quality producers, and non-accepting diagnostic evidence. The development extra supplies verification dependencies; ordinary repository pytest and the pinned Dagger graph load this package from the checkout. It is not operational Agents Remember product behavior. Product modules under `mcp/src/agents_remember` must not import this package.

## Hot Path Summary

- [code_quality/overview.md](code_quality/overview.md) governs static rails, product behavioral diagnostics, targeted selection and retry proof.
- [testing/overview.md](testing/overview.md) governs admission, pytest composition, explicit lanes, lifecycle metadata and non-accepting diagnostic evidence.
- `pytest_certifying_bootstrap.py` is the certifying pytest plugin root; `testing/certifying_bootstrap.py` requires admission before preparing certifying startup. `__init__.py` exports no convenience facade.

## Construction And Execution

The root quality configuration explicitly classifies top-level Python packages as product or verification. Ruff, Pyright, structural limits, and dependency checks remain broad. Coverage, diff-coverage, and CRAP measure product authority. Dagger owns certifying execution and its cache volumes. Ordinary isolated host pytest supports development without certification authority. The former Candidate-A command and measurement machinery remain retired.

The certification-profile path uses `code_quality/profile_selection.py` for content-addressed repository-owned selection and `code_quality/profile_rails.py` for executable Python rail adapters. An incomplete ownership result preserves unresolved inputs and blocks targeted test execution instead of silently broadening to the full Python suite. Exact-candidate retry reuse checks the selection digest. Runner-input and manifest ownership use retained consumer declarations rather than a fixed consumer count.

The Python rail adapter independently rederives the selector result and compares lint, type, coverage, test, and size paths with the executable scope. Both use canonical POSIX-string order, including siblings such as `conversation/` and `conversation-library/`; sorting retains duplicate entries rather than discarding them.

The Python suite adapter executes the pytest step constructed by the quality-plan owner. That step registers `testing.pytest_phase_reporter` when the explicit phase-report output path is supplied. For an applicable ambient scenario, the teardown adapter derives proof from the clean-room summary and both fresh replication reports with passing `L5-C10` checkpoints, bound to the frozen scenario selection. A declared not-applicable scenario instead requires the summary to be absent and publishes a zero-start proof. The focused code-quality overview owns the detailed adapter and selector contracts.

`code_quality/catalog_selection.py` narrows consumer-list-only catalog edits to the union of old and new affected consumers. Changes to broader catalog semantics retain global invalidation; malformed catalog text refuses. `code_quality/dependency_ownership.py` supplies repository-input consumer declarations and retains unresolved ownership explicitly.

`code_quality/completion_relay.py` guards the standing one-relay contract: `adapter evidence -> catalog -> notifier -> durable inbox -> owner`. The contract requires exactly two lifecycle-owned entry points into the shared terminal-observation body, one startup prime and one recurring steady-state caller, and forbids HTTP routes from advancing observation. The guard also preserves the existing notifier refresh authority rather than treating it as a third observation-entry owner. Its census records sweeper constructions, reads and mutations, observation-body calls, references to observation entry callables, route handlers, and harness-wire submissions. Reviewed sets and remediation text make additional authority visible to its direct assertion suite. This is a structural census with declared blind spots, not proof that every possible runtime indirection follows the relay.

`testing/curation_doctrine.py` owns normalized retired-wording checks and positive checks for compact curation policy. It strips Markdown emphasis and collapses wrapping before matching retired statements on the surfaces that shipped them. A separate registry checks the retired repair-loop field pairing and the corrected field names in declared documents. The module imports neither pytest nor a fixed repository root, so callers can supply staged or synthetic trees. Its retired-wording scan is a census, not a semantic check: fresh vocabulary can escape it. The compact-policy helper accepts any listed statement for each declared source; the direct canonical-source test requires every listed statement. Complete curation remains the stated intent, and those different deciding predicates must not be described as equivalent.

`code_quality/projection_types.py` carries the served observer-health schema into the generated dashboard contract. It renames `TerminalObserverHealthPayload` to `TerminalObserverHealth`, preserves its nullable properties as required `T | null` output fields, and documents numeric `maximum` as well as `minimum`. The serving serializer preserves payload nulls when observer health is present; the record schema bounds both serving-lifetime counters as unsigned 32-bit values.

Repository-owned design descriptions live in `docs/design/python-evidence-system.md` and `docs/design/python-test-evidence.md`. Candidate-specific task reports do not replace this source-paired behavior description. Historical commit and task identifiers are provenance, not current lifecycle or acceptance authority.

## Invariants And Boundaries

- Package authority is explicit, exhaustive and non-overlapping; missing or stale declarations refuse. Source placement alone does not confer product authority.
- Verification code may consume product APIs; product code must not consume verification policy or import `agents_remember_test_support`.
- Evidence lanes and ownership are explicit. Unknown or conflicting declarations refuse the affected operation rather than silently becoming unit evidence. Retry cache rejection may execute the admitted population fresh; declared full mode and proven global invalidators remain explicit selection decisions.
- Executable scope must match the independently rederived selector result and path populations before pytest runs.
- Host execution cannot mint Dagger admission or certifying evidence. Certifying startup requires admission, and the delivery boundary requires passed, immutable, candidate-bound Dagger publication.
- Production coverage is diagnostic and CRAP20 is a review trigger. Lint, typing, structural rules, real test failures and malformed diagnostic inputs remain enforcing.
- The retired causal/retry route-evidence and route-measurement machinery must not be restored as a duplicate measurement path, and removed tests must not be treated as current protection.

Case budgets belong to the root `pyproject.toml` rather than this overview or a test-local default. Its current declarations at `pyproject.toml:298-299` are `unit_case_budget = 5000` and `integration_case_budget = 1000`; D226 raises the unit ceiling from 4000 without changing integration or guard behavior. Readers must re-read that owner when the limits change.

## File-Level Onboarding Map

File-level onboarding is intended to cover every current Python source below this route with its same-route card and sidecar. The inspected tree does not yet meet that boundary: `code_quality/completion_relay.py` lacks both files, while `__init__.py`, `testing/causal_dependency.py` and `testing/candidate_snapshot.py` have Markdown cards but lack JSON sidecars. Generated route-index completeness is not established by this inventory.

## Evidence

- Canonical POSIX-string sorting retains duplicate path entries. [2]

- The enforced collected-case pair is 5000 unit/1000 integration; the unit-only policy raise leaves the guard unchanged. [3]

- The adapter rederives the selector and compares each executable path population exactly. [1]
- Development dependencies and checkout import paths are distinct from installed product-package discovery. [4]
- Certifying pytest startup requires admission before preparing candidate state and loading the certifying plugin. [5]
- The package initializer exports no facade; the certifying plugin composes shared services and worktree-service fixtures. [6]
- Root configuration classifies product and verification packages; full static scope covers tracked Python while behavioral metrics use product roots. [7]
- Targeted ownership remains typed-incomplete and refuses executable quality configuration when unresolved. [8]
- Exact-candidate cache reuse checks selection identity. [9]
- The adapter constructs an explicit phase-report path; the quality-plan owner registers its reporting plugin. [10]
- Applicable teardown validates two fresh checkpoint reports; not-applicable teardown records zero starts and requires no summary. [11]
- Consumer-only catalog changes preserve old and new consumers; repository inputs use explicit consumer declarations. [12]
- Retired-wording checks are normalized and surface-specific; compact-policy helper and canonical test use different predicates. [14]

- Current projection generator derives serialized TypeScript/schema contracts from Pydantic declarations, including the servingBuild-only served extension; removed observer-health payloads are not current required fields. [15]
- Evidence design separates development and diagnostic artifacts from immutable certifying publication and records Candidate A retirement. [16]
- Case budgets are root declarations rather than overview-owned constants. [17]
- Dagger owns the retained build and retry cache bindings. [18]
