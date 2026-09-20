# pyproject.toml

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `pyproject.toml`                           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `3888cd8600e39a52c540d6038820759e3d4ffa7a`|
| lastVerifiedCommitDate |  2026-09-20T20:02:13+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview      | `overview.md`                              |

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
| The pytest configuration section the budget pair lives in. | "[tool.pytest.ini_options]" | pyproject.toml:121-121 |
| **The declared budget pair as the file now declares it — `unit_case_budget` 4000 / `integration_case_budget` 1000, raised from 3000 / 600 by `260918-TSIP-L13`'s second developer-ruled raise on 2026-09-20; that earlier pair had itself been raised from 2300 / 400 by `260918-TSIP-L7` on 2026-09-19, and from 2200 / 400 before that by the truth-coverage census and staged-migration leaf over its own measured 2206-case candidate.** The earlier raises this row has carried are retained as the history they are: this candidate's own owning seat moved 1500 -> 1600, the merge onto the moved super line moved it to 2200 over a 2035-case population, and `260915-KS-L21` moved it to **2300** over a 2206-case population. | "unit_case_budget = 4000"; "integration_case_budget = 1000" | pyproject.toml:278-278; pyproject.toml:279-279 |
| **The dated merge entry that carries both lines' raise history verbatim — this master's `unit 1100 -> 1250`, then `1250 -> 1500` and `integration 300 -> 340`, then `1500 -> 1600` — beside the rule that each axis starts from the higher of the two lines' values and is then measured.** | "unit 1100 -> 1250"; "both axes take the higher of the two lines' values" | pyproject.toml:188-202 |
| **The dated block `260915-KS-L21` added immediately above the pair — measured 2158 collected at the base `a7076008`, 48 unit cases added by this leaf, 2206 collected against 2200, and the raise to 2300 sized for L22/L23 rather than filled — together with the integration measurement (394 against 400, unchanged) that the same block reports.** | "2158 collected"; "2206 collected" | pyproject.toml:215-243 |
| Warning exceptions and current evidence markers; the anchor is one of the three third-party exceptions the setting carries, because the setting name itself occurs three times in the file (twice inside the comments explaining it) and cannot anchor a unique claim. | "ignore::starlette.exceptions.StarletteDeprecationWarning" | pyproject.toml:331-331 |
| Budgets, populations, collection and strictness, including the integration ceiling raise and its tradeoff block. | "[tool.pytest.ini_options]"; `integration_case_budget`; `unit_case_budget` | pyproject.toml:121-121; pyproject.toml:278-279; pyproject.toml:250-250; pyproject.toml:284-291 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository implementation is claimed. | N/A | N/A |

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: "ignore::starlette.exceptions.StarletteDeprecationWarning" repointed to pyproject.toml:331-331. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 2 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `pyproject.toml.md:65` (unit_case_budget, integration_case_budget) — re-read the claim against pyproject.toml, which now declares the pair 3000 / 600 at :263-264; wording corrected, anchor re-pointed at the literal the file declares; `pyproject.toml.md:69` (integration_case_budget, unit_case_budget) — re-read the claim against pyproject.toml, which now declares the pair 3000 / 600 at :263-264; wording corrected, anchor re-pointed at the literal the file declares.
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): **re-read the budget claims against `pyproject.toml` as it now stands and reconciled every current-value claim to what the file declares.** The truth-coverage census and staged-migration leaf raised `unit_case_budget` 2200 -> **2300** (key now at `:244`, integration unchanged at `:245`), so the `## Logic` sentence that named the pair now names 2300 at `:244` / 400 at `:245`, and a new paragraph records the raise the way the two earlier ones are recorded — measured rather than projected, with the 2158-case base population, the leaf's 48-case delta, the 2206-against-2200 overage, the size of the raise (94 of headroom for L22/L23), the fact that no case, module, registration or lane member was deleted or weakened to fit 2200, and the integration measurement (394 against 400, not raised). The pair row was re-worded and re-cited to the pinned literals the file now carries (`"unit_case_budget = 2300"` at `:244`, `"integration_case_budget = 400"` at `:245`); the earlier 1500 -> 1600 and -> 2200 raises are retained as the history they are. Two rows whose cited extents the leaf's own insertion had moved were re-cited rather than re-worded — the warning-exception row (`:222-261; :254-261` -> `:284-291`, the `filterwarnings` list the exception actually sits in) and the collection/strictness row (`:121-150; :149-150; :176-176; :168-168; :214-215` -> `:121-121; :244-245; :250-250; :284-291`, whose superseded extents no longer contained any of the row's anchors) — and one row was added for the dated block this leaf contributed. No claim was deleted or softened and no anchor set was dropped. The metadata block above now names this leaf's candidate as what was read and carries **no `lastVerifiedCommitHash`**: the body was re-read against a working candidate no commit contains, so no real commit holds the content a stamp would claim to have verified, and closeout owns the stamp. The body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-09-18T13:27+02:00 — 260915-KS-L13 curator (range-closure pass): **the two budget rows were re-read against the file as it now stands and re-worded to the facts it declares.** The merged declaration is `unit_case_budget = 2200` / `integration_case_budget = 400` (`:214-215`), so the row that anchored the *current* pair on `unit_case_budget = 1600` now names 2200 and keeps this candidate's own 1500 -> 1600 raise as the history it is. The dated-entry row named `2026-09-16 -- unit 1100 -> 1250 and integration 300 -> 340`, a comment line that no longer exists: the raise history it recorded now lives verbatim inside the 2026-09-18 merge entry (`:188-202`), which carries `unit 1100 -> 1250` and `(both axes take the higher of the two lines' values)`, so the claim was re-worded to that entry and re-cited to it rather than left pointing at a deleted comment. No claim was deleted or softened and no anchor set was dropped. No verification stamp advanced: the source is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T10:45:13+00:00: Hand retirement by the 260918-TSIP-L11 closing seat of the mechanical repair this timestamp recorded. What it wrote for "[tool.pytest.ini_options]" (pyproject.toml:121-121) was re-read against `pyproject.toml` on the merged tip — which now declares the pair 3000 / 600 at `:263-264` — and re-cited by hand; the machine marker is removed so the range is no longer read as an unverified projection. No claim wording was left unread and no verification stamp is advanced over prose that was not re-read.
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 1 claim(s) here (1 x citation_claim_reopened). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "ignore::starlette.exceptions.StarletteDeprecationWarning" repointed to pyproject.toml:369-369. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:52:52+00:00: Generated citation repair: "ignore::starlette.exceptions.StarletteDeprecationWarning" repointed to pyproject.toml:222-222. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T00:50:00+00:00 — 260915-KS-L24 curator (uncommitted change set on `ar/260915-ks-l24`, base `9c12e8b1`): **re-read this card against the current source and reconciled the budget pair this candidate moved.** The declared pair is `unit_case_budget = 1500` (`pyproject.toml:304`) and `integration_case_budget = 400` (`pyproject.toml:305`), raised by the master's owning seat through the dated block at `:286-303`; the body sentence and the pair row both still carried the L7 values and the `:286-287` / `:287` coordinates, and the `[tool.pytest.ini_options]` row stopped short of the pair it names, so its range now runs to `:305`. The pair row anchors the two pinned `key = value` lines rather than the bare identifiers because **`unit_case_budget` occurs four times in this file** (three of them inside the comments explaining the raises) and cannot anchor a unique claim — the same reason the warning-exception row below pins its literal. The row that names the raise the L7 leaf executed now says so explicitly, because the pair has moved a second time and "the raise" no longer reads unambiguously. This is the edit that retires the two mechanical generated bullets above (the `:333` -> `:351` projection for the warning exception, whose claim bytes this pass re-read and re-cited itself). Nothing above the pair was re-read; the L7, LOCR and earlier dated entries and the four tradeoff blocks are intact. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-17T20:42:17+00:00: Generated citation repair: "ignore::starlette.exceptions.StarletteDeprecationWarning" repointed to pyproject.toml:212-212. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T21:50:00+00:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): **recorded the merged-line budget raise and the rule the raise's own correction produced.** The pinned pair is now **`unit_case_budget = 1250`** and **`integration_case_budget = 340`**, raised by the master's owning seat through the dated entry at `:209-285` because the merged base carried **1138 unit cases against the ceiling of 1100** *before any L7 line* and an over-budget population makes `pytest_collection_finish` raise `UsageError`, so the whole unit run executed zero tests. The card states the attribution as measured so it is not misread as a regression: the official line alone collected 1014/1100 and the KS parent 1003/1100, both green, and this atomic master is the first line carrying both populations — **a merged-line sizing defect, not a defect of either side, and not re-litigated here**. It records that the raise is headroom rather than a target, that the four earlier dated entries are intact, and that L7's 21 unit and 25 integration cases took the populations to 1159 and 304. It also carries the **command-per-number rule** this leaf's round 2 forced, together with the two stale-figure patterns that produced it (line counts and module wall times published after the bytes moved), and corrects this card's stale "1000 unit / 250 integration" pair and its line citations. Verification metadata remains empty until closeout stamps the code commit.

- 2026-09-13T17:02:00+00:00 — 260831-LOCR-L37: recorded the developer-authorized
  `integration_case_budget` raise 200 -> 250 and the dated tradeoff block that now precedes the key
  (the distinct protection each added case buys, the case count, the support cost — the existing
  `QueueFixture` plus five measurement helpers inside one new module, no new support artifact — and
  the measured runtime). Corrected the stale "1000 unit and 150 integration" statement to the actual
  pinned pair, and re-derived the `filterwarnings` extent (189-222). Verification metadata remains
  closeout-owned; no acceptance claim.

- 2026-09-06T21:48:32+00:00 — Reconciled current IAS testing and configuration policy against source; removed obsolete active coverage, host-refusal and deleted-test claims. Existing verification pins and all prior history remain unchanged.

- 2026-08-29T14:12:00+00:00 — Replaced the former multi-minor 3.11-floor contract with the single
  supported `py313` line and bounded package range. Historical 3.11 suppression cleanup remains
  history rather than current runtime authority. Verification remains closeout-owned.

- 2026-08-14T09:29:00+00:00 — R39 curator: reconciled marker documentation with credential semantics
  and Dagger-only execution. Verification remains closeout-owned.

- 2026-08-12T13:19:00+00:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T22:20:00+00:00 — Recorded root pytest `addopts` as the single owner of `-n=auto`, with
  `-n=0` reserved for explicit serial diagnosis. Verification metadata remains pinned until
  closeout.

- 2026-08-04T09:43:39+00:00 — 260731-EFA-L6 S18-B03 curator: split the runner command, exact-inventory,
  and ordinary-`fitness` claims into separately owned anchored rows; bound branch config, the reader's
  validator call, and the refusal body plus real package classifier values, narrowed the quality-test
  claim, and bound runner cardinality/equality to operative code and assertions.

- 2026-08-03T21:26:43+00:00 — 260731-EFA-L6 S18-T3: separated the full registered-marker set from
  the environment-gated runner subset. `fitness` remains an ordinary registered marker and is
  intentionally absent from gated commands. New ranges were provisional fixer input only.

- 2026-08-02T18:53:56+00:00 — W2-B04 curator: repaired 12 citation findings; scoped check passed.

- 2026-07-31T14:10:00+00:00 — 260731-EFA-L2 final state. **Retired this card's claims that the
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

- 2026-07-31T04:30:00+00:00 — 260731-EFA-L2 gate honesty (mid-leaf): recorded `C901` selected,
  `target-version` reconciled to py311, Pyright `include` widened, the first
  `[tool.coverage.run]`, the Radon `tests/*` exclusion removal, and the first
  `[tool.pytest.ini_options]`.

- 2026-06-06T10:28:00+00:00: Re-verified against current HEAD after the Pyright configuration landed; the existing Ruff, Pyright, and Radon commentary still matches.

- 2026-05-28T17:52:00+00:00: Created after Pyright was added to source-checkout quality configuration.
