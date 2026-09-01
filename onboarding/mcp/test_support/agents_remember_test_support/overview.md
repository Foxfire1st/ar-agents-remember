# Agents Remember Python Verification Infrastructure Overview

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/test_support/agents_remember_test_support` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-01T11:33+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
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
  scoring, targeted selection, retry proof, and causal preflight.
- [testing/overview.md](testing/overview.md) governs admission, pytest composition, explicit lanes,
  lifecycle metadata, cadence, and non-accepting Dagger route evidence.
- `pytest_certifying_bootstrap.py` is the one certifying pytest plugin root; `__init__.py` exports no
  convenience facade.

## Operating Model

The root quality configuration explicitly classifies top-level Python packages as product or
verification. Ruff, Pyright, structural limits, and dependency checks remain broad. Coverage,
diff-coverage, and CRAP score only product authority. Dagger owns certifying execution and its
cache volumes. Candidate A's host route is retired. Cadence reports, retry matrices, causal
comparisons, and route measurements remain non-accepting evidence.

## Local Invariants And Traps

- Source placement does not decide product behavior by accident: package authority is explicit,
  exhaustive, non-overlapping, and stale rows fail.
- No product import may point into `agents_remember_test_support`.
- Unknown test lanes, consumers, plugin declarations, effects, or cache integrity fail loudly or
  select an explicitly reasoned fresh/full route; none silently becomes unit evidence.
- Verification code may consume product APIs; product code cannot consume verification policy.
- Host execution cannot mint Dagger admission or certifying evidence.

## File-Level Onboarding Map

Every current Python source below this route has one same-route sidecar. Generated route indexes
are refreshed after the move and include the complete source population.

## Docs And Boundary References

Repository-owned design truth lives in `docs/design/python-evidence-system.md` and
`docs/design/python-test-evidence.md`. The PDLS task reports provide candidate-specific evidence;
they do not replace this source-paired behavior description.

## Update History

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
