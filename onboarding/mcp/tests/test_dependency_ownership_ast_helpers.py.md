# mcp/tests/test_dependency_ownership_ast_helpers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dependency_ownership_ast_helpers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:43+02:00 |
| lastVerifiedCommitHash | `933b011bdc07eb2ebed0fa64ea3afc019f46b2f5` |
| lastVerifiedCommitDate | 2026-09-17T10:57:11+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l17-ar` uncommitted source; base `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` (synced onto L14's landing) |
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

**The catalog pin is a byte contract at one tip, and it has now been re-pinned deliberately five
times.** `LIFECYCLE_ARTIFACT_COUNT` and `LIFECYCLE_CATALOG_SHA256` pin
`mcp/tests/evidence-lifecycle.toml` by population and digest, and `LOCR-R26@v1`'s doctrine is that any
further catalog change must re-pin them **deliberately**, at its own tip, with the reason recorded. The
value at this candidate is **4 contracts / 54 artifacts** and
**`e3651d6f3ae12a7f52933a0a0e75d3eb3618a0ce18def301467a4138890dcaeb`**, recomputed directly from the
file this pass (`sha256sum mcp/tests/evidence-lifecycle.toml`) and equal to the constant.

The history the five records carry, in landing order — each value correct **only** at its own tip:

| Re-pin | Leaf / when | Population | Digest | What moved |
| --- | --- | --- | --- | --- |
| first | R16 proof landing (`5b7a84f2`) | post-registration | `a9d83c37…` | the two `LOCR-L04` handoff support modules registered under the amended catalog-freeze clause; the proof's own artifact delta stayed empty |
| second | `260915-CAPS-L16` (2026-09-16) | 45 → **51** | `293a187f… → 812211e9…` | `260915-CAPS-L7`'s landing added the fifty-first governed artifact row; the pin had been stale since the source-line convergence merge carried the landed 260831-LOCR line's artifacts in without a re-pin (defect **D10**, the one pre-existing integration failure every master-tip candidate inherited) |
| third | `260915-CAPS-L15` (2026-09-17) | **51** (unchanged) | `812211e9… → 3342a249…` | **consumer rows only** — `mcp/tests/test_capsule_launch_wiring.py` became an importer of three governed artifacts through shared test support |
| fourth | `260915-CAPS-L14` (2026-09-17) | 51 → **54** | `3342a249…`-era → `5e938c85…` | **three NEW artifacts registered** for the fresh-user acceptance harness under `scripts/e2e_harness/`, each with its own source-derived consumers and an executable `node:` replacement; `mcp/tests/test_fresh_user_harness.py` answers for all three |
| fifth | **`260915-CAPS-L17` (2026-09-17) — this leaf** | **54** (unchanged) | `5e938c85… → e3651d6f…` | **consumer rows only again** — `mcp/tests/test_eve_effort_runtime.py` starts the shipped runtime and therefore reaches three already-governed artifacts |

**The fifth re-pin is the one this card was corrected for, and the "merged" qualifier is the whole
point.** L14 landed first, so this leaf's value is re-derived against the **merged** artifact set —
L14's three new rows *plus* this leaf's three consumer entries — and it is therefore **neither** L14's
`5e938c85…` **nor** the `563582a0…` this leaf measured before the sync at 51 artifacts. That pre-sync
value was a **superseded working measurement, not a record**: it was never correct at any committed
tip once L14 landed, and the leaf's `worktree_sync` retired it. Nothing was registered by this leaf, no
row was removed and no artifact's identity moved: the catalog's only new bytes are three consumer
entries, and the population stayed at 4 contracts / 54 artifacts.

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
| Repository inputs reach their supported consumers. | `test_repository_inputs_reach_their_supported_consumers` | mcp/tests/test_dependency_ownership_ast_helpers.py:79-79 |
| The catalog pin constants, and the docstring carrying all five deliberate re-pin records beside them. | `LIFECYCLE_SCHEMA`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-43; mcp/tests/test_dependency_ownership_ast_helpers.py:44-44; mcp/tests/test_dependency_ownership_ast_helpers.py:45-45; mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:47-109 |
| The three governed-artifact consumer rows **this** leaf added, which are the entire reason the digest moved at this tip. | `consumers` | mcp/tests/evidence-lifecycle.toml:650-650; mcp/tests/evidence-lifecycle.toml:738-738; mcp/tests/evidence-lifecycle.toml:1190-1190 |
| The three artifacts those rows belong to, each an already-governed row rather than a new registration. | `path` | mcp/tests/evidence-lifecycle.toml:604-604; mcp/tests/evidence-lifecycle.toml:721-721; mcp/tests/evidence-lifecycle.toml:1175-1175 |
| The population the pin names, re-derived at this candidate's own tip. | `[[artifact]]`; `[[contract]]` | mcp/tests/evidence-lifecycle.toml |
| The consumer rows the previous leaf added, whose shape this leaf's three entries repeat. | `consumers` | mcp/tests/evidence-lifecycle.toml:351-351; mcp/tests/evidence-lifecycle.toml:624-624; mcp/tests/evidence-lifecycle.toml:1257-1257 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

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

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Recorded the exact sixteen-consumer runner regression and explicit no-global-invalidation assertions; repaired shifted layer-contract citation and reference buckets.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): recorded the L19 ownership-vocabulary
  change — `fresh_rerun_reason` assertions became `unresolved_inputs` assertions and incomplete
  ownership now resolves to an empty test population rather than a safe-full expansion.
  Verification is pinned to the owning commit.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 added the exact `layers.toml` ownership forcing
  case and confirmed the composed declaration matches all five literal readers without safe-full
  selection. Verification remains closeout-owned.

- 2026-08-30T22:33:39+02:00 — 260821-ARSPAWN-L5 added the source-observed exact
  `.codex/config.toml` consumer proof; an unobserved declaration cannot claim complete ownership.

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: expanded the memory contract to recursive static
  pytest-plugin closure, dynamic-plugin fail-closed behavior, literal module consumers, and
  path-loaded owner reachability.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
