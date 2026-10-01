# Agents Remember Python Verification Infrastructure Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/test_support/agents_remember_test_support` |

## Governing Overview

[MCP overview](../../overview.md)

## What This Area Is

Development and repository-verification infrastructure for Python tests, quality producers, and
non-accepting diagnostic evidence. It is installed by the development extra and executed by the
pinned Dagger graph, but it is not operational Agents Remember product behavior. Product modules
under `mcp/src/agents_remember` must not import this package.

## Hot Path Summary

- [code_quality/overview.md](code_quality/overview.md) governs static rails, product behavioral
  diagnostics, targeted selection and retry proof.
- [testing/overview.md](testing/overview.md) governs admission, pytest composition, explicit lanes,
  lifecycle metadata and non-accepting diagnostic evidence.
- `pytest_certifying_bootstrap.py` is the one certifying pytest plugin root; `__init__.py` exports no
  convenience facade.

The CCR profile path adds `code_quality/profile_selection.py` for immutable repository-owned
selection and `code_quality/profile_rails.py` for the actual Python rail adapters. An
incomplete ownership result preserves unresolved inputs and blocks targeted test execution;
it no longer silently broadens to the full Python suite. Retry compatibility now binds the
exact selection digest. Runner-input and manifest ownership use the retained consumer catalog rather than an obsolete fixed consumer count. `profile_rails.py` writes a teardown proof derived from the existing clean-room summary and both real `L5-C10` checkpoint reports. The profile-declared provider rail directly invokes pytest with the existing `testing.pytest_phase_reporter` plugin and its explicit phase-report output path. The focused code-quality overview owns those detailed adapter and selector contracts; the package remains verification infrastructure rather than product authority.

The Python rail adapter compares executable scope with the exact selector outputs in canonical
POSIX-string order. This keeps full-mode populations equal when component-wise `Path` ordering
differs, such as `conversation/` beside `conversation-library/`. The comparison covers lint,
type, coverage, test, and size paths; sorting retains duplicate entries for validation.

## Operating Model

The root quality configuration explicitly classifies top-level Python packages as product or
verification. Ruff, Pyright, structural limits, and dependency checks remain broad. Coverage,
diff-coverage, and CRAP score only product authority. Dagger owns certifying execution and its
cache volumes. Ordinary isolated host pytest supports development without certification authority.
The former Candidate-A command and measurement machinery remain retired.

## Local Invariants And Traps

- Source placement does not decide product behavior by accident: package authority is explicit,
  exhaustive, non-overlapping, and stale rows fail.
- No product import may point into `agents_remember_test_support`.
- Unknown test lanes, consumers, plugin declarations, effects, or cache integrity fail loudly or
  refuse the affected selector/rail; retry cache rejection may run the already admitted
  population fresh, while declared full mode or proven global invalidators remain explicit.
  None silently becomes unit evidence.
- Executable scope must match the independently rederived selector population. Missing, extra,
  or duplicate paths refuse before pytest.
- Verification code may consume product APIs; product code cannot consume verification policy.
- Host execution cannot mint Dagger admission or certifying evidence.

## File-Level Onboarding Map

Every current Python source below this route has one same-route sidecar. Generated route indexes
are refreshed after the move and include the complete source population.

## Evidence

### Repo-Internal References

These owners bind the package's executable rail scope to the repository selector.

- The adapter rederives the selector and compares each executable path population exactly. [1]
- Canonical POSIX-string sorting retains duplicate path entries. [2]

### Docs And Boundary References

Repository-owned design truth lives in `docs/design/python-evidence-system.md` and
`docs/design/python-test-evidence.md`. The PDLS task reports provide candidate-specific evidence;
they do not replace this source-paired behavior description.


## Integrated IAS Recovery Contract

Ordinary isolated host pytest is supported for development; only the certifying bootstrap and delivery wrapper require genuine Dagger admission. Production coverage is diagnostic and CRAP20 is a review trigger; lint, typing, structural rules, real test failures and malformed diagnostic artifacts remain enforcing. `catalog_selection.py` resolves changed manifest rows against actual retained consumers. The retired causal/retry route-evidence and route-measurement modules are absent; do not restore their duplicate measurement machinery or infer protection from removed tests.

**The case budgets this package's rails run under are not declared here.** Earlier revisions of this
overview and of the cards beneath it named a pair (1,000 unit / 150, later 250, integration) as a
current reading; the enforced pair is the repository root `pyproject.toml`'s
`[tool.pytest.ini_options]` pair — `unit_case_budget = 4000` and `integration_case_budget = 1000` at
`pyproject.toml:278-279`, re-read 2026-09-20 by `260918-TSIP-L13` on memory `682bbdfd` / code `1bcf73e7` — and it moves. Read it there, and see
`system/tools.md` for why the pair is the root file's rather than any test-local default.

## Three Owners That Landed After This Route's Last Review

`code_quality/completion_relay.py` (`d834ee95`, `LOCR-R14`) is the executable form of the one-relay
rule. The completion relay is `adapter evidence -> catalog -> notifier -> durable inbox -> owner`, and
`LOCR-R14@v1` requires it to be the **only** progression path: the terminal-liveness sweeper is driven
by exactly two lifecycle-owned entry points (one startup prime, one recurring steady-state caller), no
HTTP route may advance observation, and an owner is reached through a durable inbox row rather than by
a second completion protocol. The module measures six independent facts over `mcp/src/agents_remember`
— sweeper constructions, sweeper reads, sweeper mutation sites, observation-body references, the
observation owner, and the entry points that start observation — and names the reviewed set and the
remedy for each, so "a second observation authority now exists" is a check result rather than a review
opinion.

`testing/curation_doctrine.py` (`304de8e2`, corrected by `a29a20c6`) owns the reading half of the
retired optional-curation doctrine: a registry of the retired sentences with the surface each lived on,
the exact statement every canonical source that must state the rule states it in, and the readers a
test calls. Matching is normalized — markdown emphasis stripped, line wrapping collapsed — and against
the whole retired sentence, so a statement re-inserted with different emphasis is still the same
statement, while doctrine that legitimately survives (an explicit developer request still governs full
code quality and full tests) cannot read as a regression. It is deliberately free of pytest and of any
repository constant so a case can point it at a staged or synthetic tree. It is a census, not a
semantic check: a corpus that denied the rule in fresh vocabulary this registry has never seen would
pass.

`code_quality/projection_types.py` (`e9678c56`, `LOCR-L17`) follows the served observer-health reading
into the generated dashboard contract: the `TerminalObserverHealthPayload -> TerminalObserverHealth`
rename, that payload added to the null-preserving set (it deliberately dumps nulls, so its nullable
properties stay required `T | null` on the output contract), and `maximum` admitted to the
schema-refinement keywords — the served row declares both serving-lifetime counts as unsigned 32-bit
values, and a mirror documenting only `minimum` would understate the field it mirrors.
`code_quality/dependency_ownership.py` (`15fe8678`, `KS-R18`) adds
`test_knowledge_citation_bindings.py` and `test_knowledge_citation_boundaries.py` to
`REPOSITORY_TEST_INPUT_CONSUMERS`.
