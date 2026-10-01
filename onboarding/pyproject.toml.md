# pyproject.toml

## Governing Overview

[overview.md](overview.md)

## Purpose

Shared source-checkout configuration for lint, typing, coverage measurement, package ownership, complexity reports and pytest collection.

## Code Commentary

### Logic

Ruff targets Python 3.13 and enforces C901 and the PLR complexity rules. E501 and PLR2004 are explicit readability exceptions. Test callable/import exceptions are scoped to test files. Registration-only PLR0913 permits the flat MCP schema signatures; the source comment names a historical guard test, which is not a claim that the removed test remains collected.

Pyright covers the checkout, with explicit import environments for source, verification support, tests and scripts. The selected interpreter is supplied by the quality owner. Coverage measurement includes branches and Python subprocesses for delivery reports; ordinary pytest is unmeasured. Product and verification package roots are classified separately, and the file-size detector remains armed.

Pytest defaults to four workers and excludes the integration marker. It collects the repository's class naming convention, excludes imported test classes, treats xfail success strictly, and requires registered markers/configuration. **Budgets are `unit_case_budget = 4000` (`pyproject.toml:278`) and `integration_case_budget = 1000` (`pyproject.toml:279`)** — collected cases, including parametrization, enforced on the selected population. **Both values moved for `260915-KS-L7`, and the move is a merged-line sizing defect rather than a defect of either side:** the merged base `4eb2b199` collected **1138 unit cases against a ceiling of 1100** *before any L7 line*, and because `pytest_collection_finish` raises `UsageError` on an over-budget population the whole unit run executed **zero** tests. The official line alone at its own tip `8dd62345` collected 1014/1100 and the KS parent `7db50f8f` collected 1003/1100 — **both green** — so the sizing question was ruled on by the master's owning seat and is not re-litigated here; the raise is **headroom, not a target**, and the four earlier dated tradeoff entries above the pair are intact. Each raise carries the doctrine-required dated block immediately above the key stating the distinct protection, the case count, the support size and the measured runtime cost. The single testpaths declaration is mcp/tests. Warning policy has three explicit third-party exceptions. Current marker declarations distinguish integration, evidence categories and the inherited fitness selector; the removed environment-gated runner and old vendor matrix are not current execution routes.

**`260915-KS-L24` then raised the pair again — `unit_case_budget` 1250 -> 1500 and `integration_case_budget` 340 -> 400 — by the master's owning seat, through the dated block at `pyproject.toml:286-303`.** It is the same class of event as the L7 raise above and is recorded the same way: measured at the `ar/260915-ks-l11` candidate *before* this raise, the unit population was **1250 collected against a ceiling of 1250** and integration 322 against 340, so L11 landed exactly **on** the unit ceiling and its worker consolidated the whole KS-R11 evidence into 17 cases rather than raise it. Over-budget collection is not a slow gate but no gate — `pytest_collection_finish` refuses the ENTIRE unit population (`unit suite has N cases; budget is 1250`) — so the increment's remaining requirement leaves could not have collected a unit case at all. The raise is **headroom sized for those leaves, not a target**: the dated block states the case-count delta (+250 unit, +60 integration, 0 consumed at the raise), the runtime cost it could state (the L11 unit population of 1250 cases inside a 490.73s combined run under the pinned `-n=4`), and that it licenses no weaker case. The `260915-KS-L24` candidate consumes 18 of the unit headroom (1268 collected) and 0 of the integration headroom (322 collected).

**`260915-KS-L21` then raised the unit ceiling one further step — `unit_case_budget` 2200 -> 2300 — through the dated block at `pyproject.toml:215-243`.** It is the same class of event as the two raises above and is recorded the same way, from a measurement rather than from a plan: the line's population before the leaf, measured the same way at the base it was cut from (`a7076008`), was **2158 collected**, so the 2200 ceiling carried 42 cases of headroom; the leaf's own delta is **48 unit cases in one new module** (`mcp/tests/test_migration_census.py`); and the candidate measured **2206 collected against 2200**, i.e. **six cases over**. An over-budget population is not a slow lane but no lane — `pytest_collection_finish` raises `UsageError`, so the whole unit run refuses rather than running 2200 of them — which is exactly why the overage is not left to the next leaf. The raise is to **2300**, admitting the measured 2206 plus 94 of headroom for the two requirement leaves of this increment that have not landed (L22, L23) at the ten-to-fifteen unit cases per leaf the landed leaves measured. **No case, module, registration or lane member was deleted, deselected, consolidated away or weakened to fit 2200, and no rail was lowered**: the 48 cases were added first and the ceiling was raised afterwards. **Integration is not raised** — measured **394 collected** against 400, unchanged by this leaf, which adds no integration case; the six cases of integration headroom are reported rather than consumed.

Radon configuration shapes diagnostic reports. Coverage has no acceptance percentage floor; production CRAP20 review and exact report integrity belong to the quality owner, not a numerical floor in this file.

### Conventions

Keep configuration ownership singular. Changes to budgets require the protection and cost tradeoff specified by repository policy: the block above the key states the distinct protection, the case count, the support size and the measured runtime cost. **Every number in such a block must carry the command that reproduces it** — L7's round 2 found three load-independent line counts and both module wall times stale there because they had been measured before the round's own last edit, so the entry now names, in the entry itself, the command for each class of number (sizes by `wc -l`, populations by `pytest --collect-only`, wall times by repeated serial runs) and states that a wall time is a **range over a named run list** rather than a single measurement. Do not restore retired source-text census tests or infer their continued protection from historical comments.

### Invariants And Boundaries

Package installation metadata belongs to mcp/pyproject.toml. Test failures and structural checks remain enforcing. Branch-report validation is report integrity, not mandatory branch coverage. Ordinary host test results do not acquire lifecycle certification authority.

### Todos

No new configuration or test obligation is introduced here.

## Evidence

### Docs References

No configured external domain documentation applies.

### Repo-Internal References

- Python lint policy and signature exception. [1]
- Type-checker scope and import environments. [2]
- Measurement and operational package ownership. [3]
- Radon reports. [4]
- The pytest configuration section the budget pair lives in. [5]
- **The declared budget pair as the file now declares it — `unit_case_budget` 4000 / `integration_case_budget` 1000, raised from 3000 / 600 by `260918-TSIP-L13`'s second developer-ruled raise on 2026-09-20; that earlier pair had itself been raised from 2300 / 400 by `260918-TSIP-L7` on 2026-09-19, and from 2200 / 400 before that by the truth-coverage census and staged-migration leaf over its own measured 2206-case candidate.** The earlier raises this row has carried are retained as the history they are: this candidate's own owning seat moved 1500 -> 1600, the merge onto the moved super line moved it to 2200 over a 2035-case population, and `260915-KS-L21` moved it to **2300** over a 2206-case population. [6]
- **The dated merge entry that carries both lines' raise history verbatim — this master's `unit 1100 -> 1250`, then `1250 -> 1500` and `integration 300 -> 340`, then `1500 -> 1600` — beside the rule that each axis starts from the higher of the two lines' values and is then measured.** [7]
- **The dated block `260915-KS-L21` added immediately above the pair — measured 2158 collected at the base `a7076008`, 48 unit cases added by this leaf, 2206 collected against 2200, and the raise to 2300 sized for L22/L23 rather than filled — together with the integration measurement (394 against 400, unchanged) that the same block reports.** [8]
- Warning exceptions and current evidence markers; the anchor is one of the three third-party exceptions the setting carries, because the setting name itself occurs three times in the file (twice inside the comments explaining it) and cannot anchor a unique claim. [9]
- Budgets, populations, collection and strictness, including the integration ceiling raise and its tradeoff block. [10]

### Cross-Repo References

No cross-repository implementation is claimed.
