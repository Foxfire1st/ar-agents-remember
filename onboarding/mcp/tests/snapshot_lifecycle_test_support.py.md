# mcp/tests/snapshot_lifecycle_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/snapshot_lifecycle_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T11:30+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`|
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
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
|  The registry contract and artifact row that declare this module's owner, fidelity and exact consumers. | "contract:knowledge-snapshot-lifecycle-cases" | mcp/tests/evidence-lifecycle.toml:1263-1263  |
| The lane registration that keeps both consumer modules collectable. | "mcp/tests/test_knowledge_candidate_workspace.py"; "mcp/tests/test_knowledge_snapshot_publication.py" | mcp/tests/test-evidence-lanes.toml:70-70; mcp/tests/test-evidence-lanes.toml:87-87; mcp/tests/test-evidence-lanes.toml:89-89; mcp/tests/test-evidence-lanes.toml:88-88; mcp/tests/test-evidence-lanes.toml:90-92; mcp/tests/test-evidence-lanes.toml:76-83; mcp/tests/test-evidence-lanes.toml:98-105; mcp/tests/test-evidence-lanes.toml:107-107; mcp/tests/evidence-lifecycle.toml:42-42; mcp/tests/evidence-lifecycle.toml:1258-1258; mcp/tests/test-evidence-lanes.toml:109-109; mcp/tests/evidence-lifecycle.toml:1256-1256; mcp/tests/evidence-lifecycle.toml:1297-1297; mcp/tests/test-evidence-lanes.toml:84-84 |
|  The registry contract and artifact row that declare this module's owner, fidelity and exact consumers. | "contract:knowledge-snapshot-lifecycle-cases" | mcp/tests/evidence-lifecycle.toml:1263-1263  |
| The lane registration that keeps both consumer modules collectable. | "mcp/tests/test_knowledge_candidate_workspace.py"; "mcp/tests/test_knowledge_snapshot_publication.py" | mcp/tests/test-evidence-lanes.toml:70-70; mcp/tests/test-evidence-lanes.toml:76-92; mcp/tests/test-evidence-lanes.toml:98-105; mcp/tests/test-evidence-lanes.toml:107-107; mcp/tests/evidence-lifecycle.toml:42-42; mcp/tests/evidence-lifecycle.toml:1258-1258; mcp/tests/test-evidence-lanes.toml:109-109; mcp/tests/evidence-lifecycle.toml:1256-1256; mcp/tests/evidence-lifecycle.toml:1297-1297; mcp/tests/test-evidence-lanes.toml:84-84 |
| The application seam this harness admits destinations through. | `admitted_candidate_destination`; `create_knowledge_candidate`; `publish_knowledge_snapshot` | mcp/src/agents_remember/application/knowledge_snapshot.py:67-82; mcp/src/agents_remember/application/knowledge_snapshot.py:102-107; mcp/src/agents_remember/application/knowledge_snapshot.py:134-139 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-19T22:28:52+00:00: Generated citation repair: "contract:knowledge-snapshot-lifecycle-cases" repointed to mcp/tests/evidence-lifecycle.toml:1263-1263. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "contract:knowledge-snapshot-lifecycle-cases" repointed to mcp/tests/evidence-lifecycle.toml:1263-1263. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T20:45:09+02:00 — 260915-KS-L23 post-closeout clearance (change set on `ar/260915-ks-l23`, memory base `ce3028e9`, code `5e4eb651`): **cleared the 2 enforced `citation_anchor_absent_from_range` rows in this document.** The closeout's own code commit appended one `consumers` registration above every construct these cards cite, so each cited range ended exactly one line above the line that now carries the anchor row. Widened to the carrying line: `mcp/tests/evidence-lifecycle.toml:1260-1260` → `mcp/tests/evidence-lifecycle.toml:1260-1261` (rows 103, 105). Every line the author cited stays inside its range; no claim, Anchor cell or other range was dropped or re-worded, and each named anchor now resolves inside the widened range.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-snapshot-lifecycle-cases" repointed to mcp/tests/evidence-lifecycle.toml:1260-1260. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "contract:knowledge-snapshot-lifecycle-cases" repointed to mcp/tests/evidence-lifecycle.toml:1260-1260. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-snapshot-lifecycle-cases" repointed to mcp/tests/evidence-lifecycle.toml:1257-1257. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "contract:knowledge-snapshot-lifecycle-cases" repointed to mcp/tests/evidence-lifecycle.toml:1257-1257. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-snapshot-lifecycle-cases" repointed to mcp/tests/evidence-lifecycle.toml:1253-1253. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-snapshot-lifecycle-cases" repointed to mcp/tests/evidence-lifecycle.toml:1253-1253. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-snapshot-lifecycle-cases" repointed to mcp/tests/evidence-lifecycle.toml:1136-1136. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-snapshot-lifecycle-cases" repointed to mcp/tests/evidence-lifecycle.toml:1136-1136. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "contract:knowledge-snapshot-lifecycle-cases" repointed to mcp/tests/evidence-lifecycle.toml:1134-1134. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand while resolving the memory sync** — `contract:knowledge-snapshot-lifecycle-cases`, `mcp/tests/test_knowledge_candidate_workspace.py`, `mcp/tests/test_knowledge_snapshot_publication.py`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand** — `mcp/tests/test_knowledge_candidate_workspace.py`, `mcp/tests/test_knowledge_snapshot_publication.py`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-17T19:11:00+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `mcp/tests/test_knowledge_candidate_workspace.py` in the row 104 of this card from mcp/tests/test-evidence-lanes.toml:69-69 to mcp/tests/test-evidence-lanes.toml:70, the extent of the construct the claim is about (the checker named line(s) [70] as its live location); re-pointed `mcp/tests/test_knowledge_snapshot_publication.py` in the row 104 of this card from mcp/tests/test-evidence-lanes.toml:70 to mcp/tests/test-evidence-lanes.toml:79, the extent of the construct the claim is about (the checker named line(s) [79] as its live location)

- 2026-09-16T09:30:00+00:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new shared snapshot-lifecycle harness. It records the one-runner/one-probe-set design and why it is shared rather than copied (both suites measure isolation, closure, durability and recovery the same way), the through-the-public-operations rule with its two declared raw-state exceptions, the real-child-interpreter crash probe that makes the recovery claim a process fact rather than a simulated one, and the registry contract with an exact two-consumer list whose node is a real node in a consumer. Verification metadata remains empty until closeout stamps the code commit.
