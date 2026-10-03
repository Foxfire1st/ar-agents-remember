# mcp/tests/evidence-lifecycle.toml

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-18T04:35 +02:00 against the uncommitted KS-L14 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Declares shared test-support/fixture ownership, fidelity, lifetime, replacement contracts, and
exact consumers. **Current reading (`260928-MIK-L24`, the Thirty-third deliberate re-pin): 80 `[[artifact]]`
records and 16 `[[contract]]` blocks, 2080 lines, sha256
`6fb4934d9120e1f593aaaa0e5534f49e01bf88a0f4dee04592f75063575fab65`** (see the section at the end of this
card). The rest of this paragraph is an earlier reading, kept as history, and was corrected by L24 so that
it no longer reads as current: **at `260915-KS-L30` the catalog contained 65 artifact records and fifteen
executable replacement contracts**,
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

## Current verification scope

The exact Node package-lock fixture consumer list includes test_review_read_latency.py because its reused real world reaches that fixture. The capture matrix consumes no governed artifact. Contracts/artifacts and their refusal/delta rules remain unchanged.

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets and exact ranges were checked against the current working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

- The schema version and the large-fixture discovery threshold remain explicit. [1]
- The four retained knowledge contracts and their evidence nodes. [2]
- Closeout fixture support names the retained code/memory transaction replacement. [3]
- Closeout-input support declares the cleanup-guidance consumer. [4]
- **The knowledge branching fixture's contract and artifact row, whose consumer list 260915-KS-L2 corrected to the five source-observed importers and 260915-KS-L6 extended to the two portable modules.** [5]
- The knowledge graph case-support contract and its matching artifact row, added by 260915-KS-L2 with three declared consumers. [6]
- The candidate-batch case-harness contract and its artifact row, added by 260915-KS-L3 with two declared consumers and a real evidence node. [7]
- **The snapshot-lifecycle contract and artifact row, with an exact consumer list that 260915-KS-L6 extended to the portable boundary module.** [8]
- **The common-base-merge contract and artifact row, whose exact consumer list 260915-KS-L6 extended to both portable modules.** [9]
- **The two consumer declarations 260915-KS-L6 added to the branching-fixture row.** [10]
- **The consumer declaration 260915-KS-L6 added to the snapshot-lifecycle row — the boundary module only, because the roundtrip module does not import that harness.** [11]
- **The two consumer declarations 260915-KS-L6 added to the merge-case row.** [12]
- **The node that makes that contract's claim real: both sides' disjoint edits survive into a closed, published candidate that carries no verdict.** [13]
- **The node that makes that contract's closedness claim real: a WAL-resident batch is published whole while a main-file copy is not.** [14]
- The lane rows that keep the knowledge test modules in the certifying collection path, including the two this leaf registered. [15]
- The one-to-one card for the batch harness, which records what it builds through the real seam. [16]
- The snapshot harness card, which records the registered owner and the exact consumer set. [17]
- The consumer entry this leaf appended to the snapshot harness, which is a row in a list rather than a new registration — the populations do not move because of it. [18]
- The referenced transaction test definition exists in the current source. [19]
- None [20]
- Closeout-input support names the same retained code/memory transaction replacement node. [21]
- None [22]
- The snapshot harness card, which records the registered owner and the exact consumer set. [23]
- The referenced transaction test definition exists in the current source. [24]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.

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
| artifact | `path = "mcp/tests/migration_census_test_support.py"`, `kind = "shared-support"`, `authority = "internal-canonical"`, `owner = "migration-census-cases"`, `category = "unit-regression"`, `fidelity = "local-composition"`, `cadence = "affected"`, `introduced_by = "260915-KS-L21"`, `lifetime = "permanent"`, `replacement_contract = "contract:migration-census-cases"`, `consumer_scope = "exact"` | `mcp/tests/evidence-lifecycle.toml:1676-1692`; mcp/tests/evidence-lifecycle.toml:164-164; mcp/tests/evidence-lifecycle.toml:1200-1200; mcp/tests/evidence-lifecycle.toml:1229-1229; mcp/tests/evidence-lifecycle.toml:1249-1249; mcp/tests/evidence-lifecycle.toml:1271-1271; mcp/tests/evidence-lifecycle.toml:1295-1295; mcp/tests/evidence-lifecycle.toml:1323-1323; mcp/tests/evidence-lifecycle.toml:1356-1356; mcp/tests/evidence-lifecycle.toml:1444-1444; mcp/tests/evidence-lifecycle.toml:1492-1492; mcp/tests/evidence-lifecycle.toml:1514-1514; mcp/tests/evidence-lifecycle.toml:1693-1693; mcp/tests/evidence-lifecycle.toml:1711-1711; mcp/tests/evidence-lifecycle.toml:1697-1697; mcp/tests/evidence-lifecycle.toml:1700-1700; mcp/tests/evidence-lifecycle.toml:96-96; mcp/tests/evidence-lifecycle.toml:116-116; mcp/tests/evidence-lifecycle.toml:135-135; mcp/tests/evidence-lifecycle.toml:153-153; mcp/tests/evidence-lifecycle.toml:172-172; mcp/tests/evidence-lifecycle.toml:193-193; mcp/tests/evidence-lifecycle.toml:213-213; mcp/tests/evidence-lifecycle.toml:235-235; mcp/tests/evidence-lifecycle.toml:253-253; mcp/tests/evidence-lifecycle.toml:274-274; mcp/tests/evidence-lifecycle.toml:295-295; mcp/tests/evidence-lifecycle.toml:316-316; mcp/tests/evidence-lifecycle.toml:337-337; mcp/tests/evidence-lifecycle.toml:355-355; mcp/tests/evidence-lifecycle.toml:382-382; mcp/tests/evidence-lifecycle.toml:402-402; mcp/tests/evidence-lifecycle.toml:486-486; mcp/tests/evidence-lifecycle.toml:509-509; mcp/tests/evidence-lifecycle.toml:527-527; mcp/tests/evidence-lifecycle.toml:548-548; mcp/tests/evidence-lifecycle.toml:566-566; mcp/tests/evidence-lifecycle.toml:585-585; mcp/tests/evidence-lifecycle.toml:605-605; mcp/tests/evidence-lifecycle.toml:644-644; mcp/tests/evidence-lifecycle.toml:683-683; mcp/tests/evidence-lifecycle.toml:1095-1095; mcp/tests/evidence-lifecycle.toml:1126-1126; mcp/tests/evidence-lifecycle.toml:1144-1144; mcp/tests/evidence-lifecycle.toml:1184-1184; mcp/tests/evidence-lifecycle.toml:1208-1208; mcp/tests/evidence-lifecycle.toml:1237-1237; mcp/tests/evidence-lifecycle.toml:1257-1257; mcp/tests/evidence-lifecycle.toml:1279-1279; mcp/tests/evidence-lifecycle.toml:1307-1307; mcp/tests/evidence-lifecycle.toml:1331-1331; mcp/tests/evidence-lifecycle.toml:1364-1364; mcp/tests/evidence-lifecycle.toml:1384-1384; mcp/tests/evidence-lifecycle.toml:1403-1403; mcp/tests/evidence-lifecycle.toml:1421-1421; mcp/tests/evidence-lifecycle.toml:1455-1455; mcp/tests/evidence-lifecycle.toml:1501-1501; mcp/tests/evidence-lifecycle.toml:1522-1522; mcp/tests/evidence-lifecycle.toml:1550-1550; mcp/tests/evidence-lifecycle.toml:1588-1588; mcp/tests/evidence-lifecycle.toml:1607-1607; mcp/tests/evidence-lifecycle.toml:1625-1625; mcp/tests/evidence-lifecycle.toml:1701-1701; mcp/tests/evidence-lifecycle.toml:1719-1720; mcp/tests/evidence-lifecycle.toml:745-745; mcp/tests/evidence-lifecycle.toml:746-746; mcp/tests/evidence-lifecycle.toml:1312-1312 |

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

- **The first artifact's two new consumer rows: the Node package-lock fixture, whose `consumer_scope = "exact"` list both new modules joined.** [25]
- **The second artifact's two new consumer rows: the snapshot-lifecycle shared support module, whose `consumer_scope = "exact"` list both new modules joined.** [26]
- The artifact the first pair belongs to, and the scope both lists carry. [27]
- The artifact the second pair belongs to. [28]
- The two block kinds whose counts this change does not move, and the sha256 it does move. [29]
- The constant this file's bytes pin, re-pinned deliberately in the same change. [30]
- The reason no third fixture exists: both new modules import the existing builders rather than introducing one. [31]

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

- **The first consumer row: the diff-scope shared support module, whose `consumer_scope = "exact"` list this leaf's module joined.** [32]
- **The second consumer row: the read-scope shared support module, whose `consumer_scope = "exact"` list this leaf's module joined.** [33]
- The two block kinds whose counts this change does not move, and the sha256 it does move. [34]
- The constant this file's bytes pin, re-pinned deliberately in the same change. [35]
- The reason no third fixture exists: the case module composes the two existing ones. [36]

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

- **The first of the two consumer rows: the diff-cases artifact's exact consumer list, which the new module joins.** [37]
- **The second: the read-scope artifact's exact consumer list.** [38]
- The two artifacts' own subjects, which are what make the module a source-derived consumer of each. [39]
- **The imports that make it a consumer: the candidate content path from the diff-scope support and the batch path from the read-scope support.** [40]
- The fixture module it builds on rather than duplicating, so no third enclosure fixture was introduced. [41]
- **The pinned counts and the re-pinned digest, in the module that measures this file.** [42]

## 260921-ICR-L6 One Consumer Row On The Read-Scope Artifact, Beside L18's Landed One

This leaf's ICR-R06 cases drive the real review composition over **two real read-scope snapshots**, so
its case module consumes `mcp/tests/read_scope_test_support.py` — the artifact whose
`consumer_scope = "exact"` requires its `consumers` list to equal the source-derived consumer set. One
path was appended to that list, and **no artifact and no contract was registered, none removed, and no
other row's identity moved**:

- **The row this leaf registered: its own case module, on the read-scope artifact's `consumer_scope = "exact"` list.** [43]
- **The row this leaf registered: its own case module, on the read-scope artifact's `consumer_scope = "exact"` list.** [44]
- **The row L18's landed consequence repair had already carried, now the row immediately below this leaf's: `mcp/tests/test_read_ar_files.py` imports the same fixture and was the path L19's landing left unregistered. The two are kept as a set — the census compares consumer sets — so each path is named exactly once.** [45]
- The artifact both rows belong to: its `[[artifact]]` block, its `knowledge-read-scope-cases` owner, its `consumer_scope = "exact"` and the list's exact extent on the merged candidate. [46]
- The constant this file's bytes pin, re-pinned at the sync, and the two count constants this change leaves alone. [47]

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
## 260921-ICR-L44 One Consumer Row On The Read-Scope Artifact, Counts Unmoved

The member-source locator cases in `mcp/tests/test_review_family_member_sources.py` build their store
through `read_scope_test_support.build_read_scope_fixture`, so the module is a source-derived consumer of
`mcp/tests/read_scope_test_support.py`, whose `consumer_scope = "exact"` requires the `consumers` list to
equal that set. One path was appended at the end of that list; no artifact or contract was registered or
removed, so the contract and artifact counts do not move.

- **The row registered for the member-source cases, at the end of the read-scope artifact's exact consumer list.** [48]
- The import that makes the module a consumer. [49]

**The byte pin is not current on either side of this change.** The one-line insertion changes the file's
bytes, and `LIFECYCLE_CATALOG_SHA256` in `mcp/tests/test_dependency_ownership_ast_helpers.py` matches
neither the leaf's base bytes nor the candidate bytes; the dependency-ownership lane's two red cases
reproduce on the base with identical findings, so this row adds no new failure of that kind, and
re-pinning is the owner of that lane's work. The insertion shifts every later line of the file by one, so
cards citing later ranges by line read one line lower than on the base.

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

- **The first consumer row: the diff-cases shared support module, whose `consumer_scope = "exact"` list this leaf's module joined.** [50]
- **The second: the read-scope shared support module's exact list, where the new row sits above L6's registered module and L18's landed one.** [51]
- The two artifacts' own declarations, which are what make the module a source-derived consumer of each. [52]
- **The fixture it extends rather than duplicating, and the observation helper its cases read bytes back through.** [53]
- The tracked paths the read-scope consumer row is derived from. [54]
- **The counts this change does not move, the bytes it does, and the constant that carries them.** [55]

## 260921-ICR-L45 Two Consumer Paths For The Per-Target Realization Cases

The new ordinary unit module `mcp/tests/test_curator_realization_authoring.py` is added as an exact
consumer to two existing artifacts whose `consumer_scope = "exact"` lists already carry its
curator-ingest siblings: the `mcp/tests/fixtures/repository_profiles/node/package-lock.json` artifact
(inserted at `:699`, below `test_curator_ingest_write_and_retention.py`) and the
`mcp/tests/snapshot_lifecycle_test_support.py` artifact (`contract:knowledge-snapshot-lifecycle-cases`,
inserted at `:1286`). `test_dependency_ownership_ast_helpers.py` requires every reaching consumer to be
listed; the worker found both omissions through it. No artifact, contract, node or edge was added,
removed or renamed. **Every line below `:699` moved by one, and every line below `:1286` by two**; body
rows citing this file were re-pointed through the exact base-to-candidate line map.

- The first exact consumer row. [56]
- The snapshot-lifecycle support artifact's consumer list with the new exact consumer. [57]

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

- **The three consumer entries on the diff-cases artifact's exact list, appended newest-last.** [58]
- **The same three on the read-scope artifact's exact list.** [59]
- The two artifacts' own declarations, which are what make each module a source-derived consumer of both. [60]
- The enclosure the three modules extend rather than duplicating. [61]
- **The counts this change does not move, the bytes it does, and the constant that carries them (`d2d6dc6a…`, the Twentieth re-pin).** [62]

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

## 260921-ICR-L31 The Twenty-Seventh And Twenty-Eighth Deliberate Re-Pins

**This leaf registered nothing and moved no artifact's identity, and it re-pinned the catalog twice
(`ICR-R31@v1`).** The proof's population stays at **sixteen contracts / sixty-six artifacts**. The
Twenty-seventh re-pin accompanied the leaf's first case module: the census reported
``missing=['mcp/tests/test_review_family_context.py']`` with ``unsupported=[]`` on both of the
source-derived consumer rows it reaches — ``mcp/tests/diff_scope_test_support.py`` (the two snapshots,
their recorded identities and the two real trees the enclosure is built over) and
``mcp/tests/read_scope_test_support.py`` (the authorship envelope and the recorded family/membership
topology the composition reads) — so each row gained that one path and the module gained its lane row.
The catalog moved from ``caf1b9ee…`` to ``b1c38ed8…``.

The Twenty-eighth re-pin accompanied fix round 1, which moved the four population cases into a **new**
case module rather than growing the first one past the soft rail: the same two ``consumer_scope =
"exact"`` rows each gained ``mcp/tests/test_review_family_context_population.py`` and that module gained
its lane row, so the catalog moved from ``b1c38ed8…`` to
``23dd7c0f85b50585e8968122f60f50e87e15bfbfa241b28b77b7c71b2a41e252``, measured with ``sha256sum`` on
the resolved candidate.

**Both re-pins are recorded in the module's own docstring, not here**, because that docstring is the
authority the pin is asserted against; this card records what changed in *this file*: four added
consumer entries across two rows and no removed row, no added contract and no moved artifact identity.

**Citation accounting:** seven rows of this card were re-anchored through the measured insertion map —
the two insertions shift every quoted path below them, and each mapped range was confirmed to hold the
row's anchor **in the right consumer block** rather than at the nearest matching string.

## 260921-ICR-L29 One Consumer Path, And No Registration

`ICR-R29@v1` (knowledge bootstrap initialization publication and recovery) changes this catalogue in
exactly one place. The new ordinary unit module `mcp/tests/test_knowledge_bootstrap.py` drives the
shipped `agents-remember knowledge-bootstrap` subcommand over a real coordination world, so it consumes
the shared repository-profile fixture rather than carrying a private copy of one; the census derived
that as a single finding on the `mcp/tests/fixtures/repository_profiles/node/package-lock.json` artifact
(`missing=['mcp/tests/test_knowledge_bootstrap.py'], unsupported=[]`), and only that artifact's
`consumers` list changed.

**No artifact, contract, node or edge was added, removed or renamed.** The declared population is
therefore unchanged at sixteen contracts and sixty-six artifacts, which is what the re-pinned
`LIFECYCLE_CATALOG_SHA256` in `mcp/tests/test_dependency_ownership_ast_helpers.py` asserts beside it.
Every line below the insertion point (`:734`) is one line lower than it was at the leaf's base commit,
which is why a card citing this file by line must be read against this candidate rather than against
the base.

## 260921-ICR-L43 One Consumer Path On The Read-Scope Support Artifact

The new ordinary unit module `mcp/tests/test_knowledge_review_attributed_source_content.py` imports the
population paths of `mcp/tests/read_scope_test_support.py`, so it is added to that artifact's exact
`consumers` list directly below the sibling `test_knowledge_review_source_content.py`. That is the only
change to this catalogue: no artifact, contract, node or edge was added, removed or renamed. **The
insertion is at `:1481`, so every line below it moved by one**; rows of this card citing lines below it
were shifted by one after each was verified against both the base and this candidate.

- The read-scope artifact's consumer list with the new exact consumer. [63]

## 260921-ICR-L57 Twenty-Nine Consumer Paths On Five Exact Rows, Counts Unmoved

The master's exit gate found **five** `consumer_scope = "exact"` rows whose declared `consumers` lists no
longer matched the source-derived ownership census. Each finding had `unsupported=[]`: modules that reach
the artifact were missing, and nothing was over-declared. Eight ICR case modules had landed without their
rows: `test_review_assessment_history.py`, `test_review_assessment_history_repairs.py`,
`test_review_recorded_knowledge.py`, `test_review_unchanged_knowledge.py`,
`test_curator_candidate_progression.py`, `test_curator_family_retention.py`, `test_curator_scope.py` and
`test_knowledge_review_attributed_source_content.py`. The same leaf also split three case modules across
the 1200-line rail, and the census named the three new modules on the two rows their siblings consume.
`260921-ICR-L57` added exactly the census's missing paths, 29 in all:

| Artifact | Paths added | Consumers now |
| --- | ---: | ---: |
| `mcp/tests/curator_coherence_test_support.py` | 2 | 54 |
| `mcp/tests/fixtures/repository_profiles/node/package-lock.json` | 7 | 133 |
| `mcp/tests/snapshot_lifecycle_test_support.py` | 3 | 13 |
| `mcp/tests/diff_scope_test_support.py` | 9 (6 + the 3 split modules) | 31 |
| `mcp/tests/read_scope_test_support.py` | 8 (5 + the 3 split modules) | 42 |

Each split module sits directly below the sibling it was split from. The attributed-source-content module
sits below `test_knowledge_review_source_content.py`, and the curator modules sit after
`test_curator_realization_authoring.py`. Everything else is appended at the end of its row. **No
artifact, contract, node or edge was added, removed or renamed**, so the populations stay at sixteen
contracts and sixty-six artifacts. Because the bytes moved, the catalog pin in
`test_dependency_ownership_ast_helpers.py` was re-pinned (the Thirty-second deliberate re-pin) to
`1c682524157cb12075319069b03410b39053317946a61847c51a603c146a68b2`. That pin had already been stale since three earlier leaves (L43, L44 and L45) added
consumer paths without a re-pin; see that card. The oracle reports
`evidence-lifecycle: PASS (66 governed artifacts)` on the candidate. Body rows citing this file were
re-pointed through the exact base-to-candidate line map. Ranges that span an insertion grew with the
list they cite.

- The curator-coherence support artifact's exact consumer list, with its two added paths (`test_review_assessment_history.py`, `test_review_assessment_history_repairs.py`) at the end. [64]
- The package-lock artifact's exact consumer list, with the three curator modules after `test_curator_realization_authoring.py` and four paths at the end. [65]
- The snapshot-lifecycle support artifact's exact consumer list, with the three curator modules. [66]
- The diff-scope support artifact's exact consumer list, with each split module below its sibling. [67]
- The read-scope support artifact's exact consumer list, with the same three split modules and the attributed-source-content module. [68]
- The byte pin these additions oblige. [69]


## 260928-MIK-L24 Fourteen New Rows And Five Consumer Additions, Counts 16 / 80

`260928-MIK-L24` (MIK-R24) found the integration lane red on its base: the L12 and L20–L23 leaves had
landed shared test support, and L21 the Doc14 fixtures, without catalog rows. By architect ruling this leaf
registers them with its own. The change is **insertion-only (+321/−0)**. No row, consumer or field was
removed or changed, and the new consumers are appended without re-sorting.

- **Fourteen new `[[artifact]]` rows** (`:1776-2079`). Each has its source-derived exact consumers and a
  `node:` replacement contract in a real consumer:
  - five `shared-support` modules: `knowledge_validator_test_support.py` (`introduced_by` `260928-MIK-L22`),
    `knowledge_index_test_support.py` (`260928-MIK-L23`), `knowledge_writer_test_support.py` (`260928-MIK-L12`),
    `knowledge_census_test_support.py` (`260928-MIK-L20`) and `knowledge_conversion_test_support.py` (`260928-MIK-L24`);
  - nine `fixture` files under `mcp/tests/fixtures/knowledge_files/` (`260928-MIK-L21`): the six Doc14 §4 examples
    `4.1`–`4.6`, `4.1-worktrees-overview.json`, `layout.json` and `r21-integrate.py.json`.
- **Five existing rows gain consumers:** `curator_coherence_test_support.py` (1),
  `fixtures/repository_profiles/node/package-lock.json` (9), `merge_case_test_support.py` (2),
  `generation_test_support.py` (2) and `read_scope_test_support.py` (1). The conversion toolchain case
  joins the curator-coherence and read-scope rows, and the crossing case joins the merge-case and
  generation rows.
- **Populations:** 16 contracts (unchanged) and 80 artifacts (from 66). The pin in
  `test_dependency_ownership_ast_helpers.py` moves from `1c682524…` to `6fb4934d…`.

**Follow-up for the parallel L28 (review R1 finding 12; done by `260928-MIK-L28`, see the next section):** L28's `test_knowledge_proofs.py` imports two
of these `exact` rows (`knowledge_index_test_support`, `knowledge_writer_test_support`). It must add
itself to their consumer lists, and re-pin, once L24 lands.

- The five new shared-support rows. [70]
- The nine new fixture rows for the Doc14 knowledge-file examples. [71]
- The consumer additions: the conversion toolchain case on the curator-coherence and read-scope rows, the crossing case on the merge-case and generation rows. [72]

## 260928-MIK-L28 One Consumer On Three Exact Rows, Counts 16 / 80

`260928-MIK-L28` (MIK-R28, first-class test proofs) appends its new case module
`mcp/tests/test_knowledge_proofs.py` to three existing `consumer_scope = "exact"` consumer lists, without
re-sorting: `fixtures/repository_profiles/node/package-lock.json`, `knowledge_index_test_support.py` and
`knowledge_writer_test_support.py`. These are the rows the census derives the module consumes: it imports
the two support modules, and the census's source derivation assigns it the lock file, as for the other
text-knowledge case modules in that row. This is the follow-up L24 recorded in the section above.

- **Insertion-only (+3/−0).** No row was added or removed, no consumer removed and no other field changed.
- **Populations:** 16 contracts and 80 artifacts, both unchanged. The pin in
  `test_dependency_ownership_ast_helpers.py` moves from `6fb4934d…` to `b96198c3…` (the Thirty-fourth).

- The three consumer additions, one on each exact row. [73]
- The three rows they belong to. [74]

## 260928-MIK-L08 One Consumer On One Exact Row, Counts 16 / 80

`260928-MIK-L08` (MIK-R08, the change-to-knowledge worklist) appends its new case module
`mcp/tests/test_knowledge_worklist_leaf.py` to the `consumer_scope = "exact"` consumer list of
`fixtures/repository_profiles/node/package-lock.json`, after L28's `test_knowledge_proofs.py` and without
re-sorting. The census derives it because the module drives the memory-quality controller. The other new
case module, `test_knowledge_worklist.py`, consumes no catalogued artifact and needs no row.

- **Insertion-only (+1/−0).** No row was added or removed, no consumer removed and no other field changed.
- **Populations:** 16 contracts and 80 artifacts, both unchanged. The pin in
  `test_dependency_ownership_ast_helpers.py` moves from `b96198c3…` to `11ce8089…` (the Thirty-fifth).

- The consumer addition. [75]
- The row it belongs to. [76]


## 260928-MIK-L03 One Consumer On One Exact Row, Counts 16 / 80

`260928-MIK-L03` (MIK-R03, stale invariants flagged at read time) appends its new case module
`mcp/tests/test_knowledge_currentness.py` to the `consumer_scope = "exact"` consumer list of
`fixtures/repository_profiles/node/package-lock.json`, after L08's `test_knowledge_worklist_leaf.py` and
without re-sorting. The census derives it as a transitive consumer (the worker's integration-lane run found
it).

- **Insertion-only (+1/−0).** No row was added or removed, no consumer removed and no other field changed;
  the file is now 2,085 lines.
- **Populations:** 16 contracts and 80 artifacts, both unchanged. The pin in
  `test_dependency_ownership_ast_helpers.py` moves from `11ce8089…` to `dcc1ab1d…` (the Thirty-sixth).

- The consumer addition. [77]
- The row it belongs to. [78]

## 260928-MIK-L02 One Consumer On Two Exact Rows, Counts 16 / 80

`260928-MIK-L02` (MIK-R02, bounded continuation accepted by the mounted read) appends its new case module
`mcp/tests/test_knowledge_paging.py` to two `consumer_scope = "exact"` consumer lists, each after its last
consumer and without re-sorting: `fixtures/repository_profiles/node/package-lock.json` (after L03's
`test_knowledge_currentness.py`) and `knowledge_index_test_support.py` (after `test_knowledge_proofs.py`).
The census derives the module as a transitive consumer of both (it imports the index test support).

- **Insertion-only (+2/−0).** No row was added or removed, no consumer removed and no other field changed;
  the file is now 2,087 lines.
- **Populations:** 16 contracts and 80 artifacts, both unchanged. The pin in
  `test_dependency_ownership_ast_helpers.py` moves from `dcc1ab1d…` (L03's Thirty-sixth) to `5c0a1594…`
  (the Thirty-seventh), re-measured by the architect at the sync onto `a4eba7b7`.

- The paging module's consumer line on the package-lock row. [79]
- The paging module's consumer line on the index-support row. [80]
- The index-support row that gains it. [81]

## 260928-MIK-L11 One Consumer On One Exact Row, Counts 16 / 80

`260928-MIK-L11` (MIK-R11, planned invariant effects reconciliation) appends its new case module
`mcp/tests/test_planned_knowledge_effects.py` to the `consumer_scope = "exact"` consumer list of
`fixtures/repository_profiles/node/package-lock.json`, after L02's `test_knowledge_paging.py` and without
re-sorting. The census derives it as a transitive consumer (it builds on MIK-R08's worklist world); the
worker's first integration-lane run found it.

- **Insertion-only (+1/−0).** No row was added or removed, no consumer removed and no other field changed;
  the file is now 2,088 lines.
- **Populations:** 16 contracts and 80 artifacts, both unchanged. The pin in
  `test_dependency_ownership_ast_helpers.py` moves from `5c0a1594…` (L02's Thirty-seventh) to `cb853f72…`
  (the Thirty-eighth), measured on the tree synced onto `2c6f170e` (architect ruling
  2026-09-29T22:35:34+02:00).

- The planned-effects module's consumer line. [82]
- The row it belongs to. [83]

## 260928-MIK-L01 One Consumer On Two Exact Rows, Counts 16 / 80

`260928-MIK-L01` (MIK-R01, family-complete leaf read) appends its new case module
`mcp/tests/test_knowledge_leaf_read.py` to two `consumer_scope = "exact"` consumer lists, each after its last
consumer and without re-sorting: `fixtures/repository_profiles/node/package-lock.json` (after L11's
`test_planned_knowledge_effects.py`) and `knowledge_index_test_support.py` (after L02's
`test_knowledge_paging.py`). The census derives the module as a transitive consumer of both (it imports the
index test support). The worker first wrote it after `test_knowledge_paging.py` in both rows; at the sync
onto L11 (`46ca7430`) the package-lock line was kept after L11's, as review R1 N8 asked.

- **Insertion-only (+2/−0).** No row was added or removed, no consumer removed and no other field changed;
  the file is now 2,090 lines.
- **Populations:** 16 contracts and 80 artifacts, both unchanged. The pin in
  `test_dependency_ownership_ast_helpers.py` moves from `cb853f72…` (L11's Thirty-eighth) to `a571a70f…`
  (the Thirty-ninth), measured on the synced tree (architect ruling 2026-09-30 00:08:39).

- The leaf-read module's consumer line on the package-lock row. [84]
- The leaf-read module's consumer line on the index-support row. [85]
- The two rows it belongs to. [86]

## 260928-MIK-L10 One Consumer On One Exact Row, Counts 16 / 80

`260928-MIK-L10` (MIK-R10, unexplained change disposition) appends its new case module
`mcp/tests/test_unexplained_change_disposition.py` to one `consumer_scope = "exact"` consumer list,
`fixtures/repository_profiles/node/package-lock.json`, after L01's `test_knowledge_leaf_read.py` and without
re-sorting. The census derives the module as a transitive consumer of the fixture (it reuses MIK-R08's worklist
world). At the sync onto L01 (`3772cdcd`) the two catalog files were the only conflict, and this leaf's line was
kept after L01's.

- **Insertion-only (+1/−0).** No row was added or removed, no consumer removed and no other field changed;
  the file is now 2,091 lines.
- **Populations:** 16 contracts and 80 artifacts, both unchanged. The pin in
  `test_dependency_ownership_ast_helpers.py` moves from `a571a70f…` (L01's Thirty-ninth) to `449b69ef…`
  (the Fortieth), measured on the synced tree and unchanged by the later sync onto L25 (`8a2d4b47`).

- The unexplained-change module's consumer line on the package-lock row. [87]
- The row it belongs to. [88]

## 260928-MIK-L05 One Consumer On Four Exact Rows, Counts 16 / 80

`260928-MIK-L05` (MIK-R05, route-chain family retrieval) appends its new case module
`mcp/tests/test_knowledge_route_chain.py` to four `consumer_scope = "exact"` consumer lists, each after its
last consumer and without re-sorting: `curator_coherence_test_support.py` (after
`test_knowledge_conversion_toolchain.py`), `fixtures/repository_profiles/node/package-lock.json` (after L10's
`test_unexplained_change_disposition.py`), `read_scope_test_support.py` (after
`test_knowledge_conversion_toolchain.py`) and `knowledge_index_test_support.py` (after L01's
`test_knowledge_leaf_read.py`). The census derives the module as a transitive consumer of all four: it
imports the leaf-read case module (the index support and the package-lock fixture) and the `read_ar_files`
case module (the read-scope and curator-coherence supports), as `test_knowledge_conversion_toolchain.py`
already does. The package-lock row was the textual conflict with L10 that review R1 F5 named; the ruling of
2026-09-30 04:12:49 kept both lines, and the architect's sync onto `31d761a2` placed this leaf's after L10's.

- **Insertion-only (+4/−0).** No row was added or removed, no consumer removed and no other field changed;
  the file is now 2,095 lines.
- **Populations:** 16 contracts and 80 artifacts, both unchanged. The pin in
  `test_dependency_ownership_ast_helpers.py` moves from `449b69ef…` (L10's Fortieth) to `f8b04814…` (the
  Forty-first), measured on the synced tree.

- The route-chain module's consumer lines on the four rows. [89]
- The four rows it belongs to. [90]

## 260928-MIK-L14 One Consumer On One Exact Row, Counts 16 / 80

`260928-MIK-L14` (MIK-R14, reconsideration surfacing) appends its new case module
`mcp/tests/test_reconsideration_surfacing.py` to one `consumer_scope = "exact"` consumer list,
`fixtures/repository_profiles/node/package-lock.json`, after L05's `test_knowledge_route_chain.py` and without
re-sorting. The census derives the module as a transitive consumer of the fixture (it reuses MIK-R08's worklist
world, `test_knowledge_worklist.World`). The first integration run failed exactly on the missing consumer (worker
report); the line was added, and at the syncs onto L10 (`31d761a2`) and L05 (`48f680d5`) the ordinal was renumbered
from a provisional Forty-first to the final Forty-second and re-measured.

- **Insertion-only (+1/−0).** No row was added or removed, no consumer removed and no other field changed;
  the file is now 2,096 lines.
- **Populations:** 16 contracts and 80 artifacts, both unchanged. The pin in
  `test_dependency_ownership_ast_helpers.py` moves from `f8b04814…` (L05's Forty-first) to `4477446e…` (the
  Forty-second), measured on the tree synced onto `48f680d5` and unchanged by the sync onto L31 (`b54d1b03`); the
  curator re-measured it with `sha256sum` on the candidate.

- The reconsideration module's consumer line on the package-lock row. [91]
- The row it belongs to. [92]
