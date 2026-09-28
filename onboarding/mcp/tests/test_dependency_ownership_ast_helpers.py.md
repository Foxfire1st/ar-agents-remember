# mcp/tests/test_dependency_ownership_ast_helpers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dependency_ownership_ast_helpers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:43:38+00:00 |
| lastVerifiedCommitHash | `69883386d36d7cdb7faeed5bdf275ddd66d87aea` |
| lastVerifiedCommitDate | 2026-09-28T23:28:51+02:00|
| governingOverview | `overview.md` |
## Governing Overview

[Test suite overview](overview.md)

## Purpose

Repository-input ownership discovery without broadening test selection; and the `LOCR-R26@v1` catalog
guard — the retained headless production-chain proof is ordinary `test_` source, adds no governed
evidence artifact, and leaves the catalog closed over the governed inventory.

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
is a **hard failure** rather than a silent inventory drift. **The current value is the three constants' own
reading on this candidate and nothing else: `LIFECYCLE_CONTRACT_COUNT = 16`,
`LIFECYCLE_ARTIFACT_COUNT = 66` and `LIFECYCLE_CATALOG_SHA256` pinned to
`d07c2f9d456b0f658228c91aecb2a1f3da8d13e2b6575b6b40b0b0d2ca165f6b`, which `sha256sum
mcp/tests/evidence-lifecycle.toml` reproduces on this candidate (1710 lines)** — **a live pair corrected
here rather than carried:** this sentence named
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

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository inputs reach their supported consumers. | `test_repository_inputs_reach_their_supported_consumers` |mcp/tests/test_dependency_ownership_ast_helpers.py:795-815|
| **The evidence catalog's pinned shape and bytes, and the deliberate re-pin this leaf made in the same change as its consumer rows — whose value at this candidate is **16 contracts / 66 artifacts** and `8d60a34cf56a9740e234823658312c8b6f5ae4e958344fe8ba2ea152b8ff6891`, the `260921-ICR-L9` measurement (the card's previous wording named `53ba6331…`, the `260921-ICR-L6` measurement, which was already stale at the landed base and is corrected rather than carried).** | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| **The check that makes the pin real: the file's bytes recomputed and both block kinds counted before either is compared.** | `_assert_the_catalog_kept_its_bytes_and_identities` |mcp/tests/test_dependency_ownership_ast_helpers.py:886-902|
| **The check that makes the pin real: the file's bytes recomputed and both block kinds counted before either is compared.** | `_assert_the_catalog_kept_its_bytes_and_identities` |mcp/tests/test_dependency_ownership_ast_helpers.py:886-902|
| The closure check over the governed inventory, and the lane-membership check. | `_assert_the_governed_inventory_is_closed`; `_assert_the_proof_is_selected_by_the_lane_manifest` |mcp/tests/test_dependency_ownership_ast_helpers.py:780-797; mcp/tests/test_dependency_ownership_ast_helpers.py:767-777; mcp/tests/test_dependency_ownership_ast_helpers.py:806-806; mcp/tests/test_dependency_ownership_ast_helpers.py:838-838; mcp/tests/test_dependency_ownership_ast_helpers.py:805-805; mcp/tests/test_dependency_ownership_ast_helpers.py:825-825; mcp/tests/test_dependency_ownership_ast_helpers.py:866-883; mcp/tests/test_dependency_ownership_ast_helpers.py:853-863 |
| **The contract and artifact blocks the pin counts, added by this leaf, and the consumer list its sibling artifact gained.** | "mcp/tests/diff_scope_test_support.py" | mcp/tests/evidence-lifecycle.toml:54-57; mcp/tests/evidence-lifecycle.toml:1394-1417 |
| **The contract and artifact blocks the pin counts, added by this leaf, and the consumer list its sibling artifact gained.** | "mcp/tests/diff_scope_test_support.py" | mcp/tests/evidence-lifecycle.toml:54-57; mcp/tests/evidence-lifecycle.toml:1394-1417 |
| The catalog pin constants, and the re-pin narrative the docstring carries beside them — **whose newest paragraph is now `260921-ICR-L14`'s `Sixteenth deliberate re-pin` (the synced union onto `260921-ICR-L3`'s fifteenth), and whose extent is the whole docstring.** | `LIFECYCLE_SCHEMA`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-43; mcp/tests/test_dependency_ownership_ast_helpers.py:44-44; mcp/tests/test_dependency_ownership_ast_helpers.py:45-45; mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:47-495; mcp/tests/test_dependency_ownership_ast_helpers.py:440-440; mcp/tests/test_dependency_ownership_ast_helpers.py:479-479; mcp/tests/test_dependency_ownership_ast_helpers.py:385-385; mcp/tests/test_dependency_ownership_ast_helpers.py:423-423 |
| The three consumer entries the `260915-CAPS-L17` re-pin added to three governed-artifact rows, the entire reason the digest moved at that re-pin. | "mcp/tests/fixtures/repository_profiles/node/package-lock.json"; "mcp/tests/eve_capsule_test_support.py"; "mcp/tests/eve_adapter_test_support.py" | mcp/tests/evidence-lifecycle.toml:670-671; mcp/tests/evidence-lifecycle.toml:1509-1530; mcp/tests/evidence-lifecycle.toml:1531-1550 |
| The three consumer entries the `260915-CAPS-L17` re-pin added to three governed-artifact rows, the entire reason the digest moved at that re-pin. | "mcp/tests/fixtures/repository_profiles/node/package-lock.json"; "mcp/tests/eve_capsule_test_support.py"; "mcp/tests/eve_adapter_test_support.py" | mcp/tests/evidence-lifecycle.toml:670-671; mcp/tests/evidence-lifecycle.toml:1509-1530; mcp/tests/evidence-lifecycle.toml:1531-1550 |
| The three artifacts those rows belong to, each an already-governed row rather than a new registration. | "mcp/tests/diff_scope_test_support.py"; "mcp/tests/read_scope_test_support.py" | mcp/tests/evidence-lifecycle.toml:604-604; mcp/tests/evidence-lifecycle.toml:722-722; mcp/tests/evidence-lifecycle.toml:1176-1176; mcp/tests/evidence-lifecycle.toml:75-75; mcp/tests/evidence-lifecycle.toml:61-61; mcp/tests/evidence-lifecycle.toml:66-66 |
| The population the pin names, re-derived at this candidate's own tip — **16 contracts and 66 artifacts**, the values the constants below carry. | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-45 |
| The three consumer entries the `260915-CAPS-L15` re-pin added to three governed-artifact rows, whose shape the `260915-CAPS-L17` entries repeat. | "mcp/tests/curator_coherence_test_support.py"; "mcp/tests/fixtures/repository_profiles/node/package-lock.json"; "mcp/tests/fixtures/codex_app_server_model_page.json" | mcp/tests/evidence-lifecycle.toml:390-390; mcp/tests/evidence-lifecycle.toml:670-671; mcp/tests/evidence-lifecycle.toml:1606-1624 |
| The three consumer entries the `260915-CAPS-L15` re-pin added to three governed-artifact rows, whose shape the `260915-CAPS-L17` entries repeat. | "mcp/tests/curator_coherence_test_support.py"; "mcp/tests/fixtures/repository_profiles/node/package-lock.json"; "mcp/tests/fixtures/codex_app_server_model_page.json" | mcp/tests/evidence-lifecycle.toml:390-390; mcp/tests/evidence-lifecycle.toml:670-671; mcp/tests/evidence-lifecycle.toml:1606-1624 |
| The catalog pin constants, and the re-pin narrative the docstring carries beside them — **whose last paragraph is this leaf's `Thirteenth deliberate re-pin`, and whose extent is now the whole docstring.** | `LIFECYCLE_SCHEMA`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-46; mcp/tests/test_dependency_ownership_ast_helpers.py:49-121 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |
| **The evidence catalog's pinned shape and bytes, the deliberate re-pin this leaf made in the same change as its consumer rows, and the provenance paragraph that records the consumer-only shape of that change.** | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46; mcp/tests/test_dependency_ownership_ast_helpers.py:103-116 |

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
| The appended artifact: the census fixture, with its declared kind, authority, category, fidelity, cadence, introducing leaf, lifetime, replacement contract and exact consumer list. | `"mcp/tests/migration_census_test_support.py"`; `"contract:migration-census-cases"` | mcp/tests/evidence-lifecycle.toml:1646-1662; mcp/tests/evidence-lifecycle.toml:1670-1690 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| **The re-pinned constants, with the counts this leaf did not move and the digest the merged catalog carries.** | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| **The source's own paragraph for this leaf: consumer-only, counts unchanged, and the digest it replaced.** | "260921-ICR-L20"; `LIFECYCLE_CATALOG_SHA256` docstring |mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:333-333; mcp/tests/test_dependency_ownership_ast_helpers.py:430-430; mcp/tests/test_dependency_ownership_ast_helpers.py:451-451; mcp/tests/test_dependency_ownership_ast_helpers.py:440-440; mcp/tests/test_dependency_ownership_ast_helpers.py:479-479; mcp/tests/test_dependency_ownership_ast_helpers.py:385-385; mcp/tests/test_dependency_ownership_ast_helpers.py:423-423 |
| **The source's own paragraph for this leaf: consumer-only, counts unchanged, and the digest it replaced.** | "260921-ICR-L20" |mcp/tests/test_dependency_ownership_ast_helpers.py:479-479|
| The two consumer rows this leaf's module joined, and the lane row the same module occupies. | "mcp/tests/test_knowledge_ingest_publication_route.py" | mcp/tests/evidence-lifecycle.toml:739-741; mcp/tests/evidence-lifecycle.toml:1279-1279; mcp/tests/test-evidence-lanes.toml:91-91; mcp/tests/evidence-lifecycle.toml:1288-1288; mcp/tests/test-evidence-lanes.toml:92-92; mcp/tests/evidence-lifecycle.toml:742-742 |
| The catalog check that recomputes the file's sha256 and counts both block kinds beside it. | `_assert_the_catalog_kept_its_bytes_and_identities` |mcp/tests/test_dependency_ownership_ast_helpers.py:886-902|
| The catalog check that recomputes the file's sha256 and counts both block kinds beside it. | `_assert_the_catalog_kept_its_bytes_and_identities` |mcp/tests/test_dependency_ownership_ast_helpers.py:886-902|
| The leaf's own case module, which is why no third fixture was registered. | `_declared_location`; `_ordinary_enclosure` | mcp/tests/test_knowledge_ingest_publication_route.py:229-237; mcp/tests/test_knowledge_ingest_publication_route.py:118-158 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| **The re-pinned constants, with the counts this leaf did not move and the digest it did.** | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| **The source's own paragraph for that leaf: consumer-only, two support modules, counts unchanged, and the digest it replaced.** | "260921-ICR-L1" | mcp/tests/test_dependency_ownership_ast_helpers.py:406-411; mcp/tests/test_dependency_ownership_ast_helpers.py:178-184; mcp/tests/test_dependency_ownership_ast_helpers.py:129-129; mcp/tests/test_dependency_ownership_ast_helpers.py:130-130; mcp/tests/test_dependency_ownership_ast_helpers.py:170-170; mcp/tests/test_dependency_ownership_ast_helpers.py:171-171; mcp/tests/test_dependency_ownership_ast_helpers.py:206-206; mcp/tests/test_dependency_ownership_ast_helpers.py:207-207; mcp/tests/test_dependency_ownership_ast_helpers.py:222-222; mcp/tests/test_dependency_ownership_ast_helpers.py:238-238; mcp/tests/test_dependency_ownership_ast_helpers.py:185-185; mcp/tests/test_dependency_ownership_ast_helpers.py:233-233; mcp/tests/test_dependency_ownership_ast_helpers.py:212-212 |
| The two appended consumer rows, on the two artifacts whose exact lists gained this module. | "mcp/tests/test_knowledge_review_source_endpoints.py" | mcp/tests/evidence-lifecycle.toml:1405-1441; mcp/tests/evidence-lifecycle.toml:1442-1488 |
| The catalog check that recomputes the file's sha256 and counts both block kinds beside it. | `_assert_the_catalog_kept_its_bytes_and_identities` |mcp/tests/test_dependency_ownership_ast_helpers.py:886-902|
| The catalog check that recomputes the file's sha256 and counts both block kinds beside it. | `_assert_the_catalog_kept_its_bytes_and_identities` |mcp/tests/test_dependency_ownership_ast_helpers.py:886-902|
| The leaf's own case module, which is why no third fixture was registered. | `build_endpoint_fixture` | mcp/tests/test_knowledge_review_source_endpoints.py:220-252 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| **The re-pinned digest and the two counts this leaf did not move.** | "260921-ICR-L18"; `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` |mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:44-44; mcp/tests/test_dependency_ownership_ast_helpers.py:45-45; mcp/tests/test_dependency_ownership_ast_helpers.py:294-294; mcp/tests/test_dependency_ownership_ast_helpers.py:391-405; mcp/tests/test_dependency_ownership_ast_helpers.py:412-412; mcp/tests/test_dependency_ownership_ast_helpers.py:428-428; mcp/tests/test_dependency_ownership_ast_helpers.py:440-440; mcp/tests/test_dependency_ownership_ast_helpers.py:479-479; mcp/tests/test_dependency_ownership_ast_helpers.py:385-385; mcp/tests/test_dependency_ownership_ast_helpers.py:423-423; mcp/tests/evidence-lifecycle.toml:1483-1483 |
| **The source's own paragraph for this leaf: consumer-only, two existing support builders reused, counts unchanged, and the digest it replaced.** | "260921-ICR-L18"; `LIFECYCLE_CATALOG_SHA256` docstring |mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:277; mcp/tests/test_dependency_ownership_ast_helpers.py:390-412; mcp/tests/test_dependency_ownership_ast_helpers.py:428-428; mcp/tests/test_dependency_ownership_ast_helpers.py:440-440; mcp/tests/test_dependency_ownership_ast_helpers.py:479-479; mcp/tests/test_dependency_ownership_ast_helpers.py:385-385; mcp/tests/test_dependency_ownership_ast_helpers.py:423-423; mcp/tests/evidence-lifecycle.toml:1483-1483 |
| The catalog whose bytes the pin names, and the artifact row whose consumer list gained both modules. | "mcp/tests/test_knowledge_ingest_comparison_generation.py"; "mcp/tests/test_knowledge_ingest_failure_windows.py"; "[[artifact]]" | mcp/tests/evidence-lifecycle.toml:732-733; mcp/tests/evidence-lifecycle.toml:1-1686 |
| The proof that this leaf's artifact delta is empty, which is why only a consumer change could move the digest. | `test_production_proof_adds_no_governed_evidence_artifact` |mcp/tests/test_dependency_ownership_ast_helpers.py:818-835|
| The proof that this leaf's artifact delta is empty, which is why only a consumer change could move the digest. | `test_production_proof_adds_no_governed_evidence_artifact` |mcp/tests/test_dependency_ownership_ast_helpers.py:818-835|
| The catalog whose bytes the pin names, and the two `[[artifact]]` blocks whose consumer lists gained both modules. | "mcp/tests/test_knowledge_review_comparison_generation.py" | mcp/tests/evidence-lifecycle.toml:1398-1421; mcp/tests/evidence-lifecycle.toml:1420-1452 |
| The two new modules whose lane rows this leaf added, which is the change the pin follows. | "mcp/tests/test_knowledge_ingest_comparison_generation.py"; "mcp/tests/test_knowledge_ingest_failure_windows.py" | mcp/tests/test-evidence-lanes.toml:98-98; mcp/tests/test-evidence-lanes.toml:99-99 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| **The re-pinned digest, with the two counts this change leaves alone.** | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| **The source's own paragraph for this leaf: the union of two consumer repairs, no registration, counts unchanged, and the digest it replaced. It is no longer first in the docstring — the two later records sit above it.** | "Thirteenth deliberate re-pin (260921-ICR-L6"; `LIFECYCLE_CATALOG_SHA256` |mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:277-277; mcp/tests/test_dependency_ownership_ast_helpers.py:374-374; mcp/tests/test_dependency_ownership_ast_helpers.py:395-395; mcp/tests/test_dependency_ownership_ast_helpers.py:440-440; mcp/tests/test_dependency_ownership_ast_helpers.py:479-479; mcp/tests/test_dependency_ownership_ast_helpers.py:385-385; mcp/tests/test_dependency_ownership_ast_helpers.py:423-423 |
| The catalog check that recomputes the file's sha256 and counts both block kinds beside it — re-derived here because this leaf's row and paragraph moved it. | `_assert_the_catalog_kept_its_bytes_and_identities` |mcp/tests/test_dependency_ownership_ast_helpers.py:886-902|
| The catalog check that recomputes the file's sha256 and counts both block kinds beside it — re-derived here because this leaf's row and paragraph moved it. | `_assert_the_catalog_kept_its_bytes_and_identities` |mcp/tests/test_dependency_ownership_ast_helpers.py:886-902|
| **The row this leaf registered, and L18's landed row immediately beside it, each named exactly once.** | "mcp/tests/test_knowledge_review_one_sided_statements.py"; "mcp/tests/test_read_ar_files.py" | mcp/tests/evidence-lifecycle.toml:1479-1479; mcp/tests/evidence-lifecycle.toml:1480-1481; mcp/tests/evidence-lifecycle.toml:435-435; mcp/tests/evidence-lifecycle.toml:759-759; mcp/tests/evidence-lifecycle.toml:1484-1484 |
| **The row this leaf registered, and L18's landed row immediately beside it, each named exactly once.** | "mcp/tests/test_knowledge_review_one_sided_statements.py"; "mcp/tests/test_read_ar_files.py" | mcp/tests/evidence-lifecycle.toml:1479-1479; mcp/tests/evidence-lifecycle.toml:1480-1481; mcp/tests/evidence-lifecycle.toml:435-435; mcp/tests/evidence-lifecycle.toml:759-759; mcp/tests/evidence-lifecycle.toml:1484-1484 |
| The artifact those two rows belong to, which is already governed and is why no third fixture was registered. | `"mcp/tests/read_scope_test_support.py"`; `consumer_scope` | mcp/tests/evidence-lifecycle.toml:96-1451; mcp/tests/evidence-lifecycle.toml:1420-1452 |
| The population the pin names, re-derived at the merged tip — **16 contracts and 66 artifacts**, the values the constants below carry. | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-45 |
| **The source's own paragraph for this leaf, first in the docstring: the union of two consumer repairs, no registration, counts unchanged, and the digest it replaced.** | "Thirteenth deliberate re-pin (260921-ICR-L6" |mcp/tests/test_dependency_ownership_ast_helpers.py:423-423|

## 260921-ICR-L11 Catalogue Re-Pin — Two Consumer Rows, Counts Unchanged, Bytes Moved (The Fourteenth)

The catalog change is **consumer rows only, and it is the same shape as L1's, L18's and L6's**: the
durable-comparison-generation leaf registers no artifact and no contract of its own, and its fifteen
cases live in the ordinary unit module `mcp/tests/test_knowledge_review_comparison_generation.py`, which
builds on the existing `test_knowledge_review_source_endpoints.py` enclosure fixture. That module became
a source-derived consumer of two existing shared fixtures, so both `consumer_scope = "exact"` lists
gained exactly one path each:

| Artifact | Row that gained the path | Why the module consumes it |
| --- | --- | --- |
| diff-cases (`contract:knowledge-diff-cases`) | `mcp/tests/evidence-lifecycle.toml:1408-1408` | the cases read the candidate's content back out of the retained tree and build the enclosure over two real committed Git trees |
| read-scope (`contract:knowledge-read-scope-cases`) | `mcp/tests/evidence-lifecycle.toml:1433-1433` | the frozen comparison is between two snapshots of that fixture's recorded topology; the module imports `BATCH_PATH` |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| **The pinned counts and the re-pinned digest, as this leaf's own candidate and as the merged line carry them.** | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| **The constant's own fourteenth re-pin record, which names this leaf, its base and the two consumer rows.** | `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:110-128; mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:440-440; mcp/tests/test_dependency_ownership_ast_helpers.py:479-479; mcp/tests/test_dependency_ownership_ast_helpers.py:385-385; mcp/tests/test_dependency_ownership_ast_helpers.py:423-423 |
| The two rows this leaf appended, and the artifacts whose exact consumer sets they extend. | `consumers`; `consumer_scope` | mcp/tests/evidence-lifecycle.toml:97-97; mcp/tests/evidence-lifecycle.toml:96-96; mcp/tests/evidence-lifecycle.toml:1407-1407; mcp/tests/evidence-lifecycle.toml:1434-1434; mcp/tests/evidence-lifecycle.toml:1408-1408; mcp/tests/evidence-lifecycle.toml:1435-1435 |
| The module whose two consumer entries are the entire catalog delta. | "mcp/tests/test_knowledge_review_comparison_generation.py" | mcp/tests/evidence-lifecycle.toml:1405-1441; mcp/tests/evidence-lifecycle.toml:1442-1488 |
| The lane row added to the manifest in the same change, which pins no digest and refuses an unregistered module at collection. | "mcp/tests/test_knowledge_review_comparison_generation.py"; "unit-regression = [" | mcp/tests/test-evidence-lanes.toml:120-120; mcp/tests/test-evidence-lanes.toml:5-5 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| **The re-pinned constants, with the counts this leaf did not move and the digest it did.** | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| **The source's own paragraph for `260921-ICR-L3`, third in the docstring after the Seventeenth and the synced union: no registration, two consumer rows, counts unchanged, and the digest it replaced.** | "Fifteenth deliberate re-pin (260921-ICR-L3"; `LIFECYCLE_CATALOG_SHA256` |mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:239-239; mcp/tests/test_dependency_ownership_ast_helpers.py:336-336; mcp/tests/test_dependency_ownership_ast_helpers.py:357-357; mcp/tests/test_dependency_ownership_ast_helpers.py:440-440; mcp/tests/test_dependency_ownership_ast_helpers.py:479-479; mcp/tests/test_dependency_ownership_ast_helpers.py:385-385; mcp/tests/test_dependency_ownership_ast_helpers.py:423-423 |
| **The synced union paragraph, second in the docstring after this leaf's Seventeenth: both leaves' consumer rows in one catalog, and the digest the merged file measures.** | "Sixteenth deliberate re-pin (260921-ICR-L14" |mcp/tests/test_dependency_ownership_ast_helpers.py:363-363|
| The two consumer rows the leaf's module joined, and the artifact identities they belong to. | "mcp/tests/test_knowledge_review_source_content.py"; `consumer_scope`; `consumers` | mcp/tests/evidence-lifecycle.toml:1405-1441; mcp/tests/evidence-lifecycle.toml:1442-1488 |
| The check that recomputes the file's sha256 and counts both block kinds beside it. | `_assert_the_catalog_kept_its_bytes_and_identities` |mcp/tests/test_dependency_ownership_ast_helpers.py:886-902|
| The proof that this leaf's artifact delta is empty, which is why only a consumer change could move the digest. | `test_production_proof_adds_no_governed_evidence_artifact` |mcp/tests/test_dependency_ownership_ast_helpers.py:818-835|
| The lane row the same change added, which pins no digest and refuses an unregistered module at collection. | "mcp/tests/test_knowledge_review_source_content.py" | mcp/tests/test-evidence-lanes.toml:126-126 |
| **The re-pinned constants, with the counts this leaf did not move and the digest it did (`3e9105c2…` → `8d60a34c…`, the Seventeenth re-pin).** | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| **The source's own paragraph for this leaf: consumer-only, two exact-scope support rows, counts unchanged, and the digest it replaced.** | "Seventeenth deliberate re-pin (260921-ICR-L9" |mcp/tests/test_dependency_ownership_ast_helpers.py:343-343|
| **The two consumer rows this leaf's module joined, and the artifact identities they belong to.** | "mcp/tests/test_review_subject_catalogue.py"; `consumer_scope`; `consumers` | mcp/tests/evidence-lifecycle.toml:1405-1441; mcp/tests/evidence-lifecycle.toml:1442-1488 |
| The check that recomputes the file's sha256 and counts both block kinds beside it, re-derived because the docstring's new paragraph moved it. | `_assert_the_catalog_kept_its_bytes_and_identities` |mcp/tests/test_dependency_ownership_ast_helpers.py:886-902|
| The proof that this leaf's artifact delta is empty, which is why only a consumer change could move the digest. | `test_production_proof_adds_no_governed_evidence_artifact` |mcp/tests/test_dependency_ownership_ast_helpers.py:818-835|
| The lane row the same change added, which pins no digest and refuses an unregistered module at collection. | "mcp/tests/test_review_subject_catalogue.py" | mcp/tests/test-evidence-lanes.toml:187-187 |

## Update History
- 2026-09-28T23:11:42+02:00 — 260921-ICR-L56 curator (candidate tree `0dabc51f68b613546ec971657726b97828afb69a` over code base `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`): No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_read_anchor_memo.py` row at `:173`; each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T20:07:41+02:00 — 260921-ICR-L55 curator: No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_notes_listing.py` row at `:162` (candidate tree `c77a4346480db6674dd760f974e8b24079d8f755` over code base `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`). Each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.
- 2026-09-26T21:18:16+00:00: Generated citation repair: "mcp/tests/test_knowledge_review_source_content.py" repointed to mcp/tests/test-evidence-lanes.toml:122-122. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:18:16+00:00: Generated citation repair: "mcp/tests/test_review_subject_catalogue.py" repointed to mcp/tests/test-evidence-lanes.toml:178-178. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:795-815. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:44-44; mcp/tests/test_dependency_ownership_ast_helpers.py:45-45. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "260921-ICR-L20" repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:479-479. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_production_proof_adds_no_governed_evidence_artifact` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:818-835. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_production_proof_adds_no_governed_evidence_artifact` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:818-835. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:44-44; mcp/tests/test_dependency_ownership_ast_helpers.py:45-45. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "Thirteenth deliberate re-pin (260921-ICR-L6" repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:423-423. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "Sixteenth deliberate re-pin (260921-ICR-L14" repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:363-363. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_production_proof_adds_no_governed_evidence_artifact` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:818-835. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "mcp/tests/test_knowledge_review_source_content.py" repointed to mcp/tests/test-evidence-lanes.toml:118-118. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "Seventeenth deliberate re-pin (260921-ICR-L9" repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:343-343. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_production_proof_adds_no_governed_evidence_artifact` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:818-835. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "mcp/tests/test_review_subject_catalogue.py" repointed to mcp/tests/test-evidence-lanes.toml:174-174. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "Twentieth deliberate re-pin (260921-ICR-L8" repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:283-283. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "Nineteenth deliberate re-pin (260921-ICR-L8" repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:302-302. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "Eighteenth deliberate re-pin (260921-ICR-L8" repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:321-321. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:886-902. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_production_proof_adds_no_governed_evidence_artifact` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:818-835. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T12:55:00+02:00 — 260921-ICR-L27 curator (uncommitted change set on `ar/260921-icr-l27-ar`, code base `06ed70cfcde7e3860ee5b53435727e7512e4335c`): **body update: the knowledge-bootstrap census rows and the re-pin.** This leaf's three consumer-row additions to the two evidence-lane TOMLs shift the line numbers of the tables they are inserted into, so this card's citation rows were re-read and re-anchored to the lines that now carry each anchor — a pure move, never a range derived by adding a delta to an old number, and never a workspace-wide projection. No claim wording was changed and no row was dropped. No verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **the `LIFECYCLE_CATALOG_SHA256` pin was re-pinned** to the catalog's post-edit bytes. The population it names is unchanged — the new case module joined lane and consumer rows that already existed — so the counts this card records still hold. **Citation accounting:** the ranges this card carries into the files this leaf's change set moved were re-derived against the candidate's own bytes rather than shifted by a remembered delta, and the rows the product reported as `citation_anchor_absent_from_range` were re-anchored to the constructs they name. No claim and no row was dropped, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-23T10:05+02:00 — 260921-ICR-L21 citation-repair curator (memory worktree only; no code changed, no commits; leaf base `972b44cc07b307929535fe7974d6a30d53c9c4f1` plus the worker's uncommitted delta): **body update: this card's live rows were re-read against the catalog and the lane manifest, and the fourteen enforced `citation_anchor_absent_from_range` rows it carried were repaired by hand.** The delta's three consumer entries in `mcp/tests/evidence-lifecycle.toml` (`:801`, `:1428`, `:1472`) and one lane row in `mcp/tests/test-evidence-lanes.toml` (`:212`) moved the artifact blocks below `:799` by one to three lines, while the re-pinned constant itself stayed at `:46`. Each repaired range now names the line that carries its own anchor: the three re-pin consumer entries (`:1495`, `:1517`, `:1592`), the reviewed module's two catalogue rows (`:1423`, `:1467`) beside the identity declarations they belong to (`:1409-1411`, `:1443-1445`), the consumer entries `:1412`/`:1446`, `:1419`/`:1461`, `:1420`/`:1462` and `:1463`/`:1464`, and the six relationship entries (`:1424`-`:1426`, `:1468`-`:1470`). No claim wording and no anchor was changed, no row was dropped to silence a finding, and **no verification stamp was advanced** — the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-22T15:40:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **the Seventeenth deliberate re-pin recorded (605 → 651 lines; the docstring's new paragraph is 19 of those lines).** `LIFECYCLE_CATALOG_SHA256` moves from L14's merged `3e9105c2116422debaa01c295294fc0c714288f701ee5902e6552884b64a52d8` to **`8d60a34cf56a9740e234823658312c8b6f5ae4e958344fe8ba2ea152b8ff6891`** (measured with `sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate: 1683 lines), while `LIFECYCLE_CONTRACT_COUNT` stays **16** and `LIFECYCLE_ARTIFACT_COUNT` stays **66** — the leaf registered nothing; its two consumer rows (the new `test_review_subject_catalogue.py` appended to `diff_scope_test_support`'s and `read_scope_test_support`'s `consumer_scope = "exact"` lists, at `:1416` and `:1453`) and its one lane row (`test-evidence-lanes.toml:161`, the file 337 → 338 lines) are the whole delta. The constant's docstring now opens with the `Seventeenth deliberate re-pin` paragraph at `:49-67`. The re-pin table gained this leaf's row; the current-value row's wording — which named `53ba6331…`, the `260921-ICR-L6` measurement — is **corrected rather than carried**, because it was already stale at the landed base. **Citation accounting:** every range into this file re-derived from its construct's own measured extent (the constants `43-46` unchanged, the docstring `47-495`, the Seventeenth paragraph `49-67`, the Sixteenth `69-127`, the Fifteenth `91-108`, the Fourteenth `110-128`, the Thirteenth `129`, L1 `178-183`, L18 `162-184`, L20 `185`, `test_repository_inputs_reach_their_supported_consumers` `502-522`, `test_production_proof_adds_no_governed_evidence_artifact` `525-542`, `_assert_the_proof_is_selected_by_the_lane_manifest` `559-570`, `_assert_the_governed_inventory_is_closed` `572-590`, `_assert_the_catalog_kept_its_bytes_and_identities` `592-608`), with the catalog-extent rows re-derived (`evidence-lifecycle.toml:1-1683`). One generated history bullet was left byte-identical (the 2026-09-21 repair record), and no history entry was rewritten. **Stamp accounting:** the verification pair names the leaf's base — the last real commit the reading was taken against — because the re-pin exists only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Merged measurement:** the catalog both leaves' rows now share is 1681 lines and `3e9105c2116422debaa01c295294fc0c714288f701ee5902e6552884b64a52d8`, L3's own re-pin being the fifteenth and this leaf's the sixteenth (`16 / 66` counts unchanged). **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the fifteenth deliberate re-pin, consumer rows only, counts unchanged, and every range in this card re-derived against a file that grew 19 lines inside its docstring.** `LIFECYCLE_CATALOG_SHA256` moves from L11's `aedb2636…` to **`dc6e380867302d7e2fff89f8c36549c85528ed4dafa28b4510981b573f09739b`** (measured with `sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate: 1677 lines), while `LIFECYCLE_CONTRACT_COUNT` stays **16** and `LIFECYCLE_ARTIFACT_COUNT` stays **66** — the leaf registered nothing, and its two consumer rows on `mcp/tests/evidence-lifecycle.toml`'s `consumer_scope = "exact"` lists (`:1412` on the diff-cases artifact, `:1445` on the read-scope artifact) are the whole delta, derived from the census's own `missing=[…]` / `unsupported=[]` finding. The constant's docstring now opens with the `Fifteenth deliberate re-pin` paragraph at `:49-66`, and the file is **609 lines** against the base's 590 (a 21-line diff hunk: one replaced constant plus 19 inserted docstring lines). **Citation accounting:** the quality gate reported **18 findings** for this card — 12 range-resolution rows and 6 reopened claims — and every one was cleared by re-reading the row against the candidate and re-deriving its range from the construct's own extent rather than by adding the remembered delta: the docstring-derived rows (`:47-417` → `:47-453`; L6's paragraph `:46-83` → `:87-102`; L20's `:124-138` → `:143-157`; L18's `:101-115` → `:120-134`; L1's `:117-122` → `:136-141`; L11's `:49-67` → `:68-85`), the helper rows (`:515-531` → `:550-566`, `:495-512` → `:530-547`, `:482-492` → `:517-527`, `:448-464` → `:482-499`, `:425-444` → `:459-479`), the catalog rows this leaf's own additions displaced (`mcp/tests/evidence-lifecycle.toml` `:1444`/`:1445` → `:1446`/`:1447`; the two artifact extents `:1-1673` → `:1-1677`), and the reopened claims — one row's quoted docstring label that no longer resolved anywhere (now the leaf id the paragraph actually carries), one row that named the catalog by its own path as an anchor (now the two rows that carry the modules, `:731-732`), one row whose anchor named the wrong module's file (now the two consumer rows that are the delta), and the row whose anchor cell was a non-identifier lane name (now the module path plus the lane key). No claim, anchor or row was dropped to silence a finding, and **no verification stamp was advanced** — the candidate is uncommitted and the governed closeout owns the real memory commit. **One code-side discrepancy is recorded, not edited:** the new paragraph says the leaf's module holds "sixteen source-content cases" while that module defines **twenty** `test_` functions, which is the count this card and its sibling records state.
| **The constant's own fourteenth re-pin record, which names this leaf, its base and the two consumer rows.** | `LIFECYCLE_CATALOG_SHA256`; *(docstring)* | mcp/tests/test_dependency_ownership_ast_helpers.py:46-136 |
| The two rows this leaf appended, and the artifacts whose exact consumer sets they extend. | `consumers`; `consumer_scope` | mcp/tests/evidence-lifecycle.toml:1392-1415; mcp/tests/evidence-lifecycle.toml:1418-1450 |
| The module whose two consumer entries are the entire catalog delta, and the constant they moved. | "mcp/tests/test_knowledge_review_comparison_generation.py"; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/evidence-lifecycle.toml:1392-1415; mcp/tests/evidence-lifecycle.toml:1418-1450; mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:440-440; mcp/tests/test_dependency_ownership_ast_helpers.py:479-479; mcp/tests/test_dependency_ownership_ast_helpers.py:385-385; mcp/tests/test_dependency_ownership_ast_helpers.py:423-423 |
| The lane row added to the manifest in the same change, which pins no digest and refuses an unregistered module at collection. | `unit-regression`; "mcp/tests/test_knowledge_review_evidence_channels.py" | mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/test-evidence-lanes.toml:111-112; mcp/tests/test-evidence-lanes.toml:113-113 |

## Update History
- 2026-09-21T22:25:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **the fifteenth deliberate catalog re-pin, and one stale statement on this card corrected rather than carried.** `mcp/tests/test_knowledge_review_evidence_channels.py` registers no artifact and no contract of its own — its cases build on the existing endpoint fixture and the existing curator-coherence publication helper — so the catalog delta is **four consumer rows** on existing `consumer_scope = "exact"` lists (`curator_coherence_test_support`, `diff_scope_test_support`, `read_scope_test_support` and the Node `package-lock.json` fixture the census's propagation rule reaches), and the constants are re-pinned from `aedb2636844faf41ca63b7099e6c62bcaf888720e7e7dd78e203e3a1c9e061ff` to `4d1573760968b52a1cb8b087e235c21f40f0e2eccf2a5dcae3e19f0e5ae099a1`, measured with `sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate; the populations stay **16 / 66**. A row was added to the re-pin table and the "current value" paragraph now states this leaf's pair. **That paragraph also carried a false value:** it named `24e760a1…` as the current pin, which was `260921-ICR-L1`'s measurement; the value the constant actually carried at this leaf's base is `aedb2636…` (`260921-ICR-L11`'s), read from the constant itself in the candidate before this leaf's edit. The correction is recorded on the card rather than applied silently. The module's own docstring gained the fifteenth re-pin paragraph (naming the four rows, the census finding each is derived from, and the re-pinned digest), and that docstring is the primary record; this card is the curator's. **A structural defect found and deliberately not fixed:** the card carries **two** `## Update History` headings — the merge residue of the `260921-ICR-L11` union — and this entry is prepended to the first (the newest-first list) rather than restructuring the other leaf's history placement outside this leaf's change. **Stamp accounting:** the verification pair is retained as recorded (`d80a0513…` / `2026-09-21T19:51:20+02:00`), which is the same production line this reading was against; no stamp was invented, and the governed closeout's metadata refresh remains the real one.
- 2026-09-21T22:16+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **the mechanically projected ranges this document was carrying were re-read against the constructs they now name, and the projection records were replaced by this review.** The mechanical anchor-range projection this leaf's citation pass ran wrote ``LIFECYCLE_CATALOG_SHA256`` → mcp/tests/test_dependency_ownership_ast_helpers.py:46-46 into this document's Update History. This pass read each affected claim against the construct inside the range it now cites — the wording is retained where the construct supports it and the range was left as the projection re-derived it only after that reading — so the ranges are curator-read evidence rather than unreviewed projections, and the projection bullets are superseded by this entry rather than kept beside it. The claims are not otherwise re-worded, no anchor was renamed, no citation was dropped and no verification stamp was advanced: the candidate is uncommitted and the governed closeout's own metadata refresh owns the real stamp.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:462-482. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:553-569. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:553-569. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:553-569. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `test_production_proof_adds_no_governed_evidence_artifact` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:485-502. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:553-569. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T20:44:00+02:00 — 260921-ICR-L11 curator, **memory-side sync conflict resolved as a UNION with the incoming `260921-ICR-L20` line; no side and no claim was dropped.** The header keeps both candidate rows under one `lastUpdated` and the incoming line's stamp; both re-pin sections are kept — `260921-ICR-L20`'s and this leaf's — and both history entries are kept with this leaf's first. **Citation accounting:** thirteen lines of ranges into `mcp/tests/evidence-lifecycle.toml` were re-derived against the merged file, and fourteen lines into `test_dependency_ownership_ast_helpers.py` itself were re-derived against that file's own insertion (`+19` from line 48, which is this leaf's docstring paragraph) — so the rows that cite `:105-119` now cite `:124-138`, and the whole-docstring range now ends at `:417`. **Claims corrected rather than merged:** this leaf's section now states the merged constant (`aedb2636…`, 1675 lines) beside its own-candidate measurement (`6b73894f…`, 1673 lines); `260921-ICR-L20`'s "carries `51a218a0…`" is re-framed as that leaf's own-merge measurement superseded by this leaf's two consumer rows; and an **ordinal note** records that the source's own count now numbers this leaf's record the fourteenth while `260921-ICR-L20`'s entry keeps its own candidate's ordinal as an as-of record. **No verification stamp was advanced** — the header keeps the incoming line's `945ddad6a9c90fbf5d7eef7546b9e69714c6c4fc` / `2026-09-21T18:46:40+02:00`, not this leaf's superseded `9043a82e…`.
- 2026-09-21T20:16:00+02:00 — 260921-ICR-L11 curator (uncommitted change set on `ar/260921-icr-l11`, base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`): **the fourteenth deliberate re-pin, and a consumer-only change again.** `LIFECYCLE_CATALOG_SHA256` moves from L6's `7920a0f9f6134d3849e60685ad8a9424cdc95e8209631a03b889cf7d79e05281` to **`6b73894fb010534d5cedbdace361504d1a67abb2ce8ffb76de8d00ac2e0af39e`** (measured with `sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate, `1673` lines), while `LIFECYCLE_CONTRACT_COUNT` stays **16** and `LIFECYCLE_ARTIFACT_COUNT` stays **66** — the leaf registered no artifact and no contract. The delta is one consumer path appended to each of two existing `consumer_scope = "exact"` lists (`mcp/tests/evidence-lifecycle.toml:1403` on the diff-cases artifact and `:1427` on the read-scope artifact) for `mcp/tests/test_knowledge_review_comparison_generation.py`, derived from the census's own `missing=[…] / unsupported=[]` finding rather than from inspection. The new section above supersedes the "current value" paragraph rather than editing it, because that paragraph is L1's own as-of record; the constant's docstring carries the same fourteenth re-pin beside the declaration, so the two agree at this tip. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded, because the candidate is uncommitted and the governed closeout owns the real stamp; the reading this entry was made against is named in the entry itself.
- 2026-09-21T18:35+02:00 — 260921-ICR-L20 curator, **memory-side sync conflict resolved as a UNION with the incoming `260921-ICR-L6` line; no side and no claim was dropped.** Both leaves' re-pin sections and both history blocks are kept, and the metadata block keeps the incoming line's stamp rows with this leaf's candidate reading recorded in the entry beside them. Every range the resolution keeps was then re-derived against the merged candidate rather than shifted by a remembered delta (the four rows of `260921-ICR-L1`'s re-pin table were re-derived against the merged file (its paragraph at `:98-103`, the two consumer rows at `:1410`/`:1441`, the catalog check at `:512-528`, `build_endpoint_fixture` at `:198-222`) and this leaf's own section was re-measured the same way); where both sides cited the same construct the merged extent was taken, and two claims that had become untrue in the merged state were corrected rather than kept in two wordings (this leaf's section now states the merged catalog digest `51a218a0…` and records its own pre-merge `4da5626…` as historical; `260921-ICR-L6`'s paragraph keeps its own historical `7920a0f9…`). **No verification stamp was advanced:** the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is exactly what the incoming line recorded (`9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75` / 2026-09-21T18:13:19+02:00 where that line carried it), this leaf's candidate reading was recorded in the entry as metadata and not as a stamp, and the governed closeout owns the real commit.
- 2026-09-21T18:20:00+02:00 — 260921-ICR-L6 curator (uncommitted change set on `ar/260921-icr-l6`, merged base `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **a one-row consumer re-pin, revised at the sync so the card states the merged file rather than either side of it.** The section above records the one value this leaf moved (`3f91773d…` → `7920a0f9…`, measured with `sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate), the two count constants it leaves at `16` / `66`, the `Thirteenth deliberate re-pin` paragraph at `:49-64` — written at the sync as the union of two consumer repairs, and placed first because the docstring is newest-first — and the two consumer rows in the catalogue: its own case module and L18's landed `mcp/tests/test_read_ar_files.py`, kept as a set and each named exactly once. **Citation re-derivation:** every current-claim row into this file was re-derived from each construct's own extent on the merged candidate rather than shifted by a delta — docstring `47-398`, `test_repository_inputs_reach_their_supported_consumers` `406-425`, `test_production_proof_adds_no_governed_evidence_artifact` `429-445`, `_assert_the_proof_is_selected_by_the_lane_manifest` `463-473`, `_assert_the_governed_inventory_is_closed` `476-493`, `_assert_the_catalog_kept_its_bytes_and_identities` `496-512`, `260921-ICR-L1`'s docstring paragraph `98-103`, `build_endpoint_fixture` `198-222`, and the catalogue's own extent `1-1671`. The card's `15 / 65` and `53ba6331…` statements were corrected to the merged **16 / 66** and `7920a0f9…`; the pre-sync values are named here as the earlier candidate's measurement rather than kept as live claims. L18's and L1's entries below are kept whole. Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **fourteenth deliberate re-pin — consumer rows only, counts unchanged.** `mcp/tests/test_knowledge_ingest_publication_route.py` reaches `mcp/tests/snapshot_lifecycle_test_support.py` through the ingest-list fixture module it imports, and the census's own propagation rule reaches the Node `package-lock.json` fixture through the CLI import chain those rows already name, so exactly two `consumer_scope = "exact"` rows gained the path, no `[[contract]]` and no `[[artifact]]` was added or removed, and every artifact's own identity is unmoved. The section above records the structural facts, the count that did not move, and the one row that did; the digest this leaf re-pinned on its own candidate (`4da5626…`) is recorded there as the historical value it is, because the merged catalog carries `51a218a0…`. No verification stamp was advanced — the governed closeout owns the real commit.
- 2026-09-21T15:35+02:00 — 260921-ICR-L18 curator (uncommitted change set on `ar/260921-icr-l18`, code base `0fca5c69766aa95eebe950c19fbcdc83864ec35a`): **the thirteenth deliberate re-pin, and a consumer-only change again.** `260921-ICR-L18` registered no artifact and no contract: its two new unit modules import the existing `snapshot_lifecycle_test_support` builders and the existing ingest-list fixture module rather than introducing a third support module, so both count constants stay `16`/`66` and the proof's artifact delta stays empty. Only `LIFECYCLE_CATALOG_SHA256` moved, to `4fb2bc3f2da65134e428631f0e964f4f712e6655f4816934e2a93a4cb8e32046` (measured with `sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate), and the file gained sixteen lines: the digest and a thirteen-line provenance paragraph placed **first** in the docstring at `:47-62`, above `260921-ICR-L1`'s, because the docstring is newest-first. A new section above states the change and cites it. **Citation accounting:** the insertion is inside the docstring only, so the four constants at `:43-46` keep their lines and everything from `:52` in the baseline moves by `+15`; every citation into this file across the onboarding tree was re-derived from the file's own diff-verified offset rather than shifted by a carried delta, and the one row that cited this leaf's own paragraph by line was re-pointed to the paragraph that matches its claim (ICR-L1's, at `:64-69`). `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained as recorded; the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, code base `f745e166`): **a consumer-only re-pin, and two stale current-value statements corrected rather than carried.** The leaf appends one consumer row to each of `mcp/tests/diff_scope_test_support.py`'s and `mcp/tests/read_scope_test_support.py`'s exact lists for `mcp/tests/test_knowledge_review_source_endpoints.py`, adds no contract and no artifact, and re-pins `LIFECYCLE_CATALOG_SHA256` to the file's measured sha256 `24e760a1…` (the value it replaces is `f0cb5fec…`), with the reason written beside the constant in the source's own docstring. **The counts were already 16 / 66** — `260918-TSIP-L10`'s `T129` reconciliation moved them — while the card's re-pin narrative and its `### Logic` constants paragraph still said `15 / 65` and `c499cbcc…`, so both were re-read against the constants and the file's own blocks and corrected in this pass; the re-pin table gained a row named by this leaf rather than by an ordinal, since the table's and the docstring's counts of re-pins already disagree and that question stays open. Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.

- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:349-369. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:440-456. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:324-344. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:415-431. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:25+02:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **cleared the three enforced `citation_anchor_absent_from_range` rows this card carried — the same three consumer entries the 01:37 pass repointed, moved one more line by the sync onto the master line.** The 01:37 pass read them at `mcp/tests/evidence-lifecycle.toml:1454-1454`, `:1476-1476` and `:1551-1551` on the pre-sync catalogue; the merged catalogue (this leaf's own `mcp/tests/evidence-lifecycle.toml` change and L30's re-pin, resolved by re-measuring the digest at 15 contracts / 65 artifacts) puts each named path's own line at **1455** (`"mcp/tests/eve_capsule_test_support.py"` in that artifact's `path =` line), **1477** (`"mcp/tests/eve_adapter_test_support.py"`) and **1552** (`"mcp/tests/fixtures/codex_app_server_model_page.json"`). Each of the three ranges now cites the line that carries its own named path verbatim; the sibling ranges in both rows (`:660-660` for the package-lock fixture, `:385-385` for the curator-coherence support module) were verified current and are unchanged, as are every claim, anchor and row. Claim wording and anchors are untouched, no range was dropped to silence a finding, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits. No commits.
- 2026-09-20T01:37+02:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): range repair only; every claim's wording, anchor set and row kept. Three reference rows citing this module and the governed catalogue were re-derived against the file as it stands on this candidate. The closure/lane-membership row had been left on a pre-move projection (`:191-194; :178-181; :290-320`) that names the two calls' call sites and an unrelated test, not their declarations; it now cites each declaration's own extent, `mcp/tests/test_dependency_ownership_ast_helpers.py:360-377` for `_assert_the_governed_inventory_is_closed` and `:347-357` for `_assert_the_proof_is_selected_by_the_lane_manifest`. The two catalogue rows the L23 residue entry had already repointed once moved again when the catalogue's own consumer lists grew: the `260915-CAPS-L17` row's `eve_capsule_test_support.py` and `eve_adapter_test_support.py` entries now stand at `mcp/tests/evidence-lifecycle.toml:1454-1454` and `:1476-1476` (was `:1449-1449`/`:1471-1471`), and the `260915-CAPS-L15` row's `codex_app_server_model_page.json` entry now stands at `mcp/tests/evidence-lifecycle.toml:1551-1551` (was `:1546-1546`); each is the line that carries the named path verbatim in its artifact's `consumers` list, and the sibling ranges in both rows were already correct and are unchanged. No verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-20T01:27+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared all three enforced `citation_prose_not_in_cit_form` rows this card carried, without changing what the sentence claims.** All three fired on the same sentence — the digest chain in the `260915-KS-L30` re-pin section — whose three entries read `` `633b03ee…` (L21) ``, `` `68a64207…` (L22) `` and `` `25b00f88…` (L23) ``: the checker pairs a code span with a following parenthesized `L<digits>` and reads it as the superseded `X (L47)` citation spelling. A `cit:` rewrite is not available honestly here, and this is why: the three anchors are *leaf labels*, not line ranges (the same repository uses `(L4)` as leaf shorthand, which the checker accepts); and the digests are historical catalogue identities that exist NOWHERE in the tree (only the current `73cdd218…` is in the source, at `mcp/tests/test_dependency_ownership_ast_helpers.py:46`), so any `cit:` form would have to name an anchor no range can hold — three new enforced `citation_anchor_absent_from_range` rows in place of three prose rows. The cure applied is therefore the one that states the same fact unambiguously: each of the three parentheticals now carries a comma and the qualifier this card's own sections give that leaf's re-pin — `(L21, the census leaf, the first re-pin since L11 that moved both counts)`, `(L22, bytes only)`, `(L23, four consumer rows)` — which is the form the chain's own last two entries already use (`(L28, recorded here from the source's own text)`, `(L30, this candidate)`). No digest, arrow, leaf label or claim was changed, no `cit:` citation was added or removed, and the chain's meaning is unchanged. Reviewed against the working candidate `ar/260915-ks-l30-ar`; no commit exists for these bytes and the commit stamp is not advanced.
- 2026-09-20T01:20+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 2 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `test_dependency_ownership_ast_helpers.py.md:188` ("mcp/tests/fixtures/repository_profiles/node/package-lock.json", "mcp/tests/eve_capsule_test_support.py", "mcp/tests/eve_adapter_test_support.py") — re-read the claim against the landed source: the construct moved and the cited range was widened to the line that actually carries it, per the checker's own remedy; `test_dependency_ownership_ast_helpers.py.md:191` ("mcp/tests/curator_coherence_test_support.py", "mcp/tests/fixtures/repository_profiles/node/package-lock.json", "mcp/tests/fixtures/codex_app_server_model_page.json") — re-read the claim against the landed source: the construct moved and the cited range was widened to the line that actually carries it, per the checker's own remedy.
- 2026-09-19T23:20+00:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **the tenth-plus re-pin, counts unmoved and the digest re-measured.** The leaf's catalog change is a pure consumer change — two rows appended to `mcp/tests/merge_case_test_support.py`'s exact list, one direct (`mcp/tests/test_worktree_sync.py` now builds its knowledge-dataset conflict scenario through the harness) and one transitive (`mcp/tests/test_sync_parked_candidate.py` reaches it through its existing import of `test_worktree_sync`) — so `LIFECYCLE_CONTRACT_COUNT` and `LIFECYCLE_ARTIFACT_COUNT` still read 15 and 65 while `LIFECYCLE_CATALOG_SHA256` moved to `f786c15749667cbd90797672cce4a92026b7b21ce4b773daa4eb3cb37e01e6c5`, reproduced with `sha256sum` on this candidate. The card's re-pin table gained its eleventh row, the two paragraphs that still presented `25b00f88…` as *this candidate's* value were corrected to name the L23 tip they describe, and the transitive row is recorded as the shape a reader should carry forward rather than as an oddity. Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-19T22:49:08+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:289-309. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:49:08+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:380-396. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 3 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `mcp/tests/eve_adapter_test_support.py`; `mcp/tests/eve_capsule_test_support.py`; `mcp/tests/fixtures/codex_app_server_model_page.json`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): re-read the three pinned constants against the catalogue's bytes and recorded this candidate's value: **`LIFECYCLE_CONTRACT_COUNT = 15`**, **`LIFECYCLE_ARTIFACT_COUNT = 65`** and **`LIFECYCLE_CATALOG_SHA256 = 73cdd2183e153af752773e8a4c6076e5e2eb7053d9e0ce5fa6538a69c907cefe`**, which `sha256sum mcp/tests/evidence-lifecycle.toml` reproduces and which the constant carries (was `6ec7eb0d…` at this leaf's base, L28's value by the source's own docstring). The re-pin is **bytes-only and consumer-only**: one row appended to the tail of `mcp/tests/snapshot_lifecycle_test_support.py`'s `consumers` list for `mcp/tests/test_knowledge_curator_ingest_list.py`, because the CYCLE-01 continuity case imports `build_case`/`create`/`write_record` to get a real candidate database to fork; no contract and no artifact was added, so both counts stay where they were. Three current-value statements in `### Logic` were corrected rather than carried — the "current value" paragraph's digest and its attribution, the "(`25b00f88…`)" clause, and the "value at this candidate" paragraph — and the docstring-residue claim was corrected against the file as it now stands: its opening paragraph still presents L28's `6ec7eb0d…` as "the value this line carries" while the line carries this leaf's digest, which is recorded for the owning builder rather than edited here. Two reference rows whose anchors this leaf's citation pass had left on pre-move ranges were re-cited to their constructs' own extents (the closure and lane-membership helpers, `:347-357` and `:360-377`), the pinned-population row's catalog extent was re-measured (`:1-1637` → `:1-1641`), and the constants' rows now cite `:43-46` / `:44-46`. The metadata block's `lastUpdated` names this leaf's pass and **the commit fields are untouched** — the change is uncommitted and closeout owns the stamp.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:289-309. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:380-396. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 4 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `test_dependency_ownership_ast_helpers.py.md:184` (`_assert_the_governed_inventory_is_closed`, `_assert_the_proof_is_selected_by_the_lane_manifest`); `test_dependency_ownership_ast_helpers.py.md:188` ("mcp/tests/fixtures/repository_profiles/node/package-lock.json", "mcp/tests/eve_capsule_test_support.py", "mcp/tests/eve_adapter_test_support.py"); `test_dependency_ownership_ast_helpers.py.md:190` (`LIFECYCLE_CONTRACT_COUNT`, `LIFECYCLE_ARTIFACT_COUNT`); `test_dependency_ownership_ast_helpers.py.md:191` ("mcp/tests/curator_coherence_test_support.py", "mcp/tests/fixtures/repository_profiles/node/package-lock.json", "mcp/tests/fixtures/codex_app_server_model_page.json").
- 2026-09-18T17:53:32+00:00: 260915-KS-L23 residue clearance (seat A): re-read the three `mcp/tests/evidence-lifecycle.toml` reference rows whose ranges this leaf's appended consumer rows had moved, and repointed each to the construct its anchors name on this candidate. The `260915-CAPS-L17` consumer-entry row's three anchors (`mcp/tests/fixtures/repository_profiles/node/package-lock.json`; `mcp/tests/eve_capsule_test_support.py`; `mcp/tests/eve_adapter_test_support.py`) were cited as `:604-655; :724-741; :1178-1193; :1427-1434; :1449-1456; :1437-1437; :1459-1459; :1438-1438; :1460-1460; :659-659; :1442-1442; :1464-1464; :1444-1444; :1466-1466`, which now hold the `gate_certification_evidence` consumer list's tail, the `dispatch_brief` row and the evidence-cases row rather than those three artifacts, and now read `:660-660; :1449-1449; :1471-1471` — each artifact row's own `path` line, the row the consumer entry belongs to. The `260915-CAPS-L15` row's three anchors (`mcp/tests/curator_coherence_test_support.py`; `mcp/tests/fixtures/repository_profiles/node/package-lock.json`; `mcp/tests/fixtures/codex_app_server_model_page.json`) were cited as `:329-351; :603-625; :1252-1267; :373-380; :648-655; :1524-1531; :1534-1534; :1535-1535; :384-384; :659-659; :1539-1539; :1541-1541`, a pre-move projection whose `:384-384` and `:659-659` still land on the `[[artifact]]` headers one line above each named row, and now read `:385-385; :660-660; :1546-1546`. The pinned-population row's file extent was re-measured against the file as it stands on this candidate: `mcp/tests/evidence-lifecycle.toml:1-1630` -> `mcp/tests/evidence-lifecycle.toml:1-1637`. Every pre-move range is recorded here rather than deleted; no anchor, claim, row or range was removed, no claim wording was changed to fit a range, and no row outside this residue was touched. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T19:34+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): re-read the three pinned constants against the catalogue's bytes and recorded this candidate's value: **`LIFECYCLE_CONTRACT_COUNT = 15`**, **`LIFECYCLE_ARTIFACT_COUNT = 65`** and **`LIFECYCLE_CATALOG_SHA256 = 25b00f8832420b705495931c3a04ad13a9bfe83e367a97c4a854b36030071e30`**, which `sha256sum mcp/tests/evidence-lifecycle.toml` reproduces and which the constants carry. The re-pin is **bytes-only**: no contract and no artifact was added, and the four appended consumer rows item 13 and the item-16 case produced are the whole change, each appended to the tail of its `consumers` list so that no other row of the catalogue moved. Three current-value statements in `### Logic` were corrected rather than carried — the "current value" paragraph's digest and its attribution, the "value at this candidate" paragraph, and the clause naming the digest this candidate hashes to — and the docstring-residue claim was corrected against the file as it now stands (its opening paragraph reads fifteen contracts and sixty-five artifacts; the "five times" header and the duplicated "Fourth deliberate re-pin" label are gone; the older branch counts survive at `:233` and `:254`). The re-pin ordinal problem is recorded, not re-derived: the table ends at `tenth` while the L22 section also calls itself the tenth, so the new section names the values by leaf. This entry names this leaf's candidate as the reading's basis and **the commit fields are untouched** — the change is uncommitted and closeout owns the stamp.
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): re-read all three pinned constants against the catalog's bytes and recorded the **tenth deliberate re-pin, the first since `260915-KS-L11` that moves the block counts as well as the digest**. `LIFECYCLE_CONTRACT_COUNT` is **15**, `LIFECYCLE_ARTIFACT_COUNT` is **65** and `LIFECYCLE_CATALOG_SHA256` is re-measured to **`633b03ee16893ce3d0e838659d52f2bc609903f5c75b142eb41ca8c4fdabf5e6`**, which `sha256sum mcp/tests/evidence-lifecycle.toml` reproduces and which the constants carry, because this leaf appends one `[[contract]]` (`migration-census-cases`, owner `mcp/tests/migration_census_test_support.py`, evidence node `mcp/tests/test_migration_census.py::test_the_seed_writes_every_census_record_kind_through_the_shipped_batch_operation`) and one `[[artifact]]` for that same support module, with exactly one declared consumer. Every earlier count this card states — `4 / 45`, `13 / 54`, `14 / 55`, `14 / 64` — is retained as the measurement of the tip that produced it and none was deleted, and the re-pin table now carries a tenth row beside the ninth. **The constant's own docstring still opens "fourteen contracts and sixty-four artifacts" and repeats its provenance narrative twice**, so the record states that the declarations, not the prose, are the authority and leaves the code residue to its owning builder. Two reference rows were re-cited: the pinned-population row now cites `mcp/tests/evidence-lifecycle.toml:1-1630` (was `:1-1326`, the file's previous extent) and the constants' row no longer claims the docstring holds "all five deliberate re-pin records". The metadata block above now names this leaf's candidate as what was read and carries **no `lastVerifiedCommitHash`**: the body was re-read against a working candidate no commit contains, so no real commit holds the content a stamp would claim to have verified, and closeout owns the stamp. The body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-09-18T13:36:47+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:266-286. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:357-373. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:266-286. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:05+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): recorded the **seventh deliberate re-pin of the evidence-catalog identity, again a consumer change only.** `LIFECYCLE_CATALOG_SHA256` moved to **`143b0cf5c3a8432450f45072b7351057ba51fe6c386f65eb662c0ec4cb729ce6`**, re-measured here by hashing `mcp/tests/evidence-lifecycle.toml` on this candidate, with the two counts unchanged at **14 contracts / 64 artifacts** because no contract and no artifact was added: the leaf's three test modules consume the already-registered `diff_scope_test_support` (one row) and `read_scope_test_support` (two rows) artifacts. **Two records of this re-pin disagree with the tree and are recorded as such rather than carried forward:** the provenance paragraph the leaf added beside the constants says the counts "stay thirteen and fifty-four" against constants that read 14 and 64, and the leaf's worker report names the digest `b0bedae9071ec992cb011ba3e327ae67ff4c9728d9290bdfcdd50caff1263dd7`, a value that appears nowhere in the tree. The code was not edited to reconcile either — it is not this seat's to edit — so the discrepancy is named here where a successor will meet it. Verification metadata: the reviewed candidate moved to this leaf; the commit fields are untouched because the code commit does not exist yet and closeout owns the stamp.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:232-252. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:323-339. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-diff-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:60-60. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:232-252. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-diff-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:60-60. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "id = \"knowledge-diff-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1269-1269. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 7 generated projection bullet(s) by hand while resolving the memory sync** — `id = \`, `test_repository_inputs_reach_their_supported_consumers`, `_assert_the_catalog_kept_its_bytes_and_identities`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T05:00:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **recorded the sixth deliberate re-pin of the evidence-catalog identity, the second one where only the digest moved, and re-derived this card's citations against the source the worker actually changed.** `LIFECYCLE_CATALOG_SHA256` moved `c6956899…` → **`03c384c790ef9a1e552800048f3f92fef96e1e69c7872aaed122f86b206c1968`** with **both counts unchanged at 13 / 54**, because L19's catalog change is a *consumer change only*: its two requirement-revision test modules consume the already-registered `knowledge_fixture_test_support` and `generation_test_support` fixtures, so both artifacts' `consumers` lists gained the two module paths and no artifact or contract was added. The source's own comment above the constant states that reason beside L14's, and the body now states it too — the pin's value is the only thing a reader should take from this paragraph, and any further catalog change must re-pin deliberately in the same change. **This document is a changed-source sidecar** (`mcp/tests/test_dependency_ownership_ast_helpers.py` is +11/-4 in this change set), so the body update is a content update rather than a metadata-only refresh. Two citation corrections: the pin constants' row cited `:43-65`, the span the constants' *comment block* ended at, and now cites the three declarations at `:43-46`; and the catalog-block row's `mcp/tests/evidence-lifecycle.toml` citation was re-pointed from `:1252` to `:1256`, where the `knowledge-diff-cases` contract id actually stands. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read the fifth deliberate catalogue re-pin and corrected the record against the file's own bytes.** This leaf's three consumer registrations changed `mcp/tests/evidence-lifecycle.toml`, so `LIFECYCLE_CATALOG_SHA256` was re-pinned to that file's measured sha256 — `2505cc7dd6eb52f9ab96bb61b25bf11ed1de50db72371d058524290c419d9eeb` — which is what the constant carries, while `LIFECYCLE_CONTRACT_COUNT` stays **13** and `LIFECYCLE_ARTIFACT_COUNT` stays **54** because no artifact and no contract was added. The re-pin's reasoning is written beside the constant in the source. **The leaf's own report records a different value for this re-pin that appears nowhere in the tree**, so the constant is the authority. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded the re-pinned catalog identity as a measurement of this candidate rather than a constant. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/evidence-lifecycle.toml:1252-1252` -> `mcp/tests/evidence-lifecycle.toml:1253-1253`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): recorded the **sixth deliberate re-pin of the evidence-catalog identity, and the second one where only the digest moved.** `LIFECYCLE_CATALOG_SHA256` `c6956899947b0435e5cdd8cd77ba3121db77e3dbf4676bee11406c3baf03ec68` → **`86d26fa276ca82cd0d889a5cb9cbc3be3b94c39c2d9cb20a2f41c79e99108e30`**, while `LIFECYCLE_CONTRACT_COUNT` stays **13** and `LIFECYCLE_ARTIFACT_COUNT` stays **54** — because this leaf's catalog change is again a **consumer change only**: five `consumers` rows across the already-registered ambient-runner and generation-cases artifacts and the read-scope contract, with **no new artifact and no new contract**. The value is the one measured on this candidate by hashing the file, and the provenance paragraph above the constant now states both that shape and the reason the two modules reached the catalog at all — each quotes the real corpus key the ambient-role e2e generator's run report is written about, a path-string edge the census derives rather than one any import creates. The rule the earlier entries state is unchanged and this entry keeps it: **a catalog change must re-pin deliberately in the same change, with the counts moving with the blocks they count**, and the reason written beside the constant is what makes the re-pin auditable rather than convenient. Verification metadata is **not** advanced over unreviewed content: the body was re-read against the current source, and the code commit does not exist yet — closeout owns that stamp.

- 2026-09-18T03:15:00+00:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): recorded the **fifth deliberate re-pin of the evidence-catalog identity, and the first one where only the digest moved.** `LIFECYCLE_CATALOG_SHA256` `19ed0525cd94b57389052a4e19cf1f0dfe83e9c166783ead2598f6a4e0ce8ffa` → **`c6956899947b0435e5cdd8cd77ba3121db77e3dbf4676bee11406c3baf03ec68`** (re-measured by hashing the file), while `LIFECYCLE_CONTRACT_COUNT` stays **13** and `LIFECYCLE_ARTIFACT_COUNT` stays **54** — because this leaf's catalog change is a **consumer change only**: two `consumers` rows for `mcp/tests/test_knowledge_detection_runs.py` on the already-registered `diff_scope_test_support` and `read_scope_test_support` artifacts, no new artifact and no new contract. The body's pin paragraph now states that shape explicitly, so a successor can tell a consumer-only re-pin from a population move, and it keeps the rule the earlier entries stated: **a catalog change must re-pin deliberately in the same change, with the counts moving with the blocks they count** — and the reason written beside the constant in the source is what makes the re-pin auditable rather than convenient. Verification metadata advances to the leaf's base commit `4264dcc9` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-17T23:18:00+00:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): recorded the **fourth deliberate re-pin of the evidence-catalog identity**, moved in the same change as this leaf's catalog rows — `LIFECYCLE_CONTRACT_COUNT` 12 → **13**, `LIFECYCLE_ARTIFACT_COUNT` 53 → **54**, and `LIFECYCLE_CATALOG_SHA256` `9b057632…` → **`19ed0525cd94b57389052a4e19cf1f0dfe83e9c166783ead2598f6a4e0ce8ffa`**, measured on the frozen candidate by counting the blocks and hashing the file. The body's pin paragraph now carries the whole chain of states (`4 / 45 / 293a187f…` → … → `12 / 53 / 9b057632…` → `13 / 54 / 19ed0525…`), because a successor must be able to see that every move was deliberate. The catalog change itself is one new contract/artifact pair (`knowledge-facet-cases` for `mcp/tests/facet_test_support.py`) plus a wording-only edit to the existing `knowledge-generation-cases` row. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:148-168. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: the pin section was superseded twice more by
  sibling landings before this pass, so the card was **corrected, not annotated**. It now carries all
  **nine** deliberate re-pin records in landing order — L17's two (own-branch `563582a0…` and merged
  `e3651d6f…`) and this leaf's three (own-branch `8764ea1f…`, first merged `dca9c2f9…`, and the merged
  value at this leaf's landing `31c6983d…`, 4 contracts / 54 artifacts) — with each value marked
  correct only at its own tip and the two superseded working measurements named as retired rather than
  recorded. The count is now stated **both ways** on purpose (`re-pinned deliberately eight times …
  the nine records below`), because the earlier count-only wording was itself the cause of the
  duplicate-ordinal defect `L17-10`; a card must not paraphrase that header as a bare count.
  Verification metadata remains closeout-owned: the candidate is uncommitted.


- 2026-09-17T10:43+02:00 — 260915-CAPS-L17 curator: **the fifth deliberate re-pin, re-derived against
  the merged catalog, and the card's whole pin section corrected rather than annotated.** This leaf's
  new `mcp/tests/test_eve_effort_runtime.py` starts the shipped runtime, so it reaches three
  already-governed artifacts and each `consumers` list gained one entry
  (`mcp/tests/evidence-lifecycle.toml:650`, `:738`, `:1190`, belonging to the Node `package-lock.json`
  fixture and the eve capsule / adapter shared-support modules at `:604`, `:721`, `:1175`).
  **Nothing was registered, no row was removed and no artifact's identity moved**: the population is
  **4 contracts / 54 artifacts** — L14's three registered rows plus this leaf's three consumer entries —
  and the digest is **`e3651d6f…`**, recomputed directly from the file and equal to the constant. The
  body was rewritten from "three times" to a five-record landing-order table because the earlier
  version's narrative had been overtaken twice by sibling landings; the card now also states the two
  rules those landings taught — a pre-sync measurement is **not** a record (`563582a0…`, measured at 51
  artifacts before L14 landed, is retired), and consumer rows alone move the digest. The pin reference
  row was corrected from `:43-45` to the constants' real `:44-46` (it named `LIFECYCLE_CATALOG_SHA256`
  while its range stopped one line short of it) with the docstring's true `:47-109`. **Recorded, not
  repaired:** the constant's own docstring labels two entries "Fourth deliberate re-pin" (L14's and
  this leaf's pre-sync one) and is therefore internally inconsistent with its "five times" header —
  code text, owned by the builder. **Checker result (post-sync, verbatim).** The refusal this leaf's
  pre-sync entries recorded was resolved by its `worktree_sync`: the pair is now `leaf-candidate` /
  `acceptanceEligible:true` on code base `d8ed8c21`, and the contract-scoped `memory_quality_check` ran
  against this worktree. Headline: `ok:false`, `checklistStatus:"action-required"`,
  `coherenceStatus:"not-evaluated-quality-action-required"`, `closeoutReady:false`,
  `curatorActionableCount:1690`; census `ready-for-adjudication` (13 rows, 0 blockers, 0 unonboarded).
  This card's own contribution is one `claim_reopen` error at `:88` (`LIFECYCLE_CATALOG_SHA256` changed
  from `d8ed8c21` to the working tree) — the **D11 uncommitted-candidate signature**, since the
  constant's value is exactly what this leaf re-pinned; it is recorded, not "fixed", and the closing
  evidence is the post-closeout state of the same range. Verification metadata stays at the synced base
  `d8ed8c21`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.

- 2026-09-17T10:05+02:00 — 260915-CAPS-L15 curator: **the third deliberate re-pin, and it changed no
  population.** This leaf made `mcp/tests/test_capsule_launch_wiring.py` an importer of three governed
  artifacts through the shared test support it reaches, so only **consumer rows** moved: the digest went
  `812211e9… → 3342a249…` with the populations unchanged at 4 contracts / 51 artifacts, and nothing was
  registered, removed or re-identified. The body was corrected rather than annotated — the section
  previously described "this leaf" as L16 and the second re-pin record, so it now names all three and
  states what the third one actually changed. Added the matching invariant (a consumer row is a catalog
  change; the pin is re-derived from the file's bytes) and a row pointing at the three consumer rows.
  Verification metadata moves to this leaf's base `15fa0e2c`; the candidate is deliberately uncommitted,
  so the governed closeout stamps the real code commit and no hash or fingerprint was invented here.

- 2026-09-17T01:15:00+00:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): recorded the **second deliberate re-pin of the evidence-catalog identity** and re-derived the card's citations against the new bytes — `LIFECYCLE_CONTRACT_COUNT` 10 → **11**, `LIFECYCLE_ARTIFACT_COUNT` 51 → **52**, and `LIFECYCLE_CATALOG_SHA256` `461121ca…` → **`4cf81f10dbbd6b941c50887dca45154612e5e46b7135465823af3e6604db3747`** (measured on the frozen candidate by counting the blocks and hashing the file). The card now names the check that makes the pin real — `_assert_the_catalog_kept_its_bytes_and_identities`, which recomputes the file's digest and counts both block kinds before comparing them to the constants — and records that this leaf's catalog change is a **new contract/artifact pair** (`knowledge-diff-cases` for `mcp/tests/diff_scope_test_support.py`) **plus** two consumer rows added to the existing read-scope artifact. It also keeps the rule the L7 entry stated, in the form a successor needs: **a catalog change must re-pin deliberately in the same change, with the counts moving with the blocks they count.** Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.

- 2026-09-16T21:50:00+00:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): recorded the **evidence-catalog pin** this module carries and the deliberate re-pin this leaf made alongside its own catalog row — `LIFECYCLE_CONTRACT_COUNT` 4 → **10**, `LIFECYCLE_ARTIFACT_COUNT` 45 → **51**, and `LIFECYCLE_CATALOG_SHA256` `293a187f…` → **`461121ca16567ab056938b710b19bddb98867581dd4fe3cf7ee2645111d54369`**. The card states why the pin exists in the form a successor needs: any change to `mcp/tests/evidence-lifecycle.toml` that nobody meant becomes a hard failure, and **a catalog change must re-pin deliberately in the same change, with the counts moving with the blocks they count**. It also records that the pin's comment names the digest it supersedes, so the history of the freeze is auditable from the source rather than only from this card. Verification metadata remains empty until closeout stamps the code commit.

- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: **the catalog pin was re-derived at this leaf's own
  tip** (the second deliberate re-pin `LOCR-R26@v1` requires). Count `45 → 51`, digest
  `293a187f… → 812211e9…`, taken at `8997e184` where the catalog is 4 contracts / 51 artifacts
  (260915-CAPS-L7's landing added the fifty-first row) — never borrowed from another base, because a
  value correct for someone else's base re-reds the moment the tip moves. The pin had been stale since
  the source-line convergence merge carried the landed 260831-LOCR line's governed artifacts in without
  a re-pin, and that staleness was the single pre-existing integration failure every candidate from the
  master tip inherited. The constant's docstring now carries the second re-pin record with each
  intermediate state named, and the re-pinned integration case is green. This is a **byte contract at
  this tip only**: any later leaf that changes the catalog must re-pin again. Verification metadata
  moves to this leaf's synced base `8997e184`; the candidate is deliberately uncommitted, so the
  governed closeout stamps the real code commit and no hash or fingerprint was invented here.

- 2026-09-06T21:46:00+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:17:00+00:00 — Recorded the exact sixteen-consumer runner regression and explicit no-global-invalidation assertions; repaired shifted layer-contract citation and reference buckets.

- 2026-09-03T10:30:00+00:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): recorded the L19 ownership-vocabulary
  change — `fresh_rerun_reason` assertions became `unresolved_inputs` assertions and incomplete
  ownership now resolves to an empty test population rather than a safe-full expansion.
  Verification is pinned to the owning commit.

- 2026-09-01T09:33:00+00:00 — CCR-L11 Attempt 10 added the exact `layers.toml` ownership forcing
  case and confirmed the composed declaration matches all five literal readers without safe-full
  selection. Verification remains closeout-owned.

- 2026-08-30T20:33:39+00:00 — 260821-ARSPAWN-L5 added the source-observed exact
  `.codex/config.toml` consumer proof; an unobserved declaration cannot claim complete ownership.

- 2026-08-28T04:28:00+00:00 — PDLS wave 005 curator: expanded the memory contract to recursive static
  pytest-plugin closure, dynamic-plugin fail-closed behavior, literal module consumers, and
  path-loaded owner reachability.

- 2026-08-25T13:44:00+00:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
  requirement review. Verification remains closeout-owned.
2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **re-read all three pinned constants against the catalogue's own bytes and recorded the
tenth deliberate re-pin — the first that moves the digest alone.** This leaf registers no contract
and no artifact: it appends a consumer entry to two already-governed artifacts, so
`LIFECYCLE_CONTRACT_COUNT` stays **15** and `LIFECYCLE_ARTIFACT_COUNT` stays **65**, while
`LIFECYCLE_CATALOG_SHA256` is re-measured to
**`68a64207bd808eafd31f8c6b23856302c5ef2d150a604aa8177427e5906a1012`**, which `sha256sum
mcp/tests/evidence-lifecycle.toml` reproduces and which the two count constants agree with. The new
section above states the values, keeps `633b03ee…` as the L21 measurement it supersedes, and repeats
the known text residue in the constant's docstring — it still repeats its provenance narrative and
carries older counts — while stating that the declarations, not the prose, are the authority. The
L21 and earlier sections above are retained unchanged as the measurements of the tips that produced
them. No reference row was touched in this pass; the card's ranges into the catalogue and into the
manifest are the citation-reprojection engine's to move. The metadata block above names this leaf's
uncommitted candidate in this entry's own words, and `lastVerifiedCommitHash` /
`lastVerifiedCommitDate` are left exactly as the last real verification set them because no commit
contains this candidate. The body was changed substantively and this entry is the history record,
not a metadata-only refresh.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| **The re-pinned constants, with the counts this leaf did not move and the digest it did (`8d60a34c…` → `c676b0a0…` → `b1ed7838…` → `d2d6dc6a…`).** | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| **The source's own paragraph for the third case module: no registration, two consumer rows, counts unchanged, and the digest it replaced.** | "Twentieth deliberate re-pin (260921-ICR-L8" |mcp/tests/test_dependency_ownership_ast_helpers.py:283-283|
| **The source's own paragraph for the reach case module.** | "Nineteenth deliberate re-pin (260921-ICR-L8" |mcp/tests/test_dependency_ownership_ast_helpers.py:302-302|
| **The source's own paragraph for the movement case module, and the census finding (`missing=[…]`, `unsupported=[]`) each row was derived from.** | "Eighteenth deliberate re-pin (260921-ICR-L8" |mcp/tests/test_dependency_ownership_ast_helpers.py:321-321|
| **The six consumer entries this leaf's three modules joined: three on each of the two exact-scope consumer rows.** | "mcp/tests/test_knowledge_review_relationship_movement.py"; "mcp/tests/test_knowledge_review_relationship_reach.py"; "mcp/tests/test_knowledge_review_relationship_line.py" | mcp/tests/evidence-lifecycle.toml:1405-1441; mcp/tests/evidence-lifecycle.toml:1442-1488 |
| The existing unit-regression registry contains the three relationship modules. | "unit-regression = ["; "mcp/tests/test_knowledge_review_relationship_movement.py"; "mcp/tests/test_knowledge_review_relationship_reach.py"; "mcp/tests/test_knowledge_review_relationship_line.py" | mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/test-evidence-lanes.toml:128-128; mcp/tests/test-evidence-lanes.toml:129-129; mcp/tests/test-evidence-lanes.toml:130-130 |
| The check that recomputes the catalog's sha256 and counts both block kinds beside it, re-derived because the docstring's three new paragraphs moved it. | `_assert_the_catalog_kept_its_bytes_and_identities` |mcp/tests/test_dependency_ownership_ast_helpers.py:886-902|
| The proof that this leaf's artifact delta is empty, which is why only a consumer change could move the digest three times. | `test_production_proof_adds_no_governed_evidence_artifact` |mcp/tests/test_dependency_ownership_ast_helpers.py:818-835|

## Update History
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`, confirmed from the enclosure contract): **the Eighteenth, Nineteenth and Twentieth deliberate re-pins recorded (650 → 711 lines; the three docstring paragraphs are 60 of those lines).** Three new ordinary unit modules — the movement, reach and authored-line case modules of `ICR-R08@v1` — each joined both `consumer_scope = "exact"` rows and gained one `unit-regression` lane row; no artifact was registered and no row removed, so the counts stay 16/66 and the proof's artifact delta stays empty. The catalog was re-pinned once per module (`8d60a34c…` → `c676b0a0…` → `b1ed7838…` → `d2d6dc6a…`), and every range in this card was re-derived against the grown file rather than shifted — the rows naming `_assert_the_catalog_kept_its_bytes_and_identities` and `test_production_proof_adds_no_governed_evidence_artifact` moved by the docstring's insertion and are corrected here. **Metadata removal:** this card's candidate-reading metadata rows were removed under the developer's 2026-09-22 rule, and the history sentence that pointed at such a row was corrected in the same pass so the document no longer claims the row exists. **Reopened claims:** the three claims the checklist reopened in this document — the pins whose docstring anchors (`"Seventeenth deliberate re-pin (260921-ICR-L9"`, `"Sixteenth deliberate re-pin (260921-ICR-L14"`) and the consumer path `"mcp/tests/test_review_subject_catalogue.py"` did not exist at the older verification commits — were re-read against the constructs they now name inside the 711-line module (the retitled/numbered pin paragraphs and the two exact-scope consumer rows at `mcp/tests/evidence-lifecycle.toml:1416`/`:1456`), their wording retained, and their ranges re-derived from the anchors' real positions; the citations are current and need no further repair. No verification stamp was advanced: the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-20T06:55+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **the eleventh deliberate re-pin, and this card's pinned value is corrected.** `LIFECYCLE_CATALOG_SHA256` moved from `c499cbcc…` to `c499cbcc266088f35bd6fdde655f00579431591f02bba5c4859b72f767f65f06`, measured with `sha256sum mcp/tests/evidence-lifecycle.toml` on the delivered candidate. The reason is consumer rows only: `mcp/tests/test_worktree_sync.py` now consumes the registered `generation_test_support` fixture, whose `consumer_scope = "exact"` requires its `consumers` list to equal the source-derived consumer set, so that module **and** `mcp/tests/test_sync_parked_candidate.py` (which imports it) were appended to the list. **Nothing was registered, no artifact row was removed and no identity moved**, so `LIFECYCLE_CONTRACT_COUNT` stays 15 and `LIFECYCLE_ARTIFACT_COUNT` stays 65 — the populations this master has pinned since L28. The re-pin narrative in the module's own docstring carries this leaf as the eleventh entry, which is where a reader should look for the full reason. Before the re-pin, exactly the two ownership/evidence integration cases failed: that is the catalogue census, not a behaviour regression. Verification metadata is **advanced to the candidate's base `f79f4db7`** with the working candidate named beside it; closeout owns the committed stamp.

## 260921-ICR-L10 The Twenty-First Deliberate Re-Pin, With The Population Unchanged

`260921-ICR-L10` (`ICR-R10@v1`) re-pins `LIFECYCLE_CATALOG_SHA256` for the third time in this
series' recent leaves: the new pagination module obliged **three** exact-scope consumer rows in
`mcp/tests/evidence-lifecycle.toml`, and a governed manifest's bytes are what this digest pins. The pin
moves from `d2d6dc6a…` to `b4d4a7f9…`, and the two counts beside it are **unchanged** at sixteen
contracts and sixty-six artifacts — the re-pin records an amended row, not a new contract.

The census this module runs is what confirms it: the module registers no contract, no artifact and no new
support module, so the only obligation it created was the consumer rows, and the paragraph that carries
this leaf's account is the twenty-first in the deliberate-re-pin sequence.

## Update History
- 2026-09-23T00:30:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; production line at this leaf's base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **the twenty-first deliberate re-pin, with the population unchanged.** `LIFECYCLE_CATALOG_SHA256`
moves from `d2d6dc6a…` to `b4d4a7f9…` because this leaf's module obliged three exact-scope consumer rows
in `mcp/tests/evidence-lifecycle.toml`; the contract and artifact counts beside it are unchanged at
sixteen and sixty-six. Every row on this card that cited a manifest or catalog line was re-derived against
this candidate, because the insertions moved them. No verification stamp was advanced: nothing in this leaf is committed, so the commit/closeout stamp remains closeout's.
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

## Update History
- 2026-09-23T02:40:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): **the twenty-second deliberate re-pin, one new case module's four consumer rows, counts unchanged (`ICR-R26@v1`).** The card records the four rows and the census finding each was derived from, and states explicitly that no artifact and no contract was registered, so a later reader can tell a consumer-row re-pin from a population change. The digest moves `b4d4a7f9…` → `4d874fb54c…` while `LIFECYCLE_CONTRACT_COUNT`/`LIFECYCLE_ARTIFACT_COUNT` stay at sixteen and sixty-six. **Citation accounting:** the measured baseline check reports **zero** enforced findings for this card; its rows cite the pin constants at their own declarations, which this leaf did not move. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header already names this leaf's base, and the governed closeout owns the real stamp.
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

## Update History
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **the Twenty-third deliberate re-pin (ICR-R12@v1).** The catalog moves from the Twenty-second
digest to `4ab067e360c7807c3051ad71058c09058225f1e9155e7111da6e95c73cac0258` for one new case module's
three exact-scope consumer rows and its lane row; nothing was registered, no row removed, and the
population stays at sixteen contracts / sixty-six artifacts. **Citation accounting:** the re-pin
docstring and the rows around it were re-derived against the candidate. **Stamp accounting:** no
verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real
stamp.
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

## Update History
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee):` **the Twenty-fourth deliberate re-pin — the managed-sync case module's three newly reached consumer rows (`ICR-R22@v1`).** Three exact-scope rows gained `test_sync_parked_candidate.py` and `test_worktree_sync.py`, nothing was registered and both counts stay at sixteen and sixty-six; the card also records that the constant's base value `81a518b5…` came from commit `3103e114` (`260921-ICR-L21`), which re-pinned without adding a narrative entry, so the docstring's newest entry at this base is the Twenty-third's `4ab067e3…`. **Citation-shift consequence:** this entry is inserted in the constant's docstring at `:49`, so every line below it in this module reads lower than the accounts above record it — the three entries together move the module 782 → 842 lines and every base line from `:49` onward by **+60**. **Stamp accounting:** no verification stamp was advanced — the header's verification pair names this leaf's recorded base `e605822e` because nothing in this leaf is committed, and the governed closeout owns the real stamp.

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

## Update History
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee):` **the Twenty-fifth deliberate re-pin — the module split's own closure change (`ICR-R22@v1`, fix round 1).** Three rows lost `test_sync_parked_candidate.py` and `test_worktree_sync.py` and gained `test_review_sync_rebinding.py`, while `merge_case_test_support.py` kept both and gained the new module; no artifact or contract was registered and the population stays at sixteen contracts / sixty-six artifacts. **Citation-shift consequence:** this entry is inserted in the constant's docstring at `:67`, above the Twenty-fourth's, so it is one of the three insertions that move every line below `:48` by **+60** (module extent 782 → 842 lines) and the ranges citing `:633`, `:690`, `:703` and `:723` in the accounts above read `:693`, `:750`, `:763` and `:783` on this candidate. **Stamp accounting:** no verification stamp was advanced — the header's verification pair names this leaf's recorded base `e605822e` because nothing in this leaf is committed, and the governed closeout owns the real stamp.

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

## Update History
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee):` **the Twenty-sixth deliberate re-pin — the read-side cases' own module (`ICR-R22@v1`, fix round 3).** The new `test_review_sync_movement_read.py` gained its own path on the same four exact-scope rows, no artifact or contract was registered, and the live constant reads `d07c2f9d…` with the counts unchanged at sixteen / sixty-six. This section's own value paragraph above was corrected in place from `3e9105c2…` at 1681 lines to the live pair. **Citation-shift consequence:** the three docstring insertions at `:49`, `:67` and `:88` moved every line below them — the module is 782 → 842 lines and every base line from `:49` onward reads **+60** (`:633` → `:693`, `:690` → `:750`, `:703` → `:763`, `:723` → `:783`), so every range on this card below the docstring reads lower than its account records it; the curator repairs those ranges per row, separately. **Stamp accounting:** no verification stamp was advanced — the header's verification pair names this leaf's recorded base `e605822e` because nothing in this leaf is committed, and the governed closeout owns the real stamp.

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

## Update History

- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): **the Twenty-ninth deliberate re-pin, with the
  population unchanged.** `LIFECYCLE_CATALOG_SHA256` (`:46-46`) moved from the Twenty-eighth value
  `97ae9cbefd756a6def6e8048baa2066beef2c06300f73eb93b4ab23b4ebf6879` to
  `f3dd258c161eee057edee9bdb7b7a4874220c8a4201c04a516dc146c14526589`, measured with
  `sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate, and the module's own
  docstring gained the Twenty-ninth re-pin note (`:49-65`) in the established style. The delta it
  records is exactly one consumer path, so **`LIFECYCLE_CONTRACT_COUNT` stays 16 and
  `LIFECYCLE_ARTIFACT_COUNT` stays 66** (`:44-45`) — nothing was registered, no row was removed and no
  artifact's identity moved. **No verification stamp was advanced** — the candidate is uncommitted and
  the governed closeout owns the real code and memory commits.
- 2026-09-23T22:20:00+02:00 — 260921-ICR-L31 curator (uncommitted change set on `ar/260921-icr-l31`, base `4c000b11c5243e4a8e77c08e87984fff00c1d94b`): ``LIFECYCLE_CATALOG_SHA256`` re-pinned twice (Twenty-seventh ``caf1b9ee…`` → ``b1c38ed8…``, Twenty-eighth ``b1c38ed8…`` → ``23dd7c0f…``) for the two consumer rows the leaf's three case modules gained, with contracts and artifacts unchanged at sixteen and sixty-six (`ICR-R31@v1`). Body updated with the real section above; no stamp advanced beyond the leaf's base plus the working-tree delta.


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
