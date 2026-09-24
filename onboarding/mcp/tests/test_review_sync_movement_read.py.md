# mcp/tests/test_review_sync_movement_read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_sync_movement_read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T17:15:00+02:00 |
| lastVerifiedCommitHash | `06ed70cfcde7e3860ee5b53435727e7512e4335c` |
| lastVerifiedCommitDate | 2026-09-24T10:53:01+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

**ICR-R22@v1's read-side case evidence: what the live review read renders about a sync that moved its
inputs.** The leaf `260921-ICR-L22` publishes one durable `ar-review-sync-rebinding/v1` record per judged
generation; `test_review_sync_rebinding.py` owns the sync half and the fixture. This module owns the other
half of the same obligation — the ordinary review read — and every case drives the shipped
`read_knowledge_review` rather than the sync payload, so the packet's non-conforming example ("the old
review stays current while its inputs lag the merged line") cannot survive on the surface a reviewing
agent actually looks at.

It is a **separate module because the two together are past the file-size rail**, and the seam chosen is
the one the production owners already have: *what the sync measured* beside *what the read says about it*.
It **imports** the enclosure fixture from its sibling rather than duplicating it (`:35`), so "what a leaf
enclosure is" has one construction:

| Property | Case |
| --- | --- |
| `F6` — the primary review read renders a recorded movement instead of an untouched review | `test_the_live_review_read_renders_what_the_sync_moved` (`:41`) |
| `G1` — a retained knowledge operand the sync never compared is `not-measured` with the record's own reason, never agreement | `test_an_uncompared_knowledge_channel_is_rendered_unmeasured` (`:104`) |
| `G1` — an unusable record is its own state, in both of its causes, and neither is rendered as a measurement | `test_a_record_that_cannot_be_used_is_reported_unavailable` (`:169`) |
| `G2` — the success conjunct: a carrying state beside `ok: false` is not measured at all | `test_a_carrying_state_reported_as_a_failure_is_not_measured` (`:227`) |
| `H1` — the four validator clauses no case pinned, each violated by exactly one forgery | `test_the_movement_validator_refuses_each_false_shape` (`:258`) |

## Code Commentary

### Logic

**The phases are the read's, and the primary one is asserted through one shared helper.** Case `:41-102`
drives three states on one enclosure: (1) no sync has reported, so `payload.sync_movement is None` and
staleness is `current` — an absence, not a measured agreement; (2) a sync that carried a commit without
changing the reviewed capture, so the movement is `current` with no moved identities and the generation
id of the reviewed generation; and (3) the official line moves again and the reviewed capture moves with
it. The third state is asserted by `assert_the_read_renders_the_movement` (`:328-355`), which is the
packet's own phase: the movement is `stale`, every moved identity is a `code-candidate-tree:` value, the
generation id and reviewed binding digest are the generation's, `resolved_code_head` is the worktree's own
`HEAD`, `resolved_candidate_code_tree_id` is `fixture.capture_tree()`, the composed comparison's binding
digest is **not** the recorded one, staleness is `stale` with `moved` equal to the movement's identities
and `previous_comparison_ref` equal to the movement's reviewed binding digest, the staleness statement
carries "does not describe it", the successor action names `freeze_review_comparison`, and the submission
is `disabled_stale` — a review whose inputs a sync moved is not offered for submission.

**An uncompared channel is named as unmeasured, and the agreement clause stays unreachable.** Case
`:104-167` publishes nothing to the declared location, so the record's knowledge channel is `unmeasured`
and the read renders `binding_state == "not-measured"` with no moved identities, the record's own reason
(which names the location's `not-recorded` answer), and no agreement about a dataset nothing compared:
the statement may not contain "still describes the pair it resolved" nor "the reviewed dataset", and must
contain "unmeasured". The case also pins that `R17`'s staleness stays its own fact beside the movement.
It then sweeps three forgeries built from the *rendered* movement — a measurement carrying a reason, an
absence carrying none, and a moved input reported as anything but a movement — and requires each to raise.

**An unusable record is its own state, and the case records a known field-level ambiguity rather than
papering over it.** Case `:169-225` drives both causes: bytes that are not a readable record (reason names
"not a readable"), and a valid record naming another comparison (`supersedes_binding_digest` replaced, so
the reason names "does not describe"), each rendered `unavailable` with no moved identities and without
the agreement clause. Then it pins `H2` where it can be pinned without touching production bytes: **both**
`unavailable` sub-cases report `record_readable` False, so that one field cannot separate an unreadable
artifact from a valid record naming another generation — the sub-fact is carried by `reason` — and the
field-level fix (renaming it, or narrowing its documented meaning) needs a production-byte change in
`models/knowledge/review_staleness.py` and is held for the master's ruling.

**The success conjunct is pinned as a requirement, not as a live producer.** Case `:227-256` asserts
`resolved_pair_completed(payload) is True` for the real payload and `False` once `ok` is flipped, then
removes the durable record and calls `rebinding_result_block` with the failed payload: the block reports
`"not-measured"` and no record is written, so a carrying state beside a failed result can never be
measured as a resolution. The case's own docstring states the limit: every producer of the three carrying
states returns zero today, so this pins the requirement rather than an observed producer.

**`H1` sweeps the clauses a per-clause audit found unpinned, one forgery each.** Case `:258-325` takes the
real published movement as the accepted control (`binding_state == "not-measured"`), builds valid
`unavailable` and `current` bases, and then departs from exactly one clause at a time: a `stale` movement
with nothing moved and an identity named so the missing-identity clause cannot be the one refusing it, an
unusable record reported as readable, an agreement naming a resolved identity, and a movement naming no
resolved identity. Each must raise `ValidationError`, and the label list is asserted in order, so a clause
that stops refusing fails by name.

### Conventions

The module docstring (`:1-16`) states the seam and the reuse: the sibling owns the sync-side cases and the
enclosure fixture, this module owns what a reader of the ordinary review sees, and two fixtures would be
two places for "what a leaf enclosure is" to drift. The imports are the read route
(`agents_remember.application.knowledge_review.read_knowledge_review`, `:26`), the three read-side
owner names the cases drive (`rebinding_file_name`, `rebinding_result_block`, `resolved_pair_completed`,
`:27-31`), the movement vocabulary (`ReviewSyncMovement`, `:33`), the durable reports root (`:32`) and —
deliberately — the sibling's own `NEWLINE`, `ReviewSyncFixture`, `commit_file` and `git` (`:35`). Cases
are `unittest.TestCase` methods under `LiveReviewMovementTests` (`:38`), each driving real owners inside a
`tempfile.TemporaryDirectory`, and the shared read assertion is one module-level helper (`:328-355`) rather
than a duplicated block. The module is registered as one `integration` lane row
(`mcp/tests/test-evidence-lanes.toml:299-302`) and as four `consumer_scope = "exact"` consumer rows in
`mcp/tests/evidence-lifecycle.toml` (`:801-803`, `:1305-1309`, `:1431-1435`, `:1477-1481`), whose added
rows move the catalog digest pinned in `test_dependency_ownership_ast_helpers.py:46`. It measures **356
lines**.

### Invariants And Boundaries

- **The read never fails because a measurement was unavailable.** Every absence is either `None` (no
  measurement recorded) or a reported state (`not-measured`, `unavailable`); nothing here can fail a
  response, which is what the read-side owner's own docstring states.
- **`None` is not agreement, and `unmeasured` is not movement.** Case (1) of `:41-102` pins the first
  distinction on the read, and `:104-167` pins the second on the rendered statement — the three verdicts
  of the record are three facts, and the projection is a table rather than a two-way reading of the
  channel matches.
- **The sub-fact distinction inside `unavailable` is carried by `reason`, not by `record_readable`.** `H2`
  is pinned in place as a known ambiguity: both causes report `record_readable` False, and the field-level
  fix is held for the master's ruling because it needs a production-byte change.
- **Boundary: `G2` pins a requirement, not a live producer.** No producer emits a carrying state beside
  `ok: false` today; the case constructs that payload so the conjunct cannot be removed unnoticed.
- **Boundary: the two validator sweeps are different clause sets.** `:104-167` sweeps three clauses on the
  rendered movement; `H1` (`:258-325`) sweeps the four clauses a per-clause audit found unpinned. Neither
  sweep claims to cover every branch of the vocabulary's validator.
- **Boundary: these are read-surface cases, not a rendering case.** The cases assert payload values — the
  movement, the staleness, the submission and the comparison binding digest — and no browser or pane
  rendering is driven here.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository — the memory layer's `system/sources.md`
records no entries at all. The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The claims on this card are checkable in the module's own docstrings and cases and in the read-side owners
they drive. What a reader should carry: the module is the read half of one obligation and imports its
sibling's fixture rather than rebuilding it; `None`, `not-measured` and `unavailable` are three different
facts; and `H2` is a recorded, bounded ambiguity rather than a silent one.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the seam, of what it owns, and that it shares the enclosure fixture rather than duplicating it.** | `read_knowledge_review` | mcp/tests/test_review_sync_movement_read.py:1-16 |
| **The imports that make the sibling's fixture the one enclosure construction, and the cases' own `NEWLINE`.** | `ReviewSyncFixture`; `NEWLINE`; `commit_file`; `git` | mcp/tests/test_review_sync_movement_read.py:25-37 |
| The shipped review read the cases drive, and the read-side owner names they assert on. | `read_knowledge_review`; `rebinding_file_name`; `rebinding_result_block`; `resolved_pair_completed` | mcp/tests/test_review_sync_movement_read.py:26-34 |
| The case class, and the one shared read assertion the `F6` phase ends in. | `LiveReviewMovementTests`; `assert_the_read_renders_the_movement` | mcp/tests/test_review_sync_movement_read.py:330-358; mcp/tests/test_review_sync_movement_read.py:328-355; mcp/tests/test_review_sync_movement_read.py:40-327 |
| **`F6`: the three states of the primary read — no measurement, a measured agreement, and a measured movement — ending in the packet's own phase.** | `test_the_live_review_read_renders_what_the_sync_moved`; `sync_movement` | mcp/tests/test_review_sync_movement_read.py:41-102 |
| **`G1`: an uncompared knowledge channel is `not-measured` with the record's reason, with the agreement clause asserted absent.** | `test_an_uncompared_knowledge_channel_is_rendered_unmeasured`; `"still describes the pair it resolved"` | mcp/tests/test_review_sync_movement_read.py:104-167 |
| **`G1`: both causes of an unusable record, and the `H2` pin that `record_readable` cannot separate them.** | `test_a_record_that_cannot_be_used_is_reported_unavailable`; `"not a readable"`; `record_readable` | mcp/tests/test_review_sync_movement_read.py:169-225 |
| **`G2`: the success conjunct, and a failed result that cannot be measured.** | `test_a_carrying_state_reported_as_a_failure_is_not_measured`; `resolved_pair_completed`; `rebinding_result_block` | mcp/tests/test_review_sync_movement_read.py:227-256 |
| **`H1`: the four per-clause forgeries, each departing from exactly one clause of the movement validator.** | `test_the_movement_validator_refuses_each_false_shape`; `"stale_without_identity"` | mcp/tests/test_review_sync_movement_read.py:258-325 |
| **The read-side owner: the projection, its three outcomes, and the acceptance that requires the record to describe this very generation.** | `review_sync_movement`; `_measured`; `rebinding_names_the_generation` | mcp/src/agents_remember/application/review_sync_movement.py:87-135 |
| **The record's three verdicts mapped once, because reading "did any channel differ" would promote `unmeasured` to agreement.** | `_MOVEMENT_STATES` | mcp/src/agents_remember/application/review_sync_movement.py:64-84 |
| The `unavailable` value: an absence reported with its reason and without an agreement clause. | `_unavailable` | mcp/src/agents_remember/application/review_sync_movement.py:138-155 |
| One accepted record projected, with resolved identities carried exactly on the channel that moved. | `_project` | mcp/src/agents_remember/application/review_sync_movement.py:165-213 |
| The unmeasured reason in the record's own words, and the one sentence each state publishes. | `_unmeasured_reason`; `_statement`; `_measured_clause` | mcp/src/agents_remember/application/review_sync_movement.py:216-306 |
| **The fold that makes a measured movement outrank the reader's carried identity, which is what `F6` renders.** | `review_staleness_with_sync_movement` | mcp/src/agents_remember/application/review_sync_movement.py:357-382 |
| The read route that renders the movement and folds the staleness beside it. | `review_sync_movement`; `sync_movement` | mcp/src/agents_remember/application/knowledge_review.py:483-495; mcp/src/agents_remember/application/knowledge_review.py:555-555 |
| **The four-valued movement vocabulary, and the validator clause the `H1` forgeries are aimed at.** | `ReviewSyncMovementState`; `_the_state_follows_from_what_was_measured` | mcp/src/agents_remember/models/knowledge/review_staleness.py:45-48; mcp/src/agents_remember/models/knowledge/review_staleness.py:131-187 |
| **The two fields the `H2` ambiguity turns on, and the reviewed/resolved identity fields `F6` asserts.** | `record_readable`; `reason` | mcp/src/agents_remember/models/knowledge/review_staleness.py:109-129 |
| The submission vocabulary whose `disabled_stale` state ends the `F6` phase. | `ReviewSubmission`; `"disabled_stale"` | mcp/src/agents_remember/models/knowledge/review_staleness.py:190-204; mcp/src/agents_remember/application/review_record_rendering.py:194-209 |
| **The block that says why nothing was bound, which `G2` calls with a failed payload.** | `rebinding_result_block`; `"not-measured"` | mcp/src/agents_remember/application/review_sync_rebinding.py:316-373; mcp/src/agents_remember/application/review_sync_rebinding.py:565-582 |
| **The reader whose `not-recorded` and `unreadable` states the two `G1` cases exercise.** | `read_review_sync_rebinding`; `"unreadable"` | mcp/src/agents_remember/application/review_sync_rebinding.py:376-438 |
| **The half that makes a valid record naming another comparison unusable: it is compared against the sealed manifest.** | `rebinding_names_the_generation` | mcp/src/agents_remember/application/review_sync_rebinding.py:441-476 |
| The one durable location per (leaf, generation) the cases write, read and unlink. | `rebinding_file_name`; `durable_reports_root` | mcp/src/agents_remember/application/review_sync_rebinding.py:265-268; mcp/src/agents_remember/memory/knowledge/durable_evidence.py:51-58 |
| The record model and its self-consistency validator the projected movement reads. | `ReviewSyncRebinding` | mcp/src/agents_remember/models/knowledge/review_sync_rebinding.py:193-240 |
| The generation manifest the reviewed identities and binding digest come from. | `ComparisonGenerationManifest`; `read_manifest` | mcp/src/agents_remember/application/review_comparison_generation.py:376-376; mcp/src/agents_remember/application/review_comparison_generation.py:586-620 |
| The remedy the successor action names, which no case here performs. | `freeze_review_comparison` | mcp/src/agents_remember/application/review_comparison_freeze.py:232-232 |
| The production sync tool whose payload the read-side block is attached to. | `rebinding_result_block` | mcp/src/agents_remember/application/worktree_tools.py:378-378 |
| **The module's lane row and its four exact-scope consumer rows in the evidence catalog.** | "mcp/tests/test_review_sync_movement_read.py" | mcp/tests/test-evidence-lanes.toml:306-306; mcp/tests/evidence-lifecycle.toml:805-805; mcp/tests/evidence-lifecycle.toml:1311-1311; mcp/tests/evidence-lifecycle.toml:1440-1440; mcp/tests/evidence-lifecycle.toml:1489-1489 |
| The catalog digest the added consumer rows move, pinned by the structural check. | `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:46-46 |
| The sibling module that owns the sync-side cases, the fixture and the shared helpers. | `ReviewSyncFixture`; `assert_rebinding_measures_the_location` | mcp/tests/test_review_sync_rebinding.py:102-112; mcp/tests/test_review_sync_rebinding.py:853-867 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every case runs the shipped review read against
an enclosure, a generation store and a published dataset inside one repository boundary, and it reads the
record the same leaf's own managed syncs published at that repository's durable reports root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **citation re-anchoring and history only; no claim wording changed and no row deleted.** This leaf's change set moved the lines several of this card's rows cite — `mcp/src/agents_remember/application/knowledge_curator_ingest.py` grew 3587 → 3861 while `mcp/tests/test-evidence-lanes.toml` gained one `unit-regression` row and `mcp/tests/evidence-lifecycle.toml` gained two consumer rows, each shifting every row below it — so every affected range was re-derived against the candidate's own bytes rather than shifted by a remembered delta and re-anchored to the construct it names. Nothing in the body above was deleted to clear a finding, and no verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-23T20:30:00+02:00 — 260921-ICR-L23 curator (memory worktree only; no code changed, no commits; leaf base `473ad8242bb4c22bdabed5d5253767350381eb3e` plus the working-tree delta): **the module's docstring now names its own half of the movement question, and four reference rows here were re-anchored.** The summary line reads "what the *live* review read renders about the movement a managed sync measured" and the closing paragraph points at `test_review_external_git_movement_read.py` for the raw-Git half (`:1`, `:15-17`). The repaired rows are the four whose anchors sit in this file: the shared fixture import block (`:20-37`), the case class (`:40-327`), the read route's composition call (`knowledge_review.py:483-495`, `:555`) and the production sync tool's call site (`worktree_tools.py:378`). **No verification stamp was advanced**: the candidate is uncommitted, so no commit holds the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee`): created this one-to-one card for the module this leaf introduced as **ICR-R22@v1**'s read-side case evidence — what the shipped `read_knowledge_review` renders about a sync that moved the reviewed inputs. It records what the five cases actually prove: the split from the sync-side module is the **file-size rail's**, and the seam is the one the production owners already have, so this module imports its sibling's enclosure fixture (`ReviewSyncFixture`, `NEWLINE`, `commit_file`, `git`) instead of building a second one; the primary phase asserts the movement, the composed comparison's differing binding digest, the folded staleness and the `disabled_stale` submission; an uncompared knowledge channel is `not-measured` with the record's own reason and the agreement clause asserted **absent**; both causes of an unusable record render `unavailable`; and the success conjunct is pinned as a requirement rather than an observed producer. Two boundaries are carried as boundaries and not as defects: `H2` is a recorded ambiguity — both `unavailable` causes report `record_readable` False, so the sub-fact travels in `reason`, and the field-level fix needs a production-byte change in `models/knowledge/review_staleness.py` and is held for the master's ruling; and the `H1` sweep covers the four clauses a per-clause audit found unpinned, not every branch of the validator. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name this leaf's recorded base commit `e605822eb3bf83bf63a45963c5f51d5fc28859ee` because every construct cited here exists only in this leaf's uncommitted working tree — this module and its four catalog rows are not in any commit yet; what was actually read is that working tree, and the governed closeout owns the real stamp once the code commit exists.
