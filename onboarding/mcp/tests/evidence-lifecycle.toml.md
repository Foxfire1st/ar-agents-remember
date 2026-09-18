# mcp/tests/evidence-lifecycle.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/evidence-lifecycle.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:05+02:00 |
| lastVerifiedCommitHash | `9f88a6de572dc15bbed1802cf08b77c1193fb24c` |
| lastVerifiedCommitDate | 2026-09-18T14:21:49+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l16` uncommitted staged source; base `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-18T04:35 +02:00 against the uncommitted KS-L14 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Declares shared test-support/fixture ownership, fidelity, lifetime, replacement contracts, and
exact consumers. **The catalog now contains 54 artifact records and thirteen executable replacement contracts**,
counted on this leaf's frozen candidate by counting the blocks (`54 [[artifact]]` and `13 [[contract]]`), with the
file's own sha256 re-measured as
`19ed0525cd94b57389052a4e19cf1f0dfe83e9c166783ead2598f6a4e0ce8ffa`; those declarations are not records that a test ran.
The six earlier counts are kept because they are different states of the same merged line, not competing
measurements: **48 / 9** at the pre-sync `KS-L6` base, **50 / 9** on the merged base `4eb2b199` (the incoming
official line's two extra artifacts), **51 / 10** after `KS-L7` added its one contract/artifact pair,
**52 / 11** after `KS-L8` added its own, **53 / 12** after `KS-L10` re-scoped the generation contract's
source/version statement and re-pinned the digest to `9b057632…`, and **54 / 13** after `KS-L11` added the pair
below.

**260915-KS-L14 added no contract and no artifact, and re-pinned the catalog digest anyway.** Its two new test
modules are ordinary test source, and the detection run suite deliberately uses the **already-registered**
fixtures rather than a third support module: `mcp/tests/diff_scope_test_support.py` and
`mcp/tests/read_scope_test_support.py` each gained one `consumers` row —
`mcp/tests/test_knowledge_detection_runs.py` at `:1278` and `:1298` respectively. That is a **consumer change
only**, so the populations stay at **13 contracts and 54 artifacts** and no artifact's `introduced_by`,
`lifetime` or `replacement_contract` moved. The catalog digest pinned in
`mcp/tests/test_dependency_ownership_ast_helpers.py` still had to move with the bytes
(`19ed0525…` → `c6956899947b0435e5cdd8cd77ba3121db77e3dbf4676bee11406c3baf03ec68`), and it was re-pinned
**deliberately, with the reason written beside the constant** rather than widened to force a green run. The
file's own sha256 on this candidate is
`c6956899947b0435e5cdd8cd77ba3121db77e3dbf4676bee11406c3baf03ec68` (`sha256sum mcp/tests/evidence-lifecycle.toml`),
and the two consumer rows are the whole of the byte change.

**260915-KS-L11 added the thirteenth contract and the 54th artifact and re-pinned the catalog digest in the
same change.** The facet suite's shared harness `mcp/tests/facet_test_support.py` is a *governed artifact*
(`shared-support` / `internal-canonical` / **`unit-regression`** / `in-process` / `cadence = "affected"` /
`lifetime = "permanent"`), registered at `:1196-1212` under the new contract `knowledge-facet-cases` at
`:1191-1194`, whose evidence node is
`mcp/tests/test_knowledge_facets.py::test_the_seam_registry_is_exactly_the_eight_declared_subtypes`. Its declared
consumers are exactly the one facet suite. The same change restated the `knowledge-generation-cases` contract's
`source_version_or_generator` and `permanence_rationale` so they describe **every** registered generation rather
than generation 1 alone — a wording change to an existing row, not a new contract. The catalog digest pinned in
`mcp/tests/test_dependency_ownership_ast_helpers.py` moved with it
(`9b057632…` → `19ed0525cd94b57389052a4e19cf1f0dfe83e9c166783ead2598f6a4e0ce8ffa`).

**260915-KS-L8 added the eleventh contract and the 52nd artifact, extended one existing consumer list, and
re-pinned the catalog digest in the same change.** The comparison's shared fixture
`mcp/tests/diff_scope_test_support.py` is a *governed artifact* (`shared-support` / `internal-canonical` /
**`integration`** / `local-composition` / `cadence = "affected"` / `lifetime = "permanent"`), registered at
`:1208-1225` under the new contract `knowledge-diff-cases` at `:1198-1201`, whose evidence node is
`mcp/tests/test_knowledge_diff_scope.py::test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union`
— the node that owns the packet's first non-conforming example, chosen deliberately rather than for convenience.
Its declared consumers are exactly the two diff modules. **`mcp/tests/read_scope_test_support.py` also gained two
consumer rows** (`:1242-1243`) because the diff fixture builds on it and the comparison's cases import it — a
**consumer change rather than a new artifact**, so that row's own `introduced_by` stays `260915-KS-L7`. The catalog
digest pinned in `mcp/tests/test_dependency_ownership_ast_helpers.py` moved with it
(`461121ca…` → `4cf81f10dbbd6b941c50887dca45154612e5e46b7135465823af3e6604db3747`). **A new test module costs
three registry touch-points, and this leaf paid all three for each of its two modules**: its lane row in
`mcp/tests/test-evidence-lanes.toml` (`:76` and `:159`), its path in the relevant artifact's `consumers` list, and
the catalog digest re-pin. Miss any one and collection fails for the whole catalog rather than for the module.

exact consumers. The catalog currently contains **54 artifact records** and four executable replacement
contracts; those declarations are not records that a test ran. 260915-CAPS-L9 adds **two consumer
rows and no artifact row**: `mcp/tests/test_capsule_experiment_install.py` and
`mcp/tests/test_install_runtime.py` join the `mcp/tests/fixtures/repository_profiles/node/package-lock.json`
artifact's `consumers` list, because the new module reads the pinned application's committed
lockfile through the installer it drives and `test_install_runtime.py` inherits the same reach
through the module it imports. The artifact set has moved since (L14 and L17 land into the same
file, and the merged pin is re-derived on the merged catalog — never restored from another
leaf's figure).

The count is re-derived from the file rather than carried: it stood at 43 when an earlier version of
this paragraph was written, measures **50 at this leaf's synced base `23cc7a72`**, and measures 51 with
this leaf's one added row.

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

**260915-KS-L6 added no contract and no artifact; it declared two new consumers in three existing lists.**  The
portable export/import leaf's two suites consume shared support that already existed — the branching knowledge
fixture (its authored dataset), the snapshot-lifecycle harness (the closed published destination a fresh install is
refused against) and the merge case harness (the dataset that came *through* L5's merge, which the roundtrip module
exports and restores). Declaring them is what the validator compares against the source, so leaving them out would
have refused the whole catalog for **any** input, and it is also the honest statement that this leaf needed no new
harness of its own:

- the `knowledge-identity-branching-fixture` row's `consumers` list gained
  `test_knowledge_portable_boundaries.py` and `test_knowledge_portable_roundtrip.py`;
- the `knowledge-snapshot-lifecycle-cases` row gained `test_knowledge_portable_boundaries.py` — **only the boundary
  module**, because the roundtrip module does not import the snapshot harness;
- the `common-base-merge-cases` row gained both portable modules.

Three consumer-list insertions move every row below them, so the five knowledge contract blocks now resolve at
`:1031-1059` (branching fixture), `:1061-1084` (graph case support), `:1086-1108` (candidate batch), `:1110-1133`
(snapshot lifecycle) and `:1135-1159` (common-base merge). The declared population is **unchanged at 48 artifacts
and 9 contracts**. The two consumer modules were registered in `test-evidence-lanes.toml` in the same change — both
in `integration` (rows 140-141) — because the unit population sits exactly at its declared ceiling.

**One new contract and one new artifact, and the pin they moved.** The leaf registers `contract:knowledge-evidence-cases` with `mcp/tests/evidence_test_support.py` as its owner and evidence node `mcp/tests/test_knowledge_evidence_claims.py::test_a_claim_reads_back_with_every_field_including_an_empty_limitations`, and one `[[artifact]]` row for that support module — kind `shared-support`, authority `internal-canonical`, category `unit-regression`, fidelity `in-process`, cadence `affected`, `introduced_by = "260915-KS-L12"`, lifetime `permanent`, `consumer_scope = "exact"` with exactly its two consuming modules named. The catalog's own validator passes and the pinned identity is re-pinned to what this candidate measures: **14 contracts and 55 artifacts**. The permanence rationale is the fixture's own reason for existing — an evidence claim resolves four links across two subject kinds and two coverage kinds, so a per-module copy of that topology would let the two modules disagree about which identity is the facet revision and which is the invariant revision, which is exactly the property the refusal cases assert. **The registered count and digest are measurements of this candidate, not constants**: a later leaf that registers its own artifact moves both, and the module docstring's re-pin precedent is the record of how.

**260915-CAPS-L15 added consumer rows only, and that is what moved the byte pin.** The new
`mcp/tests/test_capsule_launch_wiring.py` reaches three governed artifacts through the shared test
support it imports, so three `consumers` lists gained one entry each
(`mcp/tests/evidence-lifecycle.toml:351`, `:624`, `:1257`) — the same shape 260915-CAPS-L7 used. **No
artifact was registered, no row was removed, and no artifact's identity moved**: the populations are
unchanged at **4 contracts / 51 artifacts**, while the byte pin in
`mcp/tests/test_dependency_ownership_ast_helpers.py` moved `812211e9… → 3342a249…` because the file's
bytes changed. A consumer row is a catalog change; the pin is re-derived from the file, never maintained
by hand.

**`consumers` is a derived test population, and the loader enforces it.** For `consumer_scope = "exact"`
the loader re-derives the test modules that reach the artifact from the source graph and reports any
difference from the declared list, so a row's `consumers` cell is a checkable claim rather than prose.
The eve capsule row added by this leaf lists exactly the four test modules the loader derives for it —
one of which reaches the support only **transitively** through another support module. That transitivity
is why a row's `consumers` and its `permanence_rationale` can describe different things without either
being wrong: the list is the mechanical test population, the rationale is the artifact's semantic role.

Because the rows are derived from the graph, they are also what a base move invalidates. The merge that
produced this leaf's base re-derived every catalog consumer proof it touched, and **verifying that
re-derivation is a separate leaf's obligation**; a row that disagrees with the graph is a loader finding
to be repaired by its owner, not a tolerated inconsistency.

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
- **A consumer row is a catalog change.** Adding an importer to a `consumers` list moves the file's
  bytes and therefore the pin in `test_dependency_ownership_ast_helpers.py`, even when no artifact is
  registered or removed. The pin is re-derived at the changing leaf's own tip.
- **Consumer rows are accounting, never acceptance.** A row states that a test module reaches a
  support artifact; it does not claim the artifact's fidelity, that a test ran, or that a boundary was
  exercised in production.

### 260915-KS-L17 Three More Consumer Rows — No New Artifact, No New Contract

This leaf's change to the catalogue is **consumer-only**, and that is the fact a reader of this card
needs: three existing contracts' `consumers` lists gained this leaf's two composition test modules,
and **nothing else in the file moved**.

| Contract | Rows added | Why this leaf's modules belong there |
| --- | --- | --- |
| `knowledge-facet-cases` | `mcp/tests/test_knowledge_family_composition.py`; `mcp/tests/test_knowledge_family_composition_boundaries.py` | both build their admitted candidate through the facet leaf's registered helpers rather than through a third fixture of their own |
| `knowledge-generation-cases` | the same two modules | both drive the generation registry and its recorded-dataset helpers |
| `knowledge-read-scope-cases` | `mcp/tests/test_knowledge_family_composition_boundaries.py` | only the boundary module consumes the read-scope fixture, because only it compares the shipped selection by value |

**The counts are unchanged: 13 contracts and 54 artifacts.** No `[[artifact]]` and no `[[contract]]`
row was added, and no existing row's `path`, `owner`, `kind`, `authority` or `evidence_node` was
edited.

**The catalogue digest did move, and the measured value is the authority.** Three consumer rows
changed the file's bytes, so `LIFECYCLE_CATALOG_SHA256` in
`mcp/tests/test_dependency_ownership_ast_helpers.py` was re-pinned to this file's own sha256 on this
candidate:

```
2505cc7dd6eb52f9ab96bb61b25bf11ed1de50db72371d058524290c419d9eeb
```

That is exactly the value the constant carries. **The composition leaf's own turn report records a
different digest for the same re-pin, and that value appears nowhere in the tree** — so a later reader
reconciling the two should measure the file rather than trust the report.

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
| The schema version and the large-fixture discovery threshold remain explicit. | `schema_version`; `large_fixture_bytes`; "ar-test-evidence-lifecycle/v3"; "large_fixture_bytes = 25000" | mcp/tests/evidence-lifecycle.toml:1-2 |
| The four retained knowledge contracts and their evidence nodes. | "id = \"ar-durable-store/1.0-process-race-evidence\""; "id = \"conversation-control-public-route-contract\""; "id = \"next-supported-pi-rpc-activity-recording\""; "id = \"synthetic-test-evidence-candidate\"" | mcp/tests/evidence-lifecycle.toml:4-22 |
|  Closeout fixture support names the retained code/memory transaction replacement. | "closeout_fixture_test_support.py" | mcp/tests/evidence-lifecycle.toml:315-315  |
|  Closeout-input support declares the cleanup-guidance consumer. | "closeout_input_test_support.py" | mcp/tests/evidence-lifecycle.toml:333-333  |
| **The knowledge branching fixture's contract and artifact row, whose consumer list 260915-KS-L2 corrected to the five source-observed importers and 260915-KS-L6 extended to the two portable modules.** | "id = \"knowledge-identity-branching-fixture\"" | mcp/tests/evidence-lifecycle.toml:25-25 |
| The knowledge graph case-support contract and its matching artifact row, added by 260915-KS-L2 with three declared consumers. | "id = \"knowledge-graph-case-support\"" | mcp/tests/evidence-lifecycle.toml:30-30 |
| The candidate-batch case-harness contract and its artifact row, added by 260915-KS-L3 with two declared consumers and a real evidence node. | "id = \"candidate-batch-case-harness\"" | mcp/tests/evidence-lifecycle.toml:35-35 |
| **The snapshot-lifecycle contract and artifact row, with an exact consumer list that 260915-KS-L6 extended to the portable boundary module.** | "id = \"knowledge-snapshot-lifecycle-cases\"" | mcp/tests/evidence-lifecycle.toml:40-40 |
| **The common-base-merge contract and artifact row, whose exact consumer list 260915-KS-L6 extended to both portable modules.** | "id = \"common-base-merge-cases\"" | mcp/tests/evidence-lifecycle.toml:45-45 |
| **The two consumer declarations 260915-KS-L6 added to the branching-fixture row.** | "owner = \"knowledge-identity-branching-fixture\"" | mcp/tests/evidence-lifecycle.toml:1175-1175 |
| **The consumer declaration 260915-KS-L6 added to the snapshot-lifecycle row — the boundary module only, because the roundtrip module does not import that harness.** | "owner = \"knowledge-snapshot-lifecycle-cases\"" | mcp/tests/evidence-lifecycle.toml:1245-1245 |
| **The two consumer declarations 260915-KS-L6 added to the merge-case row.** | "owner = \"common-base-merge-cases\"" | mcp/tests/evidence-lifecycle.toml:1265-1265 |
| **The node that makes that contract's claim real: both sides' disjoint edits survive into a closed, published candidate that carries no verdict.** | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:307-376 |
| **The node that makes that contract's closedness claim real: a WAL-resident batch is published whole while a main-file copy is not.** | "test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not" | mcp/tests/test_knowledge_snapshot_publication.py:81-110 |
|  The lane rows that keep the knowledge test modules in the certifying collection path, including the two this leaf registered. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-73  |
| The one-to-one card for the batch harness, which records what it builds through the real seam. | "One admitted candidate built through the real seam" | onboarding/mcp/tests/candidate_batch_test_support.py.md:1-40 |
|The snapshot harness card, which records the registered owner and the exact consumer set.|"id = \"knowledge-snapshot-lifecycle-cases\""| mcp/tests/evidence-lifecycle.toml:40-40; onboarding/mcp/tests/snapshot_lifecycle_test_support.py.md:1-40 |
| The referenced transaction test definition exists in the current source. | "test_public_closeout_commits_code_and_memory_without_acceptance_tools"; `test_public_closeout_commits_code_and_memory_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:211-318 |
| None | "mcp/tests/closeout_fixture_test_support.py" | mcp/tests/evidence-lifecycle.toml:315-315 |
| Closeout-input support names the same retained code/memory transaction replacement node. | "mcp/tests/closeout_input_test_support.py" | mcp/tests/evidence-lifecycle.toml:333-333 |
| None | "mcp/tests/curator_coherence_test_support.py"; "mcp/tests/test_post_integration_cleanup_guidance.py" | mcp/tests/evidence-lifecycle.toml:380-380; mcp/tests/evidence-lifecycle.toml:421-421 |
|The snapshot harness card, which records the registered owner and the exact consumer set.|"id = \"knowledge-snapshot-lifecycle-cases\""| mcp/tests/evidence-lifecycle.toml:40-40; onboarding/mcp/tests/snapshot_lifecycle_test_support.py.md:1-40 |
| The referenced transaction test definition exists in the current source. | "test_public_closeout_commits_code_and_memory_without_acceptance_tools" | mcp/tests/test_transaction_only_worktree_delivery.py:211-318 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## KS-R15@v1 Consumer Row

One consumer row was added: `mcp/tests/test_curator_review_assessment_publication.py` is now declared a
consumer of the shared support module owned by `curator-coherence-test-port`. No contract and no
artifact was added, so the catalogue's counts are unchanged at 13 contracts and 54 artifacts while its
digest moves — the guard validates that direction explicitly, and the pin lives in
`mcp/tests/test_dependency_ownership_ast_helpers.py`.

The insertion shifted every line below it by one, so the contract and artifact rows this card cites
were re-derived from the current file: `id = "knowledge-snapshot-lifecycle-cases"` is at `:1112`,
`contract:knowledge-diff-cases` at `:1274` and `contract:knowledge-read-scope-cases` at `:1294`.

## 260915-CAPS-L9 Consumer Rows

The two added rows state reach that is real rather than decorative: the experiment module installs
and probes the pinned application by reading `package.json` and `package-lock.json`, and the
pre-existing `test_install_runtime.py` inherits the reach because it imports the installer module
that now does. Nothing was registered, no row was removed, and the populations are unchanged by
this leaf apart from its own two consumers. The byte pin over this file is re-derived **at this
leaf's tip** by the runbook recipe (`31c6983d…`, 4 contracts / 54 artifacts at the merged tip)
and never restored from a historical figure.

## KS-R16@v1 Consumer Rows

Three consumer rows were added, inside **two existing artifacts** and therefore mid-file rather than at the
end: `mcp/tests/diff_scope_test_support.py` gained one row
(`"mcp/tests/test_knowledge_family_integrity_pipeline.py",` at
`mcp/tests/evidence-lifecycle.toml:1388`) and `mcp/tests/read_scope_test_support.py` gained two
(`"mcp/tests/test_knowledge_family_integrity_pipeline.py",` and
`"mcp/tests/test_knowledge_registered_scope.py",` at `:1413-1414`). Both are already-registered
`shared-support` artifacts, so this leaf adds **no contract and no artifact**: the two block kinds still
count **14 contracts and 64 artifacts** as the constants in
`mcp/tests/test_dependency_ownership_ast_helpers.py` read them on this candidate, and only the catalogue's
bytes move — to
`143b0cf5c3a8432450f45072b7351057ba51fe6c386f65eb662c0ec4cb729ce6`, which re-hashing this file reproduces.
The one thing a reader should not take from the leaf's own prose is a count: the paragraph the worker added
beside that pin says "thirteen and fifty-four", which the declarations beside it contradict. Each insertion
shifted every line below it, which is the drift the routes citing this file carry.

## Update History
- 2026-09-18T14:05+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): **added the L16 section** — the three consumer rows this leaf appended to two existing `shared-support` artifacts, the fact that no contract and no artifact was added (so the populations stay at the 14 contracts / 64 artifacts the pin constants read), and the catalogue's new digest measured by re-hashing this file. It also records, where a successor will meet it, that the leaf's own provenance paragraph states a "thirteen and fifty-four" count the declarations beside it contradict, and that the counts here are the declarations' rather than the prose's.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "closeout_fixture_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:315-315. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "closeout_input_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:333-333. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:25-25. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-graph-case-support\"" repointed to mcp/tests/evidence-lifecycle.toml:30-30. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"candidate-batch-case-harness\"" repointed to mcp/tests/evidence-lifecycle.toml:35-35. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:40-40. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:45-45. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "owner = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:1175-1175. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "owner = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1245-1245. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "owner = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1265-1265. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:40-40. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/closeout_fixture_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:315-315. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/closeout_input_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:333-333. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py"; "mcp/tests/test_post_integration_cleanup_guidance.py" repointed to mcp/tests/evidence-lifecycle.toml:380-380; mcp/tests/evidence-lifecycle.toml:421-421. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:40-40. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "id = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1120-1120. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand while resolving the memory sync** — `id = \`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.
- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): added the **L17 registration rows and recorded the one thing a reader of this file most needs: its registrations are consumer-only.** Three `consumers` lists gained this leaf's two modules — `knowledge-facet-cases` (both), `knowledge-generation-cases` (both) and `knowledge-read-scope-cases` (the boundary module) — so **no artifact and no contract was added and the counts stay 13 contracts / 54 artifacts**. The section also records what a reader should measure rather than assume: this file's own sha256 on this candidate is `2505cc7dd6eb52f9ab96bb61b25bf11ed1de50db72371d058524290c419d9eeb`, which is exactly what `test_dependency_ownership_ast_helpers.LIFECYCLE_CATALOG_SHA256` carries — **the leaf's own report names a different, stale digest that appears nowhere in the tree**, so the file's bytes, not the report, are the authority. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 4 generated projection bullet(s) by hand** — `mcp/tests/curator_coherence_test_support.py`, `mcp/tests/closeout_input_test_support.py`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded the new `knowledge-evidence-cases` contract and its `shared-support` artifact, and re-pinned the catalog identity to what this candidate measures — **14 contracts and 55 artifacts** — rather than to the previous pin. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): **re-read this card against the changed manifest and recorded the one consumer row the leaf added.** `mcp/tests/test_curator_review_assessment_publication.py` is now a declared consumer of the shared support module owned by `curator-coherence-test-port`; no contract and no artifact was added, so the counts stay at 13 contracts and 54 artifacts while the digest moves, and the pin lives in `mcp/tests/test_dependency_ownership_ast_helpers.py`. The insertion shifted every line below it by one, so the contract and artifact rows cited in this card were re-derived from the current file: `id = "knowledge-snapshot-lifecycle-cases"` is at `:1112`, `contract:knowledge-diff-cases` at `:1274` and `contract:knowledge-read-scope-cases` at `:1294`. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): **re-measured this catalog rather than carrying the previous numbers, and recorded the consumer change that is this leaf's whole footprint.** The change set adds **five** `consumers` rows and nothing else: two on the ambient-runner artifact (`mcp/tests/test_knowledge_citation_bindings.py` and `mcp/tests/test_knowledge_citation_boundaries.py`), two on the generation-cases artifact (the same pair), and one on the knowledge-contract block (the boundary module) — so the populations are **unchanged at thirteen contracts and fifty-four artifacts**, and this is a **consumer-only** change of exactly the shape the L14 entry recorded before it. The pinned catalog digest is therefore re-pinned deliberately against this candidate, with the reason written beside the constant in `test_dependency_ownership_ast_helpers.py` rather than the value changed silently, and the provenance prose there now states this leaf's own consumer-only change as well. The file's own byte change is those five rows; a later reader can check the claim by re-hashing. The older per-leaf counts in the Purpose remain as the different states of one merged line they are. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current catalog; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T03:15:00+00:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): recorded the **consumer change that is this leaf's whole catalog footprint**, and re-measured the file rather than carrying the previous numbers. The new Purpose paragraph states it plainly: two `consumers` rows (`mcp/tests/test_knowledge_detection_runs.py` at `:1278` on `diff_scope_test_support.py` and at `:1298` on `read_scope_test_support.py`), **no new contract, no new artifact**, populations unchanged at **13 contracts / 54 artifacts**, and the deliberately re-pinned catalog digest `c6956899947b0435e5cdd8cd77ba3121db77e3dbf4676bee11406c3baf03ec68` with the reason written beside the constant in `test_dependency_ownership_ast_helpers.py` rather than widened to force a green run. It also records the measured file sha256 on this candidate and that the two consumer rows are the whole of the byte change, so a later reader can check the claim by re-hashing. The older per-leaf counts in the Purpose remain as the different states of one merged line they are. Verification metadata advances to the leaf's base commit `4264dcc9` because the body was re-read against the current catalog; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-17T23:18:00+00:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): measured the catalog rather than carrying the L8 numbers — **54 artifacts and thirteen contracts** (`54 [[artifact]]`, `13 [[contract]]`), with the file's sha256 re-measured as `19ed0525cd94b57389052a4e19cf1f0dfe83e9c166783ead2598f6a4e0ce8ffa` — against **53 / 12** at `KS-L10` (`9b057632…`) and **52 / 11** at `KS-L8`. It records the one contract/artifact pair this leaf added — `knowledge-facet-cases` for `mcp/tests/facet_test_support.py`, `unit-regression` / `in-process`, with exactly one declared consumer, `mcp/tests/test_knowledge_facets.py` — and the wording-only change to the existing `knowledge-generation-cases` row, whose source and permanence statements now describe every registered generation instead of generation 1 alone. The three-registry-touch-point rule the card states is paid in full for the new module (lane row, its path in the artifact's own consumers list, and the catalog re-pin). Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **consumer rows only** — `mcp/tests/test_capsule_experiment_install.py`
  and `mcp/tests/test_install_runtime.py` join the
  `mcp/tests/fixtures/repository_profiles/node/package-lock.json` artifact's `consumers` list, because the
  new module reads the pinned application's committed lockfile through the installer it drives and the
  pre-existing `test_install_runtime.py` inherits the same reach through the module it imports. Nothing was
  registered and no row was removed; the catalog's population delta on this leaf's own branch is zero rows
  at the artifact level. The byte pin over this file is re-derived at this leaf's tip (`31c6983d…`,
  4 contracts / 54 artifacts on the merged catalog) and never restored from a historical figure. The
  section above records what the two rows mean rather than only that they exist. Verification metadata
  remains closeout-owned: the candidate is uncommitted.
- 2026-09-17T10:50+02:00 — 260915-CAPS-L15 curator: **consumer rows only, and the byte pin moved for
  that alone.** This leaf's new acceptance module reaches three governed artifacts through the shared
  test support it imports, so three `consumers` lists each gained one entry; nothing was registered,
  removed or re-identified, and the populations stayed at 4 contracts / 51 artifacts while the pin went
  `812211e9… → 3342a249…`. The body states that shape and adds two invariants — a consumer row is a
  catalog change, and consumer rows are accounting rather than acceptance. Verification metadata moves
  to this leaf's base `15fa0e2c`; the candidate is deliberately uncommitted, so the governed closeout
  stamps the real code commit and no hash or fingerprint was invented here.


- 2026-09-17T10:32+02:00 — 260915-CAPS-L17 curator: **consumer rows only again, and the pin re-derived
  against the MERGED catalog — which is this leaf's own obligation.** The leaf's new test module
  `mcp/tests/test_eve_effort_runtime.py` starts the shipped runtime, so it consumes three
  already-governed artifacts and each `consumers` list gained one entry:
  `mcp/tests/fixtures/repository_profiles/node/package-lock.json` (L649),
  `mcp/tests/eve_capsule_test_support.py` (L736) and `mcp/tests/test_eve_adapter_test_support.py`
  (L1186). **Nothing was registered, no row was removed and no artifact's identity moved**, so the
  populations stay at **4 contracts / 51 artifacts**. The pin is **`563582a0…`**, and it is neither
  L15's `3342a249…` nor the `22ce7027…` this leaf measured before L15 landed: L15 landed first, so this
  value covers the **merged** artifact set. Re-derived and independently recomputed this pass —
  `sha256sum mcp/tests/evidence-lifecycle.toml` = `563582a0542f4a8721d1f717a48e92440c53fdf63a26b68fb43624c56ad90506`,
  matching the constant at `mcp/tests/test_dependency_ownership_ast_helpers.py:46` (counts 51 / 4 at
  `:44-:45`). The card's Purpose sentence attributing 51 to "this leaf's one added row" describes the
  L15 pass and is left as history; **the value, not the sentence, is the claim**, and the rule that a
  consumer row is a catalog change is what makes this re-derivation mandatory at each changing leaf.
  **Checker result (post-sync, verbatim).** The refusal this entry first recorded was resolved
  by the leaf's `worktree_sync`: the pair is now `leaf-candidate` / `acceptanceEligible:true` on
  code base `d8ed8c21`, and the contract-scoped `memory_quality_check` ran against this
  worktree. Headline: `ok:false`, `checklistStatus:"action-required"`,
  `coherenceStatus:"not-evaluated-quality-action-required"`, `closeoutReady:false`,
  `curatorActionableCount:1690`; census `ready-for-adjudication` (13 rows, 0 blockers, 0
  unonboarded). This card's own contribution: one `onboarding_drift_drifted` finding and one
  `style.update_history.history_order` "not newest-first" finding, the latter caused by the
  future-dated `10:50` stamp on the L15 entry below this one and not by this entry's content
  (see the `serving/overview.md` entry for the same attribution). The pin above was additionally
  recomputed directly and independently — it is `e3651d6f…` at **4 contracts / 54 artifacts**
  after L14 landed its fifty-fourth artifact, not the `563582a0…` this leaf measured pre-sync at
  51. Verification metadata moves to the synced base `d8ed8c21`; the candidate is deliberately
  uncommitted, so the governed closeout stamps the real code commit and no hash or fingerprint
  was invented here.

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): stamped the untimestamped Update History entries with this document's own commit clock

- 2026-09-17T01:31:11+00:00 — **Historical stamp carried from the incoming official line** (merge HEAD `12bd7fd3`; the live stamp for this file is the later synced value in the metadata table above, which closeout re-stamps): `lastUpdated` 2026-09-15T01:02; `lastVerifiedCommitHash` `88784fb26aab810c8a284f1e73e6f9bd727a5963`; `lastVerifiedCommitDate` 2026-09-16T08:31:51+02:00.

- 2026-09-17T01:15:00+00:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): **measured the catalog and recorded the one contract/artifact pair this leaf added, the one consumer list it extended, and the re-pin that came with them.** Counted on the frozen candidate: **52 artifact records and eleven contracts** (`52 [[artifact]]`, `11 [[contract]]`), with the file's sha256 re-measured as `4cf81f10dbbd6b941c50887dca45154612e5e46b7135465823af3e6604db3747` — the exact value re-pinned at `mcp/tests/test_dependency_ownership_ast_helpers.py:46`. Against **51 / 10** after L7, **50 / 9** on the merged base `4eb2b199` and **48 / 9** at the pre-sync `KS-L6` base: four states of one merged line, recorded as such rather than as competing counts. The new rows are the contract `knowledge-diff-cases` (`:1198-1201`) and its artifact `mcp/tests/diff_scope_test_support.py` (`:1208-1225`, `integration` / `local-composition`), declared with an exact two-consumer list, and its evidence node is the node that owns the packet's first non-conforming example rather than the first node alphabetically. The **`read_scope_test_support.py` row gained two consumer entries** (`:1242-1243`) because the diff fixture builds on the read fixture — a consumer change, so that artifact's `introduced_by` stays `260915-KS-L7` — and the card keeps the three-touch-point obligation a new test module carries, now paid twice over (lane rows `:76` and `:159`). Every earlier count in this card is retained as the as-of record of the state it measured. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.

- 2026-09-16T21:50:00+00:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): **measured the catalog and recorded the one contract/artifact pair this leaf added, together with the three-way registry obligation that pair carries.** Counted on the frozen candidate: **51 artifact records and ten contracts** (`51 [[artifact]]`, `10 [[contract]]`), against **50 / 9** on the merged base `4eb2b199` and **48 / 9** at the pre-sync `KS-L6` base — three states of one merged line, recorded as such rather than as competing counts, because the two registry sidecars and several route overviews had carried the merged numbers as pending. The new rows are the contract `knowledge-read-scope-cases` (`:1198-1201`) and its artifact `mcp/tests/read_scope_test_support.py` (`:1203-1221`), with an exactly-declared three-consumer list that fix round 2 extended by one module after splitting the over-limit integration module — a **consumer change, not a new artifact**, so the counts stay ten and fifty-one. The card also states the obligation a new test module carries and this leaf paid in full: its lane row, its path in this artifact's `consumers`, and the catalog digest re-pin (`293a187f…` → `461121ca…`) in `mcp/tests/test_dependency_ownership_ast_helpers.py`; miss any one and the whole catalog refuses rather than the module failing. Every earlier count in this card is retained as the as-of record of the state it measured. Verification metadata remains empty until closeout stamps the code commit.

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: **one artifact row added, one shared-support row
  extended, population re-measured.** The leaf's new `mcp/tests/eve_capsule_test_support.py` is
  registered as `shared-support` / `unit-regression`, owned by
  `mcp/src/agents_remember/application/eve_capsule/__init__.py`, with `consumer_scope = "exact"` and
  exactly the four consumers the loader derives for it; the two new L7 suites were added as exact
  consumers of the existing `mcp/tests/test_eve_adapter.py`-adjacent shared-support row. The declared
  population is corrected in the Purpose paragraph: **51 artifacts** at the candidate, of which 50 are
  the synced base `23cc7a72` and one is this leaf's — the previous 43 was stale and is now stated with
  the measurement it came from rather than silently replaced. A new paragraph records that `consumers`
  is a graph-derived population the loader enforces, which is why a transitively-derived consumer can
  appear in a list whose rationale describes a different role, and that verifying the merge's
  re-derivation of every touched consumer proof belongs to a separate leaf. Verification metadata moves
  to the leaf's synced base `23cc7a72`; the candidate is deliberately uncommitted, so the governed
  closeout stamps the real code commit and no hash or fingerprint was invented here.

- 2026-09-16T15:45:00+00:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): measured the catalog rather than carrying the L5 numbers — **48 artifacts and 9 contracts**, unchanged by this leaf — and recorded what this leaf actually did to it: **no new contract and no new artifact**, only two new consumer declarations across three existing lists (both portable modules in the branching-fixture row and in the `common-base-merge-cases` row, and the **boundary module only** in the `knowledge-snapshot-lifecycle-cases` row, because the roundtrip module does not import that harness). The card states why that is a contract obligation rather than bookkeeping: the validator derives each artifact's real test importers and refuses a declared set that differs, so leaving them out would refuse the catalog for any input. It also records that the three insertions moved the knowledge blocks — now `:1031-1059`, `:1061-1084`, `:1086-1108`, `:1110-1133` and `:1135-1159` — and re-derived the two long-stale block ranges this card still carried from 2026-09-13 (`closeout_input_test_support.py` `282-341` → `282-308`, `curator_coherence_test_support.py` `342-401` → `329-390`, both re-measured against the working file rather than shifted). Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l06`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.

- 2026-09-16T11:45:00+00:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): measured the catalog rather than carrying the L4 numbers — **48 artifacts and 9 contracts** (`load_evidence_inventory` on the frozen uncommitted candidate, and `evidence-lifecycle: PASS (48 governed artifacts)` from the public validator) — and recorded the one contract/artifact pair this leaf added: `common-base-merge-cases` for `mcp/tests/merge_case_test_support.py`, with an explicit artifact row, an exact two-consumer list, and an evidence node whose subject is precisely what the harness exists to make measurable (both sides' own work surviving into a **closed, published** candidate with no verdict attached). The card also records that the two consumer modules were registered in the same change — the unit module in `unit-regression` and the boundary module in `integration`, the latter because the unit population sits exactly at its declared ceiling — and that the snapshot contract's own ranges above were re-derived after this leaf's insertion moved them. Verification metadata remains closeout-owned.

- 2026-09-16T09:30:00+00:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): measured the catalog rather than carrying the L3 numbers — **47 artifacts and 8 contracts** (counted on the frozen uncommitted candidate) — and recorded the one contract/artifact pair this leaf added: `knowledge-snapshot-lifecycle-cases` for `mcp/tests/snapshot_lifecycle_test_support.py`, with an exact two-consumer list, an explicit artifact row, and a chosen evidence node

- 2026-09-16T08:10:00+00:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): measured the catalog rather than carrying the L2 numbers — **46 artifacts and 7 contracts** (`load_evidence_inventory` on the frozen candidate) — and recorded the two changes this leaf made: (1) a new contract `candidate-batch-case-harness` for `mcp/tests/candidate_batch_test_support.py` with an explicit artifact row, an evidence node that is a real passing node, and exactly two declared consumers (the two batch modules); its `source_version_or_generator` states the harness builds an admitted destination plus contexts *resolved* through the application seam, which is the property a future edit must not break; (2) the `knowledge-identity-branching-fixture` row gained `test_knowledge_label_operations.py` as a sixth observed consumer, because the new standalone label suite builds on that fixture — the validator derives real importers and refuses a differing declared set, so the addition was mandatory. Verification metadata remains closeout-owned.

- 2026-09-16T06:24:00+00:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): measured the catalog rather than carrying the L1 numbers — **45 artifacts and 6 contracts** (`load_evidence_inventory` on the frozen candidate) — and recorded the two changes the graph leaf made: (1) it **corrected the branching fixture's consumer list**, which named one module while five now import it, and widened that row's `source_version_or_generator` and `permanence_rationale` to state that the same builder carries the graph scenario as well (the artifact's `introduced_by` stays `260915-KS-L1`: it was extended in place, not forked); (2) it added contract `knowledge-graph-case-support` for `mcp/tests/knowledge_graph_test_support.py` with exactly three declared consumers. The "declared consumers are intent, not observation" caveat is now narrowed to a forward rule: the validator derives each artifact's real test importers and refuses a differing declared set, so a later leaf that extends either artifact must add itself to that row in the same change. Verification metadata remains closeout-owned.

- 2026-09-15T20:40:00+00:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): recorded the fifth contract `knowledge-identity-branching-fixture` and the 44th artifact row for the shared branching knowledge fixture (`shared-support`, `internal-canonical`, `unit-regression`, `in-process`, `permanent`, `consumer_scope = "exact"`, one observed consumer), corrected the populated counts in the Purpose and Logic text to the measured 44 artifacts / 5 contracts, and recorded that the artifact's governed path is why the fixture lives under `mcp/tests/**` — a row naming the module's former `mcp/test_support/**` location is stale by construction and its consumer proof is underivable. The anticipated L2–L8 consumers are named as intent in the fixture's own card and deliberately not listed as declared consumers here. Verification metadata remains closeout-owned.

- 2026-09-15T01:02:00+00:00 — Updated the documented replacement-node spelling for code/memory-only closeout and the two cleanup-guidance consumer declarations; retained registry ownership/fidelity/lifetime semantics and separated them from execution evidence. Working candidate verified by source inspection; commit metadata records real committed history only.

- 2026-09-14T18:00:00+00:00 — 260913-LCA-L12 curator (drift re-verification): the frozen catalog gained
  the `checkpoint_landing_test_support.py` artifact, so the declared population is 43
  shared-support/fixture artifacts plus four replacement contracts. Corrected the Purpose population
  count; the artifact blocks and every cited row were re-read. Verification metadata remains
  closeout-owned.

- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (flag resolved): the code worktree is frozen, so
  the earlier flag is now measured rather than conditional. `mcp/tests/evidence-lifecycle.toml`
  carries the inserted `checkpoint_landing_test_support.py` artifact block at `:342-361`, which
  leaves `path = "mcp/tests/curator_coherence_test_support.py"` at `:363` — the position this row
  already cites — and `path = "mcp/tests/closeout_input_test_support.py"` at `:283`. The pair
  `283-283` / `363-363` is confirmed against the frozen tree, and the flag above stands as the
  record of the interim state it described. Verification metadata remains closeout-owned.

- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (drift re-verification): this row cites the
  curator-coherence artifact path at `mcp/tests/evidence-lifecycle.toml:363`, which is its position
  in the current working tree, where the in-flight `checkpoint_landing_test_support.py` artifact
  block sits above it. The committed HEAD still carries that path at `:343`; the two forms differ
  only by that uncommitted insertion, so the citation is correct for the tree this leaf is being
  curated against and must be re-measured if the insertion does not land. Flagged rather than
  silently chosen; verification metadata remains closeout-owned.

- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 0 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.

- 2026-09-14T13:05:00+00:00 — 260913-LCA-L8 curator (uncommitted change set on `ar/260913-lca-l8-ar`):
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

- 2026-09-14T12:20:00+00:00 — 260913-LCA-L7 curator (uncommitted change set on `ar/260913-lca-l7`):
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

- 2026-09-14T05:05:00+00:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
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

- 2026-09-13T21:52:00+00:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
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

- 2026-09-13T18:42:00+00:00 — Child-admission seal removal (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): registered the new
  `mcp/tests/test_lifecycle_playthrough_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 316) and `curator_coherence_test_support.py` (row 372), both
  reached transitively through `QueueFixture`. No artifact row was added or re-categorised, so the
  declared population is unchanged; re-derived every shifted consumer row this card cites (the pause
  suite's entries 318 → 319 and 373 → 374, `curator_coherence_test_support.py` path 338 → 339,
  `lifecycle_enclosure_test_support.py` path 449 → 450 with the L32 entry 464 → 465) and corrected the
  three shared artifact-block ranges in the reference table to `282-336` and `338-392`. Verification
  metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-13T17:02:00+00:00 — 260831-LOCR-L37: registered the new boundary suite
  `mcp/tests/test_pause_stop_only_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 318) and `curator_coherence_test_support.py` (row 373), reached
  transitively through `QueueFixture`, and recorded that the leaf's other new module
  (`test_pause_is_not_publication.py`) consumes no artifact because it is AST-only. No artifact row was
  added or re-categorised, so the declared population is unchanged; re-derived the shifted consumer
  rows (`curator_coherence_test_support.py` 338, `lifecycle_enclosure_test_support.py` 448, L32 entry
  463). Verification metadata remains closeout-owned; no acceptance claim.

- 2026-09-13T16:09:00+00:00 — 260831-LOCR-L36: rebound two citation ranges shifted by this leaf's two
  additions to the manifest (`mcp/tests/test_cross_master_concurrency.py` in both consumer lists): the
  curator-coherence support artifact resolves at `:337` and the enclosure/worktree fixture's `path`
  cell at `:446`. Ranges only; the artifact and consumer claims are unchanged and no verification
  stamp advanced.

- 2026-09-13T09:43:00+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.

- 2026-09-13T09:12:00+00:00 — 260831-LOCR-L34 curator: recorded
  `mcp/tests/test_checkpoint_landing_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 304) and `curator_coherence_test_support.py` (row 357), both
  reached transitively through `QueueFixture`. No artifact row was added or re-categorised, so the
  declared population is unchanged; the insertion shifted three later consumer rows, which are
  re-derived and re-cited here (330, 383, 459). Verification metadata remains closeout-owned; no
  acceptance claim.

- 2026-09-12T20:55:00+00:00 — 260831-LOCR-L32 curator: recorded the new
  `mcp/tests/test_worktree_status_terminal_next_tool.py` as an exact consumer of three existing
  shared-support artifacts (`closeout_input_test_support.py` at row 329,
  `curator_coherence_test_support.py` at row 381, and `lifecycle_enclosure_test_support.py` at row 457,
  the last because the suite publishes a real enclosure through `publish_test_enclosure`). No artifact
  row was added or re-categorised, so the declared population is unchanged; added three reference rows
  and a section naming each artifact's reason for the edge. Verification metadata remains
  closeout-owned; no acceptance claim.

- 2026-09-09T22:20:36+00:00 — CCR-L42 current candidate reconciliation: The evidence registry now records the atomic-master review public and scope tests as exact consumers of existing shared support artifacts; the additions refine ownership accounting and do not claim test execution or certification.

- 2026-09-08T16:54:49+00:00 — CCR-L38 CQ02 preparation recorded the exact two R25/R26 consumers added to both shared support rows. Registry SHA `15bea1c01f402c382dad1667dec601313bb8aabfc511bb8cedac66076287606a1` and validator PASS42 are preserved as source/diagnostic evidence only; the source is uncommitted and no acceptance claim is made.

- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:17:00+00:00 — Registered the extracted gate fixture and publication-suite consumers in durable memory; reconciled exact-source runner ownership with the distinct pytest closure.

- 2026-09-03T10:30:00+00:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 registration of
  `test_gate_certificate_authority.py` as an exact consumer of the shared certification and
  closeout-input support rows whose builders its forcing suite imports. Verification is pinned
  to the owning commit.

- 2026-09-01T09:33:00+00:00 — CCR-L11 Attempt 10 expanded the certification shared-support row to
  the complete five-consumer set exposed by the source graph. Verification remains closeout-owned.

- 2026-09-01T01:11:00+00:00 — Registered the portable certification composition owner with its two
  exact focused-suite consumers. Verification remains closeout-owned.

- 2026-08-31T10:39:00+00:00 — Added `test_dispatch_agent_ambient_reviewer.py` to both exact transitive
  consumer sets after the L5 closeout fast hook identified the previously undeclared ownership
  edges.

- 2026-08-30T14:32:00+00:00 — Added `test_public_surface_conformance.py` to both exact transitive
  consumer sets after the L4 staged fast hook exposed the source-derived ownership edges; the
  focused lifecycle validator passes with 35 governed artifacts.

- 2026-08-29T21:04:00+00:00 — Added `test_memory_candidate_pair.py` to the exact source-derived
  consumer sets for the closeout-input and curator-coherence test composition roots after the
  A002 lifecycle fast hook exposed both missing edges.

- 2026-08-29T10:27:00+00:00 — Reconciled the curator-coherence helper's declared consumers with the
  source-derived transitive ownership graph after generation 7 rejected the direct-import-only
  catalog row. Verification remains closeout-owned.

- 2026-08-29T10:10:00+00:00 — Registered the shared curator-coherence fixture-input owner and its
  three exact importers after the generation-6 fast hook rejected the uncatalogued helper.
  Verification remains closeout-owned.

- 2026-08-29T07:58:00+00:00 — Added the curator-coherence suite to the exact source-derived consumer
  set for the shared closeout-input test support after the targeted closeout gate exposed the
  missing edge.

- 2026-08-28T03:10:00+00:00 — Recorded the operational unknown-suffix threshold and the lifecycle
  catalog's explicit policy-input/non-artifact boundary after Q5 v19 forced the self-reference case.

- 2026-08-27T11:32:00+00:00 — Registered the split Ruff support and its exact consumers. Verification
  remains closeout-owned.

  (`test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not`) whose subject is precisely what the harness exists to make measurable. The card also records that the two consumer modules were registered in the `unit-regression` lane in the same change. **This pass also completed the superseded table migration for this document**: both remaining `Finding | Citations | Source Path` tables were rewritten to `Finding | Anchor | Source` with `path:start-end` citations resolving to the working source, which clears the three pre-existing `citation_table_columns_wrong` findings this card carried. Verification metadata remains closeout-owned.

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

|`mcp/tests/closeout_input_test_support.py`|transitive typed closeout-input/repository-authority composition `test_worktree_support` imports| `mcp/tests/evidence-lifecycle.toml:316-387` |

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

|`mcp/tests/closeout_input_test_support.py`|imported directly by `integration_branch_authority_test_support`, whose landing fixture builds the whole-tool world| `mcp/tests/evidence-lifecycle.toml:331-407` |

|`mcp/tests/curator_coherence_test_support.py`|reached through `selected_lifecycle_test_support`, whose closeout-operation input composes it| `mcp/tests/evidence-lifecycle.toml:391-1011` |

| `mcp/tests/integration_branch_authority_test_support.py` | imported directly: `_authority_fixture` and `_closed_external_leaf_worktrees` build the real landed leaf each whole-tool case starts from | `mcp/tests/evidence-lifecycle.toml:435` |

| `mcp/tests/repository_profile_test_support.py` | imported directly by the landing fixture (`AGENTS_REMEMBER_PROFILE_REFERENCE`) | `mcp/tests/evidence-lifecycle.toml:565` |

| `mcp/tests/fixtures/repository_profiles/node/package.json` | the declared profile fixture that same support reads | `mcp/tests/evidence-lifecycle.toml:604` |

| `mcp/tests/fixtures/repository_profiles/node/package-lock.json` | the declared profile fixture that same support reads | `mcp/tests/evidence-lifecycle.toml:643` |

|`mcp/tests/gate_certification_test_support.py`|reached through `selected_lifecycle_test_support` → `test_closeout_certification_entrypoint`| `mcp/tests/evidence-lifecycle.toml:937-1011` |

|`mcp/tests/source_selection_test_support.py`|reached through `repository_profile_test_support`, which imports `source_selection_fixture`| `mcp/tests/evidence-lifecycle.toml:816-1012` |

| `mcp/tests/selected_lifecycle_test_support.py` | imported directly by the landing fixture (`selected_closeout_operation_input`) | `mcp/tests/evidence-lifecycle.toml:1038` |

| `mcp/tests/gate_certification_test_support.py` | reached through `selected_lifecycle_test_support` → `test_closeout_certification_entrypoint` | `mcp/tests/evidence-lifecycle.toml:937-1011` |

| `mcp/tests/source_selection_test_support.py` | reached through `repository_profile_test_support`, which imports `source_selection_fixture` | `mcp/tests/evidence-lifecycle.toml:816-1012` |

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
