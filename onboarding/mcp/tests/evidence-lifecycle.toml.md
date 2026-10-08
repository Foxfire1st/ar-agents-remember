# mcp/tests/evidence-lifecycle.toml

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The machine-readable inventory of durable test evidence: shared test-support modules, fixtures,
recordings, recording generators and migration proofs. Every governed file has one `[[artifact]]`
row that declares who owns it, what it proves, how long it lives, which executable contract replaces
it, and which test modules or source files consume it. Every stable contract identity has one
`[[contract]]` row. `load_evidence_inventory` in
`mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py` loads and validates
the file.

## Current master-retirement registration

The consumers of the `mcp/tests/curator_coherence_test_support.py` artifact include `test_abandoned_series_closeout.py`, `test_master_retirement.py` and `test_standalone_master_retirement.py`, and the consumer list of the `mcp/tests/fixtures/repository_profiles/node/package-lock.json` artifact includes `test_master_retirement.py` and `test_standalone_master_retirement.py`. No governed contract or artifact is added.

## Code Commentary

### Structure

- Two top-level values: `schema_version = "ar-test-evidence-lifecycle/v3"` and
  `large_fixture_bytes`, the size from which any non-source file under `mcp/tests` counts as a
  governed fixture.
- `[[contract]]` rows with `id`, `owner` (an existing file) and `evidence_node` (a file and an exact
  `::` selector of an existing function or method). Every contract must be referenced by at least
  one artifact.
- `[[artifact]]` rows with `path`, `kind`, `authority`, `owner`, `category`, `fidelity`, `cadence`,
  `source_version_or_generator`, `introduced_by`, `lifetime`, either `permanence_rationale` or
  `expires_after`, `replacement_contract` (`contract:<id>` or `node:<file>::<selector>`),
  `consumer_scope` and `consumers`.
- `consumer_scope` is `exact` (the listed test modules), `exact-source` (the listed source files)
  or `all-tests` (no list; every current test module).

The contract rows stand before the artifact rows.

### Which files need a row

`governed_artifact_paths` in `evidence_governance.py` decides it. Under `mcp/tests` these are: data
files (`.json`, `.jsonl`, `.yaml`, `.yml`, `.csv`, `.bin`), Python files that are not test modules,
files whose name has a task or date shape (the word `baseline` or six digits as a part of the name),
and any non-source file of at least `large_fixture_bytes` bytes. The lane manifest
`mcp/tests/test-evidence-lanes.toml` and the Python files directly in `scripts/e2e_harness` are
governed too. This catalog itself is not. The loader checks both directions: a governed file
without a row and a row without a governed file are both findings. The catalog also holds the
shared supports of the Paseo runtime, launch and sandbox tests, each with its declared fidelity
and exact consumers; a declaration records fixture ownership, never that evidence ran.

### Canonical form

The contract rows are ordered by `id`, the artifact rows by `path`, and every `consumers` list is in
ascending order, without duplicates, written as `consumers = [`, one path per line, `]`. The loader
refuses a catalog that is not in this form; each finding names the row and the command that repairs
it:

```text
python -m agents_remember_test_support.testing.evidence_lifecycle --project-root . --write
```

The command orders rows and lists, removes duplicate lines, and sets the `consumers` list of an
`exact` or `exact-source` row to the set that the dependency facts derive from the source tree. A
row for which the source tree shows no consumer keeps its list as written, and the command says so.
The command also removes a consumer line whose file does not exist, as long as the row keeps a
consumer. It adds and removes no row and changes no other line of a row. It refuses a form that its
line rewrite does not read (a table header that does not stand at the start of its own line, a list
key not written as `consumers = [`, a list that is not closed by `]` on its own line, a comment
inside a list) and then writes nothing. The loader refuses such a header too, and it refuses every
list that is not written with one path per line.

### Maintaining the file

- A change that adds a test file lists the file in its lane in the lane manifest and runs the
  command. The command adds the file to every `consumers` list the source tree supports. No line of
  this catalog is typed by hand for it.
- A change that adds a governed file (a support module, a fixture, a recording) adds its
  `[[artifact]]` row by hand, and a `[[contract]]` row when the artifact's replacement is a new
  contract identity; the command then orders the rows and derives the consumers.
- A change that retires a governed file removes its row by hand, and its contract row when nothing
  else references it. The command removes no row: it names a row whose artifact file does not
  exist, and the loader refuses that row.
- No test compares the bytes of this file, the number of its rows or the number of test files with
  a constant.

### Registering a test module

A new test module that reaches a governed artifact, directly or through a support module it imports, is
added to the `consumers` list of each such `exact` row. The two modules
`mcp/tests/test_reviewer_worklist_process.py` and `mcp/tests/test_reviewer_worklist_reads.py` are listed
on the row of the Node lockfile fixture
`mcp/tests/fixtures/repository_profiles/node/package-lock.json`, because the dashboard fixture they use
reaches it.

### Merging

`.gitattributes` declares `merge=union` for this file. When two changes add lines to the same list,
Git keeps both sides' lines and reports no conflict. A union merge can damage the file in four
ways. The loader refuses each of them. It runs in the validator command (Git hook gate, quality
plan), in the selection graph and in `test_the_repository_catalogs_are_in_canonical_form`, which a
default unit run includes.

- A line that both sides added can remain twice, and the merged list can be out of order. The
  loader refuses both and the command repairs both.
- A line that one side deleted can come back when the other side changed the lines next to it. A
  consumer line that came back is refused by the loader (a consumer whose file is gone, or a
  consumer the source tree does not support) and removed by the command. The row of a retired
  artifact that came back is refused by the loader (`cataloged artifact does not exist`) and is
  deleted again by hand.
- Two whole rows that two changes added at the same place can be interleaved, which leaves a file
  that does not parse. The loader's refusal then says so and gives the recovery: restore the file
  from the landed commit and add this change's row again. Then run the command. The command refuses
  to write an unparseable file.
- A side whose catalog is not in canonical order doubles the rows. The loader refuses the doubled
  rows as duplicates, and the command refuses them with the advice to restore the file from the
  landed commit and to add that side's own lines again.

The command keeps a comment that follows a table header on its line, and comment lines that stand
directly above a table header, with that row. It refuses a comment inside a list.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The catalog's consumer list names `test_leaf_handover.py` and `test_leaf_handover_review_rounds.py`; the lane catalog registers `test_leaf_retirement_wording.py`. No module artifact rows were added for the three new test modules, and the changed wording and turn-truth test artifacts keep their existing rows.

## 260928-MIK-L93 — a question for the developer goes up the chain

The R93 wording test `mcp/tests/test_developer_question_wording.py` is added to the consumer lists the source tree supports; no artifact or contract row changes, and the canonical form is unchanged.

## Shared Causal Test Helpers

The conversation-open, Eve event-pump and reviewer-worklist-process supports are permanent,
internal hand-authored artifacts. Each has an existing behavior-test owner, an exact executable
replacement contract, fidelity/cadence and source-derived consumers. They own explicit resolution,
stream completion or subprocess opportunities; cases and product assertions remain with their test
modules. Consumer-list changes follow actual source relations, including new cache/scanner tests
and the state suite's real conftest import. These declarations do not prove a test executed.

## Evidence

- The schema version and the large-fixture threshold at the top of the file. [1]
- A contract row: identity, owner file and exact evidence node. [2]
- The canonical-form findings for the layout, contract rows, artifact rows and consumers lists. [6]
- Which files are governed, and that this catalog is excluded. [7]
- The rewrite that orders rows and lists, derives the consumer lists and removes consumer lines of missing files. [8]
- The union merge attribute for this file. [9]
- The real catalogs load through their loaders, which includes the canonical-form refusal. [10]
- The governed files equal the cataloged paths in both directions. [11]
- A line that the union brings back for a deleted file is refused and then removed by the command. [12]

- The loader that validates the file and refuses a catalog that is not canonical. [13]
- The Node lockfile fixture's row: an exact consumer scope and the start of its consumer list. [94]

## 260928-MIK-L96 The host test modules

`evidence-lifecycle.toml` gained revised durable-artifact consumer sets/paths for the new host test modules (`test_paseo_install_contract`, `test_paseo_install_no_stop`, `test_paseo_node`, `test_paseo_start`, `test_dashboard_host`, `test_host_release_contract`, `test_paseo_host_environment`) and for the moved host modules. This file holds artifact consumers plus the executable `replacement_contract`/`consumers` records; it declares no lane tables and no knowledge-invariant identities. Lane membership for the host modules lives in `test-evidence-lanes.toml`, and knowledge proof identities live in the sidecar proof plane; a catalog declaration still never shows evidence ran.



- Conversation-open support declares its permanent owner and real replacement contract. [96]
- Eve event support declares its permanent owner and exact consumers. [97]


## Refreshed current evidence

- The durable-artifact consumer entries this catalog now declares; lane rows belong to test-evidence-lanes.toml. [14]
- The two reviewer worklist test modules on that row's consumer list. [95]
- Worklist process support declares its permanent local-composition contract. [98]
