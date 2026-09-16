# mcp/tests/evidence-lifecycle.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/evidence-lifecycle.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `7db50f8f4a67e60f9011266110ad6d0156f1a905` |
| lastVerifiedCommitDate | 2026-09-16T14:02:05+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l05` uncommitted source; base `3332a4ce7029777d49feca22b499350435a9f83c` |
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-16T13:45 +02:00 against the uncommitted KS-L5 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Declares shared test-support/fixture ownership, fidelity, lifetime, replacement contracts, and
exact consumers. The catalog currently contains **48 artifact records and nine executable replacement
contracts** (measured by `load_evidence_inventory` on the uncommitted KS-L5 candidate); those
declarations are not records that a test ran.

## Code Commentary

### Logic

Contract records bind a production owner to a retained executable node. Artifact records describe
category, authority, fidelity, cadence, source/generator provenance, lifetime and permanence/expiry
rationale, replacement evidence, and consumers. `large_fixture_bytes=25000` remains the catalog's
large-fixture discovery setting.

The closeout fixture and closeout-input support records now name
`test_public_closeout_commits_code_and_memory_without_acceptance_tools` as their replacement node.
That matches the current two-output transaction behavior and does not require a ledger publication.
The closeout-input and curator-coherence support records also declare
`test_post_integration_cleanup_guidance.py` as an exact consumer.

**260915-KS-L1 added the fifth contract and the 44th artifact**, and the pair is an application of the
governance rule rather than a formality. Contract `knowledge-identity-branching-fixture` binds the
shared branching knowledge fixture to the node
`mcp/tests/test_knowledge_store.py::test_two_same_label_successors_reopen_as_separate_revisions`, and
the matching `[[artifact]]` row declares
`mcp/tests/knowledge_fixture_test_support.py` as `shared-support` / `internal-canonical` /
`unit-regression` / `in-process` / `cadence = "affected"` / `lifetime = "permanent"` with
`consumer_scope = "exact"` and one observed consumer.

Two facts about that row are load-bearing for a future reader:

- **The artifact path had to be governed for the row to be registrable at all.**
  `governed_artifact_paths` discovers durable support under `mcp/tests/**` plus a small fixed root set;
  `mcp/test_support/**` is not in that set, so a catalogued row naming
  `mcp/test_support/agents_remember_test_support/testing/knowledge_fixture.py` is a stale row, and a
  module outside the test roots has no derivable test-consumer proof either. The fixture therefore
  lives under `mcp/tests/`, and moving it back silently breaks this registry.
- **A declared consumer list is checked against the source, not trusted.** The validator derives each
  governed artifact's actual test importers and refuses a set that differs from the declared one, so a
  stale count is a hard failure rather than a rounding error.

**260915-KS-L2 corrected the fixture's consumer set and added the sixth contract and the 45th
artifact.** Two changes, each an application of the same rule:

- The `knowledge-identity-branching-fixture` row's `consumers` list was **wrong, not merely thin**: it
  named one module while the L2 surface had made the fixture's identity scenario the base of four more.
  It now declares all five source-observed importers
  (`test_knowledge_family_revision.py`, `test_knowledge_graph_reads.py`, `test_knowledge_relation_rules.py`,
  `test_knowledge_revision_seals.py`, `test_knowledge_store.py`), and its
  `source_version_or_generator` and `permanence_rationale` were widened to say that the same builder now
  carries the graph scenario as well as the branching-identity one. The row's `introduced_by` stays
  `260915-KS-L1`: L1 introduced the artifact, L2 extended it in place rather than forking it.
- A new contract `knowledge-graph-case-support` binds `mcp/tests/knowledge_graph_test_support.py` —
  `shared-support` / `internal-canonical` / `unit-regression` / `in-process` / `cadence = "affected"` /
  `lifetime = "permanent"` / `consumer_scope = "exact"` — to the node
  `mcp/tests/test_knowledge_family_revision.py::test_the_family_lineage_rule_matches_the_invariant_rule`,
  with exactly three declared consumers (the three graph modules; the seals module builds its own
  seeds and does not import it). Its permanence rationale records the two real reasons a per-module copy
  would be worse: three focused modules would otherwise drift from one another, and the raw
  family-revision/edge writes are the only way to construct the cyclic state the lineage rule is
  exercised against.

The documented "intent, not observation" caveat now applies only forward: the KS-L2 rows are observed,
and a **later** leaf that is expected to extend either artifact must add itself to the relevant
`consumers` list in the same change, because the validator compares that list to the source.

**260915-KS-L3 added the seventh contract and the 46th artifact, and corrected one existing consumer
list.** The candidate-batch leaf needed a harness no existing support module could carry:

- A new contract `candidate-batch-case-harness` binds `mcp/tests/candidate_batch_test_support.py` —
  `shared-support` / `internal-canonical` / `unit-regression` / `in-process` / `cadence = "affected"` /
  `lifetime = "permanent"` / `consumer_scope = "exact"` — to the node
  `mcp/tests/test_candidate_batch_transaction.py::test_a_late_invalid_command_rolls_back_every_earlier_insert_in_the_batch`
  (a real, passing node), with exactly two declared consumers, the two candidate-batch modules. Its
  `source_version_or_generator` says what the harness builds rather than naming a generator: an admitted
  destination built through `initialize_knowledge_namespace` plus contexts resolved through
  `resolve_candidate_context`. That sentence is the contract — a future edit that hand-writes a context
  would break exactly what the harness exists to guarantee.
- The `knowledge-identity-branching-fixture` row gained `test_knowledge_label_operations.py` as a sixth
  observed consumer, because the new label-operations suite builds its cases on that fixture. The row's
  declared set is derived from the source by the validator, so the addition was mandatory rather than
  optional bookkeeping.

Other artifact categories and ownership declarations retain their own scopes. Consumer rows are
accounting for source-observed support use, including transitive use where declared; they do not
establish acceptance, installed-executor fidelity, or a production run.

**260915-KS-L4 added the eighth contract and the 47th artifact.** The snapshot leaf's two suites measure the same
four things — one admitted candidate, the write boundary it publishes, the file-level durability facts, and one
real process crash — so a per-module harness would let the two disagree about how isolation, closure or recovery
is measured:

- A new contract `knowledge-snapshot-lifecycle-cases` binds `mcp/tests/snapshot_lifecycle_test_support.py` —
  `shared-support` / `internal-canonical` / `unit-regression` / `in-process` / `cadence = "affected"` /
  `lifetime = "permanent"` / `consumer_scope = "exact"` — to the node
  `mcp/tests/test_knowledge_snapshot_publication.py::test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not`,
  with exactly two declared consumers (the two snapshot modules). That node is chosen deliberately rather than
  for convenience: it is the measurement that distinguishes a **closed** snapshot from a bare main-file copy, so a
  future edit that weakens the harness's freeze path breaks the contract's own subject.
- Its `source_version_or_generator` names what the harness builds rather than a generator: one admitted candidate
  created through the lifecycle operation, records authored through the candidate-change batch, closed snapshots
  published through the publication operation, and one real crash child interpreter. A future edit that
  hand-writes a snapshot, or that simulates the crash in-process, would break exactly what the harness guarantees.
- The two consumer modules were added to `test-evidence-lanes.toml`'s `unit-regression` lane in the same change
  (rows 69 and 75), because an unregistered consumer module is not in the certifying collection path.

**260915-KS-L5 added the ninth contract and the 48th artifact.** The merge leaf's two suites need the same four
things — an authored dataset, a real three-commit branching scenario carrying its ancestry evidence, the
measurements a refusal is judged by, and one explicit way to shape an unusual side state *before* the commits are
built — so a per-module copy would let the two modules disagree about what a base, a side or an input-preservation
check is measured against:

- A new contract `common-base-merge-cases` binds `mcp/tests/merge_case_test_support.py` —
  `shared-support` / `internal-canonical` / `unit-regression` / `in-process` / `cadence = "affected"` /
  `lifetime = "permanent"` / `consumer_scope = "exact"` — to the node
  `mcp/tests/test_knowledge_guarded_merge.py::test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate`,
  with exactly two declared consumers (the merge unit module and the merge boundary module). That node is chosen
  deliberately rather than for convenience: it is the measurement that both sides' own work survives into a
  **closed, published** candidate with no verdict field attached, so a future edit that drops a side's work, that
  publishes a live file, or that lets a compatibility judgement into the outcome breaks the contract's own subject.
- Its `source_version_or_generator` names what the harness builds rather than a generator: one repository namespace
  authored through the real store operations, two sides derived from one base state, and a temporary Git repository
  whose base commit and two child commits hold those datasets. A future edit that hand-writes a dataset, or that
  reduces the ancestry evidence to fixture bookkeeping, would break exactly what the harness guarantees.
- The two consumer modules were registered in `test-evidence-lanes.toml` in the same change — the unit module in
  `unit-regression` (row 73) and the boundary module in `integration` (row 139) — because an unregistered consumer
  module is not in the certifying collection path, and because the boundary module could not go in the unit lane:
  the unit population sits exactly at its declared ceiling after this leaf.

### Conventions

The catalog is a policy/configuration input and is not counted as an artifact inside itself.
Fidelity, lifetime, and test grouping answer different questions. Current source declarations
supersede historical per-leaf consumer positions and population counts retained below.

### Invariants And Boundaries

- Replacement node references must name the retained real test definition.
- Exact consumer declarations must correspond to actual support use; stale counts are not authority.
- A `[[artifact]]` row's path must be discoverable by `governed_artifact_paths`, which is a different
  question from whether the module exists and is imported.
- Registry consistency and permanent-support rationale do not claim execution or certification.
- Ledger retirement changes the closeout replacement node, not unrelated artifact ownership.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the current working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The schema version and the large-fixture discovery threshold remain explicit. | `schema_version`; `large_fixture_bytes` | mcp/tests/evidence-lifecycle.toml:1-2 |
| The four retained non-knowledge contracts and their evidence nodes. | `ar-durable-store/1.0-process-race-evidence`; `conversation-control-public-route-contract`; `next-supported-pi-rpc-activity-recording`; `synthetic-test-evidence-candidate` | mcp/tests/evidence-lifecycle.toml:4-22 |
| Closeout fixture support names the retained code/memory transaction replacement. | `closeout_fixture_test_support.py` | mcp/tests/evidence-lifecycle.toml:264-281 |
| Closeout-input support declares the cleanup-guidance consumer. | `closeout_input_test_support.py` | mcp/tests/evidence-lifecycle.toml:282-308 |
| The knowledge branching fixture's contract and artifact row, whose consumer list 260915-KS-L2 corrected to the five source-observed importers. | `knowledge-identity-branching-fixture` | mcp/tests/evidence-lifecycle.toml:1031-1057 |
| The knowledge graph case-support contract and its matching artifact row, added by 260915-KS-L2 with three declared consumers. | `knowledge-graph-case-support` | mcp/tests/evidence-lifecycle.toml:1059-1082 |
| The candidate-batch case-harness contract and its artifact row, added by 260915-KS-L3 with two declared consumers and a real evidence node. | `candidate-batch-case-harness` | mcp/tests/evidence-lifecycle.toml:1084-1106 |
| **The snapshot-lifecycle contract and artifact row this leaf added, with an exact two-consumer list and a real evidence node.** | `knowledge-snapshot-lifecycle-cases` | mcp/tests/evidence-lifecycle.toml:1108-1130 |
| **The common-base-merge contract and artifact row this leaf added, with an exact two-consumer list and a real evidence node.** | `common-base-merge-cases` | mcp/tests/evidence-lifecycle.toml:1132-1151 |
| **The node that makes that contract's claim real: both sides' disjoint edits survive into a closed, published candidate that carries no verdict.** | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/test_knowledge_guarded_merge.py:248-312 |
| **The node that makes that contract's closedness claim real: a WAL-resident batch is published whole while a main-file copy is not.** | "test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not" | mcp/tests/test_knowledge_snapshot_publication.py:81-110 |
| The lane rows that keep the knowledge test modules in the certifying collection path, including the two this leaf registered. | `unit-regression` | mcp/tests/test-evidence-lanes.toml:5-73 |
| The one-to-one card for the batch harness, which records what it builds through the real seam. | "One admitted candidate built through the real seam" | onboarding/mcp/tests/candidate_batch_test_support.py.md:1-40 |
| The snapshot harness card, which records the registered owner and the exact consumer set. | "knowledge-snapshot-lifecycle-cases" | onboarding/mcp/tests/snapshot_lifecycle_test_support.py.md:1-40 |
| The referenced transaction test definition exists in the current source. | "test_public_closeout_commits_code_and_memory_without_acceptance_tools" | mcp/tests/test_transaction_only_worktree_delivery.py:211-318 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): measured the catalog rather than carrying the L4 numbers — **48 artifacts and 9 contracts** (`load_evidence_inventory` on the frozen uncommitted candidate, and `evidence-lifecycle: PASS (48 governed artifacts)` from the public validator) — and recorded the one contract/artifact pair this leaf added: `common-base-merge-cases` for `mcp/tests/merge_case_test_support.py`, with an explicit artifact row, an exact two-consumer list, and an evidence node whose subject is precisely what the harness exists to make measurable (both sides' own work surviving into a **closed, published** candidate with no verdict attached). The card also records that the two consumer modules were registered in the same change — the unit module in `unit-regression` and the boundary module in `integration`, the latter because the unit population sits exactly at its declared ceiling — and that the snapshot contract's own ranges above were re-derived after this leaf's insertion moved them. Verification metadata remains closeout-owned.
- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): measured the catalog rather than carrying the L3 numbers — **47 artifacts and 8 contracts** (counted on the frozen uncommitted candidate) — and recorded the one contract/artifact pair this leaf added: `knowledge-snapshot-lifecycle-cases` for `mcp/tests/snapshot_lifecycle_test_support.py`, with an exact two-consumer list, an explicit artifact row, and a chosen evidence node
  (`test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not`) whose subject is precisely what the harness exists to make measurable. The card also records that the two consumer modules were registered in the `unit-regression` lane in the same change. **This pass also completed the superseded table migration for this document**: both remaining `Finding | Citations | Source Path` tables were rewritten to `Finding | Anchor | Source` with `path:start-end` citations resolving to the working source, which clears the three pre-existing `citation_table_columns_wrong` findings this card carried. Verification metadata remains closeout-owned.
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): measured the catalog rather than carrying the L2 numbers — **46 artifacts and 7 contracts** (`load_evidence_inventory` on the frozen candidate) — and recorded the two changes this leaf made: (1) a new contract `candidate-batch-case-harness` for `mcp/tests/candidate_batch_test_support.py` with an explicit artifact row, an evidence node that is a real passing node, and exactly two declared consumers (the two batch modules); its `source_version_or_generator` states the harness builds an admitted destination plus contexts *resolved* through the application seam, which is the property a future edit must not break; (2) the `knowledge-identity-branching-fixture` row gained `test_knowledge_label_operations.py` as a sixth observed consumer, because the new standalone label suite builds on that fixture — the validator derives real importers and refuses a differing declared set, so the addition was mandatory. Verification metadata remains closeout-owned.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): measured the catalog rather than carrying the L1 numbers — **45 artifacts and 6 contracts** (`load_evidence_inventory` on the frozen candidate) — and recorded the two changes the graph leaf made: (1) it **corrected the branching fixture's consumer list**, which named one module while five now import it, and widened that row's `source_version_or_generator` and `permanence_rationale` to state that the same builder carries the graph scenario as well (the artifact's `introduced_by` stays `260915-KS-L1`: it was extended in place, not forked); (2) it added contract `knowledge-graph-case-support` for `mcp/tests/knowledge_graph_test_support.py` with exactly three declared consumers. The "declared consumers are intent, not observation" caveat is now narrowed to a forward rule: the validator derives each artifact's real test importers and refuses a differing declared set, so a later leaf that extends either artifact must add itself to that row in the same change. Verification metadata remains closeout-owned.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): recorded the fifth contract `knowledge-identity-branching-fixture` and the 44th artifact row for the shared branching knowledge fixture (`shared-support`, `internal-canonical`, `unit-regression`, `in-process`, `permanent`, `consumer_scope = "exact"`, one observed consumer), corrected the populated counts in the Purpose and Logic text to the measured 44 artifacts / 5 contracts, and recorded that the artifact's governed path is why the fixture lives under `mcp/tests/**` — a row naming the module's former `mcp/test_support/**` location is stale by construction and its consumer proof is underivable. The anticipated L2–L8 consumers are named as intent in the fixture's own card and deliberately not listed as declared consumers here. Verification metadata remains closeout-owned.

- 2026-09-15T01:02 UTC — Updated the documented replacement-node spelling for code/memory-only closeout and the two cleanup-guidance consumer declarations; retained registry ownership/fidelity/lifetime semantics and separated them from execution evidence. Working candidate verified by source inspection; commit metadata records real committed history only.

### Preserved earlier registry notes

The following earlier-card notes retain their historical scope. Their uses of “current”, counts, and source-line positions describe those earlier passes; the working-source references above supersede them.

### CCR-L42 current candidate

The evidence registry now records the atomic-master review public and scope tests as exact consumers of existing shared support artifacts; the additions refine ownership accounting and do not claim test execution or certification.

### 260831-LOCR-L32 Three Consumer Rows

The leaf's new `mcp/tests/test_worktree_status_terminal_next_tool.py` was added as an exact
consumer of three existing shared-support artifacts — no artifact row was added, removed or
re-categorised, so the catalog's population is unchanged:

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:336` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:395` |
| `mcp/tests/lifecycle_enclosure_test_support.py` | `publish_test_enclosure` — the suite's terminal-archive fixture is a real published enclosure | `mcp/tests/evidence-lifecycle.toml:471` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.
The L4 producer-census insertion shifted all three rows by one line (from `:330`/`:383`/`:461`), and this
card names the current positions.

### 260831-LOCR-L34 Two More Consumer Rows

The leaf's new `mcp/tests/test_checkpoint_landing_end_to_end.py` was added as an exact consumer of the
same two shared-support artifacts the L32 suite consumes, again through `QueueFixture`'s transitive
composition. No artifact row was added, removed or re-categorised, so the declared population is
unchanged; the insertion did shift the later consumer rows, which are re-derived below.

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:305` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:364` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.
The L4 producer-census insertion moved all of these rows by one line: the L32 rows now resolve at `:334`,
`:391` and `:467`, the L34 rows at `:304` and `:361`, and this card names the current positions. The L32
rows' own shift history is recorded in the L32 section above.

### 260831-LOCR-L37 Two More Consumer Rows

The leaf's new `mcp/tests/test_pause_stop_only_end_to_end.py` was added as an exact consumer of the
same two shared-support artifacts every other `QueueFixture`-based boundary suite consumes, reached
transitively through that fixture's composition. No artifact row was added, removed or re-categorised,
so the declared population is unchanged; the insertion did shift the later consumer rows, which are
re-derived below.

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:322` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:380` |

The leaf's other new module, `mcp/tests/test_pause_is_not_publication.py`, is deliberately **not** a
consumer of any artifact here: it parses the source tree with `ast` and resolves module paths, so it
composes no fixture and installs no support. Consumer declarations are ownership accounting only; they
are not execution or acceptance evidence.

The L4 producer-census insertion moved these two rows by one line (from `:319` and `:376`), and this
card's references now name the current lines. The L36 rows moved with the earlier insertions
(`closeout_input_test_support.py` artifact row resolves at `:283` unchanged, `curator_coherence_test_support.py` at `:340`, the
`lifecycle_enclosure_test_support.py` artifact row at `:452` with the L32 suite's consumer entry at
`:467`), and this card's references now name the current lines.

### 260831-LOCR Seal Removal — Two More Consumer Rows

The change set's new `mcp/tests/test_lifecycle_playthrough_end_to_end.py` was added as an exact
consumer of the same two shared-support artifacts every other `QueueFixture`-based boundary suite
consumes, reached transitively through that fixture's composition. No artifact row was added, removed
or re-categorised, so the declared population is unchanged; the insertion did shift the later consumer
rows, which are re-derived below.

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:322` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:375` |

The L4 producer-census insertion did **not** move these two rows: it was added after them in both lists,
so their positions are unchanged. Consumer
declarations are ownership accounting only; they are not execution or acceptance evidence.

### 260913-LCA-L4 Two More Consumer Rows

The leaf's new `mcp/tests/test_memory_attribution_producers.py` was added as an exact consumer of two
existing shared-support artifacts, both reached transitively through the `QueueFixture` composition its
carryover case builds. No artifact row was added, removed or re-categorised, so the declared population
stays 42 shared-support artifacts and four executable replacement contracts:

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_fixture_test_support.py` | transitive closeout/lifecycle fixture composition the carryover case's `QueueFixture` relies on | `mcp/tests/evidence-lifecycle.toml:319` |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition, same fixture | `mcp/tests/evidence-lifecycle.toml:378` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.

### 260913-LCA-L5 Two More Consumer Rows

The leaf's new `mcp/tests/test_leaf_doc_master_link_binding.py` was added as an exact consumer of the
same two shared-support artifacts, reached transitively through `test_worktree_support` —
`initialized_memory_repo` imports both. No artifact row was added, removed or re-categorised, so the
declared population stays 42 shared-support artifacts and four executable replacement contracts
(measured: 42 `[[artifact]]` and 4 `[[contract]]`).

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition `test_worktree_support` imports | `mcp/tests/evidence-lifecycle.toml:316` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same import | `mcp/tests/evidence-lifecycle.toml:375` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.
Two insertions — one in each consumer list — shift everything after them, so the current positions,
measured by line number in the current file, are: the closeout-input `path` cell `:283` (unchanged) with
its block now `282-338`, the curator-coherence `path` cell `:341` with its block now `340-396`, and the
`lifecycle_enclosure_test_support.py` `path` cell `:454`. The earlier per-leaf sections above record
their own as-of positions and should be read that way; the reference table above names the current ones.

### 260913-LCA-L7 Two More Consumer Rows

The leaf's new `mcp/tests/test_closeout_projection_source_classification.py` was added as an exact
consumer of the same two shared-support artifacts every other closeout boundary suite consumes. The
module imports `QueueFixture`, `REPO` and `SPRINT` from the sibling `test_closeout_queue` fixture
rather than rebuilding the world, and that fixture's own imports carry both supports —
`curator_coherence_test_support` directly and `closeout_input_test_support` through
`test_worktree_support`, whose `initialized_memory_repo` imports it. No artifact row was added, removed
or re-categorised, so the declared population is unchanged (measured: 42 `[[artifact]]` and 4
`[[contract]]`).

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the shared `QueueFixture` relies on | `mcp/tests/evidence-lifecycle.toml:307` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same fixture | `mcp/tests/evidence-lifecycle.toml:366` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.
Two insertions — one in each consumer list — shift everything after them, so the current positions,
measured by line number in the current file, are: the closeout-input `path` cell `:283` (unchanged) with
its block now `282-339`, the curator-coherence `path` cell `:342` with its block now `341-398`, and the
`lifecycle_enclosure_test_support.py` `path` cell `:456`. Every later row moved by one line: the L5
entries `:315` → `:316` and `:373` → `:375`; the L4 census `:318` → `:319` and `:376` → `:378`; the
playthrough `:317` → `:318` and `:376` → `:377`; the pause suite `:321` → `:322` and `:380` → `:381`;
the L32 suite `:335` → `:336`, `:394` → `:395` and `:470` → `:471`; the L36 suite `:308` → `:309` and
`:367` → `:368`; and the L34 suite `:304` → `:305` and `:363` → `:364`. The earlier per-leaf sections
above record their own as-of positions and should be read that way; the reference table above names the
current ones.

### 260913-LCA-L8 Nine More Consumer Rows

The leaf's new `mcp/tests/test_terminal_blocker_reasons.py` was added as an exact consumer of nine
existing shared-support artifacts. No artifact row was added, removed or re-categorised, so the
declared population stays 42 shared-support artifacts and four executable replacement contracts
(measured: 42 `[[artifact]]` and 4 `[[contract]]`).

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | imported directly by `integration_branch_authority_test_support`, whose landing fixture builds the whole-tool world | `mcp/tests/evidence-lifecycle.toml:331` |
| `mcp/tests/curator_coherence_test_support.py` | reached through `selected_lifecycle_test_support`, whose closeout-operation input composes it | `mcp/tests/evidence-lifecycle.toml:391` |
| `mcp/tests/integration_branch_authority_test_support.py` | imported directly: `_authority_fixture` and `_closed_external_leaf_worktrees` build the real landed leaf each whole-tool case starts from | `mcp/tests/evidence-lifecycle.toml:435` |
| `mcp/tests/repository_profile_test_support.py` | imported directly by the landing fixture (`AGENTS_REMEMBER_PROFILE_REFERENCE`) | `mcp/tests/evidence-lifecycle.toml:565` |
| `mcp/tests/fixtures/repository_profiles/node/package.json` | the declared profile fixture that same support reads | `mcp/tests/evidence-lifecycle.toml:604` |
| `mcp/tests/fixtures/repository_profiles/node/package-lock.json` | the declared profile fixture that same support reads | `mcp/tests/evidence-lifecycle.toml:643` |
| `mcp/tests/gate_certification_test_support.py` | reached through `selected_lifecycle_test_support` → `test_closeout_certification_entrypoint` | `mcp/tests/evidence-lifecycle.toml:955` |
| `mcp/tests/source_selection_test_support.py` | reached through `repository_profile_test_support`, which imports `source_selection_fixture` | `mcp/tests/evidence-lifecycle.toml:1012` |
| `mcp/tests/selected_lifecycle_test_support.py` | imported directly by the landing fixture (`selected_closeout_operation_input`) | `mcp/tests/evidence-lifecycle.toml:1038` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.
Each insertion shifts everything after it, so the current positions, measured by line number in the
current file, are: the closeout-input `path` cell `:283` (unchanged) with its block now `282-341`, the
curator-coherence `path` cell `:343` with its block now `342-401`, and the
`lifecycle_enclosure_test_support.py` `path` cell `:459`. Every later row moved: the L5 entries
`:316` → `:315` and `:375` → `:375` (up one and unchanged — `test_cross_master_concurrency.py` moved
after it in the same list); the L4 census `:319` → `:320` and `:378` → `:380`; the playthrough
`:318` → `:318` and `:377` → `:378`; the pause suite `:322` → `:322` and `:381` → `:382`; the L32 suite
`:336` → `:337`, `:395` → `:397` and `:471` → `:474`; the L36 suite `:309` → `:312` and `:368` →
`:372`; the L7 suite `:307` → `:307` and `:366` → `:367`; and the L34 suite `:304` → `:304` and
`:364` → `:364` (unchanged). The earlier per-leaf sections above record their own as-of positions and
should be read that way; the reference table above names the current ones.




- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the frozen catalog gained
  the `checkpoint_landing_test_support.py` artifact, so the declared population is 43
  shared-support/fixture artifacts plus four replacement contracts. Corrected the Purpose population
  count; the artifact blocks and every cited row were re-read. Verification metadata remains
  closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (flag resolved): the code worktree is frozen, so
  the earlier flag is now measured rather than conditional. `mcp/tests/evidence-lifecycle.toml`
  carries the inserted `checkpoint_landing_test_support.py` artifact block at `:342-361`, which
  leaves `path = "mcp/tests/curator_coherence_test_support.py"` at `:363` — the position this row
  already cites — and `path = "mcp/tests/closeout_input_test_support.py"` at `:283`. The pair
  `283-283` / `363-363` is confirmed against the frozen tree, and the flag above stands as the
  record of the interim state it described. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): this row cites the
  curator-coherence artifact path at `mcp/tests/evidence-lifecycle.toml:363`, which is its position
  in the current working tree, where the in-flight `checkpoint_landing_test_support.py` artifact
  block sits above it. The committed HEAD still carries that path at `:343`; the two forms differ
  only by that uncommitted insertion, so the citation is correct for the tree this leaf is being
  curated against and must be re-measured if the insertion does not land. Flagged rather than
  silently chosen; verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 0 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T15:05+02:00 — 260913-LCA-L8 curator (uncommitted change set on `ar/260913-lca-l8-ar`):
  registered the leaf's new `mcp/tests/test_terminal_blocker_reasons.py` as an exact consumer of nine
  existing shared-support artifacts — `closeout_input_test_support.py` (`:331`),
  `curator_coherence_test_support.py` (`:391`), `integration_branch_authority_test_support.py`
  (`:435`), `repository_profile_test_support.py` (`:565`), the two `repository_profiles/node` fixture
  files (`:604`, `:643`), `gate_certification_test_support.py` (`:955`),
  `source_selection_test_support.py` (`:1012`) and `selected_lifecycle_test_support.py` (`:1038`) —
  the first two through the shared closeout/worktree fixture composition and the landing/authority
  fixture, the rest through the repository-authority and certification-profile composition the landed
  fixture carries. No artifact row was added, removed or re-categorised, so the declared population is
  unchanged (measured: 42 `[[artifact]]`, 4 `[[contract]]`). Re-derived every position this card
  cites against the current file: the closeout-input `path` cell stays `:283` with its block
  `282-341`, the curator-coherence `path` cell is `:343` with its block `342-401`, and
  `lifecycle_enclosure_test_support.py` is `:459`; among consumer rows the L5 suite is
  `:315`/`:375`, the L4 census `:320`/`:380`, the playthrough `:318`/`:378`, the pause suite
  `:322`/`:382`, the L7 suite `:307`/`:367`, the L32 suite `:337`/`:397`/`:474` and the L36 suite
  `:312`/`:372`. Corrected the reference rows that named pre-insertion values (the two artifact block
  ranges `282-339`/`341-398` → `282-341`/`342-401`, the curator-coherence `path` cell `:341` → `:343`,
  the enclosure fixture `:456` → `:459`, the L32/L34/L37/L5/L4/playthrough/L36/L7 consumer entries)
  and added the row for the nine new consumer edges. Verification metadata is **not** advanced: the
  code commit does not exist and closeout owns the stamp; no acceptance claim.
- 2026-09-14T14:20+02:00 — 260913-LCA-L7 curator (uncommitted change set on `ar/260913-lca-l7`):
  registered the leaf's new `mcp/tests/test_closeout_projection_source_classification.py` as an exact
  consumer of `closeout_input_test_support.py` (row 307) and `curator_coherence_test_support.py` (row
  366), both reached transitively through the sibling `test_closeout_queue` fixture it imports its
  world from. No artifact row was added, removed or re-categorised, so the declared population is
  unchanged (measured: 42 `[[artifact]]`, 4 `[[contract]]`). Re-derived every position this card cites
  against the current file: the closeout-input `path` cell stays `:283` with its block `282-339`, the
  curator-coherence `path` cell is `:342` with its block `341-398`, and
  `lifecycle_enclosure_test_support.py` is `:456`; among consumer rows the L5 suite moved to
  `:316`/`:375`, the L4 census to `:319`/`:378`, the playthrough to `:318`/`:377`, the pause suite to
  `:322`/`:381`, the L32 suite to `:336`/`:395`/`:471` and the L36 suite to `:309`/`:368`. Corrected
  four reference rows that named pre-insertion values (the two artifact block ranges
  `282-338`/`340-396` → `282-339`/`341-398`, the L5 consumer entries `:315`/`:373` → `:316`/`:375`, the
  L4 census `:318`/`:376` → `:319`/`:378`, and the playthrough `:317`/`:375` → `:318`/`:377`) and added
  the row for the new consumer edge. Verification metadata is **not** advanced: the code commit does
  not exist and closeout owns the stamp; no acceptance claim.
- 2026-09-14T07:05+02:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): registered the leaf's new `mcp/tests/test_leaf_doc_master_link_binding.py` as an exact
  consumer of `closeout_input_test_support.py` (row 315) and `curator_coherence_test_support.py`
  (row 373), both reached transitively through `test_worktree_support`, whose `initialized_memory_repo`
  imports both — measured, not inferred from the fixture name. No artifact row was added, removed or
  re-categorised, so the declared population is unchanged (measured: 42 `[[artifact]]`, 4
  `[[contract]]`). Re-derived every position this card cites, by line number in the current file: the
  closeout-input `path` cell stays `:283` with its block `282-338`, the curator-coherence `path` cell is
  `:341` with its block `340-396`, `lifecycle_enclosure_test_support.py` is `:454`; among consumer rows
  the pause suite moved to `:321`/`:379`, the L4 census to `:318`/`:376`, the playthrough to
  `:317`/`:375`, the L32 suite to `:335`/`:393`/`:469`, the L34 suite to `:304`/`:362` and the L36
  suite to `:308`/`:366`. Corrected four reference rows that named pre-insertion values (the
  curator-coherence `path` cell `:340` → `:341`, the enclosure fixture `:452` → `:454`, the two artifact
  block ranges `283-337`/`340-394` → `282-338`/`340-396`, and the pause/L4/playthrough consumer rows).
  Verification metadata is **not** advanced: the code commit does not exist and closeout owns the stamp;
  no acceptance claim.
- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): registered the leaf's new `mcp/tests/test_memory_attribution_producers.py` as an
  exact consumer of `closeout_fixture_test_support.py` (row 317) and `closeout_input_test_support.py`
  (row 374), both reached transitively through the `QueueFixture` its carryover case composes. No
  artifact row was added or re-categorised, so the declared population is unchanged. Corrected the two
  inline citations that named the *pre-insertion* block ranges
  (`closeout_input_test_support.py` 282-336 → 282-338 from its `path` cell at `:282`,
  `curator_coherence_test_support.py` 338-392 → 339-393 from its `path` cell at `:339`), which is the
  same shift this leaf's insertion causes. Verification metadata is **not** advanced: the registry's
  `lastVerifiedCommitHash` (`9c8a7a42`) predates this change set and the code commit does not exist yet,
  so closeout owns the stamp; no acceptance claim.
- 2026-09-13T20:42+02:00 — Child-admission seal removal (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): registered the new
  `mcp/tests/test_lifecycle_playthrough_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 316) and `curator_coherence_test_support.py` (row 372), both
  reached transitively through `QueueFixture`. No artifact row was added or re-categorised, so the
  declared population is unchanged; re-derived every shifted consumer row this card cites (the pause
  suite's entries 318 → 319 and 373 → 374, `curator_coherence_test_support.py` path 338 → 339,
  `lifecycle_enclosure_test_support.py` path 449 → 450 with the L32 entry 464 → 465) and corrected the
  three shared artifact-block ranges in the reference table to `282-336` and `338-392`. Verification
  metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: registered the new boundary suite
  `mcp/tests/test_pause_stop_only_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 318) and `curator_coherence_test_support.py` (row 373), reached
  transitively through `QueueFixture`, and recorded that the leaf's other new module
  (`test_pause_is_not_publication.py`) consumes no artifact because it is AST-only. No artifact row was
  added or re-categorised, so the declared population is unchanged; re-derived the shifted consumer
  rows (`curator_coherence_test_support.py` 338, `lifecycle_enclosure_test_support.py` 448, L32 entry
  463). Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T18:09+02:00 — 260831-LOCR-L36: rebound two citation ranges shifted by this leaf's two
  additions to the manifest (`mcp/tests/test_cross_master_concurrency.py` in both consumer lists): the
  curator-coherence support artifact resolves at `:337` and the enclosure/worktree fixture's `path`
  cell at `:446`. Ranges only; the artifact and consumer claims are unchanged and no verification
  stamp advanced.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:12+00:00 — 260831-LOCR-L34 curator: recorded
  `mcp/tests/test_checkpoint_landing_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 304) and `curator_coherence_test_support.py` (row 357), both
  reached transitively through `QueueFixture`. No artifact row was added or re-categorised, so the
  declared population is unchanged; the insertion shifted three later consumer rows, which are
  re-derived and re-cited here (330, 383, 459). Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:336-336. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: recorded the new
  `mcp/tests/test_worktree_status_terminal_next_tool.py` as an exact consumer of three existing
  shared-support artifacts (`closeout_input_test_support.py` at row 329,
  `curator_coherence_test_support.py` at row 381, and `lifecycle_enclosure_test_support.py` at row 457,
  the last because the suite publishes a real enclosure through `publish_test_enclosure`). No artifact
  row was added or re-categorised, so the declared population is unchanged; added three reference rows
  and a section naming each artifact's reason for the edge. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:335-335. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "mcp/tests/closeout_input_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:283-283. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:334-334. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: The evidence registry now records the atomic-master review public and scope tests as exact consumers of existing shared support artifacts; the additions refine ownership accounting and do not claim test execution or certification.

- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ02 preparation recorded the exact two R25/R26 consumers added to both shared support rows. Registry SHA `15bea1c01f402c382dad1667dec601313bb8aabfc511bb8cedac66076287606a1` and validator PASS42 are preserved as source/diagnostic evidence only; the source is uncommitted and no acceptance claim is made.
- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Registered the extracted gate fixture and publication-suite consumers in durable memory; reconciled exact-source runner ownership with the distinct pytest closure.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 registration of
  `test_gate_certificate_authority.py` as an exact consumer of the shared certification and
  closeout-input support rows whose builders its forcing suite imports. Verification is pinned
  to the owning commit.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 expanded the certification shared-support row to
  the complete five-consumer set exposed by the source graph. Verification remains closeout-owned.

- 2026-09-01T03:11+02:00 — Registered the portable certification composition owner with its two
  exact focused-suite consumers. Verification remains closeout-owned.

- 2026-08-31T12:39+02:00 — Added `test_dispatch_agent_ambient_reviewer.py` to both exact transitive
  consumer sets after the L5 closeout fast hook identified the previously undeclared ownership
  edges.

- 2026-08-30T16:32+02:00 — Added `test_public_surface_conformance.py` to both exact transitive
  consumer sets after the L4 staged fast hook exposed the source-derived ownership edges; the
  focused lifecycle validator passes with 35 governed artifacts.

- 2026-08-29T23:04+02:00 — Added `test_memory_candidate_pair.py` to the exact source-derived
  consumer sets for the closeout-input and curator-coherence test composition roots after the
  A002 lifecycle fast hook exposed both missing edges.

- 2026-08-29T12:27+02:00 — Reconciled the curator-coherence helper's declared consumers with the
  source-derived transitive ownership graph after generation 7 rejected the direct-import-only
  catalog row. Verification remains closeout-owned.

- 2026-08-29T12:10+02:00 — Registered the shared curator-coherence fixture-input owner and its
  three exact importers after the generation-6 fast hook rejected the uncatalogued helper.
  Verification remains closeout-owned.

- 2026-08-29T09:58+02:00 — Added the curator-coherence suite to the exact source-derived consumer
  set for the shared closeout-input test support after the targeted closeout gate exposed the
  missing edge.
- 2026-08-28T05:10+02:00 — Recorded the operational unknown-suffix threshold and the lifecycle
  catalog's explicit policy-input/non-artifact boundary after Q5 v19 forced the self-reference case.
- 2026-08-27T13:32+02:00 — Registered the split Ruff support and its exact consumers. Verification
  remains closeout-owned.
