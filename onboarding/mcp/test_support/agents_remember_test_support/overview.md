# Agents Remember Python Verification Infrastructure Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/test_support/agents_remember_test_support` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-18T18:58+02:00 |
| lastVerifiedCommitHash | `1bcf73e772b640fea56c2788fe9a52d98099bd41` |
| lastVerifiedCommitDate | 2026-09-20T05:00:13+02:00|
| governingOverview | `../../overview.md` |

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

## Repo-Internal References

These owners bind the package's executable rail scope to the repository selector.

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter rederives the selector and compares each executable path population exactly. | `_require_exact_scope` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:85-121 |
| Canonical POSIX-string sorting retains duplicate path entries. | `_paths` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:131-134 |

## Docs And Boundary References

Repository-owned design truth lives in `docs/design/python-evidence-system.md` and
`docs/design/python-test-evidence.md`. The PDLS task reports provide candidate-specific evidence;
they do not replace this source-paired behavior description.


## Integrated IAS Recovery Contract

Ordinary isolated host pytest is supported for development; only the certifying bootstrap and delivery wrapper require genuine Dagger admission. Production coverage is diagnostic and CRAP20 is a review trigger; lint, typing, structural rules, real test failures and malformed diagnostic artifacts remain enforcing. `catalog_selection.py` resolves changed manifest rows against actual retained consumers. The retired causal/retry route-evidence and route-measurement modules are absent; do not restore their duplicate measurement machinery or infer protection from removed tests.

**The case budgets this package's rails run under are not declared here.** Earlier revisions of this
overview and of the cards beneath it named a pair (1,000 unit / 150, later 250, integration) as a
current reading; the enforced pair is the repository root `pyproject.toml`'s
`[tool.pytest.ini_options]` pair — `unit_case_budget = 3000` and `integration_case_budget = 600` at
`pyproject.toml:263-264`, re-read 2026-09-20 on memory `4d0fc20a` / code `47570cd8` — and it moves. Read it there, and see
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

## Update History

- 2026-09-18T18:58+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **wrote the three owners this route had gained since its last review, and retired a stale rail claim rather than carrying it forward.** The route grew four files across four landings — `code_quality/completion_relay.py` (`d834ee95`, `LOCR-R14`), `testing/curation_doctrine.py` (`304de8e2`, corrected by `a29a20c6`), `code_quality/projection_types.py` (`e9678c56`, `LOCR-L17`) and two consumer rows in `code_quality/dependency_ownership.py` (`15fe8678`, `KS-R18`) — and the section above states what each owns, read from the modules rather than from their commit subjects. The `## Integrated IAS Recovery Contract` paragraph's **"Selected parametrized case budgets are 1,000 unit / 250 integration"** sentence was **not** a re-read: it was false, and this pass replaced it with the enforced pair (`unit_case_budget = 2300`, `integration_case_budget = 400`, root `pyproject.toml:244-245`, measured 2026-09-18 at code `c5a74a85`) plus the rule that the pair lives in the root file and moves. The 2026-09-14 entry below corrected `150` to `250` and left the sentence as a current claim; it is kept as the state it measured, and the sentence it corrected is no longer asserted here. Verification stamp advanced to `c5a74a85`, the revision read; closeout re-stamps.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the case-budget sentence
  still read 150 integration cases while `pyproject.toml:149-150` declares 250. Corrected it; the
  earlier entry had claimed this fix without it having landed. Verification metadata remains
  closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  `mcp/test_support/agents_remember_test_support/` route changed since the recorded verification
  commit. Re-read the card against the frozen on-disk source and re-checked its claims and cited
  ranges: nothing this card asserts is falsified by the change, so no wording changed. Verification
  metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the route moved since the
  recorded verification commit (the causal-preflight owner row and the dependency-ownership consumer
  catalog). Re-read the card: its own claims still hold, but its quoted case budgets were stale —
  corrected `1,000 unit / 150 integration` to the current `1,000 unit / 250 integration`
  (`pyproject.toml:149-150`). Verification metadata remains closeout-owned.
- 2026-09-09T02:35:47+02:00 — CCR-L38 inherited route reconciliation: re-read this route's purpose, member inventory, route summary, and invariants against frozen candidate code tree `4c6b7bc2362bc03d50fc7a0643f34b591b805d45`; the candidate's changed paths are outside source route `mcp/test_support/agents_remember_test_support`, so no route/member/prose/invariant change is required. route-member-count=50; source inspection only; verification metadata remains unchanged pending producer-owned realization. No acceptance or certification claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `_paths` repointed to mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:131-134. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.


- 2026-09-06T04:54:41+00:00 — L32 route-impact review against prepared commit `b34f4a59562b76a3e2413027468e0f699117b36f`: Documented canonical executable-scope ordering and retained exact missing, extra and duplicate population refusals after reading the adapter, selector and full-mode regression.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:23+00:00 — L30 route-impact review against `6e4ab81f6ae52bce35003377bb3aec7877554ed7`: Reviewed the two code-quality source changes and routed exact runner consumer ownership plus actual provider/teardown report production; package authority remains unchanged.

- 2026-09-05T07:08+00:00 — L31 cumulative source review at `ea35964985f30080488270e71ac81657ac40682b`: Reconciled explicit profile selector/rail owners and fail-closed incomplete selection, retaining non-accepting evidence boundaries. Verification records current source claims, not execution or acceptance.

- 2026-09-01T11:33+02:00 — No route impact: CCR-L11 Attempt 10 narrows ownership for one
  repository-level non-Python input inside `code_quality/`; this parent route remains verification
  infrastructure and acquires no product or acceptance authority. Verification remains
  closeout-owned.

- 2026-08-31T12:27+02:00 — No route impact: A005 retains this package as Dagger-owned
  verification support only; its child quality/testing refinements do not change the root
  product-versus-verification boundary. Verification remains closeout-owned.

- 2026-08-28T10:03:40+02:00 — Replaced the stale direct-diagnostics route summary with the current
  non-accepting Dagger evidence-route boundary after Candidate A retirement.

- 2026-08-28T06:40+02:00 — Reconciled Candidate A retirement, the complete 50-source/50-sidecar
  census, and the non-accepting cadence/retry/causal/measurement boundary.
- 2026-08-27T11:08+02:00 — Moved verification-only quality and pytest infrastructure out of the
  product package, established explicit package authority, and made this route the governing
  onboarding boundary. Verification provenance remains blank until closeout stamps the code
  candidate.
