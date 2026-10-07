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
- `RenameInferenceSources` carries the two trees and the probe together; `no_rename_inference` is the
  probe for a caller that must run no Git command.

## Evidence

- The module docstring: an inference about the source, never proof that an invariant moved. [15]
- The published command text. [16]
- A measurement, or the reason there is none. [17]
- The Git call with the parsed-diff options, and its unavailable answers. [18]
- The inference is asked once and only for movements with two different paths. [19]
- The command text with the two tree IDs. [20]
- The recorded path pairs of one movement. [21]
- The three states of an attached inference. [22]
- The record walk that refuses a malformed stream. [23]
- The option tuple for parsed diffs. [24]
