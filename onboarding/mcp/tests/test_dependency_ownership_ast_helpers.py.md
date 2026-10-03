# mcp/tests/test_dependency_ownership_ast_helpers.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Repository-input ownership discovery without broadening test selection; and the `LOCR-R26@v1` catalog
guard — the retained headless production-chain proof is ordinary `test_` source, adds no governed
evidence artifact, and leaves the catalog closed over the governed inventory.

## Current verification scope

The current catalog pin tracks the added exact test_review_read_latency consumer. Contracts/artifacts stay sixteen/eighty. The source module documents the deliberate re-pin; this card treats historical digest entries as history rather than current source identity.

## Current preview-proof registration

The current catalog union pin is 6f50c9f4119e5cd480309c388c4bd1c9ecfafe9ea9a5cff6c1e32131b644c9e6 (2,099 lines), with 16 contracts/80 artifacts unchanged. Dated L40/R47 rationale and earlier history remain; the source-derived consumer proof checks the actual union rather than replacing historical digests.

## Code Commentary

### Logic

An explicitly supported input with no consumers remains complete with a verified no-consumer decision. Unknown input is incomplete. A declared consumer is selected without global invalidation and carries the declared-consumer reason.

| Re-pin | Leaf / when | Population | Digest | What moved |
| --- | --- | --- | --- | --- |
| first | R16 proof landing (`5b7a84f2`) | post-registration | `a9d83c37…` | the two `LOCR-L04` handoff support modules registered under the amended catalog-freeze clause; the proof's own artifact delta stayed empty |
| second | `260915-CAPS-L16` (2026-09-16) | 45 → **51** | `293a187f… → 812211e9…` | `260915-CAPS-L7`'s landing added the fifty-first governed artifact row; the pin had been stale since the source-line convergence merge carried the landed 260831-LOCR line's artifacts in without a re-pin (defect **D10**, the one pre-existing integration failure every master-tip candidate inherited) |
| third | `260915-CAPS-L15` (2026-09-17) | **51** (unchanged) | `812211e9… → 3342a249…` | **consumer rows only** — `mcp/tests/test_capsule_launch_wiring.py` became an importer of three governed artifacts through shared test support |
| fourth | `260915-CAPS-L14` (2026-09-17) | 51 → **54** | `3342a249…`-era → `5e938c85…` | **three NEW artifacts registered** for the fresh-user acceptance harness under `scripts/e2e_harness/`, each with its own source-derived consumers and an executable `node:` replacement; `mcp/tests/test_fresh_user_harness.py` answers for all three |
| fifth | `260915-CAPS-L17` (2026-09-17) | **51** (unchanged) | `812211e9…`-era → `563582a0…` | **consumer rows only** — `mcp/tests/test_eve_effort_runtime.py` starts the shipped runtime and therefore reaches three already-governed artifacts; this is L17's **own branch** value |
| sixth | `260915-CAPS-L17` (2026-09-17) — the merged value at landing | 51 → **54** | `563582a0… → e3651d6f…` | L14 landed first, so this value is re-derived against the merged catalog: L14's fifty-fourth artifact row plus L17's three consumer entries |
| seventh | `260915-CAPS-L9` (2026-09-17) — this leaf's own branch value | **51** (unchanged) | `8764ea1f…` | **consumer rows only, two of them**, for the one governed artifact this leaf's installer surface reaches (`mcp/tests/fixtures/repository_profiles/node/package-lock.json`): the leaf's new `test_capsule_experiment_install.py` reads the pinned application's committed lockfile through the installer it drives, and the pre-existing `test_install_runtime.py` inherits the same reach through the module it imports |
| eighth | `260915-CAPS-L9` (2026-09-17) — the first merged value | 51 → **54** | `8764ea1f… → dca9c2f9…` | L14 landed while this leaf was in flight, so the value was re-derived after `worktree_sync` against the merged catalog |
| ninth | **`260915-CAPS-L9` (2026-09-17) — the merged value at this leaf's landing (this tip)** | **54** (unchanged) | `dca9c2f9… → 31c6983d…` | L17 landed as well, so the value is re-derived a second time against the merged catalog: L14's three registered rows, L17's three consumer entries and this leaf's own two consumer entries, over 4 contracts / 54 artifacts. The measured delta against L17's landed catalog is **exactly this leaf's two added consumer paths and nothing else**, which is why the value could be taken from neither leaf's own figure |
| tenth | **`260915-KS-L21` (2026-09-18) — the value the constants carried at that tip** | 14 / 64 → **15 / 65** | `1aef5f9b… → 633b03ee16893ce3d0e838659d52f2bc609903f5c75b142eb41ca8c4fdabf5e6` | the census leaf's one appended `[[contract]]` (`migration-census-cases`) and its one appended `[[artifact]]` for `mcp/tests/migration_census_test_support.py`; both counts move for the first time since L11, and the pin is the file's own re-hashed bytes |
| eleventh | **`260915-KS-L31` (2026-09-19) — the value the constants carry at this candidate** | **15 / 65** (unchanged) | `25b00f88…` (the L23 tip, recorded in its own paragraph above) → **`c499cbcc266088f35bd6fdde655f00579431591f02bba5c4859b72f767f65f06`** | **consumer rows only, two of them** — both appended to the tail of `mcp/tests/merge_case_test_support.py`'s exact list: `mcp/tests/test_worktree_sync.py`, which consumes the harness directly for the CYCLE-02 knowledge-dataset conflict case, and `mcp/tests/test_sync_parked_candidate.py`, which reaches it transitively through its existing import of `test_worktree_sync` and was not itself edited |

| by this leaf | **`260921-ICR-L1` (2026-09-21) — the value the constants carry at this candidate** | **16 / 66** (unchanged) | `f0cb5fec…` → **`24e760a124d5f0d3a608295533720168b47e8a2ee28f6ee85c493e3778cdbed4`** | **consumer rows only, two of them, one on each existing shared-support artifact** — `mcp/tests/test_knowledge_review_source_endpoints.py` appended to the tail of `mcp/tests/diff_scope_test_support.py`'s and `mcp/tests/read_scope_test_support.py`'s `consumer_scope = "exact"` lists, because the leaf's source-endpoint cases compose those two fixtures rather than introducing a third. No contract and no artifact was added, so both counts stay where `260918-TSIP-L10`'s `T129` reconciliation left them. |
| by this leaf | **`260921-ICR-L14` (2026-09-21) — the value the constants carry at this candidate, and the value the sync re-measured onto L3's landing** | **16 / 66** (unchanged) | `aedb2636844faf41ca63b7099e6c62bcaf888720e7e7dd78e203e3a1c9e061ff` → **`4d1573760968b52a1cb8b087e235c21f40f0e2eccf2a5dcae3e19f0e5ae099a1`** (this leaf's own candidate) → **`3e9105c2116422debaa01c295294fc0c714288f701ee5902e6552884b64a52d8`** (the merged catalog: L3's landed rows and this leaf's four consumer rows in one file) | **consumer rows only, four of them**, all appended to existing `consumer_scope = "exact"` lists for the leaf's new `mcp/tests/test_knowledge_review_evidence_channels.py`: `curator_coherence_test_support` (the publication and topology helpers the assessment channel is produced through), `diff_scope_test_support` (the two real trees and candidate bytes the enclosure is built over), `read_scope_test_support` (the repository, anchors and datasets the comparison is between) and the Node `package-lock.json` fixture the census's propagation rule reaches through those support modules. The module's own lane row was added to `mcp/tests/test-evidence-lanes.toml` in the same change. No contract and no artifact was added, so both counts stay where the landed line left them. |
| by this leaf | **`260921-ICR-L9` (2026-09-22) — the Seventeenth deliberate re-pin, the value the constants carry at this candidate** | **16 / 66** (unchanged) | `3e9105c2116422debaa01c295294fc0c714288f701ee5902e6552884b64a52d8` → **`8d60a34cf56a9740e234823658312c8b6f5ae4e958344fe8ba2ea152b8ff6891`** | **consumer rows only, two of them**, each appended to one existing `consumer_scope = "exact"` list for the leaf's new `mcp/tests/test_review_subject_catalogue.py`: `mcp/tests/diff_scope_test_support.py` (the two snapshots and the two real Git trees the catalogue populations are copied from) and `mcp/tests/read_scope_test_support.py` (the authorship and the applicability/conditions/exclusions constants the authored rows are built with). The module's own lane row was added to `mcp/tests/test-evidence-lanes.toml` (337 → 338 lines at this candidate). **Nothing was registered, no row was removed and no artifact's identity moved**, so the population stays at **sixteen contracts / sixty-six artifacts**. No contract and no artifact was added, so both counts stay where the landed line left them. |
**260915-KS-L40 re-pinned it a twelfth time, by the code's own count and the eleventh by this table's** (the table below counts the re-pins this card has narrated; the module docstring counts the catalog's own). The reason is consumer rows only: `mcp/tests/test_worktree_sync.py` now consumes the registered `generation_test_support` fixture, whose `consumer_scope = "exact"` requires its consumer list to equal the source-derived set, so that module and `mcp/tests/test_sync_parked_candidate.py` were appended there. The populations did not move (15 / 65) and the digest is `c499cbcc…`; the full reason is the docstring's own eleventh entry.

**The module also carries the evidence catalog's pinned identity, and that pin is a deliberate one.** The three
constants `LIFECYCLE_CONTRACT_COUNT`, `LIFECYCLE_ARTIFACT_COUNT` and `LIFECYCLE_CATALOG_SHA256` state the
catalog's declared shape and its exact bytes, so a change to `mcp/tests/evidence-lifecycle.toml` that nobody meant
is a **hard failure** rather than a silent inventory drift. **The current constants are `LIFECYCLE_CONTRACT_COUNT = 16`, `LIFECYCLE_ARTIFACT_COUNT = 80` and `LIFECYCLE_CATALOG_SHA256 = 6f50c9f4119e5cd480309c388c4bd1c9ecfafe9ea9a5cff6c1e32131b644c9e6`. The catalog has 2,099 lines and preserves the exact L40/R47 consumer union and dated source rationale. Earlier re-pin descriptions below remain historical** — **updated by
`260928-MIK-L14`:** this sentence named L05's Forty-first value `f8b04814…` at 2095 lines. **Updated by
`260928-MIK-L05`:** this sentence named L10's Fortieth value `449b69ef…` at 2091 lines. **Updated by
`260928-MIK-L10`:** this sentence named L01's Thirty-ninth value `a571a70f…` at 2090 lines. **Updated by
`260928-MIK-L01`:** this sentence named L11's Thirty-eighth value `cb853f72…` at 2088 lines. **Updated by
`260928-MIK-L11`:** this sentence named L02's Thirty-seventh value `5c0a1594…` at 2087 lines. **Updated by
`260928-MIK-L02`:** this sentence named L03's Thirty-sixth value `dcc1ab1d…` at 2085 lines. **Updated by
`260928-MIK-L03`:** this sentence named L08's Thirty-fifth value `11ce8089…` at 2084 lines. **Updated by
`260928-MIK-L08`:** this sentence named L28's Thirty-fourth value `b96198c3…` at 2083 lines. **Updated by
`260928-MIK-L28`:** this sentence named L24's Thirty-third value `6fb4934d…` at 2080 lines. **Corrected by
`260928-MIK-L24` rather than carried:** this sentence had still named `16 / 66` and `d07c2f9d…` at 1710
lines, a value that the Thirty-second re-pin (`1c682524…`) had already superseded before this leaf. **An
earlier live pair was also corrected here rather than carried:** this sentence named
`3e9105c2116422debaa01c295294fc0c714288f701ee5902e6552884b64a52d8` at 1681 lines, which was the merged
value `260921-ICR-L14` left and had been superseded by later deliberate re-pins before this leaf's own
three; the sections at the end of this card record the Twenty-fourth, Twenty-fifth and Twenty-sixth — **re-pinned by `260921-ICR-L14`, whose
catalog change is consumer-only**: it appended four consumer rows — one on
`mcp/tests/curator_coherence_test_support.py`, one on `mcp/tests/diff_scope_test_support.py`, one on
`mcp/tests/read_scope_test_support.py` and one on the Node `package-lock.json` fixture — for its new
`mcp/tests/test_knowledge_review_evidence_channels.py`, and both counts stay **16 / 66** because it
added no contract and no artifact. **Two corrections are recorded here rather than carried:** this
paragraph named `24e760a1…` as the current value, which was `260921-ICR-L1`'s measurement and **not**
the value the constant carried at this leaf's base; the measured base value is
`aedb2636844faf41ca63b7099e6c62bcaf888720e7e7dd78e203e3a1c9e061ff` (`260921-ICR-L11`'s, read from the
constant itself in this leaf's candidate before its edit). The sentence that follows describes
`260921-ICR-L1`'s own consumer-only change, and its `24e760a1…` is a historical value on this line.
**The card also carries two `## Update History
- 2026-09-30T12:56:40+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db` plus the staged delta; first curated over `b54d1b03`, then merged with L29's landed curation after the sync onto code `ce459423` / memory `a6075c76`, L29's committed lines kept byte-identical): Added the section "260928-MIK-L14 The Forty-Second Deliberate Re-Pin" (`f8b04814…` → `4477446e…`, the final ordinal after the sync onto `48f680d5`, re-measured on the candidate at 2,097 lines) with three rows, and updated the "current value" paragraph, recording L05's value it replaced. L05's digest row is reworded, because the pin line `:46` now holds the Forty-third value, and its note row was re-pointed by the exact +11 shift (`49-61` → `60-72`). The rows the installed fixer declined, into the shifted docstring and the lane rows, were re-pointed by the exact line shift; the fixer projected or normalised the rest, and its generated bullets are kept. No verification stamp was advanced. **After the sync:** the rows L29's landed curation had also re-pointed were taken from L29's text and re-pointed by the exact line shift from `ce459423` to the staged tree (L14's lane row now at `:127`, its catalog line `:839`, the pin docstring), each anchor checked at both ends; the other rows keep this leaf's values.
- 2026-09-30T05:58:11+02:00 — 260928-MIK-L05 curator (uncommitted change set on `ar/260928-mik-l05`, code base `31d761a241055d67b85ef3908033856b78a86a57` plus the staged and unstaged delta): Added the section "260928-MIK-L05 The Forty-First Deliberate Re-Pin" (`449b69ef…` → `f8b04814…`, the final ordinal after the sync onto `31d761a2`, review R1 F5 and the ruling of 2026-09-30 04:12:49) with three rows, and updated the "current value" paragraph to `f8b04814…` at 2,095 lines. Other rows re-pointed by the exact line shift the new docstring paragraph caused (+14 lines) are recorded as citation-only.
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): Added the section "260928-MIK-L10 The Fortieth Deliberate Re-Pin" (`a571a70f…` → `449b69ef…`, 16 / 80), after L01's. **The "current value" paragraph was updated** to the Fortieth value at 2091 lines, recording L01's value it replaced. **Two reopened claims re-read and reworded:** the ICR-L20 and ICR-L6 paragraph rows, whose `LIFECYCLE_CATALOG_SHA256` anchor now reads L10's value; the pin line `:46` changed in this leaf, so both rows now cite only their own paragraph and point to the L10 section's row for the constant. Rows into the shifted docstring and the lane rows were re-pointed by the installed fixer or by exact line shift (the pin line `:46` is the one changed line). No verification stamp was advanced.
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): No content impact: this card's source is unchanged. Rows citing lines that MIK-R25 moved in `test-evidence-lanes.toml` were re-pointed, by the installed fixer (its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; each such row was byte-identical to memory HEAD. No verification stamp was advanced.
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; MIK-R13 inserted one `unit-regression` row at `test-evidence-lanes.toml:121`, so citation ranges into later lane rows were projected by the installed `memory-citations --fix` or, for multi-anchor rows it declined, re-pointed by the exact base-to-staged line shift (+1 at or after `:121`; each such row was byte-identical to memory HEAD).
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): Added the section "260928-MIK-L01 The Thirty-Ninth Deliberate Re-Pin" (`cb853f72…` → `a571a70f…`, 16 / 80), after L11's, recording the architect ruling of 2026-09-30 00:08:39 (the ordinal renumbered at the sync onto L11). **The "current value" paragraph was updated** to the Thirty-ninth value at 2,090 lines. The ICR-L20 and ICR-L6 paragraph rows and their two sibling rows were reworded for the Thirty-ninth note now being first; this pass's two generated-repair bullets for them were removed because their claims were reworded. The other rows were projected by the installed fixer, or re-pointed by the exact line shift of `evidence-lifecycle.toml` and `test-evidence-lanes.toml`.
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; L06 inserted one `unit-regression` row at `test-evidence-lanes.toml:69`, so its citations to later lane rows moved down one line. The multi-anchor lane rows the fixer declined were re-pointed by that exact +1 shift, and each was checked to hold its anchors in the shifted ranges; any other moved row was re-pointed by the installed fixer, which records its own bullet. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): Added the section "260928-MIK-L11 The Thirty-Eighth Deliberate Re-Pin" (`5c0a1594…` → `cb853f72…`, 16 / 80), after L02's, recording the architect ruling of 2026-09-29T22:35:34 (the provisional ordinal renumbered and the digest re-measured at the sync). **The "current value" paragraph was corrected:** it named L02's value at 2087 lines, and the catalog is now 2088 lines at the Thirty-eighth value. L02's Thirty-seventh-note row was re-pointed by the exact +11 line shift; the 11-line docstring insertion moved every other re-pin note row below it, and those ranges are re-pointed by the installed fixer or the exact line map. **Two reopened SHA claims** (the ICR-L20 and ICR-L6 paragraph rows) and their two sibling rows were re-read and reworded for the Thirty-eighth note (the paragraphs are unchanged and sit eleven lines lower); only the two generated-repair bullets this pass's fixer wrote for the two reopened rows were removed.
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): Added the section "260928-MIK-L02 The Thirty-Seventh Deliberate Re-Pin" (`dcc1ab1d…` → `5c0a1594…`, 16 / 80), after L03's. **The "current value" paragraph was corrected:** it named L03's value at 2085 lines, and the catalog is now 2087 lines at the Thirty-seventh value. The 13-line docstring insertion moved every re-pin note row below it; those ranges are re-pointed by the installed fixer or the exact line map. **Two reopened SHA claims** (the ICR-L20 and ICR-L6 paragraph rows) and their two sibling rows were re-read and reworded for the Thirty-seventh note; only the two generated-repair bullets this pass's fixer wrote for the two reopened rows were removed.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`application/published_intent.py`, `mcp/tools/knowledge.py`, `mcp/registration/knowledge.py`, `models/tools/knowledge_responses.py`, `cli/__main__.py`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the installed fixer or, for the multi-anchor rows it declined, by exact base-to-working line mapping; a per-document `memory-citations` check then reported 0 findings. No claim wording changed.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): No content impact: citation-only re-measure. This card cites `mcp/tests/test-evidence-lanes.toml`, where MIK-R22's two `unit-regression` rows (`:99-100`) moved every later row down two lines. Ranges were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact line shift, and a per-document check then reported 0 findings. The claims were re-read and are unchanged. No verification stamp was advanced.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): No content impact: multi-anchor rows re-measured against their cited files; each anchor now cites the one line that holds it. Claim meaning unchanged; no stamp advanced.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`mcp/tests/test-evidence-lanes.toml`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.

- 2026-09-27T05:43:38+00:00 — Curator-authored re-citation of 3 investigated L41 source-linked claim(s). Each named registration or declaration was selected individually after the composite guarded projection declined. Prior explanation, refusal evidence, generated history and real verification stamps are preserved.

- 2026-09-27T00:34:45Z — L39: No content impact: resolved the affected registry/instruction/overview reference rows against their exact current named anchors after the scoped source changes. Existing factual meaning, verification stamps and earlier history are preserved.

- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — the catalog pin was re-taken after the split (D54).** `LIFECYCLE_CATALOG_SHA256` is a fresh `sha256sum` of the delivered catalog and the population stays 16 contracts / 66 artifacts. **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
` headings** (one after the L11 re-pin section and one at
the end, holding a single `260915-KS-L40` entry): this leaf's entry was prepended to the first, which
holds the current newest-first list, and the duplicate is left as the merge residue it is rather than
restructured outside this leaf's change. The value it replaced on this line is `f0cb5fec…`, and **the counts read
16 / 66 because `260918-TSIP-L10`'s `T129` reconciliation moved them there** — this paragraph said
`15 / 65` and `c499cbcc…` until this pass, which was the pair `260915-KS-L40`'s candidate carried; both
are corrected here rather than carried, and the section below records the re-pin. The value
this paragraph carried before that was `6ec7eb0d33e91c148b25ed64c6b791664446082bdf419bf511635f4ca3cbdd75`
(the constant at the KS-L40 base, which the source's own docstring attributes to L28's
missing-consumer registration repair), and the values this paragraph carried for the leaves before
that are retained below and in their own sections:
`633b03ee…` (`260915-KS-L21`), `68a64207…` (`260915-KS-L22`) and `25b00f88…` (`260915-KS-L23`). **`260915-KS-L21` is the latest leaf to move all
three, and it moved them because it registered a row rather than a consumer:** the census leaf appends one
`[[contract]]` (`id = "migration-census-cases"`, owner `mcp/tests/migration_census_test_support.py`) and one
`[[artifact]]` (that same path, `kind = "shared-support"`, `authority = "internal-canonical"`,
`category = "unit-regression"`, `fidelity = "local-composition"`, `cadence = "affected"`,
`introduced_by = "260915-KS-L21"`, `lifetime = "permanent"`,
`replacement_contract = "contract:migration-census-cases"`, `consumer_scope = "exact"` with the one census
module as its consumer), so the constants now read **15 contracts, 65 artifacts, digest
`633b03ee16893ce3d0e838659d52f2bc609903f5c75b142eb41ca8c4fdabf5e6`**. `260915-KS-L11` moved all three in the same change as
its catalog edit: **13 contracts, 54 artifacts, digest
`19ed0525cd94b57389052a4e19cf1f0dfe83e9c166783ead2598f6a4e0ce8ffa`** (from `4 / 45 / 293a187f…`, through the
`KS-L1`–`KS-L11` registrations, from L7's `10 / 51 / 461121ca…`, from L8's `11 / 52 / 4cf81f10…`, and from
L10's `12 / 53 / 9b057632…`).
**`260915-KS-L14` then moved only the digest — `19ed0525…` →
`c6956899947b0435e5cdd8cd77ba3121db77e3dbf4676bee11406c3baf03ec68` — with both counts unchanged, and that
is the shape worth reading.** The detection leaf's catalog change is a **consumer change only**: its two test
modules use the already-registered `diff_scope_test_support` and `read_scope_test_support` fixtures, so no
artifact and no contract was added, while the two `consumers` rows it did add changed the file's bytes. The
counts therefore stay at **13 / 54** and the pin still had to move; the comment above the constant records
that reason, alongside the standing rule that **a future catalog change must re-pin deliberately, in the
same change**, and that the counts must move with the blocks they count.

**`260915-KS-L19` added no artifact and no contract of its own — its two new test
modules consume the already-registered `knowledge_fixture_test_support` and `generation_test_support`
fixtures — so its catalog change is again a **consumer change only**: both of those artifacts' `consumers`
lists gained the two module paths, which changed the file's bytes while leaving both block kinds where
they were. The counts therefore stayed at **13 / 54** at that tip and only the digest moved,
`c6956899…` → `03c384c790ef9a1e552800048f3f92fef96e1e69c7872aaed122f86b206c1968`. **The value to read
off this card is the current one and the one the source holds** — the constants as they stand now; the comment above the constant states
L19's reason beside L14's. The pin's own verification is the module's
`_assert_the_catalog_kept_its_bytes_and_identities`, which recomputes the file's sha256 and counts both block
kinds before comparing them to the three constants.

**The pinned catalog identity was re-pinned to this candidate's measurement.** This module pins the evidence catalogue's contract and artifact counts and the digest of `mcp/tests/evidence-lifecycle.toml`. The leaf registers one contract and one artifact, so the pins moved with them. **That sentence described `260915-KS-L12`'s leaf, whose pair took the pins to 14 contracts and 55 artifacts; the leaf that owns the pair now is `260915-KS-L21`, and the constants it moved read 15 contracts and 65 artifacts** with the digest this candidate's manifest actually hashes to (`c499cbcc…`, the merged candidate's measurement; `260915-KS-L30` re-pinned it from L28's `6ec7eb0d…` and `260915-KS-L31` added the merge-case consumer rows to it). The pins are measurements rather than constants: the module's own docstring carries the re-pin precedent, and a leaf that registers its own artifact advances both rather than weakening the assertion. A stale pin fails loudly, which is the point — the alternative is a catalog nobody re-measures.

**The catalog pin is a byte contract at one tip, and it has been re-pinned deliberately at every value
its records carry — one record per deliberate value, in file order — with this candidate's the newest.**
`LIFECYCLE_ARTIFACT_COUNT`
and `LIFECYCLE_CATALOG_SHA256` pin `mcp/tests/evidence-lifecycle.toml` by population and digest, and
`LOCR-R26@v1`'s doctrine is that any further catalog change must re-pin them **deliberately**, at its
own tip, with the reason recorded. **State both numbers, never the count alone**: the previous
"five times" wording on this card was itself the cause of a duplicate-ordinal defect (`L17-10`), so
the card keeps a count and its records side by side — **nine deliberate re-pins, and the constant now
carries the fifteenth contract and sixty-fifth artifact; the resolved ordinal is ambiguous and this card
names values by leaf rather than minting another meaning**. The value at this
candidate is **15 contracts / 65 artifacts** and
**`c499cbcc266088f35bd6fdde655f00579431591f02bba5c4859b72f767f65f06`**, recomputed directly from the
file at this tip (`sha256sum mcp/tests/evidence-lifecycle.toml`) and equal to the constant. **The
docstring beside the constants has moved since the sentence above was written, and the residue is narrower
than it says:** its opening paragraph now reads "fifteen contracts and sixty-five artifacts", and neither
the "five times" header nor the duplicated "Fourth deliberate re-pin" label this card used to report is in
the file any more; what survives are older branch counts further down its provenance narrative (`:233`
reads "fourteen contracts and fifty-five artifacts" of an earlier branch and `:254` reads "thirteen and
fifty-four … fourteen and sixty-four" of the merged base it landed against). **One residue is new at this
candidate:** the docstring's first paragraph still presents L28's `6ec7eb0d…` as "the value this line
carries", while the line now carries this candidate's `c499cbcc…` — the constants, not the prose, are the
authority, and the text is the owning builder's to correct. The reading a reader should
take is the constants' own — 15 / 65 / `c499cbcc…` — and the remaining residue is recorded here for the
owning builder rather than repaired by this card, exactly as the L16 record below treats the same class of
residue.

**`260915-KS-L31` re-pinned the digest again, with both counts unmoved.** The leaf's catalog change is the
pure consumer change this registry's own doctrine describes: two rows appended to the tail of
`mcp/tests/merge_case_test_support.py`'s exact list, one because `mcp/tests/test_worktree_sync.py` now
builds its knowledge-dataset conflict scenario through that harness and one because
`mcp/tests/test_sync_parked_candidate.py` reaches the harness transitively through its existing import of
`test_worktree_sync`. `sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate reproduces
**`c499cbcc266088f35bd6fdde655f00579431591f02bba5c4859b72f767f65f06`**, which is the value the constant
carries; the two count constants still read 15 and 65. The transitive row is the part worth carrying
forward: nobody edited that module, and it became a consumer of the harness the moment its import target
did, so a list naming only the module whose diff mentioned the harness would be refused by the validator
that derives real importers from the source graph.

The history the nine records carry, in landing order — each value correct **only** at its own tip:

**The newest record in that table is `260915-KS-L21`'s, and it is the first re-pin since the count moved that also
moved both numbers.** The census leaf appends one `[[contract]]` (`migration-census-cases`, owner
`mcp/tests/migration_census_test_support.py`) and one `[[artifact]]` for that same support module, so
`LIFECYCLE_CONTRACT_COUNT` moved 14 → **15**, `LIFECYCLE_ARTIFACT_COUNT` moved 64 → **65**, and
`LIFECYCLE_CATALOG_SHA256` was re-measured to the file's own bytes,
`1aef5f9b…` → **`633b03ee16893ce3d0e838659d52f2bc609903f5c75b142eb41ca8c4fdabf5e6`** — the value the
constant carries and `sha256sum mcp/tests/evidence-lifecycle.toml` reproduces on this candidate. The
artifact declares `category = "unit-regression"`, `fidelity = "local-composition"`,
`cadence = "affected"`, `introduced_by = "260915-KS-L21"`, `lifetime = "permanent"`,
`replacement_contract = "contract:migration-census-cases"` and `consumer_scope = "exact"` with exactly
one consumer, so the census fixture's registration is the whole of the population move. The evidence
node the contract binds is
`mcp/tests/test_migration_census.py::test_the_seed_writes_every_census_record_kind_through_the_shipped_batch_operation`.

**The ninth record is the one L17's landing left in place.**
Both of that leaf's earlier values are superseded working measurements, not records correct at any
committed tip: `8764ea1f…` was measured at its own base and `dca9c2f9…` after L14 landed, and
L17's landing retired the second. Nothing was registered by that leaf, no row was removed and no
artifact's identity moved: the catalog's only new bytes are two consumer entries.

**Text residue in the constant's own docstring (reported, not repaired here).** The docstring labels
**two** different entries "Fourth deliberate re-pin" — `260915-CAPS-L14`'s `5e938c85…` and
`260915-CAPS-L17`'s pre-sync `563582a0…` — and then labels this leaf's merged `e3651d6f…` the "Fifth".
So its header ("five times") and its entry count disagree, and the pre-sync value is presented as a
record when it is a superseded working measurement. That is the same class as this master's other
*"the sentence outlived the artifact"* residues, it lives in the **code** worktree's text rather than
in memory, and it is therefore recorded here for the owning builder rather than edited by this card.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No inferred full-suite population repairs an ownership gap. This retained test does not separately exercise every old pytest-plugin AST form.

- **A pin correct for someone else's base re-reds the moment the tip moves.** Whoever changes the
  catalog last pins the value at its own tip; it is re-derived, never borrowed, and a leaf that edits
  the catalog without re-pinning hands the next candidate a red. The third and fifth re-pins are the
  proof in the consumer-rows direction — consumer rows alone moved the digest while the populations
  stayed put.
- **The re-pin is a byte contract, not a closure.** The pinned value is correct at this tip and only at
  this tip: any later leaf that changes `mcp/tests/evidence-lifecycle.toml` must re-pin again.
- **A consumer row is a catalog change.** Registering, removing or re-identifying an artifact is not
  the only thing that moves the digest — an importer reaching a governed artifact through shared test
  support does too, which is why the pin is re-derived from the file's bytes rather than maintained by
  hand.
- **A pre-sync measurement is not a record.** `563582a0…` was measured against 51 artifacts before L14
  landed and is wrong at any later tip; a value that no committed tip ever carried must not be
  presented as one of the deliberate re-pins.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Repository inputs reach their supported consumers. [1]
- **The evidence catalog's pinned shape and bytes, and the deliberate re-pin this leaf made in the same change as its consumer rows — whose value at this candidate is **16 contracts / 66 artifacts** and `8d60a34cf56a9740e234823658312c8b6f5ae4e958344fe8ba2ea152b8ff6891`, the `260921-ICR-L9` measurement (the card's previous wording named `53ba6331…`, the `260921-ICR-L6` measurement, which was already stale at the landed base and is corrected rather than carried).** [2]
- **The check that makes the pin real: the file's bytes recomputed and both block kinds counted before either is compared.** [3]
- **The check that makes the pin real: the file's bytes recomputed and both block kinds counted before either is compared.** [4]
- The closure check over the governed inventory, and the lane-membership check. [5]
- **The contract and artifact blocks the pin counts, added by this leaf, and the consumer list its sibling artifact gained.** [6]
- **The contract and artifact blocks the pin counts, added by this leaf, and the consumer list its sibling artifact gained.** [7]
- The catalog pin constants, and the re-pin narrative the docstring carries beside them — **whose newest paragraph is now `260921-ICR-L14`'s `Sixteenth deliberate re-pin` (the synced union onto `260921-ICR-L3`'s fifteenth), and whose extent is the whole docstring.** [8]
- The three consumer entries the `260915-CAPS-L17` re-pin added to three governed-artifact rows, the entire reason the digest moved at that re-pin. [9]
- The three consumer entries the `260915-CAPS-L17` re-pin added to three governed-artifact rows, the entire reason the digest moved at that re-pin. [10]
- The three artifacts those rows belong to, each an already-governed row rather than a new registration. [11]
- The population the pin names, re-derived at this candidate's own tip — **16 contracts and 66 artifacts**, the values the constants below carry. [12]
- The three consumer entries the `260915-CAPS-L15` re-pin added to three governed-artifact rows, whose shape the `260915-CAPS-L17` entries repeat. [13]
- The three consumer entries the `260915-CAPS-L15` re-pin added to three governed-artifact rows, whose shape the `260915-CAPS-L17` entries repeat. [14]
- The catalog pin constants, and the re-pin narrative the docstring carries beside them — **whose last paragraph is this leaf's `Thirteenth deliberate re-pin`, and whose extent is now the whole docstring.** [15]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
- **The evidence catalog's pinned shape and bytes, the deliberate re-pin this leaf made in the same change as its consumer rows, and the provenance paragraph that records the consumer-only shape of that change.** [16]

## KS-R15@v1 Catalogue Re-Pin

The evidence-lifecycle catalogue identity is pinned in this module, and this leaf re-pinned it because
a **consumer list** changed: the new integration module is registered as a consumer of the shared
support module owned by `curator-coherence-test-port`. No `[[contract]]` or `[[artifact]]` pair was
added, so the counts are unchanged at 13 contracts and 54 artifacts while the digest moves.

The pin now carries the value measured on this candidate,
`9ff8a75f17c87b8db87e7fb560b93e8481a2ecd6ba4be652fcaa7918a0044d79`, and the comment beside it
records what changed and why. The governed-inventory guard validates the change in both directions: a
consumer row inserted into the wrong block is refused by name, which is how this leaf's own misplaced
first attempt was caught.

## KS-R16@v1 Catalogue Re-Pin — Consumer Rows Only, And Two Records That Disagree With The Tree

`KS-R16@v1`'s three test modules reach the shipped shared support their neighbours already use, so this
leaf's catalogue change is again a **consumer change only**: `mcp/tests/diff_scope_test_support.py` gained
one row (`mcp/tests/test_knowledge_family_integrity_pipeline.py`) and
`mcp/tests/read_scope_test_support.py` gained two
(`mcp/tests/test_knowledge_family_integrity_pipeline.py` and
`mcp/tests/test_knowledge_registered_scope.py`). No `[[contract]]` and no `[[artifact]]` was added, so
`LIFECYCLE_CATALOG_SHA256` was re-pinned to the file's own measured digest —
`143b0cf5c3a8432450f45072b7351057ba51fe6c386f65eb662c0ec4cb729ce6`, which re-hashing
`mcp/tests/evidence-lifecycle.toml` on this candidate reproduces exactly — while the two counts are
unchanged.

**The counts this leaf's own prose states are not the counts the constants carry, and the constants are the
authority.** `LIFECYCLE_CONTRACT_COUNT` reads **14** and `LIFECYCLE_ARTIFACT_COUNT` reads **64** on this
candidate (the merge onto the moved super line raised them), while the provenance paragraph the leaf added
beside them says the counts "stay thirteen and fifty-four". The paragraph is a record of one leaf's
*consumer-only* shape and its arithmetic is stale against the declarations it sits above; nothing here was
corrected in the code, which is not this seat's to edit. The leaf's worker report also names the re-pinned
digest as `b0bedae9071ec992cb011ba3e327ae67ff4c9728d9290bdfcdd50caff1263dd7`, **a value that appears
nowhere in the tree** — the same class of discrepancy L17's entry already recorded against this pin, and
the reason this card states the digest by measurement rather than by report. The rule the earlier entries
state is unchanged: **a catalog change must re-pin deliberately in the same change, with the counts moving
with the blocks they count**, and the reason written beside the constant is what makes the re-pin auditable
rather than convenient.

## KS-R21@v1 Catalogue Re-Pin — The First Re-Pin Since L11 That Moves Both Counts

`260915-KS-L21` changes `mcp/tests/evidence-lifecycle.toml` by **appending one `[[contract]]` and one
`[[artifact]]`**, so both pinned counts move and the digest is re-measured against the file's own bytes:

| Constant | Was (this card's previous reading) | Is now |
| --- | --- | --- |
| `LIFECYCLE_CONTRACT_COUNT` | 14 | **15** |
| `LIFECYCLE_ARTIFACT_COUNT` | 64 | **65** |
| `LIFECYCLE_CATALOG_SHA256` | `1aef5f9b…` | **`633b03ee16893ce3d0e838659d52f2bc609903f5c75b142eb41ca8c4fdabf5e6`** |

| Registration | Anchor | Source |
| --- | --- | --- |
| The appended contract: its id, its owner and the real node it binds. | "migration-census-cases" | mcp/tests/evidence-lifecycle.toml:74-76 |
| The appended artifact: the census fixture, with its declared kind, authority, category, fidelity, cadence, introducing leaf, lifetime, replacement contract and exact consumer list. | `"mcp/tests/migration_census_test_support.py"`; `"contract:migration-census-cases"` | mcp/tests/evidence-lifecycle.toml:1676-1692; mcp/tests/evidence-lifecycle.toml:1700-1720 |

The contract is `id = "migration-census-cases"` at `mcp/tests/evidence-lifecycle.toml:74-76`, whose owner
is `mcp/tests/migration_census_test_support.py` and whose evidence node is
`mcp/tests/test_migration_census.py::test_the_seed_writes_every_census_record_kind_through_the_shipped_batch_operation`
— the one real node that proves the census records travel the shipped candidate write path rather than a
fixture's inserts. The artifact is that same support module at `:1613-1630`, declared
`shared-support` / `internal-canonical` / `unit-regression` / `local-composition` /
`cadence = "affected"` / `introduced_by = "260915-KS-L21"` / `lifetime = "permanent"` with
`replacement_contract = "contract:migration-census-cases"` and `consumer_scope = "exact"` over exactly one
source-derived consumer (`mcp/tests/test_migration_census.py`). This is the **tenth** deliberate re-pin and
the first since `260915-KS-L11` where the block kinds move rather than only the bytes, which is why the
card's `4 / 54` and `13 / 54` and `14 / 55` statements above are each retained as the measurements of the
tips that produced them.

A reader should take the **declarations**, not the prose beside them: the constant's own docstring still
opens "fourteen contracts and sixty-four artifacts" and repeats its provenance narrative twice, which is the
known text residue the L16 record above already named for the owning builder. The authority is
`sha256sum mcp/tests/evidence-lifecycle.toml` reproducing `633b03ee…` and the catalog's own blocks counting
`15 [[contract]]` / `65 [[artifact]]`.

## 260915-KS-L22 Catalogue Re-Pin — The Tenth, Moving Only The Digest

`260915-KS-L22` re-pins the catalogue identity a tenth time, and this is the first re-pin of the
series whose **counts do not move**. The leaf adds no `[[contract]]` and no `[[artifact]]`; it
appends one consumer entry to each of two already-governed artifacts
(`mcp/tests/diff_scope_test_support.py`, `mcp/tests/read_scope_test_support.py`), so the population
stays at **15 contracts and 65 artifacts** while the file's bytes change and only the digest moves:

| Constant | Was (the L21 value this card carried) | Is now |
| --- | --- | --- |
| `LIFECYCLE_CONTRACT_COUNT` | 15 | **15** (unchanged) |
| `LIFECYCLE_ARTIFACT_COUNT` | 65 | **65** (unchanged) |
| `LIFECYCLE_CATALOG_SHA256` | `633b03ee16893ce3d0e838659d52f2bc609903f5c75b142eb41ca8c4fdabf5e6` | **`68a64207bd808eafd31f8c6b23856302c5ef2d150a604aa8177427e5906a1012`** |

The new digest is `sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate, and the two
constants beside it are the file's own block counts (`15 [[contract]]`, `65 [[artifact]]`) — so the
constant pair and the file agree, and the re-pin is auditable by re-measuring rather than by trusting
the narrative beside it. That narrative is the one residue this card keeps naming: the
`LIFECYCLE_CATALOG_SHA256` docstring still repeats its provenance story in two overlapping passages
and still carries counts older than the values above, which is the owning builder's text to correct
and not this seat's to edit. **The authority is the declarations.**

## 260915-KS-L23 Catalogue Re-Pin — Bytes Only, Four Consumer Rows

`260915-KS-L23` re-pins the catalogue identity again, and this is the second consecutive re-pin whose
**counts do not move**. The leaf adds no `[[contract]]` and no `[[artifact]]`; its whole change to the
catalogue is **four consumer entries appended to three already-governed artifacts** — item 13's three
(`mcp/tests/test_knowledge_merge_right_side_writes.py` on `merge_case_test_support.py:1287`;
`mcp/tests/test_evidence_catalog_gate_boundaries.py` on `_evidence_catalog_fixture.py:172` and on
`test-evidence-lanes.toml:806`) plus one the item-16 case itself created
(`mcp/tests/test_memory_citation_resolution.py` on `test-evidence-lanes.toml:807`, because that case reads
the shipped lane manifest) — so the population stays at **15 contracts and 65 artifacts** while the file's
bytes move and only the digest does:

| Constant | Was (the L22 value this card carried) | Is now |
| --- | --- | --- |
| `LIFECYCLE_CONTRACT_COUNT` | 15 | **15** (unchanged) |
| `LIFECYCLE_ARTIFACT_COUNT` | 65 | **65** (unchanged) |
| `LIFECYCLE_CATALOG_SHA256` | `68a64207bd808eafd31f8c6b23856302c5ef2d150a604aa8177427e5906a1012` | **`25b00f8832420b705495931c3a04ad13a9bfe83e367a97c4a854b36030071e30`** |

The new digest is `sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate and is the value the
constant carries; the two constants beside it are the file's own block counts, re-counted here
(`15 [[contract]]`, `65 [[artifact]]`) rather than carried from prose.

**Every one of the four rows is appended to the tail of its list, and that is the ruling this leaf enforces
(item 16 half (a)).** An insertion in sorted position inside a `consumers` list shifts every line below it
and stales every citation into this file; appending at the end of the list moves nothing, so a consumer row
is now line-stable. The property is pinned by
`mcp/tests/test_memory_citation_resolution.py::InsertedRegistrationRangeDriftTests::test_the_shipped_registries_append_point_is_the_end_of_its_own_list`,
which measures the shipped registries and also asserts that a contrasting mid-list insertion *does* move a
row, so it cannot pass vacuously; the half (b) paired with it classifies a citation whose anchor survived a
move as a **report-only** stale range rather than as curator work. No header comment stating the new append
point was added to either registry, deliberately: a line at the top of the file would shift every row and
stale hundreds of citations — the comment would itself be the defect.

**The ordinal this card's records carry is ambiguous, and this section names values rather than minting a
third meaning.** The re-pin table in `### Logic` ends at `tenth` (`260915-KS-L21`) while the L22 section
below also calls its own re-pin "the tenth", because the two counters differ on whether the initial R16
landing pin is counted; two further values have landed since. The values are therefore named by leaf —
the L21 landing's `633b03ee…`, the L22 landing's `68a64207…`, this leaf's `25b00f88…` — and the running ordinal, including the "nine
deliberate re-pins" the `### Logic` paragraph and the history line below still carry, is left to the owning
builder rather than re-derived here.

**This catalogue sits behind two gates, and only one of them is this pin.** The **catalog byte pin** in this
module answers "is this the exact catalogue file that was measured, at the populations it was measured at?"
and its documented repair is a re-pin. The **consumer-completeness oracle**
(`load_evidence_inventory`, `mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py`,
whose docstring now names both gates at `:1-18`) answers "does the catalogue agree with the source tree it
describes?" and its documented repair is a registry row — which is why the constants above move when a row
is *added*, as they did here, rather than when the source tree drifts.
`mcp/tests/test_evidence_catalog_gate_boundaries.py` holds the case that reddens the oracle while this pin's
bytes are untouched.

## 260915-KS-L30 Catalogue Re-Pin — Consumer Row Only, Counts Unchanged

`260915-KS-L30` re-pins the catalogue identity again, and it is one more re-pin whose **counts do not
move**: the leaf adds no `[[contract]]` and no `[[artifact]]`, and its whole change to the catalogue is
**one consumer row appended to an already-governed artifact** —
`mcp/tests/test_knowledge_curator_ingest_list.py` on the
`mcp/tests/snapshot_lifecycle_test_support.py` artifact (`mcp/tests/evidence-lifecycle.toml:1267`,
inside that artifact's `consumers` list at `:1265-1270`, whose
`replacement_contract = "contract:knowledge-snapshot-lifecycle-cases"` and
`consumer_scope = "exact"`). The driver is real rather than incidental: the CYCLE-01 continuity case
imports `build_case`, `create` and `write_record` from that support module to obtain a real candidate
database whose stored namespace the operation must read, and an import edge is a declared consumer.

| Constant | Was (the value at this leaf's base) | Is now |
| --- | --- | --- |
| `LIFECYCLE_CONTRACT_COUNT` | 15 | **15** (unchanged) |
| `LIFECYCLE_ARTIFACT_COUNT` | 65 | **65** (unchanged) |
| `LIFECYCLE_CATALOG_SHA256` | `6ec7eb0d33e91c148b25ed64c6b791664446082bdf419bf511635f4ca3cbdd75` | **`73cdd2183e153af752773e8a4c6076e5e2eb7053d9e0ce5fa6538a69c907cefe`** |

The new digest is `sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate and is the value the
constant carries; the two constants beside it are the file's own block counts, re-counted here
(`15 [[contract]]`, `65 [[artifact]]`) rather than carried from prose. The row is appended at the
**tail** of its list, which is the L23 ruling this leaf keeps: an insertion in sorted position would
shift every line below it and stale every citation into the file.

**Two values between the L23 record and this one are named rather than narrated, because this card
carries no section for them.** The digest this leaf re-pinned *from* is `6ec7eb0d…`, the constant at
this leaf's base, which the source's own docstring attributes to `260915-KS`'s L28 leaf repairing the
missing-consumer registration that reddened the repository's own gate step. This card has no L28
section: the value it recorded last is L23's `25b00f88…`, so L28's `6ec7eb0d…` and this leaf's
`73cdd218…` are the two values that landed after it, and the ordinal question the L23 section already
records stays open rather than being re-derived here. The chain a successor should read is therefore
`633b03ee…` (L21, the census leaf, the first re-pin since L11 that moved both counts) → `68a64207…` (L22, bytes only) → `25b00f88…` (L23, four consumer rows) → `6ec7eb0d…` (L28, recorded here from the
source's own text) → `73cdd218…` (L30's re-pin, correct only at L30's own tip) → `c499cbcc…` (the merged candidate of the L31-era re-pin, recorded in the L31 re-pin section below) → `f0cb5fec…` (the value `LIFECYCLE_CATALOG_SHA256` carried when `260921-ICR-L1` cut, per that paragraph's own record) → `24e760a1…` (this leaf's re-pin, the value the constant carries now), each correct only at its own tip.

## 260921-ICR-L20 Re-Pin — Consumer Rows Only, Counts Unchanged, And The Digest This Leaf's Two Rows Moved

This leaf's catalog change is the same shape as its two predecessors on this master: a **pure consumer
change**. `mcp/tests/test_knowledge_ingest_publication_route.py` reaches
`mcp/tests/snapshot_lifecycle_test_support.py` through the ingest-list fixture module it imports, and the
census's own propagation rule reaches the Node `package-lock.json` fixture through the CLI import chain
those rows already name — so exactly two `consumer_scope = "exact"` rows gained the path, **no
`[[contract]]` and no `[[artifact]]` was added or removed**, and every artifact's own identity is
unmoved.

**Measured on this leaf's own merge, from the file's own bytes and the catalog's own paragraph (and
superseded on the sync line by `260921-ICR-L11`'s two consumer rows — see the section above):**
`LIFECYCLE_CATALOG_SHA256` carries
`51a218a09ea5721197cb15b445f98fb8f1dd734c2d083124c913226e599a8745` — the sha256 of the merged
`mcp/tests/evidence-lifecycle.toml`, which holds both this leaf's two consumer rows and `260921-ICR-L6`'s
one — replacing `3f91773d…`, and the counts stay at **16 contracts / 66 artifacts**, which is what
`LIFECYCLE_CONTRACT_COUNT` and `LIFECYCLE_ARTIFACT_COUNT` carry. The source's own paragraph for this leaf
records the same thing in place (above the `260918-TSIP-L10` paragraph, below the `260921-ICR-L1` one),
and the constants — not the prose — remain the authority. The digest this leaf alone measured on its own
candidate was `4da562629ba16373ce387f0b7cfe83f110eede155fced865de9fa92f7eb41df7`; that value is
**historical**, correct only at this leaf's pre-merge candidate, and the merged paragraph and constant
carry `51a218a0…`. `260921-ICR-L6`'s own paragraph above keeps *its* historical value (`7920a0f9…`) for
the same reason: each paragraph records the bytes its own measurement saw.

**The source file also grew by two paragraphs, and that is what moved the citations.** This leaf's
insertion is 16 lines after line 87 (its paragraph now occupies `:105-119`) and `260921-ICR-L6`'s is
above it at `:49-64`, so every range this card and its sibling cards carry into
`mcp/tests/test_dependency_ownership_ast_helpers.py` below line 64 was re-derived rather than shifted;
the rows into `mcp/tests/evidence-lifecycle.toml` moved with the consumer rows the two leaves added
(`:733` and `:1271` from this leaf, `:1442` from L6), by one line at or below `:733` and by two at or
below `:1271`.

- **The re-pinned constants, with the counts this leaf did not move and the digest the merged catalog carries.** [17]
- **The source's own paragraph for this leaf: consumer-only, counts unchanged, and the digest it replaced (re-read at `260928-MIK-L10`: the paragraph is unchanged and sits eleven lines lower again, under the Fortieth, Thirty-ninth, Thirty-eighth and Thirty-seventh re-pin notes; the constant it describes now holds L10's Fortieth value, cited in the L10 section).** [18]
- **The source's own paragraph for this leaf, below the later re-pin notes (the Thirty-ninth, `260928-MIK-L01`, now first): consumer-only, counts unchanged, and the digest it replaced.** [19]
- The two consumer rows this leaf's module joined, and the lane row the same module occupies. [20]
- The catalog check that recomputes the file's sha256 and counts both block kinds beside it. [21]
- The catalog check that recomputes the file's sha256 and counts both block kinds beside it. [22]
- The leaf's own case module, which is why no third fixture was registered. [23]

## 260921-ICR-L1 Catalogue Re-Pin — Two Consumer Rows, And The Counts Corrected To What The Constants Read

This leaf's catalog change is a **pure consumer change**: it appends one row to the tail of each of two
existing `consumer_scope = "exact"` lists — `mcp/tests/diff_scope_test_support.py` (owner
`knowledge-diff-cases`) and `mcp/tests/read_scope_test_support.py` (owner `knowledge-read-scope-cases`) —
both for `mcp/tests/test_knowledge_review_source_endpoints.py`, whose source-endpoint cases compose those
two fixtures rather than introducing a third. **No `[[contract]]` and no `[[artifact]]` was added**, so the
populations do not move, and the digest is re-pinned deliberately in the same change rather than silently
widened to keep a green run.

**Measured on this candidate, from the file's own bytes and declarations:** `sha256sum
mcp/tests/evidence-lifecycle.toml` is `24e760a124d5f0d3a608295533720168b47e8a2ee28f6ee85c493e3778cdbed4`
— which is what `LIFECYCLE_CATALOG_SHA256` carries — and counting the blocks gives **16 `[[contract]]`
and 66 `[[artifact]]`**, which is what the two count constants carry. **The count half of that reading is
a correction this pass owed the card, not a change this leaf made**: the re-pin narrative above and the
constants paragraph in `### Logic` both said `15 / 65` and `c499cbcc…` until now, which was the pair
`260915-KS-L40`'s candidate carried; `260918-TSIP-L10`'s `T129` reconciliation had already moved the counts
to 16 / 66 afterwards. Both statements were corrected against the constants and the file's own blocks in
this pass, and the `f0cb5fec…` value this leaf replaced is recorded beside them.

**What the leaf's own source change also does.** The constants' docstring gained the paragraph naming this
leaf's consumer-only change and its two rows — placed above the `260918-TSIP-L10` paragraph — and that
prose is the file's own record of the re-pin; the constants, not the prose, remain the authority.

- **The re-pinned constants, with the counts this leaf did not move and the digest it did.** [24]
- **The source's own paragraph for that leaf: consumer-only, two support modules, counts unchanged, and the digest it replaced.** [25]
- The two appended consumer rows, on the two artifacts whose exact lists gained this module. [26]
- The catalog check that recomputes the file's sha256 and counts both block kinds beside it. [27]
- The catalog check that recomputes the file's sha256 and counts both block kinds beside it. [28]
- The leaf's own case module, which is why no third fixture was registered. [29]

## 260921-ICR-L18 Re-Pin — Consumer Rows Only, Counts Unchanged, Bytes Moved

This leaf moved exactly one value in this file: `LIFECYCLE_CATALOG_SHA256`, from
`24e760a124d5f0d3a608295533720168b47e8a2ee28f6ee85c493e3778cdbed4` to
`4fb2bc3f2da65134e428631f0e964f4f712e6655f4816934e2a93a4cb8e32046`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the delivered candidate. The two count constants beside
it are **untouched**: `LIFECYCLE_CONTRACT_COUNT` stays `16` and `LIFECYCLE_ARTIFACT_COUNT` stays `66`,
because `260921-ICR-L18` registered no artifact and no contract of its own — its two new unit modules
joined two existing `consumer_scope = "exact"` lists, and a consumer registration is not an artifact.
The proof's own artifact delta therefore remains exactly empty, which is what
`test_production_proof_adds_no_governed_evidence_artifact` measures.

**Corrected at the sync: this leaf's paragraph is no longer the first one in the pin's docstring.** It
sits at `:82-96`, below `260921-ICR-L6`'s paragraph at `:49-64`, which the sync wrote last and the
newest-first convention therefore places first. The claim's subject survives unchanged — the docstring
is ordered so that a reader asking why the digest is what it is reads the leaf that last moved it, and
that paragraph states the consumer-only shape, names both new modules, and names the two artifacts
whose lists gained them. This is the thirteenth re-pin narrative in the docstring and it follows the
convention every re-pin before it followed: the narrative is added, no earlier narrative is rewritten,
and the constants — not the prose — remain the authority.

- **The re-pinned digest and the two counts this leaf did not move.** [30]
- **The source's own paragraph for this leaf: consumer-only, two existing support builders reused, counts unchanged, and the digest it replaced.** [31]
- The catalog whose bytes the pin names, and the artifact row whose consumer list gained both modules. [32]
- The proof that this leaf's artifact delta is empty, which is why only a consumer change could move the digest. [33]
- The proof that this leaf's artifact delta is empty, which is why only a consumer change could move the digest. [34]
- The catalog whose bytes the pin names, and the two `[[artifact]]` blocks whose consumer lists gained both modules. [35]
- The two new modules whose lane rows this leaf added, which is the change the pin follows. [36]

## 260921-ICR-L6 Catalogue Re-Pin — One Consumer Row, Counts Unchanged, Bytes Moved

This leaf moved exactly one value in this file: `LIFECYCLE_CATALOG_SHA256`, from
`3f91773d5533139aa24df0e75ddafcecbc68cd9797b7663084f8aca567176c57` — L18's own measurement on
`71a4433e`, which is this leaf's merged base — to
`7920a0f9f6134d3849e60685ad8a9424cdc95e8209631a03b889cf7d79e05281`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate. The two count constants beside
it are **untouched**: `LIFECYCLE_CONTRACT_COUNT` stays `16` and `LIFECYCLE_ARTIFACT_COUNT` stays `66`,
because `260921-ICR-L6` registered no artifact and no contract of its own — its case module joined one
existing `consumer_scope = "exact"` list, and a consumer registration is not an artifact. The proof's
own artifact delta therefore remains exactly empty, which is what
`test_production_proof_adds_no_governed_evidence_artifact` measures.

**Why the bytes moved, and why the row beside this leaf's is not this leaf's claim.** The ICR-R06 cases
drive the real review composition over two real read-scope snapshots, so
`mcp/tests/test_knowledge_review_one_sided_statements.py` belongs on
`mcp/tests/read_scope_test_support.py`'s consumer list. That is the **one** path this leaf added there:
L18's landed consequence repair already carried `mcp/tests/test_read_ar_files.py` for the L19 import,
the two are kept as a set because the census compares consumer sets, and the reason no third fixture
exists is the same as the sibling leaf's — the new cases compose the two existing shared-support
fixtures rather than introducing one.

**The docstring gained the paragraph that records this re-pin, and the sync placed it first** because it
was written last: the docstring is newest-first, so the reader asking why the digest is what it is reads
`` **Thirteenth deliberate re-pin (260921-ICR-L6, at the sync onto ``71a4433e``, 2026-09-21) -- the
union of two consumer repairs, re-measured on the merged file.** `` at `:49-64`, above `260921-ICR-L18`'s
paragraph at `:82-96` and `260921-ICR-L1`'s at `:98-103`. Its 16 lines are what moves every construct
below it, and the merged extents are: docstring `47-398`,
`test_repository_inputs_reach_their_supported_consumers` (`406-425`),
`test_production_proof_adds_no_governed_evidence_artifact` (`429-445`),
`_assert_the_proof_is_ordinary_test_source` (`448-460`),
`_assert_the_proof_is_selected_by_the_lane_manifest` (`463-473`),
`_assert_the_governed_inventory_is_closed` (`476-493`) and
`_assert_the_catalog_kept_its_bytes_and_identities` (`496-512`). The constants, not the prose, remain
the authority.

- **The re-pinned digest, with the two counts this change leaves alone.** [37]
- **The source's own paragraph for this leaf: the union of two consumer repairs, no registration, counts unchanged, and the digest it replaced. It is no longer first in the docstring: the later records sit above it, most recently `260928-MIK-L10`'s Fortieth, and the constant now holds that leaf's value, cited in the L10 section.** [38]
- The catalog check that recomputes the file's sha256 and counts both block kinds beside it — re-derived here because this leaf's row and paragraph moved it. [39]
- The catalog check that recomputes the file's sha256 and counts both block kinds beside it — re-derived here because this leaf's row and paragraph moved it. [40]
- **The row this leaf registered, and L18's landed row immediately beside it, each named exactly once.** [41]
- **The row this leaf registered, and L18's landed row immediately beside it, each named exactly once.** [42]
- The artifact those two rows belong to, which is already governed and is why no third fixture was registered. [43]
- The population the pin names, re-derived at the merged tip — **16 contracts and 66 artifacts**, the values the constants below carry. [44]
- **The source's own paragraph for this leaf, once first in the docstring and now below the later records (the Thirty-ninth, `260928-MIK-L01`, on top): the union of two consumer repairs, no registration, counts unchanged, and the digest it replaced.** [45]

## 260921-ICR-L11 Catalogue Re-Pin — Two Consumer Rows, Counts Unchanged, Bytes Moved (The Fourteenth)

The catalog change is **consumer rows only, and it is the same shape as L1's, L18's and L6's**: the
durable-comparison-generation leaf registers no artifact and no contract of its own, and its fifteen
cases live in the ordinary unit module `mcp/tests/test_knowledge_review_comparison_generation.py`, which
builds on the existing `test_knowledge_review_source_endpoints.py` enclosure fixture. That module became
a source-derived consumer of two existing shared fixtures, so both `consumer_scope = "exact"` lists
gained exactly one path each:

| Artifact | Row that gained the path | Why the module consumes it |
| --- | --- | --- |
| diff-cases (`contract:knowledge-diff-cases`) | `mcp/tests/evidence-lifecycle.toml:1421-1421` | the cases read the candidate's content back out of the retained tree and build the enclosure over two real committed Git trees |
| read-scope (`contract:knowledge-read-scope-cases`) | `mcp/tests/evidence-lifecycle.toml:1447-1447` | the frozen comparison is between two snapshots of that fixture's recorded topology; the module imports `BATCH_PATH` |

Both entries were derived from the census's own finding — `missing=['mcp/tests/test_knowledge_review_comparison_generation.py']`
with `unsupported=[]` on both rows — which is the rule this card exists to enforce: a
`consumer_scope = "exact"` list must equal the source-derived consumer set, whether or not anybody wrote
the consumer down.

**The measured value, and the paragraph above this section is superseded by it.** `LIFECYCLE_CONTRACT_COUNT`
stays **16** and `LIFECYCLE_ARTIFACT_COUNT` stays **66** — nothing was registered, no row was removed and
no artifact's identity moved — while `LIFECYCLE_CATALOG_SHA256` moves from L6's
`7920a0f9f6134d3849e60685ad8a9424cdc95e8209631a03b889cf7d79e05281` to
**`6b73894fb010534d5cedbdace361504d1a67abb2ce8ffb76de8d00ac2e0af39e`**, the value this leaf's own
candidate measured (`1673` lines). **On the merged line the constant carries
`aedb2636844faf41ca63b7099e6c62bcaf888720e7e7dd78e203e3a1c9e061ff`** (`1675` lines, this leaf's two consumer rows plus
`260921-ICR-L20`'s two), and the constant's own docstring numbers this leaf's record the **fourteenth
deliberate re-pin** — so the declaration and the prose agree at this tip.

**Ordinal note, because two entries claimed the same count.** `260921-ICR-L20`'s history entry below also
says "fourteenth" — that is the ordinal its own candidate's count gave it, and the merge superseded its
value: the source's docstring now carries one unnumbered paragraph for that leaf (stating the merged
digest) and numbers this leaf's record fourteenth. Read that entry's ordinal as that leaf's as-of record,
not as a competing current count.

- **The pinned counts and the re-pinned digest, as this leaf's own candidate and as the merged line carry them.** [46]
- **The constant's own fourteenth re-pin record, which names this leaf, its base and the two consumer rows.** [47]
- The two rows this leaf appended, and the artifacts whose exact consumer sets they extend. [48]
- The module whose two consumer entries are the entire catalog delta. [49]
- The lane row added to the manifest in the same change, which pins no digest and refuses an unregistered module at collection. [50]

## 260921-ICR-L3 Catalogue Re-Pin — Two Consumer Rows, Counts Unchanged, Bytes Moved (The Fifteenth)

The one value this leaf moved in this file is `LIFECYCLE_CATALOG_SHA256`, from L11's
`aedb2636844faf41ca63b7099e6c62bcaf888720e7e7dd78e203e3a1c9e061ff` to
`dc6e380867302d7e2fff89f8c36549c85528ed4dafa28b4510981b573f09739b`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate. The two count constants beside it
are **untouched**: `LIFECYCLE_CONTRACT_COUNT` stays `16` and `LIFECYCLE_ARTIFACT_COUNT` stays `66`, because
`260921-ICR-L3` registered no artifact and no contract of its own — its twenty source-content cases live in
the ordinary unit module `mcp/tests/test_knowledge_review_source_content.py`, which extends the existing
`test_knowledge_review_source_endpoints.py` enclosure fixture rather than introducing a second one, so its
whole catalog footprint is **two consumer entries**: one on each of the two existing
`consumer_scope = "exact"` rows it is a source-derived consumer of. The proof's own artifact delta
therefore remains exactly empty, which is what
`test_production_proof_adds_no_governed_evidence_artifact` measures.

**The constant's docstring gained the paragraph that records this re-pin, and it is first because the
docstring is newest-first.** The paragraph now opens the pin's own text at `:49-66`, above L11's
`Fourteenth deliberate re-pin` at `:68-85` and L6's `Thirteenth deliberate re-pin` at `:87-102`; it records
what was registered (nothing), the two rows that moved the bytes, the census finding the two paths were
derived from (`missing=['mcp/tests/test_knowledge_review_source_content.py']` with `unsupported=[]` on both
rows), the counts that did not move, the value it replaced and the fact that the module's own lane row was
added to `mcp/tests/test-evidence-lanes.toml`, which pins no digest and refuses an unregistered module at
collection. **The insertion is 19 lines inside the docstring only**, so the four constants at `:43-46` keep
their lines and every construct below `:48` in the base reads 19 lines lower on this candidate — the
docstring now ends at `:453`, `test_repository_inputs_reach_their_supported_consumers` sits at `:459-479`,
`test_production_proof_adds_no_governed_evidence_artifact` at `:482-499`,
`_assert_the_proof_is_ordinary_test_source` at `:502-514`,
`_assert_the_proof_is_selected_by_the_lane_manifest` at `:517-527`,
`_assert_the_governed_inventory_is_closed` at `:530-547` and
`_assert_the_catalog_kept_its_bytes_and_identities` at `:550-566`. The constants, not the prose, remain the
authority.


**One code-side inaccuracy is recorded rather than silently reconciled.** The paragraph the constant's
docstring gained says `260921-ICR-L3`'s "sixteen source-content cases", while the module it names defines
**twenty** `test_` functions — the count this card and the leaf's other records state. The docstring is code
and not this seat's to edit, so the discrepancy is named here for the owning builder; the constants and the
module's own collected cases remain the authority.

- **The re-pinned constants, with the counts this leaf did not move and the digest it did.** [51]
- **The source's own paragraph for `260921-ICR-L3`, third in the docstring after the Seventeenth and the synced union: no registration, two consumer rows, counts unchanged, and the digest it replaced.** [52]
- **The synced union paragraph, second in the docstring after this leaf's Seventeenth: both leaves' consumer rows in one catalog, and the digest the merged file measures.** [53]
- The two consumer rows the leaf's module joined, and the artifact identities they belong to. [54]
- The check that recomputes the file's sha256 and counts both block kinds beside it. [55]
- The proof that this leaf's artifact delta is empty, which is why only a consumer change could move the digest. [56]
- The lane row the same change added, which pins no digest and refuses an unregistered module at collection. [57]
- **The re-pinned constants, with the counts this leaf did not move and the digest it did (`3e9105c2…` → `8d60a34c…`, the Seventeenth re-pin).** [58]
- **The source's own paragraph for this leaf: consumer-only, two exact-scope support rows, counts unchanged, and the digest it replaced.** [59]
- **The two consumer rows this leaf's module joined, and the artifact identities they belong to.** [60]
- The check that recomputes the file's sha256 and counts both block kinds beside it, re-derived because the docstring's new paragraph moved it. [61]
- The proof that this leaf's artifact delta is empty, which is why only a consumer change could move the digest. [62]
- The lane row the same change added, which pins no digest and refuses an unregistered module at collection. [63]

## 260921-ICR-L8 Re-Pins — Three Case Modules, Six Consumer Rows, Counts Unchanged (The Eighteenth, Nineteenth And Twentieth)

`260921-ICR-L8` (`ICR-R08@v1`, movement and relationship evolution) registered **no artifact** and no
contract of its own. Its twenty-three cases live in three ordinary unit modules —
`mcp/tests/test_knowledge_review_relationship_movement.py` (eleven), `…_reach.py` (seven) and
`…_line.py` (five) — each authored through the public store operations inside the existing
`mcp/tests/test_knowledge_review_source_endpoints.py` enclosure and each importing the shared builders
from its siblings rather than duplicating them. Each is therefore a source-derived consumer of the same
**two** `consumer_scope = "exact"` rows (the candidate's own transitions in
`mcp/tests/diff_scope_test_support.py` and the recorded topology in
`mcp/tests/read_scope_test_support.py`), derived from the census's own finding
(`missing=['<the module>']` with `unsupported=[]` on both), and each gained its own `unit-regression` lane
row in `mcp/tests/test-evidence-lanes.toml`. **Nothing was registered, no row was removed and no
artifact's identity moved**, so `LIFECYCLE_CONTRACT_COUNT` stays `16` and `LIFECYCLE_ARTIFACT_COUNT`
stays `66`; the proof's own artifact delta remains exactly empty, which is what
`test_production_proof_adds_no_governed_evidence_artifact` measures.

**The catalog was re-pinned three times in this leaf, once per case module, and the constant's docstring
records all three newest-first** — the Twentieth at `:49-66`, the Nineteenth at `:68-85` and the
Eighteenth at `:87-106` — each naming the module, the two consumer rows, the census finding it was
derived from, the counts that did not move and the digest it replaced. The pin chain is
`8d60a34c…` (L9's Seventeenth) → `c676b0a0…` (Eighteenth) → `b1ed7838…` (Nineteenth) → `d2d6dc6a…`
(Twentieth, measured with `sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate); the
catalog holds 1689 lines and the lane manifest 341. The docstring's own 60 new lines are why every
construct below `:48` reads lower on this candidate, and every range this card carried for them was
re-derived rather than shifted.

- **The re-pinned constants, with the counts this leaf did not move and the digest it did (`8d60a34c…` → `c676b0a0…` → `b1ed7838…` → `d2d6dc6a…`).** [64]
- **The source's own paragraph for the third case module: no registration, two consumer rows, counts unchanged, and the digest it replaced.** [65]
- **The source's own paragraph for the reach case module.** [66]
- **The source's own paragraph for the movement case module, and the census finding (`missing=[…]`, `unsupported=[]`) each row was derived from.** [67]
- **The six consumer entries this leaf's three modules joined: three on each of the two exact-scope consumer rows.** [68]
- The existing unit-regression registry contains the three relationship modules. [69]
- The check that recomputes the catalog's sha256 and counts both block kinds beside it, re-derived because the docstring's three new paragraphs moved it. [70]
- The proof that this leaf's artifact delta is empty, which is why only a consumer change could move the digest three times. [71]

## 260921-ICR-L10 The Twenty-First Deliberate Re-Pin, With The Population Unchanged

`260921-ICR-L10` (`ICR-R10@v1`) re-pins `LIFECYCLE_CATALOG_SHA256` for the third time in this
series' recent leaves: the new pagination module obliged **three** exact-scope consumer rows in
`mcp/tests/evidence-lifecycle.toml`, and a governed manifest's bytes are what this digest pins. The pin
moves from `d2d6dc6a…` to `b4d4a7f9…`, and the two counts beside it are **unchanged** at sixteen
contracts and sixty-six artifacts — the re-pin records an amended row, not a new contract.

The census this module runs is what confirms it: the module registers no contract, no artifact and no new
support module, so the only obligation it created was the consumer rows, and the paragraph that carries
this leaf's account is the twenty-first in the deliberate-re-pin sequence.

## 260921-ICR-L26 The Twenty-Second Deliberate Re-Pin, With The Population Unchanged

`260921-ICR-L26` (`ICR-R26@v1`) registers **no** artifact and **no** contract of its own: its thirteen
subject-and-comparison-isolation cases live in the ordinary unit module
`mcp/tests/test_knowledge_review_subject_isolation.py`, which is a source-derived consumer of **four**
rows — every one of them derived from the census's own finding
(`missing=['mcp/tests/test_knowledge_review_subject_isolation.py']` with `unsupported=[]` on all four):
`mcp/tests/curator_coherence_test_support.py` (the recorded task topology the publication binds),
`mcp/tests/fixtures/repository_profiles/node/package-lock.json`,
`mcp/tests/diff_scope_test_support.py` (the two snapshots, their recorded identities and the two real
trees the enclosure is built over) and `mcp/tests/read_scope_test_support.py` (the authorship envelope
and the recorded family/membership topology the classification's recorded relationships are read from).
All four `consumer_scope = "exact"` rows gained that one path each, and the module's own lane row was
added to `mcp/tests/test-evidence-lanes.toml`, which pins no digest and refuses an unregistered module
at collection.

**Nothing was registered, no row was removed and no artifact's identity moved**, so the population stays
at **sixteen contracts / sixty-six artifacts**, and the catalog is re-pinned from
`b4d4a7f9e9500ba10f763dacdc916c0b77054113fc388f3096869fbedeef92cd` (the Twenty-first) to
`4d874fb54c627549db098177caa477040e09ca63c7ae2cba2246bd1390a338e0`. The proof's own artifact delta
remains exactly empty, and `LIFECYCLE_CONTRACT_COUNT`/`LIFECYCLE_ARTIFACT_COUNT` are deliberately **not**
touched: a re-pin that moved neither count is the evidence that the case module was registered as a
consumer rather than promoted into the lifecycle as an artifact.

## 260921-ICR-L12 The Twenty-Third Deliberate Re-Pin

`260921-ICR-L12` (`ICR-R12@v1`) re-pins the lifecycle catalog a **twenty-third** time, and the
re-pin is the whole of this module's change: `LIFECYCLE_CATALOG_SHA256` moves from
`4d874fb54c627549db098177caa477040e09ca63c7ae2cba2246bd1390a338e0` (the Twenty-second, `260921-ICR-L26`)
to `4ab067e360c7807c3051ad71058c09058225f1e9155e7111da6e95c73cac0258`, measured with `sha256sum
mcp/tests/evidence-lifecycle.toml` on the resolved candidate.

**What the new digest is of, and what did not change.** The leaf registers no artifact and no contract
of its own: its eight committed-leaf cases live in the ordinary unit module
`mcp/tests/test_historical_committed_leaf_review.py`, which builds on the existing R01 enclosure
fixture rather than introducing a second enclosure or a second support module. It is therefore a
source-derived consumer of **three** rows — `mcp/tests/diff_scope_test_support.py` (the two snapshots
and the two real trees the enclosure is built over), `mcp/tests/read_scope_test_support.py` (the
repository, the recorded anchors and the tracked paths) and the Node `package-lock.json` fixture the
census's own propagation rule reaches through those rows — and all three `consumer_scope = "exact"`
rows gained that one path each, together with the module's own lane row in
`mcp/tests/test-evidence-lanes.toml`. The population stays at **sixteen contracts / sixty-six
artifacts**, no row was removed, and the proof's own artifact delta remains exactly empty. The
docstring's census finding is the evidence: `missing=['mcp/tests/test_historical_committed_leaf_review.py']`
with `unsupported=[]` on exactly those three rows.

## 260921-ICR-L22 The Twenty-Fourth Deliberate Re-Pin — The Managed-Sync Case Module's Three Newly Reached Rows

`260921-ICR-L22` (`ICR-R22@v1`, the managed Git recovery rebinding requirement) re-pins the
lifecycle catalog on its own account as the **twenty-fourth** deliberate re-pin:
`LIFECYCLE_CATALOG_SHA256` moves from
`81a518b567b654375bd1ea4e5af5395cefe3a3464563308c17f31278e276134c` — the value the constant carries at
this leaf's base `e605822e`, read from the constant itself — to
`8ce61c57b8660011b1cb81f0c2f21bd493ce3e2295359228d8804f0b8192b9d1`, measured with ``sha256sum
mcp/tests/evidence-lifecycle.toml`` on the resolved candidate.

The leaf registers no artifact and no contract of its own: its four managed-sync rebinding cases live in
the module the packet's own anchor names, ``mcp/tests/test_worktree_sync.py``, which already owns the
managed merge/conflict production-operation evidence. What moved is that module's **consumer closure**:
the new cases build the leaf enclosure the review leaves use, so the module now imports the shared
endpoint fixture and the authorship envelope, and the census derives three further consumers from that —
``mcp/tests/fixtures/repository_profiles/node/package-lock.json``,
``mcp/tests/diff_scope_test_support.py`` and ``mcp/tests/read_scope_test_support.py`` — each reporting
``missing=['mcp/tests/test_sync_parked_candidate.py', 'mcp/tests/test_worktree_sync.py']`` with
``unsupported=[]``. ``mcp/tests/test_sync_parked_candidate.py`` reaches the same rows transitively because
it already imports ``SyncFixture`` from the case module, which is a fact of the existing tree rather than
of this leaf. All three ``consumer_scope = "exact"`` rows gained those two paths, in the position each row
already lists the sibling case modules. **Nothing was registered, no row was removed, no artifact's
identity moved and no lane row changed**, so the population stays at **sixteen contracts / sixty-six
artifacts**, and the proof's own artifact delta remains exactly empty.

**One measurement the next reader needs beside that "from" value.** The docstring's newest entry at this
leaf's base is the **Twenty-third**'s, whose own landed value is
``4ab067e360c7807c3051ad71058c09058225f1e9155e7111da6e95c73cac0258``, while the constant itself carried
``81a518b5…``: commit ``3103e114`` (``260921-ICR-L21``) re-pinned the value for its own consumer rows
without adding an entry to this narrative. The re-pin above is therefore measured from the constant's own
reading rather than from the newest narrative entry, and a reader matching a "from X (the Nth)" sentence
against the chain should expect that one-entry gap at this base.

## 260921-ICR-L22 The Twenty-Fifth Deliberate Re-Pin — The Module Split's Own Closure Change

The leaf's first fix round re-pinned the catalog a **twenty-fifth** time, and the entry is inserted
immediately above the Twenty-fourth's: `LIFECYCLE_CATALOG_SHA256` moves from `8ce61c57…` to
`7c8c1646272ca4a17f87a16ecbe105a4aea558c0e0d0c4d62b1883d6d69e683c`, measured with ``sha256sum
mcp/tests/evidence-lifecycle.toml`` on the resolved candidate.

The F5 ruling moved this leaf's four managed-sync rebinding cases, their fixture and their module-level
helpers out of ``mcp/tests/test_worktree_sync.py`` into a new
``mcp/tests/test_review_sync_rebinding.py``, so the case module that already owned the managed-sync
evidence is back in the soft band and the whole-tree hard-rail census returns to its base count. The
census derived the delta exactly: ``mcp/tests/test_sync_parked_candidate.py`` and
``mcp/tests/test_worktree_sync.py`` are **no longer** consumers of the endpoint and scope support rows
(their only route to them was the case module's own import, which moved), and the new module is a consumer
of four rows — the Node ``package-lock.json`` fixture, ``mcp/tests/merge_case_test_support.py``,
``mcp/tests/diff_scope_test_support.py`` and ``mcp/tests/read_scope_test_support.py`` — reporting
``missing=['mcp/tests/test_review_sync_rebinding.py']`` with
``unsupported=['mcp/tests/test_sync_parked_candidate.py', 'mcp/tests/test_worktree_sync.py']`` on the three
that had carried them. Each row was corrected to exactly the derived set: three lost the two paths,
``mcp/tests/merge_case_test_support.py`` kept both and gained the new one. The new module's lane row was
added to ``mcp/tests/test-evidence-lanes.toml`` in the integration lane beside its sibling. **Nothing was
registered, no row was removed and no artifact's identity moved**, so the population stays at **sixteen
contracts / sixty-six artifacts**, and the proof's own artifact delta remains exactly empty.

## 260921-ICR-L22 The Twenty-Sixth Deliberate Re-Pin — The Read-Side Cases' Own Module

The leaf's third fix round re-pinned the catalog a **twenty-sixth** time, and this is the value the
constant carries on the live candidate: `LIFECYCLE_CATALOG_SHA256` at `:46` reads
`d07c2f9d456b0f658228c91aecb2a1f3da8d13e2b6575b6b40b0b0d2ca165f6b`, measured with ``sha256sum
mcp/tests/evidence-lifecycle.toml`` — 1710 lines — and the value it replaces is `7c8c1646…`, the
Twenty-fifth.

Fix round 3's H1 case pushed ``mcp/tests/test_review_sync_rebinding.py`` to 1263 lines, which would have
made it a **new** offender in the whole-tree ≥1200 census (26 → 27) — the exact condition this master's
ruling refuses. The fix is extraction at the seam the production owners already have: the five *read-side*
cases (what the shipped ``read_knowledge_review`` renders about a sync that moved its inputs, plus the
movement validator's own refusals) moved into a new ``mcp/tests/test_review_sync_movement_read.py`` (356
lines), which imports the enclosure fixture from its sibling (now 942 lines) rather than duplicating it.
The census derived the delta exactly: the new module is a consumer of the same four rows, each reporting
``missing=['mcp/tests/test_review_sync_movement_read.py']`` with ``unsupported=[]``, so each gained that
one path, and its lane row was added to ``mcp/tests/test-evidence-lanes.toml`` in the integration lane
beside its sibling. **Nothing was registered, no row was removed and no artifact's identity moved**, so
the population stays at **sixteen contracts / sixty-six artifacts**, ``LIFECYCLE_CONTRACT_COUNT`` and
``LIFECYCLE_ARTIFACT_COUNT`` are deliberately **not** touched, and the artifact delta remains exactly
empty.

**What the three entries did to this module's own lines.** They are inserted in the constant's docstring
at `:49`, `:67` and `:88`, so the module's size moves **782 → 842 lines** and **every line from the base's
`:49` onward reads 60 lines lower**: `test_repository_inputs_reach_their_supported_consumers` `:633` →
`:693`, `_assert_the_proof_is_selected_by_the_lane_manifest` `:690` → `:750`,
`_assert_the_governed_inventory_is_closed` `:703` → `:763`, and
`_assert_the_catalog_kept_its_bytes_and_identities` `:723` → `:783`. The three constants' own lines are
unchanged (`:43-46`), the constants still read **16 / 66**, and every range on this card that cites a line
below the docstring was left for the curator's separate per-row repair rather than shifted by a
remembered delta.

## 260921-ICR-L31 The Twenty-Seventh And Twenty-Eighth Re-Pins, And The Catalog Pin They Move

**``LIFECYCLE_CATALOG_SHA256`` now names ``23dd7c0f85b50585e8968122f60f50e87e15bfbfa241b28b77b7c71b2a41e252``
(`ICR-R31@v1`).** The constant is re-pinned deliberately at every value below, and this leaf moved it
twice for the two reasons the module's own docstring records in full: the Twenty-seventh re-pin
followed ``mcp/tests/test_review_family_context.py`` becoming a source-derived consumer of the
``diff_scope_test_support`` and ``read_scope_test_support`` rows, and the Twenty-eighth followed fix
round 1's new ``mcp/tests/test_review_family_context_population.py`` joining those same two rows. The
leaf registered no artifact and no contract of its own, so ``LIFECYCLE_CONTRACT_COUNT`` stays **16** and
``LIFECYCLE_ARTIFACT_COUNT`` stays **66**, and the proof's own artifact delta remains exactly empty.

**What a reader should take from this card.** The pin is an assertion about bytes: the proof compares
``sha256sum mcp/tests/evidence-lifecycle.toml`` against this constant, so a consumer row added anywhere
in that file fails the proof until the constant is re-pinned here — which is why the re-pin is
deliberate and recorded rather than mechanical. The docstring below the constant is the authority for
every re-pin's reason; this section records only that two more happened and that neither moved the
population.

**Citation accounting:** six rows of this card were re-anchored. The prose anchors here quote passages
of this module's *own* docstring, so each was resolved to the paragraph it names — the L1 entry, the L18
consequence-repair entry and the L18 entry — and each repaired range was confirmed to hold its quoted
passage on the frozen bytes. Two descending (``start > end``) ranges, which the checker reads as empty,
were replaced by the true range of the passage their row names.

## 260921-ICR-L29 The Twenty-Ninth Deliberate Re-Pin

`ICR-R29@v1` moves `LIFECYCLE_CATALOG_SHA256` (`:46`) from
`97ae9cbefd756a6def6e8048baa2066beef2c06300f73eb93b4ab23b4ebf6879` (the Twenty-eighth re-pin) to
`f3dd258c161eee057edee9bdb7b7a4874220c8a4201c04a516dc146c14526589`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate, and adds the Twenty-ninth
re-pin note to the module's own docstring in the established style.

**The delta it records is exactly one consumer path** — the new `mcp/tests/test_knowledge_bootstrap.py`
added to the `mcp/tests/fixtures/repository_profiles/node/package-lock.json` artifact's consumer list —
so `LIFECYCLE_CONTRACT_COUNT` stays `16` and `LIFECYCLE_ARTIFACT_COUNT` stays `66`. The proof's own
artifact delta remains empty, which is the property this pin exists to assert: a re-pin that ever
accompanied a population change would be the signal that something was registered rather than
discovered.

## 260921-ICR-L57 The Thirty-Second Deliberate Re-Pin, And A Pin That Was Already Stale

`260921-ICR-L57` (the master's exit-gate repair leaf, which owns no ICR requirement) moves
`LIFECYCLE_CATALOG_SHA256` (`:46`) from `49b1e98bdf4adead6a36038ecfb182646ab6de324d0a4e4f3c3ac81a28372e83`
(the Thirty-first re-pin, `260921-ICR-L32`) to
`1c682524157cb12075319069b03410b39053317946a61847c51a603c146a68b2`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate. It adds the Thirty-second note to
the module's docstring in the established style.

**The delta is 29 consumer paths on five exact rows**, described on
[`evidence-lifecycle.toml`](evidence-lifecycle.toml.md): eight landed case modules the census had
derived but no row declared, and the three modules split off across the file-size rail.
`LIFECYCLE_CONTRACT_COUNT` stays `16` and `LIFECYCLE_ARTIFACT_COUNT` stays `66`. The proof's own
artifact delta remains empty.

**The pin was already stale before this leaf, and the gate could not see it.** Three commits added
consumer paths without a re-pin: `55c62237` (L43, one), `9b2f775f` (L44, one) and `eda94732` (L45, two).
They left the catalog at `aaf23d7890387ad6f069a5206c10717091b03360f12928b011dca1b83794459c`. The byte
assertion never ran. In `test_production_proof_adds_no_governed_evidence_artifact`,
`_assert_the_governed_inventory_is_closed` runs before `_assert_the_catalog_kept_its_bytes_and_identities`,
and it failed first (worker report, gate evidence). So one red
case hid a second defect. After a consumer repair, the byte assertion is the next thing to fail.

- The re-pinned constant beside the unchanged counts. [72]
- **The Thirty-second re-pin note: the census-derived paths, the three splits, the earlier unpinned additions and the unchanged populations.** [73]
- The order that masked the stale pin: the inventory-closure assertion runs before the byte assertion. [74]


## 260928-MIK-L24 The Thirty-Third Deliberate Re-Pin — Fourteen New Rows, Counts 16 / 80

`260928-MIK-L24` (MIK-R24, conversion and boundary crossing) moves `LIFECYCLE_ARTIFACT_COUNT` (`:45`)
from `66` to **`80`** and `LIFECYCLE_CATALOG_SHA256` (`:46`) from
`1c682524157cb12075319069b03410b39053317946a61847c51a603c146a68b2` (the Thirty-second) to
`6fb4934d9120e1f593aaaa0e5534f49e01bf88a0f4dee04592f75063575fab65`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml`. `LIFECYCLE_CONTRACT_COUNT` stays `16`. It adds the
"Thirty-third deliberate re-pin" paragraph at the top of the module docstring's re-pin log.

**This lane was already red on the leaf's base, and the architect ruled that L24 repairs it.** The
L20–L23 leaves (and L12 and L21) had landed shared test support and fixtures without catalog rows, so
`test_repository_inputs_reach_their_supported_consumers` and
`test_production_proof_adds_no_governed_evidence_artifact` failed on `cd3e943d`. The catalog change is
**insertion-only** (+321/−0), described on [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md):

- **fourteen new `[[artifact]]` rows:** the five `shared-support` modules
  `knowledge_validator_test_support.py` (`260928-MIK-L22`), `knowledge_index_test_support.py` (`260928-MIK-L23`),
  `knowledge_writer_test_support.py` (`260928-MIK-L12`), `knowledge_census_test_support.py` (`260928-MIK-L20`) and
  `knowledge_conversion_test_support.py` (`260928-MIK-L24`), plus the nine `fixture` files
  `mcp/tests/fixtures/knowledge_files/*.json` (`260928-MIK-L21`). Each has its source-derived consumers and a
  `node:` replacement in a real consumer;
- **five existing rows gain consumers, appended without re-sorting:** `curator_coherence_test_support.py`
  (1), `fixtures/repository_profiles/node/package-lock.json` (9), `merge_case_test_support.py` (2),
  `generation_test_support.py` (2) and `read_scope_test_support.py` (1).

No row, consumer or field was removed or changed, and the proof's own artifact delta remains empty. The
reviewer confirmed that the diff is purely additive and that the integration lane passes (447 passed,
15 skipped).

**Known follow-up (review R1 finding 12; done by `260928-MIK-L28`, see the next section):** the parallel leaf L28's `test_knowledge_proofs.py` imports
`knowledge_index_test_support` and `knowledge_writer_test_support`, which are now `consumer_scope = "exact"`
rows. So once L24 lands, L28 must add itself to those two consumer lists and re-pin again.

- The re-pinned count and digest, beside the unchanged contract count. [75]
- **The Thirty-third re-pin note: the base was already red, fourteen new rows, five consumer additions, nothing removed, 16 / 80.** [76]

## 260928-MIK-L28 The Thirty-Fourth Deliberate Re-Pin — One Consumer On Three Rows, Counts 16 / 80

`260928-MIK-L28` (MIK-R28, first-class test proofs) moves `LIFECYCLE_CATALOG_SHA256` (`:46`) from
`6fb4934d9120e1f593aaaa0e5534f49e01bf88a0f4dee04592f75063575fab65` (the Thirty-third) to
`b96198c3b59d0a7909dccd3dca389b8af93182d51c9886d0b2b9cb02ed5c64c9`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml`. `LIFECYCLE_CONTRACT_COUNT` stays `16` and
`LIFECYCLE_ARTIFACT_COUNT` stays `80`. It adds the "Thirty-fourth deliberate re-pin" paragraph at the top of
the module docstring's re-pin log.

This is the follow-up L24 recorded above. The new case module `mcp/tests/test_knowledge_proofs.py` imports
`knowledge_index_test_support.py` and `knowledge_writer_test_support.py`, and the census's source
derivation also assigns it `fixtures/repository_profiles/node/package-lock.json`. Each of those three
`consumer_scope = "exact"` rows gains the one consumer, appended without re-sorting (described on
[`evidence-lifecycle.toml`](evidence-lifecycle.toml.md)). No row was added or removed, no consumer removed
and no other field changed; the proof's own artifact delta remains empty. The worker ran the integration
lane of this module: 2 passed.

- The re-pinned digest beside the two unchanged counts. [77]
- **The Thirty-fourth re-pin note: the new case module on three exact rows, nothing else changed, 16 / 80.** [78]

## 260928-MIK-L08 The Thirty-Fifth Deliberate Re-Pin — One Consumer On One Row, Counts 16 / 80

`260928-MIK-L08` (MIK-R08, the change-to-knowledge worklist) moves `LIFECYCLE_CATALOG_SHA256` (`:46`) from
`b96198c3b59d0a7909dccd3dca389b8af93182d51c9886d0b2b9cb02ed5c64c9` (the Thirty-fourth) to
`11ce80899b5a38e4b5fe73691a1cfa4dee076161a2554c21d15b0f2b31c18a51`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml`. `LIFECYCLE_CONTRACT_COUNT` stays `16` and
`LIFECYCLE_ARTIFACT_COUNT` stays `80`. It adds the "Thirty-fifth deliberate re-pin" paragraph at the top of
the module docstring's re-pin log, above L28's Thirty-fourth.

The new case module `mcp/tests/test_knowledge_worklist_leaf.py` drives the memory-quality controller, so the
census derives it as a consumer of `fixtures/repository_profiles/node/package-lock.json`; that one
`consumer_scope = "exact"` row gains the path, appended after L28's `test_knowledge_proofs.py` without
re-sorting (described on [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md)). No row was added or
removed and no other field changed; the proof's own artifact delta remains empty. The worker renumbered
this paragraph from Thirty-fourth to Thirty-fifth when the leaf was synced onto L28, and the reviewer
confirmed the pin equals `sha256sum` of the catalog (integration lane: 2 passed).

- The re-pinned digest beside the two unchanged counts. [79]
- **The Thirty-fifth re-pin note: the worklist leaf case module on one exact row, nothing else changed, 16 / 80.** [80]


## 260928-MIK-L03 The Thirty-Sixth Deliberate Re-Pin — One Consumer On One Row, Counts 16 / 80

`260928-MIK-L03` (MIK-R03, stale invariants flagged at read time) moves `LIFECYCLE_CATALOG_SHA256` (`:46`)
from `11ce80899b5a38e4b5fe73691a1cfa4dee076161a2554c21d15b0f2b31c18a51` (the Thirty-fifth) to
`dcc1ab1dd89330fa429608a4483183fa10e755690e6cdc6071f71ddc27dbd53c`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml`. `LIFECYCLE_CONTRACT_COUNT` stays `16` and
`LIFECYCLE_ARTIFACT_COUNT` stays `80`. It adds the "Thirty-sixth deliberate re-pin" paragraph at the top of
the module docstring's re-pin log, above L08's Thirty-fifth.

The new case module `mcp/tests/test_knowledge_currentness.py` transitively consumes
`fixtures/repository_profiles/node/package-lock.json`, so that one `consumer_scope = "exact"` row gains the
path, appended after L08's `test_knowledge_worklist_leaf.py` without re-sorting (described on
[`evidence-lifecycle.toml`](evidence-lifecycle.toml.md)). No row was added or removed and no other field
changed; the proof's own artifact delta remains empty. The integration lane passed after the re-pin (447
passed, 15 skipped), and review round 2 reran it.

- The re-pinned digest beside the two unchanged counts. [81]
- **The Thirty-sixth re-pin note: the currentness case module on one exact row, nothing else changed, 16 / 80.** [82]

## 260928-MIK-L02 The Thirty-Seventh Deliberate Re-Pin — One Consumer On Two Rows, Counts 16 / 80

`260928-MIK-L02` (MIK-R02, bounded continuation accepted by the mounted read) moves `LIFECYCLE_CATALOG_SHA256`
(`:46`) from `dcc1ab1dd89330fa429608a4483183fa10e755690e6cdc6071f71ddc27dbd53c` (L03's Thirty-sixth) to
`5c0a15941c93d17a808263a9250afb7074d76ef7014ada0114b2780d6eea2fe5`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the synced tree. `LIFECYCLE_CONTRACT_COUNT` stays `16` and
`LIFECYCLE_ARTIFACT_COUNT` stays `80`. It adds the "Thirty-seventh deliberate re-pin" paragraph at the top of
the module docstring's re-pin log, above L03's Thirty-sixth, which is kept as it was.

- **The ordinal.** The worker first wrote the paragraph as a provisional "Thirty-sixth", because L03 held that
  ordinal in parallel; at the sync onto L03 it became the Thirty-seventh and the digest was re-measured
  (architect ruling of 2026-09-29 20:40:40). Review round 2 confirmed the pin holds on `a4eba7b7`, with L30
  in.
- The new case module `mcp/tests/test_knowledge_paging.py` transitively consumes
  `fixtures/repository_profiles/node/package-lock.json` and imports `knowledge_index_test_support.py`, so both
  `consumer_scope = "exact"` rows gain the path, each appended without re-sorting (described on
  [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md)). No row was added or removed and no other field
  changed; the proof's own artifact delta remains empty. The integration lane passed after the re-pin (447
  passed, 15 skipped).

- The Thirty-seventh digest beside the two unchanged counts. [83]
- **The Thirty-seventh re-pin note: the paging case module on two exact rows, nothing else changed, 16 / 80.** [84]

## 260928-MIK-L11 The Thirty-Eighth Deliberate Re-Pin — One Consumer On One Row, Counts 16 / 80

`260928-MIK-L11` (MIK-R11, planned invariant effects reconciliation) moves `LIFECYCLE_CATALOG_SHA256`
(`:46`) from `5c0a15941c93d17a808263a9250afb7074d76ef7014ada0114b2780d6eea2fe5` (L02's Thirty-seventh) to
`cb853f727a557d39a5cd96161aac46cbcda6b63cc11b8fef7d2f293906921583`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the tree synced onto `2c6f170e`. `LIFECYCLE_CONTRACT_COUNT`
stays `16` and `LIFECYCLE_ARTIFACT_COUNT` stays `80`. It adds the "Thirty-eighth deliberate re-pin"
paragraph at the top of the module docstring's re-pin log, above L02's Thirty-seventh, which is kept as it
was.

- **The ordinal.** The worker first wrote the paragraph as a provisional "Thirty-eighth" at `94c8f252…` on
  base `a4eba7b7`, because L02 held the Thirty-seventh in parallel; at the sync onto L02 (`2c6f170e`) the
  catalog conflict was resolved by keeping L02's consumer line and appending this leaf's after it, and the
  digest was re-measured (architect ruling of 2026-09-29T22:35:34+02:00). Review round 2 confirmed the pin
  on the staged blob and the working file.
- The new case module `mcp/tests/test_planned_knowledge_effects.py` transitively consumes
  `fixtures/repository_profiles/node/package-lock.json`, so that `consumer_scope = "exact"` row gains the
  path, appended without re-sorting (described on [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md)).
  No row was added or removed and no other field changed; the proof's own artifact delta remains empty. The
  integration lane passed after the re-pin (447 passed, 15 skipped).

- The Thirty-eighth digest beside the two unchanged counts. [85]
- **The Thirty-eighth re-pin note: the planned-effects case module on one exact row, nothing else changed, 16 / 80.** [86]

## 260928-MIK-L01 The Thirty-Ninth Deliberate Re-Pin — One Consumer On Two Rows, Counts 16 / 80

`260928-MIK-L01` (MIK-R01, family-complete leaf read) moves `LIFECYCLE_CATALOG_SHA256` (`:46`) from
`cb853f727a557d39a5cd96161aac46cbcda6b63cc11b8fef7d2f293906921583` (L11's Thirty-eighth) to
`a571a70fe261116a14251daa9cea3fd5c47c08a2b0e478c27d28caf98385cc30`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the tree synced onto L11 (`46ca7430`).
`LIFECYCLE_CONTRACT_COUNT` stays `16` and `LIFECYCLE_ARTIFACT_COUNT` stays `80`. It adds the "Thirty-ninth
deliberate re-pin" paragraph at the top of the module docstring's re-pin log, above L11's Thirty-eighth,
which is kept as it was.

- **The ordinal.** The worker first wrote the paragraph as a provisional "Thirty-ninth" on base `2c6f170e`,
  because L02 held the Thirty-seventh and L11 a provisional Thirty-eighth; at the sync onto L11 the catalog
  conflict was resolved by keeping L11's consumer line and appending this leaf's after it, and the digest was
  re-measured (architect ruling of 2026-09-30 00:08:39). The later syncs onto L27 and L06 (base `7127756c`)
  did not touch the catalog, so the pin stands.
- The new case module `mcp/tests/test_knowledge_leaf_read.py` imports `knowledge_index_test_support.py` and
  through it consumes `fixtures/repository_profiles/node/package-lock.json`, so each of those two
  `consumer_scope = "exact"` rows gains the path, appended without re-sorting (described on
  [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md)). No row was added or removed and no other field
  changed; the proof's own artifact delta remains empty. The integration lane passed after the re-pin (447
  passed, 15 skipped).

- The Thirty-ninth digest beside the two unchanged counts. [87]
- **The Thirty-ninth re-pin note: the leaf-read case module on two exact rows, nothing else changed, 16 / 80.** [88]

## 260928-MIK-L10 The Fortieth Deliberate Re-Pin — One Consumer On One Row, Counts 16 / 80

`260928-MIK-L10` (MIK-R10, unexplained change disposition) moves `LIFECYCLE_CATALOG_SHA256` (`:46`) from
`a571a70fe261116a14251daa9cea3fd5c47c08a2b0e478c27d28caf98385cc30` (L01's Thirty-ninth) to
`449b69efb61498ac2e81d888c9891be3a7227562d267f1d184aea70104b7d254`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the tree synced onto L01 (`3772cdcd`) and unchanged by the
later sync onto L25 (`8a2d4b47`). `LIFECYCLE_CONTRACT_COUNT` stays `16` and `LIFECYCLE_ARTIFACT_COUNT` stays
`80`. It adds the "Fortieth deliberate re-pin" paragraph at the top of the module docstring's re-pin log,
above L01's Thirty-ninth, which is kept as it was.

- **The ordinal.** The worker first wrote the paragraph as a provisional "Fortieth" on base `c493b557`,
  because L01 held the Thirty-ninth; at the sync onto L01 only the two catalog files conflicted, this leaf's
  consumer line was appended after L01's `test_knowledge_leaf_read.py`, and the digest was re-measured.
- The new case module `mcp/tests/test_unexplained_change_disposition.py` consumes
  `fixtures/repository_profiles/node/package-lock.json` transitively (the census derives it), so that
  `consumer_scope = "exact"` row gains the path, appended without re-sorting (described on
  [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md)). No row was added or removed and no other field
  changed; the proof's own artifact delta remains empty. The integration lane passed after the re-pin (447
  passed, 15 skipped; reviewer R1 and R2).
- **For L05:** its provisional Forty-first re-pin must be re-measured after this leaf lands (reviewer R1).

- The Fortieth digest beside the two unchanged counts. [89]
- **The Fortieth re-pin note: the unexplained-change case module on one exact row, nothing else changed, 16 / 80.** [90]
- The consumer line the census derived. [91]

## 260928-MIK-L05 The Forty-First Deliberate Re-Pin — One Consumer On Four Rows, Counts 16 / 80

`260928-MIK-L05` (MIK-R05, route-chain family retrieval) moves `LIFECYCLE_CATALOG_SHA256` (`:46`) from
`449b69efb61498ac2e81d888c9891be3a7227562d267f1d184aea70104b7d254` (L10's Fortieth) to
`f8b048143a4072e35d3a65e9fcce16cd7bfd9ca6a2f253272ae251ea912f212b`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the tree synced onto base `31d761a2` (L13, L25 and L10
landed); the curator re-measured the same digest on the candidate. `LIFECYCLE_CONTRACT_COUNT` stays `16` and
`LIFECYCLE_ARTIFACT_COUNT` stays `80`. It adds the "Forty-first deliberate re-pin" paragraph at the top of the
module docstring's re-pin log, above L10's Fortieth, which is kept as it was.

- **The ordinal.** The worker first wrote the paragraph as a provisional "Forty-first" (`3cee6014…`) on base
  `3772cdcd`, because L10 held the Fortieth; review R1 F5 and the ruling of 2026-09-30 04:12:49 kept both
  consumer lines at the conflicting `evidence-lifecycle.toml` row and asked for a re-measure after L10 landed.
  At the sync onto `31d761a2` the architect resolved the conflict (L05's line after L10's
  `test_unexplained_change_disposition.py` on the package-lock row) and the pin became the final Forty-first.
- The new case module `mcp/tests/test_knowledge_route_chain.py` imports the leaf-read case module (so
  transitively `knowledge_index_test_support.py` and `fixtures/repository_profiles/node/package-lock.json`) and
  the `read_ar_files` case module (so transitively `read_scope_test_support.py` and
  `curator_coherence_test_support.py`); each of those four `consumer_scope = "exact"` rows gains the path,
  appended without re-sorting (described on [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md)). No row
  was added or removed and no other field changed; the proof's own artifact delta remains empty. The
  integration lane passed after the re-pin (447 passed, 15 skipped, `full-integration-r4.txt`).

- The two unchanged counts beside the pin line, which since `260928-MIK-L14` holds the Forty-second digest (see that section's row). [92]
- **The Forty-first re-pin note: the route-chain case module on four exact rows, nothing else changed, 16 / 80.** [93]
- The consumer lines the census derived. [94]

## 260928-MIK-L14 The Forty-Second Deliberate Re-Pin — One Consumer On One Row, Counts 16 / 80

`260928-MIK-L14` (MIK-R14, reconsideration surfacing) moves `LIFECYCLE_CATALOG_SHA256` (`:46`) from
`f8b048143a4072e35d3a65e9fcce16cd7bfd9ca6a2f253272ae251ea912f212b` (L05's Forty-first) to
`4477446eb501ccc6e4c76e627f893c11d08edc313dc92fb399dc1d5e13316d10`, measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the tree synced onto base `48f680d5`, after L05 landed, and
unchanged by the sync onto L31's base `b54d1b03`; the curator re-measured the same digest on the candidate (2,096 lines).
`LIFECYCLE_CONTRACT_COUNT` stays `16` and `LIFECYCLE_ARTIFACT_COUNT` stays `80`. It adds the "Forty-second
deliberate re-pin" paragraph at the top of the module docstring's re-pin log, above L05's Forty-first, which is
only re-wrapped (its word sequence is identical, review R3).

- **The ordinal.** The worker first wrote a provisional "Forty-first" (`ad4e9fa1…`) on base `3eb034a6`, then a
  provisional "Forty-second" (`6dc45062…`) at the sync onto `31d761a2` (L10 held the Fortieth and L05 the
  Forty-first). At the sync onto `48f680d5` the pin became the final Forty-second (`4477446e…`), verified by
  reviews R3 to R6.
- The new case module `mcp/tests/test_reconsideration_surfacing.py` reuses MIK-R08's worklist world, so it
  transitively consumes `fixtures/repository_profiles/node/package-lock.json`; that `consumer_scope = "exact"` row
  gains the path, appended after L05's `test_knowledge_route_chain.py` without re-sorting (described on
  [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md)). No row was added or removed and no other field
  changed; the proof's own artifact delta remains empty. The integration lane passed after the re-pin (447 passed,
  15 skipped, at every round through R6).

- The Forty-second digest beside the two unchanged counts. [95]
- **The Forty-second re-pin note: the reconsideration case module on one exact row, nothing else changed, 16 / 80.** [96]
- The consumer line the census derived. [97]
