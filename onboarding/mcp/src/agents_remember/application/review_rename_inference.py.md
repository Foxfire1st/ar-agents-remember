# mcp/src/agents_remember/application/review_rename_inference.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Git's rename detection over the two bound code trees of a review, as a labelled inference. The module
asks Git once, over two tree objects and never over a branch, a working tree or `HEAD`, and attaches the
answer beside relationship movements that the recorded anchors already established. The inference says
which recorded old path looks like the file that moved. It creates, moves and attributes nothing.

## Code Commentary

- **The measurement.** `git_rename_inference(before, after)` runs `git diff` with `PARSED_DIFF_OPTIONS`
  (`--no-color`, `--no-ext-diff`, `--src-prefix=a/`, `--dst-prefix=b/`) and `--raw -z --find-renames` on
  the two tree IDs, in the after side's repository. The explicit options keep the output in the format
  `_rename_pairs` parses whatever the user's Git configuration sets for colour, external drivers and
  prefixes.
- **Three answers.** `RenameObservations.available` separates a measurement from its absence. A side
  without a tree ID, a side without a repository root, a failed Git call and output that is not the
  NUL-delimited record format each give `available=False` with the reason and no pairs. Two trees that
  share no rename give `available=True` with no pairs.
- **Parsing.** `_rename_pairs` walks the records: a metadata token starts with `:` and has five fields; a
  status that begins with `R` or `C` carries two paths, every other status one. Paths are kept verbatim.
  Any token that does not fit returns `None`, so a partial read is never reported as "no rename".
- **Attaching.** `with_rename_inferences(movements, route, sources)` asks for the inference only when a
  movement names two different recorded paths (`moved_pairs`), and then once for the review. Each such
  movement gets a `ReviewRenameInference` in one of three states: `inferred` with the paired paths and
  Git's similarity, `not_paired`, or `unavailable` with the reason. Movements keep their order; none is
  added or dropped.
- **The published command.** `rename_command` fills `RENAME_INFERENCE_COMMAND`, the text
  `git diff --no-color --no-ext-diff --src-prefix=a/ --dst-prefix=b/ --raw -z --find-renames
  {before_tree} {after_tree}`, with the two tree IDs, or with `<no such tree requested>` for a side
  without one. The text is built from the same `_RENAME_ARGS` tuple the measurement passes to Git,
  `PARSED_DIFF_OPTIONS` included.
- `RenameInferenceSources` carries the two exact trees and an optional probe. `_inference_for` reports the absence of a measurement when the probe is absent; it does not run a substitute Git command. The former `no_rename_inference` factory is removed.

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

## Evidence

### Repo-Internal References

- `with_rename_inferences` implements the retained boundary described above. [25]
- `_inference_for` implements the retained boundary described above. [26]
- `git_rename_inference` implements the retained boundary described above. [27]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the uncommitted candidate: the module's own docstring and
twenty definitions, the Git runner it calls, the wire value it fills, the traversal that calls it last,
and the cases that measure the three states.

- **The module's own statement of the two-tree measurement, the labelled value, and the rule that a rename is never proof that an invariant moved.** [28]
- The published surface: the command, the observation and sources values, the seam and the four functions. [29]
- **The declared command with both bound tree objects substituted and never a branch, a working tree or `HEAD`.** [30]
- The three stated reasons an inference was not measured, and the two Git status letters that carry two paths in the `-z` raw form. [31]
- **One Git rename record, and the honesty boundary between a measured non-pairing and an unmeasured inference.** [32]
- The seam the inference is measured through, so a case measures one review with a substituted observation. [33]
- **The two bound trees and the seam as one measurement, with the answer or the reason it was not measured.** [34]
- **The inference asked at most once and attached only to movements whose recorded addresses differ, with the stream's order untouched.** [35]
- **The three states as sentences: the pairing that states it is not proof, the measured non-pairing that names every pair asked about, and the unmeasured one that claims no inference either way.** [36]
- The declared record format reader that refuses an output which is not this interface's. [37]
- The wire value, whose validator keeps a pairing and its state one fact and refuses a similarity word on an unmeasured inference. [38]

- The traversal that calls this module last, after the movements exist. [39]

- The Git runner the measurement goes through. [40]

- The cases that measure the movement inference: a source rename is never a recorded movement and carries no inference, the same rename with no authored edge is a retraction and an addition, and a side that did not resolve exactly keeps its own state and reason. [41]


### Cross-Repo References

No cross-repository behavior is implemented in this file. It asks one repository's Git object store one
question about two tree ids that belong to it.

No applicable cross-repository source was found.
