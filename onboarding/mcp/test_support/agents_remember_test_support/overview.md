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

The Python suite adapter executes the pytest step constructed by the quality-plan owner. That step registers `testing.pytest_phase_reporter` when the explicit phase-report output path is supplied. The earlier ambient teardown adapter and its two-replication `L5-C10`/zero-start proof protocol were removed with the old orchestration in MIK L113; they are historical evidence rules, not current rails. The focused code-quality overview owns the detailed adapter and selector contracts.

> Retained earlier card wording; superseded by the current account above:
> The Python suite adapter executes the pytest step constructed by the quality-plan owner. That step registers `testing.pytest_phase_reporter` when the explicit phase-report output path is supplied. For an applicable ambient scenario, the teardown adapter derives proof from the clean-room summary and both fresh replication reports with passing `L5-C10` checkpoints, bound to the frozen scenario selection. A declared not-applicable scenario instead requires the summary to be absent and publishes a zero-start proof. The focused code-quality overview owns the detailed adapter and selector contracts.


`code_quality/catalog_selection.py` narrows consumer-list-only catalog edits to the union of old and new affected consumers. Changes to broader catalog semantics retain global invalidation; malformed catalog text refuses. `code_quality/dependency_ownership.py` supplies repository-input consumer declarations and retains unresolved ownership explicitly.

The earlier `code_quality/completion_relay.py` account described a structural census for the relay `adapter evidence -> catalog -> notifier -> durable inbox -> owner`, with startup and recurring observation entry points. That module is absent from the frozen source tree, so this account is historical and supplies no current relay guard, HTTP exclusion check or runtime-indirection guarantee.

`testing/curation_doctrine.py` owns normalized retired-wording checks and positive checks for compact curation policy. It strips Markdown emphasis and collapses wrapping before matching retired statements on the surfaces that shipped them. A separate registry checks the retired repair-loop field pairing and the corrected field names in declared documents. The module imports neither pytest nor a fixed repository root, so callers can supply staged or synthetic trees. Its retired-wording scan is a census, not a semantic check: fresh vocabulary can escape it. The compact-policy helper accepts any listed statement for each declared source; the direct canonical-source test requires every listed statement. Complete curation remains the stated intent, and those different deciding predicates must not be described as equivalent.

`code_quality/projection_types.py` folds the served projection's `servingBuild`, `watcherHealth` and `checkoutBinding` definitions into the generated dashboard contract. Its supplemental renames are `ServingBuildPayload`, `WatcherHealthPayload` and `CheckoutBindingPayload`; nullable fields omitted by `exclude_none=True` become optional output properties. The declared refinement keywords include `minimum` but not `maximum`, and unsupported schema keywords refuse generation. The former terminal observer-health payload and counter account is historical; it does not describe this candidate's served tail.

> Retained earlier card wording; superseded by the current account above:
> `code_quality/projection_types.py` carries the served observer-health schema into the generated dashboard contract. It renames `TerminalObserverHealthPayload` to `TerminalObserverHealth`, preserves its nullable properties as required `T | null` output fields, and documents numeric `maximum` as well as `minimum`. The serving serializer preserves payload nulls when observer health is present; the record schema bounds both serving-lifetime counters as unsigned 32-bit values.


Repository-owned design descriptions live in `docs/design/python-evidence-system.md` and `docs/design/python-test-evidence.md`. Candidate-specific task reports do not replace this source-paired behavior description. Historical commit and task identifiers are provenance, not current lifecycle or acceptance authority.

## Invariants And Boundaries

- Package authority is explicit, exhaustive and non-overlapping; missing or stale declarations refuse. Source placement alone does not confer product authority.
- Verification code may consume product APIs; product code must not consume verification policy or import `agents_remember_test_support`.
- Evidence lanes and ownership are explicit. Unknown or conflicting declarations refuse the affected operation rather than silently becoming unit evidence. Retry cache rejection may execute the admitted population fresh; declared full mode and proven global invalidators remain explicit selection decisions.
- Executable scope must match the independently rederived selector result and path populations before pytest runs.
- Host execution cannot mint Dagger admission or certifying evidence. Certifying startup requires admission, and the delivery boundary requires passed, immutable, candidate-bound Dagger publication.
- Production coverage is diagnostic and CRAP20 is a review trigger. Lint, typing, structural rules, real test failures and malformed diagnostic inputs remain enforcing.
- The retired causal/retry route-evidence and route-measurement machinery must not be restored as a duplicate measurement path, and removed tests must not be treated as current protection.

Case budgets belong to the root `pyproject.toml` rather than this overview or a test-local default. Its current declarations at `pyproject.toml:333-334` are `unit_case_budget = 10000` and `integration_case_budget = 2000`; the unit ceiling has been raised three times since D226's 4000 — to 5000, to 6000 by L54 and to 10000 by L193's D460 — and the unit ceiling remains 10000 and D579 raises integration to 2000; guard behavior is unchanged. Readers must re-read that owner when the limits change.

## File-Level Onboarding Map

File-level onboarding is intended to cover every current Python source below this route with its same-route card and sidecar. The inspected memory tree still has Markdown cards but no JSON sidecars for `__init__.py`, `testing/causal_dependency.py` and `testing/candidate_snapshot.py`. `code_quality/completion_relay.py` is absent from source and is not a missing-current-source-card case. Generated route-index completeness is not established by this inventory.





















### Integration headroom

On 2026-10-26, the integration ceiling rises from 1000 to 2000; unit remains 10000. The source-file cases protect Git listing, bounded reads and readable excluded citations. The original 16-case shape measured 18.56 s and independently 20.15 s; grouping preserved its scenarios in four cases and 14 subtests at 19.70 s. The two link-class regressions produce four cases and 16 subtests: v2 measured 27.47 s and v3 38.20 s. No case was weakened or moved to the unit lane. Both over-budget refusal directions remain enforced. These are scenario-run measurements, not whole-suite runtime or a claimed speedup.

## Evidence
- Canonical POSIX-string sorting retains duplicate path entries. [2]
- The root declares 10000 unit and 2000 integration selected cases. The current integration raise preserves marker classification and both over-budget refusal directions. [3]
- The adapter rederives the selector and compares each executable path population exactly. [1]
- Development dependencies and checkout import paths are distinct from installed product-package discovery. [4]
> Retained earlier citation wording: - Certifying pytest startup requires admission before preparing candidate state and loading the certifying plugin. [5]
- The package initializer exports no facade; the certifying plugin composes shared services and worktree-service fixtures. [6]
- Root configuration classifies product and verification packages; full static scope covers tracked Python while behavioral metrics use product roots. [7]
- Targeted ownership remains typed-incomplete and refuses executable quality configuration when unresolved. [8]
- Exact-candidate cache reuse checks selection identity. [9]
- The adapter constructs an explicit phase-report path; the quality-plan owner registers its reporting plugin. [10]
- Consumer-only catalog changes preserve old and new consumers; repository inputs use explicit consumer declarations. [12]
- Retired-wording checks are normalized and surface-specific; compact-policy helper and canonical test use different predicates. [14]
- The current projection generator derives the serialized TypeScript and schema contracts from the Pydantic declarations, folding the served tail fields (`servingBuild`, `watcherHealth`, `checkoutBinding`) that `ServedWorkspaceProjection` declares into the same generated output. [15]
- Evidence design separates development and diagnostic artifacts from immutable certifying publication and records Candidate A retirement. [16]
- Case budgets are root declarations rather than overview-owned constants. [17]
- Dagger owns the retained build and retry cache bindings. [18]
- Certifying pytest startup requires admission before preparing candidate state and loading the certifying plugin. [5]
- The dated raise states the headroom, measured scenario costs and preserved refusal directions. [19]
