# mcp/tests/test_review_sync_movement_read.py

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
(`mcp/tests/test-evidence-lanes.toml:372-373`) and as four `consumer_scope = "exact"` consumer rows in
`mcp/tests/evidence-lifecycle.toml` (`:801-803`, `:1305-1309`, `:1431-1435`, `:1477-1481`). It measures **356
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

## Evidence

### Docs References

No domain documentation source is configured for this repository — the memory layer's `system/sources.md`
records no entries at all. The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The claims on this card are checkable in the module's own docstrings and cases and in the read-side owners
they drive. What a reader should carry: the module is the read half of one obligation and imports its
sibling's fixture rather than rebuilding it; `None`, `not-measured` and `unavailable` are three different
facts; and `H2` is a recorded, bounded ambiguity rather than a silent one.

- **The module's own statement of the seam, of what it owns, and that it shares the enclosure fixture rather than duplicating it.** [1]
- **The imports that make the sibling's fixture the one enclosure construction, and the cases' own `NEWLINE`.** [2]
- The shipped review read the cases drive, and the read-side owner names they assert on. [3]
- The case class, and the one shared read assertion the `F6` phase ends in. [4]
- **`F6`: the three states of the primary read — no measurement, a measured agreement, and a measured movement — ending in the packet's own phase.** [5]
- **`G1`: an uncompared knowledge channel is `not-measured` with the record's reason, with the agreement clause asserted absent.** [6]
- **`G1`: both causes of an unusable record, and the `H2` pin that `record_readable` cannot separate them.** [7]
- **`G2`: the success conjunct, and a failed result that cannot be measured.** [8]
- **`H1`: the four per-clause forgeries, each departing from exactly one clause of the movement validator.** [9]
- **The read-side owner: the projection, its three outcomes, and the acceptance that requires the record to describe this very generation.** [10]
- **The record's three verdicts mapped once, because reading "did any channel differ" would promote `unmeasured` to agreement.** [11]
- The `unavailable` value: an absence reported with its reason and without an agreement clause. [12]
- One accepted record projected, with resolved identities carried exactly on the channel that moved. [13]
- The unmeasured reason in the record's own words, and the one sentence each state publishes. [14]
- **The fold that makes a measured movement outrank the reader's carried identity, which is what `F6` renders.** [15]
- **The four-valued movement vocabulary, and the validator clause the `H1` forgeries are aimed at.** [17]
- **The two fields the `H2` ambiguity turns on, and the reviewed/resolved identity fields `F6` asserts.** [18]
- The submission vocabulary whose `disabled_stale` state ends the `F6` phase. [19]
- **The block that says why nothing was bound, which `G2` calls with a failed payload.** [20]
- **The reader whose `not-recorded` and `unreadable` states the two `G1` cases exercise.** [21]
- **The half that makes a valid record naming another comparison unusable: it is compared against the sealed manifest.** [22]
- The one durable location per (leaf, generation) the cases write, read and unlink. [23]
- The record model and its self-consistency validator the projected movement reads. [24]
- The generation manifest the reviewed identities and binding digest come from. [25]
- The remedy the successor action names, which no case here performs. [26]
- The production sync tool whose payload the read-side block is attached to. [27]
- **The module's lane row and its four exact-scope consumer rows in the evidence catalog.** [28]
- The sibling module that owns the sync-side cases, the fixture and the shared helpers. [30]

- The read route that renders the movement and folds the staleness beside it. [32]

### Cross-Repo References

No cross-repository behavior is implemented in this file. Every case runs the shipped review read against
an enclosure, a generation store and a published dataset inside one repository boundary, and it reads the
record the same leaf's own managed syncs published at that repository's durable reports root.

No meaningful cross-repo references found.

