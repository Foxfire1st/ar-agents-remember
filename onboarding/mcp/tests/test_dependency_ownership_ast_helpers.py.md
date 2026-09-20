# mcp/tests/test_dependency_ownership_ast_helpers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dependency_ownership_ast_helpers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T00:31+02:00 |
| lastVerifiedCommitHash |  `0da444b3b2b61f6a86fa4076b283c305db025d22`|
| lastVerifiedCommitDate |  2026-09-20T02:38:15+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted change set; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
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
| eleventh | **`260915-KS-L31` (2026-09-19) — the value the constants carry at this candidate** | **15 / 65** (unchanged) | `25b00f88…` (the L23 tip, recorded in its own paragraph above) → **`825abfd65a17899cf1334d6191bd944d1f618347db7e599a44629f2bec910ef2`** | **consumer rows only, two of them** — both appended to the tail of `mcp/tests/merge_case_test_support.py`'s exact list: `mcp/tests/test_worktree_sync.py`, which consumes the harness directly for the CYCLE-02 knowledge-dataset conflict case, and `mcp/tests/test_sync_parked_candidate.py`, which reaches it transitively through its existing import of `test_worktree_sync` and was not itself edited |

**The module also carries the evidence catalog's pinned identity, and that pin is a deliberate one.** The three
constants `LIFECYCLE_CONTRACT_COUNT`, `LIFECYCLE_ARTIFACT_COUNT` and `LIFECYCLE_CATALOG_SHA256` state the
catalog's declared shape and its exact bytes, so a change to `mcp/tests/evidence-lifecycle.toml` that nobody meant
is a **hard failure** rather than a silent inventory drift. **The current value is the three constants' own
reading on this candidate and nothing else: `LIFECYCLE_CONTRACT_COUNT = 15`,
`LIFECYCLE_ARTIFACT_COUNT = 65` and `LIFECYCLE_CATALOG_SHA256` pinned to
`825abfd65a17899cf1334d6191bd944d1f618347db7e599a44629f2bec910ef2`, which `sha256sum
mcp/tests/evidence-lifecycle.toml` reproduces on this worktree** — **re-pinned by both leaves, so this
candidate's value is the merge of the two re-pins**: `260915-KS-L30` appended one consumer row on
`mcp/tests/snapshot_lifecycle_test_support.py` and `260915-KS-L31` appended two on
`mcp/tests/merge_case_test_support.py`, and both counts stay **15 / 65** because neither added a contract
or an artifact. The value is correct only at this candidate's tip. The value
this paragraph carried before it was `6ec7eb0d33e91c148b25ed64c6b791664446082bdf419bf511635f4ca3cbdd75`
(the constant at this leaf's base, which the source's own docstring attributes to L28's
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

**The pinned catalog identity was re-pinned to this candidate's measurement.** This module pins the evidence catalogue's contract and artifact counts and the digest of `mcp/tests/evidence-lifecycle.toml`. The leaf registers one contract and one artifact, so the pins moved with them. **That sentence described `260915-KS-L12`'s leaf, whose pair took the pins to 14 contracts and 55 artifacts; the leaf that owns the pair now is `260915-KS-L21`, and the constants it moved read 15 contracts and 65 artifacts** with the digest this candidate's manifest actually hashes to (`825abfd6…`, the merged candidate's measurement; `260915-KS-L30` re-pinned it from L28's `6ec7eb0d…` and `260915-KS-L31` added the merge-case consumer rows to it). The pins are measurements rather than constants: the module's own docstring carries the re-pin precedent, and a leaf that registers its own artifact advances both rather than weakening the assertion. A stale pin fails loudly, which is the point — the alternative is a catalog nobody re-measures.

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
**`825abfd65a17899cf1334d6191bd944d1f618347db7e599a44629f2bec910ef2`**, recomputed directly from the
file at this tip (`sha256sum mcp/tests/evidence-lifecycle.toml`) and equal to the constant. **The
docstring beside the constants has moved since the sentence above was written, and the residue is narrower
than it says:** its opening paragraph now reads "fifteen contracts and sixty-five artifacts", and neither
the "five times" header nor the duplicated "Fourth deliberate re-pin" label this card used to report is in
the file any more; what survives are older branch counts further down its provenance narrative (`:233`
reads "fourteen contracts and fifty-five artifacts" of an earlier branch and `:254` reads "thirteen and
fifty-four … fourteen and sixty-four" of the merged base it landed against). **One residue is new at this
candidate:** the docstring's first paragraph still presents L28's `6ec7eb0d…` as "the value this line
carries", while the line now carries this candidate's `825abfd6…` — the constants, not the prose, are the
authority, and the text is the owning builder's to correct. The reading a reader should
take is the constants' own — 15 / 65 / `825abfd6…` — and the remaining residue is recorded here for the
owning builder rather than repaired by this card, exactly as the L16 record below treats the same class of
residue.

**`260915-KS-L31` re-pinned the digest again, with both counts unmoved.** The leaf's catalog change is the
pure consumer change this registry's own doctrine describes: two rows appended to the tail of
`mcp/tests/merge_case_test_support.py`'s exact list, one because `mcp/tests/test_worktree_sync.py` now
builds its knowledge-dataset conflict scenario through that harness and one because
`mcp/tests/test_sync_parked_candidate.py` reaches the harness transitively through its existing import of
`test_worktree_sync`. `sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate reproduces
**`825abfd65a17899cf1334d6191bd944d1f618347db7e599a44629f2bec910ef2`**, which is the value the constant
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
| Repository inputs reach their supported consumers. | `test_repository_inputs_reach_their_supported_consumers` | mcp/tests/test_dependency_ownership_ast_helpers.py:289-309 |
| **The evidence catalog's pinned shape and bytes, and the deliberate re-pin this leaf made in the same change as its catalog rows — whose value at this candidate is 15 contracts / 65 artifacts and `825abfd6…`, the merged measurement of the `260915-KS-L30` and `260915-KS-L31` re-pins.** | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-46; mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| **The check that makes the pin real: the file's bytes recomputed and both block kinds counted before either is compared.** | `_assert_the_catalog_kept_its_bytes_and_identities` | mcp/tests/test_dependency_ownership_ast_helpers.py:380-396 |
| The closure check over the governed inventory, and the lane-membership check. | `_assert_the_governed_inventory_is_closed`; `_assert_the_proof_is_selected_by_the_lane_manifest` | mcp/tests/test_dependency_ownership_ast_helpers.py:360-377; mcp/tests/test_dependency_ownership_ast_helpers.py:347-357 |
| **The contract and artifact blocks the pin counts, added by this leaf, and the consumer list its sibling artifact gained.** | "id = \"knowledge-diff-cases\"" | mcp/tests/evidence-lifecycle.toml:60-60 |
| The catalog pin constants, and the re-pin narrative the docstring carries beside them — **stale on this candidate, as the L21 record below says: it still reads "fourteen contracts and sixty-four artifacts".** | `LIFECYCLE_SCHEMA`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-43; mcp/tests/test_dependency_ownership_ast_helpers.py:44-44; mcp/tests/test_dependency_ownership_ast_helpers.py:45-45; mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:47-109 |
| The three consumer entries the `260915-CAPS-L17` re-pin added to three governed-artifact rows, the entire reason the digest moved at that re-pin. | "mcp/tests/fixtures/repository_profiles/node/package-lock.json"; "mcp/tests/eve_capsule_test_support.py"; "mcp/tests/eve_adapter_test_support.py" | mcp/tests/evidence-lifecycle.toml:660-660; mcp/tests/evidence-lifecycle.toml:1455-1455; mcp/tests/evidence-lifecycle.toml:1477-1477 |
| The three artifacts those rows belong to, each an already-governed row rather than a new registration. | "mcp/tests/diff_scope_test_support.py"; "mcp/tests/read_scope_test_support.py" | mcp/tests/evidence-lifecycle.toml:604-604; mcp/tests/evidence-lifecycle.toml:721-721; mcp/tests/evidence-lifecycle.toml:1175-1175; mcp/tests/evidence-lifecycle.toml:75-75; mcp/tests/evidence-lifecycle.toml:61-61; mcp/tests/evidence-lifecycle.toml:66-66 |
| The population the pin names, re-derived at this candidate's own tip — **15 contracts and 65 artifacts**, the values the constants below carry. | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-44; mcp/tests/test_dependency_ownership_ast_helpers.py:45-45; mcp/tests/evidence-lifecycle.toml:1-1641 |
| The three consumer entries the `260915-CAPS-L15` re-pin added to three governed-artifact rows, whose shape the `260915-CAPS-L17` entries repeat. | "mcp/tests/curator_coherence_test_support.py"; "mcp/tests/fixtures/repository_profiles/node/package-lock.json"; "mcp/tests/fixtures/codex_app_server_model_page.json" | mcp/tests/evidence-lifecycle.toml:385-385; mcp/tests/evidence-lifecycle.toml:660-660; mcp/tests/evidence-lifecycle.toml:1552-1552 |
| **The contract and artifact blocks the pin counts, added by this leaf, and the consumer list its sibling artifact gained.** | "id = \"knowledge-diff-cases\"" | mcp/tests/evidence-lifecycle.toml:60-60 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |
| **The evidence catalog's pinned shape and bytes, the deliberate re-pin this leaf made in the same change as its consumer rows, and the provenance paragraph that records the consumer-only shape of that change.** | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-50; mcp/tests/test_dependency_ownership_ast_helpers.py:69-82 |

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
| The appended artifact: the census fixture, with its declared kind, authority, category, fidelity, cadence, introducing leaf, lifetime, replacement contract and exact consumer list. | `"mcp/tests/migration_census_test_support.py"`; `"contract:migration-census-cases"` | mcp/tests/evidence-lifecycle.toml:1613-1630 |

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
source's own text) → `73cdd218…` (L30's re-pin, correct only at L30's own tip) → `825abfd6…` (the merged candidate, this card's current value, recorded in the L31 re-pin section below), each correct only at its own tip.

## Update History
- 2026-09-20T02:25+02:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **cleared the three enforced `citation_anchor_absent_from_range` rows this card carried — the same three consumer entries the 01:37 pass repointed, moved one more line by the sync onto the master line.** The 01:37 pass read them at `mcp/tests/evidence-lifecycle.toml:1454-1454`, `:1476-1476` and `:1551-1551` on the pre-sync catalogue; the merged catalogue (this leaf's own `mcp/tests/evidence-lifecycle.toml` change and L30's re-pin, resolved by re-measuring the digest at 15 contracts / 65 artifacts) puts each named path's own line at **1455** (`"mcp/tests/eve_capsule_test_support.py"` in that artifact's `path =` line), **1477** (`"mcp/tests/eve_adapter_test_support.py"`) and **1552** (`"mcp/tests/fixtures/codex_app_server_model_page.json"`). Each of the three ranges now cites the line that carries its own named path verbatim; the sibling ranges in both rows (`:660-660` for the package-lock fixture, `:385-385` for the curator-coherence support module) were verified current and are unchanged, as are every claim, anchor and row. Claim wording and anchors are untouched, no range was dropped to silence a finding, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits. No commits.
- 2026-09-20T01:37+02:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): range repair only; every claim's wording, anchor set and row kept. Three reference rows citing this module and the governed catalogue were re-derived against the file as it stands on this candidate. The closure/lane-membership row had been left on a pre-move projection (`:191-194; :178-181; :290-320`) that names the two calls' call sites and an unrelated test, not their declarations; it now cites each declaration's own extent, `mcp/tests/test_dependency_ownership_ast_helpers.py:360-377` for `_assert_the_governed_inventory_is_closed` and `:347-357` for `_assert_the_proof_is_selected_by_the_lane_manifest`. The two catalogue rows the L23 residue entry had already repointed once moved again when the catalogue's own consumer lists grew: the `260915-CAPS-L17` row's `eve_capsule_test_support.py` and `eve_adapter_test_support.py` entries now stand at `mcp/tests/evidence-lifecycle.toml:1454-1454` and `:1476-1476` (was `:1449-1449`/`:1471-1471`), and the `260915-CAPS-L15` row's `codex_app_server_model_page.json` entry now stands at `mcp/tests/evidence-lifecycle.toml:1551-1551` (was `:1546-1546`); each is the line that carries the named path verbatim in its artifact's `consumers` list, and the sibling ranges in both rows were already correct and are unchanged. No verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-20T01:27+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared all three enforced `citation_prose_not_in_cit_form` rows this card carried, without changing what the sentence claims.** All three fired on the same sentence — the digest chain in the `260915-KS-L30` re-pin section — whose three entries read `` `633b03ee…` (L21) ``, `` `68a64207…` (L22) `` and `` `25b00f88…` (L23) ``: the checker pairs a code span with a following parenthesized `L<digits>` and reads it as the superseded `X (L47)` citation spelling. A `cit:` rewrite is not available honestly here, and this is why: the three anchors are *leaf labels*, not line ranges (the same repository uses `(L4)` as leaf shorthand, which the checker accepts); and the digests are historical catalogue identities that exist NOWHERE in the tree (only the current `73cdd218…` is in the source, at `mcp/tests/test_dependency_ownership_ast_helpers.py:46`), so any `cit:` form would have to name an anchor no range can hold — three new enforced `citation_anchor_absent_from_range` rows in place of three prose rows. The cure applied is therefore the one that states the same fact unambiguously: each of the three parentheticals now carries a comma and the qualifier this card's own sections give that leaf's re-pin — `(L21, the census leaf, the first re-pin since L11 that moved both counts)`, `(L22, bytes only)`, `(L23, four consumer rows)` — which is the form the chain's own last two entries already use (`(L28, recorded here from the source's own text)`, `(L30, this candidate)`). No digest, arrow, leaf label or claim was changed, no `cit:` citation was added or removed, and the chain's meaning is unchanged. Reviewed against the working candidate `ar/260915-ks-l30-ar`; no commit exists for these bytes and the commit stamp is not advanced.
- 2026-09-19T23:20+00:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **the tenth-plus re-pin, counts unmoved and the digest re-measured.** The leaf's catalog change is a pure consumer change — two rows appended to `mcp/tests/merge_case_test_support.py`'s exact list, one direct (`mcp/tests/test_worktree_sync.py` now builds its knowledge-dataset conflict scenario through the harness) and one transitive (`mcp/tests/test_sync_parked_candidate.py` reaches it through its existing import of `test_worktree_sync`) — so `LIFECYCLE_CONTRACT_COUNT` and `LIFECYCLE_ARTIFACT_COUNT` still read 15 and 65 while `LIFECYCLE_CATALOG_SHA256` moved to `f786c15749667cbd90797672cce4a92026b7b21ce4b773daa4eb3cb37e01e6c5`, reproduced with `sha256sum` on this candidate. The card's re-pin table gained its eleventh row, the two paragraphs that still presented `25b00f88…` as *this candidate's* value were corrected to name the L23 tip they describe, and the transitive row is recorded as the shape a reader should carry forward rather than as an oddity. Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-19T22:49:08+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:289-309. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:49:08+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:380-396. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 3 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `mcp/tests/eve_adapter_test_support.py`; `mcp/tests/eve_capsule_test_support.py`; `mcp/tests/fixtures/codex_app_server_model_page.json`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): re-read the three pinned constants against the catalogue's bytes and recorded this candidate's value: **`LIFECYCLE_CONTRACT_COUNT = 15`**, **`LIFECYCLE_ARTIFACT_COUNT = 65`** and **`LIFECYCLE_CATALOG_SHA256 = 73cdd2183e153af752773e8a4c6076e5e2eb7053d9e0ce5fa6538a69c907cefe`**, which `sha256sum mcp/tests/evidence-lifecycle.toml` reproduces and which the constant carries (was `6ec7eb0d…` at this leaf's base, L28's value by the source's own docstring). The re-pin is **bytes-only and consumer-only**: one row appended to the tail of `mcp/tests/snapshot_lifecycle_test_support.py`'s `consumers` list for `mcp/tests/test_knowledge_curator_ingest_list.py`, because the CYCLE-01 continuity case imports `build_case`/`create`/`write_record` to get a real candidate database to fork; no contract and no artifact was added, so both counts stay where they were. Three current-value statements in `### Logic` were corrected rather than carried — the "current value" paragraph's digest and its attribution, the "(`25b00f88…`)" clause, and the "value at this candidate" paragraph — and the docstring-residue claim was corrected against the file as it now stands: its opening paragraph still presents L28's `6ec7eb0d…` as "the value this line carries" while the line carries this leaf's digest, which is recorded for the owning builder rather than edited here. Two reference rows whose anchors this leaf's citation pass had left on pre-move ranges were re-cited to their constructs' own extents (the closure and lane-membership helpers, `:347-357` and `:360-377`), the pinned-population row's catalog extent was re-measured (`:1-1637` → `:1-1641`), and the constants' rows now cite `:43-46` / `:44-46`. The metadata block's `lastUpdated` names this leaf's pass and **the commit fields are untouched** — the change is uncommitted and closeout owns the stamp.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `test_repository_inputs_reach_their_supported_consumers` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:289-309. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `_assert_the_catalog_kept_its_bytes_and_identities` repointed to mcp/tests/test_dependency_ownership_ast_helpers.py:380-396. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:53:32+00:00: 260915-KS-L23 residue clearance (seat A): re-read the three `mcp/tests/evidence-lifecycle.toml` reference rows whose ranges this leaf's appended consumer rows had moved, and repointed each to the construct its anchors name on this candidate. The `260915-CAPS-L17` consumer-entry row's three anchors (`mcp/tests/fixtures/repository_profiles/node/package-lock.json`; `mcp/tests/eve_capsule_test_support.py`; `mcp/tests/eve_adapter_test_support.py`) were cited as `:604-655; :724-741; :1178-1193; :1427-1434; :1449-1456; :1437-1437; :1459-1459; :1438-1438; :1460-1460; :659-659; :1442-1442; :1464-1464; :1444-1444; :1466-1466`, which now hold the `gate_certification_evidence` consumer list's tail, the `dispatch_brief` row and the evidence-cases row rather than those three artifacts, and now read `:660-660; :1449-1449; :1471-1471` — each artifact row's own `path` line, the row the consumer entry belongs to. The `260915-CAPS-L15` row's three anchors (`mcp/tests/curator_coherence_test_support.py`; `mcp/tests/fixtures/repository_profiles/node/package-lock.json`; `mcp/tests/fixtures/codex_app_server_model_page.json`) were cited as `:329-351; :603-625; :1252-1267; :373-380; :648-655; :1524-1531; :1534-1534; :1535-1535; :384-384; :659-659; :1539-1539; :1541-1541`, a pre-move projection whose `:384-384` and `:659-659` still land on the `[[artifact]]` headers one line above each named row, and now read `:385-385; :660-660; :1546-1546`. The pinned-population row's file extent was re-measured against the file as it stands on this candidate: `mcp/tests/evidence-lifecycle.toml:1-1630` -> `mcp/tests/evidence-lifecycle.toml:1-1637`. Every pre-move range is recorded here rather than deleted; no anchor, claim, row or range was removed, no claim wording was changed to fit a range, and no row outside this residue was touched. Verification stamp not advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T19:34+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): re-read the three pinned constants against the catalogue's bytes and recorded this candidate's value: **`LIFECYCLE_CONTRACT_COUNT = 15`**, **`LIFECYCLE_ARTIFACT_COUNT = 65`** and **`LIFECYCLE_CATALOG_SHA256 = 25b00f8832420b705495931c3a04ad13a9bfe83e367a97c4a854b36030071e30`**, which `sha256sum mcp/tests/evidence-lifecycle.toml` reproduces and which the constants carry. The re-pin is **bytes-only**: no contract and no artifact was added, and the four appended consumer rows item 13 and the item-16 case produced are the whole change, each appended to the tail of its `consumers` list so that no other row of the catalogue moved. Three current-value statements in `### Logic` were corrected rather than carried — the "current value" paragraph's digest and its attribution, the "value at this candidate" paragraph, and the clause naming the digest this candidate hashes to — and the docstring-residue claim was corrected against the file as it now stands (its opening paragraph reads fifteen contracts and sixty-five artifacts; the "five times" header and the duplicated "Fourth deliberate re-pin" label are gone; the older branch counts survive at `:233` and `:254`). The re-pin ordinal problem is recorded, not re-derived: the table ends at `tenth` while the L22 section also calls itself the tenth, so the new section names the values by leaf. The metadata block's `reviewedWorkingCandidate` row now names this leaf's candidate and **the commit fields are untouched** — the change is uncommitted and closeout owns the stamp.
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
uncommitted candidate in `reviewedWorkingCandidate`, and `lastVerifiedCommitHash` /
`lastVerifiedCommitDate` are left exactly as the last real verification set them because no commit
contains this candidate. The body was changed substantively and this entry is the history record,
not a metadata-only refresh.
