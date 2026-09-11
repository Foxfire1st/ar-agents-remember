# pyproject.toml

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `pyproject.toml`                           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:48:32+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

Shared source-checkout configuration for lint, typing, coverage measurement, package ownership, complexity reports and pytest collection.

## Code Commentary

### Logic

Ruff targets Python 3.13 and enforces C901 and the PLR complexity rules. E501 and PLR2004 are explicit readability exceptions. Test callable/import exceptions are scoped to test files. Registration-only PLR0913 permits the flat MCP schema signatures; the source comment names a historical guard test, which is not a claim that the removed test remains collected.

Pyright covers the checkout, with explicit import environments for source, verification support, tests and scripts. The selected interpreter is supplied by the quality owner. Coverage measurement includes branches and Python subprocesses for delivery reports; ordinary pytest is unmeasured. Product and verification package roots are classified separately, and the file-size detector remains armed.

Pytest defaults to four workers and excludes the integration marker. It collects the repository's class naming convention, excludes imported test classes, treats xfail success strictly, and requires registered markers/configuration. Budgets are 1000 unit and 150 integration collected cases, including parametrization. The single testpaths declaration is mcp/tests. Warning policy has three explicit third-party exceptions. Current marker declarations distinguish integration, evidence categories and the inherited fitness selector; the removed environment-gated runner and old vendor matrix are not current execution routes.

Radon configuration shapes diagnostic reports. Coverage has no acceptance percentage floor; production CRAP20 review and exact report integrity belong to the quality owner, not a numerical floor in this file.

### Conventions

Keep configuration ownership singular. Changes to budgets require the protection and cost tradeoff specified by repository policy. Do not restore retired source-text census tests or infer their continued protection from historical comments.

### Invariants And Boundaries

Package installation metadata belongs to mcp/pyproject.toml. Test failures and structural checks remain enforcing. Branch-report validation is report integrity, not mandatory branch coverage. Ordinary host test results do not acquire lifecycle certification authority.

### Todos

No new configuration or test obligation is introduced here.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Python lint policy and signature exception. | "[tool.ruff]" | pyproject.toml:1-41 |
| Type-checker scope and import environments. | "[tool.pyright]" | pyproject.toml:43-66 |
| Measurement and operational package ownership. | "[tool.coverage.run]" | pyproject.toml:68-88 |
| Radon reports. | "[tool.radon]" | pyproject.toml:90-119 |
| Budgets, populations, collection and strictness. | "[tool.pytest.ini_options]" | pyproject.toml:121-150 |
| Warning exceptions and current evidence markers. | `filterwarnings` | pyproject.toml:165-198 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository implementation is claimed. | N/A | N/A |

## Update History

- 2026-09-06T21:48:32+00:00 — Reconciled current IAS testing and configuration policy against source; removed obsolete active coverage, host-refusal and deleted-test claims. Existing verification pins and all prior history remain unchanged.

- 2026-08-29T16:12+02:00 — Replaced the former multi-minor 3.11-floor contract with the single
  supported `py313` line and bounded package range. Historical 3.11 suppression cleanup remains
  history rather than current runtime authority. Verification remains closeout-owned.

- 2026-08-14T11:29+02:00 — R39 curator: reconciled marker documentation with credential semantics
  and Dagger-only execution. Verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T00:20+02:00 — Recorded root pytest `addopts` as the single owner of `-n=auto`, with
  `-n=0` reserved for explicit serial diagnosis. Verification metadata remains pinned until
  closeout.

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: split the runner command, exact-inventory,
  and ordinary-`fitness` claims into separately owned anchored rows; bound branch config, the reader's
  validator call, and the refusal body plus real package classifier values, narrowed the quality-test
  claim, and bound runner cardinality/equality to operative code and assertions.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: separated the full registered-marker set from
  the environment-gated runner subset. `fitness` remains an ordinary registered marker and is
  intentionally absent from gated commands. New ranges were provisional fixer input only.

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 12 citation findings; scoped check passed.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 final state. **Retired this card's claims that the
  four complexity codes are held by `quality/complexity-baseline.txt` and that `PLR0913` is
  deliberately off with a named owner.** The baseline is deleted and all four codes are
  enforced by `ruff` directly; `PLR0913` runs at the default of 5 args with 274 of 293
  findings refactored (163 parameter objects) and the remaining 19 covered by the single
  `mcp/src/agents_remember/mcp/registration/*.py` per-file-ignore, which an AST test holds
  shut. Also corrected the `[tool.coverage.run]` section — CRAP now *consumes* branch data
  and refuses a report without it, rather than "branch coverage is available but not
  consumed" — and corrected the `filterwarnings` cap from five entries including two of our
  own leaks to **exactly three third-party entries**, ours having been fixed at source.
  Recorded that the eight markers are now applied (they were registered but decorated
  nothing, so `-m` selected 0 of 3402). Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 gate honesty (mid-leaf): recorded `C901` selected,
  `target-version` reconciled to py311, Pyright `include` widened, the first
  `[tool.coverage.run]`, the Radon `tests/*` exclusion removal, and the first
  `[tool.pytest.ini_options]`.
- 2026-06-06T12:28+02:00: Re-verified against current HEAD after the Pyright configuration landed; the existing Ruff, Pyright, and Radon commentary still matches.
- 2026-05-28T19:52+02:00: Created after Pyright was added to source-checkout quality configuration.
