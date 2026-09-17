# mcp/tests/snapshot_lifecycle_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/snapshot_lifecycle_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T11:30+02:00 |
| lastVerifiedCommitHash | `9c12e8b1ec027b8bb07f4c0cc79ef99a655ff890`|
| lastVerifiedCommitDate | 2026-09-18T01:58:08+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The deterministic candidate inputs a case's receipt carries. | `DEFAULT_AUTHORITY_HOME`; `CODE_TREE_ID`; `MEMORY_TREE_ID` | mcp/tests/snapshot_lifecycle_test_support.py:79-81 |
| The real-child-interpreter crash script and its open uncommitted transaction. | `_CRASH_SCRIPT` | mcp/tests/snapshot_lifecycle_test_support.py:85-129 |
| The one case runner and its lifecycle verbs. | `SnapshotCase`; `build_case`; `create`; `clone`; `clone_from`; `derive_case`; `open_candidate` | mcp/tests/snapshot_lifecycle_test_support.py:130-176; mcp/tests/snapshot_lifecycle_test_support.py:177-205; mcp/tests/snapshot_lifecycle_test_support.py:207-211; mcp/tests/snapshot_lifecycle_test_support.py:213-221; mcp/tests/snapshot_lifecycle_test_support.py:235-244; mcp/tests/snapshot_lifecycle_test_support.py:223-233; mcp/tests/snapshot_lifecycle_test_support.py:246-250 |
| The authored-write helper that drives the real batch boundary. | `write_record`; `write_label_on_live_store`; `add_raw_invariant` | mcp/tests/snapshot_lifecycle_test_support.py:261-291; mcp/tests/snapshot_lifecycle_test_support.py:301-321; mcp/tests/snapshot_lifecycle_test_support.py:333-345 |
| The publication and read-gate drivers. | `publish`; `publication_state` | mcp/tests/snapshot_lifecycle_test_support.py:357-380; mcp/tests/snapshot_lifecycle_test_support.py:382-390 |
| The file-level probes the durability claims rest on. | `journal_peer_names`; `read_journal_mode`; `file_digest`; `byte_copy`; `row_counts`; `logical_identity_of`; `vacuum` | mcp/tests/snapshot_lifecycle_test_support.py:410-418; mcp/tests/snapshot_lifecycle_test_support.py:433-441; mcp/tests/snapshot_lifecycle_test_support.py:404-408; mcp/tests/snapshot_lifecycle_test_support.py:453-459; mcp/tests/snapshot_lifecycle_test_support.py:420-431; mcp/tests/snapshot_lifecycle_test_support.py:443-451; mcp/tests/snapshot_lifecycle_test_support.py:323-331 |
| The real-process crash probe, which asserts the committed batch survived rather than only reporting it. | `crash_and_abandon`; `CrashOutcome` | mcp/tests/snapshot_lifecycle_test_support.py:477-533; mcp/tests/snapshot_lifecycle_test_support.py:468-475 |
|  The registry contract and artifact row that declare this module's owner, fidelity and exact consumers. | "contract:knowledge-snapshot-lifecycle-cases" | mcp/tests/evidence-lifecycle.toml:1110-1130  |
| The lane registration that keeps both consumer modules collectable. | "mcp/tests/test_knowledge_candidate_workspace.py"; "mcp/tests/test_knowledge_snapshot_publication.py" | mcp/tests/test-evidence-lanes.toml:70-83 |
| The application seam this harness admits destinations through. | `admitted_candidate_destination`; `create_knowledge_candidate`; `publish_knowledge_snapshot` | mcp/src/agents_remember/application/knowledge_snapshot.py:67-82; mcp/src/agents_remember/application/knowledge_snapshot.py:102-107; mcp/src/agents_remember/application/knowledge_snapshot.py:134-139 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `mcp/tests/test_knowledge_candidate_workspace.py` in the row 104 of this card from mcp/tests/test-evidence-lanes.toml:69-69 to mcp/tests/test-evidence-lanes.toml:70, the extent of the construct the claim is about (the checker named line(s) [70] as its live location); re-pointed `mcp/tests/test_knowledge_snapshot_publication.py` in the row 104 of this card from mcp/tests/test-evidence-lanes.toml:70 to mcp/tests/test-evidence-lanes.toml:79, the extent of the construct the claim is about (the checker named line(s) [79] as its live location)
- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new shared snapshot-lifecycle harness. It records the one-runner/one-probe-set design and why it is shared rather than copied (both suites measure isolation, closure, durability and recovery the same way), the through-the-public-operations rule with its two declared raw-state exceptions, the real-child-interpreter crash probe that makes the recovery claim a process fact rather than a simulated one, and the registry contract with an exact two-consumer list whose node is a real node in a consumer. Verification metadata remains empty until closeout stamps the code commit.
