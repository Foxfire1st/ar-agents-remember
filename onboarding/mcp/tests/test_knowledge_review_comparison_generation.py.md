# mcp/tests/test_knowledge_review_comparison_generation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_review_comparison_generation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:18:54+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4` |
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **production-composition evidence for `ICR-R11@v1`**: one frozen comparison survives restart,
worktree cleanup and Git object reclamation. The packet names the one non-conforming shape directly — a
manifest that stores only a digest of already-deleted SQLite bytes — and these fifteen cases measure that
through the real production composition, never through a preconstructed payload: a real enclosure
contract on disk, a real linked worktree with staged, unstaged and untracked content, the real resolution
and capture owners, the real comparison, the real storage snapshot owner and a **real Git object store**.

Three measurements together make the first case the packet's journey rather than a re-read of what the
implementation just wrote (`:336-387`): a written-and-pruned **control object** proves `git gc
--prune=now` really reclaimed something in this run, so the candidate tree's survival is attributable to
the recorded pin rather than to a reclamation that did nothing; the fixture's whole worktree group —
worktree, live datasets and stage — is removed; and the reopen happens in a **child process** that shares
no state with the one that froze the comparison (`_reopen_in_a_new_process`, `:279-315`, running the
inline `_CHILD_REOPEN` program at `:102-164`).

The module's docstring states the load-bearing properties one case each; the header lists all fifteen.

## Code Commentary

### Logic

The manifest-binding case expects the ordinary producer's actual R14/currentness inputs and explicit assessment availability. It still compares exact owner identities and preserves zero records when the authority is unavailable. The adjustment is grouped assertions inside the existing case, not a new case or a relaxation of source/knowledge custody.

**The fixture is shared with the sibling review suite, not rebuilt.** `comparison_fixture` (`:168-171`)
calls `build_endpoint_fixture` imported from `test_knowledge_review_source_endpoints` — the R01
production-composition fixture — so these cases measure the *same* real enclosure, worktree and capture
path the source-endpoint cases measure rather than a second, drifting one. The two Git-truth helpers are
taken from the shipped scope-test support (`_git`, `BATCH_PATH`, `BATCH_PATH_CANDIDATE_TEXT`), and the
file whose candidate bytes are read back (`CANDIDATE_CONTENT_PATH`) is the one the fixture edits
**without staging it**, so its content exists in no commit and only the pin keeps it.

**`_freeze` (`:174-185`) requires a published generation.** Every journey case starts from a freeze that
asserted `state == "published"` and carries the refusal as its message, so a case can never silently
measure a refusal path while claiming to measure retention.

**The child process is a real restart.** `_CHILD_REOPEN` imports the package from the worktree it is
pointed at, builds its own `McpRuntimeConfig` from the payload, calls
`reopen_comparison_generation(..., generation_id=…)` with **no enclosure, no worktree and no live
state**, and reads the candidate content back with `git show <tree>:<path>` under an isolated
environment. It prints one JSON summary, and `_reopen_in_a_new_process` raises with the child's exit code
and stderr if the child failed — so a broken child is a failure, never an empty result.

**`_live_composition` (`:318-330`) is the independent counter-value.** It composes the same review again
from the live surface and returns the owners' own values (the comparison's `binding_digest`, its
`policy_version`, the digest over R02's inventory payload and its `listed_total`), which is how the
"what the manifest binds" case compares the record against a second reading instead of against itself.

**Damage is injected, never simulated.** The helpers exist to inject exactly the four shapes the cases
need: `_reseal` (`:244-253`) recomputes the seal over an edited field set **the way a fabrication would
have to** — so whatever catches it can only be a *second* statement of the same identity, which is what
`read_manifest`'s directory-name check is; `_write_control_object` (`:236-241`) writes an unreferenced
object for the reclamation measurement; `_hidden_stages` (`:229-233`) lists the stage directories the
freeze is supposed to have removed; `_refs` (`:224-226`) lists `refs/ar/` so "no pin was created" is
measured; and `_side`/`_artifact` (`:265-276`) address a half by its own name rather than by position.

**The fifteen cases, and the property each one protects:**

| Case | Property |
| --- | --- |
| `test_a_frozen_comparison_reopens_the_exact_content_after_restart_and_reclamation` (`:336-387`) | the packet's journey: freeze → real reclamation (with control) → worktree group removed → child-process reopen of the exact tree, both exact datasets and the cited evidence |
| `test_the_manifest_binds_the_owners_identities_versions_and_its_own_fields` (`:393-477`) | what the record stores is the **owners'** values (contract base, capture tree, each dataset's logical identity, R02's inventory, the comparison's binding digest, all five policy stamps), and its seal covers its own fields |
| `test_an_explicit_release_records_unavailable_history_and_is_measured_not_assumed` (`:483-550`) | the release leaves a record, the reopen reports `custody_observed="absent"` beside `unavailable-history`, and the object ids are still named rather than resolving to today's data |
| `test_a_missing_or_damaged_retained_input_is_reported_per_channel` (`:556-598`) | an injected deleted snapshot is `missing`, a corrupted one is `corrupt`, a rewritten citation is `corrupt`, and the untouched channel stays `available` |
| `test_a_record_that_cannot_be_read_is_not_a_readable_generation` (`:601-669`) | four unreadable shapes in order: unparseable bytes, a sealed field edited in place, the verifier's full **reseal**, and a reseal plus a matching id — each `manifest-unreadable` with no payload |
| `test_a_refused_freeze_publishes_nothing_and_reclaims_its_stage_and_pin` (`:675-708`) | a refused freeze leaves no generation directory, no hidden stage and no pin it created, and the same leaf freezes successfully after the damaged half is repaired |
| `test_an_exact_retry_converges_and_a_superseding_generation_names_its_predecessor` (`:711-762`) | `reused=True` with a byte-identical manifest, then a successor naming its predecessor by id **and** manifest digest while the first generation's bytes are untouched |
| `test_a_half_with_no_recorded_generation_freezes_as_typed_absence_never_as_inference` (`:768-836`) | R05's typed absence and the comparison's own `not-selected` are recorded as statements and each half is reported in its own state without calling the generation unavailable |
| `test_a_declared_absence_beside_present_bytes_is_refused` (`:839-866`) | a declared historical absence standing beside a readable dataset is refused |
| `test_the_leaf_s_own_work_branch_is_not_custody_and_the_pin_survives_losing_it` (`:869-910`) | the F1 falsifier reproduced exactly: commit on the work branch → `custody="retained"` + one ref → `worktree remove --force` → `branch -D` → `gc --prune=now` → child-process reopen `available` |
| `test_protected_history_taking_custody_stops_the_pin_and_the_generation_still_reopens` (`:913-966`) | the genuine `committed-history` path: the protected source branch fast-forwarded the way integration does it → **no ref created** → still reopens after the same deletions |
| `test_a_retention_ref_that_moved_is_never_deleted` (`:969-1016`) | a moved ref is refused, records nothing, and is left in place |
| `test_a_stage_a_dead_freeze_left_behind_is_reclaimed_and_a_live_one_is_not` (`:1030-1057`) | a real child process creates a stage and exits; after one freeze the dead stage is gone, this process's stage is untouched, and `_hidden_stages` is exactly the live one |
| `test_discarding_snapshots_records_the_bytes_it_measured_and_refuses_a_mismatch` (`:1060-1124`) | a mismatched snapshot is refused with both files in place and no record; recorded digests then equal the frozen ones; both halves report `unavailable-history`; the retry records `None` |
| `test_a_frozen_again_comparison_reports_its_live_pin_before_the_release_history` (`:1127-1170`) | release → refs empty → re-freeze → `reused=True`, same digest, ref back → reopen reports `pin_present=True` **and** `release_recorded=True` with the live measurement leading the detail |

### Conventions

`pytestmark = pytest.mark.evidence_unit` (`:81`) is the module's lane marker, and the module's path is
registered in `mcp/tests/test-evidence-lanes.toml`'s `unit-regression` lane. It also appears as a
**source-derived consumer** in the two `consumer_scope = "exact"` rows of `mcp/tests/evidence-lifecycle.toml`
that its imports make it a consumer of (`diff_scope_test_support.py`, `read_scope_test_support.py`) — so
the catalog's consumer sets stay exact rather than approximate. Every case is deterministic: no case
depends on wall-clock ordering, and order-sensitive Git commands run through helpers that pin `PATH`,
`HOME` and `GIT_CONFIG_NOSYSTEM`.

### Invariants And Boundaries

- **Production composition only.** No case injects a preconstructed manifest, a fake repository or a
  hand-built payload; every value the record binds is produced by the shipped owner.
- **Restart is measured, not simulated.** The reopen runs in a child process that shares no state, and a
  child failure is an assertion failure with its stderr, never an empty result.
- **Reclamation is proven to have happened.** The control object makes "the tree survived `gc`" a
  measurement rather than an assumption.
- **A fabrication is caught by a second statement of the same identity**, which is why the reseal case
  exists: an internally consistent forgery is exactly what a seal-only check would accept.
- **Damage is injected into real artifacts**, so the channel states are measured on the real readers.
- **No case reaches the HTTP surface, a browser or a route.** The reopen is exercised through the
  application operation only; wiring a route or a pane is R12/R13/R17/R20/R21 territory.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the module's own docstring, helpers and cases. Three details a
reader should carry: the fixture is **shared with the R01 source-endpoint suite** rather than rebuilt, so
these cases measure the same real enclosure and capture path; the reopen really is a child process, and
the module's first case also proves `git gc --prune=now` reclaimed something via an unreferenced control
object; and the unreadable-record case injects a **full reseal** specifically because a seal-only check
would accept it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the packet's journey and of the load-bearing property behind each case. | "ICR-R11@v1" | mcp/tests/test_knowledge_review_comparison_generation.py:1-30 |
| The lane marker, the two content constants the fixture edits without staging, and the cited-evidence paths. | `pytestmark`; `CANDIDATE_CONTENT_PATH`; `CANDIDATE_CONTENT`; `_EVIDENCE_RELATIVE`; `_EVIDENCE_TEXT`; `_EVIDENCE_REWRITTEN` | mcp/tests/test_knowledge_review_comparison_generation.py:81-81; mcp/tests/test_knowledge_review_comparison_generation.py:85-86; mcp/tests/test_knowledge_review_comparison_generation.py:94-96 |
| **The child program: a real restart that builds its own config, reopens from the task artifact plane alone, and reads the candidate bytes back through `git show`.** | `_CHILD_REOPEN`; `_reopen_in_a_new_process` | mcp/tests/test_knowledge_review_comparison_generation.py:102-164; mcp/tests/test_knowledge_review_comparison_generation.py:279-315 |
| The shared R01 production fixture these cases build on rather than duplicating. | `comparison_fixture`; `build_endpoint_fixture`; `EndpointFixture`; `LEAF_ID` | mcp/tests/test_knowledge_review_comparison_generation.py:167-171; mcp/tests/test_knowledge_review_source_endpoints.py:71-71; mcp/tests/test_knowledge_review_source_endpoints.py:93-93; mcp/tests/test_knowledge_review_source_endpoints.py:113-197; mcp/tests/test_knowledge_review_source_endpoints.py:207-239 |
| The freeze helper that requires a published generation, and the evidence-citation options. | `_freeze`; `_cite_evidence`; `_evidence_options` | mcp/tests/test_knowledge_review_comparison_generation.py:174-185; mcp/tests/test_knowledge_review_comparison_generation.py:188-194; mcp/tests/test_knowledge_review_comparison_generation.py:197-200 |
| **The injection helpers: the reclamation control object, the fabrication's own reseal, the hidden-stage list and the `refs/ar/` list.** | `_write_control_object`; `_reseal`; `_hidden_stages`; `_refs`; `_object_present`; `_digest` | mcp/tests/test_knowledge_review_comparison_generation.py:220-221; mcp/tests/test_knowledge_review_comparison_generation.py:224-226; mcp/tests/test_knowledge_review_comparison_generation.py:229-233; mcp/tests/test_knowledge_review_comparison_generation.py:236-241; mcp/tests/test_knowledge_review_comparison_generation.py:244-253; mcp/tests/test_knowledge_review_comparison_generation.py:259-262 |
| The independent counter-value the "what the record binds" case compares against. | `_live_composition` | mcp/tests/test_knowledge_review_comparison_generation.py:318-330 |
| **The packet's journey, with the control object and the removed worktree group.** | `test_a_frozen_comparison_reopens_the_exact_content_after_restart_and_reclamation` | mcp/tests/test_knowledge_review_comparison_generation.py:336-387 |
| **The owners' values versus the record's own fields.** | `test_the_manifest_binds_the_owners_identities_versions_and_its_own_fields` | mcp/tests/test_knowledge_review_comparison_generation.py:393-479 |
| **The release record, and the custody measured before reclamation reported beside the deletion.** | `test_an_explicit_release_records_unavailable_history_and_is_measured_not_assumed` | mcp/tests/test_knowledge_review_comparison_generation.py:485-552 |
| **Per-channel damage: missing, corrupt, corrupt citation, and the untouched channel.** | `test_a_missing_or_damaged_retained_input_is_reported_per_channel` | mcp/tests/test_knowledge_review_comparison_generation.py:558-600 |
| **The four unreadable shapes, including the internally consistent reseal that only a second identity statement catches.** | `test_a_record_that_cannot_be_read_is_not_a_readable_generation` | mcp/tests/test_knowledge_review_comparison_generation.py:603-671 |
| **A refused freeze publishes nothing and reclaims its own stage and pin.** | `test_a_refused_freeze_publishes_nothing_and_reclaims_its_stage_and_pin` | mcp/tests/test_knowledge_review_comparison_generation.py:677-710 |
| **Convergence on a published record, and a successor's resolved lineage.** | `test_an_exact_retry_converges_and_a_superseding_generation_names_its_predecessor` | mcp/tests/test_knowledge_review_comparison_generation.py:713-764 |
| **The typed absences, and the refusal of a declaration beside present bytes.** | `test_a_half_with_no_recorded_generation_freezes_as_typed_absence_never_as_inference`; `test_a_declared_absence_beside_present_bytes_is_refused` | mcp/tests/test_knowledge_review_comparison_generation.py:770-838; mcp/tests/test_knowledge_review_comparison_generation.py:841-868 |
| **The two custody cases: the work branch is not custody, and protected history taking custody stops the pin.** | `test_the_leaf_s_own_work_branch_is_not_custody_and_the_pin_survives_losing_it`; `test_protected_history_taking_custody_stops_the_pin_and_the_generation_still_reopens` | mcp/tests/test_knowledge_review_comparison_generation.py:871-912; mcp/tests/test_knowledge_review_comparison_generation.py:915-968 |
| The moved-ref refusal, and the dead-versus-live stage sweep driven through a real child process. | `test_a_retention_ref_that_moved_is_never_deleted`; `test_a_stage_a_dead_freeze_left_behind_is_reclaimed_and_a_live_one_is_not`; `_stage_left_by_a_dead_process` | mcp/tests/test_knowledge_review_comparison_generation.py:971-1018; mcp/tests/test_knowledge_review_comparison_generation.py:1032-1059; mcp/tests/test_knowledge_review_comparison_generation.py:1175-1196 |
| **The measured-discard case, and the live-pin-before-release-history case.** | `test_discarding_snapshots_records_the_bytes_it_measured_and_refuses_a_mismatch`; `test_a_frozen_again_comparison_reports_its_live_pin_before_the_release_history` | mcp/tests/test_knowledge_review_comparison_generation.py:1062-1126; mcp/tests/test_knowledge_review_comparison_generation.py:1129-1172 |
| The lane row this module was registered under, inside the array whose own key declares the classification. | "mcp/tests/test_knowledge_review_comparison_generation.py"; "unit-regression = [" | mcp/tests/test-evidence-lanes.toml:153-153; mcp/tests/test-evidence-lanes.toml:5-5 |
| **The two exact-consumer rows this module was added to, because its imports make it a source-derived consumer — each cited down to the artifact's own `consumer_scope` and the list it opens.** | `consumer_scope`; `consumers` | mcp/tests/evidence-lifecycle.toml:96-96; mcp/tests/evidence-lifecycle.toml:97-97 |
| The lane row this module was registered under. | `unit-regression`; "mcp/tests/test_knowledge_review_comparison_generation.py" | mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/test-evidence-lanes.toml:153-153 |
| **The two exact-consumer rows this module was added to, because its imports make it a source-derived consumer.** | `consumers`; `consumer_scope` | mcp/tests/evidence-lifecycle.toml:83-101; mcp/tests/evidence-lifecycle.toml:97-1713 |
| The Git-truth support helpers the module reads its evidence through. | `_git`; `BATCH_PATH`; `BATCH_PATH_CANDIDATE_TEXT` | mcp/tests/diff_scope_test_support.py:113-113; mcp/tests/diff_scope_test_support.py:516-531; mcp/tests/read_scope_test_support.py:118-118; mcp/tests/read_scope_test_support.py:752-767 |

The following declarations carry the changed boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The manifest is checked against actual owner records, identities and availability. | `test_the_manifest_binds_the_owners_identities_versions_and_its_own_fields` | mcp/tests/test_knowledge_review_comparison_generation.py:393-479 |

## Cross-Repo References

No cross-repository behavior is measured in this file. It creates a local repository, an enclosure and a
task-artifact root under `tmp_path` for each case.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): No content impact: this card's own source is unchanged. MIK-R32 moved lines in `mcp/tests/test-evidence-lanes.toml`, so the citation rows into them that moved were re-pointed by the installed fixer (run once; its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; every re-pointed row was byte-identical to memory HEAD beforehand and was checked to hold its anchors in the new range. No verification stamp was advanced.
- 2026-09-30T12:56:40+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db` plus the staged delta; first curated over `b54d1b03`, then merged with L29's landed curation after the sync onto code `ce459423` / memory `a6075c76`, L29's committed lines kept byte-identical): No content impact: citation-only repair. This card's source is unchanged; MIK-R14 inserted one `unit-regression` row at `test-evidence-lanes.toml:127` (`:126` before the sync onto L29), so every later lane row moved down by one line. The rows citing those lines, which the installed fixer declined, were re-pointed by that exact shift (each row byte-identical to memory HEAD, its anchors checked in the base and shifted ranges). No verification stamp was advanced. **After the sync:** the rows L29's landed curation had also re-pointed were taken from L29's text and re-pointed by the exact line shift from `ce459423` to the staged tree (L14's lane row now at `:127`, its catalog line `:839`, the pin docstring), each anchor checked at both ends; the other rows keep this leaf's values.
- 2026-09-30T12:15:39+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`): No content impact: this card's own source is unchanged. MIK-R29 grew `mcp/tests/test-evidence-lanes.toml` (one `unit-regression` row at `:108`), so the citation rows into it that moved were re-pointed by the installed fixer's normalisation or by the exact base-to-staged line shift; every re-pointed row was checked to hold its anchors in the new range, and no claim was reworded. No verification stamp was advanced.
- 2026-09-30T05:58:11+02:00 — 260928-MIK-L05 curator (uncommitted change set on `ar/260928-mik-l05`, code base `31d761a241055d67b85ef3908033856b78a86a57` plus the staged and unstaged delta): No content impact: citation-only repair. This card's source is unchanged. Rows citing `mcp/tests/test-evidence-lanes.toml` were re-pointed to the lines MIK-R05 moved, by the installed fixer or by the exact line shift where it declined (each such row byte-identical to memory HEAD, its anchors checked in the base and the shifted ranges); no claim was reworded.
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; rows citing lane rows after the one `unit-regression` row MIK-R10 inserted at `test-evidence-lanes.toml:124` (or catalog lines after `evidence-lifecycle.toml:836`) were re-pointed by the installed fixer or, where it declined, by the exact line shift over rows byte-identical to memory HEAD. No claim was reworded, so the fixer's bullets are kept. No verification stamp was advanced.
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): No content impact: this card's source is unchanged. Rows citing lines that MIK-R25 moved in `test-evidence-lanes.toml` were re-pointed, by the installed fixer (its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; each such row was byte-identical to memory HEAD. No verification stamp was advanced.
- 2026-09-30T03:13:03+02:00 — 260928-MIK-L13 curator (uncommitted change set on `ar/260928-mik-l13`, code base `3772cdcd008fcacdc5a86e264a3ef63e879ea544` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; MIK-R13 inserted one `unit-regression` row at `test-evidence-lanes.toml:121`, so citation ranges into later lane rows were projected by the installed `memory-citations --fix` or, for multi-anchor rows it declined, re-pointed by the exact base-to-staged line shift (+1 at or after `:121`; each such row was byte-identical to memory HEAD).
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; MIK-R01 moved lines in `test-evidence-lanes.toml`, so citation ranges into it were projected by the installed `memory-citations --fix` or, for multi-anchor rows it declined, re-pointed by the exact base-to-staged line shift (each such row was byte-identical to memory HEAD).
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; L06 inserted one `unit-regression` row at `test-evidence-lanes.toml:69`, so its citations to later lane rows moved down one line. The multi-anchor lane rows the fixer declined were re-pointed by that exact +1 shift, and each was checked to hold its anchors in the shifted ranges; any other moved row was re-pointed by the installed fixer, which records its own bullet. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R11's changes, were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R02's changes (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-staged line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): No content impact: citation-only repair. Ranges into `mcp/tests/test-evidence-lanes.toml`, moved by MIK-R30's line insertions (or normalised by the installed fixer in the same pass), were re-pointed by the installed `memory-citations --fix` or, for rows it declined, by the exact base-to-working line map. Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R03 added one row at `:112` of `test-evidence-lanes.toml`, moving every later row down one line, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). The fixer also normalised passing ranges in rows that cite files this leaf did not change; those ranges are measurement-true. No claim, anchor or source file of this card changed.
- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): No content impact: citation ranges only. MIK-R08 moved lines in `test-evidence-lanes.toml`, and the rows here that cite them were re-pointed to the same constructs (by the installed `memory-citations --fix` where it could regenerate a range, and otherwise by the exact base-to-candidate line map). No claim, anchor or source file of this card changed.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`mcp/tests/evidence-lifecycle.toml` and `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the exact base-to-working line map (multi-anchor rows the installed fixer declined); no claim wording changed. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): No content impact: this card's source is unchanged; its citations into `mcp/tests/test-evidence-lanes.toml` moved by this leaf's two-line `unit-regression` insertion at `:107-108` and were re-pointed (by the installed anchor-range projection where it could, otherwise by exact base-to-working line mapping). Each re-pointed row cites the same lane line it cited at base; no claim wording changed and no verification stamp was advanced.
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **No content impact** — citation-only repair. MIK-R20 inserts two `unit-regression` rows at `mcp/tests/test-evidence-lanes.toml:102-103`, which moves every later lane row down by two lines; this card's lane-row citations were re-pointed by that exact shift (by base-to-working line mapping where the installed fixer declined a multi-anchor row), their claims unchanged. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`test-evidence-lanes.toml`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`application/published_intent.py`, `mcp/tools/knowledge.py`, `mcp/registration/knowledge.py`, `models/tools/knowledge_responses.py`, `cli/__main__.py`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the installed fixer or, for the multi-anchor rows it declined, by exact base-to-working line mapping; a per-document `memory-citations` check then reported 0 findings. No claim wording changed.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): No content impact: citation-only re-measure. This card cites `mcp/tests/test-evidence-lanes.toml`, where MIK-R22's two `unit-regression` rows (`:99-100`) moved every later row down two lines. Ranges were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact line shift, and a per-document check then reported 0 findings. The claims were re-read and are unchanged. No verification stamp was advanced.
- 2026-09-29T06:00:00+02:00 — 260928-MIK-L07 curator (uncommitted change set on `ar/260928-mik-l07`, code base `45fe37749b388de348d16ced50c28c03490dce64` plus the working-tree delta): No content impact: MIK-R07 inserts one `unit-regression` row at `mcp/tests/test-evidence-lanes.toml:98`, so this card's rows citing lane lines below it were re-pointed one line down (by the installed anchor-range projection or, where it declined a multi-anchor row, by an exact one-line shift confirmed by every anchor resolving in the current file). Claim wording unchanged. No stamp advanced.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): No content impact: the lane row re-pointed to `test-evidence-lanes.toml:122` after MIK-R21's two-line insertion. Claim meaning unchanged; no stamp advanced.
- 2026-09-28T23:41:23+02:00 — 260921-ICR-L57 curator (uncommitted candidate tree `a0358351a0f6b5157f7abc2255a0a6e46066ae6b` over code base `69883386d36d7cdb7faeed5bdf275ddd66d87aea`): No content impact: re-pointed 5 citations into `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_endpoints.py` through the exact base-to-candidate line map after this leaf's behaviour-preserving splits and catalog/lane/pin repairs; each moved range cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T17:08:17+02:00 — 260921-ICR-L45 curator (uncommitted candidate over code base `9b2f775f` after the L44 sync; first measured on tree `0daccca407864fe0da7b0b034d647b5eecd0a640` over `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed through the exact base-to-candidate line map; each moved row cites the same line content it cited at base. Wording is unchanged, and no stamp was advanced.

- 2026-09-27T05:43:38+00:00 — Curator-authored re-citation of 2 investigated L41 source-linked claim(s). Each named registration or declaration was selected individually after the composite guarded projection declined. Prior explanation, refusal evidence, generated history and real verification stamps are preserved.
- 2026-09-27T05:29:38+00:00: Generated citation repair: "mcp/tests/test_knowledge_review_comparison_generation.py" repointed to mcp/tests/test-evidence-lanes.toml:119-119. No content impact: mechanical anchor-range projection bound to citation source snapshot a9e4bf20669ecb356be8a208a2ac77489c28fc161e108a6d1b20c61579617d84; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-27T04:58:33+00:00 — Reconciled the existing manifest-binding assertion with normal owner-record collection. Verification hashes/dates remain closeout-owned.

- 2026-09-27T00:34:45Z — L39: No content impact: resolved the affected registry/instruction/overview reference rows against their exact current named anchors after the scoped source changes. Existing factual meaning, verification stamps and earlier history are preserved.

- 2026-09-26T21:19:30+00:00: Generated citation repair: "mcp/tests/test_knowledge_review_comparison_generation.py" repointed to mcp/tests/test-evidence-lanes.toml:116-116. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "mcp/tests/test_knowledge_review_comparison_generation.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and history only; no claim wording changed and no row deleted.** This leaf's change set moved the lines several of this card's rows cite — `mcp/src/agents_remember/application/knowledge_curator_ingest.py` grew 3587 → 3861 while `mcp/tests/test-evidence-lanes.toml` gained one `unit-regression` row and `mcp/tests/evidence-lifecycle.toml` gained two consumer rows, each shifting every row below it — so every affected range was re-derived against the candidate's own bytes rather than shifted by a remembered delta and re-anchored to the construct it names. Nothing in the body above was deleted to clear a finding, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation repair only, forced by the lane row and the two consumer rows this leaf's sibling changes moved.** This file is not a changed source file; the ranges that moved belong to `mcp/tests/test-evidence-lanes.toml` (one row inserted at `:111`, below this module's `:107`) and `mcp/tests/evidence-lifecycle.toml`. Three rows were re-read and re-derived: the lane row — whose anchor cell named a non-identifier lane label and so stated nothing checkable — now names this module's own path beside the `unit-regression = [` key; the two exact-consumer rows now cite each artifact's own `consumer_scope` line and the list it opens (`:1403-1405`, `:1428-1430`) rather than the bare row lines; and the docstring row's placeholder anchor was replaced by the requirement id the docstring actually carries (`"ICR-R11@v1"`). No claim's substance was changed, and **no verification stamp was advanced** — the recorded stamp is kept, because the candidate is uncommitted and closeout owns the real commit.
- 2026-09-21T19:55:00+02:00 — 260921-ICR-L11 curator (uncommitted change set on `ar/260921-icr-l11`, base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`): created this one-to-one card for the module this leaf introduced as the **production-composition evidence for ICR-R11@v1**. It records what the fifteen cases actually protect rather than restating their names: the first is the packet's journey and proves `git gc --prune=now` really reclaimed via an unreferenced control object, so the pinned tree's survival is attributable to the pin; restart is **measured**, not simulated, through a child process with no shared state whose failure is an assertion failure and never an empty result; the fabrication case injects a **full reseal** — an internally consistent forgery — because a seal-only check would accept it, which is exactly what the re-derived id plus the directory-name agreement exist to catch; and the two custody cases reproduce the verification falsifier (commit on the leaf's own work branch → `custody="retained"` → worktree removed, branch deleted, gc → child-process reopen `available`) beside the genuine committed-history path where **no ref is created**. It also records the fixture provenance — the cases build on the R01 source-endpoint suite's real enclosure and capture path rather than a second fixture — and the governance shape: the module's lane row in `test-evidence-lanes.toml` and its addition to the two exact-consumer rows in `evidence-lifecycle.toml` that its imports make it a consumer of. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`, this leaf's recorded base — because every construct cited here exists only in this leaf's uncommitted candidate; what was actually read is this leaf's uncommitted working tree, and closeout owns the real stamp once the code commit exists.
