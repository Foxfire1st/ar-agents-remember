# mcp/src/agents_remember/application/review_source_inventory.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The source half of a review: the exact list of paths that differ between the two bound code trees, and
the source pane that renders the list with the attribution facts of the comparison. The inventory is
measured from the two tree objects alone. It reads no database, so a review without any knowledge
selection still has its complete source change list.

## Code Commentary

### The measurement

- `tree_difference_observation(before, after)` is the one observation both the review's inventory and
  the comparison's expansion use. It runs two Git commands on the two tree IDs in the after side's
  repository: `_RAW_ARGS` for status and modes and `_NUMSTAT_ARGS` for whether content is text.
- Both argument tuples start with `diff` and `PARSED_DIFF_OPTIONS` (`--no-color`, `--no-ext-diff`,
  `--src-prefix=a/`, `--dst-prefix=b/`) and end with `-z --no-renames`. The explicit options keep the
  output in the parsed format whatever the user's Git configuration sets. `--no-renames` reports a rename
  as a deletion and an addition. `-z` gives NUL-terminated records, so a path with a tab or a newline is
  carried whole.
- `_raw_records` reads alternating metadata and path tokens. An odd token count, a metadata token without
  the leading `:`, fewer or more than five fields, a mode that is not six octal digits or an empty path
  refuses the whole observation. No output at all is a measured empty change set.
- `_content_classification` maps each path to "binary or not" from `--numstat`; when that call fails or a
  record is malformed, the classification is `None` and the observation is `partial` with its entries
  intact.
- Each record becomes a `TreeChange` with a status (`added`, `deleted`, `modified`, `type_changed`, or
  `unknown` for another letter), a content kind (`submodule` and `symlink` from the mode, `binary` or
  `text` from the classification, else `unknown`), and the mode-change flag. Entries are sorted by path.
- A path with a byte that is not valid UTF-8 (`is_text_path`) is kept apart in `unrepresentable` and
  reported by its byte form (`byte_form`); the observation is then `partial`.
- A side without a tree ID, a side without a root, a failed raw call and malformed raw output each give
  `available=False` with the reason. No branch, working tree or `HEAD` is read in place of a tree.

### The inventory and the pane

- `review_inventory(before, after, probe=None, observed=None)` renders an observation as
  `ReviewSourceInventory`: state `measured` or `unavailable`, one entry per path, the `partial` flag, a
  detail sentence, the command and the two tree IDs. An observation that names paths without entries is
  listed with status and content `unknown`.
- `inventory_command` returns the text `git -C <root> diff --no-color --no-ext-diff --src-prefix=a/
  --dst-prefix=b/ --raw -z --no-renames <before> <after>`, with a placeholder for a side that named no
  tree. The text is built from the same `_RAW_ARGS` tuple the measurement passes to Git,
  `PARSED_DIFF_OPTIONS` included.
- `inventory_limitations` declares `limitation:source_inventory_unavailable` or
  `limitation:source_inventory_partial`.
- `source_pane` composes the inventory, the locations of the traversed relationships
  (`source_locations`), the relationships themselves, the attribution's three path lists and six counts.
  A count that was not measured carries its reason and no value (`_stated_or_absent`).
- `attribution_limitations` declares `limitation:unknown_attribution_changed_paths` when the attribution
  was not measured or has undetermined paths, in the second case with the counted omission.

## Evidence

- The module docstring: measured from the pair, delimiter-safe, three separate facts, failure as a state. [27]
- The two Git questions with the parsed-diff options, no renames and NUL records. [28]
- The observation: two Git calls, the unavailable answers, and the partial flag. [29]
- A path that cannot be carried as text. [30]
- The raw record reader that refuses a malformed stream. [31]
- The content classification from numstat. [32]
- The content kind of one record. [33]
- The command text of an inventory. [34]
- The inventory value for one pair. [35]
- The pane: inventory, locations, relationships, attribution lists and counts. [36]
- A count is a value or a reason, never both. [37]
- Both argument tuples hold the parsed-diff options. [38]
- The review body is identical under a hostile Git configuration. [39]
