# mcp/tests/evidence-lifecycle.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/evidence-lifecycle.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T04:31:57+02:00 |
| lastVerifiedCommitHash | `473ad8242bb4c22bdabed5d5253767350381eb3e` |
| lastVerifiedCommitDate | 2026-09-23T17:26:55+02:00|
| governingOverview | `overview.md` |
## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-18T04:35 +02:00 against the uncommitted KS-L14 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Declares shared test-support/fixture ownership, fidelity, lifetime, replacement contracts, and
exact consumers. **The catalog now contains 65 artifact records and fifteen executable replacement contracts**,
counted on this leaf's frozen candidate by counting the blocks (`65 [[artifact]]` and `15 [[contract]]`), with the
file's own sha256 re-measured as
`825abfd65a17899cf1334d6191bd944d1f618347db7e599a44629f2bec910ef2`; those declarations are not records that a test ran.
That reading is `260915-KS-L30`'s, and it is a **bytes-only** move: one consumer entry appended to an
already-governed artifact, no contract and no artifact added, so the populations are unchanged from the
`15 / 65` that `260915-KS-L21` set when it appended the census pair — the last change here that moved a block
kind since `KS-L11`. **This candidate's value is the merge of the two re-pins**: the merged candidate
carries **both** leaves' consumer rows — `260915-KS-L30`'s one row on
`mcp/tests/snapshot_lifecycle_test_support.py` and `260915-KS-L31`'s two on
`mcp/tests/merge_case_test_support.py` — so the digest is their merge while both counts stay **15 / 65**. The digest this leaf re-pinned from is `6ec7eb0d…` (the constant at its base, L28's
value), and the three digests before that are retained in their own sections — the L21 landing pinned `633b03ee…`, the L22 landing pinned `68a64207…`, and the L23 landing pinned `25b00f88…`. The six earlier counts are kept because they are different states of the same merged line, not competing
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

exact consumers. The catalog measured here contains **65 artifact records** and fifteen executable replacement
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
  with four declared consumers on this candidate — the two snapshot modules, the candidate-workspace module
  and, since `260915-KS-L30`, `mcp/tests/test_knowledge_curator_ingest_list.py`, whose CYCLE-01 continuity
  case imports `build_case`/`create`/`write_record` to get a real candidate database to fork. That node is chosen deliberately rather than
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
| The four retained knowledge contracts and their evidence nodes. | "id = \"ar-durable-store/1.0-process-race-evidence\""; "id = \"conversation-control-public-route-contract\""; "id = \"next-supported-pi-rpc-activity-recording\""; "id = \"synthetic-test-evidence-candidate\"" | mcp/tests/evidence-lifecycle.toml:4-22; mcp/tests/evidence-lifecycle.toml:191-191; mcp/tests/evidence-lifecycle.toml:380-380; mcp/tests/evidence-lifecycle.toml:464-464; mcp/tests/evidence-lifecycle.toml:467-467; mcp/tests/evidence-lifecycle.toml:1170-1170; mcp/tests/evidence-lifecycle.toml:1194-1194; mcp/tests/evidence-lifecycle.toml:1223-1223; mcp/tests/evidence-lifecycle.toml:1243-1243; mcp/tests/evidence-lifecycle.toml:1473-1473; mcp/tests/evidence-lifecycle.toml:1608-1608; mcp/tests/evidence-lifecycle.toml:1647-1647; mcp/tests/evidence-lifecycle.toml:1683-1683 |
|  Closeout fixture support names the retained code/memory transaction replacement. | "closeout_fixture_test_support.py" | mcp/tests/evidence-lifecycle.toml:325-325  |
|  Closeout-input support declares the cleanup-guidance consumer. | "closeout_input_test_support.py" | mcp/tests/evidence-lifecycle.toml:343-343  |
| **The knowledge branching fixture's contract and artifact row, whose consumer list 260915-KS-L2 corrected to the five source-observed importers and 260915-KS-L6 extended to the two portable modules.** | "id = \"knowledge-identity-branching-fixture\"" | mcp/tests/evidence-lifecycle.toml:25-25 |
| The knowledge graph case-support contract and its matching artifact row, added by 260915-KS-L2 with three declared consumers. | "id = \"knowledge-graph-case-support\"" | mcp/tests/evidence-lifecycle.toml:30-30 |
| The candidate-batch case-harness contract and its artifact row, added by 260915-KS-L3 with two declared consumers and a real evidence node. | "id = \"candidate-batch-case-harness\"" | mcp/tests/evidence-lifecycle.toml:35-35 |
| **The snapshot-lifecycle contract and artifact row, with an exact consumer list that 260915-KS-L6 extended to the portable boundary module.** | "id = \"knowledge-snapshot-lifecycle-cases\"" | mcp/tests/evidence-lifecycle.toml:40-40 |
| **The common-base-merge contract and artifact row, whose exact consumer list 260915-KS-L6 extended to both portable modules.** | "id = \"common-base-merge-cases\"" | mcp/tests/evidence-lifecycle.toml:45-45 |
| **The two consumer declarations 260915-KS-L6 added to the branching-fixture row.** | "owner = \"knowledge-identity-branching-fixture\"" |mcp/tests/evidence-lifecycle.toml:1190-1190|
| **The consumer declaration 260915-KS-L6 added to the snapshot-lifecycle row — the boundary module only, because the roundtrip module does not import that harness.** | "owner = \"knowledge-snapshot-lifecycle-cases\"" |mcp/tests/evidence-lifecycle.toml:1262-1262|
| **The two consumer declarations 260915-KS-L6 added to the merge-case row.** | "owner = \"common-base-merge-cases\"" |mcp/tests/evidence-lifecycle.toml:1286-1286|
| **The node that makes that contract's claim real: both sides' disjoint edits survive into a closed, published candidate that carries no verdict.** | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:307-376 |
| **The node that makes that contract's closedness claim real: a WAL-resident batch is published whole while a main-file copy is not.** | "test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not" | mcp/tests/test_knowledge_snapshot_publication.py:81-110 |
|  The lane rows that keep the knowledge test modules in the certifying collection path, including the two this leaf registered. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-73  |
| The one-to-one card for the batch harness, which records what it builds through the real seam. | "One admitted candidate built through the real seam" | onboarding/mcp/tests/candidate_batch_test_support.py.md:1-40 |
|The snapshot harness card, which records the registered owner and the exact consumer set.|"id = \"knowledge-snapshot-lifecycle-cases\""| mcp/tests/evidence-lifecycle.toml:40-40; onboarding/mcp/tests/snapshot_lifecycle_test_support.py.md:1-40 |
| The consumer entry this leaf appended to the snapshot harness, which is a row in a list rather than a new registration — the populations do not move because of it. | "mcp/tests/test_knowledge_curator_ingest_list.py", | mcp/tests/evidence-lifecycle.toml:668-798 |
| The referenced transaction test definition exists in the current source. | "test_public_closeout_commits_code_and_memory_without_acceptance_tools"; `test_public_closeout_commits_code_and_memory_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:211-318 |
| None | "mcp/tests/closeout_fixture_test_support.py" | mcp/tests/evidence-lifecycle.toml:325-325 |
| Closeout-input support names the same retained code/memory transaction replacement node. | "mcp/tests/closeout_input_test_support.py" | mcp/tests/evidence-lifecycle.toml:343-343 |
| None | "mcp/tests/curator_coherence_test_support.py"; "mcp/tests/test_post_integration_cleanup_guidance.py" | mcp/tests/evidence-lifecycle.toml:380-380; mcp/tests/evidence-lifecycle.toml:421-421; mcp/tests/evidence-lifecycle.toml:384-390; mcp/tests/evidence-lifecycle.toml:425-431 |
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

## KS-R20@v1 Consumer Row

`KS-R20@v1` adds **no contract and no artifact**, and its whole footprint in this catalogue is **one
consumer row**. The leaf's integration acceptance module,
`mcp/tests/test_knowledge_projection_vault_safety.py`, builds its dataset through the registered
`shared-support` fixture `mcp/tests/read_scope_test_support.py`, so that artifact's
`consumers` list gained the module —
`"mcp/tests/test_knowledge_projection_vault_safety.py",` at
`mcp/tests/evidence-lifecycle.toml:1409` — and nothing else in the file changed.

The reason a consumer row is **mandatory** rather than polite is the artifact's own declaration:
`mcp/tests/read_scope_test_support.py` carries `consumer_scope = "exact"`, so the validator requires its
`consumers` list to equal the *source-derived* consumer set. A new module that imports the fixture without
being listed makes that equality false **without touching this file at all** — which is exactly the
invisible-failure shape the L19 precedent records, and why the row had to be added here rather than
discovered by a later leaf.

**One row, one count that does not move, one digest that does.** A `consumers` addition belongs *inside* its
existing list, where the ordering lives, so it shifts every line below it; that shift is the drift the
routes citing this file carry, and it is inherent to the registry rather than a mistake. The two block
counts therefore stay **14 contracts and 64 artifacts** — measured here by counting the file's own
declarations (`64 [[artifact]]` and `14 [[contract]]`), which is the same reading
`mcp/tests/test_dependency_ownership_ast_helpers.py`'s `LIFECYCLE_CONTRACT_COUNT` and
`LIFECYCLE_ARTIFACT_COUNT` carry — while the catalogue's bytes move to
`1aef5f9b928055d3762df13d8042f1719d8614de8c0141c71bd0e0209bc91df7`, which re-hashing this file reproduces
and which the same module's `LIFECYCLE_CATALOG_SHA256` pinned at that candidate. **The counts and the digest are
measurements of one candidate, not constants**: a later leaf that registers its own artifact moves the
counts, and every leaf moves the digest — and `260915-KS-L21` is exactly that later leaf: it appends one
contract and one artifact, so the pair this paragraph measured as `14 / 64` with `1aef5f9b…` now reads
**`15 / 65`** with `633b03ee…`. That reading is retained as the state it measured, and the L21 section below
carries the current one.

## KS-R21@v1 Contract And Artifact — The Census Cases And Their Fixture

`260915-KS-L21` appends **one `[[contract]]` and one `[[artifact]]`**, which makes it the first catalog change
since `KS-L11` that moves both block kinds rather than only the file's bytes:

| | Registration | Where |
| --- | --- | --- |
| contract | `id = "migration-census-cases"`, owner `mcp/tests/migration_census_test_support.py`, evidence node `mcp/tests/test_migration_census.py::test_the_seed_writes_every_census_record_kind_through_the_shipped_batch_operation` | `mcp/tests/evidence-lifecycle.toml:74-76`; mcp/tests/evidence-lifecycle.toml:77-77 |
| artifact | `path = "mcp/tests/migration_census_test_support.py"`, `kind = "shared-support"`, `authority = "internal-canonical"`, `owner = "migration-census-cases"`, `category = "unit-regression"`, `fidelity = "local-composition"`, `cadence = "affected"`, `introduced_by = "260915-KS-L21"`, `lifetime = "permanent"`, `replacement_contract = "contract:migration-census-cases"`, `consumer_scope = "exact"` | `mcp/tests/evidence-lifecycle.toml:1642-1658`; mcp/tests/evidence-lifecycle.toml:164-164; mcp/tests/evidence-lifecycle.toml:1188-1188; mcp/tests/evidence-lifecycle.toml:1217-1217; mcp/tests/evidence-lifecycle.toml:1237-1237; mcp/tests/evidence-lifecycle.toml:1259-1259; mcp/tests/evidence-lifecycle.toml:1283-1283; mcp/tests/evidence-lifecycle.toml:1307-1307; mcp/tests/evidence-lifecycle.toml:1340-1340; mcp/tests/evidence-lifecycle.toml:1427-1427; mcp/tests/evidence-lifecycle.toml:1467-1467; mcp/tests/evidence-lifecycle.toml:1486-1486; mcp/tests/evidence-lifecycle.toml:1659-1659; mcp/tests/evidence-lifecycle.toml:1677-1677; mcp/tests/evidence-lifecycle.toml:1663-1663; mcp/tests/evidence-lifecycle.toml:1666-1666; mcp/tests/evidence-lifecycle.toml:96-96; mcp/tests/evidence-lifecycle.toml:116-116; mcp/tests/evidence-lifecycle.toml:135-135; mcp/tests/evidence-lifecycle.toml:153-153; mcp/tests/evidence-lifecycle.toml:172-172; mcp/tests/evidence-lifecycle.toml:193-193; mcp/tests/evidence-lifecycle.toml:213-213; mcp/tests/evidence-lifecycle.toml:235-235; mcp/tests/evidence-lifecycle.toml:253-253; mcp/tests/evidence-lifecycle.toml:274-274; mcp/tests/evidence-lifecycle.toml:295-295; mcp/tests/evidence-lifecycle.toml:316-316; mcp/tests/evidence-lifecycle.toml:337-337; mcp/tests/evidence-lifecycle.toml:355-355; mcp/tests/evidence-lifecycle.toml:382-382; mcp/tests/evidence-lifecycle.toml:402-402; mcp/tests/evidence-lifecycle.toml:484-484; mcp/tests/evidence-lifecycle.toml:507-507; mcp/tests/evidence-lifecycle.toml:525-525; mcp/tests/evidence-lifecycle.toml:546-546; mcp/tests/evidence-lifecycle.toml:564-564; mcp/tests/evidence-lifecycle.toml:583-583; mcp/tests/evidence-lifecycle.toml:603-603; mcp/tests/evidence-lifecycle.toml:642-642; mcp/tests/evidence-lifecycle.toml:681-681; mcp/tests/evidence-lifecycle.toml:1083-1083; mcp/tests/evidence-lifecycle.toml:1114-1114; mcp/tests/evidence-lifecycle.toml:1132-1132; mcp/tests/evidence-lifecycle.toml:1172-1172; mcp/tests/evidence-lifecycle.toml:1196-1196; mcp/tests/evidence-lifecycle.toml:1225-1225; mcp/tests/evidence-lifecycle.toml:1245-1245; mcp/tests/evidence-lifecycle.toml:1267-1267; mcp/tests/evidence-lifecycle.toml:1291-1291; mcp/tests/evidence-lifecycle.toml:1315-1315; mcp/tests/evidence-lifecycle.toml:1348-1348; mcp/tests/evidence-lifecycle.toml:1368-1368; mcp/tests/evidence-lifecycle.toml:1387-1387; mcp/tests/evidence-lifecycle.toml:1405-1405; mcp/tests/evidence-lifecycle.toml:1435-1435; mcp/tests/evidence-lifecycle.toml:1475-1475; mcp/tests/evidence-lifecycle.toml:1494-1494; mcp/tests/evidence-lifecycle.toml:1516-1516; mcp/tests/evidence-lifecycle.toml:1554-1554; mcp/tests/evidence-lifecycle.toml:1573-1573; mcp/tests/evidence-lifecycle.toml:1591-1591; mcp/tests/evidence-lifecycle.toml:1667-1667; mcp/tests/evidence-lifecycle.toml:1685-1685 |

Both blocks are **appended**, not inserted mid-list, so this leaf's registration shifts no other row: the
contract joins the tail of the contract block (`:74-76`, after `knowledge-evidence-cases` at `:69-72`) and
the artifact joins the very end of the file (`:1613-1630`), below the fresh-user acceptance harness rows.
The artifact's `consumers` list is its source-derived set exactly — one module,
`mcp/tests/test_migration_census.py`, which is the only importer of the fixture — and its
`permanence_rationale` states why the census cannot use a hand-built fixture: the states the accounting has
to separate (a claim with no assessment, a curator's recorded verdict, a piece outside the cohort, one claim
text recorded twice, an artifact that did not parse, and a card whose declared source is absent) are states
the shipped write path produces and an insert-based fixture could not.

**The counts moved to 15 contracts and 65 artifacts, and the pin moved with the bytes.** The file's own
sha256 on this candidate is
`633b03ee16893ce3d0e838659d52f2bc609903f5c75b142eb41ca8c4fdabf5e6`, which re-hashing
`mcp/tests/evidence-lifecycle.toml` reproduces, and `mcp/tests/test_dependency_ownership_ast_helpers.py`
pins exactly that value beside `LIFECYCLE_CONTRACT_COUNT = 15` and `LIFECYCLE_ARTIFACT_COUNT = 65`
(`mcp/tests/test_dependency_ownership_ast_helpers.py:44-46`). The evidence-lifecycle gate reports
`PASS (65 governed artifacts)` on this candidate. **The counts and the digest remain measurements of one
candidate rather than constants**, exactly as the sections above say: the next leaf that registers or
removes a block moves the counts, and every leaf that touches these bytes moves the digest.

## 260915-KS-L22 Consumer Rows And A Re-Pin That Moves Bytes Only

`260915-KS-L22` changes no contract and registers no artifact. Its whole change to this catalogue is
**one consumer entry appended to each of two already-governed artifacts**:
`mcp/tests/diff_scope_test_support.py` and `mcp/tests/read_scope_test_support.py` each gained
`mcp/tests/test_knowledge_review_surface.py` in their `consumers` list, because that module imports
both fixtures to build the candidate and the read scope it reviews. The two blocks are declared
`consumer_scope = "exact"`, so the additions are obligations rather than housekeeping: a module that
imports the fixture without being listed falsifies the equality without touching this file.

Because the blocks are unchanged, the counts stay at **15 contracts and 65 artifacts** — the values
`260915-KS-L21` set when it appended the census contract and artifact — while the file's own bytes
move, and the re-pin is therefore a **bytes-only** move: the sha256 goes from
`633b03ee16893ce3d0e838659d52f2bc609903f5c75b142eb41ca8c4fdabf5e6` to
`68a64207bd808eafd31f8c6b23856302c5ef2d150a604aa8177427e5906a1012`, which re-hashing
`mcp/tests/evidence-lifecycle.toml` reproduces and which
`mcp/tests/test_dependency_ownership_ast_helpers.py` now pins beside the unchanged count constants.
The distinction is the one worth carrying forward: a census leaf moves what the blocks *are*, a
consumer leaf moves only *who is declared to consume them*, and the two land in different constants.

Both entries are **appended** to the tails of their `consumers` lists rather than inserted, so no row
of either block was moved: the two artifacts keep their published extents and every other line number
in the manifest stands. The later record in `test_dependency_ownership_ast_helpers.py` above, which
still names `633b03ee…` and calls the pin "in force", is the L21 measurement of the tip that produced
it and is retained as such rather than rewritten.

## 260915-KS-L23 Four Consumer Rows, A Population That Does Not Move, And The Append-Only Point

`260915-KS-L23` changes no contract and registers no artifact. Its whole change to this catalogue is
**four consumer entries appended to three already-governed artifacts**, owed to two items:

| Artifact | Row appended | Why the module reaches it |
| --- | --- | --- |
| `mcp/tests/merge_case_test_support.py` (`consumer_scope = "exact"`) | `mcp/tests/test_knowledge_merge_right_side_writes.py` at `:1287` | item 2's case drives the merge through the already-registered common-base harness |
| `mcp/tests/_evidence_catalog_fixture.py` (`exact`) | `mcp/tests/test_evidence_catalog_gate_boundaries.py` at `:172` | the item-13 case builds its synthetic catalogue through the registered fixture |
| `mcp/tests/test-evidence-lanes.toml` (`exact`) | `mcp/tests/test_evidence_catalog_gate_boundaries.py` at `:806` | the item-13 case's fixture chain reaches the lane manifest |
| `mcp/tests/test-evidence-lanes.toml` (`exact`) | `mcp/tests/test_memory_citation_resolution.py` at `:807` | the item-16 case reads the **shipped** lane manifest to pin the append point |

**The populations do not move: 15 contracts and 65 artifacts**, re-counted on this candidate from the
file's own blocks (`15 [[contract]]`, `65 [[artifact]]`). The bytes do move, and the pinned identity moves
with them: `sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate is
`25b00f8832420b705495931c3a04ad13a9bfe83e367a97c4a854b36030071e30`, which is what
`mcp/tests/test_dependency_ownership_ast_helpers.py`'s `LIFECYCLE_CATALOG_SHA256` carries beside the
unchanged count constants. The states in between are retained in their own sections: `633b03ee…`
(`260915-KS-L21`, the census pair) and `68a64207…` (`260915-KS-L22`).

**All four rows are appended to the tail of their list, and that is the shape this leaf enforces (item 16
half (a)).** The `KS-R20@v1` and L22 sections above record the opposite shape — a `consumers` addition
"belongs *inside* its existing list, where the ordering lives, so it shifts every line below it", which was
true of this registry and is the drift every route citing this file carried. Appending at the end of a list
**moves no existing row of that list**, so a citation into the list's own entries — which is what a
registry citation almost always is — keeps its line. The lines *below* an append still move, and this
leaf's three append points do move them: by one below `:172`, by three below `:807` and by four below
`:1287`, the file going from 1632 to 1636 lines. That residue is precisely the class item 16 half (b) now
reports as a **pure move** rather than billing it as curator work. The property itself is pinned by
`mcp/tests/test_memory_citation_resolution.py::InsertedRegistrationRangeDriftTests::test_the_shipped_registries_append_point_is_the_end_of_its_own_list`,
which measures the shipped registries and asserts that a contrasting mid-list insertion *does* move a row,
so it cannot pass vacuously. Its half (b) classifies a citation whose anchor survived a move as a
**report-only** stale range rather than as curator work, which is what stops an append from being billed to
a later leaf. No header comment stating the new append point was added to either registry, deliberately: a
line at the top of the file would shift every row and stale hundreds of citations — the comment would
itself be the defect.

**One of those four rows was created by the case that pins the ruling**, and that is the shape a reader
should carry forward: the item-16 case reads the lane manifest, so it became a consumer of
`mcp/tests/test-evidence-lanes.toml`, which is a catalogue change like any other — a module that reaches a
governed artifact must be declared, and the validator derives that from the source graph rather than
trusting the list.

## 260915-KS-L31 Two Consumer Rows On The Merge-Case Artifact — One Direct, One Transitive

`260915-KS-L31` registers no contract and no artifact. Its whole change to this catalogue is **two
consumer entries appended to the tail of one already-governed artifact's exact list**, on
`mcp/tests/merge_case_test_support.py`:

| Row appended | Module reaches the harness because |
| --- | --- |
| `mcp/tests/test_worktree_sync.py` at `:1292` | **directly** — the CYCLE-02 knowledge-dataset case builds its real three-commit branching scenario with `merge_case_test_support.build_case` and measures the inputs with `file_digest` |
| `mcp/tests/test_sync_parked_candidate.py` at `:1291` | **transitively** — it imports `SyncFixture`, `commit_file`, `git` and `section` from `test_worktree_sync`, so the census's transitive import walk reaches the harness through the edge the sibling above gained |

**The second row is the one worth reading**, because nobody edited that module: it was already a
consumer of `test_worktree_sync` and became a consumer of *the harness* the moment its import target
started consuming it. That is the census working as designed and stated here rather than left as a
surprise — the declaration is derived from the import graph, so a new edge anywhere in the closure adds
a row, and a list that only named the module whose diff mentioned the harness would be refused by the
validator that derives real importers and compares them with the declared set.

**The populations do not move: 15 contracts and 65 artifacts**, and the byte pin does.
`sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate is
`825abfd65a17899cf1334d6191bd944d1f618347db7e599a44629f2bec910ef2`, which is the value
`mcp/tests/test_dependency_ownership_ast_helpers.py`'s `LIFECYCLE_CATALOG_SHA256` carries beside the
unchanged count constants. **This candidate's value is the merge of the two re-pins**, because the
merged candidate carries both leaves' consumer rows — `260915-KS-L30`'s one row on
`mcp/tests/snapshot_lifecycle_test_support.py` and this leaf's two rows on
`mcp/tests/merge_case_test_support.py` — while both counts stay **15 / 65**; the L31 byte value this
paragraph was written against was `f786c157…`, correct only at this leaf's own tip. The values in between are retained in their own sections above, one record
per leaf: the L23 tip, L22 and L21 each carry theirs there.

**Both rows are appended to the end of their list**, which is the append point L23 pinned: an append
moves no existing row of that list, so the citations into its own entries keep their lines, and the
lines below the append are the class L23's item 16 half (b) reports as a pure move rather than as
curator work.

## 260921-ICR-L18 Two Consumer Rows On Two Artifacts, Counts Unmoved — No Third Fixture

This leaf's whole footprint in this catalog is **two consumer rows on each of two artifacts and nothing
else**: its two new case modules joined the `consumers` lists of
`mcp/tests/snapshot_lifecycle_test_support.py` (owner `snapshot-lifecycle-cases`,
`consumer_scope = "exact"`, rows `1268-1269`) and of the Node fixture
`mcp/tests/fixtures/repository_profiles/node/package-lock.json` (also `consumer_scope = "exact"`, rows
`731-732`). The reason is the leaf's own shape: its cases build every enclosure out of the **existing**
`snapshot_lifecycle_test_support` builders and the existing ingest-list fixture module rather than
introducing a third support module, so it registers **no artifact and no contract** — which is why both
block counts are untouched and only the byte pin moves. The second list is reached by the census's own
propagation rule from the support module the first row already names, so it is one change of subject
seen twice rather than two independent registrations.

**The populations do not move: 16 contracts and 66 artifacts**, the pair `260918-TSIP-L10`'s `T129`
reconciliation set and every leaf since has left alone. The byte pin does:
`sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate is
`4fb2bc3f2da65134e428631f0e964f4f712e6655f4816934e2a93a4cb8e32046`, which is the value
`mcp/tests/test_dependency_ownership_ast_helpers.py`'s `LIFECYCLE_CATALOG_SHA256` carries beside the
unchanged count constants, and the value it replaces on this line is `24e760a1…`. The older per-leaf byte
values in the sections above remain the records of the tips that produced them.

**Both insertions are mid-list, not appends**, so a citation that names a line below them reads lower than
it did before this leaf: everything from `731` moves by `+2` and everything from `1265` by `+4`. The cards
that cite those ranges by line were re-derived in the same pass rather than left to rot.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The first artifact's two new consumer rows: the Node package-lock fixture, whose `consumer_scope = "exact"` list both new modules joined.** | "mcp/tests/test_knowledge_ingest_comparison_generation.py"; "mcp/tests/test_knowledge_ingest_failure_windows.py" | mcp/tests/evidence-lifecycle.toml:668-798; mcp/tests/evidence-lifecycle.toml:732-732 |
| **The second artifact's two new consumer rows: the snapshot-lifecycle shared support module, whose `consumer_scope = "exact"` list both new modules joined.** | "mcp/tests/test_knowledge_ingest_comparison_generation.py"; "mcp/tests/test_knowledge_ingest_failure_windows.py" |mcp/tests/evidence-lifecycle.toml:734-734; mcp/tests/evidence-lifecycle.toml:735-735|
| The artifact the first pair belongs to, and the scope both lists carry. | "mcp/tests/fixtures/repository_profiles/node/package-lock.json"; "exact" | mcp/tests/evidence-lifecycle.toml:668-798; mcp/tests/evidence-lifecycle.toml:1265-1265 |
| The artifact the second pair belongs to. | "mcp/tests/snapshot_lifecycle_test_support.py" | mcp/tests/evidence-lifecycle.toml:39-42 |
| The two block kinds whose counts this change does not move, and the sha256 it does move. | "[[contract]]"; "[[artifact]]" | mcp/tests/evidence-lifecycle.toml:1-1673 |
| The constant this file's bytes pin, re-pinned deliberately in the same change. | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| The reason no third fixture exists: both new modules import the existing builders rather than introducing one. | `build_case`; `create` | mcp/tests/snapshot_lifecycle_test_support.py:178-205; mcp/tests/snapshot_lifecycle_test_support.py:208-211 |

## 260921-ICR-L1 Two Consumer Rows, Counts Unmoved — No Third Fixture

This leaf's whole footprint in this catalog is **two `consumers` rows and nothing else**: one on
`mcp/tests/diff_scope_test_support.py` (owner `knowledge-diff-cases`, `consumer_scope = "exact"`) and one
on `mcp/tests/read_scope_test_support.py` (owner `knowledge-read-scope-cases`, `consumer_scope = "exact"`),
each appended to the tail of its own list, both for `mcp/tests/test_knowledge_review_source_endpoints.py`.
The reason is the leaf's own shape: its source-endpoint cases build a live enclosure out of the **two
existing** shared-support fixtures rather than introducing a third one, so it registers **no artifact and
no contract** — which is why both block counts are untouched and only the byte pin moves.

**The populations do not move: 16 contracts and 66 artifacts**, the pair `260918-TSIP-L10`'s `T129`
reconciliation set and every leaf since has left alone. The byte pin does:
`sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate is
`24e760a124d5f0d3a608295533720168b47e8a2ee28f6ee85c493e3778cdbed4`, which is the value
`mcp/tests/test_dependency_ownership_ast_helpers.py`'s `LIFECYCLE_CATALOG_SHA256` carries beside the
unchanged count constants, and the value it replaces on this line is `f0cb5fec…`. The older per-leaf byte
values in the sections above remain the records of the tips that produced them.

**Both rows are appended to the end of their list**, which is the append point `260915-KS-L23` pinned: an
append moves no existing row of that list, so citations into this file's earlier entries keep their lines.
The two rows do sit below the insertion points of earlier leaves — `1404` and `1435` in this candidate —
so a citation that names a line below them reads one or two lines lower than it did before this leaf, and
the two cards that cite those ranges by line were re-derived in the same pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The first consumer row: the diff-scope shared support module, whose `consumer_scope = "exact"` list this leaf's module joined.** | "mcp/tests/test_knowledge_review_source_endpoints.py" |mcp/tests/evidence-lifecycle.toml:1423-1419|
| **The second consumer row: the read-scope shared support module, whose `consumer_scope = "exact"` list this leaf's module joined.** | "mcp/tests/test_knowledge_review_source_endpoints.py" |mcp/tests/evidence-lifecycle.toml:1467-1461|
| The two block kinds whose counts this change does not move, and the sha256 it does move. | "[[contract]]"; "[[artifact]]" | mcp/tests/evidence-lifecycle.toml:1-1679; mcp/tests/evidence-lifecycle.toml:1-1669 |
| The constant this file's bytes pin, re-pinned deliberately in the same change. | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |
| The reason no third fixture exists: the case module composes the two existing ones. | `build_diff_fixture`; `build_read_scope_fixture` | mcp/tests/test_knowledge_review_source_endpoints.py:181-199; mcp/tests/diff_scope_test_support.py:196-242 |

## 260921-ICR-L11 Two Consumer Rows On Two Artifacts, Counts Unmoved — The Keystone Record's Cases Consume Two Fixtures

This leaf registers **no artifact and no contract of its own**. Its fifteen durable-comparison-generation
cases live in the ordinary unit module `mcp/tests/test_knowledge_review_comparison_generation.py`, which
builds on the existing `mcp/tests/test_knowledge_review_source_endpoints.py` enclosure fixture rather than
introducing a second one — so its catalog footprint is **two consumer entries**, both added to
`consumer_scope = "exact"` rows and both derived from the census's own finding rather than from
inspection:

- the **diff-cases** artifact (`replacement_contract = "contract:knowledge-diff-cases"`,
  `introduced_by = "260915-KS-L8"`), whose consumer list gained
  `mcp/tests/test_knowledge_review_comparison_generation.py` at row `:1405`, first in the list: the
  module's cases read the candidate's content back out of the retained tree and build the enclosure over
  two real committed Git trees, which is exactly this fixture's subject;
- the **read-scope** artifact (`replacement_contract = "contract:knowledge-read-scope-cases"`,
  `introduced_by = "260915-KS-L7"`), whose consumer list gained the same path at row `:1429`: the
  comparison the cases freeze is between two snapshots of this fixture's recorded topology, and the
  module imports `read_scope_test_support.BATCH_PATH` for the one path whose candidate bytes exist in no
  commit.

The derivation rule matters more than the rows: the census reported
`missing=['mcp/tests/test_knowledge_review_comparison_generation.py']` with `unsupported=[]` on both rows,
and that finding is the whole justification — a `consumer_scope = "exact"` list must equal the
source-derived consumer set, so a module whose imports reach a fixture is a consumer of it whether or not
anybody remembered to write it down. A **second copy of one path** would pass silently, which is why both
rows are recorded as one set.

**Nothing was registered, no row was removed and no artifact's identity moved**, so the population stays
at the measured **sixteen contracts / sixty-six artifacts** (`LIFECYCLE_CONTRACT_COUNT = 16`,
`LIFECYCLE_ARTIFACT_COUNT = 66`), and the file's bytes move only by these two rows and the two
`260921-ICR-L20` landed on the sync line. On this leaf's own candidate the file was **1673 lines** and
hashed to `6b73894fb010534d5cedbdace361504d1a67abb2ce8ffb76de8d00ac2e0af39e`; **on the merged line it is
1675 lines and hashes to `aedb2636844faf41ca63b7099e6c62bcaf888720e7e7dd78e203e3a1c9e061ff`**, which is what
`test_dependency_ownership_ast_helpers.LIFECYCLE_CATALOG_SHA256` carries (the fourteenth deliberate
re-pin, whose docstring record names this leaf). All four insertions are **mid-list**: `260921-ICR-L20`'s
at `:733` and `:1271`, this leaf's at `:1405` and `:1429` — so a range authored against the pre-sync file
is displaced by one for each of those four rows at or below it.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The first of the two consumer rows: the diff-cases artifact's exact consumer list, which the new module joins.** | `consumers`; `consumer_scope`; `replacement_contract` | mcp/tests/evidence-lifecycle.toml:83-101; mcp/tests/evidence-lifecycle.toml:96-1681; mcp/tests/evidence-lifecycle.toml:97-1681 |
| **The second: the read-scope artifact's exact consumer list.** | `consumers`; `consumer_scope`; `replacement_contract` | mcp/tests/evidence-lifecycle.toml:1429-1430; mcp/tests/evidence-lifecycle.toml:97-1681; mcp/tests/evidence-lifecycle.toml:1427-1427 |
| The two artifacts' own subjects, which are what make the module a source-derived consumer of each. | `source_version_or_generator`; `introduced_by` | mcp/tests/evidence-lifecycle.toml:83-101; mcp/tests/evidence-lifecycle.toml:92-1681; mcp/tests/evidence-lifecycle.toml:91-1681; mcp/tests/evidence-lifecycle.toml:1424-1424 |
| **The imports that make it a consumer: the candidate content path from the diff-scope support and the batch path from the read-scope support.** | `BATCH_PATH_CANDIDATE_TEXT`; `BATCH_PATH` | mcp/tests/diff_scope_test_support.py:113-113; mcp/tests/read_scope_test_support.py:118-118 |
| The fixture module it builds on rather than duplicating, so no third enclosure fixture was introduced. | `build_endpoint_fixture`; `EndpointFixture` | mcp/tests/test_knowledge_review_source_endpoints.py:198-222; mcp/tests/test_knowledge_review_source_endpoints.py:105-188 |
| **The pinned counts and the re-pinned digest, in the module that measures this file.** | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |

## 260921-ICR-L6 One Consumer Row On The Read-Scope Artifact, Beside L18's Landed One

This leaf's ICR-R06 cases drive the real review composition over **two real read-scope snapshots**, so
its case module consumes `mcp/tests/read_scope_test_support.py` — the artifact whose
`consumer_scope = "exact"` requires its `consumers` list to equal the source-derived consumer set. One
path was appended to that list, and **no artifact and no contract was registered, none removed, and no
other row's identity moved**:

| Finding | Anchor | Source |
| --- | --- | --- |
| **The row this leaf registered: its own case module, on the read-scope artifact's `consumer_scope = "exact"` list.** | "mcp/tests/test_knowledge_review_one_sided_statements.py" |mcp/tests/evidence-lifecycle.toml:1461-1461|
| **The row this leaf registered: its own case module, on the read-scope artifact's `consumer_scope = "exact"` list.** | "mcp/tests/test_knowledge_review_one_sided_statements.py" |mcp/tests/evidence-lifecycle.toml:1461-1461|
| **The row L18's landed consequence repair had already carried, now the row immediately below this leaf's: `mcp/tests/test_read_ar_files.py` imports the same fixture and was the path L19's landing left unregistered. The two are kept as a set — the census compares consumer sets — so each path is named exactly once.** | "mcp/tests/test_read_ar_files.py"; "from read_scope_test_support import" | mcp/tests/evidence-lifecycle.toml:389-454; mcp/tests/test_read_ar_files.py:56-56 |
| The artifact both rows belong to: its `[[artifact]]` block, its `knowledge-read-scope-cases` owner, its `consumer_scope = "exact"` and the list's exact extent on the merged candidate. | `"mcp/tests/read_scope_test_support.py"`; `consumer_scope`; `consumers` | mcp/tests/evidence-lifecycle.toml:1412-1445 |
| The constant this file's bytes pin, re-pinned at the sync, and the two count constants this change leaves alone. | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-46 |

**Population, measured on the merged candidate: sixteen contracts and sixty-six artifacts** (`grep -c
'^\[\[contract\]\]'` / `grep -c '^\[\[artifact\]\]'`), which is the pair every leaf since
`260918-TSIP-L10`'s `T129` reconciliation has left alone and which supersedes the `15 / 65` reading the
Purpose paragraph above still carries from `260915-KS-L30` — that reading was already stale on this
leaf's base, before this leaf touched the file. **The byte pin moves at the sync:** the merged file's
`sha256sum` is `7920a0f9f6134d3849e60685ad8a9424cdc95e8209631a03b889cf7d79e05281`, the value
`mcp/tests/test_dependency_ownership_ast_helpers.py`'s `LIFECYCLE_CATALOG_SHA256` carries beside the
unchanged counts, and it replaces `3f91773d…` — L18's own measurement on `71a4433e`, which the sync
superseded because the merged file carries both leaves' rows.

**The one row is appended inside one list, so no earlier entry of this file moves.** It sits at `:1440`
in the merged candidate, above L18's `:1441`, so a citation naming a line **below** them reads one line
lower than it did on `71a4433e` while a citation into an earlier entry keeps its line. The cards that
cite this file's later ranges by line were left to the citation-reprojection pass rather than
re-pointed by hand; no range was dropped to silence a finding, and no claim was re-worded.
## 260921-ICR-L3 Two Consumer Rows On Two Artifacts, Counts Unmoved — The Source-Content Cases Extend The R01 Enclosure

This leaf registers **no artifact and no contract of its own**. Its twenty source-content cases live in the
ordinary unit module `mcp/tests/test_knowledge_review_source_content.py`, which extends the existing
`mcp/tests/test_knowledge_review_source_endpoints.py` enclosure fixture —
`build_endpoint_fixture(tmp_path / "content", datasets=False)`, with the content classes the packet names
written into that same worktree — rather than introducing a second enclosure. Its catalog footprint is
therefore **two consumer entries**, both on `consumer_scope = "exact"` rows and both derived from the
census's own finding rather than from inspection:

- the **diff-cases** artifact (`replacement_contract = "contract:knowledge-diff-cases"`,
  `introduced_by = "260915-KS-L8"`), whose consumer list gained the path at row `:1412`: the cases build the
  enclosure over the fixture's two real committed trees and read one side's bytes back through that
  fixture's `_git` observation helper;
- the **read-scope** artifact (`replacement_contract = "contract:knowledge-read-scope-cases"`,
  `introduced_by = "260915-KS-L7"`), whose consumer list gained the same path at row `:1445`: the tracked
  paths whose bytes the cases read back — `AUXILIARY_PATH`, `MISMATCH_PATH`, `SYNCHRONIZATION_PATH` — are
  that fixture's own recorded topology.

The rule is the one this card exists to enforce: the census reported
`missing=['mcp/tests/test_knowledge_review_source_content.py']` with `unsupported=[]` on both rows, and a
`consumer_scope = "exact"` list must equal the source-derived consumer set whether or not anybody wrote the
consumer down. **Nothing was registered, no row was removed and no artifact's identity moved**, so the
population stays at the measured **sixteen contracts / sixty-six artifacts**
(`LIFECYCLE_CONTRACT_COUNT = 16`, `LIFECYCLE_ARTIFACT_COUNT = 66`), and the catalog is **1677 lines**:

| Constant | Was (the L11 value this card carried) | Is now |
| --- | --- | --- |
| `LIFECYCLE_CONTRACT_COUNT` | 16 | **16** (unchanged) |
| `LIFECYCLE_ARTIFACT_COUNT` | 66 | **66** (unchanged) |
| `LIFECYCLE_CATALOG_SHA256` | `aedb2636844faf41ca63b7099e6c62bcaf888720e7e7dd78e203e3a1c9e061ff` | **`dc6e380867302d7e2fff89f8c36549c85528ed4dafa28b4510981b573f09739b`** |

The new digest is `sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate (1677 lines),
which is the value `mcp/tests/test_dependency_ownership_ast_helpers.py`'s `LIFECYCLE_CATALOG_SHA256`
carries beside the unchanged counts — the **Fifteenth deliberate re-pin** as `260921-ICR-L3`'s own candidate measured it; **the sync then re-measured the merged file** to 1681 lines and `3e9105c2116422debaa01c295294fc0c714288f701ee5902e6552884b64a52d8`, the value the constant carries now (see the resolution entry in the Update History). The paragraph the constant's
own docstring now opens with.

**Both rows are appended to the tail of their list, so no earlier entry of this file moved.** The
diff-cases list ends at `:1412` (before its closing bracket at `:1413`) and the read-scope list ends at
`:1445` (with `mcp/tests/test_knowledge_review_one_sided_statements.py` at `:1446` and
`mcp/tests/test_read_ar_files.py` at `:1447` below it), which is the line-stable append point
`260915-KS-L23` pinned — but the two rows do sit below earlier insertions, so a citation into this file's
later ranges reads one or two lines lower than it did before this leaf, and every such range this card and
its sibling cards carry was re-derived against the post-edit bytes rather than shifted by a remembered
delta.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The first consumer row: the diff-cases shared support module, whose `consumer_scope = "exact"` list this leaf's module joined.** | "mcp/tests/test_knowledge_review_source_content.py" |mcp/tests/evidence-lifecycle.toml:1424-1420|
| **The second: the read-scope shared support module's exact list, where the new row sits above L6's registered module and L18's landed one.** | "mcp/tests/test_knowledge_review_source_content.py"; "mcp/tests/test_knowledge_review_one_sided_statements.py"; "mcp/tests/test_read_ar_files.py" |mcp/tests/evidence-lifecycle.toml:1462; mcp/tests/evidence-lifecycle.toml:1468-1462; mcp/tests/evidence-lifecycle.toml:1463; mcp/tests/evidence-lifecycle.toml:1469-1463; mcp/tests/evidence-lifecycle.toml:434-434|
| The two artifacts' own declarations, which are what make the module a source-derived consumer of each. | `replacement_contract`; `consumer_scope`; `consumers` | mcp/tests/evidence-lifecycle.toml:95-95; mcp/tests/evidence-lifecycle.toml:96-96; mcp/tests/evidence-lifecycle.toml:97-97 |
| **The fixture it extends rather than duplicating, and the observation helper its cases read bytes back through.** | `build_endpoint_fixture`; `EndpointFixture`; `_git` | mcp/tests/test_knowledge_review_source_endpoints.py:198-222; mcp/tests/test_knowledge_review_source_endpoints.py:104-188; mcp/tests/diff_scope_test_support.py:516-531 |
| The tracked paths the read-scope consumer row is derived from. | `AUXILIARY_PATH`; `MISMATCH_PATH`; `SYNCHRONIZATION_PATH` | mcp/tests/read_scope_test_support.py:116-121 |
| **The counts this change does not move, the bytes it does, and the constant that carries them.** | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |

## Update History
- 2026-09-23T10:05+02:00 — 260921-ICR-L21 citation-repair curator (memory worktree only; no code changed, no commits; leaf base `972b44cc07b307929535fe7974d6a30d53c9c4f1` plus the worker's uncommitted delta): **body update: every live row on this card was re-read against the catalog's current bytes, and the seven enforced `citation_anchor_absent_from_range` rows it carried were repaired by hand.** The delta added a `mcp/tests/test_review_final_output_receipt.py` consumer entry to three artifact blocks (`:801`, `:1428`, `:1472`), which moved the diff-scope block's `introduced_by`/`replacement_contract` lines to `:1406`/`:1409` and the read-scope block's `replacement_contract` to `:1443`, displacing every consumer entry cited below them. Each repaired range now names the line that actually carries its own anchor: the endpoint module's first and second consumer rows (`:1419`, `:1461`), the source-content module's (`:1420`, `:1462`), the one-sided-statements module's (`:1463`), and the three relationship modules on each exact list (`:1424`-`:1426` and `:1468`-`:1470`; the read-scope set was re-pointed from the diff-scope lines its row had been naming). No claim wording and no anchor was changed, no row was dropped to silence a finding, and **no verification stamp was advanced** — the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-22T15:52:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **body update for the two consumer rows this leaf's module obliged, and every live row re-derived against the 1683-line catalog.** The new `mcp/tests/test_review_subject_catalogue.py` imports `diff_scope_test_support` and `read_scope_test_support`, whose `[[artifact]]` rows carry `consumer_scope = "exact"`, so the module's path was appended to **both** consumers lists (newest last, matching file convention): `:1416` on the diff-cases artifact and `:1453` on the read-scope artifact — the census's own `missing=[…]` finding, `unsupported=[]` on both, is what makes the registration obligatory. **No row was added, removed or renamed and no artifact's identity moved**: the population stays sixteen contracts / sixty-six artifacts, and the catalog is re-pinned from `3e9105c2116422debaa01c295294fc0c714288f701ee5902e6552884b64a52d8` to `8d60a34cf56a9740e234823658312c8b6f5ae4e958344fe8ba2ea152b8ff6891` by `mcp/tests/test_dependency_ownership_ast_helpers.py` (whose card records the Seventeenth re-pin). **Citation accounting:** every live table row citing a catalog position before the first insertion kept its range; rows at or above the two insertions moved by their cumulative delta (+1 between `:1414` and `:1451`, +2 from `:1451`), re-derived per range end with the history sections left byte-identical. **Stamp accounting:** the verification pair names the leaf's base — the last real commit the reading was taken against — because the two consumer rows exist only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Merged measurement:** the catalog both leaves' rows now share is 1681 lines and `3e9105c2116422debaa01c295294fc0c714288f701ee5902e6552884b64a52d8`, L3's own re-pin being the fifteenth and this leaf's the sixteenth (`16 / 66` counts unchanged). **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **body update for the two consumer rows this leaf's module obliged, and for the catalog ranges its own additions displaced.** `mcp/tests/test_knowledge_review_source_content.py` extends the existing R01 source-endpoint enclosure fixture, so it registers no artifact and no contract: exactly one path joined the `consumer_scope = "exact"` list of `mcp/tests/diff_scope_test_support.py` (row `:1412`) and one the list of `mcp/tests/read_scope_test_support.py` (row `:1445`), both derived from the census's own `missing=[…]` / `unsupported=[]` finding, and the population stays at **sixteen contracts / sixty-six artifacts**. The catalog is **1677 lines** and re-pinned from L11's `aedb2636…` to `dc6e380867302d7e2fff89f8c36549c85528ed4dafa28b4510981b573f09739b` (measured with `sha256sum` on this candidate), the value the constants beside it carry as the **Fifteenth deliberate re-pin**. **Citation accounting:** the quality gate reported 3 range findings for this card and all 3 were cleared by re-deriving each range from the line that carries its anchor — the L1 section's `test_knowledge_review_source_endpoints.py` row `:1443` → `:1444`, the L6 section's own case-module row `:1444` → `:1446`, and the L6 section's `test_read_ar_files.py` row `:1445` → `:1447`; the report-only stale-by-a-move rows in the handover tables were repointed the same way rather than shifted by a delta (`selected_lifecycle_test_support` `:1154` → `:1158`, `test_worktree_support` `:441` → `:448`, `integration_branch_authority_test_support` `:464` → `:471`, and `test_closeout_certification_entrypoint` `:406` → `:412`). No claim, anchor or row was dropped, and **no verification stamp was advanced** — the candidate is uncommitted and the governed closeout owns the real memory commit.
## 260921-ICR-L14 Four Consumer Rows On Four Artifacts, Counts Unmoved — No Fifth Fixture

`ICR-R14@v1` registers **no artifact and no contract** of its own. Its new case module,
`mcp/tests/test_knowledge_review_evidence_channels.py`, builds on the existing endpoint fixture
(`mcp/tests/test_knowledge_review_source_endpoints.py`) and the existing curator-coherence publication
helper rather than introducing a third fixture of either, so the census derives it as a
source-derived consumer of **four** rows that already exist, each `consumer_scope = "exact"`:

| Artifact | Row that gained the path | Why the module consumes it |
| --- | --- | --- |
| `mcp/tests/curator_coherence_test_support.py` (shared-support) | `:453` | the assessment channel is produced through that module's task-topology and publication helpers, so the review's curator authority is the real one |
| `mcp/tests/fixtures/repository_profiles/node/package-lock.json` (fixture) | `:797` | the census's own propagation rule reaches it through the support modules the rows above and below already name |
| `mcp/tests/diff_scope_test_support.py` (shared-support) | `:1414` | the enclosure is built over that fixture's two real committed Git trees, and the candidate bytes the records are recorded against are its own |
| `mcp/tests/read_scope_test_support.py` (shared-support) | `:1449` | the repository, the anchors and the datasets the comparison is between come from that fixture's recorded topology |

**Both counts are unmoved at 16 / 66** — no contract and no artifact was added — and the digest moved
only because four existing `consumers` lists gained one path each; the value is
`4d1573760968b52a1cb8b087e235c21f40f0e2eccf2a5dcae3e19f0e5ae099a1` on this leaf's own candidate — the sync's merged measurement is `3e9105c2116422debaa01c295294fc0c714288f701ee5902e6552884b64a52d8` — measured with
`sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate. The module's own lane row was
added to `mcp/tests/test-evidence-lanes.toml` in the same change. The catalog is the one owner of
these lists: the module names no artifact and derives none of them, which is why the census's finding
(`missing=['mcp/tests/test_knowledge_review_evidence_channels.py']`, `unsupported=[]` on every row) is
what decided the four, not a convention of this leaf's.

## Update History
- 2026-09-21T22:35:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **four consumer rows on four already-governed artifacts, and nothing registered.** `ICR-R14@v1`'s case module consumes the endpoint fixture and the curator-coherence publication helper rather than introducing a third fixture, so the catalog's delta is one appended path on each of `mcp/tests/curator_coherence_test_support.py` (`:453`), the Node `package-lock.json` fixture (`:797`), `mcp/tests/diff_scope_test_support.py` (`:1414`) and `mcp/tests/read_scope_test_support.py` (`:1449`) — each derived from the census's own finding, with `unsupported=[]` on every row — and the populations stay **16 / 66** while the digest moves to `4d157376…` because four existing `consumers` lists changed. A new section records the four rows, the reason each is reached, and the measured counts and digest; nothing was registered and no row was removed. **Stamp accounting:** no verification stamp was invented or advanced; the governed closeout's metadata refresh owns it.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "owner = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:1187-1187. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "owner = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1258-1258. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "owner = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1282-1282. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T19:16:12+00:00: Generated citation repair: "mcp/tests/test_knowledge_review_one_sided_statements.py" repointed to mcp/tests/evidence-lifecycle.toml:1447-1447. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fbe69f2d182c46961e2554810a980cd29ac68e855e9213c9f6c1f2ac72173ec; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-21T20:44:00+02:00 — 260921-ICR-L11 curator, **memory-side sync conflict resolved as a UNION with the incoming `260921-ICR-L20` line; no side and no claim was dropped.** The header keeps both candidate rows (`ar/260921-icr-l20` and `ar/260921-icr-l11`) under one `lastUpdated` and the incoming line's stamp; both history entries are kept, this leaf's above `260921-ICR-L20`'s. **Citation accounting:** this card's ranges into `mcp/tests/evidence-lifecycle.toml` were re-derived against the merged file rather than shifted — the merged file is **1675 lines**, and a range authored against the pre-sync file is displaced by one for each of the four inserted rows at or below it (`260921-ICR-L20`'s consumer rows at `:733` and `:1271`, this leaf's at `:1405` and `:1429`) — twelve lines changed, including this leaf's own two rows, and the ranges into `test_dependency_ownership_ast_helpers.py` below line 47 were re-derived against that file's own insertion (`+19`, 14 lines). **Claims corrected rather than merged:** this leaf's section now states the merged value (`aedb2636…`, 1675 lines) beside its own-candidate measurement (`6b73894f…`, 1673 lines) instead of claiming the pre-sync bytes were current, and `260921-ICR-L20`'s `51a218a0…` is left as that entry's as-of measurement. **No verification stamp was advanced** — the header keeps the incoming line's `945ddad6a9c90fbf5d7eef7546b9e69714c6c4fc` / `2026-09-21T18:46:40+02:00`, not this leaf's superseded `9043a82e…`.
- 2026-09-21T20:12:00+02:00 — 260921-ICR-L11 curator (uncommitted change set on `ar/260921-icr-l11`, base `9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75`): **two consumer rows on two artifacts, counts unmoved, no third fixture.** `260921-ICR-L11` registers no artifact and no contract of its own — its fifteen durable-comparison-generation cases live in the ordinary unit module `mcp/tests/test_knowledge_review_comparison_generation.py`, which builds on the existing `mcp/tests/test_knowledge_review_source_endpoints.py` enclosure fixture — so its catalog footprint is two consumer entries: the same path joined the `consumer_scope = "exact"` list of the diff-cases artifact (row `:1403`) and of the read-scope artifact (row `:1427`). Both were derived from the census's own finding (`missing=['mcp/tests/test_knowledge_review_comparison_generation.py']`, `unsupported=[]` on both rows), not from inspection. **Nothing was registered, no row was removed and no artifact's identity moved**, so the population stays at the measured **16 contracts / 66 artifacts**; the file is **1673 lines** and hashes to `6b73894fb010534d5cedbdace361504d1a67abb2ce8ffb76de8d00ac2e0af39e` (measured with `sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate), which supersedes L6's `7920a0f9…` and is the value `LIFECYCLE_CATALOG_SHA256` is re-pinned to in the same change set. Both insertions are mid-list, so everything from `:1403` reads one line lower and everything from `:1427` two lines lower; the two cards that cite ranges below them were re-derived in this pass. Verification metadata is **not** advanced: the candidate is uncommitted and the governed closeout owns the stamp.
- 2026-09-21T18:35+02:00 — 260921-ICR-L20 curator, **memory-side sync conflict resolved as a UNION with the incoming `260921-ICR-L6` line; no side and no claim was dropped.** Both leaves' consumer-row sections and both history blocks are kept, and the metadata block keeps the incoming line's stamp rows with this leaf's candidate reading recorded in the entry beside them. Every range the resolution keeps was then re-derived against the merged candidate rather than shifted by a remembered delta (the rows into this file and into `mcp/tests/test_dependency_ownership_ast_helpers.py` were re-derived for the merged file (1,673 lines: this leaf's rows at `:733` and `:1271`, `260921-ICR-L6`'s at `:1442`)); where both sides cited the same construct the merged extent was taken, and two claims that had become untrue in the merged state were corrected rather than kept in two wordings (the merged catalog's digest is `51a218a0…`; this leaf's pre-merge `4da5626…` is recorded as the historical value it is, and no other leaf's paragraph was rewritten). **No verification stamp was advanced:** the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is exactly what the incoming line recorded (`9043a82ecd8cf6cfd0c2d08e2e36cd060b0c5f75` / 2026-09-21T18:13:19+02:00 where that line carried it), this leaf's candidate reading was recorded in the entry as metadata and not as a stamp, and the governed closeout owns the real commit.
- 2026-09-21T18:20:00+02:00 — 260921-ICR-L6 curator (uncommitted change set on `ar/260921-icr-l6`, merged base `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **one consumer row on the read-scope artifact, counts unmoved, and this entry was revised at the sync so the section states the merged file rather than either side of it.** The new section records `mcp/tests/test_knowledge_review_one_sided_statements.py` appended at `:1440` because the leaf's ICR-R06 cases drive the real composition over two real read-scope snapshots, and records `mcp/tests/test_read_ar_files.py` at `:1441` as **L18's landed consequence repair for the L19 import** rather than as this leaf's claim — the two rows are kept as a set, because the census compares consumer sets and a second copy of one path would pass silently. Populations stay at the measured **16 contracts / 66 artifacts**; the merged file's pin is `7920a0f9…`, which supersedes L18's own `3f91773d…` because the merged bytes carry both leaves' rows. The entry also corrects the record without rewriting it: the Purpose paragraph's `15 / 65` reading was already stale on this leaf's base, and the new section says so. L18's entry below is kept whole. Verification metadata is **not** advanced — the candidate is uncommitted and the governed closeout owns the stamp.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **citation repair only, forced by this leaf's own moves in the files this card cites.** The source file this card documents did **not** change; the ranges that moved belong to the leaf's other edits — this leaf appended two `consumer_scope = "exact"` rows to `mcp/tests/evidence-lifecycle.toml` (`:733`, `:1271`), so every range at or below them shifted by one and two respectively. Each row was re-read against the construct it names and its range re-derived from that construct's own extent in the moved file rather than shifted by a remembered delta. No claim was re-worded, no anchor was renamed and no row was dropped, and no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **two consumer rows added, and every citation into this file below them re-derived.** `mcp/tests/test_knowledge_ingest_publication_route.py` joined two `consumer_scope = "exact"` lists: the `snapshot_lifecycle_test_support` artifact's row (reached through the ingest-list fixture module the new case module imports) at `:733`, and the Node `package-lock.json` fixture's row (reached through the CLI import chain those rows already name) at `:1271`. **No contract, no artifact and no population moved** — the counts stay sixteen and sixty-six. The digest this leaf re-pinned on its own candidate was `4da562629ba16373ce387f0b7cfe83f110eede155fced865de9fa92f7eb41df7`; **that value is historical**, correct only before the merge, and the merged catalog carries `51a218a09ea5721197cb15b445f98fb8f1dd734c2d083124c913226e599a8745` (this leaf's two rows and `260921-ICR-L6`'s one, measured with `sha256sum` on the merged file). **Citation accounting:** the file is 1,670 → **1,673** lines on the merged candidate (this leaf's rows at `:733` and `:1271`, `260921-ICR-L6`'s at `:1442`), so every range at or below `:733` shifted by one, at or below `:1271` by two and at or below `:1442` by three; each was re-derived from the post-edit bytes rather than shifted by a remembered delta — including the `consumer_scope = "exact"` rows, the `test_knowledge_review_source_endpoints.py` consumer blocks `:1410-1410`/`:1441-1441`, the snapshot-support row `:1253`, and the failure-windows row `:1270`. No claim and no row was dropped, and no verification stamp was advanced — the governed closeout owns it.
- 2026-09-21T15:35+02:00 — 260921-ICR-L18 curator (uncommitted change set on `ar/260921-icr-l18`, code base `0fca5c69766aa95eebe950c19fbcdc83864ec35a`): **two consumer rows on each of two artifacts, counts unmoved, and every citation into this file was re-derived against the moved file.** `260921-ICR-L18` registered no artifact and no contract of its own — its two new case modules import the existing `snapshot_lifecycle_test_support` builders and the existing ingest-list fixture module rather than introducing a third support module — so its catalog footprint is four consumer entries: both modules joined the `consumer_scope = "exact"` list of `mcp/tests/snapshot_lifecycle_test_support.py` (rows `1268-1269`) and of the Node fixture `mcp/tests/fixtures/repository_profiles/node/package-lock.json` (rows `731-732`), the second reached by the census's own propagation rule. **Nothing was registered, no row was removed and no artifact's identity moved**, so the population stays at **sixteen contracts / sixty-six artifacts**; the catalog's bytes do move, and it is re-pinned to `4fb2bc3f2da65134e428631f0e964f4f712e6655f4816934e2a93a4cb8e32046` (measured with `sha256sum mcp/tests/evidence-lifecycle.toml` on this candidate), replacing `24e760a1…`. Both insertions are **mid-list**, so everything from `:731` moves by `+2` and everything from `:1265` by `+4`; all 534 citations into this file across the onboarding tree were re-derived from the file's own diff-verified offset. **Citation accounting:** the same pass re-derived every range into the four changed `.py` files, so the rows on this card that cite `test_dependency_ownership_ast_helpers.py`'s constants (`:44-46`, unchanged) and the two support modules were re-read rather than assumed. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained as recorded; the candidate is uncommitted and the governed closeout owns the real stamp.- 2026-09-21T13:07:00+02:00 — 260921-ICR-L1 curator (uncommitted change set on `ar/260921-icr-l1`, code base `f745e166`): **two consumer rows and nothing else — no artifact, no contract, so the populations are unchanged and only the byte pin moves.** The section above records the two appended rows (`mcp/tests/test_knowledge_review_source_endpoints.py` on `knowledge-diff-cases` and on `knowledge-read-scope-cases`, both `consumer_scope = "exact"`), the measured counts **16 / 66** from this candidate's blocks, the measured sha256 `24e760a1…` that `LIFECYCLE_CATALOG_SHA256` carries beside them, and the reason the module needed no third fixture. It also records the pure-move consequence for citations: the two rows sit at `:1404` and `:1435`, so a range below them reads one or two lines lower than before, and the two cards that cite such ranges by line were re-derived in this pass. Verification metadata is **not** advanced: the candidate is uncommitted and the governed closeout owns the stamp.
- 2026-09-20T02:05:20+00:00: Generated citation repair: "closeout_fixture_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:325-325. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: "closeout_input_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:343-343. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: "owner = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:1182-1182. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: "owner = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1253-1253. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: "owner = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1274-1274. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: "mcp/tests/closeout_fixture_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:325-325. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:05:20+00:00: Generated citation repair: "mcp/tests/closeout_input_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:343-343. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T02:25+02:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **cleared the `update_history_not_newest_first` finding this card carried, with the shipped order fixer and no change to any entry's text.** This leaf's own 23:20Z entry recorded the pre-sync tip's pinned digest and was written below the L30 entry it follows in time; the two are now in newest-first order. Sorting is the fixer's whole edit: every entry keeps its own bytes and no timestamp was reworded. The body above already carries the merged line's value — `LIFECYCLE_CATALOG_SHA256` is `825abfd6…` on this candidate, measured with `sha256sum` against `mcp/tests/evidence-lifecycle.toml`, with the counts still 15 contracts / 65 artifacts — and the entries naming `f786c157…` and the earlier digests are retained as the states they record. No verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits. No commits.
- 2026-09-20T01:20+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `evidence-lifecycle.toml.md:355` ("mcp/tests/curator_coherence_test_support.py", "mcp/tests/test_post_integration_cleanup_guidance.py") — re-read the claim against the landed source: the construct moved and the cited range was widened to the line that actually carries it, per the checker's own remedy.
- 2026-09-19T23:20+00:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **two consumer rows on the merge-case artifact, no new contract and no new artifact.** The direct row is `mcp/tests/test_worktree_sync.py`, which now consumes `merge_case_test_support` for the knowledge-dataset conflict case; the transitive row is `mcp/tests/test_sync_parked_candidate.py`, which reaches the harness through its existing import of `test_worktree_sync` and was not itself edited. The counts stay 15 / 65 and the pinned digest moves to `f786c157…`, re-measured with `sha256sum` on this candidate and recorded in the constants beside the counts. Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-19T22:49:08+00:00: Generated citation repair: "owner = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:1184-1184. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:49:08+00:00: Generated citation repair: "owner = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1255-1255. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:49:08+00:00: Generated citation repair: "owner = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1275-1275. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): re-read this card against the CYCLE-01 repair, whose whole change here is **one consumer row** appended at the tail of the `mcp/tests/snapshot_lifecycle_test_support.py` artifact's `consumers` list (`mcp/tests/evidence-lifecycle.toml:1267`, inside `:1265-1270`) for `mcp/tests/test_knowledge_curator_ingest_list.py` — that module's new continuity case imports `build_case`/`create`/`write_record`, and an import edge is a declared consumer. **No contract and no artifact was added, so the populations do not move: 65 artifacts / 15 contracts.** The card's Purpose paragraph and its "value at this candidate" statement now read the digest the file actually hashes to on this candidate, `73cdd2183e153af752773e8a4c6076e5e2eb7053d9e0ce5fa6538a69c907cefe` (re-pinned from `6ec7eb0d…`, the value at this leaf's base), and the earlier digests (`633b03ee…` L21, `68a64207…` L22, `25b00f88…` L23) are retained as the states they were. One further claim the change falsifies was corrected rather than carried: the snapshot contract row said the harness artifact has "exactly two declared consumers (the two snapshot modules)", which is not what the file declares — the list holds four on this candidate, so the row now states the set and names this leaf's addition. A reference row was added for the appended consumer entry. No verification stamp was advanced: the candidate is uncommitted and closeout owns the real code and memory commits.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "owner = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:1184-1184. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "owner = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1255-1255. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "owner = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1276-1276. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T20:45:09+02:00 — 260915-KS-L23 post-closeout clearance (change set on `ar/260915-ks-l23`, memory base `ce3028e9`, code `5e4eb651`): **cleared the 3 enforced `citation_anchor_absent_from_range` rows in this document.** The closeout's own code commit appended one `consumers` registration above every construct these cards cite, so each cited range ended exactly one line above the line that now carries the anchor row. Widened to the carrying line: `mcp/tests/evidence-lifecycle.toml:1182-1182` → `mcp/tests/evidence-lifecycle.toml:1182-1183` (row 344); `mcp/tests/evidence-lifecycle.toml:1252-1252` → `mcp/tests/evidence-lifecycle.toml:1252-1253` (row 345); `mcp/tests/evidence-lifecycle.toml:1272-1272` → `mcp/tests/evidence-lifecycle.toml:1272-1273` (row 346). Every line the author cited stays inside its range; no claim, Anchor cell or other range was dropped or re-worded, and each named anchor now resolves inside the widened range.
- 2026-09-18T19:53:17+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document** (one table row, two anchors). The row cited `evidence-lifecycle.toml:384-384` for `"mcp/tests/curator_coherence_test_support.py"` — the `[[artifact]]` header, one line above the `path = …` line that carries it — and `425-425` for `"mcp/tests/test_post_integration_cleanup_guidance.py"`, one line above the consumer entry that carries it. Both ranges were widened by one line (`384-385`, `425-426`) rather than re-pointed; the two consumer-list ranges and the claim are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "closeout_fixture_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:320-320. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "closeout_input_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:338-338. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "owner = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:1182-1182. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "owner = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1252-1252. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "owner = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1272-1272. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/closeout_fixture_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:320-320. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/closeout_input_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:338-338. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:28+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **added the L23 section** — the four consumer entries this leaf appended across three already-governed artifacts (item 2's merge case on the common-base harness; the item-13 gate-boundary case on the catalogue fixture and on the lane manifest; the item-16 case on the lane manifest, because it reads the shipped registries), the fact that no contract and no artifact was added so the populations stay at **15 / 65**, and this candidate's digest measured by re-hashing the file, `25b00f88…`, which is the value `test_dependency_ownership_ast_helpers.LIFECYCLE_CATALOG_SHA256` carries beside the unchanged counts. It also records the shape change this leaf enforces: every row is **appended to the tail of its `consumers` list** rather than inserted in sorted position, so no other row of this file moved — which supersedes the "a `consumers` addition belongs inside its existing list … it shifts every line below it" statement the `KS-R20@v1` and L22 sections above record, and which the item-16 case pins against the shipped registries (with the paired half classifying a pure move as a report-only stale range rather than curator work). The Purpose's digest and its attribution were corrected in place rather than carried, and the earlier states are retained in their own sections. **This entry names this leaf's candidate as the reading's basis, and the commit fields are untouched** — the change is uncommitted and closeout owns the stamp.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "closeout_fixture_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:319-319. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "closeout_input_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:337-337. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "owner = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:1179-1179. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "owner = \"knowledge-snapshot-lifecycle-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1249-1249. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "owner = \"common-base-merge-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1269-1269. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/closeout_fixture_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:319-319. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/closeout_input_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:337-337. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): **added the L21 section and re-read the catalog's population claims against the file's own declarations.** This leaf appends one `[[contract]]` (`migration-census-cases`, owner `mcp/tests/migration_census_test_support.py`, evidence node `mcp/tests/test_migration_census.py::test_the_seed_writes_every_census_record_kind_through_the_shipped_batch_operation`) and one `[[artifact]]` for that same support module, so for the first time since `KS-L11` both block kinds move: the counts go **14 / 64 → 15 / 65** and the catalogue's sha256 is re-measured to `633b03ee16893ce3d0e838659d52f2bc609903f5c75b142eb41ca8c4fdabf5e6`, which re-hashing the file reproduces and which `test_dependency_ownership_ast_helpers.py` pins beside `LIFECYCLE_CONTRACT_COUNT = 15` and `LIFECYCLE_ARTIFACT_COUNT = 65`. Both blocks are appended rather than inserted, so no other row's line moved. Three population statements were corrected in place rather than carried: the Purpose's opening count, the second half's `54 artifact records`, and the closing paragraph of the `KS-R20@v1` section, whose `14 / 64` reading and `1aef5f9b…` digest are kept as the state that leaf measured. No claim was deleted and no superseded value was removed. The metadata block above now names this leaf's candidate as what was read and carries **no `lastVerifiedCommitHash`**: the body was re-read against a working candidate no commit contains, so no real commit holds the content a stamp would claim to have verified, and closeout owns the stamp. The body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): **added the L20 section** — the one `consumers` row this leaf appended to the already-registered `shared-support` artifact `mcp/tests/read_scope_test_support.py`, why that row is mandatory rather than polite (the artifact declares `consumer_scope = "exact"`, so a module that imports the fixture without being listed falsifies the equality **without touching this file**), and the two measurements that move differently for a consumer-only change: the block counts stay at **14 contracts / 64 artifacts** — re-counted here from the declarations (`64 [[artifact]]`, `14 [[contract]]`) rather than carried from prose — while the digest is re-measured to `1aef5f9b…`, which re-hashing the file reproduces and which the pin constant carries. It also records that a `consumers` insertion lands mid-list by necessity and therefore shifts every line below it, which is the drift the routes citing this file carry. **No contract and no artifact was added**; the body changed substantively and this entry is the history record, not a metadata-only refresh.
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

|`mcp/tests/closeout_input_test_support.py`|transitive typed closeout-input/repository-authority composition `test_worktree_support` imports| `mcp/tests/evidence-lifecycle.toml:316-387`; mcp/tests/evidence-lifecycle.toml:448-448 |

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

| `mcp/tests/closeout_input_test_support.py` | imported directly by `integration_branch_authority_test_support`, whose landing fixture builds the whole-tool world | `mcp/tests/evidence-lifecycle.toml:331-407`; mcp/tests/evidence-lifecycle.toml:471-471; mcp/tests/evidence-lifecycle.toml:472-472 |

| `mcp/tests/curator_coherence_test_support.py` | reached through `selected_lifecycle_test_support`, whose closeout-operation input composes it | `mcp/tests/evidence-lifecycle.toml:391-1011`; mcp/tests/evidence-lifecycle.toml:1158-1158; mcp/tests/evidence-lifecycle.toml:1160-1160 |

| `mcp/tests/integration_branch_authority_test_support.py` | imported directly: `_authority_fixture` and `_closed_external_leaf_worktrees` build the real landed leaf each whole-tool case starts from | `mcp/tests/evidence-lifecycle.toml:435` |

| `mcp/tests/repository_profile_test_support.py` | imported directly by the landing fixture (`AGENTS_REMEMBER_PROFILE_REFERENCE`) | `mcp/tests/evidence-lifecycle.toml:565` |

| `mcp/tests/fixtures/repository_profiles/node/package.json` | the declared profile fixture that same support reads | `mcp/tests/evidence-lifecycle.toml:604` |

| `mcp/tests/fixtures/repository_profiles/node/package-lock.json` | the declared profile fixture that same support reads | `mcp/tests/evidence-lifecycle.toml:643` |

| `mcp/tests/gate_certification_test_support.py` | reached through `selected_lifecycle_test_support` → `test_closeout_certification_entrypoint` | `mcp/tests/evidence-lifecycle.toml:939-1013`; mcp/tests/evidence-lifecycle.toml:1158-1158; mcp/tests/evidence-lifecycle.toml:412-412; mcp/tests/evidence-lifecycle.toml:1160-1160 |

|`mcp/tests/source_selection_test_support.py`|reached through `repository_profile_test_support`, which imports `source_selection_fixture`| `mcp/tests/evidence-lifecycle.toml:818-1014`; mcp/tests/repository_profile_test_support.py:60-60; mcp/tests/source_selection_test_support.py:20-20 |

| `mcp/tests/selected_lifecycle_test_support.py` | imported directly by the landing fixture (`selected_closeout_operation_input`) | `mcp/tests/evidence-lifecycle.toml:1038` |

| `mcp/tests/gate_certification_test_support.py` | reached through `selected_lifecycle_test_support` → `test_closeout_certification_entrypoint` | `mcp/tests/evidence-lifecycle.toml:939-1013`; mcp/tests/evidence-lifecycle.toml:1158-1158; mcp/tests/evidence-lifecycle.toml:412-412; mcp/tests/evidence-lifecycle.toml:1160-1160 |

| `mcp/tests/source_selection_test_support.py` | reached through `repository_profile_test_support`, which imports `source_selection_fixture` | `mcp/tests/evidence-lifecycle.toml:818-1014`; mcp/tests/repository_profile_test_support.py:60-60; mcp/tests/source_selection_test_support.py:20-20 |

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
2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **recorded the two consumer entries and the bytes-only re-pin they force.** This leaf
appends `mcp/tests/test_knowledge_review_surface.py` to the `consumers` list of the already-governed
artifacts `mcp/tests/diff_scope_test_support.py` and `mcp/tests/read_scope_test_support.py` — both
declared `consumer_scope = "exact"`, so the additions are obligations — and changes nothing else in
the catalogue: the population stays at **15 contracts / 65 artifacts** while the sha256 moves from
`633b03ee16893ce3d0e838659d52f2bc609903f5c75b142eb41ca8c4fdabf5e6` to
`68a64207bd808eafd31f8c6b23856302c5ef2d150a604aa8177427e5906a1012`, re-derived by re-hashing the
file and carried by the pin constant beside the unchanged counts. The new section above states that,
draws the distinction between what a census leaf moves and what a consumer leaf moves, and records
that both entries are appended to the tails of their lists so no row of this file was relocated. The
L21 record's `633b03ee…` value is kept as that tip's measurement rather than rewritten. No reference
row was touched in this pass; the card's ranges into the catalogue are the citation-reprojection
engine's to move. The metadata block above now names this leaf's uncommitted candidate in
the candidate reading recorded in the entry itself, and `lastVerifiedCommitHash` / `lastVerifiedCommitDate` are left exactly
as the last real verification set them because no commit contains this candidate. The body was
changed substantively and this entry is the history record, not a metadata-only refresh.

## 260921-ICR-L8 Three Case Modules, Six Consumer Rows, Counts Unmoved — The Eighteenth, Nineteenth And Twentieth Re-Pins

`260921-ICR-L8` (`ICR-R08@v1`, movement and relationship evolution) registers **no artifact and no
contract of its own**. Its twenty-three cases live in three ordinary unit modules —
`mcp/tests/test_knowledge_review_relationship_movement.py` (eleven),
`mcp/tests/test_knowledge_review_relationship_reach.py` (seven) and
`mcp/tests/test_knowledge_review_relationship_line.py` (five) — each authored through the public store
operations inside the existing `mcp/tests/test_knowledge_review_source_endpoints.py` enclosure and each
importing the shared builders from its siblings. Its catalog footprint is therefore **six consumer
entries**, three on each `consumer_scope = "exact"` row, and each derived from the census's own finding
(`missing=['<the module>']` with `unsupported=[]` on both rows) rather than from inspection:

- the **diff-cases** artifact (`replacement_contract = "contract:knowledge-diff-cases"`,
  `introduced_by = "260915-KS-L8"`), whose consumer list gained the three paths at `:1417-1419`: the
  cases build the enclosure over the fixture's two real committed trees and read one side's bytes back
  through that fixture's `_git` observation helper;
- the **read-scope** artifact (`replacement_contract = "contract:knowledge-read-scope-cases"`,
  `introduced_by = "260915-KS-L7"`), whose consumer list gained the same three paths at `:1457-1459`:
  the recorded paths and the family topology the moved associations are read from are that fixture's
  own.

**Both rows are appended to the tail of their list, so no earlier entry moved; the two insertions are
what moves every citation below them.** The catalog is **1689 lines** (1683 → 1689), the counts stay at
the measured **sixteen contracts / sixty-six artifacts**, and the bytes were re-pinned once per module:
`8d60a34c…` (L9's Seventeenth) → `c676b0a0…` (Eighteenth) → `b1ed7838…` (Nineteenth) → **`d2d6dc6a…`**
(Twentieth), which is `sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate and the
value `mcp/tests/test_dependency_ownership_ast_helpers.py`'s `LIFECYCLE_CATALOG_SHA256` carries beside
the unchanged counts.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The three consumer entries on the diff-cases artifact's exact list, appended newest-last.** | "mcp/tests/test_knowledge_review_relationship_movement.py"; "mcp/tests/test_knowledge_review_relationship_reach.py"; "mcp/tests/test_knowledge_review_relationship_line.py" |mcp/tests/evidence-lifecycle.toml:1424; mcp/tests/evidence-lifecycle.toml:1428-1424; mcp/tests/evidence-lifecycle.toml:1425; mcp/tests/evidence-lifecycle.toml:1429-1425; mcp/tests/evidence-lifecycle.toml:1426; mcp/tests/evidence-lifecycle.toml:1430-1426|
| **The same three on the read-scope artifact's exact list.** | "mcp/tests/test_knowledge_review_relationship_movement.py"; "mcp/tests/test_knowledge_review_relationship_reach.py"; "mcp/tests/test_knowledge_review_relationship_line.py" |mcp/tests/evidence-lifecycle.toml:1468; mcp/tests/evidence-lifecycle.toml:1474-1468; mcp/tests/evidence-lifecycle.toml:1469; mcp/tests/evidence-lifecycle.toml:1475-1469; mcp/tests/evidence-lifecycle.toml:1470; mcp/tests/evidence-lifecycle.toml:1476-1470|
| The two artifacts' own declarations, which are what make each module a source-derived consumer of both. | `replacement_contract`; `consumer_scope` | mcp/tests/evidence-lifecycle.toml:94-96; mcp/tests/evidence-lifecycle.toml:1394-1396 |
| The enclosure the three modules extend rather than duplicating. | `build_endpoint_fixture`; `EndpointFixture` | mcp/tests/test_knowledge_review_source_endpoints.py:215-247; mcp/tests/test_knowledge_review_source_endpoints.py:199-202 |
| **The counts this change does not move, the bytes it does, and the constant that carries them (`d2d6dc6a…`, the Twentieth re-pin).** | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:44-46 |

## Update History
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`, confirmed from the enclosure contract): **body update for the six consumer rows this leaf's three modules obliged, and every live row re-derived against the 1689-line catalog (1683 → 1689).** The three new case modules import `diff_scope_test_support` and `read_scope_test_support`, whose `[[artifact]]` rows carry `consumer_scope = "exact"`, so each module's path was appended to **both** consumer lists: `:1417-1419` on the diff-cases artifact and `:1457-1459` on the read-scope artifact, derived from the census's own `missing=[…]` finding with `unsupported=[]` on both. **No row was added, removed or renamed and no artifact's identity moved**: the population stays sixteen contracts / sixty-six artifacts, and the catalog was re-pinned once per module — `8d60a34c…` → `c676b0a0…` → `b1ed7838…` → `d2d6dc6a…`, the last being `sha256sum mcp/tests/evidence-lifecycle.toml` on the resolved candidate. **Citation accounting:** rows citing positions below the first insertion kept their ranges; the rows at or above the two insertions moved by their cumulative delta (+3 between `:1414` and `:1453`, +6 from `:1454`), which is why this card and its sibling cards' later ranges were re-derived rather than shifted by a remembered delta. **Metadata removal:** this card's candidate-reading metadata rows were removed under the developer's 2026-09-22 rule, and the history sentence that pointed at such a row was corrected in the same pass so the document no longer claims the row exists. No verification stamp was advanced: the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-20T06:55+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **two consumer paths were appended to one already-governed row, and this card's population claim is unchanged because nothing else moved.** The `generation_test_support` artifact's `consumers` list gained `mcp/tests/test_worktree_sync.py` (which now consumes the `shared-support` fixture) and `mcp/tests/test_sync_parked_candidate.py` (which imports that module and is therefore a consumer by the census's own propagation rule). This is the consumer-completeness oracle, not the byte pin: the catalogue was already stale **without the file changing** for the first of those two, which is exactly the two-registry trap this master disclosed as D-19. No artifact was registered, no contract added, no row removed: the governed populations stay at **fifteen contracts / sixty-five artifacts**, and the digest pinned in the sibling card was re-derived to `c499cbcc…`. Verification metadata is **advanced to the candidate's base `f79f4db7`** with the working candidate named beside it; closeout owns the committed stamp.

## 260921-ICR-L10 Three Consumer Rows, And The Catalog Digest They Re-Pin

`260921-ICR-L10` (`ICR-R10@v1`, complete bounded pagination) registers one ordinary unit module
against **three** exact-scope consumer rows, which is why this manifest moves at all: the new
`mcp/tests/test_review_bounded_pagination.py` consumes three catalog-registered support modules, and each
row is appended to its own artifact's `consumers` list, newest-last, so every entry at or below each
insertion reads one line lower than the accounts above record it. The first list's three relationship
rows sit at 1418–1420 and the read-scope artifact's three at 1459–1461, one line further down than the
pre-leaf accounts.

Because a governed manifest changed, `LIFECYCLE_CATALOG_SHA256` is re-pinned to `b4d4a7f9…` as this
leaf's deliberate re-pin; the population is unchanged at **sixteen** contracts and **sixty-six**
artifacts, and the two counts beside the digest are untouched.

## Update History
- 2026-09-23T00:30:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; production line at this leaf's base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **three consumer rows appended, and the catalog digest re-pinned.** The new pagination module's
three exact-scope consumer rows are appended newest-last to the `knowledge-diff-cases` artifact's list
(now 1418–1420) and the `knowledge-read-scope-cases` artifact's list (now 1459–1461), so every row below
each insertion moved one line; `LIFECYCLE_CATALOG_SHA256` is re-pinned to `b4d4a7f9…` with the population
unchanged at sixteen contracts and sixty-six artifacts. Every row on this card that cited a manifest line
was re-derived against this candidate. No verification stamp was advanced: nothing in this leaf is committed, so the commit/closeout stamp remains closeout's.
## 260921-ICR-L26 Four Consumer Rows For One New Case Module

`260921-ICR-L26` (`ICR-R26@v1`) added **four** consumer paths to this registry and nothing else: the
module `mcp/tests/test_knowledge_review_subject_isolation.py` is a source-derived consumer of four
existing artifacts, so each of their `consumers` lists gained that one path — the rows for
`mcp/tests/curator_coherence_test_support.py`, `mcp/tests/fixtures/repository_profiles/node/package-lock.json`,
`mcp/tests/diff_scope_test_support.py` and `mcp/tests/read_scope_test_support.py`, all
`consumer_scope = "exact"`. No `[[artifact]]` row, no `[[contract]]` row and no consumer was removed, so
the population this file publishes stays at **sixteen contracts / sixty-six artifacts**, and the file's
own byte digest moved to `4d874fb54c627549db098177caa477040e09ca63c7ae2cba2246bd1390a338e0`, which the
ownership gate re-pins in the same change set.

**Why these four and no others.** Each path is the census's own answer for that artifact
(`missing=['mcp/tests/test_knowledge_review_subject_isolation.py']`, `unsupported=[]`): the fixture's
task topology, the repository profile it builds the enclosure over, the two snapshots whose recorded
identities the classification reads, and the authorship envelope plus recorded family membership the
context rows are reached through. A consumer row states the artifact is *used* by that module; it does
not promote the module into the lifecycle, and the artifact delta this leaf's proof observes is
deliberately empty.

## Update History
- 2026-09-23T02:40:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): **four consumer rows for one new case module, nothing registered (`ICR-R26@v1`).** The card names the four artifacts, the census finding each row was derived from, and the fact that the contract/artifact counts do not move. **Citation accounting:** the measured baseline check reports **zero** enforced findings for this card; the consumer rows it cites are list members rather than declarations, and this leaf appended one path to each. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header already names this leaf's base, and the governed closeout owns the real stamp.
## 260921-ICR-L12 Three Exact-Scope Consumer Rows For The Committed-Leaf Cases

`260921-ICR-L12` (`ICR-R12@v1`) adds **three** consumer rows to this catalog and no artifact and no
contract. The new module `mcp/tests/test_historical_committed_leaf_review.py` is a source-derived
consumer of exactly the rows the census's own finding names —
`missing=['mcp/tests/test_historical_committed_leaf_review.py']` with `unsupported=[]` on three rows:

- the diff-scope fixture row (`contract:knowledge-diff-cases`), whose two snapshots and two real
  committed trees the R01 enclosure is built over;
- the read-scope fixture row (`contract:knowledge-read-scope-cases`), whose repository, recorded
  anchors and tracked paths the enclosure's records are read from;
- the unit-regression consumer list, which gained the module's own path.

Every row is `consumer_scope = "exact"`, so the registration is complete rather than permissive: a
fourth fixture dependency would have to be registered rather than inferred. **Nothing was registered,
no row was removed and no artifact's identity moved**, which is why the file's own digest change is a
consumer-list change and not an artifact delta — the population stays at sixteen contracts / sixty-six
artifacts, and `mcp/tests/test_dependency_ownership_ast_helpers.py` re-pins the catalog to
`4ab067e360c7807c3051ad71058c09058225f1e9155e7111da6e95c73cac0258`.

## Update History
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **three exact-scope consumer rows for the committed-leaf cases (ICR-R12@v1).** The new case module
is registered as a consumer of the diff-scope fixture row, the read-scope fixture row and the
unit-regression list, each `consumer_scope = "exact"`; no artifact, no contract and no identity moved,
and the population stays at sixteen contracts / sixty-six artifacts. **Citation accounting:** the rows
below the insertions were re-derived against the candidate; the file's own digest is re-pinned in
`test_dependency_ownership_ast_helpers.py`. **Stamp accounting:** no verification stamp was advanced —
the candidate is uncommitted and the governed closeout owns the real stamp.
## 260921-ICR-L22 Eight Consumer Rows For Two New Case Modules, Counts Unmoved

`260921-ICR-L22` (`ICR-R22@v1`, managed Git recovery rebinding) adds **eight** consumer entries to this
catalog and registers nothing. The two modules this leaf adds —
`mcp/tests/test_review_sync_rebinding.py` (the sync-side cases: what a managed sync measured and the
durable rebinding record it published) and `mcp/tests/test_review_sync_movement_read.py` (the read-side
cases: what the shipped `read_knowledge_review` renders about that measurement) — are source-derived
consumers of the same **four** existing rows, so every one of those `consumer_scope = "exact"` lists
gained **both** paths, inserted newest-last in the position the list already keeps:

| Artifact | `[[artifact]]` block / `path` row | `consumers` entries | the two inserted rows |
| --- | --- | --- | --- |
| `mcp/tests/fixtures/repository_profiles/node/package-lock.json` | `:669` / `:670` | 118 → **120** (`:684-803`) | `:802-803` |
| `mcp/tests/merge_case_test_support.py` | `:1285` / `:1286` | 7 → **9** (`:1300-1308`) | `:1307-1308` |
| `mcp/tests/diff_scope_test_support.py` | `:1401` / `:1402` | 17 → **19** (`:1416-1434`) | `:1433-1434` |
| `mcp/tests/read_scope_test_support.py` | `:1437` / `:1438` | 27 → **29** (`:1452-1480`) | `:1479-1480` |

The four rows are the `node:` fixture row the census's own propagation rule reaches through the other
three, `contract:common-base-merge-cases`, `contract:knowledge-diff-cases` and
`contract:knowledge-read-scope-cases`; each path's derivation is the census's own finding, recorded in
`mcp/tests/test_dependency_ownership_ast_helpers.py`'s constant docstring and in that card's sections
below, which this leaf re-pinned three times in the same change set.

**The four insertions moved every line below them, and that is this card's citation fact.** Each row
contributes two lines, so a line above the first insertion is unchanged, while a line below the first
reads **+2**, below the second **+4**, below the third **+6** and below the fourth **+8**: the file's own
extent is **1702 → 1710 lines**, `merge_case_test_support.py`'s own block moves `:1284` → `:1286`,
`diff_scope_test_support.py`'s `:1398` → `:1402` and `read_scope_test_support.py`'s `:1432` → `:1438`, so
every row this card or an earlier account cites at or below one of the four insertions reads lower than
that account records it.

**Nothing was registered, no row was removed and no artifact's identity moved**, so the counted shape is
unchanged: **66 `[[artifact]]` blocks and 16 `[[contract]]` blocks** on the live file, whose own bytes
measure `d07c2f9d456b0f658228c91aecb2a1f3da8d13e2b6575b6b40b0b0d2ca165f6b`
(`sha256sum mcp/tests/evidence-lifecycle.toml`), which
`mcp/tests/test_dependency_ownership_ast_helpers.py` re-pins in the same change set as its Twenty-fourth,
Twenty-fifth and Twenty-sixth deliberate re-pins. The Purpose paragraph's `65 [[artifact]]` /
`15 [[contract]]` reading is `260915-KS-L30`'s **frozen-candidate** count rather than a live one — the
live count is **66 / 16** — and this leaf's own artifact delta is exactly empty.

## Update History
- 2026-09-23T17:15:00+02:00 — 260921-ICR-L22 curator (uncommitted change set on `ar/260921-icr-l22`, base `e605822eb3bf83bf63a45963c5f51d5fc28859ee):` **eight consumer rows for two new case modules, nothing registered (`ICR-R22@v1`).** The two modules the leaf adds each consume the same four exact-scope rows, so each list gained both paths; the card names each artifact, its block and entry extents, and the fact that no artifact, no contract and no identity moved. **Citation-shift consequence:** the four two-line insertions at `:802-803`, `:1307-1308`, `:1433-1434` and `:1479-1480` moved every line below them by +2, +4, +6 and +8 respectively, so the file's extent is 1702 → 1710 lines and every range below an insertion reads lower than the account above it records it; the curator repairs those ranges per row, separately. **Stamp accounting:** no verification stamp was advanced — the header's verification pair names this leaf's recorded base `e605822e` because nothing in this leaf is committed, and the governed closeout owns the real stamp.
