# mcp/src/agents_remember/application/review_rename_inference.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_rename_inference.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T19:40:00+02:00 |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc` |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The labelled Git rename inference over two bound code trees** (`ICR-R08@v1`). The packet allows a
source rename to be *displayed* as a labelled Git inference and forbids it from being proof that an
invariant moved; this module owns that distinction as a value. Git's own similarity detection is asked
once, over the two **bound tree objects** — never a branch, a working tree or `HEAD` — and its answer
travels as `ReviewRenameInference`, whose `basis` can only be Git's detection (`git_rename_detection`),
whose `state` separates a measured pairing (`inferred`) from a measured non-pairing (`not_paired`) and
from a measurement that was never made (`unavailable`), and whose `statement` says in its own words
that this is a similarity inference about the source.

Nothing here creates, moves or attributes anything. The pairs are asked about **after** a movement has
been established by the recorded anchors and the author's own edges, and the answer is attached beside
that movement: the inference can say which recorded old address looks like the file that moved, and it
can say nothing about which invariant moved, because the traversal never reads it back.

The module is new in `260921-ICR-L8` and exists only in that leaf's uncommitted candidate (branch
`ar/260921-icr-l8`); the verification basis recorded above is the production line at this leaf's base,
`02957762709c9b515b4ff57f7f13524a7c0dfb8d`. Closeout owns the stamp once the code commit exists.

## Code Commentary

### Logic

**`git_rename_inference` is the one measurement, and it publishes the interface it used.**
`RENAME_INFERENCE_COMMAND` is the full command with both tree ids substituted, so a reader reproduces
the inference without this module. A side that named no exact tree, a side that named a tree without
the repository root it lives in, a Git failure and an answer that is not the declared NUL-delimited
`--raw -z` record format each return `available=False` **with their reason** — never an empty pairing,
because "Git found no rename" and "Git was not asked" are different facts.

**`RenameObservations` is the honesty boundary, and `RenameInferenceSources` holds one measurement
together.** A pair of trees with no rename produces `available=True` with no pairs; a measurement that
was not made produces `available=False` with its reason and no pairs either. The two bound trees and
the probe seam travel as one frozen value (`observe()` asks the seam or states why it did not), so an
inference measured over another pair of trees, or through another seam, cannot wear this one's identity.
`no_rename_inference` is the seam a caller substitutes when it must run no Git command at all.

**`moved_pairs` decides what is worth asking about.** One pair per recorded before address that differs
from the recorded after address, in sorted order — so a movement with several old addresses asks about
each of them and the answer names the one Git paired, which is exactly the extra, labelled fact an
inference may add. A movement whose addresses are all the same asks nothing at all.

**`with_rename_inferences` asks at most once and only decorates.** It is called with the movements the
traversal built and the route movement, selects the movements that name two different recorded
addresses, and — only when there are any — measures once and attaches the labelled value to exactly
those movements; every other movement keeps what it already displayed and the stream keeps its own
order, so nothing is reordered, created or dropped because of an inference. `_inference_for` builds one
of the three states: the pairing sentence names the paths and the similarity the Git record reported
and states that it "is not proof that the invariant moved"; the `not_paired` sentence names every
address pair that was asked about and states that a path which changed without a rename pairing is a
deletion and an addition rather than a move; the `unavailable` sentence carries the reason and claims no
inference either way.

### Conventions

`__all__` publishes the command constant, the two observation values, the seam type, the sources value
and the four functions. `RenamePair`, `RenameObservations`, `RenameInferenceSources` and
`RenameInferenceProbe` are the module's own values/seam; the wire value is
`models/knowledge/review_relationships.py`'s `ReviewRenameInference`, whose validator refuses an
inferred state without the pair Git reported, a non-inferred state that carries paths, and an
`unavailable` state carrying a similarity word. The module writes nothing and derives no side, identity
or attribution from what it measures.

### Invariants And Boundaries

- **The basis can only be Git's own detection.** The literal has one member, so no caller can record a
  rename of its own as though a tool had measured it.
- **A measured absence and an unmeasured inference are different states**, and neither is rendered as
  the other; a similarity word exists only where a pairing was measured.
- **The two trees are addressed by object id.** No branch, working tree or `HEAD` is substituted, and
  the command a reader reproduces names both bound ids (or states that a side named no tree).
- **The inference proves nothing.** No side, identity, attribution or association is built from it, and
  the traversal that displays the movement never reads it — the movement is the pair of recorded
  anchors and the inference travels beside it.
- **Boundaries.** A real Git rename-detection failure is measured through the substituted seam (a
  production `unavailable` through an unreadable object store shares the branch but is not measured
  here); rendering the labelled inference in the browser is `ICR-R24`'s.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring and
twenty definitions, the Git runner it calls, the wire value it fills, the traversal that calls it last,
and the cases that measure the three states.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the two-tree measurement, the labelled value, and the rule that a rename is never proof that an invariant moved.** | `git_rename_inference` | mcp/src/agents_remember/application/review_rename_inference.py:1-19; mcp/src/agents_remember/application/review_rename_inference.py:96-125 |
| The published surface: the command, the observation and sources values, the seam and the four functions. | `__all__` | mcp/src/agents_remember/application/review_rename_inference.py:30-41 |
| **The declared command with both bound tree objects substituted and never a branch, a working tree or `HEAD`.** | `RENAME_INFERENCE_COMMAND`; `rename_command`; `_tree_word` | mcp/src/agents_remember/application/review_rename_inference.py:47-47; mcp/src/agents_remember/application/review_rename_inference.py:180-191; mcp/src/agents_remember/application/review_rename_inference.py:194-199 |
| The three stated reasons an inference was not measured, and the two Git status letters that carry two paths in the `-z` raw form. | `_MISSING_TREE_RENAME_DETAIL`; `_UNROOTED_RENAME_DETAIL`; `_UNPARSED_RENAME_DETAIL`; `_TWO_PATH_STATUSES` | mcp/src/agents_remember/application/review_rename_inference.py:61-64; mcp/src/agents_remember/application/review_rename_inference.py:57-60; mcp/src/agents_remember/application/review_rename_inference.py:53-56; mcp/src/agents_remember/application/review_rename_inference.py:51-51 |
| **One Git rename record, and the honesty boundary between a measured non-pairing and an unmeasured inference.** | `RenamePair`; `RenameObservations` | mcp/src/agents_remember/application/review_rename_inference.py:68-73; mcp/src/agents_remember/application/review_rename_inference.py:77-88 |
| The seam the inference is measured through, so a case measures one review with a substituted observation. | `RenameInferenceProbe`; `no_rename_inference` | mcp/src/agents_remember/application/review_rename_inference.py:93-93; mcp/src/agents_remember/application/review_rename_inference.py:128-132 |
| **The two bound trees and the seam as one measurement, with the answer or the reason it was not measured.** | `RenameInferenceSources` | mcp/src/agents_remember/application/review_rename_inference.py:136-152 |
| **The inference asked at most once and attached only to movements whose recorded addresses differ, with the stream's order untouched.** | `with_rename_inferences`; `moved_pairs`; `_with_inference` | mcp/src/agents_remember/application/review_rename_inference.py:155-177; mcp/src/agents_remember/application/review_rename_inference.py:202-220; mcp/src/agents_remember/application/review_rename_inference.py:223-235 |
| **The three states as sentences: the pairing that states it is not proof, the measured non-pairing that names every pair asked about, and the unmeasured one that claims no inference either way.** | `_inference_for`; `_addressed` | mcp/src/agents_remember/application/review_rename_inference.py:238-288; mcp/src/agents_remember/application/review_rename_inference.py:291-294 |
| The declared record format reader that refuses an output which is not this interface's. | `_rename_pairs` | mcp/src/agents_remember/application/review_rename_inference.py:297-331 |
| The wire value, whose validator keeps a pairing and its state one fact and refuses a similarity word on an unmeasured inference. | `ReviewRenameInference`; `RenameInferenceState` | mcp/src/agents_remember/models/knowledge/review_relationships.py:221-255; mcp/src/agents_remember/models/knowledge/review_relationships.py:105-105 |
| The traversal that calls this module last, after the movements exist. | `relationship_movements` | mcp/src/agents_remember/application/review_relationship_movement.py:142-177 |
| The Git runner the measurement goes through. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:150-214 |
| **The cases that measure the inference: a source rename displayed as a labelled Git inference, the same rename with no authored edge producing a retraction and an addition rather than a movement, and the separation of a measured absence from a measurement never made.** | `test_a_source_rename_is_displayed_as_a_labelled_git_inference`; `test_the_same_rename_with_no_authored_edge_is_a_retraction_and_an_addition`; `test_the_rename_inference_separates_a_measured_absence_from_a_measurement_never_made` | mcp/tests/test_knowledge_review_relationship_movement.py:607-637; mcp/tests/test_knowledge_review_relationship_movement.py:675-717; mcp/tests/test_knowledge_review_relationship_reach.py:544-591 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It asks one repository's Git object store one
question about two tree ids that belong to it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`, confirmed from the enclosure contract): **created.** The module is new in this leaf (`ICR-R08@v1`) and this is its one-to-one card. It records the packet's rename clause as a value rather than a comment: Git's own detection over two bound tree objects, a basis that can only be `git_rename_detection`, three states that keep a measured pairing, a measured non-pairing and an unmeasured inference apart, the exact command that reproduces the measurement, and the sentence that states the inference is not proof that the invariant moved. It also records that the inference is attached after the movements exist and is never read back, and the measured boundary that a real Git detection failure is exercised through the substituted seam. **Basis accounting:** the verification pair above names this leaf's base, the last real commit the reading was taken against; the candidate is named here in the body rather than in a metadata row, and closeout owns the stamp once the code commit exists.
