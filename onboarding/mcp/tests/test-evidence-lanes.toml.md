# mcp/tests/test-evidence-lanes.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| lastUpdated | 2026-09-19T19:52+02:00 |
| lastVerifiedCommitHash | `eca18fe69b7a8aa4d64911497a210aa256f60222` |
| lastVerifiedCommitDate | 2026-09-19T23:28:48+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l5-ar` uncommitted source (1 modified path; `test-evidence-lanes.toml` 269 → **270** lines, one row added at `:153`); base `f05ba167cd6dfb56b48a775f3da5d45528c09c82` |
| reviewedWorkingCandidate | `ar/260918-tsip-l4-ar` uncommitted source; base `0dd04d6adbca3e8ba61849b605ece3137005829e` |
| reviewedWorkingCandidate | `ar/260918-tsip-l2-ar` uncommitted source (1 modified path; `test-evidence-lanes.toml` 266 → **267** lines, one row added at `:246`); base `d9becade1a373f2272501f7451746ccc259ca9ac` |
| reviewedWorkingCandidate | `ar/260918-tsip-l1-ar` uncommitted source (1 modified path); base `f031314345b674d0733c4619fe34d78c1b02ba26` |
| reviewedWorkingCandidate | `ar/260915-caps-l15-ar` uncommitted source (17 dirty paths); base `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
| reviewedWorkingCandidate | `ar/260915-caps-l11-ar` uncommitted source; base `a29a20c6eefea424a7e0321a54fcda2ed1b35098` |
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted change set; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| path | `mcp/tests/test-evidence-lanes.toml` |
| doc_type | `file-level-onboarding` |
| governingOverview | `overview.md` |

## 260918-TSIP-L2 Row — The Record-Integrity Module

This leaf adds **one row** to the same `architecture-fitness` lane, at `:246`, as that array's last
entry — between `mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py` (`:245`) and the lane's
closing bracket (`:247`):

```toml
  "mcp/tests/test_record_integrity.py",
```

`architecture-fitness` is the behaviour-preserving lane for it because the module imports the
verification package (`agents_remember_test_support.code_quality.record_integrity`) and executes
nothing over a real boundary: no process, no Node, no temporary repository. The manifest now carries
**249 module rows**, and the file is **267 lines** at that candidate — **both superseded by
`260918-TSIP-L4`, which added two further rows and re-read the shipped loader at 251 rows / 251
modules over a 269-line file** (`:165` the chain-order module in `integration`, `:244` the
response-conformance module in `architecture-fitness`) — **and superseded again by
`260918-TSIP-L5`, which added one further row at `:153` and re-read the file at 252 rows / 252
modules over 270 lines** (see its own section below).

**The insertion moved every manifest entry below it, and no other position was available.** An
`architecture-fitness` entry must sit between its own header (`:227`) and the next lane header
(`provider-conformance`, `:248`), and the array read **18** entries at `228-245` before this leaf, so
`:246` — the array's last row — is the minimum-displacement position. The one-line shift invalidated
three citations, and the shift is therefore a memory repair rather than an edit that could be
avoided:

| Affected citation | Before | After | Disposition |
| --- | --- | --- | --- |
| this card's row **"Empty former stress/migration populations"** | `:262-265` | **`:263-266`** | **BROKEN**: `migration = [` moved `265` → `266` and fell out of the range; repaired |
| this card's row **"The manifest still has no default classification for an unregistered test file"** | `:4-265` | **`:4-266`** | stale end — its anchor still resolved, so **no check reported it**; repaired by reading the file |
| `onboarding/mcp/tests/test_codex_capsule_delivery.py.md`, its `provider-conformance` lane-row citation | `:254-254` | **`:255-255`** | **BROKEN**: that row's own path moved `:254` → `:255`; repaired |
| this card's row **"Provider contract classifications"** | `:242-256` | unchanged | **INTACT**: the range still covers `provider-conformance` at `:248` |

**Not every range that moved broke**, which is why those dispositions are a list rather than a rule:
a range still containing its anchor is not a finding, and only the product's own `range_resolution`
check separates the two. It reported exactly **two** of them at this candidate — this card's
`:262-265` and the `test_codex_capsule_delivery.py.md` row. The stale `:4-265` end was found by
reading the file instead, which is `T45`'s class exactly: a range that no longer reaches the line it
described renders like a correct one.

**And the loader is not silent at this candidate — a correction to the section below.** The row above
registers this leaf's module as the fail-closed loader requires, and the manifest is still **one row
short of the modules it must classify**: `load_lane_manifest(<repository root>)` on this candidate
refuses with

```
test evidence lanes have 1 finding(s):
  - test files without an explicit lane: ['mcp/tests/test_atomic_series_chain_pair_order.py']
```

That module was added by `260915-CAPS-L25` at `f0313143` and was never registered; the gap is **one
row at every commit since**, measured `247 entries / 248 modules on disk` at `f0313143`, `248 / 249`
at `d9becade`, and `249 / 250` here. So this is not this leaf's doing and not this leaf's to repair —
registering that module is a change to this file and belongs to the lane registry's owner — but two
claims in the section below are wrong because of it and are corrected here rather than repeated:
`pytest tests/test_evidence_lanes.py tests/test_suite_budget.py -q` does **not** exercise
`load_lane_manifest` (its one registry case validates the lane *categories*), so its green says
nothing about the loader; and the loader was already refusing at the previous leaf's candidate, not
silent.

After this insertion the lane populations are: unit-regression **150** (`6-155`), public-contract
**2** (`158-159`), integration **64** (`162-225`), architecture-fitness **19** (`228-246`),
provider-conformance **14** (`249-262`), with `stress-durability` (`:264`) and `migration` (`:266`)
still empty — every lane above the insertion is unchanged.

## 260918-TSIP-L1 Row — The Instrument-Discipline Module

This leaf adds **one row** to the existing `architecture-fitness` lane, at `:232`, between
`mcp/tests/test_file_size_detector.py` (`:231`) and `mcp/tests/test_layering.py` (`:233`):

```toml
  "mcp/tests/test_instrument_discipline.py",
```

`architecture-fitness` is the behaviour-preserving lane for it because the module imports the
verification package (`agents_remember_test_support.code_quality.instrument_discipline`) and executes
nothing over a real boundary: no process, no Node, no temporary repository. `unit-regression` and
`integration` would both misdescribe it. **Corrected by the `260918-TSIP-L2` curator, and wrong when
written:** the claim that the fail-closed loader is silent at this candidate rested on
`pytest tests/test_evidence_lanes.py tests/test_suite_budget.py -q` → **4 passed in 0.54 s**, a run
that never calls `load_lane_manifest` (its one registry case validates the lane *categories*). Called
directly, the loader already refused at this candidate — `test files without an explicit lane:
['mcp/tests/test_atomic_series_chain_pair_order.py']`, an unregistered module from `260915-CAPS-L25`
that no seat on this master has registered. The module does collect into the lane, which is what the
row above establishes; the loader's silence was never measured. See the section above.

**The insertion is a one-line change that moved the 27 manifest entries below it, and that is the
fact to carry forward.** Every entry at or below `:232` gained one line; the entries above it did
not. Measured against the base commit, the two rows whose citations this invalidated are:

| Module | Before | After |
| --- | ---: | ---: |
| `mcp/tests/test_pause_is_not_publication.py` | 235 | **236** |
| `mcp/tests/test_codex_capsule_delivery.py` | 253 | **254** |

The pause suite's own row, `mcp/tests/test_pause_stop_only_end_to_end.py` at `:199`, is **above** the
insertion point and did not move — which is worth stating because the L37 lane-registration row in
`mcp/tests/overview.md` pairs that unmoved `:199` with the moved `:236`, and a reader who assumed
both had shifted would mis-cite one of them.

Four memory documents cited the pre-insertion numbers for those rows, and all four were repaired in
the same pass. Three were pure moves and the shipped citation fixer projected them mechanically
(`ccr-r10@v1`): this card's own `:235` → `:236` at line 762, `test_pause_is_not_publication.py.md`'s
`:235` → `:236`, and `test_codex_capsule_delivery.py.md`'s `:253` → `:254`. The fourth — the L37
lane-registration row in `mcp/tests/overview.md` — was **declined** by the fixer
(`projection_no_resolved_extent`: one anchor resolved to four extents) and was corrected by hand to
cite the two ranges that actually hold its two named anchors. This is the same hazard the L11 curator
recorded on this card after the six `D9` rows were added: **a row insertion renumbers every row below
it, and a cited line number is only true against one revision of this file.**

**Population.** No row was removed and no lane key moved; the module count rose by exactly one. This
card's earlier population paragraphs remain the as-of records of the leaves that wrote them and are
not restated here as current.

## 260918-TSIP-L2 Row — The Record-Integrity Module

This leaf adds **one row** to the same `architecture-fitness` lane, at `:246`, as that array's last
entry — between `mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py` (`:245`) and the lane's
closing bracket (`:247`):

```toml
  "mcp/tests/test_record_integrity.py",
```

`architecture-fitness` is the behaviour-preserving lane for it because the module imports the
verification package (`agents_remember_test_support.code_quality.record_integrity`) and executes
nothing over a real boundary: no process, no Node, no temporary repository. The manifest now carries
**249 module rows**, and the file is **267 lines** at that candidate — **both superseded by
`260918-TSIP-L4`, which added two further rows and re-read the shipped loader at 251 rows / 251
modules over a 269-line file** (`:165` the chain-order module in `integration`, `:244` the
response-conformance module in `architecture-fitness`) — **and superseded again by
`260918-TSIP-L5`, which added one further row at `:153` and re-read the file at 252 rows / 252
modules over 270 lines** (see its own section below).

**The insertion moved every manifest entry below it, and no other position was available.** An
`architecture-fitness` entry must sit between its own header (`:227`) and the next lane header
(`provider-conformance`, `:248`), and the array read **18** entries at `228-245` before this leaf, so
`:246` — the array's last row — is the minimum-displacement position. The one-line shift invalidated
three citations, and the shift is therefore a memory repair rather than an edit that could be
avoided:

| Affected citation | Before | After | Disposition |
| --- | --- | --- | --- |
| this card's row **"Empty former stress/migration populations"** | `:262-265` | **`:263-266`** | **BROKEN**: `migration = [` moved `265` → `266` and fell out of the range; repaired |
| this card's row **"The manifest still has no default classification for an unregistered test file"** | `:4-265` | **`:4-266`** | stale end — its anchor still resolved, so **no check reported it**; repaired by reading the file |
| `onboarding/mcp/tests/test_codex_capsule_delivery.py.md`, its `provider-conformance` lane-row citation | `:254-254` | **`:255-255`** | **BROKEN**: that row's own path moved `:254` → `:255`; repaired |
| this card's row **"Provider contract classifications"** | `:242-256` | unchanged | **INTACT**: the range still covers `provider-conformance` at `:248` |

**Not every range that moved broke**, which is why those dispositions are a list rather than a rule:
a range still containing its anchor is not a finding, and only the product's own `range_resolution`
check separates the two. It reported exactly **two** of them at this candidate — this card's
`:262-265` and the `test_codex_capsule_delivery.py.md` row. The stale `:4-265` end was found by
reading the file instead, which is `T45`'s class exactly: a range that no longer reaches the line it
described renders like a correct one.

**And the loader is not silent at this candidate — a correction to the section below.** The row above
registers this leaf's module as the fail-closed loader requires, and the manifest is still **one row
short of the modules it must classify**: `load_lane_manifest(<repository root>)` on this candidate
refuses with

```
test evidence lanes have 1 finding(s):
  - test files without an explicit lane: ['mcp/tests/test_atomic_series_chain_pair_order.py']
```

That module was added by `260915-CAPS-L25` at `f0313143` and was never registered; the gap is **one
row at every commit since**, measured `247 entries / 248 modules on disk` at `f0313143`, `248 / 249`
at `d9becade`, and `249 / 250` here. So this is not this leaf's doing and not this leaf's to repair —
registering that module is a change to this file and belongs to the lane registry's owner — but two
claims in the section below are wrong because of it and are corrected here rather than repeated:
`pytest tests/test_evidence_lanes.py tests/test_suite_budget.py -q` does **not** exercise
`load_lane_manifest` (its one registry case validates the lane *categories*), so its green says
nothing about the loader; and the loader was already refusing at the previous leaf's candidate, not
silent.

After this insertion the lane populations are: unit-regression **150** (`6-155`), public-contract
**2** (`158-159`), integration **64** (`162-225`), architecture-fitness **19** (`228-246`),
provider-conformance **14** (`249-262`), with `stress-durability` (`:264`) and `migration` (`:266`)
still empty — every lane above the insertion is unchanged.

## 260918-TSIP-L1 Row — The Instrument-Discipline Module

This leaf adds **one row** to the existing `architecture-fitness` lane, at `:232`, between
`mcp/tests/test_file_size_detector.py` (`:231`) and `mcp/tests/test_layering.py` (`:233`):

```toml
  "mcp/tests/test_instrument_discipline.py",
```

`architecture-fitness` is the behaviour-preserving lane for it because the module imports the
verification package (`agents_remember_test_support.code_quality.instrument_discipline`) and executes
nothing over a real boundary: no process, no Node, no temporary repository. `unit-regression` and
`integration` would both misdescribe it. **Corrected by the `260918-TSIP-L2` curator, and wrong when
written:** the claim that the fail-closed loader is silent at this candidate rested on
`pytest tests/test_evidence_lanes.py tests/test_suite_budget.py -q` → **4 passed in 0.54 s**, a run
that never calls `load_lane_manifest` (its one registry case validates the lane *categories*). Called
directly, the loader already refused at this candidate — `test files without an explicit lane:
['mcp/tests/test_atomic_series_chain_pair_order.py']`, an unregistered module from `260915-CAPS-L25`
that no seat on this master has registered. The module does collect into the lane, which is what the
row above establishes; the loader's silence was never measured. See the section above.

**The insertion is a one-line change that moved the 27 manifest entries below it, and that is the
fact to carry forward.** Every entry at or below `:232` gained one line; the entries above it did
not. Measured against the base commit, the two rows whose citations this invalidated are:

| Module | Before | After |
| --- | ---: | ---: |
| `mcp/tests/test_pause_is_not_publication.py` | 235 | **236** |
| `mcp/tests/test_codex_capsule_delivery.py` | 253 | **254** |

The pause suite's own row, `mcp/tests/test_pause_stop_only_end_to_end.py` at `:199`, is **above** the
insertion point and did not move — which is worth stating because the L37 lane-registration row in
`mcp/tests/overview.md` pairs that unmoved `:199` with the moved `:236`, and a reader who assumed
both had shifted would mis-cite one of them.

Four memory documents cited the pre-insertion numbers for those rows, and all four were repaired in
the same pass. Three were pure moves and the shipped citation fixer projected them mechanically
(`ccr-r10@v1`): this card's own `:235` → `:236` at line 762, `test_pause_is_not_publication.py.md`'s
`:235` → `:236`, and `test_codex_capsule_delivery.py.md`'s `:253` → `:254`. The fourth — the L37
lane-registration row in `mcp/tests/overview.md` — was **declined** by the fixer
(`projection_no_resolved_extent`: one anchor resolved to four extents) and was corrected by hand to
cite the two ranges that actually hold its two named anchors. This is the same hazard the L11 curator
recorded on this card after the six `D9` rows were added: **a row insertion renumbers every row below
it, and a cited line number is only true against one revision of this file.**

**Population.** No row was removed and no lane key moved; the module count rose by exactly one. This
card's earlier population paragraphs remain the as-of records of the leaves that wrote them and are
not restated here as current.

## 260915-KS-L21 Lane Row (Declared) — **the current account**

This leaf registers **one** module, `mcp/tests/test_migration_census.py`, as a `unit-regression` row
**inserted mid-list** in the alphabetical knowledge run — after `test_memory_scope_task_derivation.py` at
`:127` and above `test_models.py` at `:129`, so its row is `mcp/tests/test-evidence-lanes.toml:128`. The
lane is the behaviour-preserving classification rather than a budget convenience: the module is hermetic —
temporary directories, in-process APSW databases built through the shipped candidate write path, no
integration marker, no repository working tree, no subprocess and no network — and the census it measures is
a read over records that one in-process candidate batch wrote. It adds **48 cases and no integration case**,
which is why the integration lane is untouched by this leaf.

**Measured on this candidate, from the manifest and the modules on disk rather than by adding any earlier
account:**

| | measured on the working candidate |
| --- | --- |
| Declared lane entries | **291** |
| `mcp/tests/test_*.py` modules on disk | **291** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| `unit-regression` | **184**, key `:5`, rows `6-189` |
| `public-contract` | **2**, key `:191`, rows `192-193` |
| `integration` | **74**, key `:195`, rows `196-269` |
| `architecture-fitness` | **17**, key `:271`, rows `272-288` |
| `provider-conformance` | **14**, key `:290`, rows `291-304` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:306` and `:308`) |

**Why every later line of this file shifted, and what it obliges.** The insertion is *mid-list*, so every
entry below it moved by one: the previously-recorded `test_knowledge_change_sets.py` row at `:187` is at
`:188` now, `test_worktree_status_terminal_next_tool.py` moved `:262` → `:263`, and every citation into this
manifest from any route card that pointed below `:128` was re-derived in this pass rather than carried. That
is the mechanical reason several of this card's own rows were re-cited, and it is inherent to the registry
rather than a mistake.

**The budget pair moved too, and this is the leaf that moved it.** `260915-KS-L21`'s 48 unit cases took the
merged unit population from **2158** (measured at its base `a7076008`) to **2206** — six past the then-declared
2200 — so `pyproject.toml`'s unit ceiling was raised to **`unit_case_budget = 2300`** at
`pyproject.toml:244`, with the measured entry recorded above the value (populations at the raise, this leaf's
delta, the increment's per-leaf growth and the zero-tests consequence). Integration is **unchanged at
`integration_case_budget = 400`** at `:245`, measured **394 collected**: this leaf adds no integration case
and its six cases of headroom are reported rather than consumed. The earlier `1500` / `2200` / `1250` / `1100`
values this card quotes in its historical sections are retained as the rulings that produced them and none
was deleted.

## 260915-KS-L22 Lane Row — The Review-Surface Module, And Why It Is A Unit Row

This leaf registers **one** module, `mcp/tests/test_knowledge_review_surface.py`, as a
`unit-regression` entry **inserted mid-list** in the alphabetical knowledge run — between
`test_knowledge_read_scope.py` at `:102` and `test_knowledge_requirement_reference_contract.py` at
`:104` — so its row is `mcp/tests/test-evidence-lanes.toml:103`. The lane is the
behaviour-preserving classification rather than a budget convenience: the module drives the review
surface over temporary directories and in-process databases it builds itself, with no integration
marker, no repository working tree, no subprocess and no network.

**Measured against the manifest and the modules on disk rather than carried from any earlier
account:**

| | measured on this candidate |
| --- | --- |
| Declared lane entries | **292** |
| `mcp/tests/test_*.py` modules on disk | **292** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| `unit-regression` | **185**, key `:5`, rows `6-190` |
| `public-contract` | **2**, key `:192`, rows `193-194` |
| `integration` | **74**, key `:196`, rows `197-270` |
| `architecture-fitness` | **17**, key `:272`, rows `273-289` |
| `provider-conformance` | **14**, key `:291`, rows `292-305` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:307` and `:309`) |

The insertion is *inside* a lane, so every entry below `:103` moves one line down — the mechanical
reason the L21 section's row numbers above read one lower than this file's current positions, and
the reason a batch of citations into this manifest needed re-projecting in the same change rather
than carried.

## 260915-KS-L23 Five Appended Lane Rows — The Line-Stable Append Point

This leaf registers **five** modules, all as `unit-regression` entries **appended to the end of the list**
(`mcp/tests/test-evidence-lanes.toml:191-195`) and never inserted mid-list:

| Row | Module | Why the unit lane |
| ---: | --- | --- |
| `:191` | `mcp/tests/test_next_step_address_binding.py` | 4 cases over `compute_next_step` and `bound_next_step`: no store, no process, no network |
| `:192` | `mcp/tests/test_terminal_preview_expectation.py` | 3 cases over the terminal-validation preview expectation: no store, no process |
| `:193` | `mcp/tests/test_knowledge_merge_right_side_writes.py` | 3 cases over in-process APSW databases the shared merge fixture builds under `tmp_path` |
| `:194` | `mcp/tests/test_evidence_catalog_gate_boundaries.py` | 2 cases over a synthetic catalogue and a disposable `git init` / `git add` repository under `tmp_path` — the only one of the five that shells out, and only against a temporary root |
| `:195` | `mcp/tests/test_curator_coherence_publication_discoverability.py` | 8 cases over the request, the refusal and the `prepare` text, with the surface's collaborators patched through `unittest.mock` |

**Why all five took the unit lane, stated as the constraint it is.** Four are focused suites over
in-process or temporary state; the fifth (`test_evidence_catalog_gate_boundaries.py`) really does shell out
to `git init` / `git add`, against a temporary root it owns. The rows are all in `unit-regression` anyway
because three constraints meet here: the loader requires every `mcp/tests/test_*.py` module to hold exactly
one lane; the integration lane is at exactly **400 / 400** in this change set, so an integration row would
refuse collection and that lane would execute zero tests; and item 16(a)'s append point is the end of a
list, so the row had to go where an append moves nothing — a mid-list or cross-lane placement would have
moved exactly the rows this leaf exists to keep still.

**The append point is the point.** These five rows are the change that makes this manifest's unit list
**not alphabetical at its tail**, and that is deliberate: an insertion in the knowledge run shifts every
row below it and stales every citation into this file (one landing staled **90** rows tree-wide at L19 —
74 inherited, 16 shifted by the leaf's own rows), while an append at the end of the list leaves **every
existing row of that list** where it was. It moves no row; the lane keys below `unit-regression` still
shift, by five here, and that residue is the pure-move class item 16 half (b) reports rather than bills as
curator work. The property is pinned by
`mcp/tests/test_memory_citation_resolution.py::InsertedRegistrationRangeDriftTests::test_the_shipped_registries_append_point_is_the_end_of_its_own_list`,
which measures the **shipped** manifest and also asserts that a contrasting mid-list insertion *does* move a
row, so it cannot pass vacuously; the paired half classifies a citation whose anchor survived a move as a
**report-only** stale range rather than as curator work. No header comment stating the new append point was
added to this file, deliberately — a line at `:1` would shift every row in it and stale hundreds of
citations, so the comment would itself be the defect. The rule lives where it is enforced, in that case.
The five rows are also the manifest's whole byte change: no row was moved, edited or removed.

**Measured on this candidate from the manifest and the modules on disk, not carried from any earlier
account:**

| | measured on this candidate |
| --- | --- |
| Declared lane entries | **297** |
| `mcp/tests/test_*.py` modules on disk | **297** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| `unit-regression` | **190**, key `:5`, rows `6-195` |
| `public-contract` | **2**, key `:197`, rows `198-199` |
| `integration` | **74**, key `:201`, rows `202-275` |
| `architecture-fitness` | **17**, key `:277`, rows `278-294` |
| `provider-conformance` | **14**, key `:296`, rows `297-310` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:312` and `:314`) |

`297` is `292 + 5`: the five modules are new in this change set, so the count moved by exactly the rows the
change set added. This section supersedes the per-lane tables above, including the L21 table whose heading
still calls itself the current account.

**The declared rails are the repository-root file's, and only one lane has headroom.** The budgets are
`unit_case_budget = 2300` at `pyproject.toml:244` and `integration_case_budget = 400` at `:245`
(`mcp/pyproject.toml` declares no `[tool.pytest.ini_options]`, so the root file is the inifile pytest
actually reads; `mcp/tests/conftest.py` now registers the two option names **without** the dead
`default=1100`/`default=300` declarations item 12 removed). In this change set the unit population measured
**2278 / 2300** and the integration population **400 / 400** — attributed to seat W1's worktree-bound
`pytest … --collect-only` runs, not to this pass, which ran no pytest. Integration therefore has **zero**
headroom, and it matters here: `pytest_collection_finish` raises `UsageError` on an over-budget population,
and an over-budget lane **executes zero tests** — which is why all five of this leaf's rows had to take a
unit lane rather than the integration one, and why the five rows were first mis-appended to the integration
list and corrected after that `UsageError` was measured.

## 260915-CAPS-L11 Row — D9's Six Historical Modules Registered

**This leaf registers the six modules D9 had left unregistered**, all in `unit-regression`, each in a
behaviour-preserving lane chosen by what the module actually does:

| Row | Module | Line | Lane | Why that lane |
| --- | --- | ---: | --- | --- |
| 1 | `mcp/tests/test_eve_adapter.py` | 57 | unit-regression | drives the adapter over doubles; no real runtime |
| 2 | `mcp/tests/test_eve_protocol.py` | 60 | unit-regression | pure protocol encode/decode |
| 3 | `mcp/tests/test_role_capsule_admission.py` | 112 | unit-regression | hermetic over a disposable corpus copy |
| 4 | `mcp/tests/test_role_capsule_compiler.py` | 113 | unit-regression | builds its own fixture; reads no real tree |
| 5 | `mcp/tests/test_role_instruction_corpus.py` | 114 | unit-regression | reads the authored corpus, starts nothing |
| 6 | `mcp/tests/test_task_projection.py` | 139 | unit-regression | in-process projection over fixtures |

**The loader is now silent, and the six are asserted to collect.** `load_lane_manifest` returns
`LANE-REGISTRY-OK 243 0` with no unregistered-module finding, and each of the six modules carries its
own row and collects (14+55+50+11+35+33 = **198** cases under the unit selection, **0** under
`-m integration`). Registering them is not a lane judgement taken by name: the six per-module
`unit-regression` dispositions were re-derived at this leaf's tip, and the seed
`S-D9-lane-row-removed` (delete one row) makes the loader **refuse by name** rather than classify it
by default — which is what proves the rows are load-bearing rather than decorative.

**A method fact worth keeping, because this leaf lost time to it.** The registry's digest must be
**asked of the product**, never rebuilt by hand. An intermediate draft computed
`sha256("\n".join(sorted(f"file:{p}={c}") + …))` — prefixed terms and a merged sort — where
`lane_manifest.py` hashes unprefixed `path=category` pairs with overrides appended unsorted after
them. That reconstruction produced a self-consistent checksum of the *script's own rendering*
(`bfbd21af…`) that described no artifact. The product's own value for this candidate is
**`61f9fba80e5c1c78015eabfc56aac31ca2778bb79a5f75f9a73a6bf984acaaa7`** over **243** files / **0**
overrides. The counts and dispositions were never in question; only the fingerprint was.

## 260915-CAPS-L9 Row

This leaf adds **one** manifest row — `mcp/tests/test_capsule_experiment_install.py:19` — and its
module is **not** a seventh `D9` module: the fail-closed loader still names exactly the same six
at this tip as at the clean base (`test_eve_adapter`, `test_eve_protocol`,
`test_role_capsule_admission`, `test_role_capsule_compiler`, `test_role_instruction_corpus`,
`test_task_projection`). The `test_install_runtime.py` mention at `:74` is pre-existing context
for the catalog consumer proof, not a row this leaf added.

## 260915-CAPS-L20 Lane Row — The Governing-Overview Guard

This leaf added the module its change set created to the existing `unit-regression` lane, one row, so
the fail-closed loader still names no module at all:

```toml
  "mcp/tests/test_governing_overview_resolution.py",
```

The lane is the behaviour-preserving one rather than a judgement call: the module writes only into a
`TemporaryDirectory`, drives no real repository, no boundary process and no network, and its whole
subject is one pure function over a six-file synthetic tree. It is a focused hermetic suite, which is
what the default delivery lane is for.

**Measured at this leaf's frozen candidate, through the product's own loader rather than by reading
this file** (`load_lane_manifest(Path('.'))` in the candidate worktree):

```
lane rows = 244
digest    = 4354cc9f2cca2e33cd1f9e6bb31c8ef4742f61782bf9da9ce9b23cefcd922cdc
new module registered = True -> unit-regression
distribution = unit-regression 147 · integration 64 · architecture-fitness 17 ·
               provider-conformance 14 · public-contract 2
validate_lane_registry() = None
```

`244` is `243 + 1`: `D9` was already complete at this leaf's base — L11 left **243 modules / 243 rows
/ 0 unregistered, 0 stale** — so this leaf's obligation is the one new row and nothing else. The
**digest is unchanged from the base** (`4354cc9f…`, the value the owning seat and L20's reviewer both
read at `621db898`), and that is the expected result rather than a stale read: the manifest digest
covers the declared lane *structure*, and a row added to an existing lane leaves it as it was.

**Why one row is the whole obligation.** `load_lane_manifest` derives the repository's actual test
modules and refuses a manifest that omits one, so an unregistered module is a **hard load failure**
rather than a silent gap — the same fail-closed property `260831-LOCR-L30` repaired a manifest for.
`test_governing_overview_resolution.py` and the extended `test_memory_quality_runs.py` are therefore
both collectable into lanes by construction, and the delivery graph's lane-based selection sees the
regression guards this leaf added.

## Governing Overview

[Tests overview](overview.md)

| Module | Lane | Row | Why that lane |
| --- | --- | ---: | --- |
| `mcp/tests/test_knowledge_detection_runs.py` | `unit-regression` | `:71` | 19 nodes; hermetic — temporary directories, in-process APSW databases, a synthetic union built in memory, and one module-scoped real two-snapshot fixture built by the already-registered `diff_scope_test_support`; no integration marker, no process, no publication |
| `mcp/tests/test_knowledge_detection_signals.py` | `unit-regression` | `:72` | 28 collected cases (20 definitions, one a nine-parameter table) measuring a typed record's own construction boundary — which fields are required, which vocabulary a value must come from, which shape is refused |

| | measured on the working candidate |
| --- | --- |
| Declared lane entries | **249** |
| `mcp/tests/test_*.py` modules on disk | **249** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| `unit-regression` | **149**, rows `5-155` |
| `public-contract` | **2**, rows `156-159` |
| `integration` | **68**, rows `160-229` |
| `architecture-fitness` | **17**, rows `230-248` |
| `provider-conformance` | **13**, rows `249-263` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:264` and `:266`, both closed at `:267`) |

| Module | Lane | Row | Why that lane |
| --- | --- | ---: | --- |
| `mcp/tests/test_knowledge_diff_scope.py` | `unit-regression` | `:76` | 13 nodes; hermetic — temporary directories under `tmp_path`, two in-process APSW databases built through the public store operations (the candidate copied from the closed baseline and curated through the store), two local committed Git trees built by the fixture, no integration marker |
| `mcp/tests/test_knowledge_diff_boundaries.py` | `integration` | `:159` | 15 nodes over the same real trees **driving the production Git probe** rather than a substitute, a real curated candidate database, a real write that moves the logical digest, and the serialized response |

| | measured on the frozen candidate |
| --- | --- |
| Declared lane entries | **243** |
| `mcp/tests/test_*.py` modules on disk | **243** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| Duplicate declarations | **0** |
| `unit-regression` | **143**, rows `5-149` |
| `public-contract` | **2**, rows `150-153` |
| `integration` | **68**, rows `154-223` |
| `architecture-fitness` | **17**, rows `224-242` |
| `provider-conformance` | **13**, rows `243-257` |
| `stress-durability` / `migration` | **0** / **0** (keys at `:258` and `:260`, both closed at `:261`) |

| Module | Lane | Row | Why that lane |
| --- | --- | ---: | --- |
| `mcp/tests/test_knowledge_read_scope.py` | `unit-regression` | `:75` | 21 nodes; hermetic — temporary directories under `tmp_path`, in-process APSW databases built through the public store operations, no repository working tree, no network, no integration marker |
| `mcp/tests/test_knowledge_read_boundaries.py` | `integration` | `:157` | 20 nodes over a **real committed Git tree**, a real published database and real snapshot/namespace refusals |
| `mcp/tests/test_knowledge_read_paths.py` | `integration` | `:158` | 5 nodes that measure Git's own `ls-tree` behavior with their own subprocess calls; it exists because these cases pushed the boundaries module past the 1 200-line hard limit in fix round 2, and the limit was paid rather than waived |

| | measured on the frozen candidate |
| --- | --- |
| Declared lane entries | **241** |
| `mcp/tests/test_*.py` modules on disk | **241** |
| Declared-but-absent / present-but-undeclared | **0 / 0** |
| Duplicate declarations | **0** |
| `unit-regression` | **142**, rows `6-148` |
| `public-contract` | **2**, rows `150-152` |
| `integration` | **67**, rows `154-221` |
| `architecture-fitness` | **17**, rows `223-240` |
| `provider-conformance` | **13**, rows `242-255` |
| `stress-durability` / `migration` | **0** / **0** |

## 260915-KS-L16 Lane Rows (Declared) — **the current account**
This leaf registered **three** modules: two under `unit-regression`, inserted mid-list among the knowledge
suites, and one appended to `integration`. The two mid-list insertions are what moved every later line of
this file by two:
| Lane | Row | Module | Why this lane |
| --- | ---: | --- | --- |
| `unit-regression` | `:92` | `mcp/tests/test_knowledge_family_review.py` | hermetic: a composition over typed records — which matches a merge keeps, which status an owner may report, what a moved input does to a binding |
| `unit-regression` | `:93` | `mcp/tests/test_knowledge_registered_scope.py` | hermetic: a construction over recorded rows and one declaration, driven by an in-process two-snapshot fixture |
| `integration` | `:265` | `mcp/tests/test_knowledge_family_integrity_pipeline.py` | it drives a real two-snapshot comparison over two real databases and two real Git trees and publishes real bytes to a real destination, and carries `pytestmark = pytest.mark.integration` |
The classification is the **behaviour-preserving** one, not a budget convenience: the two unit modules ask
questions about records and about a declaration, and the one integration module asks the whole-pipeline
question the packet's §6/§7 worked example is about. **The declared ceilings are the ones `pyproject.toml` actually carries** — `unit_case_budget = 2300` at
`pyproject.toml:244` and `integration_case_budget = 400` at `:245`. This section first recorded the pair as
`2200` / `400`; `260915-KS-L21` raised the unit ceiling to 2300 over the measured 2206 collected (six past
2200), so **2200 is retained here as the value this section measured and is no longer the declaration**, and
the integration value is unchanged at 400. The
three rows are a small delta inside them.
**Why every later line of this file shifted.** The two `unit-regression` rows are inserted mid-list (after
`test_knowledge_family_composition_boundaries.py`), so every entry below them — and every citation into
this file from any route card — moved by two. That is the mechanical reason several other cards' ranges
into this manifest are stale on this candidate.

## 260915-KS-L17 Lane Rows (Declared) — **the previous account, superseded on the three rows above**
This leaf registered **two** modules, both under `unit-regression`, and its insertions are what moved
every later line of this file by two:
| Lane | Row | Module | Why this lane |
| --- | ---: | --- | --- |
| `unit-regression` | `:74` | `mcp/tests/test_knowledge_family_composition.py` | hermetic: temporary directories and in-process APSW databases driven through the real admitted destination — no integration marker, no repository working tree, no subprocess |
| `unit-regression` | `:75` | `mcp/tests/test_knowledge_family_composition_boundaries.py` | the same shape, plus a byte-comparison of the dataset file around a refused read |
The classification is the **behaviour-preserving** one for both modules, not a budget convenience: the
suite's one integration-shaped question — whether composition edges move the retrieval selection — is
answered **by value** over the registered read-scope fixture inside the unit lane rather than by a
second real Git world. **The budget pair this section quotes is the one that candidate carried and is not
the current declaration:** it recorded the unit population at **1341** against the then-pinned
`"unit_case_budget = 1500"` and the integration population at **322** against
`"integration_case_budget = 400"`. The file declares `unit_case_budget = 2300` at `pyproject.toml:244` and
`integration_case_budget = 400` at `:245` on this candidate, and the measured populations are **2206** unit
and **394** integration. This leaf is a +26-unit, +0-integration delta and raises
nothing.
**Why every later line of this file shifted.** These two rows are inserted mid-list under
`unit-regression` (after `test_knowledge_facets.py`), so every entry below them — and every citation
into this file from any route card — moved by two. That is the mechanical reason several other
cards' ranges into this manifest were stale on this candidate and were re-cited during this leaf's
curation.
## 260915-KS-L14 Lane Rows (Declared) — **the current account**
## 260915-KS-L12 Lane Rows (Declared) — **the current account**
**Two new rows, and the line shifts they caused everywhere else.** `mcp/tests/test_knowledge_evidence_claims.py` and `mcp/tests/test_knowledge_evidence_observations.py` are registered in the `unit-regression` lane (rows 73 and 74), each carrying `pytestmark = pytest.mark.evidence_unit`. Every *other* file that cites a line of this manifest moved by the same insertion, and the citations in the cards that quote this file were repaired to the lines that now carry their anchors rather than left pointing at the row above. The lane membership is asserted by the gate rather than by this file alone: a module in the tree that no lane names fails the ownership check.
## 260915-KS-L14 Lane Rows (Declared) — **the previous account, superseded on the two rows above**

The KS-L14 change set adds **two** modules and their rows in the same change, and both are
behaviour-preserving classifications:

Both are inserted into the alphabetical knowledge run, which is why they are rows `:71` and `:72` rather
than appended: `test_knowledge_candidate_workspace.py` precedes them and `test_knowledge_facets.py`
follows. **A two-line insertion moves every later line of this file**, which is the mechanical reason a
number of citations to this manifest elsewhere in the memory tree need re-pointing in the same change.

**The merged measurement, taken on this leaf's working candidate** (measured from the manifest and the
module population on disk, not derived by adding any earlier account):

Against the previous account: **247 / 247** after the L11 and L24 leaves (147 / 2 / 68 / 17 / 13), so this
leaf's two modules are the whole difference. The declared budget pair is `unit_case_budget = 1500`
(`pyproject.toml:304`) and `integration_case_budget = 400` (`pyproject.toml:305`) **as this section measured
it — the pair declared now is `unit_case_budget = 2300` at `pyproject.toml:244` and
`integration_case_budget = 400` at `:245`** — **unchanged by this
leaf**, whose measured populations are 1315 unit and 322 integration and which consolidated nothing,
skipped nothing, deselected nothing and widened no ceiling.

**This leaf's support-module decision is what keeps the artifact counts unchanged.** Both new modules are
ordinary test source; the run module uses the two **already-registered** fixtures
(`diff_scope_test_support.py` and `read_scope_test_support.py`) rather than adding a third support module,
so `mcp/tests/evidence-lifecycle.toml` gained only two `consumers` rows and its populations stay at
**13 contracts and 54 artifacts**.

## 260915-KS-L8 Lane Rows (Declared) — **the previous account, superseded on the counts above**

The KS-L8 change set adds **two** modules and their rows in the same change, and each lane is that
module's behaviour-preserving classification:

Their shared support module `mcp/tests/diff_scope_test_support.py` is **not** a lane row: it is a governed
artifact (`shared-support` / `internal-canonical` / `integration` / `local-composition`, contract
`knowledge-diff-cases`) in `mcp/tests/evidence-lifecycle.toml`, with exactly those two modules as its
declared consumers — and it is also why `mcp/tests/read_scope_test_support.py`'s consumer list gained the
same two paths in this change, because the diff fixture builds on the read fixture.

### The merged measurement, taken on this leaf's frozen candidate

**Measured from the manifest and the module population on disk, not derived by adding any earlier
account:**

Against the previous leaf: **241 / 241** after `KS-L7` (142 / 2 / 67 / 17 / 13) and **238 / 238** on the
merged base `4eb2b199` (141 / 2 / 65 / 17 / 13), so this leaf's two modules are the whole difference. The
insertions sort into the alphabetical knowledge run — the scope module into unit-regression and the
boundaries module into integration — which is why they are rows `:76` and `:159` rather than adjacent.

**The declared budget pair is unchanged by this leaf:** `unit_case_budget` is **1250** at
`pyproject.toml:286` and `integration_case_budget` is **340** at `pyproject.toml:287`, and
`git status --porcelain pyproject.toml` is **empty** — no dated entry, no comment edit, no value moved.
The raised pair and its merged-line attribution (official 1014/1100 green, KS parent 1003/1100 green,
merged 1138/1100 red *before any L7 line*) are recorded in the L7 section below and are **not re-opened
here**: this leaf's populations fit under both ceilings (unit 1172, integration 319 measured by the final
verification round against the frozen bytes), it consolidated nothing, and it skipped, xfailed,
deselected or widened nothing.

## 260915-KS-L7 Lane Rows (Declared) — **the previous account, superseded on the counts above**

The KS-L7 change set adds **three** modules and their rows in the same change, and the lane each takes is
its behaviour-preserving classification:

Their shared support module `mcp/tests/read_scope_test_support.py` is **not** a lane row: it is a governed
artifact (`shared-support` / `internal-canonical` / `unit-regression`, contract `knowledge-read-scope-cases`)
in `mcp/tests/evidence-lifecycle.toml`, with the three modules above as its exactly-declared consumers.

**The two labelled accounts this card carried below were measured against different code states and their
merged counts were recorded as pending. They have now been measured, and this is the measured account** —
counted from the manifest and the module population on disk, not derived by adding the two accounts:

For the same reason the earlier accounts are labelled rather than merged: the **merged base** `4eb2b199`
carried **238** entries and **238** modules (141 / 2 / 65 / 17 / 13), so this leaf's three test modules are the
whole difference, and neither earlier account alone describes the merged tree. Nothing here is arithmetic on
the two superseded numbers.

**The declared budget pair moved again for this leaf, and every earlier value recorded below is stale.**
`unit_case_budget` is **1250** at `pyproject.toml:286` and `integration_case_budget` is **340** at
`pyproject.toml:287`, raised by the owning seat's dated entry in the same file because the merged line's unit
population was **1138 against a ceiling of 1100** *before any L7 line* — an over-budget population raises
`UsageError` in `pytest_collection_finish`, so the whole unit run executed **zero** tests. This is a
**merged-line sizing defect and not a defect of either side**: the official line alone at `tip 8dd62345`
collected 1014 against its own 1100, and the KS parent `7db50f8f` collected 1003 against the same 1100, and
both were green. **The raise is headroom, not a target**, and the sizing question is not re-opened here: no
existing case was consolidated, deleted, skipped, xfailed or deselected, and the four earlier dated entries
are intact. This leaf's own populations: **unit 1138 → 1159** collected (its 21 unit cases), integration
**279 → 304** selected (its 25 integration cases).

## 260915-KS-L6 Lane Rows (Declared) — **the current account, which supersedes every per-lane number below**

The KS-L6 change set adds **two** modules and their rows in the same change — `test_knowledge_portable_roundtrip.py`
and `test_knowledge_portable_boundaries.py` — both in the **integration** lane at
`mcp/tests/test-evidence-lanes.toml:140-141`. The lane is not a preference here, it is forced: the unit population
sits exactly at its declared `unit_case_budget` of 1000, so a unit row would refuse collection, and both modules are
boundary executors anyway — they create real SQLite databases under `tmp_path`, publish and re-open closed files, and
measure destination bytes and directory contents.

Measured against the working manifest, the population is closed in both directions at **221 modules on disk and 221
declared entries**, with the current brackets: unit-regression **127** at rows 6-132, public-contract 2 at 135-136,
integration **63** at 139-201, architecture-fitness 16 at 204-219 and provider-conformance 13 at 222-234, with
stress-durability (236) and migration (238) empty. The two portable modules sort into the alphabetical integration
run, which is why they are rows 140-141 rather than at the end of the lane; every later integration row moved by two.

Their registration is the same precondition it has been at every KS leaf: an unregistered `test_*.py` module makes
`load_lane_manifest` refuse the repository, which `evidence_lanes.pytest_collection_modifyitems` turns into a
collection error. Classification only — never execution or acceptance evidence.

**The declared budget pair moved for that leaf, and every value in this paragraph is now superseded by `1250` / `340`.** At `KS-L6` `integration_case_budget` was raised 250 → **300** at `pyproject.toml:186` with the doctrine-required dated tradeoff above the pair, and `unit_case_budget` was **1000** at `pyproject.toml:185` with the real unit population 1003 under the warning override this host needs — the pre-existing defect recorded as **D-7**, which the incoming official line closed by raising its own ceiling to 1100. Both then had to move again for `KS-L7` when the *merged* line carried both populations (see the L7 section at the top of this card). The lane's own population at that leaf was **255 cases + 41 subtests**, green with no `--ignore`.

## Current population (measured at this leaf's synced base `23cc7a72` plus its own two rows)

**236** `test_*.py` modules on disk and **230** manifest entries, with the loader reporting **one**
finding: six test files carry no explicit lane. Those six —
`test_eve_adapter.py`, `test_eve_protocol.py`, `test_role_capsule_admission.py`,
`test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`, `test_task_projection.py` — are
**pre-existing at the pristine base** and are none of them this leaf's modules; this leaf adds two rows
and closes none of that gap. Every count stated in the earlier sections below is an earlier
measurement and must be read as such.

**This paragraph is the L7 candidate's measurement, not the current one.** Measured at the L16
candidate (base `8997e184` plus its change set): **232 declared rows** against **238** modules on disk,
the same six D9 modules unregistered. The L16 section below carries that measurement; nothing in this
paragraph is a claim about the current population.

Lane brackets as measured now: unit-regression 134 entries (key `:5`), public-contract 2 (`:141`),
integration 63 (`:145`), architecture-fitness 17 (`:210`), provider-conformance 14 (`:229`), with
stress-durability (`:245`) and migration (`:247`) empty.

Case budgets are `pyproject.toml`'s and are **not** lane membership: `unit_case_budget = 1500` and
`integration_case_budget = 300` (`.tool.pytest.ini_options`). Every earlier 150/200/250/1000/1100
figure quoted in this card's history is stale.

## Purpose

**Population measured in the 260915-KS change set (this branch).** Classifies 217 retained test-shaped modules into explicit evidence categories: **126 unit-regression, 2 public-contract, 60 integration, 16 architecture-fitness and 13 provider-conformance; stress-durability and migration are empty** (measured in the 260915-KS-L4 change set, which is the account that supersedes every per-lane number recorded below). The 260915-KS-L1 change set registered `test_knowledge_store.py` in **unit-regression** (row 74 in the current manifest), the 260915-KS-L2 change set registered four further knowledge modules in that same lane (rows 69-73), and the 260915-KS-L3 change set registered `test_candidate_batch_commands.py` and `test_candidate_batch_transaction.py` (rows 18-19) plus `test_knowledge_label_operations.py` (row 70). The KS-L3 section below carries the measured current brackets; the KS-L2 and KS-L1 sections are those leaves' as-of records. The focused terminal-evidence cursor suite `test_terminal_evidence_cursors.py` and the parked-external-await separation guard `test_parked_external_await_separation.py` are unit-regression members, and 260831-LOCR-L32 added `test_worktree_status_terminal_next_tool.py` to the **integration** lane (row 175; it drives real worktree services and a real repository under `tmp_path`), while 260831-LOCR-L34 added `test_checkpoint_landing_end_to_end.py` to that same lane (row 132; it drives the public checkpoint/closeout operations over real temporary Git repositories), and 260831-LOCR-L36 added `test_cross_master_concurrency.py` to that lane as well (row 143; it drives two sprint-commanded atomic masters and the public land/resume operations over one real temporary Git world), while 260831-LOCR-L37 added `test_pause_stop_only_end_to_end.py` to that same lane (row 159; it drives the public pause over one real temporary Git world holding two atomic masters and measures refs, object databases, coordination tree, worktrees and task documents before and after) **and** `test_pause_is_not_publication.py` to **architecture-fitness** (row 191; it is an AST-only import-closure guard that executes nothing), and the 260831-LOCR seal-removal change set added `test_lifecycle_playthrough_end_to_end.py` to **integration** (row 153; it plays the whole leaf-and-master lifecycle in order over one real temporary Git world and is the regression proof for the deleted child-admission seal). The 260913-LCA-L7 change set added one more integration member.

**Population measured on the official line at the `260831-LOCR-L39` hardening tip (the incoming account).** Classifies the retained test-shaped modules into explicit evidence categories. **Current population measured at the `260831-LOCR-L39` hardening tip (code base `a5f5380b`): 224 modules on disk and 224 manifest entries — 130 unit-regression (key `:5`, rows 6-135, next key `:137`), 2 public-contract (key `:137`, rows 138-139), 62 integration (key `:141`, rows 142-203), 17 architecture-fitness (key `:205`, rows 206-222) and 13 provider-conformance (key `:224`, rows 225-237); stress-durability (`:239`) and migration (`:241`) are empty. The unit-regression bracket is `:5-135`, the integration bracket is `:141-203`.** The L05 measurement and its method are in the `## 260831-LOCR-L04 Lane Row (Declared)` and `## 260831-LOCR-L05 Lane Row (Declared)` sections below; the `## 260831-LOCR-L06 Lane Row (Declared)` section carries the immediately preceding 215-module measurement (pair code base `e9678c56`), the `## 260831-LOCR-L17 Lane Row (Declared)` section the 214-module one before that and the `## 260831-LOCR-L18 Lane Row (Declared)` section the 213-module one before that. Every count and bracket in the two paragraphs below is an earlier measurement — L23 measured 208 modules, and sibling unit-lane insertions from L01 (`:97`) and L10 then moved the later file lines down; L27's own integration row at `:183` accounts for the rest; those two declared sections are the as-of records that carry their own evidence. The focused terminal-evidence cursor suite `test_terminal_evidence_cursors.py` and the parked-external-await separation guard `test_parked_external_await_separation.py` are unit-regression members, and 260831-LOCR-L32 added `test_worktree_status_terminal_next_tool.py` to the **integration** lane (row 175; it drives real worktree services and a real repository under `tmp_path`), while 260831-LOCR-L34 added `test_checkpoint_landing_end_to_end.py` to that same lane (row 132; it drives the public checkpoint/closeout operations over real temporary Git repositories), and 260831-LOCR-L36 added `test_cross_master_concurrency.py` to that lane as well (row 143; it drives two sprint-commanded atomic masters and the public land/resume operations over one real temporary Git world), while 260831-LOCR-L37 added `test_pause_stop_only_end_to_end.py` to that same lane (row 159; it drives the public pause over one real temporary Git world holding two atomic masters and measures refs, object databases, coordination tree, worktrees and task documents before and after) **and** `test_pause_is_not_publication.py` to **architecture-fitness** (row 191; it is an AST-only import-closure guard that executes nothing), and the 260831-LOCR seal-removal change set added `test_lifecycle_playthrough_end_to_end.py` to **integration** (row 153; it plays the whole leaf-and-master lifecycle in order over one real temporary Git world and is the regression proof for the deleted child-admission seal). The 260913-LCA-L7 change set added one more integration member.

**These two accounts are each an as-of record of the state they were measured against, and neither is the merged tree's count.** The merged counts were measured by this branch's curators and are recorded in the `260915-KS-L8 Lane Rows (Declared)` section at the top of this card — **243 declared entries against 243 modules on disk** on this leaf's frozen candidate, after `KS-L7`'s measured 241/241 — so the placeholder this sentence used to carry is resolved rather than still pending. The two accounts below are kept, not deleted, under the memory doctrine's as-of rule.
`test_closeout_projection_source_classification.py` (entry row 137) — it composes the real
`QueueFixture` over temporary Git repositories and drives the production graph admission and
projection path through `graph_context` and `capture_projection_source`, so that is its
behaviour-preserving lane — bringing the manifest to 205 rows. The 260913-LCA-L3 change set registered one more unit-regression member, the new `mcp/tests/test_memory_backfill.py` (entry row 69), and 260831-LOCR-L23 registered `mcp/tests/test_terminal_liveness_registration_order.py` in that same lane (entry row 118), which was `260831-LOCR-L23`'s measured population of 208 modules on disk and 208 manifest entries. The insertions split the alphabetical run again, so the unit-regression lane now carries 117 entries at rows 5-122, public-contract its 2 at 123-126, integration its 60 at 127-188, architecture-fitness its 16 at 189-206 and provider-conformance its 13 at 207-221, while stress-durability (222-223) and migration (224-225) remain empty. The population had earlier fallen below its historical peak because the de-entanglement cut deleted four integration modules — `test_integration_ref_transaction.py`, `test_worktree_integrate_quality_gate.py`, `test_closeout_memory_certification_reuse.py` and `test_prepared_publication_recovery.py` — and the 188 rows this manifest held before 260831-LOCR-L30 were that reduced set; the eight rows added by that leaf brought it to 196, L32's row to 197, L34's to 198, L36's to 199, and L37's two to 201. Every `mcp/tests/test_*.py` module on disk is listed exactly once and no path is duplicated — 224 modules, 224 manifest entries. File counts are not collected-case counts, and the lane bracket is the unit of accounting: unit-regression is the default delivery lane, while the integration lane is capped at 300 collected cases (`pyproject.toml:168`; 260831-LOCR-L37 raised it 200 -> 250 and 260831-LOCR-L24 250 -> 300, with the unit ceiling 1,000 -> 1,100, on the explicit developer tradeoff recorded in `pyproject.toml`, and every earlier 150, 200 and 250 figure recorded in entries of this card is stale). The closeout auto-carry change registered one new module, `test_sync_parked_candidate.py`, in the existing `unit-regression` lane, and the L28 leaf registered its boundary-delivery module `test_state_signal_boundary_delivery.py` in that same lane; the per-lane counts above are the current source membership.

260831-LOCR-L30 registered eight members and, in doing so, repaired a manifest that could not load at
all. `load_lane_manifest` independently proves the declared population closed — it derives the
repository's actual test modules and refuses a manifest that omits one — so an unregistered module is
a **hard load failure**, not a silent gap. Seven tracked `test_*.py` modules (one of them,
`test_record_landing.py`, shipped by the immediately preceding leaf) had no lane row, which made every
manifest consumer fail rather than mis-classify. The eight rows are `test_checkpoint_landing.py`,
`test_closeout_kept_rules_pins.py`, `test_memory_scope_task_derivation.py`,
`test_post_integration_cleanup_guidance.py`, `test_record_landing.py`,
`test_retired_door_publication_fields.py` and `test_automatic_post_integration_cleanup.py` in the
existing lanes, plus `test_memory_quality_is_independent_of_the_closeout_plane.py` in
`architecture-fitness`. Each took its behaviour-preserving lane: the six new unit-regression rows are
hermetic focused suites and the integration lane is capped at 200 collected cases
(`pyproject.toml:135`; the "150" this card's earlier entries recorded is stale), so nothing was
moved into it beyond the one module that genuinely exercises an integration boundary.
## 260915-KS-L4 Lane Rows (Declared)

The KS-L4 change set adds **two** modules and their rows in the same change — `test_knowledge_candidate_workspace.py`
and `test_knowledge_snapshot_publication.py` — both in the **unit-regression** lane at
`mcp/tests/test-evidence-lanes.toml:69` and `:75`. Each is hermetic: temporary directories under `tmp_path`,
in-process APSW databases driven through the real admitted destination and the real publication lock, a child
interpreter used as a crash probe (not a service), no integration marker, and no repository working tree or
network. The default unit lane is therefore each one's behaviour-preserving classification, exactly as it was for
the L2 and L3 knowledge modules beside them.

The two rows sort into the alphabetical run beside the rest of the knowledge block, which is why they sit within
rows 69-76 rather than at the end of the lane.

**Measured current brackets, by entry row** — this is the current account, and it supersedes every earlier
per-lane bracket in this card: unit-regression **126** entries at rows 6-131, public-contract 2 at 134-135,
integration 60 at 138-197, architecture-fitness 16 at 200-215, provider-conformance 13 at 218-230, with
stress-durability (232) and migration (234) empty. The population is closed in both directions at **217** modules
on disk and 217 declared entries — the KS-L3 population was 215 and these are the two additions. Every knowledge
module registered by L1, L2, L3 and L4 now sits inside rows 69-76. Unit collected cases remain inside the declared
`unit_case_budget` 1000 (`pyproject.toml:149`).

Registration is still the same precondition: an unregistered `test_*.py` module makes `load_lane_manifest` refuse
the whole repository, which `evidence_lanes.pytest_collection_modifyitems` turns into a collection error.
Classification only — never execution or acceptance evidence.

## 260915-KS-L2 Lane Rows (Declared)

The KS-L2 change set adds **four** modules and their rows in the same change — `test_knowledge_family_revision.py`,
`test_knowledge_graph_reads.py`, `test_knowledge_relation_rules.py` and `test_knowledge_revision_seals.py` — at
rows `mcp/tests/test-evidence-lanes.toml:70-74`, all in the **unit-regression** lane. Each is hermetic (temporary
directories under `tmp_path`, in-process APSW databases, no integration marker, no repository or subprocess), so
the default unit lane is each one's behaviour-preserving classification. The population is closed in both
directions at **212** modules on disk and 212 declared entries — the KS-L1 population was 208 and these are the
four additions.

**Measured current brackets, by entry row** — this is the current account, and it supersedes every earlier
per-lane bracket in this card: unit-regression **121** entries at rows 6-126, public-contract 2 at 129-130,
integration 60 at 133-192, architecture-fitness 16 at 195-210, provider-conformance 13 at 213-225, with
stress-durability (226-228) and migration (229-231) empty. The knowledge modules sit at rows 67-71, inside the
alphabetical run, so the insertion shifted the lanes after it. Unit collected cases remain inside the declared
`unit_case_budget` 1000 (`pyproject.toml:149`).

`test_knowledge_revision_seals.py` arrived one round later than the other three, as the fix for sealed review
finding `260915-KS-L2-RV-1`: the round-1 mutation array could not kill the sealed predecessor field on either
payload, and the new module is where the field-isolating evidence for it now lives. Its row was added in the same
change, which is why one leaf is recorded as three rows plus one.

Registration here is not bookkeeping, and the KS-L1 note below states why: `load_lane_manifest` derives the
repository's actual test modules and refuses a manifest that omits one, so an unregistered module is a **hard load
failure** — the lane plugin raises `pytest.UsageError` during collection and the quality path swallows the same
error into a run without retry proof. These rows are classification only — never execution or acceptance evidence.

## 260915-KS-L3 Lane Rows (Declared)

The KS-L3 change set adds **three** modules and their rows in the same change — `test_candidate_batch_commands.py`,
`test_candidate_batch_transaction.py` and `test_knowledge_label_operations.py` — all in the **unit-regression**
lane. Each is hermetic (temporary directories under `tmp_path`, in-process APSW databases driven through the real
admitted destination, no integration marker, no repository and no subprocess), so the default unit lane is each
one's behaviour-preserving classification. The direct rows are
`mcp/tests/test-evidence-lanes.toml:18`, `:19` and `:70`; the two batch modules sort into the alphabetical run
near its top, which is why the first two sit at rows 18-19 rather than beside the knowledge block.

The first two are the pair the requirement's verification evidence asks for, and their third sibling exists
because a passing batch suite could not cover the standalone label guard: `test_candidate_batch_transaction.py`
carries the all-or-nothing proof (mutating the rollback to a commit fails a named node), the admission and lane
refusals, the completed-graph lineage rule and the removal receipts; `test_candidate_batch_commands.py` carries the
closed union's coverage and the receipt's fidelity; `test_knowledge_label_operations.py` drives the two standalone
label edits so deleting the CAS in `labels.py` fails a named node — the mutation that left every batch case green
before this module existed (sealed finding `260915-KS-L3-RV-4`).

The population is closed in both directions at **215** modules on disk and 215 declared entries — the KS-L2
population was 212 and these are the three additions. **Measured current brackets, by entry row** — this is the
current account, and it supersedes every earlier per-lane bracket in this card: unit-regression **124** entries at
rows 5-130, public-contract 2 at 131-134, integration 62 at 135-196, architecture-fitness 18 at 197-214,
provider-conformance 13 at 215-229, with stress-durability (230-231) and migration (232-233) empty. The five
earlier knowledge modules sit at rows 69-74, inside the alphabetical run. Unit collected cases remain inside the
declared `unit_case_budget` 1000 (`pyproject.toml:149`).

Registration is the same precondition it has been at every KS leaf: an unregistered `test_*.py` module makes
`load_lane_manifest` refuse the whole repository, which `evidence_lanes.pytest_collection_modifyitems` turns into a
collection error. Classification only — never execution or acceptance evidence.

## 260915-KS-L1 Lane Row (Declared)

The KS-L1 change set adds `mcp/tests/test_knowledge_store.py` **and** its row in the same change, so the
manifest stays closed at **208** modules on disk and 208 manifest entries — the L3 population was 207 and this is
the one addition. The row is `mcp/tests/test-evidence-lanes.toml:67`, in the **unit-regression** lane: the module
is hermetic (temporary directories under `tmp_path`, in-process APSW databases, no integration marker, no
repository or subprocess), so the default unit lane is its behaviour-preserving classification.

Registration here is not bookkeeping. `load_lane_manifest` derives the repository's actual test modules and
refuses a manifest that omits one, so an unregistered module is a **hard load failure**: the lane plugin raises
`pytest.UsageError` during collection and the quality path swallows the same error into a run without retry proof.
The leaf's own independent review confirmed both consequences before the row existed. The row is classification
only — never execution or acceptance evidence.

Measured current brackets, by entry row: unit-regression **117** entries at rows 6-122, public-contract 2 at
125-126, integration 60 at 129-188, architecture-fitness 16 at 191-206, provider-conformance 13 at 209-221, with
stress-durability (222-224) and migration (225-227) empty; the lane key itself sits at `:5`. Unit collected cases
remain inside the declared `unit_case_budget` 1000 (`pyproject.toml:149`). The insertion is at `:67`, above every
row the L3 entry above cites, so the L4/L5/L7/L8 sections' bracket numbers and row positions are unchanged by this
change and the L3 note remains their superseding account. The population is closed in both directions: 208 modules
on disk, 208 declared entries, no undeclared module and no stale row.

## 260915-CAPS-L15 Lane Row (Declared)

The L15 change set adds `mcp/tests/test_capsule_launch_wiring.py` **and** its row in the same change, so
the manifest stays closed in that change set. The row is `mcp/tests/test-evidence-lanes.toml:19`, in the
**unit-regression** lane, inserted alphabetically between `test_causal_quality_preflight.py` and
`test_capsule_serving.py`. That is its behaviour-preserving lane: the module's fourteen cases drive the
launch points, the runner preparation and the adapter factory **in process**, with the vendor boundary
recorded and the tmux host doubled — it starts no real process and calls no vendor — so the hermetic
default unit lane is where it belongs. **Lane row added; no case added to any capped population that
was not already there.**

**The loader invariant is the point of this row (defect D9).** `load_lane_manifest` independently proves
the declared population closed — it derives the repository's actual test modules and refuses a manifest
that omits one — so a new test module without a lane row is a **hard load failure** for every manifest
consumer, not a silent gap. L15 followed that rule in the same change that added the module; the six
historical D9 modules remain the final-verification leaf's, unchanged by this leaf. Classification only:
lane membership is not execution, certification or acceptance evidence.

## 260915-CAPS-L16 Lane Row (Declared)

The L16 change set adds `mcp/tests/test_citation_source_index_membership.py` **and** its row in the same
change, so the manifest stays closed in that change set. The row is
`mcp/tests/test-evidence-lanes.toml:26`, in the **unit-regression** lane, inserted alphabetically
between `test_checkpoint_landing.py` and `test_cli_discovery.py`. That is its behaviour-preserving
lane: the module's seven cases build disposable code roots and drive the real citation source index
in-process — they start no server, launch no process and touch no product surface — so the hermetic
default unit lane is where a previously-unmarked module already ran. **Lane row added; no case added
to any capped population that was not already there.**

Measured at this leaf's synced base `8997e184` **plus** this change set, by counting the manifest's
declared path rows and the modules on disk: **232 declared rows** against **238** `mcp/tests/test_*.py`
modules, so **six** modules remain unregistered — exactly the pre-existing D9 set owned by the
final-verification leaf (`test_eve_adapter.py`, `test_eve_protocol.py`, `test_role_capsule_admission.py`,
`test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`, `test_task_projection.py`). This
leaf closed none of that gap. The lane keys still sit at unit-regression `:5`, public-contract `:143`,
integration `:147`, architecture-fitness `:212`, provider-conformance `:231`, with stress-durability
(`:247`) and migration (`:249`) empty; the one insertion at `:26` pushes every row below it down one
line, so the section immediately above records the previous candidate's row numbering and is that
leaf's as-of record. Classification only: lane membership is not execution, certification or
acceptance evidence.

## 260915-CAPS-L17 Lane Row (Declared)

The L17 change set adds `mcp/tests/test_eve_effort_runtime.py` **and** its row in the same change, so the
manifest stays closed over the modules it declares. The row is
`mcp/tests/test-evidence-lanes.toml:190`, in the **integration** lane, inserted alphabetically between
`test_eve_capsule_runtime.py` (`:189`) and `test_git_command.py` (`:191`). (`:188`/`:187`/`:189` were this
row's position at the L17 change set; `260918-TSIP-L6`'s two insertions moved all three by +2.) That is its
behaviour-preserving lane: each case starts the **real** runtime process with a complete verified capsule
binding, boots a real hermetic Node application and reads the request body a live recording provider
received — so it is a boundary executor, not a hermetic unit. It carries three cases and no `-m`
override; the integration lane is where they belong.

Measured at this change set by deriving the disk file list and the manifest rows and diffing them:
**240** `mcp/tests/test_*.py` modules on disk against **234** declared rows, with **no stale row** (every
declared path exists) and **six** modules unregistered — exactly the pre-existing D9 set owned by the
final-verification leaf (`test_eve_adapter.py`, `test_eve_protocol.py`, `test_role_capsule_admission.py`,
`test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`, `test_task_projection.py`). **This
leaf closed none of that gap** and added no row beyond its own. Lane brackets, by entry row:
unit-regression 137 entries (key `:5`, rows 6-142), public-contract 2 (key `:144`, rows 145-146),
integration 64 (key `:148`, rows 149-212), architecture-fitness 17 (key `:214`, rows 215-231),
provider-conformance 14 (key `:233`, rows 234-247), with stress-durability (`:249`) and migration
(`:251`) empty.

**Recorded, not repaired: D27 lives in one of the six modules above.** The unregistered
`mcp/tests/test_eve_adapter.py` is also the module whose
`EveRegistryTests::test_the_registry_leaves_the_path_harnesses_on_the_ordinary_lookup` asserts an
environment fact another test in the same run can falsify; `AR_EVE_NODE` in the pytest process
environment is the confirmed one-variable trigger. Neither the missing lane row nor the assertion's
shape is this leaf's repair — both are carried with their direction and owner so the next reader finds
attribution rather than an unexplained red.

Classification only: lane membership is not execution, certification or acceptance evidence.

## 260913-LCA-L4 Pending Lane Row (Open At L4, Resolved Since)

**Resolved — see the L5 section below.** At the L4 change set the manifest was one row short.

The L4 change set added `mcp/tests/test_memory_attribution_producers.py` and did **not** register it in
this manifest, so the closed population the `Logic` section below describes does not hold for that
change set. Measured at base `5bb124d4` plus that change set, by diffing the file list against the
manifest:

- 203 `mcp/tests/test_*.py` modules exist on disk; the manifest declares 202 (114 unit-regression, 2
  public-contract, 57 integration, 16 architecture-fitness, 13 provider-conformance, 0 stress-durability,
  0 migration).
- The single undeclared path is `mcp/tests/test_memory_attribution_producers.py` — the one file in the
  disk set with no manifest row — and there is no stale row naming a file that is gone.

This is not a documentation gap but the hard failure this card already records from 260831-LOCR-L30:
`load_lane_manifest` derives the repository's actual test modules and refuses a manifest that omits one.
The derivation reaches the new module — `testpaths = ["mcp/tests"]` in the repository-root
`pyproject.toml:155` puts it inside the test roots, and its `test_` prefix classifies it as a test module
— and `mcp/test_support/agents_remember_test_support/code_quality/check.py:677` is a manifest consumer, so
every consumer fails rather than mis-classifying. The lane the module belongs in is the builder's call and
is **not** asserted here: the module is hermetic except for its two cases that compose `QueueFixture` over
real temporary Git repositories. The row is recorded as pending so the next reader finds the gap rather
than a claim of completeness.

## 260913-LCA-L5 Lane Row (Declared)

**Superseding the L4 section above, the manifest is closed again.** Measured at base `52875e7a` by
diffing the disk file list against the manifest, the L4 module `test_memory_attribution_producers.py`
does have its lane row (line `:68`, `unit-regression`, added by the commit that landed L4), so the
203-modules/203-entries population held at this leaf's base and the open gap the L4 section records is
resolved.

The L5 change set adds `mcp/tests/test_leaf_doc_master_link_binding.py` **and** its row in the same
change, so the population stays closed at 204 modules on disk and 204 manifest entries. The row is
`mcp/tests/test-evidence-lanes.toml:194`, in the **integration** lane: it drives the real public
`worktree_start` over one disposable code repository and one external memory repository per case, so it
is a boundary executor rather than a hermetic unit — that is its behaviour-preserving lane.

Measured current brackets, by entry row: unit-regression 115 entries at rows 6-120, public-contract 2
at 123-124, integration 58 at 127-184, architecture-fitness 16 at 187-202, provider-conformance 13 at
205-217, stress-durability and migration empty. The Purpose paragraph records the current L3
measurement (207 modules, 116 unit-regression, 60 integration), so these L5 brackets are that leaf's
as-of record; the insertion at `:152` shifted every integration entry after it and both later lane
blocks by one.

## 260913-LCA-L7 Lane Row (Declared)

The L7 change set adds `mcp/tests/test_closeout_projection_source_classification.py` **and** its row in
the same change, so the manifest stays closed at 205 modules on disk and 205 manifest entries — the L5
population was 204 and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:176`, in the **integration** lane: the module composes the real
`QueueFixture` over temporary Git repositories and drives the production graph admission and projection
path, so it is a boundary executor rather than a hermetic unit — that is its behaviour-preserving lane.
The manifest is also a fail-closed input here, not a list of cases: `test_closeout_queue.py` is a
one-to-one sidecar source whose card describes a shared fixture with no retained standalone queue tests,
and this new module is a real consumer of that fixture rather than a rename or replacement of it. No
existing row moved and no existing row changed lane: the insertion at `:137` sits inside the
alphabetical integration run and pushes only the later line numbers down by one.

Measured current brackets, by entry row: unit-regression 115 entries at rows 5-120, public-contract 2
at 122-124, integration 59 at 126-185, architecture-fitness 16 at 187-203, provider-conformance 13 at
205-218, stress-durability and migration empty. The Purpose paragraph records the current L3
measurement and the L5 section carries the 204-module brackets; these L7 numbers are that leaf's
as-of record, superseded by the L3 population. The insertion at `:137` sits before entries that this
card cites, so each of those rows is one line higher than the L5 section recorded it:
`test_leaf_doc_master_link_binding.py` `:152` → `:153`, `test_lifecycle_playthrough_end_to_end.py`
`:155` → `:156`, `test_pause_stop_only_end_to_end.py` `:161` → `:162`,
`test_worktree_status_terminal_next_tool.py` `:181` → `:182`, and
`test_pause_is_not_publication.py` `:193` → `:194`; the unit-lane
`test_memory_attribution_producers.py` row at `:68` and every row above the insertion are unchanged.

## 260913-LCA-L8 Lane Row (Declared)

The L8 change set adds `mcp/tests/test_terminal_blocker_reasons.py` **and** its row in the same
change, so the manifest stays closed at 206 modules on disk and 206 manifest entries — the L7
population was 205 and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:219`, in the **integration** lane: the module builds a real landed
leaf over disposable code and external-memory repositories, completes the integration through the
public `worktree_integrate_tool`, and drives the public `lifecycle_finalize_task_tool` plus a real
permission failure on the provider-runtime tree, so it is a boundary executor rather than a hermetic
unit — that is its behaviour-preserving lane.

Measured current brackets, by entry row: unit-regression 115 entries at rows 5-120, public-contract 2
at 122-124, integration 60 at 126-186, architecture-fitness 16 at 188-204, provider-conformance 13 at
206-219, stress-durability and migration empty. The L7 section above carries the 205-module brackets,
which are that leaf's as-of record; the Purpose paragraph carries the current L3 measurement (207
modules, 207 manifest entries), which supersedes these L8 numbers.

The insertion at `:177` also corrects three out-of-order entries that the earlier insertions had left
behind in the closeout-input consumer list: `test_cross_master_concurrency.py` moves after
`test_context_packet.py` (`:309` → `:312`), `test_lifecycle_finalize.py` after
`test_leaf_doc_master_link_binding.py` (`:315` → `:316`) and `test_memory_attribution_producers.py`
after `test_mcp_stdio_transport.py` (`:319` → `:320`). That is why the L5 row moves **up** one line
(`:316` → `:315`) while the L4 row moves down one (`:319` → `:320`). No existing row changed lane. Two
rows this card cites sit after the insertion and are one line higher than the L7 section recorded
them: `test_worktree_status_terminal_next_tool.py` `:182` → `:183` and
`test_pause_is_not_publication.py` `:194` → `:195`; `test_pause_stop_only_end_to_end.py` `:162`, the
playthrough `:156`, the L7 row `:137` and the L4 row's lane are unchanged.

## 260915-CAPS-L5 Lane Row (Declared)

The L5 change set adds `mcp/tests/test_codex_capsule_delivery.py` **and** its row in the same change.
The row is `mcp/tests/test-evidence-lanes.toml:258`, in the **provider-conformance** lane, inserted
alphabetically between `test_codex_app_server_adapter_turns.py` and
`test_harness_control_claude.py`. That is its behaviour-preserving lane: the module's subject is the
vendor app-server's instruction channel — an instruction-channel fixture generated from the installed
`codex-cli 0.151.0` schema, one live native case, and the Codex adapter/session seam — which is exactly
what the sibling `test_codex_app_server_*` modules are classified as. The module carries **28 collected
cases and no `integration` marker**, so nothing here spends integration budget.

**Additive proof, measured by the loader itself.** Before the row the fail-closed loader reported
**7** findings including this module; after it, **6** — and the module is absent from them. No existing
row was edited, reordered or removed.

**Measured population at this candidate.** 216 `mcp/tests/test_*.py` modules on disk, **210** manifest
rows — unit-regression **118**, public-contract 2, integration 60, architecture-fitness 16,
provider-conformance **14**, with stress-durability and migration empty — so **6 modules remain
unregistered**, and they are exactly the pre-existing D9 set owned by the final-verification leaf:
`test_eve_adapter.py`, `test_eve_protocol.py`, `test_role_capsule_admission.py`,
`test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`, `test_task_projection.py`. This leaf
added its own row and **did not** touch the other six; the loader's exact output is the pin.

Classification only: lane membership is not execution or acceptance evidence, and the six D9 rows are
not this leaf's to classify.

## 260915-CAPS-L4 Lane Row (Declared) — And The Unit Population Now Refuses Collection

The L4 change set adds `mcp/tests/test_capsule_serving.py` **and** its row in the same change, so the
manifest stays closed over the modules it declares at **208 rows** — the L3 population plus this one.
The row is `mcp/tests/test-evidence-lanes.toml:19`, in the **unit-regression** lane, inserted
alphabetically between `test_causal_quality_preflight.py` and `test_certification_lane_bridge.py`. That
is its behaviour-preserving lane: 19 of the module's 21 cases are hermetic (a disposable coordination
root and a synthetic skills corpus, no integration marker) and only the two real-process exchanges are
marked `integration`, so the module's default lane is unit-regression and only its two marked items
spend integration budget.

Measured brackets at this leaf, by entry row: unit-regression **117** entries at rows 5-121,
public-contract 2 at 124-126, integration 60 at 128-189, architecture-fitness 16 at 190-207,
provider-conformance 13 at 208-222, with stress-durability (223-224) and migration (225-226) empty. The
Purpose paragraph above carries the L3 measurement (207 modules, 116 unit-regression); these are the
measured L4 numbers and the one addition is this module.

**The unit population now refuses collection on this branch, and this leaf did not cause it.** The
default unit selection collects **1083** cases against `unit_case_budget = 1000`
(`pyproject.toml:149`), and it already collected **1064** against that ceiling at the leaf's base — so
the overage is 83 and **64 of it predates this leaf**. This leaf's contribution is 19 unit cases over
two new public surfaces and it did **not** edit the ceiling, move the module into another lane to dodge
the check, or drop a case. The enforcement point is
`conftest.pytest_collection_finish`, which raises `pytest.UsageError` for the unit population **before
any case executes**, so a default `pytest` run cannot execute on this worktree at all. The integration
population is 227 against its 250 ceiling and is not implicated. This is recorded rather than repaired
because raising a declared case budget requires an explicit change tradeoff and is an owner-level
decision (the leaf's `F-L4-01`, escalated to the master's owning seat; L11 owns the ceiling and the
master-tip overage).

**Six tracked test modules remain undeclared.** The manifest declares 208 rows while **214**
`mcp/tests/test_*.py` modules exist on disk: `test_eve_adapter.py`, `test_eve_protocol.py`,
`test_role_capsule_admission.py`, `test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`
and `test_task_projection.py`. These are the pre-existing master-tip gaps recorded as `D9` in
`notes/product-defects-observed.md` and owned by L11; `load_lane_manifest` names exactly these six and
`test_capsule_serving.py` is **not** among them. This leaf added its own row and deliberately touched no
other entry.

Measured current brackets, by entry row: unit-regression 117 entries at rows 5-121, public-contract 2
at 124-126, integration 60 at 128-189, architecture-fitness 16 at 190-207, provider-conformance 13 at
208-222, stress-durability and migration empty; the one insertion at `:19` moved every cited row below
it one line higher.

## 260831-LOCR-L01 Lane Row (Declared)

The LOCR-L01 change set adds `mcp/tests/test_serving_observation_loop.py` **and** its row in the same
change, so the manifest stays closed in that change set — the L3 population was 207 modules and 207
entries, and this is the one addition. The row is `mcp/tests/test-evidence-lanes.toml:98`, in the
**unit-regression** lane: the module injects fakes, issues no HTTP request, starts no process and
publishes nothing, so it is a hermetic unit rather than a boundary executor — that is its
behaviour-preserving lane.

The insertion sits inside the alphabetical unit-regression run, between
`test_semantic_topology_refusals.py` and `test_signal_routing.py`, so every entry below it and every
later lane key is one line higher than the L3 entry recorded, and the Purpose paragraph's
207-modules/207-entries / 116-unit-regression figures are that L3 measurement rather than this one.
The read-only bounds in this paragraph are that leaf's as-of record: L27's own insertion at `:182`
moved the later **file lines** again. The `## 260831-LOCR-L27 Lane Row (Declared)` section below
carries the measurement that includes both insertions. Classification only: lane membership is not
execution or acceptance evidence, and the verification stamps remain closeout-owned.

## 260831-LOCR-L27 Lane Row (Declared)

The L27 change set adds `mcp/tests/test_terminal_liveness_pane_authority.py` **and** its row in the
same change, so the manifest stays closed in that change set — the L23 population was 208 modules and
208 entries, and further unit-lane rows arrived from L01 and L10 before this leaf settled. At base
`52bee429` **plus** this change set the manifest holds 211 modules on disk and 211 manifest entries.
The row is `mcp/tests/test-evidence-lanes.toml:219`, in the **integration** lane, between
`test_terminal_liveness.py` at `:218` and `test_tools.py` at `:220`.

That is its behaviour-preserving lane even though the module is hermetic (temporary catalogs,
in-process `unittest`, no `worktree_services`): it is registered exactly as its sibling
`test_terminal_liveness.py` is at `:218`, and a new module in this family needs a row or its
application imports run inside ordinary unit collection. The module is the first member of that
family to be **added** rather than extended — an in-place extension of `test_terminal_liveness.py`
reached the coding-guidelines 900-1200 band, so the proof was split out instead and the sibling stayed
byte-unchanged. **Line-number discipline for this row:** it sat at `:181` on this candidate's own
build base `b368b661`, at `:182` on base `163ba8a9` plus this change set, and at `:183` at base
`52bee429` plus this change set. The verdict and worker report cite `:181`; every later figure is a
base effect from sibling unit-lane insertions, not a change to this leaf's delta, which is always
exactly one inserted row.

Measured current membership at base `52bee429` **plus** this change set: unit-regression 119 entries,
its key at `:5` and the next key at `:126`; public-contract 2 (key `:126`); integration **61** (key
`:130`); architecture-fitness 16 (key `:193`); provider-conformance 13 (key `:211`); stress-durability
(`:226`) and migration (`:228`) empty. This module is entry ordinal **53 of 61** in the integration
lane. No existing row changed lane and no case budget was raised; the integration ceiling stays 250
(`pyproject.toml:150`). Classification only: lane membership is not execution, certification or
acceptance evidence.

## 260831-LOCR-L17 Lane Row (Declared)

The L17 change set adds `mcp/tests/test_terminal_observer_health.py` **and** its row in the same
change, so the manifest stays closed in that change set — the population at base `99534dc5` alone was
213 modules and 213 entries, and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:123`, in the **unit-regression** lane, immediately below
`test_terminal_liveness_registration_order.py` at `:121` and above `test_terminal_paste.py` at `:123`.
The module drives the record, the writer, the accumulator, and the real `_state_response` handler and
`stream_events` generator against stub projectors — it issues no HTTP request, starts no server and
starts no process — so the hermetic default unit lane is its behaviour-preserving classification. The
route half deliberately avoids an ASGI app: the integration population has only three cases of
headroom against its 250-case cap and the brief forbids raising it, so the production handler and
generator are called directly instead.

Measured at base `99534dc5` **plus** this change set, by diffing the disk file list against the
manifest and by bracket position: **214** `mcp/tests/test_*.py` modules on disk and **214** manifest
entries — unit-regression **121** entries (key `:5`, rows 6-126, next key `:128`), public-contract 2
(key `:128`, rows 129-130), integration **62** (key `:132`, rows 133-194), architecture-fitness 16
(key `:196`, rows 197-212), provider-conformance 13 (key `:214`, rows 215-227), with stress-durability
(`:229`) and migration (`:231`) empty. No existing row changed lane and no case budget was raised; the
integration ceiling stays 250 (`pyproject.toml:150`). The insertion sits inside the alphabetical
unit-regression run, so it moves the later lane keys, not the rows above it — in particular
`test_serving_observation_loop.py` stays at `:97` and `test_serving_startup_prime.py` at `:98`, so
**`LOCR-R11@v1`'s and `LOCR-R18@v1`'s classifications are untouched by this leaf**. Classification
only: lane membership is not execution, certification or acceptance evidence, and the verification
stamps remain closeout-owned.

## 260831-LOCR-L18 Lane Row (Declared)

The L18 change set adds `mcp/tests/test_serving_startup_prime.py` **and** its row in the same change,
so the manifest stays closed in that change set — the population at base `d868486c` alone was 212
modules and 212 entries, and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:99`, in the **unit-regression** lane, immediately below its
sibling `test_serving_observation_loop.py` at `:97` and above `test_signal_routing.py` at `:99`. The
module drives the real `_serving_lifespan` under a temporary catalog, a virtual event-loop clock, an
in-process fake tmux host and parked sibling loops — it issues no HTTP request, starts no process and
publishes nothing — so the hermetic default unit lane is its behaviour-preserving classification, the
same lane its sibling already holds for the same reason.

Measured at base `d868486c` **plus** this change set, by diffing the disk file list against the
manifest and by bracket position: **213** `mcp/tests/test_*.py` modules on disk and **213** manifest
entries — unit-regression **120** entries (key `:5`, bracket `:5-125`, next key `:127`),
public-contract 2 (`:127`), integration **62** (key `:131`, bracket `:131-193`), architecture-fitness
16 (`:195`), provider-conformance 13 (`:213`), with stress-durability (`:228`) and migration (`:230`)
empty. No existing row changed lane and no case budget was raised; the integration ceiling stays 250
(`pyproject.toml:150`). The insertion sits inside the alphabetical unit-regression run, so it moves
the later lane keys, not the rows above it. Classification only: lane membership is not execution,
certification or acceptance evidence, and the verification stamps remain closeout-owned.

## 260831-LOCR-L06 Lane Row (Declared)

The L06 change set adds `mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py` **and** its row
in the same change, so the manifest stays closed in that change set. The row is
`mcp/tests/test-evidence-lanes.toml:68`, in the **unit-regression** lane, immediately below
`test_lifecycle_operation_model_helpers.py` at `:67` and above `test_memory_attribution_producers.py`
at `:69`. The module drives the real `TerminalCatalogLivenessSweeper` over a real `TerminalCatalog`
with a scripted single-seat adapter endpoint, hands the resulting native page to the production lift
(`latest_native_terminal_evidence`), and then drives the real `run_agent_notifier_sweep` to persist
the durable row — it issues no HTTP request, starts no server and starts no process, and its only
durable write is the ordinary inbox row under test — so the hermetic default unit lane is its
behaviour-preserving classification.

Measured at pair code base `e9678c56` (which already carries L17's landed row) **plus** this change
set, by diffing the disk file list against the manifest and by bracket position: **215**
`mcp/tests/test_*.py` modules on disk and **215** manifest entries, every module listed exactly once
and no path duplicated — unit-regression **122** entries (key `:5`, rows 6-127, next key `:129`),
public-contract 2 (key `:129`, rows 130-131), integration **62** (key `:133`, rows 134-195),
architecture-fitness 16 (key `:197`, rows 198-213), provider-conformance 13 (key `:215`, rows 216-228),
with stress-durability (`:230`) and migration (`:232`) empty. No existing row changed lane and no case
budget was raised; the declared case budgets live in `pyproject.toml`, which is the authority for
them. The insertion sits inside the alphabetical unit-regression run and below every row this card
cites from `LOCR-R09@v1`, `LOCR-R11@v1`, `LOCR-R18@v1` and the L17 observer-health proof, so those
classifications are untouched by this leaf — it moves the later lane keys and the rows at or below
`:68`, which is why every affected citation in this card and in `overview.md` was re-derived against
the candidate rather than carried.

Scope note: this leaf is a **preservation leaf** — `mcp/src` is byte-unchanged by it (`git status
--porcelain` = ` M mcp/tests/test-evidence-lanes.toml` plus the untracked module; `mcp/src` diff = 0
files), and the module's digest, line count and lane ordinal are measurements of an uncommitted,
unaccepted tree. Classification only: lane membership is not execution, certification or acceptance
evidence, and the verification stamps remain closeout-owned.

## 260831-LOCR-L05 Lane Row (Declared)

The L05 change set adds `mcp/tests/test_state_signal_worker_wake.py` **and** its row in the same
change, so the manifest stays closed in that change set. The row is
`mcp/tests/test-evidence-lanes.toml:105`, in the **unit-regression** lane, immediately below
`test_state_signal_restart_recovery.py` at `:104` and above `test_structural_dispatch_recovery.py`
at `:106`. The module seeds owned worker and manager seats on a real `TerminalCatalog`, drives the
real `run_agent_notifier_sweep` over a temporary coordination root with real task documents, a real
inbox log and the real durable stores, and asserts the whole inbox store rather than its state-signal
subset — it issues no HTTP request, starts no server and starts no process, and its only durable write
is the ordinary inbox row under test — so the hermetic default unit lane is its behaviour-preserving
classification.

Measured at pair code base `67c91534` (which already carries `260831-LOCR-L06`'s landed row) **plus**
this change set, by diffing the disk file list against the manifest and by bracket position: **216**
`mcp/tests/test_*.py` modules on disk and **216** manifest entries, every module listed exactly once
and no path duplicated — unit-regression **123** entries (key `:5`, rows 6-128, next key `:130`),
public-contract 2 (key `:130`, rows 131-132), integration **62** (key `:134`, rows 135-196),
architecture-fitness 16 (key `:198`, rows 199-214), provider-conformance 13 (key `:216`, rows 217-229),
with stress-durability (`:231`) and migration (`:233`) empty. The population is closed and the
fail-closed load holds: the live test-module derivation and the manifest agree module for module, so
no unregistered module can make `load_lane_manifest` refuse. No existing row changed lane and no case
budget was raised; the declared case budgets live in `pyproject.toml`, which is the authority for
them. The insertion sits inside the alphabetical unit-regression run and above every row this card
cites from `LOCR-R09@v1`, `LOCR-R11@v1`, `LOCR-R18@v1`, the L17 observer-health proof and the L06
reviewer-relay proof, so those classifications are untouched by this leaf — it moves the later lane
keys and the rows at or below `:105`, which is why every affected citation in this card and in
`overview.md` was re-derived against the candidate rather than carried.

Scope note: this leaf is a **preservation leaf** — `mcp/src` is byte-unchanged by it (`git status
--porcelain` = ` M mcp/tests/test-evidence-lanes.toml` plus the untracked module; `mcp/src` diff = 0
files), and the module's digest, line count and lane ordinal are measurements of an uncommitted,
unaccepted tree. Classification only: lane membership is not execution, certification or acceptance
evidence, and the verification stamps remain closeout-owned.
## 260831-LOCR-L04 Lane Row (Declared)

The L04 change set adds `mcp/tests/test_serving_notifier_handoff.py` **and** its row in the same change,
so the manifest stays closed in that change set — the population at base `e9678c56` alone was 214 modules
and 214 manifest entries (L17's own row already landed there at `:122`), and this is the one addition. The
row is `mcp/tests/test-evidence-lanes.toml:97`, in the **unit-regression** lane, immediately below
`test_semantic_topology_refusals.py` at `:96` and above `test_serving_observation_loop.py` at `:98`. The
module enters the real `_serving_lifespan` under a deadline-correct virtual clock and drives the real
observation loop, the real sweeper, the real catalog commit boundary and the real notifier sweep — it
issues no HTTP request, starts no server and starts no process, and publishes nothing outside a
disposable `tempfile` case root — so the hermetic default unit lane is its behaviour-preserving
classification.

The leaf's two **support** modules, `mcp/tests/_handoff_clock.py` and `mcp/tests/_serving_handoff.py`, take
no lane row: the manifest classifies `test_*.py` modules, and this is the same treatment the directory's
other support modules receive (`_store_durability.py`, `_quality_admission.py`, `_control_plane.py` and
their siblings are absent from the manifest by the same rule). Their onboarding is the pair of file cards
created with this row.

Measured at base `e9678c56` **plus** this change set, by diffing the disk file list against the manifest
and by bracket position: **215** `mcp/tests/test_*.py` modules on disk and **215** manifest entries —
unit-regression **122** entries (key `:5`, rows 6-127, next key `:129`), public-contract 2 (key `:129`,
rows 130-131), integration **62** (key `:133`, rows 134-195), architecture-fitness 16 (key `:197`, rows
198-213), provider-conformance 13 (key `:215`, rows 216-228), with stress-durability (`:230`) and
migration (`:232`) empty. No existing row changed lane and no case budget was raised or is quoted here:
`pyproject.toml` is the authority for the declared budgets, and this leaf adds no collected case to any
capped population.

**This insertion is above the previously-latest unit rows, so it moves rows rather than sitting below
them.** Every manifest line at or after `:97` shifts by one: `test_serving_observation_loop.py` `:97` →
`:98`, `test_serving_startup_prime.py` `:98` → `:99`, L17's `test_terminal_observer_health.py` `:122` →
`:123`, and every later lane key with them. The citations into the manifest were therefore **re-derived
against the current file rather than carried**: 59 live citations across this card, the tests route
overview and fifteen sibling cards were re-pointed to the line that actually carries their anchor, and
the dated `## KS-R15@v1 Lane Registrations

The leaf's two new modules are registered here: the unit module `mcp/tests/test_review_assessments.py`
in the **unit-regression** lane, and the integration module
`mcp/tests/test_curator_review_assessment_publication.py` in the **integration** lane. Both rows were
inserted at the head of their lane's list, which is why **every cited row number below the insertion
points in this card moved** — the offsets are +1 for rows after the unit insertion and the integration
insertion, and the card's own reference rows were re-derived from the current file while re-reading it
rather than left at their pre-leaf coordinates.

Every other lane row in this card that cites this file was re-pointed in the same pass, because the
regenerated table below would otherwise describe a file that no longer exists in that shape. No lane
was added, removed, renamed or re-classified: the leaf registers two modules in the lanes their
behaviour already belongs to.

## Update History` entries — as-of records of earlier candidates — were deliberately left as

the dated `## Update History
- 2026-09-18T17:02+02:00 — 260918-TSIP-L4 curator (uncommitted change set on `ar/260918-tsip-l4-ar`, base `0dd04d6a`): two rows added (`:165`, `:244`), 267 → 269 lines, and the citations the insertion moved re-derived by enumeration rather than from the finding set. Verification metadata stays at the recorded verification because the candidate is uncommitted and the governed closeout owns the real code commit; `lastUpdated` advances with this body edit.

- 2026-09-17T10:45+02:00 — 260915-CAPS-L15 curator: the manifest gained one row for this leaf's own new
  module, `mcp/tests/test_capsule_launch_wiring.py`, at `:19` in the **unit-regression** lane — its
  behaviour-preserving lane, since the module drives the launch points, the real runner preparation and
  the real adapter factory in process with the vendor boundary recorded and no real process started. A
  declared section records the row, its insertion point and the D9 rule it satisfies in the same change
  that adds the module. No row was removed, moved between lanes, or added to a capped population beyond
  the one module's own. Verification metadata moves to this leaf's base `15fa0e2c`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.

- 2026-09-17T10:43+02:00 — 260915-CAPS-L17 curator: the manifest gained one row for this leaf's own new
  module, `mcp/tests/test_eve_effort_runtime.py`, at `:173` in the **integration** lane — its
  behaviour-preserving lane, since each case starts the real runtime process with a complete verified
  capsule binding and reads the body a live recording provider received. A declared section records the
  row, its insertion point, the measured population at this change set (**240** modules on disk, **234**
  declared rows, no stale row, the same six pre-existing D9 modules unregistered, this leaf closing none
  of that gap) and the D27 note that one of those six is also the environment-sensitive registry case —
  carried with its confirmed `AR_EVE_NODE` trigger and its repair direction, **not repaired here**. No
  row was removed, moved between lanes, or added to a capped population beyond this module's own.
  **Checker result (post-sync, verbatim).** The refusal this entry first recorded was resolved by the
  leaf's `worktree_sync`: the pair is now `leaf-candidate` / `acceptanceEligible:true` on code base
  `d8ed8c21`, and the contract-scoped `memory_quality_check` ran against this worktree. Headline:
  `ok:false`, `checklistStatus:"action-required"`,
  `coherenceStatus:"not-evaluated-quality-action-required"`, `closeoutReady:false`,
  `curatorActionableCount:1690`; census `ready-for-adjudication` (13 rows, 0 blockers, 0 unonboarded).
  This card's own contribution: one `onboarding_drift_drifted` finding and two
  `style.update_history.history_order` "not newest-first" findings, attributable to the future-dated
  `10:45` stamp on the L15 entry below this one (same reasoning as the `serving/overview.md` entry). The
  population figures in this section were also derived directly from the manifest and the disk file
  list, independently of the checker. Verification metadata moves to the synced base `d8ed8c21`; the
  candidate is deliberately uncommitted, so the governed closeout stamps the real code commit and no
  hash or fingerprint was invented here.
Verification metadata moves to the synced base `d8ed8c21`; the candidate is deliberately uncommitted, so
the governed closeout stamps the real code commit and no hash or fingerprint was invented here.

` entries — as-of records of earlier candidates — were deliberately left as
written. One citation was corrected beyond the shift because it was already stale before this leaf
(`test_checkpoint_landing_end_to_end.py`, cited at `:143-143`, which the manifest carries at `:140`).
Classification only: lane membership is not execution, certification or acceptance evidence, and the
verification stamps remain closeout-owned.

The leaf is a **preservation** requirement — `LOCR-R04@v1` requires zero production change — so the
manifest's only movement is this one row; `mcp/src` is byte-unchanged by the change set.

## 260831-LOCR-L07 Lane Row (Declared)

The L07 change set adds `mcp/tests/test_state_signal_curator_wake.py` **and** its row in the same
change, so the manifest stays closed in that change set — the population at base `e9678c56` alone is
214 modules and 214 manifest entries, and this is the one addition. The row is
`mcp/tests/test-evidence-lanes.toml:102`, in the **unit-regression** lane, immediately below
`test_state_signal_boundary_delivery.py` at `:101` and above `test_state_signal_relay.py` at `:103`,
so the state-signal siblings stay one contiguous alphabetical run. The module drives the real
`TerminalCatalogLivenessSweeper`, the real agent-notifier sweep and the real `run_agent_notifier_sweep`
entry point over temporary catalogs, an in-process tmux host and an accepting paster double — it
issues no HTTP request, starts no server and starts no process — so the hermetic default unit lane is
its behaviour-preserving classification, the same lane its three siblings already hold for the same
reason. This is a preservation leaf: `mcp/src` is unchanged by the change set, and the row is
registration only.

Measured at base `e9678c56` **plus** this change set, by diffing the disk file list against the
manifest and by bracket position: **215** `mcp/tests/test_*.py` modules on disk and **215** manifest
entries — unit-regression **122** entries (key `:5`, bracket `:5-127`), public-contract 2 (key
`:129`, rows 130-131), integration **62** (key `:133`, bracket `:134-195`), architecture-fitness 16
(key `:197`, rows 198-213), provider-conformance 13 (key `:215`, rows 216-228), with
stress-durability (`:230`) and migration (`:232`) empty. No existing row changed lane and no case
budget was raised; `pyproject.toml` remains the authority for the pinned budgets. The insertion sits
inside the alphabetical unit-regression run above every later lane key, so it moves the later lane
keys and every row this card cites from `:102` down by one, while every row at `:101` and above is
unchanged — including `test_serving_observation_loop.py` (`:97`) and
`test_serving_startup_prime.py` (`:98`), so `LOCR-R11@v1`'s and `LOCR-R18@v1`'s classifications are
untouched by this leaf. Classification only: lane membership is not execution, certification or
acceptance evidence, and the verification stamps remain closeout-owned.

## Code Commentary

### Logic

Paths are explicit and unique. The root conftest reads integration/stress membership once to avoid
integration imports in default unit runs and marks selected integration items. The
`test_terminal_evidence_cursors.py` row owns the focused deque-envelope, unsupported-harness,
bounded-Pi, and liveness-containment checks for the terminal-evidence lift. Other categories
retain their classification meaning without requiring separate copies or historical edge suites.
A test-shaped helper module may remain listed for dependency classification even when it contains
no test functions; importability is not a passing test.

`load_lane_manifest` independently proves the declared population closed: it derives the
repository's actual test modules and refuses a manifest that omits a module or declares a stale
row, so an unregistered module is a hard load failure rather than a silent gap. Three modules
created by the CCR transaction-only closeout reform (`test_review_state.py`,
`test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`) were left
unregistered by the commit that created them, and the checking hooks that would have caught the
omission were later removed from closeout, so the gap survived until the manifest was explicitly
repaired. All three are registered as `unit-regression`, which is behaviour-preserving: they had
been running unmarked and therefore already counted as unit, and the integration lane sat at its
hard cap of 150 collected cases, so an `integration` row would have overflowed the cap and raised
during collection. Registration here is classification only; it is never execution or acceptance
evidence.

`test_dagger_registry_lock.py`, the registered activation/admission proof, the registered
route-review transport proof, and actual document/publication/durability boundaries are integration
members. The R28 `test_terminal_liveness_deferred_work.py` module is a unit-regression member: it is
hermetic (temporary catalogs, in-process `unittest` classes, no `worktree_services` use) even though
it exercises the real catalog/sweeper post-commit ordering and failure boundaries. The new diagnostic
quality, selected-case-budget and canonical terminal-evidence mapping tests are unit-regression members,
as is `test_sync_parked_candidate.py`. Three pre-existing CCR modules (`test_review_state.py`,
`test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`) were created by `8885939e`
in the same change that edited this manifest, but their required rows were omitted; the missing
`unit-regression` rows were restored so the manifest loads and no retained module stays unclassified.
A full run previously collected all three unmarked, so `unit-regression` is their behaviour-preserving
lane. Adding the parked-candidate row shifted every later lane block, so its citations were re-derived.
The executable case budgets live in pyproject/conftest, not in this list. Coverage percentages are
diagnostic and cannot require restoring deleted entries.

The current manifest is complete and duplicate-free: every `mcp/tests/test_*.py` module on disk is
listed exactly once, and every listed path exists. Three formerly unlisted modules
(`test_review_state.py`, `test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`)
were created by the CCR transaction-only delivery commit and omitted from this manifest in the same
change; they ran unmarked rather than in an explicit lane. They are registered in `unit-regression`,
which is the behaviour-preserving lane for an unmarked module, because moving them to `integration`
would push that lane past its 150-case cap. The same three rows also reached this series branch with
the LOCR-L28 landing. That repair is repo-hygiene and is not part of any LOCR requirement.

`test_cross_master_concurrency.py` (260831-LOCR-L36) is an **integration** member, and that is its
behaviour-preserving lane: it builds one real temporary Git world per case — disposable code and
external-memory repositories, real series/leaf contracts, a real ledger — and drives the public
activation, checkpoint-landing and integration operations against it, so it is a boundary executor
rather than a hermetic unit. It is the forcing module for the contract-scoped activation record: two
atomic masters commanded by one sprint share one protected source pair, so the module can prove both
progress independently and that a sibling's pause blocks nobody. Registration is classification only;
it is never execution or acceptance evidence.

`test_terminal_liveness_registration_order.py` (260831-LOCR-L23) is a **unit-regression** member, and
that is its behaviour-preserving lane: it drives the real `TerminalCatalog` over `tempfile` catalogs
and the real `TerminalCatalogLivenessSweeper.refresh` with in-process `unittest` doubles for the
registrar and the compactor, so it is hermetic — no `worktree_services`, no real repository, no
provider — despite exercising the catalog batch, the terminated-row read and the retention predicate.
It is registered at entry row 118, immediately after its sibling
`test_terminal_liveness_deferred_work.py` at `:117`, which holds the same lane for the same reason.
Registration is classification only; it is never execution or acceptance evidence.

### Invariants And Boundaries

- Unknown, duplicate or conflicting file classification must not silently acquire authority.
- Every current `mcp/tests/test_*.py` module holds exactly one explicit lane; an unlisted module is a
  manifest defect, and its behaviour-preserving lane is the default unit lane rather than the capped
  integration lane.
- Evidence class is separate from whether a test invokes a real external producer.
- Current source membership governs; old final-Codex executor/status-wait/deleted-edge lists do not.
- Host development pytest is supported; only explicit certification requires Dagger admission.
- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 1000 at `pyproject.toml:185`, `integration_case_budget` **300** at `pyproject.toml:186`; the 150, 200 and 250 values in earlier entries of this card are stale). **That pair is a historical reading of this card's own, retained as the state it measured; the pair the file declares now is `unit_case_budget = 2300` at `pyproject.toml:244` and `integration_case_budget = 400` at `pyproject.toml:245`.** A module that was previously running unmarked already spends unit budget, so registering it as `unit-regression` preserves behaviour; moving it into `integration` can push full-suite collection past the integration cap and fail collection outright. Classification cannot be chosen for semantic tidiness alone.
- Full suites and whole-candidate review occur at master completion, not once for every lane or leaf.
- Lane membership must keep each collected population inside its declared case budget: `unit_case_budget` 1000 and `integration_case_budget` **300** (root `pyproject.toml:185-186`) **at that earlier candidate** — the file now declares `unit_case_budget = 2300` (`pyproject.toml:244`) and `integration_case_budget = 400` (`pyproject.toml:245`) — enforced in `pytest_collection_finish`. A module that a full run previously collected unmarked - and therefore already counted as unit - belongs in `unit-regression`; moving it to `integration` can refuse collection.

- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 1500, `integration_case_budget` 250 — `pyproject.toml:158-159`; the 150/200/1000 values in earlier entries of this card are stale) **as that candidate read them. The pair declared now is `unit_case_budget = 2300` (`pyproject.toml:244`) and `integration_case_budget = 400` (`pyproject.toml:245`).** **The unit ceiling was raised from 1000 to 1500 by 260915-CAPS-L8, executing the developer's ruling**, because the default selection had outgrown 1000 and so refused collection before any case ran; the raise restored a working default selection and is a ceiling rather than a target. A module that was previously running unmarked already spends unit budget, so registering it as `unit-regression` preserves behaviour; moving it into `integration` can push full-suite collection past the integration cap and fail collection outright. Classification cannot be chosen for semantic tidiness alone.
- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 2000, `integration_case_budget` 300 — `pyproject.toml:168-176`; the 150/200/250/1000/1500 values in earlier entries of this card are stale). **Every figure in this card is measured against the leaf's base ceiling (2000/300); the merged line this leaf syncs onto raises both to 2300/400 (`T79`), so the two ceilings must not be quoted interchangeably.** **The unit ceiling was raised from 1000 to 1500 by 260915-CAPS-L8, executing the developer's ruling**, because the default selection had outgrown 1000 and so refused collection before any case ran; the raise restored a working default selection and is a ceiling rather than a target. A module that was previously running unmarked already spends unit budget, so registering it as `unit-regression` preserves behaviour; moving it into `integration` can push full-suite collection past the integration cap and fail collection outright. Classification cannot be chosen for semantic tidiness alone.
- Full suites and whole-candidate review occur at master completion, not once for every lane or leaf.
- Lane membership must keep each collected population inside its declared case budget: `unit_case_budget` 1000 and `integration_case_budget` **300** (root `pyproject.toml:185-186`) **at that earlier candidate** — the file now declares `unit_case_budget = 2300` (`pyproject.toml:244`) and `integration_case_budget = 400` (`pyproject.toml:245`) — enforced in `pytest_collection_finish`. A module that a full run previously collected unmarked - and therefore already counted as unit - belongs in `unit-regression`; moving it to `integration` can refuse collection.

- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 1500, `integration_case_budget` 250 — `pyproject.toml:158-159`; the 150/200/1000 values in earlier entries of this card are stale) **as that candidate read them. The pair declared now is `unit_case_budget = 2300` (`pyproject.toml:244`) and `integration_case_budget = 400` (`pyproject.toml:245`).** **The unit ceiling was raised from 1000 to 1500 by 260915-CAPS-L8, executing the developer's ruling**, because the default selection had outgrown 1000 and so refused collection before any case ran; the raise restored a working default selection and is a ceiling rather than a target. A module that was previously running unmarked already spends unit budget, so registering it as `unit-regression` preserves behaviour; moving it into `integration` can push full-suite collection past the integration cap and fail collection outright. Classification cannot be chosen for semantic tidiness alone.
- Full suites and whole-candidate review occur at master completion, not once for every lane or leaf.
- Lane membership must keep each collected population inside its declared case budget: `unit_case_budget` 1500 and `integration_case_budget` 250 (root `pyproject.toml:158-159`) **at that earlier candidate — the declaration now reads `unit_case_budget = 2300` (`pyproject.toml:244`) and `integration_case_budget = 400` (`pyproject.toml:245`)**, enforced in `pytest_collection_finish`. A module that a full run previously collected unmarked - and therefore already counted as unit - belongs in `unit-regression`; moving it to `integration` can refuse collection.
- Lane membership is additionally bounded by the declared collected-case budgets (`unit_case_budget` 2000, `integration_case_budget` 300 — `pyproject.toml:168-176`; the 150/200/250/1000/1500 values in earlier entries of this card are stale) **as that candidate read them. The pair declared now is `unit_case_budget = 2300` (`pyproject.toml:244`) and `integration_case_budget = 400` (`pyproject.toml:245`).**

## Docs References

No external Domain Documentation source is configured; these are repository-owned implementation facts.

## Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Retained unit-regression membership, including the R28 deferred-work and canonical terminal-evidence mapping proofs | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-198 |
| Small actual integration file population | `integration` | mcp/tests/test-evidence-lanes.toml:203-279 |
| Retained structural detector classifications | "architecture-fitness" | mcp/tests/test-evidence-lanes.toml:280-301 |
| Provider contract classifications | "provider-conformance" | mcp/tests/test-evidence-lanes.toml:302-317 |
| Empty former stress/migration populations, in the manifest's two remaining empty lanes | "stress-durability"; "migration" | mcp/tests/test-evidence-lanes.toml:318-322; mcp/tests/test-evidence-lanes.toml:320-321 |
| L38 registered public activation/admission and route-review transport ownership | `integration` | mcp/tests/test-evidence-lanes.toml:203-279 |
| The new parked-candidate suite is registered in the unit-regression lane. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-198 |
| The manifest still has no default classification for an unregistered test file. | "stress-durability" | mcp/tests/test-evidence-lanes.toml:318-320 |
| LOCR-L09 boundary-delivery forcing module registered in the unit lane | "mcp/tests/test_state_signal_boundary_delivery.py" | mcp/tests/test-evidence-lanes.toml:159-159 |
| The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. | "mcp/tests/test_checkpoint_landing.py" | mcp/tests/test-evidence-lanes.toml:29-29 |
| The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 272 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_worktree_status_terminal_next_tool.py" | mcp/tests/test-evidence-lanes.toml:274-274 |
| The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 218 now, after the L4, L5, L7, L8 and L3 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:220-220 |
| The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 230 now, after the L4, L5, L7, L8 and L3 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:232-232 |
| The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 249 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 289 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:291-291 |
| The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 243 now, after the L4, L5, L7, L8 and L3 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:245-245 |
| The L4 producer-census suite is registered in the unit-regression lane by the commit that landed L4, closing the gap the L4 section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:117-117 |
| The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 240 now, after the L7, L8 and L3 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:242-242 |
| The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 222 now, after the L8 and L3 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:224-224 |
| The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 insertion) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:267-267 |
| The L2 knowledge graph suite is registered in the unit-regression lane by the same change set that created it (entry rows 69-73) — all four modules are hermetic (temporary directories, in-process APSW databases, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. | "mcp/tests/test_knowledge_family_revision.py"; "mcp/tests/test_knowledge_graph_reads.py"; "mcp/tests/test_knowledge_relation_rules.py"; "mcp/tests/test_knowledge_revision_seals.py"; "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:97-97; mcp/tests/test-evidence-lanes.toml:99-99; mcp/tests/test-evidence-lanes.toml:108-108; mcp/tests/test-evidence-lanes.toml:109-109; mcp/tests/test-evidence-lanes.toml:118-118 |
| The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. | "mcp/tests/test_knowledge_family_revision.py"; "mcp/tests/test_knowledge_graph_reads.py"; "mcp/tests/test_knowledge_relation_rules.py"; "mcp/tests/test_knowledge_revision_seals.py"; "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:97-97; mcp/tests/test-evidence-lanes.toml:99-99; mcp/tests/test-evidence-lanes.toml:108-108; mcp/tests/test-evidence-lanes.toml:109-109; mcp/tests/test-evidence-lanes.toml:118-118 |
| The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 insertion) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:267-267 |
| The L2 knowledge graph suite is registered in the unit-regression lane by the same change set that created it (entry rows 69-73) — all four modules are hermetic (temporary directories, in-process APSW databases, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. | "mcp/tests/test_knowledge_family_revision.py"; "mcp/tests/test_knowledge_graph_reads.py"; "mcp/tests/test_knowledge_relation_rules.py"; "mcp/tests/test_knowledge_revision_seals.py" | mcp/tests/test-evidence-lanes.toml:97-97; mcp/tests/test-evidence-lanes.toml:99-99; mcp/tests/test-evidence-lanes.toml:108-108; mcp/tests/test-evidence-lanes.toml:109-109 |
| The L3 candidate-batch pair and the label-operations suite are registered in the unit-regression lane by the same change set that created them (entry rows 18-19, and row 71 now after the L4 insertions) — all three are hermetic (temporary directories, in-process APSW databases driven through the real admitted destination, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. | "mcp/tests/test_candidate_batch_commands.py"; "mcp/tests/test_candidate_batch_transaction.py"; "mcp/tests/test_knowledge_label_operations.py" | mcp/tests/test-evidence-lanes.toml:18-18; mcp/tests/test-evidence-lanes.toml:19-19; mcp/tests/test-evidence-lanes.toml:98-98 |
| The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (row 118 now, after the L4 insertions) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:118-118 |
| **The L4 snapshot pair is registered in the unit-regression lane by the same change set that created them (rows 69 and 75)** — both modules are hermetic: temporary directories under `tmp_path`, in-process APSW databases driven through the real admitted destination and the real publication lock, and a child interpreter used only as a crash probe, with no integration marker, no repository working tree and no network. | "mcp/tests/test_knowledge_candidate_workspace.py"; "mcp/tests/test_knowledge_snapshot_publication.py" | mcp/tests/test-evidence-lanes.toml:83-83; mcp/tests/test-evidence-lanes.toml:111-111 |
| **The knowledge block's current membership across all four KS leaves**, whose insertion order is why the rows are not contiguous by leaf. | "mcp/tests/test_knowledge_store.py" | mcp/tests/test-evidence-lanes.toml:112-112 |
| **The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value — raised to 400 by this master's owning seat at the `260915-KS-L24` candidate, not by this leaf's fix round, and still 400 on this candidate.** | "integration_case_budget = 400" | pyproject.toml:245-245 |
| **The unit ceiling, cited as the pinned key and value — raised to 1500 at the `260915-KS-L24` candidate, again to 1600 by that candidate's owning seat, again to 2200 by the merge onto the moved super line, and now to 2300 by `260915-KS-L21`, because an over-budget population makes `pytest_collection_finish` raise `UsageError` and run no tests at all. Every earlier value is retained as the ruling that produced it.** | "unit_case_budget = 2300" | pyproject.toml:244-244 |
| **The two lane rows this leaf registered in the same change, both in `integration` because the unit population sits exactly at its declared ceiling.** | "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" | mcp/tests/test-evidence-lanes.toml:207-209 ; mcp/tests/test-evidence-lanes.toml:206-209|
| The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. | `load_lane_manifest` | mcp/test_support/agents_remember_test_support/testing/lane_manifest.py:99-144 |
| Retained unit-regression membership, including the R28 deferred-work, canonical terminal-evidence mapping and L23 registration-order proofs | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-198 |
| The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 272 now, after the L4, seal-removal, L5, L7, L8, L3, L01 and L17 insertions). | "mcp/tests/test_worktree_status_terminal_next_tool.py" | mcp/tests/test-evidence-lanes.toml:274-274 |
| The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 218 now, after the L4, L5, L7, L8, L3 and L01 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:220-220 |
| The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 230 now, after the L4, L5, L7, L8, L3 and L01 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:232-232 |
| The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 249 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 insertions). | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 289 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 insertions). | "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:291-291 |
| The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 243 now, after the L4, L5, L7, L8, L3 and L01 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:245-245 |
| The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 240 now, after the L7, L8, L3 and L01 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:242-242 |
| The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 222 now, after the L8, L3 and L01 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:224-224 |
| The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 and L01 insertions) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:267-267 |
| The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:118-118 |
| The L23 registration-order proof is registered in the unit-regression lane by the same change set that created it (entry row 118) — it drives the real catalog and sweeper over `tempfile` files with in-process registrar/compactor doubles, so it is hermetic and the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_terminal_liveness_registration_order.py" | mcp/tests/test-evidence-lanes.toml:184-184 |
| The L27 pane-authority proof is registered in the integration lane by the same change set that created it — entry ordinal **53** of 61 in that lane; file line `:183` at base `52bee429` **plus** this change set (`:182` at that base alone, and `:181` at this candidate's own build base `b368b661`, which is the figure the leaf's verdict and worker report cite). It is hermetic but takes the lane of its sibling `test_terminal_liveness.py`, and a new module of this family needs a row or its application imports run inside ordinary unit collection. | "mcp/tests/test_terminal_liveness_pane_authority.py" | mcp/tests/test-evidence-lanes.toml:269-269 |
| The unit-regression bracket the L23 row sits inside, whose upper bound has moved with each later unit-lane insertion (L23, then L01, then L10). | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-198 |
| The L01 steady-state observation suite is registered in the unit-regression lane by the same change set that created it (entry row 97) — it drives the real lifespan finalizer, the real sweeper and the real catalog under a virtual event-loop clock and issues no HTTP request, so the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_serving_observation_loop.py" | mcp/tests/test-evidence-lanes.toml:154-154 |
| The L18 startup-prime proof is registered in the unit-regression lane by the same change set that created it (entry row 98), immediately below its sibling and sharing that sibling's fixture — it drives the real lifespan over a temporary catalog under a virtual clock with no HTTP request and no process, so the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_serving_startup_prime.py" | mcp/tests/test-evidence-lanes.toml:156-156 |
| The unit-regression bracket at the L18 candidate measurement, whose upper bound moved with each later unit-lane insertion (L23, L01, L10, then L18). | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-198 |
| The integration bracket at the L18 candidate measurement. | `integration` | mcp/tests/test-evidence-lanes.toml:203-279 |
| The L17 observer-health proof is registered in the unit-regression lane by the same change set that created it (entry row 122, immediately below `test_terminal_liveness_registration_order.py` at `:121`) — it drives the record, the writer, the accumulator and the real `_state_response` handler and `stream_events` generator against stub projectors with no HTTP transport and no server, so the default unit lane is its behaviour-preserving classification. The insertion sits below `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no earlier row moved. | "mcp/tests/test_terminal_observer_health.py" | mcp/tests/test-evidence-lanes.toml:185-185 |
| The L06 reviewer-relay proof is registered in the unit-regression lane by the same change set that created it (entry row 68, immediately below `test_lifecycle_operation_model_helpers.py` at `:67` and above `test_memory_attribution_producers.py` at `:69`) — it drives the real observer, the production terminal-evidence lift and the real notifier sweep over a temporary coordination root with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. Unlike the L17/L18 insertions this row lands inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate. | "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" | mcp/tests/test-evidence-lanes.toml:116-116 |
| The L05 worker turn owner wake module is registered in the unit-regression lane by the same change set that created it (entry row 105, immediately below `test_state_signal_restart_recovery.py` at `:104` and above `test_state_signal_structural_dispatch_recovery.py` at `:106`) — it seeds owned worker and manager seats on a real `TerminalCatalog`, drives the real `run_agent_notifier_sweep` over a temporary coordination root with real task documents and the real durable stores, issues no HTTP request, starts no server and starts no process, and asserts the whole inbox store rather than its state-signal subset, so the default unit lane is its behaviour-preserving classification. The insertion sits inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate rather than carried. | "mcp/tests/test_state_signal_worker_wake.py" | mcp/tests/test-evidence-lanes.toml:163-163 |
| The L17 observer-health proof is registered in the unit-regression lane by the same change set that created it (entry row 122, immediately below `test_terminal_liveness_registration_order.py` at `:121`) — it drives the record, the writer, the accumulator and the real `_state_response` handler and `stream_events` generator against stub projectors with no HTTP transport and no server, so the default unit lane is its behaviour-preserving classification. The insertion sits below `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no earlier row moved. | "mcp/tests/test_terminal_observer_health.py" | mcp/tests/test-evidence-lanes.toml:185-185 |
| The L07 curator-wake proof is registered in the unit-regression lane by the same change set that created it (entry row 102), immediately below `test_state_signal_boundary_delivery.py` at `:101` and above `test_state_signal_relay.py` at `:103` — it drives the real liveness sweeper, the real agent-notifier sweep and the real `run_agent_notifier_sweep` over temporary catalogs and an in-process tmux host, with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_state_signal_curator_wake.py" | mcp/tests/test-evidence-lanes.toml:160-160 |
| Empty former stress/migration populations | "stress-durability"; "migration" | mcp/tests/test-evidence-lanes.toml:318-322; mcp/tests/test-evidence-lanes.toml:320-321 |
| Small actual integration file population | `integration` | mcp/tests/test-evidence-lanes.toml:203-279 |
| Retained structural detector classifications | "architecture-fitness" | mcp/tests/test-evidence-lanes.toml:280-301 |
| Provider contract classifications | "provider-conformance" | mcp/tests/test-evidence-lanes.toml:302-317 |
| Empty former stress/migration populations | "stress-durability"; "migration" | mcp/tests/test-evidence-lanes.toml:318-322; mcp/tests/test-evidence-lanes.toml:320-321 |
| L38 registered public activation/admission and route-review transport ownership | `integration` | mcp/tests/test-evidence-lanes.toml:203-279 |
| The new parked-candidate suite is registered in the unit-regression lane. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-198 |
| The manifest still has no default classification for an unregistered test file. | "stress-durability" | mcp/tests/test-evidence-lanes.toml:318-320 |
| LOCR-L09 boundary-delivery forcing module registered in the unit lane | "mcp/tests/test_state_signal_boundary_delivery.py" | mcp/tests/test-evidence-lanes.toml:159-159 |
| The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. | "mcp/tests/test_checkpoint_landing.py" | mcp/tests/test-evidence-lanes.toml:29-29 |
| The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 272 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_worktree_status_terminal_next_tool.py" | mcp/tests/test-evidence-lanes.toml:274-274 |
| The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 218 now, after the L4, L5, L7, L8 and L3 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:220-220 |
| The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 230 now, after the L4, L5, L7, L8 and L3 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:232-232 |
| The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 249 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 289 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:291-291 |
| The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 243 now, after the L4, L5, L7, L8 and L3 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:245-245 |
| The L4 producer-census suite is registered in the unit-regression lane by the commit that landed L4, closing the gap the L4 section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:117-117 |
| The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 240 now, after the L7, L8 and L3 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:242-242 |
| The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 222 now, after the L8 and L3 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:224-224 |
| The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 insertion) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:267-267 |
| The L2 knowledge graph suite is registered in the unit-regression lane by the same change set that created it (entry rows 69-73) — all four modules are hermetic (temporary directories, in-process APSW databases, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. | "mcp/tests/test_knowledge_family_revision.py"; "mcp/tests/test_knowledge_graph_reads.py"; "mcp/tests/test_knowledge_relation_rules.py"; "mcp/tests/test_knowledge_revision_seals.py" | mcp/tests/test-evidence-lanes.toml:97-97; mcp/tests/test-evidence-lanes.toml:99-99; mcp/tests/test-evidence-lanes.toml:108-108; mcp/tests/test-evidence-lanes.toml:109-109 |
| The L3 candidate-batch pair and the label-operations suite are registered in the unit-regression lane by the same change set that created them (entry rows 18-19, and row 71 now after the L4 insertions) — all three are hermetic (temporary directories, in-process APSW databases driven through the real admitted destination, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. | "mcp/tests/test_candidate_batch_commands.py"; "mcp/tests/test_candidate_batch_transaction.py"; "mcp/tests/test_knowledge_label_operations.py" | mcp/tests/test-evidence-lanes.toml:18-18; mcp/tests/test-evidence-lanes.toml:19-19; mcp/tests/test-evidence-lanes.toml:98-98 |
| The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (row 118 now, after the L4 insertions) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:118-118 |
| **The L4 snapshot pair is registered in the unit-regression lane by the same change set that created them (rows 69 and 75)** — both modules are hermetic: temporary directories under `tmp_path`, in-process APSW databases driven through the real admitted destination and the real publication lock, and a child interpreter used only as a crash probe, with no integration marker, no repository working tree and no network. | "mcp/tests/test_knowledge_candidate_workspace.py"; "mcp/tests/test_knowledge_snapshot_publication.py" | mcp/tests/test-evidence-lanes.toml:83-83; mcp/tests/test-evidence-lanes.toml:111-111 |
| **The knowledge block's current membership across all four KS leaves**, whose insertion order is why the rows are not contiguous by leaf. | "mcp/tests/test_knowledge_store.py" | mcp/tests/test-evidence-lanes.toml:112-112 |
| **The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value — raised to 400 by this master's owning seat at the `260915-KS-L24` candidate, not by this leaf's fix round, and still 400 on this candidate.** | "integration_case_budget = 400" | pyproject.toml:245-245 |
| **The unit ceiling, cited as the pinned key and value — raised to 1500 at the `260915-KS-L24` candidate, again to 1600 by that candidate's owning seat, again to 2200 by the merge onto the moved super line, and now to 2300 by `260915-KS-L21`, because an over-budget population makes `pytest_collection_finish` raise `UsageError` and run no tests at all. Every earlier value is retained as the ruling that produced it.** | "unit_case_budget = 2300" | pyproject.toml:244-244 |
| **The two lane rows this leaf registered in the same change, both in `integration` because the unit population sits exactly at its declared ceiling.** | "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" | mcp/tests/test-evidence-lanes.toml:207-209 ; mcp/tests/test-evidence-lanes.toml:206-209|
| The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. | `load_lane_manifest` | mcp/test_support/agents_remember_test_support/testing/lane_manifest.py:99-144 |
| Retained unit-regression membership, including the R28 deferred-work, canonical terminal-evidence mapping and L23 registration-order proofs | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-198 |
| The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 272 now, after the L4, seal-removal, L5, L7, L8, L3, L01 and L17 insertions). | "mcp/tests/test_worktree_status_terminal_next_tool.py" | mcp/tests/test-evidence-lanes.toml:274-274 |
| The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 218 now, after the L4, L5, L7, L8, L3 and L01 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:220-220 |
| The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 230 now, after the L4, L5, L7, L8, L3 and L01 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:232-232 |
| The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 249 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 insertions). | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 289 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 insertions). | "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:291-291 |
| The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 243 now, after the L4, L5, L7, L8, L3 and L01 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:245-245 |
| The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 240 now, after the L7, L8, L3 and L01 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:242-242 |
| The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 222 now, after the L8, L3 and L01 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:224-224 |
| The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 and L01 insertions) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:267-267 |
| The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:118-118 |
| The L23 registration-order proof is registered in the unit-regression lane by the same change set that created it (entry row 118) — it drives the real catalog and sweeper over `tempfile` files with in-process registrar/compactor doubles, so it is hermetic and the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_terminal_liveness_registration_order.py" | mcp/tests/test-evidence-lanes.toml:184-184 |
| The L27 pane-authority proof is registered in the integration lane by the same change set that created it — entry ordinal **53** of 61 in that lane; file line `:183` at base `52bee429` **plus** this change set (`:182` at that base alone, and `:181` at this candidate's own build base `b368b661`, which is the figure the leaf's verdict and worker report cite). It is hermetic but takes the lane of its sibling `test_terminal_liveness.py`, and a new module of this family needs a row or its application imports run inside ordinary unit collection. | "mcp/tests/test_terminal_liveness_pane_authority.py" | mcp/tests/test-evidence-lanes.toml:269-269 |
| The unit-regression bracket the L23 row sits inside, whose upper bound has moved with each later unit-lane insertion (L23, then L01, then L10). | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-198 |
| The L01 steady-state observation suite is registered in the unit-regression lane by the same change set that created it (entry row 97) — it drives the real lifespan finalizer, the real sweeper and the real catalog under a virtual event-loop clock and issues no HTTP request, so the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_serving_observation_loop.py" | mcp/tests/test-evidence-lanes.toml:154-154 |
| The L18 startup-prime proof is registered in the unit-regression lane by the same change set that created it (entry row 98), immediately below its sibling and sharing that sibling's fixture — it drives the real lifespan over a temporary catalog under a virtual clock with no HTTP request and no process, so the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_serving_startup_prime.py" | mcp/tests/test-evidence-lanes.toml:156-156 |
| The unit-regression bracket at the L18 candidate measurement, whose upper bound moved with each later unit-lane insertion (L23, L01, L10, then L18). | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-198 |
| The integration bracket at the L18 candidate measurement. | `integration` | mcp/tests/test-evidence-lanes.toml:203-279 |
| The L17 observer-health proof is registered in the unit-regression lane by the same change set that created it (entry row 122, immediately below `test_terminal_liveness_registration_order.py` at `:121`) — it drives the record, the writer, the accumulator and the real `_state_response` handler and `stream_events` generator against stub projectors with no HTTP transport and no server, so the default unit lane is its behaviour-preserving classification. The insertion sits below `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no earlier row moved. | "mcp/tests/test_terminal_observer_health.py" | mcp/tests/test-evidence-lanes.toml:185-185 |
| The L06 reviewer-relay proof is registered in the unit-regression lane by the same change set that created it (entry row 68, immediately below `test_lifecycle_operation_model_helpers.py` at `:67` and above `test_memory_attribution_producers.py` at `:69`) — it drives the real observer, the production terminal-evidence lift and the real notifier sweep over a temporary coordination root with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. Unlike the L17/L18 insertions this row lands inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate. | "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" | mcp/tests/test-evidence-lanes.toml:116-116 |
| The L05 worker turn owner wake module is registered in the unit-regression lane by the same change set that created it (entry row 105, immediately below `test_state_signal_restart_recovery.py` at `:104` and above `test_state_signal_structural_dispatch_recovery.py` at `:106`) — it seeds owned worker and manager seats on a real `TerminalCatalog`, drives the real `run_agent_notifier_sweep` over a temporary coordination root with real task documents and the real durable stores, issues no HTTP request, starts no server and starts no process, and asserts the whole inbox store rather than its state-signal subset, so the default unit lane is its behaviour-preserving classification. The insertion sits inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate rather than carried. | "mcp/tests/test_state_signal_worker_wake.py" | mcp/tests/test-evidence-lanes.toml:163-163 |
| The L17 observer-health proof is registered in the unit-regression lane by the same change set that created it (entry row 122, immediately below `test_terminal_liveness_registration_order.py` at `:121`) — it drives the record, the writer, the accumulator and the real `_state_response` handler and `stream_events` generator against stub projectors with no HTTP transport and no server, so the default unit lane is its behaviour-preserving classification. The insertion sits below `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no earlier row moved. | "mcp/tests/test_terminal_observer_health.py" | mcp/tests/test-evidence-lanes.toml:185-185 |
| The L07 curator-wake proof is registered in the unit-regression lane by the same change set that created it (entry row 102), immediately below `test_state_signal_boundary_delivery.py` at `:101` and above `test_state_signal_relay.py` at `:103` — it drives the real liveness sweeper, the real agent-notifier sweep and the real `run_agent_notifier_sweep` over temporary catalogs and an in-process tmux host, with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. | "mcp/tests/test_state_signal_curator_wake.py" | mcp/tests/test-evidence-lanes.toml:160-160 |
| Retained unit-regression membership, including the R28 deferred-work and canonical terminal-evidence mapping proofs. The range moved by +2 when this change set and L4 each inserted one row additively into the same list. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-198 |
| Small actual integration file population | `integration` | mcp/tests/test-evidence-lanes.toml:203-279 |
| Retained structural detector classifications | "architecture-fitness" | mcp/tests/test-evidence-lanes.toml:280-301 |
| Provider contract classifications | "provider-conformance" | mcp/tests/test-evidence-lanes.toml:302-317 |
| Empty former stress/migration populations | "stress-durability"; "migration" |mcp/tests/test-evidence-lanes.toml:318-322; mcp/tests/test-evidence-lanes.toml:320-321|
| L38 registered public activation/admission and route-review transport ownership | `integration` | mcp/tests/test-evidence-lanes.toml:203-279 |
| The new parked-candidate suite is registered in the unit-regression lane. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-198 |
| The manifest still has no default classification for an unregistered test file. | "stress-durability" | mcp/tests/test-evidence-lanes.toml:4-321 |
| LOCR-L09 boundary-delivery forcing module registered in the unit lane | "mcp/tests/test_state_signal_boundary_delivery.py" | mcp/tests/test-evidence-lanes.toml:159-159 |
| The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. | "mcp/tests/test_checkpoint_landing.py" | mcp/tests/test-evidence-lanes.toml:29-29 |
| The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 272 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_worktree_status_terminal_next_tool.py" | mcp/tests/test-evidence-lanes.toml:274-274 |
| The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 218 now, after the L4, L5, L7, L8 and L3 insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:220-220 |
| The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 230 now, after the L4, L5, L7, L8 and L3 insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:232-232 |
| The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 249 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row 289 now, after the L4, seal-removal, L5, L7, L8 and L3 insertions). | "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:291-291 |
| The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 243 now, after the L4, L5, L7, L8 and L3 insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:245-245 |
| The L4 producer-census suite is registered in the unit-regression lane by the commit that landed L4, closing the gap the L4 section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:117-117 |
| The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 240 now, after the L7, L8 and L3 insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:242-242 |
| The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 222 now, after the L8 and L3 insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:224-224 |
| The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row 265 now, after the L3 insertion) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:267-267 |
| The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:118-118 |
| The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value. | "integration_case_budget = 400" | pyproject.toml:245-245 |
| The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value. | "integration_case_budget = 400" | pyproject.toml:245-245 |
| Retained unit-regression membership, including the R28 deferred-work and canonical terminal-evidence mapping proofs. **Re-derived at `260918-TSIP-L6`:** the block is `5-159`, because this leaf added `test_response_address_binding.py` at `:112`, L5 had added its own row at `:153`, and L4 inserted one row additively into the same list. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-159 |
| Small actual integration file population | `integration` | mcp/tests/test-evidence-lanes.toml:164-230 |
| Retained structural detector classifications | "architecture-fitness" | mcp/tests/test-evidence-lanes.toml:231-282 |
| Provider contract classifications | "provider-conformance" | mcp/tests/test-evidence-lanes.toml:253-304 |
| Empty former stress/migration populations | "stress-durability"; "migration" | mcp/tests/test-evidence-lanes.toml:269-322; mcp/tests/test-evidence-lanes.toml:271-322 |
| L38 registered public activation/admission and route-review transport ownership | `integration` | mcp/tests/test-evidence-lanes.toml:164-230 |
| The new parked-candidate suite is registered in the unit-regression lane. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-159 |
| The manifest still has no default classification for an unregistered test file. | "stress-durability" | mcp/tests/test-evidence-lanes.toml:4-320 |
| LOCR-L09 boundary-delivery forcing module registered in the unit lane | "mcp/tests/test_state_signal_boundary_delivery.py" | mcp/tests/test-evidence-lanes.toml:159-159 |
| The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. | "mcp/tests/test_checkpoint_landing.py" | mcp/tests/test-evidence-lanes.toml:29-29 |
| The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row **226** now, after the L4, seal-removal, L5, L7, L8, L3 and `260918-TSIP-L6` insertions). | "mcp/tests/test_worktree_status_terminal_next_tool.py" | mcp/tests/test-evidence-lanes.toml:274-274 |
| The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row **172** now, after the L4, L5, L7, L8, L3 and `260918-TSIP-L6` insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:220-220 |
| The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row **184** now, after the L4, L5, L7, L8, L3 and `260918-TSIP-L6` insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:232-232 |
| The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row **203** now, after the L4, seal-removal, L5, L7, L8, L3 and `260918-TSIP-L6` insertions). | "mcp/tests/test_pause_stop_only_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it (row 190 at that leaf; row **240** now, after the L4, seal-removal, L5, L7, L8, L3 and `260918-TSIP-L6` insertions). | "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:291-291 |
| The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row **197** now, after the L4, L5, L7, L8, L3 and `260918-TSIP-L6` insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:245-245 |
| The L4 producer-census suite is registered in the unit-regression lane by the commit that landed L4, closing the gap the L4 section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:117-117 |
| The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row **194** now, after the L7, L8, L3 and `260918-TSIP-L6` insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:242-242 |
| The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row **176** now, after the L8, L3 and `260918-TSIP-L6` insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. | "mcp/tests/test_closeout_projection_source_classification.py" | mcp/tests/test-evidence-lanes.toml:224-224 |
| The L8 terminal-blocker suite is registered in the integration lane by the same change set that created it (entry row **219** now, after the L3 and `260918-TSIP-L6` insertions) — it builds a real landed leaf over disposable repositories and drives the public finalization route, so that is its behaviour-preserving lane. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:267-267 |
| The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 69) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:118-118 |
| The integration lane's collected-case cap that constrains lane choice, cited as the pinned key and value. | "integration_case_budget = 300" | pyproject.toml:170-176 |
| The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. | `load_lane_manifest` | mcp/test_support/agents_remember_test_support/testing/lane_manifest.py:99-142 |
| The L4 capsule-and-skill-serving suite is registered in the unit-regression lane by the same change set that created it (entry row 19) — 19 of its 21 cases are hermetic over a disposable coordination root and a synthetic skills corpus and only its two real-process exchanges carry the integration marker, so that is its behaviour-preserving lane. | "mcp/tests/test_capsule_serving.py" | mcp/tests/test-evidence-lanes.toml:23-23 |
| The unit collected-case ceiling. **Corrected four times:** it read 1000 and the default selection had outgrown it (1053 collected at the base, so `pytest mcp/tests` refused collection before any case executed); 260915-CAPS-L8 executed the developer's raise to 1500, the merged line's 2026-09-17 ruling raised it to **2000**, the merge onto the moved super line raised it to **2200** over the merged 2035-case population, and `260915-KS-L21` raised it to **2300** — which is what the declaration reads now — over the measured 2206, six cases past 2200. Superseded four times, never deleted: the condition each value recorded was real and is what caused the ruling that replaced it. | "unit_case_budget = 2300" | pyproject.toml:244-244 |
## Cross-Repo References

No separate cross-repository authority is established by this file.

## 260918-TSIP-L4 — Two Rows, And The Citations The Insertion Moved

This leaf added **two** rows and no other content changed: `"mcp/tests/test_atomic_series_chain_pair_order.py"`
in **`integration`** at **`:165`** (`T49` — the module existed with no lane row, so the loader
refused: `test evidence lanes have 1 finding(s): test files without an explicit lane`) and
`"mcp/tests/test_tool_response_conformance.py"` in **`architecture-fitness`** at **`:244`**. The
file is **267 → 269 lines**, and the shipped loader now reports
`LOADED: f5f3c26265e1846f55b0ee6f13d56282c1fd1ffaa5a624de29474813c3db953c`, **251 rows / 251
modules**.

**The measured remap is `n ≤ 164 → n`, `165-242 → n+1`, `243-268 → n+2`.** (The worklist handed to
the curator wrote `n ≤ 163 → n`, `164-243 → n+1`, `244+ → n+2`; the boundary is one line out —
`integration = [` is old `:161` and old `:164` is the last unchanged line, so a citation anchored
exactly at old 164 or 243 would have been moved wrongly. No citation in the population anchors
there, so no repair was affected.)

**How the citations were repaired, and why the count is not the finding count.** The shipped
`citation_fix` was run tree-wide over the leaf worktree: **81 failing claims, 66 repaired, 25
documents written, 15 declined, 28 findings remaining**. The 15 declines are anchor-ambiguous
cases the fixer refuses by design (`integration` and `nextAction` occur many times;
`class LeafRefResolutionError`, `contractFingerprint`, `"AgentRole = Literal["` resolve to several
extents). The curator then **enumerated instead of trusting the finding set**: 13 changed paths ×
every active citation and prose mention into them = **290 occurrences, 165 of them moved**, against
the checker's **96 `range_resolution` findings** — so **69 moved citations were green**, the
`range_resolution` blind spot this card already records. All 98 the fixer could not reach were
repaired from the measured map and 11 by hand, and the final containment check reports **213 claims
citing a changed path with 0 missing anchors**.

**Two aggregate rows, fixed from the map rather than by the fixer.** `:861`/`:865`
(`157-221 → 157-222`) and `:867` (`4-266 → 4-268`) are the rows whose single anchor resolves to
several extents; they were repaired from the measured map and then re-read in the file.

**One correction inside this card that is not this leaf's arithmetic.** The four
`… Lane Row (Declared)` narratives (`:296`, `:400`, `:428`, `:515`) carried line numbers that were
already stale at this leaf's base — the L17 narrative's `:172`/`:173`/`:174` were 13 lines from the
rows they name (`:185`/`:186`/`:187` at base), the L27 narrative's `:182`/`:184` were 34 lines out,
and the L8 and L5 narratives 13 and 38 out. The five prose mentions in them were set to the **true
current rows** (`187`/`186`/`188`, `216`, `257`, `218`/`217`/`219`) rather than moved by `+1`/`+2`,
because moving a stale number preserves a reader-facing error that no check can see (`T45`).

## 260918-TSIP-L5 — One Row, And The Bracket Figures Re-Derived

This leaf adds **one** row and changes no other line of the manifest:
`"mcp/tests/test_tool_entry_point_sweep.py"` in **`unit-regression`** at **`:153`**, inserted
alphabetically between `test_terminal_paste.py` (`:152`) and `test_tool_response_budgets.py`
(`:154`). That is the behaviour-preserving lane: the module's whole world is a `tempfile`
coordination root with no docker, no network and no real state, it carries no `-m` override, and
its 14 cases run in the ordinary default selection. The file is **269 → 270 lines**, the manifest
entries **251 → 252**, and the modules on disk **251 → 252** — every module on disk now has
exactly one row.

**The measured remap is `n ≤ 152 → n`, `n = 153..269 → n+1`.** Verified as a pure one-line
insertion (one added line; the shifted tail compared line by line). `integration = [` is old
`:161` → new `:162`, `architecture-fitness = [` old `:228` → new `:229`, and the new row's own
line is `:153` — so the lane-bracket rows and every per-module row below `:152` move, and the
three entities the previous section named as static (`unit-regression = [` at `:5`, and the
`stress-durability`/`migration` declarations) keep their relation to the insertion.

**The population, enumerated rather than inferred (`T60`).** Every citation into this file was
enumerated from **this leaf's memory worktree** (`d185e459` — the tree the enclosure contract
names, and the only one `application/memory_tools.py::_refuse_official_memory` permits):
**115 moving anchors across 20 documents — 48 live, 67 under `## Update History` and therefore
exempt — moving 111 document lines (45 live, 66 exempt)**. The census was taken twice; the second
pass found the first **three rows short**, because those rows spell the path as the bare basename
(`test-evidence-lanes.toml:184-190`) rather than the routed path — an enumeration must match both
spellings. **No memory document cites the new module** (it did not exist at this base), so its own
card is the only artifact it needs.

**`T52` measured on this leaf: the checker saw 31 of the 48 live movers.** The baseline
`range_resolution` run reported exactly 31 `citation_anchor_absent_from_range` findings against
these documents; the other 17 moved citations were **green** because the anchor still sat inside
the cited range — the five `## … Lane Row (Declared)` prose mentions, the two ranges that span the
insertion (`test_terminal_blocker_reasons.py.md`'s `128-199`, this card's `4-268`), and the six
bracket rows whose anchor is the range's own first line. Enumerating the population rather than
the finding set is what found them.

**The bracket rows, re-derived at this candidate rather than shifted.** The reference rows at
`:866-872` have been carried across leaves by `+1` shifts since at least `621db898`, and their
values **matched no bracket of this file**: measured here, `integration` runs from its declaration
`:161` to its closing bracket `:227`, not `157-222`. They are now this candidate's measured
brackets, computed as the lane's declaration line through its closing bracket (an empty lane cited
at its declaration line, as its existing shape does): `integration` **`162-228`**,
`architecture-fitness` **`229-250`**, `provider-conformance` **`251-266`**, `stress-durability`
**`267-267`**, `migration` **`269-269`**, whole manifest **`4-269`**. **Reported, not repaired:**
the two `5-151` rows at `:865` and `:871` under-claim the unit-regression block, which is `5-157`
here (`:5` declaration → `:157` closing bracket). Their own text — "the range moved by +2 when
this change set and L4 each inserted one row additively into the same list" — declares them a
moved-range record, so they are left and reported rather than re-derived. Same disposition for the
as-of blocks that name their own base (`## Current population (measured at this leaf's synced base
23cc7a72 plus its own two rows)` at `:214` and the L2 lane-population paragraph at `:70`).

**Nine prose figures inside the reference table were 30-40 lines stale and are now the measured
rows** (`:875` `row 184 now` → `row 224 now`, `:876` 134 → 170, `:877` 146 → 182, `:878` 163 →
201, `:879` 196 → 238, `:880` 157 → 195, `:882` 154 → 192, `:883` 138 → 174, `:884` 178 → 217).
Each of those cells cites its module's current row in the Source column, so prose and citation
contradicted each other once this leaf's shift landed; no check reads either number.

**A fifth `… Lane Row (Declared)` prose mention, missed by the L4 pass.** The `260913-LCA-L5`
narrative at `:366-367` said the master-link module's row "is `…:153`"; at this leaf's base that
row is `:191` — **38 lines stale**, the same class `260918-TSIP-L4` repaired in four sibling
narratives, and one row short of L4's own list. It now names the true row, `:192`. That narrative
carries no routed path, so neither a citation enumeration nor any checker ever saw it: the
preceding card said "the five `… Lane Row (Declared)` sections" and there are six.

**And one claim's provenance had to be re-worded to survive being touched.** The
`test_automatic_post_integration_cleanup.py.md` row at `:140` was already demoted as pre-existing
debt because its literal anchor `Path("mcp/tests/test_automatic_post_integration_cleanup.py")`
resolves **twice** in `dependency_ownership.py` (`:65` and `:111`) — ambiguous provenance, which
the check enforces on any document a task touches ("touch it, own it"). This leaf must repair that
row's citation anyway, so the anchor is now the unique owning key
`"AMBIENT_ROLE_RUNNER_PATH: frozenset("` at `dependency_ownership.py:62-65`, which resolves once,
and the `integration = [` range moved `161` → `162` with the rest of the population.

## 260918-TSIP-L6 The Two Insertions, And Every Figure Re-Derived From This Candidate

**This leaf added two rows, both pure insertions, both `unit-regression`.** `270 → 272` lines,
`2 insertions, 0 deletions`, two hunks: `test_response_address_binding.py` at **`:112`** and
`test_tool_refusal_conformance.py` at **`:155`**. The insertion coordinates in the pre-change file
are OLD lines **112** and **154** — the boundary is `old_start + old_len`, and reading the hunk
header's `+109` straight off is off by one, which is the trap this card's own shift rule exists to
prevent. The rule is `new = old + (1 if old >= 112) + (1 if old >= 154)`; it reproduces the
file's own line map exactly (`270/270` base lines have an exact counterpart, `0` replaced).

**The population, enumerated from this leaf's memory worktree at `4e21dd22`** (not the official
checkout, `T65`) and with **both spellings** of the path (`T60`'s one-spelling-down lesson):

| | routed spelling only | both spellings |
| --- | --- | --- |
| documents citing the target | 53 | 53 |
| anchored occurrences | 218 (105 live / 113 exempt) | **226 (106 live / 120 exempt)** |
| unanchored mentions | 53 | 98 (includes `path:(N, N)` tuple records) |

The eight extra anchored rows are basename-spelled; **one is live** —
`onboarding/mcp/tests/test-evidence-lanes.toml.md:961`, the `:184-190` row L5's `F2` also found —
and the other seven are exempt `## Update History` bullets. The 45 extra unanchored mentions are
prose and tuple records, not citations.

**`T52` measured on this leaf.** The checker's `range_resolution` reported **102** stale rows
across **93** documents-and-lines. An independent enumeration of the same population found
**117** stale rows across **99** lines: the checker is silent on **15 rows / 6 lines** because
those rows pool several ranges and another range still holds the anchor. So the blind spot here is
**13 % of rows** — much smaller than L4's 58 % or L5's 65 %, because this leaf's change moved its
anchors *out* of their ranges rather than leaving them inside.

**Every bracket row and every `row N` figure in this card was re-derived from THIS candidate**,
not shifted: `unit-regression` is `5-159`, `public-contract` `160-163`, `integration` `164-230`,
`architecture-fitness` `231-252`, `provider-conformance` `253-268`, `stress-durability` `269-270`,
`migration` `271-272`, and the manifest holds **254 entries for 254 modules on disk**
(`153 + 2 + 65 + 20 + 14`). Five narratives that state a *current* position were stale and are
corrected: the L17 row is `:190` (was `:188`, with its neighbours `:189`/`:191`), the L5
master-link row `:194` (was `:192`), the L7 capacity-refusal row `:176` (was `:138` — 38 lines),
the L8 terminal-blocker row `:219` (was `:217`), and the L5 codex row `:260` (was `:258`).

**Post-sync note (`T75`'s precedent).** This leaf's anchors are true of the **272-line** file at
the leaf's base. After the governed closeout and the master sync, the same file is **323 lines**
with the two new rows at `145` and `188`, and every anchor below OLD 112 moves by a different
amount — the loader must be re-run after that sync rather than carried.

## Update History
- 2026-09-19T19:52+02:00 — 260918-TSIP-L6 curator (uncommitted change set on `ar/260918-tsip-l6-ar`, base `a1351504`): the two new rows (`:112`, `:155`, both `unit-regression`, 270 → 272 lines) recorded with the shift rule and the insertion coordinates; the population enumerated from this leaf's memory worktree with both spellings (226 anchored = 106 live / 120 exempt, and the eight basename-spelled rows the routed-only scan misses); the `T52` measurement (the checker saw 102 rows / 93 lines of 117 rows / 99 lines); every bracket row and `row N` figure re-derived from this candidate (254 entries for 254 modules on disk); five current-position narratives corrected. Closeout owns the real commit stamp; the post-sync pass must re-derive these anchors against the 323-line merged file.
- 2026-09-18T19:56:44+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the four enforced `citation_anchor_absent_from_range` rows in this document** (four table rows, all naming `"stress-durability"`). Each row's lane-entry list stopped at `309-309` while the lane key the claim is about — `stress-durability = [`, empty since the population was emptied — now sits at `312`; each row's last range was widened to `309-312` so it reaches that key. The appended `migration` key at `314` is not named by any of these rows and was left alone. Claims, anchors and the other ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T19:48+02:00 — 260918-TSIP-L5 curator (uncommitted change set on `ar/260918-tsip-l5-ar`, base `f05ba167`, `test-evidence-lanes.toml` **269 → 270 lines**, `+1`): recorded this leaf's one added row — `mcp/tests/test_tool_entry_point_sweep.py` at `:153`, in **`unit-regression`** — with the measured remap (`n ≤ 152 → n`, `153..269 → n+1`), the enumerated citation population (**115 moving anchors / 20 documents: 48 live, 67 exempt; 111 lines, 45 live**), the `T52` measurement (the checker saw 31 of the 48 live movers), the six bracket rows re-derived to this candidate's measured brackets (`162-228`, `229-250`, `251-266`, `267-267`, `269-269`, `4-269`), the nine stale `row N now` figures and the fifth stale `… Lane Row (Declared)` mention set to their true rows, and the one ambiguous literal anchor re-worded to the unique owner key so the touched document's provenance verifies. Verification metadata remains the recorded base commit plus the closeout's advance; the candidate is uncommitted and the governed closeout stamps the real code commit.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:219-219. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:285-285. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:246-246. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:227-227. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:269-269. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:312-312. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:296-296. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:277-277. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:219-219. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:285-285. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:246-246. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:227-227. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:269-269. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:205-205; mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:219-219. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:285-285. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:246-246. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:227-227. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:269-269. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:312-312. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:296-296. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:277-277. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:219-219. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:285-285. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:246-246. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:227-227. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:269-269. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:205-205; mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:219-219. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:285-285. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:246-246. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:227-227. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:269-269. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:312-312. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:296-296. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:277-277. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:201-201. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:28+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **added the L23 section** — the five `unit-regression` rows this leaf appended at the end of the list (`:191-195`: `test_next_step_address_binding.py`, `test_terminal_preview_expectation.py`, `test_knowledge_merge_right_side_writes.py`, `test_evidence_catalog_gate_boundaries.py`, `test_curator_coherence_publication_discoverability.py`), four of them focused suites over in-process or temporary state and the fifth shelling out to `git init` / `git add` against a temporary root it owns, and the population measured on this candidate from the manifest and the modules on disk: **297 declared entries against 297 modules on disk, 0 declared-but-absent and 0 present-but-undeclared**, with `unit-regression` **190** (key `:5`, rows `6-195`), `public-contract` 2 (`:197`, rows `198-199`), `integration` 74 (`:201`, rows `202-275`), `architecture-fitness` 17 (`:277`, rows `278-294`) and `provider-conformance` 14 (`:296`, rows `297-310`). It records the append point as this leaf's ruling (item 16 half (a)): an append moves no existing row of its own list while a mid-list insertion displaces every entry after it and still shifts the lines below, the property is pinned against the shipped manifest by `test_memory_citation_resolution.py::InsertedRegistrationRangeDriftTests`, and no header comment was added because a line at `:1` would itself be the defect. It also states the declared rails and this change set's measured populations — `unit_case_budget = 2300` (`pyproject.toml:244`), `integration_case_budget = 400` (`:245`), **2278 / 2300** unit and **400 / 400** integration, the latter with zero headroom and a `UsageError`-means-zero-tests consequence for any further integration case — both counts attributed to seat W1's worktree-bound collect-only runs, not to this pass. No existing row was re-pointed, reordered or edited and no earlier account was deleted; the metadata block's `reviewedWorkingCandidate` row now names this leaf's candidate and the commit fields are untouched.
2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **recorded this leaf's lane row and re-measured the manifest rather than carrying L21's
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:257-257. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:214-214. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:232-232. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:116-116. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:280-280. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:241-241. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:222-222. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:307-307. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:291-291. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:272-272. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:158-158. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:183-183. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:161-161. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:115-115. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:183-183. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:154-154. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:152-152. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:259-259. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:182-182. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:257-257. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:214-214. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:232-232. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:280-280. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:241-241. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:222-222. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:200-200; mcp/tests/test-evidence-lanes.toml:199-199. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:257-257. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:214-214. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:232-232. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:116-116. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:280-280. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:241-241. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:222-222. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:307-307. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:291-291. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:272-272. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:158-158. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:183-183. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:161-161. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:115-115. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:183-183. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:154-154. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:152-152. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:259-259. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:182-182. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:257-257. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:214-214. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:232-232. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:280-280. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:241-241. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:222-222. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:200-200; mcp/tests/test-evidence-lanes.toml:199-199. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:257-257. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:257-257. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:214-214. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:232-232. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:116-116. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:280-280. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:241-241. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:222-222. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:307-307. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:291-291. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T16:13:35+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:272-272. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:256-256. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:234-234. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:279-279. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:221-221. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:209-209. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:263-263. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:306-306. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:290-290. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:271-271. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:182-182. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:160-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:182-182. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:195-195. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:153-153. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:151-151. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:258-258. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:181-181. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:256-256. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:234-234. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:279-279. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:221-221. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:209-209. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:263-263. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:199-199; mcp/tests/test-evidence-lanes.toml:198-198. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:256-256. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:234-234. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:279-279. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:221-221. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:209-209. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:263-263. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:306-306. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:290-290. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:271-271. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:182-182. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:160-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:182-182. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:153-153. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:151-151. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:258-258. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:181-181. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:256-256. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:234-234. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:279-279. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:221-221. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:209-209. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:263-263. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:199-199; mcp/tests/test-evidence-lanes.toml:198-198. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:256-256. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:256-256. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:234-234. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:279-279. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:221-221. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:209-209. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:263-263. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:306-306. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:290-290. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:271-271. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): **added the L21 lane-row account and re-read every budget claim this card carries as a current value.** The leaf registers one module — `mcp/tests/test_migration_census.py`, `unit-regression`, inserted mid-list at `mcp/tests/test-evidence-lanes.toml:128` between `test_memory_scope_task_derivation.py` (`:127`) and `test_models.py` (`:129`) — and the card now records the measured population (291 declared entries against 291 modules on disk, 0/0 undeclared or absent, 184 / 2 / 74 / 17 / 14 across the five lanes) and the fact that one mid-list insertion moved every later line by one. **The budget pair was re-read and re-worded, not carried:** `unit_case_budget = 2300` at `pyproject.toml:244` and `integration_case_budget = 400` at `:245` are what the file declares now, and the census leaf raised the unit ceiling 2200 → 2300 because its 48 cases took the merged population to 2206, six past the then-declared 2200; the L16, L17 and L14 sections' `2200`, `1500`, `1250` and `1100` pairs are retained as the rulings that produced them, each now marked with the pair the file declares. Two pinned-literal rows were corrected from `"unit_case_budget = 2200"` / `pyproject.toml:214-214` to `"unit_case_budget = 2300"` / `pyproject.toml:244-244`, the two integration-cap rows re-cited from `:215` to `:245`, and the `Corrected three times` row re-worded to its fourth correction. No claim and no history entry was deleted. The metadata block above now names this leaf's candidate as what was read and carries **no `lastVerifiedCommitHash`**: the body was re-read against a working candidate no commit contains, so no real commit holds the content a stamp would claim to have verified, and closeout owns the stamp. The body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:173-173. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:191-191. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:194-194. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:200-200. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:181-181. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:169-169. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:223-223. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "stress-durability"; "migration" repointed to mcp/tests/test-evidence-lanes.toml:266-266; mcp/tests/test-evidence-lanes.toml:268-268. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_capsule_serving.py" repointed to mcp/tests/test-evidence-lanes.toml:24-24. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:255-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:212-212. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:230-230. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:115-115. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:233-233. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:278-278. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:239-239. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:220-220. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing.py" repointed to mcp/tests/test-evidence-lanes.toml:30-30. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:155-155. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:305-305. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:289-289. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:270-270. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:181-181. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:159-159. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:114-114. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:181-181. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:152-152. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:257-257. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:180-180. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:116-116. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:255-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:212-212. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:230-230. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:233-233. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:278-278. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:239-239. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:220-220. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:198-198; mcp/tests/test-evidence-lanes.toml:197-197. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:110-110. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:116-116. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:255-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:212-212. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:230-230. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:115-115. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:233-233. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:278-278. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:239-239. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:220-220. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing.py" repointed to mcp/tests/test-evidence-lanes.toml:30-30. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:155-155. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:305-305. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:289-289. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:270-270. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:181-181. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:159-159. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:114-114. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:181-181. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:152-152. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:257-257. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:180-180. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:116-116. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:255-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:212-212. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:230-230. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:233-233. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:278-278. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:239-239. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:220-220. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:198-198; mcp/tests/test-evidence-lanes.toml:197-197. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:110-110. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:116-116. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:255-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:255-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:212-212. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:230-230. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:115-115. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:233-233. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:278-278. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:239-239. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:220-220. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:262-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing.py" repointed to mcp/tests/test-evidence-lanes.toml:30-30. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:155-155. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:305-305. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:289-289. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:44:36+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:270-270. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:228-228. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:113-113. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:275-275. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:206-206. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:260-260. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:153-153. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:302-302. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:286-286. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:267-267. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:154-154. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:179-179. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:179-179. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:148-148. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:255-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:178-178. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:114-114. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:228-228. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:275-275. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:206-206. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:260-260. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196; mcp/tests/test-evidence-lanes.toml:195-195. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:108-108. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:114-114. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:228-228. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:113-113. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:275-275. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:206-206. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:260-260. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:153-153. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:302-302. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:286-286. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:267-267. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:154-154. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:179-179. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:179-179. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:148-148. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:255-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:178-178. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:114-114. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:228-228. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:275-275. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:206-206. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:260-260. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196; mcp/tests/test-evidence-lanes.toml:195-195. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:108-108. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:114-114. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:210-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:228-228. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:113-113. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:275-275. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:237-237. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:206-206. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:260-260. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:153-153. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:302-302. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:286-286. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:267-267. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:05+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): **added the L16 lane-row account above and relabelled the L17 section as superseded on those three rows.** This leaf registered three modules — two `unit-regression` rows inserted mid-list at `:92-93` (which is why every later line of this file moved by two) and one `integration` row appended at `:265` — each classified by behaviour rather than by budget convenience, and the section states the ceiling pair `pyproject.toml` actually carries (`2200` at `:214`, `400` at `:215`) rather than the `1500`/`300` values earlier sections of this card quote as current. No claim was deleted or softened, and no verification stamp advanced: the source is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T13:42+02:00 — 260918-TSIP-L2 curator (uncommitted change set on `ar/260918-tsip-l2-ar`,
  base `d9becade`, `test-evidence-lanes.toml` **266 → 267 lines**, `+1`): recorded this leaf's one
  added row — `mcp/tests/test_record_integrity.py` at `:246`, in the existing **`architecture-fitness`**
  lane, because the module imports the verification package and executes nothing over a real boundary.
  Added a declared section carrying the row, the lane rationale, the unavailability of any
  lower-displacement position, and the renumbering it caused; **the insertion moved the 21 entries
  below it (`:246-266`) by +1 and left every lane above it alone, so the lane populations are now
  150 / 2 / 64 / **19** / 14 with `stress-durability` and `migration` empty.** Three citations were
  invalidated and all three are repaired in this same pass, with the ranges **re-derived from the
  post-edit bytes rather than from the numbers the edit was planned against**: this card's
  `:262-265` → `:263-266` (the one the product's own `range_resolution` check reported) and `:4-265`
  → `:4-266` (which no check reported, because its anchor still resolved inside the old range), plus
  `onboarding/mcp/tests/test_codex_capsule_delivery.py.md` `:254-254` → `:255-255`. This card's
  `:242-256` row was checked and **left alone** — its prefix still covers `provider-conformance` at
  `:248`. **Two corrections to the section below, made rather than repeated:** the `:4-265` stale end
  and the fail-closed-loader claim are both `T45`'s class — a figure a reader takes as current while
  no check can see it. `lastUpdated` advances with this body edit;
  `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are deliberately unchanged because the candidate
  is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T13:27+02:00 — 260915-KS-L13 curator (range-closure pass): **the four budget-declaration rows in this card were re-read against `pyproject.toml` as it now stands and re-cited to the merged declaration.** Two of them (the ceiling row repeated in the L11 facet table and the L17 composition table) quoted `unit_case_budget = 1600` with an EMPTY Source cell; the merged file declares `unit_case_budget = 2200` (`:214`) and `integration_case_budget = 400` (`:215`), so both anchors were corrected to 2200 and both Source cells filled with `pyproject.toml:214-214`. The integration-cap row quoted `integration_case_budget = 300` at `pyproject.toml:170-176`, a value and extent the file no longer carries: it now names 400 at `pyproject.toml:215-215`. The "Corrected twice … 2000" row was re-worded to its third correction: the merge onto the moved super line raised the unit ceiling to **2200** over the merged 2035-case population, which is what the declaration reads now — the earlier 1500 and 2000 rulings are retained as the history they are. No claim was deleted or softened. No verification stamp advanced: the source is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_capsule_serving.py" repointed to mcp/tests/test-evidence-lanes.toml:23-23. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:272-272. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:258-258. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing.py" repointed to mcp/tests/test-evidence-lanes.toml:29-29. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:151-151. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:299-299. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "stress-durability"; "migration" repointed to mcp/tests/test-evidence-lanes.toml:299-299; mcp/tests/test-evidence-lanes.toml:301-301. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:283-283. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:152-152. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:177-177. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:155-155. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:110-110. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:177-177. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:148-148. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:146-146. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:272-272. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:258-258. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:194-194; mcp/tests/test-evidence-lanes.toml:193-193. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "integration_case_budget = 400" repointed to pyproject.toml:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:106-106. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:272-272. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:258-258. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing.py" repointed to mcp/tests/test-evidence-lanes.toml:29-29. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:151-151. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:299-299. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:283-283. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:152-152. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:177-177. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:155-155. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:110-110. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:177-177. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:148-148. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:146-146. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:272-272. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:258-258. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:194-194; mcp/tests/test-evidence-lanes.toml:193-193. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "integration_case_budget = 400" repointed to pyproject.toml:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:106-106. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:208-208. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:272-272. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:258-258. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing.py" repointed to mcp/tests/test-evidence-lanes.toml:29-29. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:151-151. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:299-299. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:283-283. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:264-264. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T11:55+02:00 — 260918-TSIP-L1 curator (uncommitted change set on `ar/260918-tsip-l1-ar`,
  base `f0313143`, `test-evidence-lanes.toml` +1): recorded this leaf's **one** added row —
  `mcp/tests/test_instrument_discipline.py` at `:232`, in the existing **`architecture-fitness`**
  lane, because the module imports the verification package and executes nothing over a real
  boundary. Added a declared section carrying the row, its lane rationale, the measured loader result
  and the renumbering it caused. **The insertion moved the 27 entries below it**, which invalidated
  four citation rows in this memory tree: three were pure moves repaired mechanically by the shipped
  citation fixer (this card's own `:235` → `:236` at line 762,
  `test_pause_is_not_publication.py.md` `:235` → `:236`, and `test_codex_capsule_delivery.py.md`
  `:253` → `:254`), and the fourth — the L37 lane-registration row in `mcp/tests/overview.md` — was
  declined by the fixer as ambiguous and corrected by hand. The before/after pairs in the new section
  were **measured** against the base commit, which is how the first draft's claim that the pause
  suite's row had also moved was caught and removed: `:199` is above the insertion and did not move.
  This entry's stamp was moved from `11:46+02:00` to `11:55+02:00` on the same pass: the generated
  citation repair below is stamped `09:46:27+00:00`, which is the **same instant** as `11:46:27+02:00`,
  so a `11:46+02:00` stamp sorted *below* it in UTC and the document failed
  `style.update_history.history_order`. The repair is a re-stamp to the time this text actually
  reached its current form, not a reordering of anyone else's entry and not an invented future stamp.
  `lastUpdated` advances with this body edit; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are
  deliberately unchanged because the source is an uncommitted candidate and the governed closeout owns
  the real code and memory commits.
- 2026-09-18T09:46:27+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:236-236. No content impact: mechanical anchor-range projection bound to citation source snapshot 8e3e09b7b677dec09df0166f3450a2d9625d30e9bcf243ce7027ad865fd26365; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:188-188. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:250-250. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:184-184. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:236-236. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:174-174; mcp/tests/test-evidence-lanes.toml:173-173. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:250-250. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:184-184. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:236-236. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:276-276. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:261-261. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:242-242. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:188-188. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:250-250. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:184-184. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:236-236. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:174-174; mcp/tests/test-evidence-lanes.toml:173-173. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:250-250. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:213-213. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:184-184. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:236-236. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:276-276. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:261-261. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:242-242. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 2 claim(s) here (2 x citation_claim_reopened). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_state_signal_curator_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:134-134. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_state_signal_worker_wake.py" repointed to mcp/tests/test-evidence-lanes.toml:137-137. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py" repointed to mcp/tests/test-evidence-lanes.toml:97-97. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_terminal_observer_health.py" repointed to mcp/tests/test-evidence-lanes.toml:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:130-130. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_serving_observation_loop.py" repointed to mcp/tests/test-evidence-lanes.toml:128-128. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:186-186. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:172-172; mcp/tests/test-evidence-lanes.toml:171-171. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "integration_case_budget = 400" repointed to pyproject.toml:323-323. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:93-93. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:99-99. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:227-227. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:202-202. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:98-98. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:205-205. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:248-248. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:211-211. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:194-194. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:182-182. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:234-234. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:133-133. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:274-274. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "provider-conformance" repointed to mcp/tests/test-evidence-lanes.toml:259-259. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "architecture-fitness" repointed to mcp/tests/test-evidence-lanes.toml:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 79 generated projection bullet(s) by hand while resolving the memory sync** — `architecture-fitness`, `provider-conformance`, `stress-durability`, `mcp/tests/test_state_signal_boundary_delivery.py`, `mcp/tests/test_worktree_status_terminal_next_tool.py`, `mcp/tests/test_checkpoint_landing_end_to_end.py`, `mcp/tests/test_cross_master_concurrency.py`, `mcp/tests/test_pause_stop_only_end_to_end.py` and 20 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): re-read this leaf's own two lane rows against the manifest's bytes and recorded what they oblige: both modules are `unit-regression` rows inserted **mid-list**, after the facet suite, which is the mechanical reason every later line of this file — and every route card citing into it — moved by two on this candidate. The section states the behaviour-preserving classification and why it is the honest one here (the suite's one integration-shaped question is answered by value over the registered read-scope fixture, inside the unit lane), and the measured populations that show no ceiling moved: **1341** unit against the pinned unit budget literal and **322** integration against the integration budget literal. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded the two new unit-regression rows and the line shifts their insertion caused in every card that cites this manifest. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.
- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 107 generated projection bullet(s) by hand** — `architecture-fitness`, `provider-conformance`, `stress-durability`, `migration`, `mcp/tests/test_state_signal_boundary_delivery.py`, `mcp/tests/test_worktree_status_terminal_next_tool.py`, `mcp/tests/test_checkpoint_landing_end_to_end.py`, `mcp/tests/test_cross_master_concurrency.py` and 30 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 35 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"architecture-fitness"` → `mcp/tests/test-evidence-lanes.toml:232-232`; `"provider-conformance"` → `mcp/tests/test-evidence-lanes.toml:251-251`; `"stress-durability"` → `mcp/tests/test-evidence-lanes.toml:266-266`; `"mcp/tests/test_state_signal_boundary_delivery.py"` → `mcp/tests/test-evidence-lanes.toml:128-128`; `"mcp/tests/test_worktree_status_terminal_next_tool.py"` → `mcp/tests/test-evidence-lanes.toml:227-227`; `"mcp/tests/test_checkpoint_landing_end_to_end.py"` → `mcp/tests/test-evidence-lanes.toml:175-175`; `"mcp/tests/test_cross_master_concurrency.py"` → `mcp/tests/test-evidence-lanes.toml:187-187`; `"mcp/tests/test_pause_stop_only_end_to_end.py"` → `mcp/tests/test-evidence-lanes.toml:204-204`; `"mcp/tests/test_pause_is_not_publication.py"` → `mcp/tests/test-evidence-lanes.toml:240-240`; `"mcp/tests/test_lifecycle_playthrough_end_to_end.py"` → `mcp/tests/test-evidence-lanes.toml:198-198`; `"mcp/tests/test_memory_attribution_producers.py"` → `mcp/tests/test-evidence-lanes.toml:93-93`; `"mcp/tests/test_leaf_doc_master_link_binding.py"` → `mcp/tests/test-evidence-lanes.toml:195-195`; `"mcp/tests/test_terminal_blocker_reasons.py"` → `mcp/tests/test-evidence-lanes.toml:220-220`; `"mcp/tests/test_memory_backfill.py"` → `mcp/tests/test-evidence-lanes.toml:94-94`; `"mcp/tests/test_knowledge_store.py"` → `mcp/tests/test-evidence-lanes.toml:88-88`; `"mcp/tests/test_knowledge_portable_roundtrip.py"; "mcp/tests/test_knowledge_portable_boundaries.py"` → `mcp/tests/test-evidence-lanes.toml:165-165; mcp/tests/test-evidence-lanes.toml:164-164`; `"mcp/tests/test_worktree_status_terminal_next_tool.py"` → `mcp/tests/test-evidence-lanes.toml:227-227`; `"mcp/tests/test_checkpoint_landing_end_to_end.py"` → `mcp/tests/test-evidence-lanes.toml:175-175`; `"mcp/tests/test_cross_master_concurrency.py"` → `mcp/tests/test-evidence-lanes.toml:187-187`; `"mcp/tests/test_pause_stop_only_end_to_end.py"` → `mcp/tests/test-evidence-lanes.toml:204-204`; `"mcp/tests/test_pause_is_not_publication.py"` → `mcp/tests/test-evidence-lanes.toml:240-240`; `"mcp/tests/test_lifecycle_playthrough_end_to_end.py"` → `mcp/tests/test-evidence-lanes.toml:198-198`; `"mcp/tests/test_leaf_doc_master_link_binding.py"` → `mcp/tests/test-evidence-lanes.toml:195-195`; `"mcp/tests/test_closeout_projection_source_classification.py"` → `mcp/tests/test-evidence-lanes.toml:179-179`; `"mcp/tests/test_terminal_blocker_reasons.py"` → `mcp/tests/test-evidence-lanes.toml:220-220`; `"mcp/tests/test_memory_backfill.py"` → `mcp/tests/test-evidence-lanes.toml:94-94`; `"mcp/tests/test_terminal_liveness_registration_order.py"` → `mcp/tests/test-evidence-lanes.toml:151-151`; `"mcp/tests/test_terminal_liveness_pane_authority.py"` → `mcp/tests/test-evidence-lanes.toml:222-222`; `"mcp/tests/test_serving_observation_loop.py"` → `mcp/tests/test-evidence-lanes.toml:123-123`; `"mcp/tests/test_serving_startup_prime.py"` → `mcp/tests/test-evidence-lanes.toml:125-125`; `"mcp/tests/test_terminal_observer_health.py"` → `mcp/tests/test-evidence-lanes.toml:152-152`; `"mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py"` → `mcp/tests/test-evidence-lanes.toml:92-92`; `"mcp/tests/test_state_signal_worker_wake.py"` → `mcp/tests/test-evidence-lanes.toml:132-132`; `"mcp/tests/test_terminal_observer_health.py"` → `mcp/tests/test-evidence-lanes.toml:152-152`; `"mcp/tests/test_state_signal_curator_wake.py"` → `mcp/tests/test-evidence-lanes.toml:129-129`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.
- 2026-09-18T04:05:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): **re-read the manifest against the current source and moved the population it states as a fact.** This leaf's change set inserts **two** rows — `mcp/tests/test_knowledge_citation_bindings.py` into the alphabetical knowledge run of `unit-regression` (row `:71`) and `mcp/tests/test_knowledge_citation_boundaries.py` as the opening row of `integration` (row `:162`) — so the declared population and the module count on disk both move **249 → 251**, and the lane counts move with them. The two-lane split is a classification rather than a convenience: the vocabulary module is hermetic (in-process models, the real registry, temporary directories) and the boundary module opens a real store and builds a real Git repository in most of its cases. Both rows are insertions inside a lane rather than appendices, which is the mechanical reason every later line of this file moved and why a batch of citations pointing into it needed re-pointing in the same change. Verification metadata is **not** advanced over unreviewed content: the body was re-read against the current source, and the code commit does not exist yet — closeout owns that stamp.
- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/test-evidence-lanes.toml:230-230` -> `mcp/tests/test-evidence-lanes.toml:232-232`; `mcp/tests/test-evidence-lanes.toml:249-249` -> `mcp/tests/test-evidence-lanes.toml:251-251`; `mcp/tests/test-evidence-lanes.toml:264-264` -> `mcp/tests/test-evidence-lanes.toml:266-266`; `mcp/tests/test-evidence-lanes.toml:225-225` -> `mcp/tests/test-evidence-lanes.toml:226-226`; `mcp/tests/test-evidence-lanes.toml:173-173` -> `mcp/tests/test-evidence-lanes.toml:174-174`; `mcp/tests/test-evidence-lanes.toml:185-185` -> `mcp/tests/test-evidence-lanes.toml:186-186`; `mcp/tests/test-evidence-lanes.toml:202-202` -> `mcp/tests/test-evidence-lanes.toml:203-203`; `mcp/tests/test-evidence-lanes.toml:238-238` -> `mcp/tests/test-evidence-lanes.toml:240-240`; `mcp/tests/test-evidence-lanes.toml:196-196` -> `mcp/tests/test-evidence-lanes.toml:197-197`; `mcp/tests/test-evidence-lanes.toml:193-193` -> `mcp/tests/test-evidence-lanes.toml:194-194`; `mcp/tests/test-evidence-lanes.toml:218-218` -> `mcp/tests/test-evidence-lanes.toml:219-219`; `mcp/tests/test-evidence-lanes.toml:162-163` -> `mcp/tests/test-evidence-lanes.toml:163-164`; `mcp/tests/test-evidence-lanes.toml:225-225` -> `mcp/tests/test-evidence-lanes.toml:226-226`; `mcp/tests/test-evidence-lanes.toml:173-173` -> `mcp/tests/test-evidence-lanes.toml:174-174`; `mcp/tests/test-evidence-lanes.toml:185-185` -> `mcp/tests/test-evidence-lanes.toml:186-186`; `mcp/tests/test-evidence-lanes.toml:202-202` -> `mcp/tests/test-evidence-lanes.toml:203-203`; `mcp/tests/test-evidence-lanes.toml:238-238` -> `mcp/tests/test-evidence-lanes.toml:240-240`; `mcp/tests/test-evidence-lanes.toml:196-196` -> `mcp/tests/test-evidence-lanes.toml:197-197`; `mcp/tests/test-evidence-lanes.toml:193-193` -> `mcp/tests/test-evidence-lanes.toml:194-194`; `mcp/tests/test-evidence-lanes.toml:177-177` -> `mcp/tests/test-evidence-lanes.toml:178-178`; `mcp/tests/test-evidence-lanes.toml:218-218` -> `mcp/tests/test-evidence-lanes.toml:219-219`; `mcp/tests/test-evidence-lanes.toml:220-220` -> `mcp/tests/test-evidence-lanes.toml:221-221`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-18T03:15:00+00:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): recorded the **two new lane rows and the merged measurement they move**, and superseded the L8 section's "current account" heading because its counts no longer describe the file. The new section states each module's lane and why it is that lane (`test_knowledge_detection_runs.py` `:71` and `test_knowledge_detection_signals.py` `:72`, both `unit-regression`, each with the reason the classification holds), the merged measurement taken on the working candidate — **249 declared entries against 249 modules on disk, 0/0 undeclared or absent, 149 / 2 / 68 / 17 / 13 across the five lanes** — against the previous 247/247, the unchanged budget pair with the *pinned* `"unit_case_budget = 1500"` and `"integration_case_budget = 400"` literals, and the mechanical fact that matters to the rest of the memory tree: **a two-line insertion moves every later line of this manifest**, which is why a batch of citations pointing into this file needed re-pointing in the same change. It also records why the artifact populations stay at 13 contracts / 54 artifacts: the two modules use the already-registered `diff_scope_test_support` and `read_scope_test_support` fixtures rather than a third support module. Verification metadata advances to the leaf's base commit `4264dcc9` because the body was re-read against the current manifest; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T00:55:00+00:00 — 260915-KS-L24 curator (uncommitted change set on `ar/260915-ks-l24`, base `9c12e8b1`): **re-read the two budget rows this candidate falsified and re-cited them to the current pinned literals.** Both rows quoted the pinned key and value, and both quoted values left the file when the master's owning seat raised the pair at this candidate — `"integration_case_budget = 340"` and `"unit_case_budget = 1250"` now exist **nowhere in the code tree**, so the claims, not the pointers, were what needed re-reading. They now cite `"integration_case_budget = 400"` (`pyproject.toml:305`) and `"unit_case_budget = 1500"` (`pyproject.toml:304`), and each claim names the candidate that raised it. The rows' lane-choice reasoning is unchanged and still holds: the integration cap is what constrains lane choice, and an over-budget unit population makes `pytest_collection_finish` run no tests at all. No other row of this card was re-read in this pass. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:86-86. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:172-172. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:190-190. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:85-85. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:193-193. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:235-235. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:199-199. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:180-180. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:168-168. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:222-222. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:125-125. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: recorded this leaf's row addition — `tests/test_governing_overview_resolution.py` is registered in `test-evidence-lanes.toml`, so the new module is collectable into a lane rather than failing the fail-closed loader. `D9`'s loader was already complete at this leaf's base (243 modules / 243 rows); this leaf adds the 244th module and its row together. Verification metadata was already at this leaf's frozen code base.
- 2026-09-17T16:00+02:00 — 260915-CAPS-L11 curator (**final-verification leaf**): recorded this leaf's **six added rows** — the `D9` family the fail-closed loader had been naming since before this master (`test_eve_adapter`, `test_eve_protocol`, `test_role_capsule_admission`, `test_role_capsule_compiler`, `test_role_instruction_corpus`, `test_task_projection`), all `unit-regression`, with the loader now silent at **243 files / 0 overrides** and the six asserted to collect (**198** unit, **0** integration). Recorded the per-row lane reasoning, the `S-D9-lane-row-removed` seed that makes the loader **refuse by name**, and the method lesson from this leaf: **the registry digest must be asked of the product, never rebuilt by hand** (a hand-rebuilt `bfbd21af…` described the script's own rendering; the product's value is `61f9fba8…`). **Re-anchored every range in this card**, because the row insertions in three places moved them: 44 occurrences of a changed range were corrected to the line that now carries the named module or lane. Two `style.update_history.history_order` findings on this card are **not repaired here and must not be**: they are the cross-leaf stamp collision the ledger records as structural — each curator stamps with its own clock, so entries written into this *shared* card by two leaves can sort a later stamp below an earlier one, and satisfying the checker would need an invented future stamp, which the rules forbid. Every earlier entry, including L15's and L17's, is preserved as the dated record it is; no other leaf's entry was re-stamped or reordered.
- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: recorded this leaf's **one** added row
  (`mcp/tests/test_capsule_experiment_install.py:19`) and the unchanged `D9` set — the fail-closed
  loader names the same six modules at this tip as at the clean base, and this leaf's module is not a
  seventh. The `test_install_runtime.py` mention at `:74` is pre-existing catalog-consumer context,
  not a row this leaf added. Verification metadata remains closeout-owned (the candidate is
  uncommitted).
- 2026-09-17T01:31:11+00:00 — **Historical stamp carried from the incoming official line** (merge HEAD `12bd7fd3`; the live stamp for this file is the later synced value in the metadata table above, which closeout re-stamps): `lastUpdated` 2026-09-15T15:02+02:00; `lastVerifiedCommitHash` `806649b91bdce18f7b915bfbbf6727967f4e7a88`; `lastVerifiedCommitDate` 2026-09-16T12:23:53+02:00.
- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): stamped the untimestamped Update History entries with this document's own commit clock
- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `mcp/tests/test_knowledge_candidate_workspace.py` in the row 719 of this card from mcp/tests/test-evidence-lanes.toml:69-69 to mcp/tests/test-evidence-lanes.toml:70, the extent of the construct the claim is about (the checker named line(s) [70] as its live location); re-pointed `mcp/tests/test_knowledge_label_operations.py` in the row 717 of this card from mcp/tests/test-evidence-lanes.toml:18-19 to mcp/tests/test-evidence-lanes.toml:72, the extent of the construct the claim is about (the checker named line(s) [72] as its live location); re-pointed `mcp/tests/test_knowledge_snapshot_publication.py` in the row 719 of this card from mcp/tests/test-evidence-lanes.toml:70 to mcp/tests/test-evidence-lanes.toml:79, the extent of the construct the claim is about (the checker named line(s) [79] as its live location); re-pointed `migration` in the row 700 of this card from mcp/tests/test-evidence-lanes.toml:232-232 to mcp/tests/test-evidence-lanes.toml:260, the extent of the construct the claim is about (the checker named line(s) [260] as its live location)
- 2026-09-17T01:15:00+00:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): **recorded this leaf's two lane rows and re-measured the whole manifest rather than carrying L7's numbers.** The rows are `test_knowledge_diff_scope.py` (unit-regression, `:76`, 13 hermetic nodes) and `test_knowledge_diff_boundaries.py` (integration, `:159`, 15 nodes that drive the **production Git probe** over two real committed trees and a real curated candidate database) — each the module's behaviour-preserving classification, not a budget consequence. **The measured account: 243 declared entries against 243 modules on disk**, closed in both directions, 0 duplicates, with unit-regression 143 (`5-149`), public-contract 2 (`150-153`), integration 68 (`154-223`), architecture-fitness 17 (`224-242`), provider-conformance 13 (`243-257`) and the two empty lanes; against 241/241 after L7 and 238/238 on the merged base, so this leaf's two modules are the whole difference. The shared support module is named as a *governed artifact* (`knowledge-diff-cases`) rather than a lane row, and the card records that **the read-scope artifact's consumer list gained the same two paths** in this change. **The budget pair did not move**: 1250 / 340 with `pyproject.toml` clean, and the sizing question and its merged-line attribution are left exactly where L7 recorded them. The sentence that said the merged counts were pending now points at this leaf's measured account, and the earlier accounts are kept as as-of records. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T21:50:00+00:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): **recorded this leaf's three lane rows and, as the closing curator, produced the merged measurement the two labelled accounts were waiting for.** The rows are `test_knowledge_read_scope.py` (unit-regression, `:75`), `test_knowledge_read_boundaries.py` (integration, `:157`) and `test_knowledge_read_paths.py` (integration, `:158`), with the split explained as what it is — the 1 200-line hard limit was paid, not waived — and the shared support module named as a *governed artifact* rather than a lane row. **The merged counts are measured, not derived:** 241 declared entries against 241 modules on disk, with unit-regression 142 (`6-148`), public-contract 2 (`150-152`), integration 67 (`154-221`), architecture-fitness 17 (`223-240`), provider-conformance 13 (`242-255`) and the two empty lanes, and the merged base's own 238/238 recorded beside them so the difference is attributable rather than merged. The sentence that said the merged counts were *pending* now says they were measured and where they are recorded, and the earlier accounts are kept as as-of records under the memory doctrine. The card also carries the raised budget pair **1250 / 340** with the merged-line attribution stated as measured (official 1014/1100 green, KS parent 1003/1100 green, merged 1138/1100 red *before any L7 line*), the note that the raise is headroom rather than a target, and this leaf's own populations (unit 1138 → 1159, integration 279 → 304). Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: **one row added — `test_citation_source_index_membership.py`
  at `:26`, unit-regression** — and the population re-measured at this leaf's synced base `8997e184` plus
  its change set: **232 declared rows** against **238** modules on disk, leaving exactly the six
  pre-existing D9 modules unregistered (this leaf closed none of that gap and added no case to a capped
  population that was not already there). A new declared section carries the measurement and the
  behaviour-preserving lane rationale; the older "Current population" paragraph is now explicitly marked
  as the L7 candidate's measurement rather than the current one, because the insertion at `:26` moved
  every row below it and a reader must not take its 230/236 pair as current. Verification metadata moves
  to `8997e184` with the reviewed working candidate named; the candidate is deliberately uncommitted, so
  the governed closeout stamps the real code commit and no hash or fingerprint was invented here.
- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: **two rows added and the population re-measured at
  the current base.** Registered this leaf's `mcp/tests/test_eve_capsule_binding.py` in
  **unit-regression** (hermetic focused cases: no process, no Node) and
  `mcp/tests/test_eve_capsule_runtime.py` in **integration** (it executes the shipped TypeScript under a
  real Node). Added a measured `## Current population` section because the card's standing numbers were
  from an older base and no longer described the tree: **236** modules on disk, **230** manifest
  entries, unit-regression 134 (key `:5`), public-contract 2 (`:141`), integration 63 (`:145`),
  architecture-fitness 17 (`:210`), provider-conformance 14 (`:229`), stress-durability and migration
  empty. The loader's **one** finding — six test files with no explicit lane
  (`test_eve_adapter.py`, `test_eve_protocol.py`, `test_role_capsule_admission.py`,
  `test_role_capsule_compiler.py`, `test_role_instruction_corpus.py`, `test_task_projection.py`) — is
  recorded as **pre-existing at the pristine base** and none of it is this leaf's; this leaf adds two
  rows and closes none of that gap. Case budgets are recorded as `pyproject.toml`'s own
  (`unit_case_budget = 1500`, `integration_case_budget = 300`) and explicitly separated from lane
  membership, with the card's older 150/200/250/1000/1100 figures marked stale rather than edited out of
  the history. Verification metadata moves to the leaf's synced base `23cc7a72`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.
- 2026-09-16T15:45:00+00:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): registered the change set's two new knowledge modules and re-measured the whole manifest rather than carrying the L5 numbers — **221 declarations and 221 modules on disk**, with the current brackets unit-regression 127 at rows 6-132, public-contract 2 at 135-136, integration **63** at 139-201, architecture-fitness 16 at 204-219 and provider-conformance 13 at 222-234. Both additions are `test_knowledge_portable_roundtrip.py` and `test_knowledge_portable_boundaries.py` in the **integration** lane (rows 140-141), and the lane is forced rather than preferred: the unit population sits exactly at its declared 1000-case ceiling, and both modules are boundary executors (real databases under `tmp_path`, published closed files, destination bytes and directory contents measured). **The declared budget pair is corrected in this card**: `integration_case_budget` is now **300** at `pyproject.toml:186` (raised by this leaf's fix round with the doctrine-required dated tradeoff above the pair) and `unit_case_budget` stays **1000** at `pyproject.toml:185`; every earlier entry's `250` at `pyproject.toml:150` is stale, including the reference row that carried it — which is also the one pre-existing `citation_claim_reopened` finding this card owned, so that finding is cleared by re-pointing the claim at the key's current line and value. The lane-section layout is unchanged but a new leading section carries the current account so a reader does not have to reconstruct it from eight historical as-of records. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l06`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: registered the leaf's new
  `mcp/tests/test_codex_capsule_delivery.py` in the **provider-conformance** lane (entry row 216,
  between `test_codex_app_server_adapter_turns.py` and `test_harness_control_claude.py`) — its subject
  is the vendor app-server instruction channel, the same lane as its sibling `test_codex_app_server_*`
  modules, and its 28 cases carry no `integration` marker. Additive proof by the loader itself: 7
  findings including this module before the row, 6 after, and the module absent from them. Reconciled
  the brackets this insertion moved (provider-conformance 209-224, stress-durability 225-226,
  migration 227-228). Measured population at this candidate: 216 modules on disk, 210 rows (118
  unit-regression, 2 public-contract, 60 integration, 16 architecture-fitness, 14 provider-conformance),
  so the **six D9 modules remain unregistered** — named in the new section and left to L11.
  Classification only; verification metadata stays at the current committed base `c1dbebf8`.
- 2026-09-16T11:45:00+00:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): registered the change set's two new knowledge modules and re-measured the whole manifest rather than carrying the L4 numbers — **219 declarations and 219 modules on disk**, with the current brackets unit-regression 127 at rows 6-133, public-contract 2 at 135-136, integration 61 at 139-200, architecture-fitness 16 at 202-218 and provider-conformance 13 at 220-233. The two additions are `test_knowledge_guarded_merge.py` in **unit-regression** (row 73) and `test_knowledge_guarded_merge_boundaries.py` in **integration** (row 139); the split is a budget decision, because the unit population sits exactly at its declared 1000-case ceiling after this leaf and each boundary scenario needs its own three-commit Git world. Every entry-row citation in this card below the insertions was re-derived against the new bytes. Verification metadata remains closeout-owned.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "integration_case_budget = 250" repointed to pyproject.toml:159-159. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:83-83. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:211-211. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_closeout_projection_source_classification.py" repointed to mcp/tests/test-evidence-lanes.toml:168-168. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:186-186. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:82-82. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:189-189. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_pause_is_not_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_pause_stop_only_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:195-195. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:164-164. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_checkpoint_landing.py" repointed to mcp/tests/test-evidence-lanes.toml:27-27. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "mcp/tests/test_state_signal_boundary_delivery.py" repointed to mcp/tests/test-evidence-lanes.toml:122-122. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:(258, 258)-(258, 258). No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:43:27+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:(157, 221)-(157, 221). No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: **a second leaf's row, and the two merged
  additively.** This change set registers `mcp/tests/test_eve_product_integration.py` under
  `unit-regression` (line 52), inserted in the alphabetically-kept list between
  `test_environment_reconstruction.py` and `test_final_catalog_plan_attestation.py`. L4's row for
  `mcp/tests/test_capsule_serving.py` (line 19) arrived in the same file when the leaf's source branch
  advanced, and the two insertions merged without conflict — the loader now names exactly the six
  historical D9 modules and neither leaf's module is among them. The invariant the row exists for: the
  lane loader is fail-closed and raises `LaneManifestError` for any module under `testpaths` without
  an explicit row, which ordinary pytest never detects. Verification metadata moves to the leaf's
  synced base `ff97072c`; the candidate is deliberately uncommitted, so the governed closeout stamps
  the real code commit and no hash or fingerprint was invented here.
- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator (uncommitted change set on `ar/260915-caps-l4`, base
  `b00a4ac2`): registered the change set's new `mcp/tests/test_capsule_serving.py` in the
  **unit-regression** lane at entry row 19 — 19 of its 21 cases are hermetic and only its two
  real-process exchanges are marked `integration`, so the default unit lane is its
  behaviour-preserving classification — and re-measured rather than carried: 208 declared rows, 117
  unit-regression (5-121), 2 public-contract (124-126), 60 integration (128-189), 16
  architecture-fitness (190-207), 13 provider-conformance (208-222), stress-durability and migration
  empty. **Recorded the collection refusal as current state, not as a repair**: the default unit
  selection collects 1083 against `unit_case_budget = 1000` (`pyproject.toml:149`) and already
  collected 1064 against that ceiling at this leaf's base, so 64 of the 83-case overage predates it;
  `conftest.pytest_collection_finish` therefore raises `pytest.UsageError` before any case runs. The
  ceiling was not edited and the module was not moved into another lane to dodge the check — raising a
  declared budget needs an explicit tradeoff and is the owner's decision (`F-L4-01`, L11 owns the
  ceiling). Also recorded that the manifest declares 208 rows while **214** `test_*.py` modules exist
  on disk, the six undeclared modules being the pre-existing `D9` master-tip gaps owned by L11
  (`test_capsule_serving.py` is not among them). Corrected the Repo-Internal References table to add
  the L4 row and the unit-budget row; the one insertion at `:19` moves every cited row below it one
  line higher than this card's earlier entries record. Classification only: lane membership is not
  execution, certification or acceptance evidence, and the verification stamps remain closeout-owned.
- 2026-09-16T09:30:00+00:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): registered the change set's two new knowledge modules in the **unit-regression** lane — `test_knowledge_candidate_workspace.py` at row 69 and `test_knowledge_snapshot_publication.py` at row 75 — and re-measured the manifest rather than carrying the L3 numbers: **217 modules on disk and 217 declared entries** with no undeclared module and no stale row, 126 unit-regression (6-131), 2 public-contract (134-135), 60 integration (138-197), 16 architecture-fitness (200-215), 13 provider-conformance (218-230), and stress-durability (232) and migration (234) empty. Both modules are hermetic — `tmp_path` directories, in-process APSW databases driven through the real admitted destination and the real publication lock, and a child interpreter used only as a crash probe — so the default unit lane is each one's behaviour-preserving classification. Their insertion inside the alphabetical knowledge block is why the rows are 69 and 75 rather than adjacent, and it is also why every entry-row citation below moved by two: **this pass re-derived all of them against the working manifest** (the `unit-regression`, `integration`, `architecture-fitness`, `provider-conformance`, `stress-durability` and `migration` row citations plus the twelve per-leaf row citations), which clears the pre-existing `citation_anchor_absent_from_range` findings this card carried. Classification only, so lane membership is not execution or acceptance evidence; verification metadata remains closeout-owned.
- 2026-09-16T08:10:00+00:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): registered the change set's three new knowledge modules in the **unit-regression** lane — `test_candidate_batch_commands.py` and `test_candidate_batch_transaction.py` at entry rows 18-19, `test_knowledge_label_operations.py` at row 70; all three are hermetic and driven through the real admitted destination, no integration marker, no repository or subprocess — and re-measured the manifest rather than carrying the L2 numbers: 215 modules on disk and 215 declared entries with no undeclared module and no stale row, 124 unit-regression (5-130), 2 public-contract (131-134), 62 integration (135-196), 18 architecture-fitness (197-214), 13 provider-conformance (215-229), stress-durability and migration empty. The five earlier knowledge modules are now at rows 69-74 and were re-cited. Recorded again why the rows are load-bearing rather than bookkeeping: an unregistered module makes `load_lane_manifest` refuse the repository, which raises at collection. Classification only, so lane membership is not execution or acceptance evidence; verification metadata remains closeout-owned.
- 2026-09-16T06:24:00+00:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base
  `60e0820e`): registered the change set's four new knowledge modules in the **unit-regression** lane
  at entry rows 67-70 — `test_knowledge_family_revision.py`, `test_knowledge_graph_reads.py`,
  `test_knowledge_relation_rules.py` and `test_knowledge_revision_seals.py`; all four are hermetic
  (temporary directories, in-process APSW databases, no integration marker, no repository or
  subprocess), so the default unit lane is each one's behaviour-preserving classification — and
  re-measured the manifest rather than carrying the L1 numbers: 212 modules on disk and 212 declared
  entries with no undeclared module and no stale row, 121 unit-regression (entries 6-126), 2
  public-contract (129-130), 60 integration (133-192), 16 architecture-fitness (195-210), 13
  provider-conformance (213-225), stress-durability and migration empty. One of the four arrived in
  the fix-verification round as the evidence repair for sealed finding `260915-KS-L2-RV-1`, and its
  row was added in the same change. Recorded again why the rows are load-bearing rather than
  bookkeeping: an unregistered module makes `load_lane_manifest` refuse the repository, which raises
  `pytest.UsageError` at collection and quietly drops the quality path's retry proof. Classification
  only, so lane membership is not execution or acceptance evidence; verification metadata remains
  closeout-owned.
- 2026-09-15T20:40:00+00:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base
  `67b21aeb`): registered the change set's new `mcp/tests/test_knowledge_store.py` in the
  **unit-regression** lane at entry row 67 — the module is hermetic (temporary directories, in-process
  APSW databases, no integration marker, no repository or subprocess), so the default unit lane is its
  behaviour-preserving classification — and re-measured the manifest rather than carrying the L3
  numbers: 208 modules on disk and 208 declared entries with no undeclared module and no stale row,
  117 unit-regression (entries 6-122), 2 public-contract (125-126), 60 integration (129-188),
  16 architecture-fitness (191-206), 13 provider-conformance (209-221), stress-durability and
  migration empty. Recorded why the row is load-bearing rather than bookkeeping: an unregistered
  module makes `load_lane_manifest` refuse the repository, which raises `pytest.UsageError` at
  collection and quietly drops the quality path's retry proof. Classification only, so lane
  membership is not execution or acceptance evidence; verification metadata remains closeout-owned.
- 2026-09-15T21:40+02:00 — 260831-LOCR-L05 curator, **re-dispatch** (uncommitted change set on
  `ar/260831-locr-l05`, pair code base `67c91534`, memory base `309110f8`,
  `mcp/tests/test-evidence-lanes.toml` +1/−0): registered the change set's new
  `mcp/tests/test_state_signal_worker_wake.py` in the **unit-regression** lane at file line `:105`,
  immediately below `test_state_signal_restart_recovery.py` at `:104` and above
  `test_structural_dispatch_recovery.py` at `:106` — the module seeds owned worker and manager seats
  on a real `TerminalCatalog`, drives the real `run_agent_notifier_sweep` over a temporary
  coordination root with real task documents and the real durable stores, issues no HTTP request,
  starts no server and starts no process, and asserts the whole inbox store rather than its
  state-signal subset, so the hermetic default unit lane is its behaviour-preserving classification.
  Re-measured the manifest against the candidate rather than carrying the L06 numbers: 216 modules on
  disk and 216 manifest entries, every module listed exactly once and no path duplicated — 123
  unit-regression (key `:5`, rows 6-128), 2 public-contract (key `:130`), 62 integration (key `:134`),
  16 architecture-fitness (key `:198`) and 13 provider-conformance (key `:216`), with
  stress-durability (`:231`) and migration (`:233`) empty; the live test-module derivation and the
  manifest therefore agree module for module and the fail-closed load holds. No existing row changed
  lane and no case budget was raised (the declared case budgets live in `pyproject.toml`, which is
  their authority). **Every citation in this card and in `overview.md` whose anchored row this
  insertion moved was re-derived against the candidate rather than carried** — the insertion sits in
  the unit run above the rows those tables cite, so 20 citations in this card and 8 in the route
  overview moved by one line and were repointed; the 686 `style.citations.range_resolution` findings
  the up-front check reports are pre-existing legacy drift on other files and were left alone. Scope
  note: this is a preservation leaf — `mcp/src` is byte-unchanged (`git status --porcelain` = the
  modified manifest plus the untracked module; `mcp/src` diff = 0 files). Classification only: lane
  membership is not execution, certification or acceptance evidence, and the verification stamps
  remain closeout-owned.
- 2026-09-15T19:40:00+00:00 — 260831-LOCR-L05 curator, **re-dispatch** (uncommitted change set on
- 2026-09-15T21:25+02:00 — 260831-LOCR-L04 curator (uncommitted change set on `ar/260831-locr-l04`,
  base `e9678c56`, `mcp/tests/test-evidence-lanes.toml` +1/−0): registered the change set's new
  `mcp/tests/test_serving_notifier_handoff.py` in the **unit-regression** lane at file line `:97`,
  between `test_semantic_topology_refusals.py` at `:96` and `test_serving_observation_loop.py` at `:98`.
  The module is the proof half of a preservation leaf: it enters the real `_serving_lifespan` under a
  deadline-correct virtual clock and measures the observer-to-notifier handoff latency against the
  oracle's bound and its decomposition, with no HTTP request, no server and no process, so the hermetic
  default unit lane is its behaviour-preserving classification. The leaf's two support modules
  (`_handoff_clock.py`, `_serving_handoff.py`) take no row, by the same rule that keeps the directory's
  other support modules out of the manifest. Re-measured at base `e9678c56` plus this change set:
  **215** modules on disk and **215** manifest entries — unit-regression **122** (key `:5`, rows 6-127,
  next key `:129`), public-contract 2 (`:129`), integration 62 (`:133`, rows 134-195),
  architecture-fitness 16 (`:197`), provider-conformance 13 (`:215`), stress-durability (`:230`) and
  migration (`:232`) empty. No case budget is quoted here and none was raised; `pyproject.toml` is the
  authority. **Because this insertion at `:97` sits above every previously-latest unit row, it moved
  every later manifest line by one**, so the citations into this file were re-derived against the
  current manifest rather than carried — 59 live citations in this card, the tests route overview and
  fifteen sibling cards; dated `## Update History` entries were left as written as-of records, and one
  citation already stale before this leaf (the L34 boundary suite at `:143-143` → `:140-140`) was
  corrected to the line that carries it. Verification metadata remains closeout-owned; no stamp
  advanced.
- 2026-09-15T19:25:00+00:00 — 260831-LOCR-L04 curator (uncommitted change set on `ar/260831-locr-l04`,
- 2026-09-15T21:21+02:00 — 260831-LOCR-L06 curator, **re-dispatch** (uncommitted change set on
  `ar/260831-locr-l06`, pair code base `e9678c56`, memory base `ee93a0fc`,
  `mcp/tests/test-evidence-lanes.toml` +1/−0): registered the change set's new
  `mcp/tests/test_lifecycle_owned_completion_relay_reviewer.py` in the **unit-regression** lane at
  file line `:68`, immediately below `test_lifecycle_operation_model_helpers.py` at `:67` and above
  `test_memory_attribution_producers.py` at `:69` — the module drives the real terminal observer, the
  production terminal-evidence lift and the real notifier sweep over a temporary coordination root,
  with no HTTP request, no server and no process, so the hermetic default unit lane is its
  behaviour-preserving classification. Re-measured the manifest against the candidate rather than
  carrying the L17 numbers: 215 modules on disk and 215 manifest entries — 122 unit-regression (key
  `:5`, rows 6-127), 2 public-contract (key `:129`), 62 integration (key `:133`), 16
  architecture-fitness (key `:197`), 13 provider-conformance (key `:215`), stress-durability (`:230`)
  and migration (`:232`) empty. Unlike the L17 and L18 insertions this row lands **above** the rows
  this card cites, so every manifest citation in the module table at or below `:68` was re-derived
  against the candidate — the L4/L5/L7/L8/L23/L27/L34/L36/L37/L01/L17 module rows plus the
  `integration` and `stress-durability` key lines — and this card's purpose paragraph was
  re-measured with them. `LOCR-R09@v1`, `LOCR-R11@v1` and `LOCR-R18@v1` classifications are
  untouched: no existing row changed lane and no case budget was raised, the budget authority
  remaining `pyproject.toml`. The leaf is a preservation leaf, so no production byte moved.
  Verification metadata remains closeout-owned; no stamp advanced.
- 2026-09-15T19:21:00+00:00 — 260831-LOCR-L06 curator, **re-dispatch** (uncommitted change set on
- 2026-09-15T21:19+02:00 — 260831-LOCR-L07 curator (uncommitted change set on `ar/260831-locr-l07`,
  base `e9678c56`, `mcp/tests/test-evidence-lanes.toml` +1/−0): registered the change set's new
  `mcp/tests/test_state_signal_curator_wake.py` in the **unit-regression** lane at file line `:102`,
  between its two alphabetically adjacent state-signal siblings — the module drives the real
  `TerminalCatalogLivenessSweeper`, the real agent-notifier sweep and the real `run_agent_notifier_sweep`
  over temporary catalogs, an in-process tmux host and an accepting paster double, with no HTTP
  request, no server and no process, so the hermetic default unit lane is its behaviour-preserving
  classification, the same lane its three siblings hold for the same reason. Re-measured the manifest
  against the candidate rather than carrying the L17 numbers: **215** modules on disk and 215 manifest
  entries — 122 unit-regression (key `:5`, bracket `:5-127`), 2 public-contract (key `:129`), 62
  integration (key `:133`, bracket `:134-195`), 16 architecture-fitness (key `:197`), 13
  provider-conformance (key `:215`), with stress-durability (`:230`) and migration (`:232`) empty. The
  Purpose paragraph now opens with that measured population instead of the L17 214-module figure it
  previously presented as current, and the L17 measurement is retained below as its own as-of record.
  Every live line reference in the module table that this insertion moved (target line `:102` or
  below) was re-derived against the manifest as it now stands; three of them — the L34, L36 and L37
  rows — were already four to six lines adrift of the source before this leaf and are now cited at
  their measured lines, and the per-row prose "row N now" figures of an earlier era were left as
  found. This is a preservation leaf: `mcp/src` is unchanged by the change set, and no case budget was
  touched — `pyproject.toml` remains the authority for the pinned budgets. Classification only: lane
  membership is not execution, certification or acceptance evidence, and the verification stamps
  remain closeout-owned.
- 2026-09-15T19:19:00+00:00 — 260831-LOCR-L07 curator (uncommitted change set on `ar/260831-locr-l07`,
- 2026-09-15T18:42:00+00:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`,
  base `99534dc5`, `mcp/tests/test-evidence-lanes.toml` +1/−0): registered the change set's new
  `mcp/tests/test_terminal_observer_health.py` in the **unit-regression** lane at file line `:122`,
  immediately below `test_terminal_liveness_registration_order.py` at `:121` — the module drives
  the record, the writer, the serving-lifetime accumulator and the real `_state_response` handler
  and `stream_events` generator against stub projectors, with no HTTP transport, no server and no
  process, so the hermetic default unit lane is its behaviour-preserving classification. Re-measured
  the manifest against the candidate rather than carrying the L18 numbers: 214 modules on disk and
  214 manifest entries — 121 unit-regression (key `:5`, rows 6-126), 2 public-contract (key
  `:128`), 62 integration (key `:132`), 16 architecture-fitness (key `:196`), 13 provider-conformance
  (key `:214`), stress-durability (`:229`) and migration (`:231`) empty. The insertion sits below
  `test_serving_observation_loop.py` (`:97`) and `test_serving_startup_prime.py` (`:98`), so no row
  this card cites from `LOCR-R11@v1` or `LOCR-R18@v1` moved; the L18 measurement is retained below
  as its own as-of record. Every line reference in the module table was re-derived against the
  candidate (the L34/L36/L37/L38 and seal-removal rows had drifted by one to six lines as later
  insertions moved them). Verification metadata remains closeout-owned; no stamp advanced.
- 2026-09-15T13:02:00+00:00 — 260831-LOCR-L18 curator (uncommitted change set on `ar/260831-locr-l18`,
  base `d868486c`): registered the change set's new `mcp/tests/test_serving_startup_prime.py` in the
  **unit-regression** lane at file line `:98`, immediately below its sibling
  `test_serving_observation_loop.py` at `:97` — the module drives the real `_serving_lifespan` under a
  temporary catalog, a virtual clock, an in-process fake tmux host and parked sibling loops, with no
  HTTP request and no process, so the hermetic default unit lane is its behaviour-preserving
  classification, the same lane and reason as its sibling. Re-measured the manifest against the
  candidate rather than carrying the L27 numbers: 213 modules on disk and 213 manifest entries — 120
  unit-regression (key `:5`, bracket `:5-125`, next key `:127`), 2 public-contract (`:127`), 62
  integration (key `:131`, bracket `:131-193`), 16 architecture-fitness (`:195`), 13
  provider-conformance (`:213`), with stress-durability (`:228`) and migration (`:230`) empty. The
  Purpose paragraph now opens with that measured population instead of the L27 211-module figure it
  previously presented as current, and three reference rows were added (the L18 row, the
  unit-regression bracket, the integration bracket). No existing row changed lane and no case budget
  was raised; the integration ceiling stays 250 (`pyproject.toml:150`). Classification only: lane
  membership is not execution, certification or acceptance evidence, and the verification stamps
  remain closeout-owned.
- 2026-09-15T13:57+02:00 — 260831-LOCR-L02 curator (uncommitted change set on `ar/260831-locr-l02`,
  base `67b21aeb`): registered the change set's new `mcp/tests/test_serving_terminal_catalog_read.py`
  in the **integration** lane (entry row 171) — it drives the real registered route over
  `fastapi.testclient.TestClient` and the real composed `create_app`, so the boundary lane is its
  behaviour-preserving classification — and re-measured the manifest rather than carrying a count:
  208 modules on disk and 208 manifest entries, 116 unit-regression, 2 public-contract, 61
  integration, 16 architecture-fitness, 13 provider-conformance, stress-durability and migration
  empty, with the 250-case integration ceiling (`pyproject.toml:150`) unchanged and no budget raised.
  A `## 260831-LOCR-L02 Lane Row (Declared)` section records the measurement and states explicitly
  that it is this leaf's as-of population over base `67b21aeb`, because concurrent sibling leaves
  landed their own rows on the same source branch. The Purpose paragraph gained the matching clause.
  Verification metadata stays closeout-owned: the candidate is uncommitted, so no stamp advanced.
- 2026-09-15T11:57:00+00:00 — 260831-LOCR-L02 curator (uncommitted change set on `ar/260831-locr-l02`,
- 2026-09-15T13:36+02:00 — 260831-LOCR-L27 curator (uncommitted change set on `ar/260831-locr-l27`,
  base `b368b661`): registered the change set's new `mcp/tests/test_terminal_liveness_pane_authority.py`
  in the **integration** lane at file line 181, between `test_terminal_liveness.py` at `:180` and
  `test_tools.py` at `:182`. The module is hermetic, but it takes the lane of its sibling
  `test_terminal_liveness.py`, and a new module of this family needs its own row or its application
  imports run inside ordinary unit collection — that is why the leaf added a lane entry at all. The
  module is the family's first **addition** rather than an extension: extending
  `test_terminal_liveness.py` in place reached 1094 lines, inside the `system/coding-guidelines.md`
  900-1200 band, so the proof was split out and the sibling stayed byte-unchanged. Re-measured the
  manifest rather than carrying the L23 numbers: 209 modules on disk and 209 manifest entries, 117
  unit-regression (file lines 5-123), 2 public-contract (124-127), **61** integration (128-190), 16
  architecture-fitness (191-208), 13 provider-conformance (209-223), stress-durability and migration
  empty. The insertion moved only the integration, architecture-fitness and provider-conformance file
  lines and left every unit-regression and public-contract row untouched; no existing row changed lane
  and no case budget was raised (the integration ceiling stays 250, `pyproject.toml:150`). Three stale
  bracket citations in this card's Repo-Internal References table were repaired in the same pass, and
  the Purpose paragraph now opens with the current population before the L23-measured text it
  previously presented as current. Classification only: lane membership is not execution,
  certification or acceptance evidence, and the verification stamps remain closeout-owned.
- 2026-09-15T11:36:00+00:00 — 260831-LOCR-L27 curator, **second post-sync reconciliation** (final
  measurement for this leaf; the base advanced once more, `163ba8a9` → `52bee429`, as L10 landed in the
  unit lane): the memory sync fast-forwarded cleanly with all five of this card's change-set files
  restored, and the manifest was re-measured at the new base **plus** this change set: 211 modules on
  disk and 211 manifest entries — 119 unit-regression (key `:5`, next key `:126`), 2 public-contract
  (`:126`), 61 integration (`:130`), 16 architecture-fitness (`:193`), 13 provider-conformance
  (`:211`), with stress-durability (`:226`) and migration (`:228`) empty. This module's row sits at
  file line `:183`, entry ordinal **53 of 61** in the integration lane, between
  `test_terminal_liveness.py` at `:182` and `test_tools.py` at `:184`. **This is the figure the card
  now carries**; `:182` was the `163ba8a9` measurement and `:181` is this candidate's build base,
  which the leaf's verdict and worker report cite. The unit-regression bracket citation was corrected
  from `:5-124` to `:5-125` in the same pass. Every one of these shifts is a sibling unit-lane
  insertion moving the file lines of a row this leaf never touched: this leaf's own manifest delta is
  exactly one inserted integration row and no lane, budget or production change. Verification metadata
  is pinned to `52bee429` (code) — the closeout transaction stamps the final commit.
- 2026-09-15T11:36:00+00:00 — 260831-LOCR-L27 curator, **post-sync reconciliation** (same change set;
  the memory sync advanced the base from `b368b661` to `163ba8a9` and parked this card's WIP over the
  two incoming memory commits): the sync brought L01's own declared-row section into this card, which
  collided with the L27 section above in the same region, so both sections were kept and reconciled
  rather than one being dropped. The incoming line numbers were re-measured rather than carried: at
  base `163ba8a9` **plus** this change set the manifest holds 209 modules on disk and 209 entries —
  118 unit-regression (key `:5`, next key `:125`), 2 public-contract (`:125`), 61 integration
  (`:129`), 16 architecture-fitness (`:192`), 13 provider-conformance (`:210`), with
  stress-durability (`:225`) and migration (`:227`) empty. L01's unit-lane insertion at `:97` moved
  every row below it down one line, so this module's own row now sits at `:182` (it was `:181` on this
  candidate's build base, which is the figure the leaf's verdict and worker report cite), and the
  Purpose paragraph and the three later lane-bracket citations were recomputed against that base. No
  row changed lane and no case budget moved. The merge is a memory-side reconciliation only: no
  production byte and no entry in the manifest itself was authored by this pass.
- 2026-09-15T11:36:00+00:00 — 260831-LOCR-L27 curator (uncommitted change set on `ar/260831-locr-l27`,
- 2026-09-15T11:20:00+00:00 — 260831-LOCR-L23 curator (uncommitted change set on `ar/260831-locr-l23`,
  base `67b21aeb`): registered the change set's new `mcp/tests/test_terminal_liveness_registration_order.py`
  in the **unit-regression** lane at entry row 118 — the module drives the real `TerminalCatalog` over
  `tempfile` catalogs and the real `TerminalCatalogLivenessSweeper.refresh` with in-process
  registrar/compactor doubles and no `worktree_services`, so it is hermetic and the default unit lane
  is its behaviour-preserving classification, the same lane as its sibling at `:117`. Re-measured the
  manifest rather than carrying the L3 numbers: 208 modules on disk and 208 manifest entries, 117
  unit-regression (5-122), 2 public-contract (123-126), 60 integration (127-188), 16
  architecture-fitness (189-206), 13 provider-conformance (207-221), with stress-durability (222-223)
  and migration (224-225) empty. The insertion moved **no** other row: row 118 is bracketed by
  `test_terminal_liveness_deferred_work.py` at `:117` and `test_terminal_paste.py` at `:119`, both
  alphabetically adjacent, so every citation below that does not name the unit bracket is unchanged;
  the Purpose population sentence and the unit bracket citation were the two that moved. No lane
  changed and no case budget was raised. Classification only: lane membership is not execution,
  certification or acceptance evidence, and the verification stamps remain closeout-owned.
- 2026-09-15T11:19:00+00:00 — 260831-LOCR-L01 curator (uncommitted change set on `ar/260831-locr-l01`,
  base `67b21aeb`): registered the change set's new `mcp/tests/test_serving_observation_loop.py` in
  the **unit-regression** lane at entry row 97 — the module injects fakes, issues no HTTP request,
  starts no process and publishes nothing, so the default unit lane is its behaviour-preserving
  classification — and re-measured the manifest rather than carrying the L3 numbers: 208 modules on
  disk and 208 manifest entries, 117 unit-regression (key `:5`), 2 public-contract (`:124`),
  60 integration (`:128`), 16 architecture-fitness (`:190`), 13 provider-conformance (`:208`), with
  stress-durability (`:223`) and migration (`:225`) empty. The insertion sits at `:97` between
  `test_semantic_topology_refusals.py` and `test_signal_routing.py`, so every later lane key is one
  line higher than the L3 entry recorded; the Purpose paragraph's 207/207 and 116 figures are that L3
  measurement, not this one. Because the insertion moves every later row, this card's own lane
  citations were re-derived against the current manifest rather than carried:
  `test_state_signal_boundary_delivery.py` `:99` → `:100`, `test_checkpoint_landing_end_to_end.py`
  `:134` → `:135`, `test_closeout_projection_source_classification.py` `:138` → `:139`,
  `test_cross_master_concurrency.py` `:146` → `:147`, `test_leaf_doc_master_link_binding.py` `:154` →
  `:155`, the playthrough `:157` → `:158`, `test_pause_stop_only_end_to_end.py` `:163` → `:164`,
  `test_terminal_blocker_reasons.py` `:178` → `:179`,
  `test_worktree_status_terminal_next_tool.py` `:184` → `:185`,
  `test_pause_is_not_publication.py` `:196` → `:197`, the `integration` lane key `:127` → `:128`, and
  the empty-lane keys `:222`/`:224` → `:223`/`:225`; the four lane brackets were re-measured the same
  way (`unit-regression` `5-121` → `5-122`, `integration` `127-188` → `128-189`,
  `architecture-fitness` `189-206` → `190-207`, `provider-conformance` `207-221` → `208-222`).
  Classification only: lane membership is not execution or acceptance
  evidence, and the verification stamps remain closeout-owned.
- 2026-09-15T11:15:00+00:00 — 260831-LOCR-L10 curator: registered the change set's new `mcp/tests/test_state_signal_restart_recovery.py` in the **unit-regression** lane at entry row `:101` — its seven cases drive one temporary durable world per case through the retained sweep/action entry points with an injected store fault or a structural rebind, so the hermetic default lane is its behaviour-preserving classification — and re-measured the manifest rather than carrying the L3 numbers: 208 modules on disk and 208 manifest entries, 117 unit-regression (5-122), 2 public-contract (124-126), 60 integration (128-188), 16 architecture-fitness (190-206), 13 provider-conformance (208-221), stress-durability and migration empty. The insertion sits near the end of the unit run, so no row this card cites moved. The module's own card owns the case inventory; this row is selection and cost classification only. Verification metadata remains closeout-owned.
- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): registered the change set's new `mcp/tests/test_memory_backfill.py` in the
  **unit-regression** lane at entry row 69 — its cases drive the backfill plan and apply paths against
  disposable `tempfile` repositories and the module carries no integration marker, so the default unit
  lane is its behaviour-preserving classification — and re-measured the manifest rather than carrying
  the L8 numbers: 207 modules on disk and 207 manifest entries, 116 unit-regression (5-121), 2
  public-contract (123-126), 60 integration (127-188), 16 architecture-fitness (189-206), 13
  provider-conformance (207-221), with stress-durability (222-223) and migration (224-225) empty. The
  insertion sits at `:69`, so every cited row below it moved one line and was re-cited:
  `test_state_signal_boundary_delivery.py` `:98` → `:99`, `test_checkpoint_landing_end_to_end.py`
  `:133` → `:134`, `test_cross_master_concurrency.py` `:145` → `:146`,
  `test_lifecycle_playthrough_end_to_end.py` `:156` → `:157`, `test_pause_stop_only_end_to_end.py`
  `:162` → `:163`, `test_terminal_blocker_reasons.py` `:177` → `:178`,
  `test_worktree_status_terminal_next_tool.py` `:183` → `:184`, `test_pause_is_not_publication.py`
  `:195` → `:196`, `test_leaf_doc_master_link_binding.py` `:153` → `:154`,
  `test_closeout_projection_source_classification.py` `:137` → `:138`, the L38 `integration` key
  `:126` → `:127`, and the empty-lane keys `:221`/`:223` → `:222`/`:224`.
  `test_checkpoint_landing.py` (`:24`) and `test_memory_attribution_producers.py` (`:68`) sit above the
  insertion and are unchanged, and the Purpose paragraph plus the L5, L7 and L8 bracket notes were
  corrected to the measured L3 population; classification only, so lane membership is not execution
  or acceptance evidence and the verification stamps remain closeout-owned.
- 2026-09-14T15:20:00+00:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
- 2026-09-14T13:05:00+00:00 — 260913-LCA-L8 curator (uncommitted change set on `ar/260913-lca-l8-ar`):
  registered the change set's new `mcp/tests/test_terminal_blocker_reasons.py` in the **integration**
  lane (entry row 177) — it builds a real landed leaf over disposable code and external-memory
  repositories and drives the public landing, integration and `lifecycle_finalize_task` routes, so
  that is its behaviour-preserving lane — and reconciled the population and every lane bracket against
  the current manifest, measured rather than carried: 206 modules on disk and 206 manifest entries,
  115 unit-regression (5-120), 2 public-contract (122-124), 60 integration (126-186), 16
  architecture-fitness (188-204), 13 provider-conformance (206-219), with stress-durability and
  migration empty. The same change set also corrected three out-of-order consumer entries in
  `evidence-lifecycle.toml`, which moves the L5 row up one line (`:316` → `:315`) and the L4 row down
  one (`:319` → `:320`) without changing any lane. Two rows this card cites after the insertion are
  one line higher than the L7 entry recorded: `test_worktree_status_terminal_next_tool.py`
  `:182` → `:183` and `test_pause_is_not_publication.py` `:194` → `:195`; re-derived the bracket rows
  (`126-185` → `126-186`, `187-203` → `188-204`, `205-218` → `206-219`, the empty-lane keys
  `220-220`/`222-222` → `221-221`/`223-223`) and corrected two rows that were already one line short
  of their entries (`test_checkpoint_landing_end_to_end.py` `:132` → `:133` and
  `test_cross_master_concurrency.py` `:143` → `:145`). Classification only: lane membership is not
  execution or acceptance evidence, and the verification stamps remain closeout-owned.
- 2026-09-14T12:20:00+00:00 — 260913-LCA-L7 curator (uncommitted change set on `ar/260913-lca-l7`):
  registered the change set's new `mcp/tests/test_closeout_projection_source_classification.py` in the
  **integration** lane (entry row 137) — it composes the real `QueueFixture` over temporary Git
  repositories and drives the production graph admission and projection path, so that is its
  behaviour-preserving lane — and reconciled the population and every lane bracket against the current
  manifest, measured rather than carried: 205 modules on disk and 205 manifest entries, 115
  unit-regression (5-120), 2 public-contract (122-124), 59 integration (126-185), 16 architecture-fitness
  (187-203), 13 provider-conformance (205-218), with stress-durability and migration empty. The single
  insertion sits before rows this card cites, so each of them is one line higher than the L5 entry
  recorded: `test_leaf_doc_master_link_binding.py` `:152` → `:153`, the playthrough `:155` → `:156`, the
  pause suite `:161` → `:162`, the L32 suite `:181` → `:182` and the pause architecture guard `:193` →
  `:194`, with the integration bracket `126-184` → `126-185`; added the L7 registration row and the
  reference row for it, and left every per-leaf section above as its own as-of record. Classification
  only: lane membership is not execution or acceptance evidence, and the verification stamps remain
  closeout-owned.
- 2026-09-14T05:05:00+00:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): registered the change set's new `mcp/tests/test_leaf_doc_master_link_binding.py` in the
  **integration** lane (entry row 152) — it drives the real public `worktree_start` over one disposable
  code repository and one external-memory repository per case, so that is its behaviour-preserving lane —
  and reconciled the population and every lane bracket against the current manifest, measured rather than
  carried from the previous entry: 204 modules on disk and 204 manifest entries, 115 unit-regression
  (entry rows 6-120), 2 public-contract (123-124), 58 integration (127-184), 16 architecture-fitness
  (187-202), 13 provider-conformance (205-217), with stress-durability and migration empty. **Also
  corrected the L4 section, which recorded an open gap that no longer exists**: measured at base
  `52875e7a`, `test_memory_attribution_producers.py` holds its lane row at `:68` in `unit-regression`, so
  the 203-modules/203-entries population held at this leaf's base and the fail-closed load failure the L4
  entry predicted was already repaired by the commit that landed L4. Re-derived every position this card
  cites against the current manifest by line number (integration `126-184`, architecture-fitness
  `186-202`, provider-conformance `204-217`, stress-durability `:219`, migration `:221`, the L38 row
  `:126`, `test_state_signal_boundary_delivery.py` `:98`, `test_worktree_status_terminal_next_tool.py`
  `:181`, the pause suite `:161`, the pause architecture guard `:193`, the playthrough `:155`) and added
  the L4 and L5 registration rows. The Purpose paragraph above carries pre-L4 counts and is superseded by
  the measured ones; classification only, lane membership is not execution or acceptance evidence, and
  the verification stamps remain closeout-owned.
- 2026-09-13T21:52:00+00:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`, base
  `5bb124d4`): **flagged an open gap rather than repairing it, because the file itself is unchanged and
  the repair is code work.** The change set added `mcp/tests/test_memory_attribution_producers.py` and
  declared no lane row for it, so the manifest's closed population no longer holds: measured by diffing
  the disk file list against the manifest, 203 `test_*.py` modules exist and 202 are declared, the one
  undeclared path being the new module, with no stale row pointing at a missing file. Because
  `load_lane_manifest` refuses a manifest that omits a module, this is the same hard load failure the
  card already records from 260831-LOCR-L30, and `code_quality/check.py:677` is a consumer. Recorded in
  a new section with the measurement method, the derivation path (`testpaths` in the repository-root
  `pyproject.toml:155`), the consumer that fails, and the explicit statement that the lane choice is the
  builder's and is not asserted here. The manifest file itself is **not** modified by this curator pass.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T18:42:00+00:00 — Child-admission seal removal (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): registered the change set's new
  `mcp/tests/test_lifecycle_playthrough_end_to_end.py` in the **integration** lane (entry row 153) —
  it plays the whole leaf-and-master lifecycle in order over one real temporary Git world through the
  public master-level operations, so that is its behaviour-preserving lane — and reconciled the
  population and every lane bracket against the current manifest, measured rather than carried from the
  previous entry: 202 modules on disk and 202 manifest entries, 114 unit-regression (entry rows 6-119),
  2 public-contract (122-123), 57 integration (126-182), 16 architecture-fitness (185-200), 13
  provider-conformance (203-215), with stress-durability and migration empty. The insertion shifted the
  three later rows this card cites (`test_worktree_status_terminal_next_tool.py` 178 → 179, the pause
  boundary suite 158 → 159, the pause architecture guard 190 → 191) and every lane bracket after
  integration. Also corrected two stale invariant bullets that still declared
  `integration_case_budget` as 200 at `pyproject.toml:134-135`; the measured source reads 250 at
  `pyproject.toml:150`, which the L37 entry had already recorded for the reference row. Classification
  only: lane membership is not execution or acceptance evidence, and the verification stamps remain
  closeout-owned.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "integration_case_budget" repointed to pyproject.toml:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "mcp/tests/test_worktree_status_terminal_next_tool.py" repointed to mcp/tests/test-evidence-lanes.toml:218-218. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:(258, 258)-(258, 258). No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "stress-durability"; "migration" repointed to mcp/tests/test-evidence-lanes.toml:(260, 261)-(260, 261); mcp/tests/test-evidence-lanes.toml:(260, 261)-(260, 261). No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 citation review (curator-authored, not a mechanical
  projection): re-read the `integration_case_budget` claim against the current `pyproject.toml` and
  re-cited it to the key's own line, `pyproject.toml:150-150`, where the declared integration ceiling of
  250 now lives. The wording ("the integration lane's collected-case cap that constrains lane choice")
  holds: the cap is the reason the L37 additions and the L30/L34 restorations were classified as they
  were. The previous range arrived from a generated projection and is superseded by this curator
  confirmation.
- 2026-09-13T17:02:00+00:00 — 260831-LOCR-L37 curator: registered the leaf's two new modules —
  `mcp/tests/test_pause_stop_only_end_to_end.py` in the **integration** lane (entry row 158) because
  it drives the public pause over a real temporary Git world holding two atomic masters, and
  `mcp/tests/test_pause_is_not_publication.py` in **architecture-fitness** (entry row 190) because it
  is an AST-only import-closure guard that executes nothing. Reconciled the population and every lane
  bracket against the current manifest, measured rather than carried from the previous entry: 201
  modules on disk and 201 manifest entries, 114 unit-regression (entry rows 6-119), 2 public-contract
  (122-123), 56 integration (126-181), 16 architecture-fitness (184-199), 13 provider-conformance
  (202-214), with stress-durability and migration empty. Also corrected the stale cap sentence: the
  integration lane is capped at 250 collected cases (`pyproject.toml:150`), not 200. Classification
  only: lane membership is not execution or acceptance evidence, and the verification stamps remain
  closeout-owned.
- 2026-09-13T17:02:00+00:00 — 260831-LOCR-L37 citation review (curator-authored, not a mechanical
- 2026-09-13T12:20:09+00:00 — 260831-LOCR-L36 curator: registered the leaf's new `mcp/tests/test_cross_master_concurrency.py` in the **integration** lane (row 143) — it drives two sprint-commanded atomic masters and the public land/resume operations over one real temporary Git world, so that is its behaviour-preserving lane — and reconciled the population and every lane bracket against the current manifest: 199 modules, 114 unit-regression (5-120), 2 public-contract (121-124), 55 integration (125-181), 15 architecture-fitness (182-198), 13 provider-conformance (199-213), with stress-durability (214-215) and migration (216-217) empty. The insertion shifted the L32 row (176 → 177) and every bracket after the integration block, all re-cited here. Classification only: lane membership is not execution or acceptance evidence, and the verification stamps remain closeout-owned.
- 2026-09-13T09:43:00+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:12:00+00:00 — 260831-LOCR-L34 curator: registered the leaf's new
  `mcp/tests/test_checkpoint_landing_end_to_end.py` in the **integration** lane (row 132) — it drives
  the public checkpoint and closeout operations over real temporary Git repositories under
  `tmp_path`, so that is its behaviour-preserving lane — and re-derived the population and every lane
  bracket against the current manifest: 198 modules, 114 unit-regression (5-120), 2 public-contract
  (121-124), 54 integration (125-180), 15 architecture-fitness (181-197), 13 provider-conformance
  (198-212), with stress-durability (213-214) and migration (215-215) empty. The insertion shifted the
  L32 row (175 → 176) and every later lane bracket, all re-cited here; also replaced the last stale
  "150 collected cases" bound in the L30 paragraph with the measured 200. Classification only: lane
  membership is not execution, certification or acceptance evidence, and verification metadata remains
  closeout-owned.
- 2026-09-12T20:55:00+00:00 — 260831-LOCR-L32 curator: registered the leaf's new
  `mcp/tests/test_worktree_status_terminal_next_tool.py` in the **integration** lane (row 175) — it
  drives real worktree services and a real repository under `tmp_path`, so that is its
  behaviour-preserving lane — and re-derived the population and every lane bracket against the
  current manifest: 197 modules, 114 unit-regression (5-120), 2 public-contract (121-124), 53
  integration (125-179), 15 architecture-fitness (180-196), 13 provider-conformance (197-211), with
  stress-durability (212-213) and migration (214-215) empty. Also corrected a stale bound rather than
  propagating it: `pyproject.toml:135` declares `integration_case_budget = 200`, not the 150 recorded
  in this card's earlier entries, so the two invariants and the purpose paragraph now cite the
  measured value. Classification only: lane membership is not execution, certification or acceptance
  evidence, and verification metadata remains closeout-owned.
- 2026-09-12T00:50:00+00:00 — 260831-LOCR-L30 checkpoint landing: registered eight members
  (`test_checkpoint_landing.py`, `test_closeout_kept_rules_pins.py`,
  `test_memory_scope_task_derivation.py`, `test_post_integration_cleanup_guidance.py`,
  `test_record_landing.py`, `test_retired_door_publication_fields.py`,
  `test_automatic_post_integration_cleanup.py`, and
  `test_memory_quality_is_independent_of_the_closeout_plane.py`) and repaired a manifest that could
  not load: seven tracked modules — one of them shipped by the preceding leaf — declared no lane, and
  `load_lane_manifest` refuses an incomplete population. Re-derived the population to 196 (114
  unit-regression, 2 public-contract, 52 integration, 15 architecture-fitness, 13 provider-
  conformance) and every lane bracket citation. Classification only: lane membership is not
  execution, certification or acceptance evidence, and verification metadata remains closeout-owned.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `integration` repointed to mcp/tests/test-evidence-lanes.toml:(157, 221)-(157, 221). No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `integration` repointed to mcp/tests/test-evidence-lanes.toml:119-119. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "unit-regression" repointed to mcp/tests/test-evidence-lanes.toml:(5, 151)-(5, 151). No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T15:06+02:00 — Parked-candidate lane registration: recorded the new `mcp/tests/test_sync_parked_candidate.py` row in the existing `unit-regression` lane and re-derived every lane-block citation shifted by it; reconciled the current population to 183 files (99 unit-regression, 55 integration). No case budget was raised. Verification metadata remains closeout-owned.
- 2026-09-10T13:06:00+00:00 — Parked-candidate lane registration: recorded the new `mcp/tests/test_sync_parked_candidate.py` row in the existing `unit-regression` lane and re-derived every lane-block citation shifted by it; reconciled the current population to 183 files (99 unit-regression, 55 integration). No case budget was raised. Verification metadata remains closeout-owned.
- 2026-09-10T12:23+02:00 — 260831-LOCR-L20 curator post-sync refresh: the leaf was synced forward to
  code `bb38d04e`, and the manifest union now holds 187 rows: 103 unit-regression, 2 public-contract,
  55 integration, 14 architecture-fitness and 13 provider-conformance (L28's landed
  `test_terminal_liveness_deferred_work.py` is the extra unit-regression row, inserted at line 104).
  This card's population prose and all six lane bracket citations were re-derived against the new tree,
  and the two synced conflicts were resolved hunk-by-hunk with the synced side authoritative for ranges
  and structure. One synced claim was **corrected rather than preserved**: that row described the
  integration population as "including the R28 deferred-work proof", but
  `test_terminal_liveness_deferred_work.py` registers in `unit-regression` at line 104, so the clause
  was dropped as contradicted by the current tree. Lane classification only; focused execution and any
  later acceptance remain separately owned.
- 2026-09-10T10:23:00+00:00 — 260831-LOCR-L20 curator post-sync refresh: the leaf was synced forward to
- 2026-09-10T09:55:00+00:00 — Post-sync union curation for 260831-LOCR-L03: the landed LOCR master tip `bb38d04e` carried the sibling R28 registration and its own re-derivation of the authorized three-row CCR landing-debt repair, while this branch carried the L03 `test_terminal_evidence_mapping.py` row. Both rows are kept, sorted, and this card's population statement and all six lane citations were re-derived against the union to 187 declared modules (103 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance). The sibling's two-range empty-population citation for stress-durability/migration and its R28 attribution were retained, with the R28 attribution moved to the unit-regression row it actually belongs to. Supersedes the 186-module figures recorded below. Classification only; no execution, certification or acceptance claim.
- 2026-09-10T09:53:00+00:00 — 260831-LOCR-L09 curator: resolved this card's sync merge and re-derived the whole lane account against the merged manifest — 187 modules, 103 unit-regression / 2 public-contract / 55 integration / 14 architecture-fitness / 13 provider-conformance, with stress-durability and migration empty. Corrected every lane bracket range to current line numbers, replaced the ambiguous `integration` anchor (three resolutions at the verified commit) with the unique `"integration = ["` literal, split the former combined L38 row into its two module paths, and recorded this leaf's boundary-delivery module plus the three pre-existing omitted-row repairs already carried by LOCR-L28. Verification metadata is the merged base `bb38d04e`; the real commit stamp remains closeout-owned.
- 2026-09-10T09:52:46+00:00 — 260831-LOCR-L25 curator: resolved the merge with landed LOCR-L28 (`e26b55db`) and re-derived every lane bracket and the population against the synced manifest: 187 modules — 103 unit-regression (`5-109`), 2 public-contract (`110-113`), 55 integration (`114-170`), 14 architecture-fitness (`171-186`), 13 provider-conformance (`187-201`), with stress-durability (`202-203`) and migration (`204-205`) empty; every row unique and present on disk. Supersedes the 186 / 102 figures recorded above by both leaves. Classification only: lane membership is not execution or acceptance evidence, and verification metadata remains closeout-owned.
- 2026-09-10T09:25:00+00:00 — Authorized repair of a pre-existing manifest omission: `8885939e` created `test_review_state.py`, `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py` in the same change that edited this manifest, but their required rows were omitted, so `load_lane_manifest` could not resolve them. The three rows were restored as `unit-regression` - their behaviour-preserving lane, since a full run had already collected them unmarked - and this card's population statement and all six lane citations were re-derived to 186 declared modules (102 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance). Registering them as `integration` was rejected because that lane sits at its 150-case cap and collection fails. Classification only; no execution, certification or acceptance claim.
- 2026-09-10T09:24:00+00:00 — 260831-LOCR-L28 curator: re-derived the manifest population and every lane range against the current tree after the authorized repair of three missing CCR landing-debt registrations, all three created by code commit 8885939e but omitted from this manifest. All three take the `unit-regression` lane because the integration lane is capped at 150 collected cases and registering them as integration raised a full-suite collection above that cap; in unit-regression the collection succeeds and the previously unmarked modules keep their existing behaviour. This leaf's own `test_terminal_liveness_deferred_work.py` row was corrected the same way, from integration to `unit-regression`: the module is hermetic and registering it as integration took that lane to 155 against the same 150 cap. Current population is 186 modules: 102 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance; stress-durability and migration empty. Supersedes the 183-module account in this leaf's first entry. Classification metadata only; focused results and certification remain closeout-owned.
- 2026-09-10T09:22:48+00:00 — 260831-LOCR-L25 curator: corrected the lane split for the three restored CCR landing-debt rows. The first registration put `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py` in `integration`, which pushed full-suite collection to 157 against the 150-case integration cap and raised `UsageError` at collection finish; because both modules previously ran unmarked (unit), the behaviour-preserving lane is `unit-regression`. All three restored rows (`test_review_state.py`, `test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`) are now `unit-regression`. Re-derived population: 102 unit-regression / 2 public-contract / **55** integration / 14 architecture-fitness / 13 provider-conformance = 186 files, superseding the 100 / 2 / 57 figures recorded at 11:04 on the same tree. Integration collects 150 (cap 150), unit collects 712 (cap 1000). The bracket ranges were re-measured (`integration` is again 113-169, `unit-regression` 5-108) and the cap consequence is recorded as a current invariant. Classification only: no execution or acceptance claim, and verification metadata remains closeout-owned.
- 2026-09-10T09:04:12+00:00 — 260831-LOCR-L25 curator: re-derived this card against the developer-authorized manifest repair that restored the three CCR landing-debt rows `8885939e` omitted (recorded here as `test_review_state.py` unit-regression; `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py` integration; the three modules already had cards). All five lane bracket ranges and the L38 row were re-measured and the population was recorded as 100 unit-regression / 2 public-contract / 57 integration / 14 architecture-fitness / 13 provider-conformance = 186 files, replacing 99 / 2 / 55 / 14 / 13 = 183. **The 57-integration split in this entry was superseded by the 11:22 correction above; the total of 186 and the restored-row set remain correct.** Classification only: lane membership is not execution or acceptance evidence, and verification metadata remains closeout-owned.
- 2026-09-10T08:55:00+00:00 — 260831-LOCR-L20 curator manifest refresh: the developer authorized
  repairing the pre-existing registration omission, and three modules created by the CCR
  transaction-only closeout reform were restored to the closed population —
  `test_review_state.py`, `test_task_doc_review_public.py` and
  `test_transaction_only_worktree_delivery.py`, all in `unit-regression`. They had been running
  unmarked (counted as unit), and the integration lane already sat at its hard cap of 150 collected
  cases, so `integration` would have overflowed the cap; the unit lane is the behaviour-preserving
  classification. The manifest then held 186 rows: 102 unit-regression, 2 public-contract,
  55 integration, 14 architecture-fitness and 13 provider-conformance. `load_lane_manifest` refused
  the incomplete manifest before the repair and loads it now. This card's population prose and all
  six lane bracket citations were re-derived against the file as it stood; the preceding L20 entry's
  183 rows was the count before that restoration. This records lane classification only; focused
  execution and any later acceptance remain separately owned.
- 2026-09-10T08:06:31+00:00 — 260831-LOCR-L25 curator: registered the new separation-guard module `mcp/tests/test_parked_external_await_separation.py` in the `unit-regression` lane and re-derived every lane bracket and membership range against the current manifest on the leaf candidate base `6096941f41204c9a7d6ccb2b29f6b2e862ed56b4`. The recorded population (96 unit / 54 integration / 179 files) had already drifted from the manifest, which held 98 / 55 / 182 before this leaf's row; it is now recorded as 99 / 55 / 183. Classification only: lane membership is not execution or acceptance evidence, and verification metadata remains closeout-owned.
- 2026-09-10T08:06:31+00:00 — 260831-LOCR-L25 curator: registered the new separation-guard module `mcp/tests/test_parked_external_await_separation.py` in the `unit-regression` lane and re-derived every lane bracket and membership range against the current manifest on the leaf candidate base `6096941f41204c9a7d6ccb2b29f6b2e862ed56b4`. The recorded population (96 unit / 54 integration / 179 files) had already drifted from the manifest, which held 98 / 55 / 182 before this leaf's row; it is now recorded as 99 / 55 / 183. Classification only: lane membership is not execution or acceptance evidence, and verification metadata remains closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "stress-durability" repointed to mcp/tests/test-evidence-lanes.toml:(258, 258)-(258, 258). No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T14:05:21+00:00 — CCR-L38 source-grounded candidate pass: recorded the two registered public integration modules and reconciled the manifest population to 179 files (54 integration). Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.
- 2026-09-08T12:39:00+00:00 — 260831-LOCR-L20 curator reconciliation: registered the new
  `test_terminal_evidence_cursors.py` unit-regression member and reconciled the manifest
  population to its then-current 183 rows (99 unit-regression, 55 integration), adding the focused
  deque-envelope, unsupported-harness, bounded-Pi, and liveness-containment checks to this route's
  account, and re-anchored every lane citation in this card to the tree as it stood. This records lane
  classification only; focused execution and any later acceptance remain separately owned.
- 2026-09-08T12:35:00+00:00 — 260831-LOCR-L28 curator: registered the new `test_terminal_liveness_deferred_work.py` integration proof and re-derived the manifest population and every lane range against the current tree (183 modules: 98 unit-regression, 2 public-contract, 56 integration, 14 architecture-fitness, 13 provider-conformance; stress-durability and migration empty). The lane remains classification metadata; focused results and certification remain closeout-owned.
- 2026-09-08T12:30:38+00:00 — Added the canonical terminal-evidence mapping regression to the `unit-regression` inventory and reconciled the retained population to 183 modules (99 unit-regression, 55 integration) on the current base, re-deriving this card's lane citations after the new row shifted them. Lane membership controls selection/classification only; this candidate entry does not claim execution, certification or acceptance.
- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.
- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Recorded the real transaction suite integration membership and shifted only exact affected lane citations; classification remains distinct from acceptance. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.
- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.
- 2026-09-05T22:17:00+00:00 — Added current retained-evidence, producer-publication and registry-lock lane assignments with explicit distinctions between classification and execution fidelity.
- 2026-09-05T06:14:14+00:00 — Reconciled all accumulated CCR lane additions and clarified that lane membership does not itself prove real production integration.
- 2026-09-04T20:45:00+00:00 - 260831-CCR-L14 Gate-5 memory pass: recorded the five CCR-R14 final-codex contract suites (rows 64-68, `unit-regression`) and the executor plus diff-coverage closure suites (rows 291-292, `integration`) and re-anchored the manifest citations shifted by the new rows (fence 102, gate-certificate 77, doctrine 526-528, retry 157/427/529, kernel 150, future-code 303, pair 385, ARSPAWN 301/396/426/515, CCR-R01 nine suites 29-30/73/158-161/180-181). Verification stamp is the full leaf code commit `54ff803a05209e06f732f2de1f90e2a71a069e08`.
- 2026-09-04T20:23:00+00:00 - 260831-CCR-L17 Gate-5 memory pass: recorded the six CCR-R17 measured-replay suites (rows 148-153, `unit-regression`) and re-anchored the manifest citations shifted by the new rows plus prior registrations (doctrine 525-527, retry 158/426/528, kernel 145, future-code 302, pair 384, ARSPAWN 300/395/425/514, fence 97, CCR-R01 nine suites 29-30/68/159-162/181-182, gate-certificate 72). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185`.
- 2026-09-04T18:19:44+00:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the three status-wait test modules added to the integration evidence lane.
- 2026-09-04T15:50:00+00:00 — 260831-CCR-L13 Gate-5 memory pass: recorded the four CCR-R13 diagnostic contract suites (rows 60-63, unit-regression) and the executor plus diff-coverage closure suites (rows 284-285, integration) and re-anchored the manifest citations shifted by the new rows (fence 97, doctrine 518-520, retry 152/420/521, kernel 145, future-code 296, pair 378, ARSPAWN 294/389/419/507, CCR-R01 29-30/68/153-156/175-176, gate-certificate 72). Verification stamp is the full leaf code commit `4ba18bb23ba90e201bb37341d61c0efc64161fcf`.
- 2026-09-04T15:15:00+00:00 - 260831-CCR-L20 Gate-5 memory pass (code commit `ce7f10b5`):
  registered the standalone CCR-R20 terminal rail-failure suite as explicit `integration`
  evidence (row 465) and re-anchored every manifest lane citation in this card to the committed
  tree positions (doctrine 513-515, retry 148/414/516, kernel 141, future-code 290, pair 372,
  ARSPAWN 288/383/413/502, fence 93, CCR-R01 nine suites 29-30/64/149-152/171-172) after
  intermediate registrations and the new row shifted the manifest. Verification stamp is the full
  leaf code commit `ce7f10b565f82bc41421d60ba914ee1d0abf61c4`.
- 2026-09-04T10:30:00+00:00 - 260831-CCR-L16 Gate-5 memory pass: recorded the six new
  durable gate-and-rail telemetry suites (unit-regression lanes file rows 178-183) and re-anchored
  every manifest citation shifted by their rows (doctrine 512-514, retry 148/414/515, kernel 141,
  future-code 290, pair 372, ARSPAWN 288/383/413/501, fence 93, CCR-R01 nine suites
  29-30/64/149-152/171-172). Verification stamp advanced to the certified commit
  `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`.
- 2026-09-04T08:05:00+00:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the `test_generation_coherent_lifecycle_projection.py` unit-regression lane registration and the manifest line shift it causes. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.
- 2026-09-04T08:05:00+00:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the explicit `integration` lane registration for the new host-authority suite `test_dagger_runtime_authority.py`.
- 2026-09-03T23:48:00+00:00 — 260831-CCR-L08 Gate-5 memory pass: recorded the CCR-R08
  integration-lane registration of the five final full memory-coherence certification suites
  (rows 365-369) so each forcing suite enters the closed population exactly once. Verification
  metadata pinned to the owning commit 16d1a4d6.
- 2026-09-03T23:15:00+00:00 - 260831-CCR-L10 Gate-5 memory pass: recorded the CCR-R10 lane registration of
  `mcp/tests/test_citation_deterministic_projection.py` as explicit `integration` evidence (toml row 223)
  and re-anchored every manifest citation shifted by that row (retry 147/401/501, ARSPAWN
  280/370/400/487, future-code 282, pair 364, doctrine 498-500). Verification pinned to the
  leaf code commit 709dd076.
- 2026-09-03T23:06:00+00:00 — 260831-CCR-L23 Gate-5 memory pass: recorded the `test_serving_requirements.py` integration-lane registration and re-anchored the manifest citations shifted by the new row (doctrine 498-500, ARSPAWN e2e 487, retry-coverage 501).
- 2026-09-03T11:30:00+00:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored all
  21 manifest lane citations to the exact current line numbers after the L21 gate-certificate
  registration and prior registrations shifted rows (doctrine 497-499, retry 147/400/500,
  kernel 140, future-code 281, pair 363, ARSPAWN 279/369/399/486, fence 92, CCR-R01 nine
  suites 29-30/64/148-151/170-171). Verification remains pinned to the pre-commit source
  history until closeout.
- 2026-09-03T11:30:00+00:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored all 21 manifest lane citations to the exact current line numbers after the L21 gate-certificate registration and prior registrations shifted rows (doctrine 497-499, retry 147/400/500, kernel 140, future-code 281, pair 363, ARSPAWN 279/369/399/486, fence 92, CCR-R01 nine suites 29-30/64/148-151/170-171). Verification remains pinned to the pre-commit source history until closeout.
- 2026-09-03T10:30:00+00:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 lane registration of
  `mcp/tests/test_gate_certificate_authority.py` as explicit `unit-regression` evidence so the
  new forcing suite enters the closed population exactly once. Verification is pinned to the
  owning commit.
- 2026-09-03T10:30:00+00:00 - 260831-CCR memory curation pass for 6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 lane registration of `mcp/tests/test_gate_certificate_authority.py` as explicit `unit-regression` evidence so the new forcing suite enters the closed population exactly once. Verification is pinned to the owning commit.
- 2026-09-01T09:33:00+00:00 — CCR-L11 Attempt 10 added explicit `unit-regression` ownership for the
  three focused certification edge suites and re-anchored every manifest citation shifted by
  those rows. Verification remains closeout-owned.
- 2026-09-01T09:33:00+00:00 - CCR-L11 Attempt 10 added explicit `unit-regression` ownership for the three focused certification edge suites and re-anchored every manifest citation shifted by those rows. Verification remains closeout-owned.
- 2026-09-01T06:13:00+00:00 — Final CCR-R01 reconciliation: expanded the current lane account from
  six to all nine focused unit-regression suites, including the three coverage-edge companions, and
  regenerated every manifest citation shifted by their rows. The manifest supplies selection and
  cost classification only; verification remains closeout-owned.
- 2026-09-01T06:13:00+00:00 - Final CCR-R01 reconciliation: expanded the current lane account from six to all nine focused unit-regression suites, including the three coverage-edge companions, and regenerated every manifest citation shifted by their rows. The manifest supplies selection and cost classification only; verification remains closeout-owned.
- 2026-09-01T03:22:00+00:00 — 260831-CCR-L01 Attempt 9: added explicit `unit-regression`
  ownership for the six focused CCR-R01 suites and re-anchored every manifest citation shifted by
  those rows. The lane declaration governs selection/cost only; accepted task evidence remains
  reviewer-owned. Verification remains closeout-owned.
- 2026-09-01T03:22:00+00:00 - 260831-CCR-L01 Attempt 9: added explicit `unit-regression` ownership for the six focused CCR-R01 suites and re-anchored every manifest citation shifted by those rows. The lane declaration governs selection/cost only; accepted task evidence remains reviewer-owned. Verification remains closeout-owned.
- 2026-09-01T02:34:00+00:00 — Added explicit `unit-regression` ownership for the two certification
  contract suites and repaired every manifest citation shifted by those rows. The manifest remains
  fail-closed; no default, fallback, or alternate classification authority was introduced.
- 2026-09-01T02:34:00+00:00 - Added explicit `unit-regression` ownership for the two certification contract suites and repaired every manifest citation shifted by those rows. The manifest remains fail-closed; no default, fallback, or alternate classification authority was introduced.
- 2026-08-31T18:30:00+00:00 — 260831-DER: explicitly classified
  `mcp/tests/test_integration_publication_fence.py` in the `unit-regression` lane.
- 2026-08-31T18:30:00+00:00 - 260831-DER: explicitly classified `mcp/tests/test_integration_publication_fence.py` in the `unit-regression` lane.
- 2026-08-31T06:05:00+00:00 — Classified the four A003-unregistered ARSPAWN proof modules exactly
  once: three integration routes and one architecture-fitness selector-closure route.
- 2026-08-31T06:05:00+00:00 - Classified the four A003-unregistered ARSPAWN proof modules exactly once: three integration routes and one architecture-fitness selector-closure route.
- 2026-08-30T13:15:36+00:00 — Classified `test_public_surface_conformance.py` explicitly as
  integration evidence. Verification remains closeout-owned.
- 2026-08-30T13:15:36+00:00 - Classified `test_public_surface_conformance.py` explicitly as integration evidence. Verification remains closeout-owned.
- 2026-08-30T02:54:00+00:00 — Added explicit integration-lane ownership for the exact
  code-memory candidate-pair suite after the lifecycle Dagger census rejected an unclassified
  test file. No product or requirement semantics changed.
- 2026-08-30T02:54:00+00:00 - Added explicit integration-lane ownership for the exact code-memory candidate-pair suite after the lifecycle Dagger census rejected an unclassified test file. No product or requirement semantics changed.
- 2026-08-29T06:52:00+00:00 — Added explicit integration classification for the structured
  curator-coherence forcing suite. Verification remains closeout-owned.
- 2026-08-29T06:52:00+00:00 - Added explicit integration classification for the structured curator-coherence forcing suite. Verification remains closeout-owned.
- 2026-08-29T05:35:00+00:00 — Added explicit integration-lane ownership for the future-code
  candidate real-Git matrix and repaired exact manifest citations shifted by that row.
- 2026-08-29T05:35:00+00:00 - Added explicit integration-lane ownership for the future-code candidate real-Git matrix and repaired exact manifest citations shifted by that row.
- 2026-08-28T12:18:00+00:00 — Reconciled manifest citations against the committed PDLS candidate;
  the explicit-lane contract is unchanged.
- 2026-08-28T12:18:00+00:00 - Reconciled manifest citations against the committed PDLS candidate; the explicit-lane contract is unchanged.
- 2026-08-28T03:10:00+00:00 — Removed the two stale Candidate A test rows and retained the renamed
  kernel regression module in its explicit unit lane after Q5 v19 forced the stale-row refusal.
- 2026-08-28T03:10:00+00:00 - Removed the two stale Candidate A test rows and retained the renamed kernel regression module in its explicit unit lane after Q5 v19 forced the stale-row refusal.
- 2026-08-27T16:33:00+00:00 — Recorded explicit unit-regression membership for the retry coverage
  composition and quality child-environment suites.
- 2026-08-27T16:33:00+00:00 - Recorded explicit unit-regression membership for the retry coverage composition and quality child-environment suites.
- 2026-08-27T16:06:00+00:00 — Added explicit architecture-fitness membership for the M40-M45
  Requirement Attempt Journal structural proof.
- 2026-08-27T16:06:00+00:00 - Added explicit architecture-fitness membership for the M40-M45 Requirement Attempt Journal structural proof.
- 2026-08-27T15:19:00+00:00 — Added explicit unit-regression membership for the retry-selection
  forcing suite in the same change that introduced it.
- 2026-08-27T15:19:00+00:00 - Added explicit unit-regression membership for the retry-selection forcing suite in the same change that introduced it.
- 2026-08-27T11:32:00+00:00 — Added explicit architecture-fitness membership for M39 compilation
  doctrine and the split tool-signature exemption suite. Verification remains closeout-owned.
- 2026-08-27T11:32:00+00:00 - Added explicit architecture-fitness membership for M39 compilation doctrine and the split tool-signature exemption suite. Verification remains closeout-owned.
- 2026-08-27T10:43:00+00:00 — M38: created the manifest sidecar and recorded explicit registration
  of the acceptance-envelope structural test. Verification metadata remains empty until governed
  closeout stamps the PDLS code commit.
- 2026-08-27T10:43:00+00:00 - M38: created the manifest sidecar and recorded explicit registration of the acceptance-envelope structural test. Verification metadata remains empty until governed closeout stamps the PDLS code commit.
metadata-only refresh.
set them. The body was changed substantively and this entry is the history record, not a
`lastVerifiedCommitHash` / `lastVerifiedCommitDate` are left exactly as the last real verification
metadata block above names this leaf's uncommitted candidate in `reviewedWorkingCandidate`, and
and the engine's own generated entries in this card's history are left exactly where they are. The
row was touched by this pass: ranges into this file are the citation-reprojection engine's to move,
need reprojection. The L21 section is retained unchanged as that leaf's as-of account. No reference
by one, which is why the L21 section's positions read one lower and why citations into this manifest
former lanes empty at keys `:307` and `:309`** — and states that the insertion moves every later row
modules, 0/0 undeclared or absent, 185 / 2 / 74 / 17 / 14 across the five occupied lanes, both
the measurement taken from the manifest and the modules on disk — **292 declared entries against 292
module's behaviour-preserving classification because it is hermetic. The new section above carries
at `:102` and `test_knowledge_requirement_reference_contract.py` at `:104`; the lane is the
`mcp/tests/test-evidence-lanes.toml:103`, inserted mid-list between `test_knowledge_read_scope.py`
numbers.** `mcp/tests/test_knowledge_review_surface.py` joins `unit-regression` at
---
