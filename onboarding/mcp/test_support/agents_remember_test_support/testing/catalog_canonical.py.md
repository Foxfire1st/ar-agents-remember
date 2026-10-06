# mcp/test_support/agents_remember_test_support/testing/catalog_canonical.py

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Defines the canonical form of the two test catalogs, `mcp/tests/evidence-lifecycle.toml` and
`mcp/tests/test-evidence-lanes.toml`, and holds the code that both catalog loaders and the one
rewrite command share. Git merges the two catalogs by union (`.gitattributes`), which works only
while the catalogs are kept in one canonical form; this module is where that form is defined,
checked and written.

Canonical form means: contract rows ordered by `id`, artifact rows ordered by `path`, and every list
of paths in ascending order (plain string comparison), without duplicates, written with one path
per line.

A side whose catalogs are not in canonical order does not merge with the union: the union keeps
both orders and doubles the rows. The lifecycle loader refuses the doubled rows as duplicates and
the command refuses to repair them; its refusal says to restore the file from the landed commit and
to add that side's own lines again.

## Code Commentary

### What the loaders use

- `list_defect` names what keeps a list from canonical form: out of order (a value is greater than
  the value after it), duplicates, or both. It returns `None` for a canonical list.
- `list_findings` turns that into at most one finding for one list. The finding names the owner of
  the list (an artifact path or a lane), the defect, and the command `WRITE_COMMAND`. A value that is
  not a list of strings yields no finding here; the loaders report that shape themselves.
- `row_order_defects` returns one finding for every row whose key sorts before the key of the row
  above it. The finding names the row, the field the rows are ordered by, and `WRITE_COMMAND`. Two
  rows with the same key are not an order defect; the lifecycle loader reports them as duplicates.
- `layout_findings` checks how the lists are written. It cuts the catalog text into blocks as the
  command does and compares each `consumers` list of an artifact row, and each lane list of the
  `[files]` table, with the lines the command would write for the same values: `key = [`, one
  quoted path per line, `]`. A list written otherwise is one finding that names the row or lane and
  `WRITE_COMMAND`. When the TOML parser sees a table whose header the line scan does not find, that
  is the one finding: the command's own `_require_tables_read` message, which says how to write the
  header and names no command.
- `unreadable_catalog` builds the refusal text for a file that cannot be read or parsed: `cannot read <what> <path>: <error>`. When the error is a TOML parse error it adds
  `INTERLEAVED_ROWS_HINT`: two rows added by different leaves may have been interleaved by the
  merge; restore the file from the landed commit and add this leaf's row again. `read_catalog`
  reads and parses one catalog and raises it through the caller's own refusal type; `parse_catalog`
  does the same for text a reader already holds, such as test selection with the catalog of the
  base revision. Both loaders, the start of a test run, the helper test and test selection read
  through one of them, so none shows a bare parser error.
- `lane_files` returns the `[files]` table of a parsed lane manifest and refuses by name a manifest
  that has none.
- `LANE_CATALOG_PATH` is the lane manifest's path; `lane_manifest.py` takes its own path constant
  from it.

### The rewrite: `write_canonical_catalogs`

`write_canonical_catalogs(root)` is what `evidence_lifecycle --write` runs. It returns one report
line per change and makes no decision about the catalogs' content.

1. It reads both catalogs. A file that cannot be read or decoded, or that holds a carriage return
   (CRLF line endings), is refused.
2. It builds the repository dependency facts. A directory whose files Git cannot list, facts that
   are incomplete (for example because a Python file does not parse), and ambiguous module names are
   each refused.
3. `canonical_lifecycle_text` rewrites the lifecycle catalog. It refuses text that does not parse.
   It cuts the file into the lines before the first table and one block per table header; a comment
   may follow a header on its line, and comment lines directly above a header belong to that block
   and move with it. `_require_tables_read` refuses a catalog in which the parser sees a table whose
   header the line scan did not find (for example an indented header). A contract or artifact row
   whose key is listed twice is refused, because the command removes no row. The contract blocks
   are ordered by `id` and the artifact blocks by `path`; blocks of one table kind are written
   together, the kinds in the order in which they first appear. Blocks of any other kind keep their
   order.
4. For each artifact block, `_canonicalize_consumers` rewrites the `consumers` list. For a row whose
   `consumer_scope` is `exact` or `exact-source` the list becomes the set the dependency facts
   derive from the source tree (`observed_test_consumers`, or `observed_source_consumers` for
   `exact-source`), sorted. When the tree shows no consumer for such a row, the list is kept as
   written, sorted and without duplicates, and a report line says so. When such a row has no
   `consumers` list and the tree shows consumers, the list is appended to the block. A list of an
   `all-tests` row is only sorted and de-duplicated. A `consumers` key that the parser sees and the
   line scan does not (for example `consumers=[`) is refused by `_require_lists_read`.
5. `_drop_gone_consumers` then looks at files that no longer exist. A row whose own `path` does not
   exist is named in the report and left as it is. When at least one listed consumer exists, each
   consumer line whose file does not exist is removed and reported. When none of the listed
   consumers exists, the list is left as written, so a row is never left without a consumer.
6. `canonical_lane_text` rewrites the lane manifest: every list of the `[files]` table is sorted and
   de-duplicated, and each lane line whose file does not exist is removed and reported (`_drop_gone`).
   It never adds a path to a lane and never moves one between lanes. It refuses a manifest
   without a `[files]` table (`lane_files`) and a `[files]` header that the line scan does not
   read; a lane list that the parser sees and the line scan does not is refused too. Other tables
   are left as they are.
7. `_rewrite_lists` does the list work for both catalogs. It reads a list that starts with
   `key = [` at the start of a line and ends with a line holding only `]`, or that stands on one
   line. It refuses a list that holds a `#` character, because a comment inside a list cannot be
   kept; a list that is not closed by `]` on its own line (`_values_of`); and a list that holds
   anything but strings. It writes the list as `key = [`, one quoted value per line with two spaces
   of indent and a trailing comma, and `]`. Every other line of a block passes through unchanged. A
   list whose quotes or commas changed is rewritten in that form and reported as `rewritten with
   one path per line, in double quotes, with a comma after each path`; a change of spacing alone
   is reported once per file as `whitespace normalised`.
8. Blocks are joined with one blank line between them and the file ends with one newline.
9. Only now are the files written, and only a file whose text changed. Everything is computed
   before anything is written, so a refusal leaves both files untouched. A refusal is a
   `CatalogWriteError`.

The report names each list it changed: `derived from source (added [...], removed [...])`,
`removed N duplicate line(s)`, `reordered`, and `removed <path>: the file does not exist` for each
line of a missing file. Row reordering is reported once per table kind. A file whose text changed
although no list or row did is reported as `whitespace normalised`, and only when no other line
about that file is printed.

The command adds and removes no row and changes no line of a row other than its `consumers` list. A
second run on its own output changes nothing.

## Evidence

- The module states the canonical form and that the command makes no decision. [1]
- A list is out of order when a value is greater than the next one, and duplicated when its set is smaller than the list. [3]
- One finding per row that sorts before the row above it, naming the order field and the command. [4]
- At most one finding per list, naming its owner, the defect and the command. [5]
- The rewrite reads both catalogs, builds the dependency facts, computes both new texts and writes only afterwards. [6]
- The lifecycle catalog's rows are ordered by key, a row listed twice is refused with the advice for a side that was not canonical, and no row is added or removed. [7]
- A file with CRLF line endings is refused. [9]
- A catalog that does not parse is refused and never guessed at. [10]
- Comment lines directly above a table header belong to that table's block. [11]
- The consumers of an exact or exact-source row are set to the derived set; when the tree shows none, the list is kept as written. [12]
- What a report line says about one changed list. [14]
- The real catalogs load through both loaders, which includes every canonical-form finding. [15]
- The attribute that makes Git merge both catalogs by union. [16]
- One finding per list that is not written one path per line, or the header finding. [18]
- A table the parser sees and the line scan does not is refused. [19]
- A list the parser sees and the line scan does not is refused. [20]
- A row whose artifact file is gone is named and kept; consumer lines of missing files are removed only while a listed consumer exists. [21]
- Each list line whose file does not exist is removed and reported. [22]
- A list that is not closed by `]` on its own line is refused. [23]

- `read_catalog` and `parse_catalog` read through one shared refusal, and `lane_files` refuses a manifest without a `[files]` table by name. [24]

- The command text that every finding names, the sentence for an interleaved file and the text of the layout finding. [25]
- The lane manifest's `[files]` lists are sorted without duplicates and the lines of missing files are removed. [26]
- A list is rewritten sorted and without duplicates, one value per line; a comment inside a list is refused. [27]
- The refusal both loaders, the start of a test run, the helper test and test selection give, with the interleaving sentence on a parse error; the command gives the same sentence in its own refusal. [28]
