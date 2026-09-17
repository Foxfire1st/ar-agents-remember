# mcp/tests/test_dependency_ownership_ast_helpers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dependency_ownership_ast_helpers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:05+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l15-ar` uncommitted source (17 dirty paths); base `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
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

**The catalog pin is a byte contract at one tip, and it has now been re-pinned deliberately three
times.** `LIFECYCLE_ARTIFACT_COUNT` and `LIFECYCLE_CATALOG_SHA256` pin
`mcp/tests/evidence-lifecycle.toml` by population and digest, and `LOCR-R26@v1`'s doctrine is that any
further catalog change must re-pin them **deliberately**, at its own tip, with the reason recorded. The
pin had fallen behind the file: at the convergence merge the catalog already read 4 contracts / 50
artifacts while the pin still said 45, because the merge carried the landed 260831-LOCR line's governed
artifacts in without a re-pin, and 260915-CAPS-L13 then moved the file again. That stale pin was the
single pre-existing integration failure every candidate cut from the master tip inherited — not any
leaf's finding. 260915-CAPS-L16 re-derived it at its own tip (`8997e184`, where the catalog is **4
contracts / 51 artifacts** because 260915-CAPS-L7's landing added the fifty-first row), re-pinning
count `45 → 51` and digest `293a187f… → 812211e9…`.

**The third deliberate re-pin is `260915-CAPS-L15`'s, and it changed no population.** This leaf added
**consumer rows only** — `mcp/tests/test_capsule_launch_wiring.py` became an importer of three governed
artifacts through the shared test support it reaches — so the populations are unchanged at **4
contracts / 51 artifacts** and the digest moved `812211e9… → 3342a249…`. Nothing was registered, no row
was removed, and no artifact's identity moved: the constant's docstring carries the third record, naming
what actually changed (consumer proofs, not the inventory), which is the same shape 260915-CAPS-L7 used
when its own module became a consumer. The value is re-derived at this leaf's tip (`15fa0e2c` plus its
own dirty candidate), never borrowed from another base.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No inferred full-suite population repairs an ownership gap. This retained test does not separately exercise every old pytest-plugin AST form.

- **A pin correct for someone else's base re-reds the moment the tip moves.** Whoever changes the
  catalog last pins the value at its own tip; it is re-derived, never borrowed, and a leaf that edits
  the catalog without re-pinning hands the next candidate a red.
- **The re-pin is a byte contract, not a closure.** The pinned value is correct at this tip and only at
  this tip: any later leaf that changes `mcp/tests/evidence-lifecycle.toml` must re-pin again. This
  leaf's own re-pin is the proof: consumer rows alone moved the digest, and the populations stayed put.
- **A consumer row is a catalog change.** Registering, removing or re-identifying an artifact is not
  what moves the digest by itself — an importer reaching a governed artifact through shared test support
  does too, which is why the pin is re-derived from the file's bytes rather than maintained by hand.

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
| The catalog pin, and the three deliberate re-pin records beside it — the third being this leaf's consumer-rows-only re-derivation, which left the populations unchanged. | `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-45; mcp/tests/test_dependency_ownership_ast_helpers.py:47-78 |
| The consumer rows this leaf added, which are the entire reason the digest moved. | `consumers` | mcp/tests/evidence-lifecycle.toml:351-351; mcp/tests/evidence-lifecycle.toml:624-624; mcp/tests/evidence-lifecycle.toml:1257-1257 |
| The population the pin names, re-derived at this leaf's own tip. | `[[artifact]]`; `[[contract]]` | mcp/tests/evidence-lifecycle.toml |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

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
