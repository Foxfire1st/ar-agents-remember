# pyproject.toml

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `pyproject.toml`                           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `1ff1893f44d875073d58af863238501a6be35288`|
| lastVerifiedCommitDate | 2026-09-16T23:58:57+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

Shared source-checkout configuration for lint, typing, coverage measurement, package ownership, complexity reports and pytest collection.

## Code Commentary

### Logic

Ruff targets Python 3.13 and enforces C901 and the PLR complexity rules. E501 and PLR2004 are explicit readability exceptions. Test callable/import exceptions are scoped to test files. Registration-only PLR0913 permits the flat MCP schema signatures; the source comment names a historical guard test, which is not a claim that the removed test remains collected.

Pyright covers the checkout, with explicit import environments for source, verification support, tests and scripts. The selected interpreter is supplied by the quality owner. Coverage measurement includes branches and Python subprocesses for delivery reports; ordinary pytest is unmeasured. Product and verification package roots are classified separately, and the file-size detector remains armed.

Pytest defaults to four workers and excludes the integration marker. It collects the repository's class naming convention, excludes imported test classes, treats xfail success strictly, and requires registered markers/configuration. **Budgets are `unit_case_budget = 1250` (`pyproject.toml:286`) and `integration_case_budget = 340` (`pyproject.toml:287`)** — collected cases, including parametrization, enforced on the selected population. **Both values moved for `260915-KS-L7`, and the move is a merged-line sizing defect rather than a defect of either side:** the merged base `4eb2b199` collected **1138 unit cases against a ceiling of 1100** *before any L7 line*, and because `pytest_collection_finish` raises `UsageError` on an over-budget population the whole unit run executed **zero** tests. The official line alone at its own tip `8dd62345` collected 1014/1100 and the KS parent `7db50f8f` collected 1003/1100 — **both green** — so the sizing question was ruled on by the master's owning seat and is not re-litigated here; the raise is **headroom, not a target**, and the four earlier dated tradeoff entries above the pair are intact. Each raise carries the doctrine-required dated block immediately above the key stating the distinct protection, the case count, the support size and the measured runtime cost. The single testpaths declaration is mcp/tests. Warning policy has three explicit third-party exceptions. Current marker declarations distinguish integration, evidence categories and the inherited fitness selector; the removed environment-gated runner and old vendor matrix are not current execution routes.

Radon configuration shapes diagnostic reports. Coverage has no acceptance percentage floor; production CRAP20 review and exact report integrity belong to the quality owner, not a numerical floor in this file.

### Conventions

Keep configuration ownership singular. Changes to budgets require the protection and cost tradeoff specified by repository policy: the block above the key states the distinct protection, the case count, the support size and the measured runtime cost. **Every number in such a block must carry the command that reproduces it** — L7's round 2 found three load-independent line counts and both module wall times stale there because they had been measured before the round's own last edit, so the entry now names, in the entry itself, the command for each class of number (sizes by `wc -l`, populations by `pytest --collect-only`, wall times by repeated serial runs) and states that a wall time is a **range over a named run list** rather than a single measurement. Do not restore retired source-text census tests or infer their continued protection from historical comments.

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
| The pytest configuration section the budget pair lives in. | "[tool.pytest.ini_options]" | pyproject.toml:121-287 |
| **The declared budget pair, and the merged-line raise this leaf executed.** | `integration_case_budget`; `unit_case_budget` | pyproject.toml:286-287 |
| **The dated entry that carries the raise, its merged-line attribution and the command-per-number rule.** | "2026-09-16 -- unit 1100 -> 1250 and integration 300 -> 340" | pyproject.toml:209-285 |
| Warning exceptions and current evidence markers; the anchor is one of the three third-party exceptions the setting carries, because the setting name itself occurs three times in the file (twice inside the comments explaining it) and cannot anchor a unique claim. | "ignore::starlette.exceptions.StarletteDeprecationWarning" | pyproject.toml:189-201 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository implementation is claimed. | N/A | N/A |

## Update History

- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): **recorded the merged-line budget raise and the rule the raise's own correction produced.** The pinned pair is now **`unit_case_budget = 1250`** and **`integration_case_budget = 340`**, raised by the master's owning seat through the dated entry at `:209-285` because the merged base carried **1138 unit cases against the ceiling of 1100** *before any L7 line* and an over-budget population makes `pytest_collection_finish` raise `UsageError`, so the whole unit run executed zero tests. The card states the attribution as measured so it is not misread as a regression: the official line alone collected 1014/1100 and the KS parent 1003/1100, both green, and this atomic master is the first line carrying both populations — **a merged-line sizing defect, not a defect of either side, and not re-litigated here**. It records that the raise is headroom rather than a target, that the four earlier dated entries are intact, and that L7's 21 unit and 25 integration cases took the populations to 1159 and 304. It also carries the **command-per-number rule** this leaf's round 2 forced, together with the two stale-figure patterns that produced it (line counts and module wall times published after the bytes moved), and corrects this card's stale "1000 unit / 250 integration" pair and its line citations. Verification metadata remains empty until closeout stamps the code commit.

- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: recorded the developer-authorized
  `integration_case_budget` raise 200 -> 250 and the dated tradeoff block that now precedes the key
  (the distinct protection each added case buys, the case count, the support cost — the existing
  `QueueFixture` plus five measurement helpers inside one new module, no new support artifact — and
  the measured runtime). Corrected the stale "1000 unit and 150 integration" statement to the actual
  pinned pair, and re-derived the `filterwarnings` extent (189-222). Verification metadata remains
  closeout-owned; no acceptance claim.
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
