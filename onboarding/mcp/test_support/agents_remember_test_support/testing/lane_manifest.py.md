# mcp/test_support/agents_remember_test_support/testing/lane_manifest.py

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Loads `mcp/tests/test-evidence-lanes.toml`, the one explicit assignment of every current Python test
file to an evidence lane, with optional class or test-node overrides, and proves it complete
against the test files the source tree holds. No test file gets a lane by default.

## Code Commentary

### `load_lane_manifest`

The loader collects every finding and raises one `LaneManifestError` that lists them all
(`test evidence lanes have N finding(s)`).

1. It reads the manifest. A file that cannot be read or parsed is refused at once with the text of
   `unreadable_catalog` from `catalog_canonical.py` (`cannot read evidence lane manifest <path>`).
   When the cause is a TOML parse error, the refusal ends with the sentence that two rows may have
   been interleaved by a merge and that the file is restored from the landed commit. A manifest
   that parses but holds no `[files]` table is refused at once by name, before any finding is
   collected (`lane_files` from `catalog_canonical.py`).
2. Layout comes first: `layout_findings` reports each lane list that is not written with one path
   per line, naming the lane and the `--write` command, and a table header that the command does
   not read.
3. The schema version must be `ar-test-evidence-lanes/v1`, and the only top-level names are
   `schema_version`, `files` and `override`.
4. `[files]` maps each lane to a list of paths. The lane must be a known category, and it must be an
   accepting one: `diagnostic` is refused. Every accepting category must be present, also with an
   empty list.
5. Order and duplicates: a lane list that is out of ascending order or holds a duplicate is one
   finding that names the lane and the `--write` command (`list_findings` from
   `catalog_canonical.py`).
6. Each path must be repository-relative and confined. A path whose file does not exist is a
   finding that names the `--write` command, which removes such a line. A path that exists and is
   not a Python test module is a finding without the command. A path listed in two different lanes
   is the finding `conflicting file lanes`. A path listed twice in the same lane is not a conflict;
   the lane list's duplicate finding of step 5 reports it.
7. `[[override]]` rows hold exactly `selector` and `category`. The selector's file must have a base
   lane, the selector must name a current class or test node, and no selector is listed twice.
8. The declared files are compared with the test modules of the dependency facts: a test file
   without a lane and a lane row that is not a current test file are both findings. The finding for
   a test file without a lane says to list each file in its lane in the manifest and names the
   `--write` command. The facts are built from Git's file listing, so the project root must be a
   Git repository.

The keyword `build_facts` replaces `RepositoryDependencyFacts.build`, so that a caller running both
catalog loaders derives the source graph once; without it the loader builds the facts itself.

The returned `LaneManifest` carries a digest over the sorted `path=category` lines and the override
lines.

### `LaneManifest`

- `category_for_node` resolves a collected node id. It drops the parametrization suffix, requires
  the file to have a lane, and applies the most specific matching override. Two equally specific
  overrides with different categories are refused.
- `population_for` returns the files and overrides of one category.
- `compatibility_population` renders the accepted categories and the whole population; the retry
  proof binds this value, so a retry identity covers the full lane population and not only the
  selected files.

### Who calls the loader

The pytest plugin `evidence_lanes.py` calls it at collection and turns a refusal into a
`pytest.UsageError`, so a manifest that is incomplete or not canonical stops a test run before any
test executes. The validator command in `evidence_lifecycle.py` and the quality check
(`code_quality/check.py`) call it too.

## Evidence

- The path constant comes from the canonical-form module; diagnostic is not an accepting category. [2]
- A lane list that is out of order or holds a duplicate is one finding that names the lane. [4]
- A path twice in one lane is left to the lane list's finding; a path in two lanes is a conflict; a path whose file is gone names the command. [5]
- An override names an existing class or test node of a file that has a base lane. [6]
- A node's category is its file's lane unless the most specific override says otherwise. [7]
- The collection hook turns a refusal of the loader into a usage error. [8]
- The layout check both loaders call. [10]

- The loader refuses an unreadable manifest and a manifest without a `[files]` table, starts with the layout findings, checks schema and top-level names, and compares the declared files with the test modules of the source tree. [11]
- Every accepting category must be present in `[files]`. [12]
