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

## 260928-MIK-L101 — rule 6 budget registry and test

The `test_role_capsule_budgets.py` module joined the Node lockfile fixture's consumer list (fixture `mcp/tests/fixtures/repository_profiles/node/package-lock.json`, consumer entry at evidence-lifecycle.toml:1355) alongside the unit-regression lane (test-evidence-lanes.toml:254); no artifact or contract row changes, and the canonical form is unchanged. The rule 6 budget registry itself is a producer-side contract and makes no consumer-list claim.

## Shared Causal Test Helpers

The conversation-open, Eve event-pump and reviewer-worklist-process supports are permanent,
internal hand-authored artifacts. Each has an existing behavior-test owner, an exact executable
replacement contract, fidelity/cadence and source-derived consumers. They own explicit resolution,
stream completion or subprocess opportunities; cases and product assertions remain with their test
modules. Consumer-list changes follow actual source relations, including new cache/scanner tests
and the state suite's real conftest import. These declarations do not prove a test executed.

## 260928-MIK-L114 River-Test Registration And Catalog Rewrite

The `unit-regression` lane registers the river tests (`test_f07_missing_lock_cursor.py`,
`test_f08_registered_handler_river.py`, `test_tool_event_river.py`) in canonical byte
order. The lifecycle catalog is rewritten in canonical form around them: merge-doubled
contract rows dropped to one copy each, the `knowledge-generation-cases` pair resolved to
the branch copy whose evidence node file is present, and rows whose owner and evidence
files are both gone removed without file restores.

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

## Current catalog registration

At the landed L71 checkpoint, the catalog holds 13 contract rows and 87 governed artifacts. The shared `preview_read_only_test_support.py` artifact declares the registered-preview call-record comparison as permanent local-composition evidence, with the existing repeatable-preview test as its replacement contract. Its exact consumers are `test_worktree_start_preview.py` and `test_master_retirement_readiness.py`: the latter reaches the support transitively through the preview fixture. That consumer addition leaves the row's metadata, existing direct consumer and every other catalog row unchanged. Artifact and consumer declarations establish ownership and reachability, not test execution or acceptance. This landed population is not a count of the separately composed L74 working catalog.

- The registered-preview comparator's artifact row retains its replacement contract and lists both direct and transitive consumers. [260]
The admitted lifecycle replacement, landed upstream of L74, replaced the earlier 32-contract catalog with 13 contracts; `tool_log_witness` predates L74 and the river-scale measurement (`l114_e4_river_scale.py`) is also carried upstream content. Earlier per-leaf artifact counts are historical, not the current composed population. L74's rule-test consumers and the landed preview consumers are both retained; the working catalog's final row population must be read from the completed composition, not inferred from either historical count.

## 260928-MIK-L74 The derived index sheds the dataset shape

L74 rebinds the `knowledge-identity-branching-fixture` contract and its four artifact references to `test_three_separately_recorded_revisions_stay_independently_addressable`. Its `knowledge_row_codec_test_support.py` consumer reconciliation is source-derived: the prior L74 comparison removed three unsupported consumers and measured 20 declared against 20 derived; this is a dated comparison, not a constant for the later composed consumer set. L74 also adds the permanent `read_boundary_oracle_test_support.py` artifact, shared by the boundary, controls and roster cases, with the existing unauthorized-object control as its replacement contract. The earlier no-artifact-addition claim is superseded by that explicit registration. These declarations do not show that the cases ran or that the read boundary is accepted.

## 260928-MIK-L96 The host test modules

`evidence-lifecycle.toml` gained revised durable-artifact consumer sets/paths for the new host test modules (`test_paseo_install_contract`, `test_paseo_install_no_stop`, `test_paseo_node`, `test_paseo_start`, `test_dashboard_host`, `test_host_release_contract`, `test_paseo_host_environment`) and for the moved host modules. This file holds artifact consumers plus the executable `replacement_contract`/`consumers` records; it declares no lane tables and no knowledge-invariant identities. Lane membership for the host modules lives in `test-evidence-lanes.toml`, and knowledge proof identities live in the sidecar proof plane; a catalog declaration still never shows evidence ran.



| Conversation-open support (`mcp/tests/conversation_open_test_support.py`) declares its permanent owner and real replacement contract. [258] |  | mcp/tests/evidence-lifecycle.toml |
| Eve event support (`mcp/tests/eve_adapter_event_test_support.py`) declares its permanent owner and exact consumers. [259] |  | mcp/tests/evidence-lifecycle.toml |

## 260928-MIK-L129 Repeated-cleanup regression test consumers

`mcp/tests/test_cleanup_repeated_archive_ready.py` joins the three consumer lists the source tree supports (two lifecycle `consumers` lists and one exact-scope artifact's `consumers` list) through the documented `--write` command, and joins the `integration` lane. No artifact or contract row is added, removed or reordered by hand, and the canonical form is unchanged.

## Refreshed current evidence

- Worklist process support declares its permanent local-composition contract. [98]
### Conventions

The catalog is a policy/configuration input and is not counted as an artifact inside itself.
Fidelity, lifetime, and test grouping answer different questions. Current source declarations
supersede historical per-leaf consumer positions and population counts retained below.
### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.
### Invariants And Boundaries

- Replacement node references must name the retained real test definition.
- Exact consumer declarations must correspond to actual support use; stale counts are not authority.
- A `[[artifact]]` row's path must be discoverable by `governed_artifact_paths`, which is a different
  question from whether the module exists and is imported.
- Registry consistency and permanent-support rationale do not claim execution or certification.
- Ledger retirement changes the closeout replacement node, not unrelated artifact ownership.
- **A consumer row is a catalog change.** Adding an importer to a `consumers` list moves the file's
  bytes; `test_dependency_ownership_ast_helpers.py` computes every property from the catalog — no byte,
  row count or file count is written down there, so adding a test file never edits that module.
- **Consumer rows are accounting, never acceptance.** A row states that a test module reaches a
  support artifact; it does not claim the artifact's fidelity, that a test ran, or that a boundary was
  exercised in production.
### Repo-Internal References

These repository-relative targets and exact ranges were checked against the current working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

- The schema version and the large-fixture discovery threshold remain explicit.
- The four retained knowledge contracts and their evidence nodes.
- Closeout fixture support names the retained code/memory transaction replacement.
- Closeout-input support declares the cleanup-guidance consumer.
- None
- None
- None
- None
- The referenced transaction test definition exists in the current source.
- None
- Closeout-input support names the same retained code/memory transaction replacement node.
- None
- None
- The referenced transaction test definition exists in the current source.

- The schema version and the large-fixture discovery threshold remain explicit. [212]
- The four retained knowledge contracts and their evidence nodes. [213]
- The referenced transaction test definition exists in the current source. [214]
- The referenced transaction test definition exists in the current source. [215]
- The artifact the first pair belongs to, and the scope both lists carry. [216]
- The fixture module it builds on rather than duplicating, so no third enclosure fixture was introduced. [217]
- **The row registered for the member-source cases, at the end of the read-scope artifact's exact consumer list.** [218]
- **The fixture it extends rather than duplicating, and the observation helper its cases read bytes back through.** [219]
- **The three consumer entries on the diff-cases artifact's exact list, appended newest-last.** [220]
- **The same three on the read-scope artifact's exact list.** [221]
- The enclosure the three modules extend rather than duplicating. [222]
- The read-scope artifact's consumer list with the new exact consumer. [223]
- The nine new fixture rows for the Doc14 knowledge-file examples. [224]
- The consumer additions: the conversion toolchain case on the curator-coherence and read-scope rows, the crossing case on the merge-case and generation rows. [225]
- The three consumer additions, one on each exact row. [226]
- The three rows they belong to. [227]
- The consumer addition. [228]
- The row it belongs to. [229]
- The consumer addition. [230]
- The row it belongs to. [231]
- The paging module's consumer line on the package-lock row. [232]
- None [233]
- The planned-effects module's consumer line. [234]
- The row it belongs to. [235]
- The leaf-read module's consumer line on the package-lock row. [236]
- None [237]
- The two rows it belongs to. [238]
- The unexplained-change module's consumer line on the package-lock row. [239]
- The row it belongs to. [240]
- The route-chain module's consumer lines on the four rows. [241]
- The reconsideration module's consumer line on the package-lock row. [242]
- The row it belongs to. [243]

- The schema version and the large-fixture discovery threshold remain explicit. [244]
- The four retained knowledge contracts and their evidence nodes. [245]
- Closeout fixture support names the retained code/memory transaction replacement. [246]
- Closeout-input support declares the cleanup-guidance consumer. [247]
- None [248]
- None [249]
- None [250]
- None [251]
- The referenced transaction test definition exists in the current source. [252]
- None [253]
- Closeout-input support names the same retained code/memory transaction replacement node. [254]
- None [255]
- None [256]
- The referenced transaction test definition exists in the current source. [257]
The converted-drift test module joins the consumer lists it exercises with: one test per packet rule,
each behavioural case failing before its fix and passing after.
- The converted-drift module is registered as a consumer of the evidence it exercises. [99]
- The durable-artifact consumer entries this catalog now declares; lane rows belong to test-evidence-lanes.toml. [14]
- The two reviewer worklist test modules on that row's consumer list. [95]

The converted-drift registration once tabled under keys 14/95 now stands as the [99] line above; keys 14 and 95 cite the catalog's durable-artifact and reviewer-worklist rows.
