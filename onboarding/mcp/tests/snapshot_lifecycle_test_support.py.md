# mcp/tests/snapshot_lifecycle_test_support.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The shared harness for the two snapshot-lifecycle suites. Both modules measure the same four things — one
admitted candidate, the write boundary it publishes, the file-level durability facts, and one **real process
crash** — and a per-module copy would let the two disagree about how isolation, closure or recovery is measured.
This module owns that construction plus the probes a case needs.

It is test support, not production code: it decides nothing, and every builder goes through the **public typed
operations** so a case cannot prove something the operations do not do.

## Code Commentary

### Logic

- `build_case` / `SnapshotCase` is the one runner: a temporary directory holding a candidate directory, an
  admitted destination built through `application.knowledge_snapshot.admitted_candidate_destination`, and the
  repository/namespace identity the case was built for. `create`, `clone`, `clone_from`, `derive_case` and
  `open_candidate` are the lifecycle verbs a case composes, each returning a `SnapshotCase` so cases chain.
- `write_record` authors one real record through the **candidate-change batch** (`change_candidate`), which is what
  makes the published bytes carry authored work rather than an empty schema; `write_label_on_live_store` and
  `add_raw_invariant` are the two deliberate exceptions — a label edit through the store's own guarded operation,
  and a raw row insert for the states the operations forbid.
- `publish` drives `publish_candidate_snapshot`; `publication_state` drives the read-side gate;
  `publish_prepared`-style direct installs go through `publish_prepared_snapshot`, so a case can address the
  reusable half as well as the composed one.
- The **probes** are the module's second job, because the interesting claims are file-level rather than row-level:
  `journal_peer_names` (what SQLite left beside a database), `read_journal_mode`, `logical_identity_of`,
  `read_identity`, `read_schema_name`, `row_counts`, `file_digest`, `statement_present`, `byte_copy` (a main-file
  copy that must **not** carry a WAL-resident committed batch) and `vacuum`.
- `crash_and_abandon` is the real-crash half: it runs a **child interpreter** (`_CRASH_SCRIPT`) that opens the
  candidate, writes through the batch, and then leaves a second connection holding an open write transaction
  before the process exits without committing and without closing — which is what a killed runtime looks like on
  disk. `CrashOutcome` reports what the child left behind, so a case can assert that the committed batch survived
  and the abandoned one did not.

### Conventions

- Every value is built through the public operations; the two raw helpers exist only to construct state the
  operations refuse to produce.
- The module is registered with the evidence-lifecycle registry as `knowledge-snapshot-lifecycle-cases`
  (`mcp/tests/evidence-lifecycle.toml`) with an **exact** consumer list of the two suites, and the registry
  validator derives real importers and refuses a differing declared set — a new importer must be added to that row
  in the same change.
- Its evidence node is a real node in one consumer
  (`test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not`), so the row is not a claim about
  a helper nobody exercises.
- `CODE_TREE_ID` / `MEMORY_TREE_ID` are fixed 40-character object ids so a case's receipt carries deterministic
  inputs without needing a Git repository.

### Invariants And Boundaries

- **Through-the-public-operations is the rule**, with exactly two declared exceptions whose entire purpose is to
  construct a state the operations forbid.
- **The crash probe is a real process, not a simulated one.** The suite's recovery claim rests on a child
  interpreter that exits with an uncommitted write transaction open.
- **File-level facts are measured, not inferred.** Journal peers, journal mode, byte digests and row counts are
  read from the artifacts themselves.
- **Test support decides nothing about the snapshot contract.** No production module imports this file, and it
  must not become a place where a publication or lifecycle rule is defined.
- **Boundary.** This module lives under `mcp/tests/**` because that is the governed artifact root the registry
  discovers; it is not a production seam.

### Todos

None recorded for this slice.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The deterministic candidate inputs a case's receipt carries. [1]
- The real-child-interpreter crash script and its open uncommitted transaction. [2]
- The one case runner and its lifecycle verbs. [3]
- The authored-write helper that drives the real batch boundary. [4]
- The publication and read-gate drivers. [5]
- The file-level probes the durability claims rest on. [6]
- The real-process crash probe, which asserts the committed batch survived rather than only reporting it. [7]
- The registry contract and artifact row that declare this module's owner, fidelity and exact consumers. [8]
- The lane registration that keeps both consumer modules collectable. [9]
- The registry contract and artifact row that declare this module's owner, fidelity and exact consumers. [10]
- The lane registration that keeps both consumer modules collectable. [11]
- The application seam this harness admits destinations through. [12]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
