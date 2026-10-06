# mcp/tests/test-evidence-lanes.toml

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The one explicit assignment of every current Python test file to an evidence lane. A test file has
no lane by default: a file that is not listed, a listed path that is not a current test file, and a
file listed in two lanes each stop the test collection. `load_lane_manifest` in
`mcp/test_support/agents_remember_test_support/testing/lane_manifest.py` loads and validates the
file.

## Code Commentary

### Structure

- `schema_version = "ar-test-evidence-lanes/v1"`.
- The table `[files]` with one list of test-file paths per accepting lane: `unit-regression`,
  `public-contract`, `integration`, `architecture-fitness`, `provider-conformance`,
  `stress-durability` and `migration`. Every accepting lane must be present; a lane without files
  has an empty list. `diagnostic` is not an accepting lane and may not appear.
- Optional `[[override]]` rows, each with exactly `selector` and `category`, give one class or test
  node another lane than its file's.

The Paseo runtime, bridge, launch, messaging, sandbox and previous-host cases are registered in
`unit-regression`; the real child tool-server, role-handover binding and canonical-reader
protocol cases are in `integration`. A shared support module collects no cases and gains no lane
row.

Which lane a file belongs to is an authored choice. Nothing assigns a lane automatically.

### What reads the file

- The pytest plugin `evidence_lanes.py` loads the manifest at collection. A refusal becomes a
  `pytest.UsageError`, so no test runs. Each collected item gets the marker of its lane and the
  report properties `arEvidenceCategory` and `arEvidenceLaneDigest`.
- `mcp/tests/conftest.py` reads the `integration` and `stress-durability` lists directly when
  pytest is configured. The files in those two lists get the `integration` marker, and a run with
  the mark expression `not integration` does not collect them. This is the first read of a test
  run and it does not go through the loader. A manifest that cannot be read or parsed ends the run
  there with a `pytest.UsageError` that names the file and, for a parse error, holds the sentence
  about interleaved rows.
- The validator command of `evidence_lifecycle.py` loads the manifest after the lifecycle catalog,
  and the quality check binds the manifest's digest and population into the retry proof.
- The file is governed evidence itself: it has an `all-tests` row in
  `mcp/tests/evidence-lifecycle.toml`, and the selection graph treats a change to it as a global
  test input.

### Canonical form

Every lane list is in ascending order, without duplicates, written as `<lane> = [`, one path per
line, `]`. The loader refuses a list that is not: the finding names the lane and the command that
repairs it:

```text
python -m agents_remember_test_support.testing.evidence_lifecycle --project-root . --write
```

A path listed twice in the same lane is reported as a duplicate of that lane list, not as a
conflict between lanes. The command sorts and de-duplicates the lists of `[files]` and removes each
line whose file does not exist. It never adds a path to a lane and never moves one between lanes.
It refuses a form that its line rewrite does not read (a `[files]` header that does not stand at
the start of its own line, a lane key not written as `<lane> = [`, a list that is not closed by
`]` on its own line, a comment inside a list) and a manifest without a `[files]` table, and then
writes nothing.

### Maintaining the file

A change that adds a test file adds one line with its path to the list of its lane and runs the
command, which puts the line in order and derives the consumer lists of the lifecycle catalog. A
change that deletes a test file deletes its line, or runs the command, which removes the line of a
file that does not exist. No test compares the bytes of this file or the number of its lines with a
constant.

### Merging

`.gitattributes` declares `merge=union` for this file. When two changes add a line to the same lane
list, Git keeps both lines and reports no conflict. A union merge can damage the file in three
ways. The loader, which runs at every test collection, refuses them, except a returned line that is
valid for it:

- A line that both sides added can remain twice, and the merged list can be out of order. The
  loader refuses both and the command repairs both.
- A line that one side deleted can come back when the other side changed the lines next to it. The
  lane line of a deleted test file is refused by the loader, which names the command, and the
  command removes it. The returned lane line of a file that one side moved to another lane leaves
  the file in two lanes, which the loader refuses as `conflicting file lanes`; the stale line is
  deleted by hand. A returned line that the loader accepts is not refused, for example an
  `[[override]]` row that one side removed.
- A file that does not parse any more is refused with the sentence that two rows may have been
  interleaved by the merge and that the file is restored from the landed commit. The loader, the
  command and the pytest start-up all give that sentence.

## Evidence

- The schema version, the one comment and the head of the `[files]` table. [1]
- A lane list that is out of order or holds a duplicate is one finding that names the lane. [5]
- A path twice in one lane is not a conflict between lanes, and a path whose file is gone names the command. [6]
- The collection hook loads the manifest, refuses with a usage error and marks each item with its lane. [7]
- The union merge attribute for this file. [10]
- The manifest is a global test input of the selection graph. [11]
- The lane loader names an unordered lane and a duplicated path. [13]
- The layout check that refuses a lane list not written one path per line. [14]

- The loader that validates the file against the test modules of the source tree. [18]
- The configuration hook reads the integration and stress-durability lists and explains a manifest it cannot read. [16]
- The rewrite sorts the `[files]` lists without duplicates and removes the lines of missing files. [17]
