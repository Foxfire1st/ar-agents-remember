# mcp/tests/test_dependency_ownership_ast_helpers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dependency_ownership_ast_helpers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T05:15+02:00 |
| lastVerifiedCommitHash | `65e3791bce458eb6265f752889435a1bcaac5f2e` |
| lastVerifiedCommitDate | 2026-09-18T06:16:59+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l14` uncommitted source; base `4264dcc9decf50e64c863e9c6526ea09117be71b` |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Repository-input ownership discovery without broadening test selection.

## Code Commentary

### Logic

An explicitly supported input with no consumers remains complete with a verified no-consumer decision. Unknown input is incomplete. A declared consumer is selected without global invalidation and carries the declared-consumer reason.

**The module also carries the evidence catalog's pinned identity, and that pin is a deliberate one.** The three
constants `LIFECYCLE_CONTRACT_COUNT`, `LIFECYCLE_ARTIFACT_COUNT` and `LIFECYCLE_CATALOG_SHA256` state the
catalog's declared shape and its exact bytes, so a change to `mcp/tests/evidence-lifecycle.toml` that nobody meant
is a **hard failure** rather than a silent inventory drift. `260915-KS-L11` moved all three in the same change as
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
same change**, and that the counts must move with the blocks they count. The pin's own verification is the module's
`_assert_the_catalog_kept_its_bytes_and_identities`, which recomputes the file's sha256 and counts both block
kinds before comparing them to the three constants.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No inferred full-suite population repairs an ownership gap. This retained test does not separately exercise every old pytest-plugin AST form.

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
| Repository inputs reach their supported consumers. | `test_repository_inputs_reach_their_supported_consumers` | mcp/tests/test_dependency_ownership_ast_helpers.py:72-91 |
| **The evidence catalog's pinned shape and bytes, and the deliberate re-pin this leaf made in the same change as its catalog rows.** | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-65 |
| **The check that makes the pin real: the file's bytes recomputed and both block kinds counted before either is compared.** | `_assert_the_catalog_kept_its_bytes_and_identities` | mcp/tests/test_dependency_ownership_ast_helpers.py:162-178 |
| The closure check over the governed inventory, and the lane-membership check. | `_assert_the_governed_inventory_is_closed`; `_assert_the_proof_is_selected_by_the_lane_manifest` | mcp/tests/test_dependency_ownership_ast_helpers.py:142-159; mcp/tests/test_dependency_ownership_ast_helpers.py:129-139 |
| **The contract and artifact blocks the pin counts, added by this leaf, and the consumer list its sibling artifact gained.** | "id = \"knowledge-diff-cases\"" | mcp/tests/evidence-lifecycle.toml:1253-1253 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

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

## Update History
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/evidence-lifecycle.toml:1252-1252` -> `mcp/tests/evidence-lifecycle.toml:1253-1253`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-18T05:15+02:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): recorded the **fifth deliberate re-pin of the evidence-catalog identity, and the first one where only the digest moved.** `LIFECYCLE_CATALOG_SHA256` `19ed0525cd94b57389052a4e19cf1f0dfe83e9c166783ead2598f6a4e0ce8ffa` → **`c6956899947b0435e5cdd8cd77ba3121db77e3dbf4676bee11406c3baf03ec68`** (re-measured by hashing the file), while `LIFECYCLE_CONTRACT_COUNT` stays **13** and `LIFECYCLE_ARTIFACT_COUNT` stays **54** — because this leaf's catalog change is a **consumer change only**: two `consumers` rows for `mcp/tests/test_knowledge_detection_runs.py` on the already-registered `diff_scope_test_support` and `read_scope_test_support` artifacts, no new artifact and no new contract. The body's pin paragraph now states that shape explicitly, so a successor can tell a consumer-only re-pin from a population move, and it keeps the rule the earlier entries stated: **a catalog change must re-pin deliberately in the same change, with the counts moving with the blocks they count** — and the reason written beside the constant in the source is what makes the re-pin auditable rather than convenient. Verification metadata advances to the leaf's base commit `4264dcc9` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-18T01:18+02:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): recorded the **fourth deliberate re-pin of the evidence-catalog identity**, moved in the same change as this leaf's catalog rows — `LIFECYCLE_CONTRACT_COUNT` 12 → **13**, `LIFECYCLE_ARTIFACT_COUNT` 53 → **54**, and `LIFECYCLE_CATALOG_SHA256` `9b057632…` → **`19ed0525cd94b57389052a4e19cf1f0dfe83e9c166783ead2598f6a4e0ce8ffa`**, measured on the frozen candidate by counting the blocks and hashing the file. The body's pin paragraph now carries the whole chain of states (`4 / 45 / 293a187f…` → … → `12 / 53 / 9b057632…` → `13 / 54 / 19ed0525…`), because a successor must be able to see that every move was deliberate. The catalog change itself is one new contract/artifact pair (`knowledge-facet-cases` for `mcp/tests/facet_test_support.py`) plus a wording-only edit to the existing `knowledge-generation-cases` row. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): recorded the **second deliberate re-pin of the evidence-catalog identity** and re-derived the card's citations against the new bytes — `LIFECYCLE_CONTRACT_COUNT` 10 → **11**, `LIFECYCLE_ARTIFACT_COUNT` 51 → **52**, and `LIFECYCLE_CATALOG_SHA256` `461121ca…` → **`4cf81f10dbbd6b941c50887dca45154612e5e46b7135465823af3e6604db3747`** (measured on the frozen candidate by counting the blocks and hashing the file). The card now names the check that makes the pin real — `_assert_the_catalog_kept_its_bytes_and_identities`, which recomputes the file's digest and counts both block kinds before comparing them to the constants — and records that this leaf's catalog change is a **new contract/artifact pair** (`knowledge-diff-cases` for `mcp/tests/diff_scope_test_support.py`) **plus** two consumer rows added to the existing read-scope artifact. It also keeps the rule the L7 entry stated, in the form a successor needs: **a catalog change must re-pin deliberately in the same change, with the counts moving with the blocks they count.** Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): recorded the **evidence-catalog pin** this module carries and the deliberate re-pin this leaf made alongside its own catalog row — `LIFECYCLE_CONTRACT_COUNT` 4 → **10**, `LIFECYCLE_ARTIFACT_COUNT` 45 → **51**, and `LIFECYCLE_CATALOG_SHA256` `293a187f…` → **`461121ca16567ab056938b710b19bddb98867581dd4fe3cf7ee2645111d54369`**. The card states why the pin exists in the form a successor needs: any change to `mcp/tests/evidence-lifecycle.toml` that nobody meant becomes a hard failure, and **a catalog change must re-pin deliberately in the same change, with the counts moving with the blocks they count**. It also records that the pin's comment names the digest it supersedes, so the history of the freeze is auditable from the source rather than only from this card. Verification metadata remains empty until closeout stamps the code commit.

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
