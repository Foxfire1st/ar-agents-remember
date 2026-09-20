# mcp/tests/test_capsule_serving.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_capsule_serving.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T12:20+02:00 |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c` |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

The selected cases for the capsule operation and the SEP-2640 skill surface: **30 collected items**,
**28 in the unit population and 2 marked `integration`** (the two real client/server exchanges), in a
1,535-line module. It is registered in `mcp/tests/test-evidence-lanes.toml` under `unit-regression`.

The module's assertions compare against an expected side that is the fixture's own bytes, a frozen
vocabulary, or a second server instance — never against a value the code under test produced for
itself. That rule is the one two repair rounds sharpened: the round-1 review found cases that derived
their expectation from the same artifact they were checking and cases whose names claimed failures
they did not assert, and the current module replaces them (see "Repair history" below). It also still
carries `test_the_mutation_harness_can_actually_fail`, which keeps the mutation evidence honest.

## Code Commentary

### Logic

- `World` (line 419) is the fixture: a disposable coordination root with a contract plus leaf and
  master task documents, and a synthetic skills corpus. `_synthetic_corpus` (line 308) writes a corpus
  whose bytes the cases can predict — including a nested skill — and `_contract_text` (line 181),
  `_leaf_document` (line 241), `_master_document` (line 259) and `_sprint_document` (line 279) build the
  admitted side.
- The **capsule admission** cases assert routed blocks carry the fixture's own bytes
  (`test_the_capsule_carries_routed_blocks_with_the_bytes_this_fixture_wrote`), that the operation
  writes nothing to the tree it reads, that changing the role string cannot acquire another role, that
  an unknown role gets its own status, that a task path escaping the task root is refused, that the
  manifest decides the source set rather than the caller, and that a moved task document is **read
  again** with the capsule carrying the new digest
  (`test_a_moved_task_document_is_read_again_and_the_capsule_carries_the_new_digest`) while a recorded
  admission whose bytes moved is refused
  (`test_a_recorded_admission_whose_bytes_moved_is_refused`). Two further cases pin altitude admission
  across **every** role the document can carry, so an implementation that hardcoded one role fails
  (`test_altitude_admission_admits_every_role_the_document_can_carry_and_refuses_the_rest`,
  `test_the_capsule_operation_serves_every_seat_its_document_can_carry`).
- The **skill serving** cases assert a served skill keeps its origin and revision, that a read refuses
  a body whose bytes changed since the catalog, that reading a skill grants none of the tools its
  frontmatter names, that a resource read leaves the tool surface and response registry unchanged, that
  same-named skills from two servers stay distinct, that the discovery registry is not the
  model-visible catalog, that a skill body is not composed into the instruction stream, and that a
  non-conforming skill directory is recorded rather than served.
- The **entry-shape and guard** cases are the ones the repairs added or sharpened:
  `test_every_sep_2640_entry_is_complete_and_carries_verbatim_frontmatter` (the SEP entry contract),
  `test_this_servers_own_index_resource_keeps_the_agent_skills_discovery_shape` (this server's own
  index is the Agent Skills shape and is *not* the enumeration surface),
  `test_a_catalog_record_that_escapes_its_skill_directory_is_refused` (drives the containment guard
  **directly**, rather than relying on an earlier lookup refusal),
  `test_the_index_reader_refuses_while_a_skill_cannot_be_served` (the `require_servable` gate on the
  index loader), `test_a_skill_whose_directory_name_disagrees_with_its_name_is_recorded_not_served`
  (the declared-name == final-path-segment rule),
  `test_the_extension_declaration_is_installed_once_per_server` (the install-once idempotence guard),
  and `test_a_nested_skill_is_published_flat_like_any_other` (nesting with flat publication).
- Three cases run against the **shipped corpus** rather than the synthetic one: the corpus parses and
  every served skill has a root revision, the composition manifest declares the skill that is served,
  and the index document has the expected shape. These are the cases that would catch a packaging drift
  between the canonical root `skills/` tree and the served copy.
- The two `integration` cases (lines 1195 and 1268) start the real entry point as its own process
  (`python -m agents_remember.mcp --config <tmp>/mcp-settings.json` with `PYTHONPATH` pointing at the
  worktree source) and drive it with the **installed SDK's own client** (`mcp.client.stdio` +
  `ClientSession`) — an implementation independent of the server code under test. The exchange case
  observes the negotiated capabilities, the resource list, the index, a selected body, a supporting
  file, a refusal, **and both extension methods** — `skills/list` plus `skills/get`, with `skills/get`
  on an absent URI refused `-32602`. The other attempts a traversal path from the live process and
  requires the read to be refused.

### Conventions

Cases are top-level functions with a `world` fixture rather than classes, and their names state the
guarantee rather than the mechanism. Only the two cases that need a live exchange carry
`@pytest.mark.integration`; everything else is unit-population. Method-name literals used by the
protocol cases are declared as module constants (`SKILLS_LIST_METHOD`, `SKILLS_GET_METHOD`) so a case
names the method rather than spelling it.

### Invariants And Boundaries

- **An expectation must not come from the artifact under test.** Two round-1 cases compared the index
  document against the same catalog's own entries and imported the extension id and index URI from the
  module under test; those are the shape the current module moved away from, and it is why the guard
  cases now drive their target directly instead of asserting from a neighbouring surface.
- **A case named for a failure must assert that failure.** Round 1 found a case asserting `stale.ok`
  under a name claiming a refusal; the current module separates the two behaviours into
  `…read_again…carries_the_new_digest` and `…bytes_moved_is_refused`.
- **The two integration cases are the only ones that need a real process** and are not to be
  multiplied: the repository's case-budget policy keeps the integration population small rather than
  moving unit bloat into it.
- The shipped-corpus cases assert a **root revision exists per skill**, not a hard-coded digest: the
  served copy is generated, so a pinned digest would fail on every legitimate sync.
- The corpus override on the payload builders is what lets the synthetic cases run without touching the
  shipped tree; it is deliberately not on the registered tool signatures.

### Todos

None recorded. One owner-level finding is recorded against this module's **cost** rather than its
correctness: the default unit selection collects more cases than its declared ceiling allows, of which
this module's 28 unit items are one contribution. The ceiling was not edited here and the module was
not moved to another lane to dodge the check. See the leaf's worker report `F-L4-01`.

## Repair history (why this module looks different from its round-1 form)

Round 1's baseline review seeded five further removals of required behaviour and found four surviving
all 21 of the then-current cases — the containment guard, the `require_servable` gate on the index
loader, the declared-name rule, and the extension-declaration idempotence guard — beside two cases
mislabelled or self-derived, one case pinning the non-SEP index shape under a SEP-2640 name, and the
extension constants imported from the module under test. The repairs added one case per unpinned
behaviour, corrected the mislabels, retargeted the index case to what it actually pins, and took the
extension id and index URI as fixture literals. The module grew 21 → 30 items across the two rounds;
the two `integration` cases and the mutation-harness self-check are unchanged in intent.

## Docs References

The exchange cases are conformance evidence for the MCP skills extension. Its operative facts for a
reader of this module: the extension introduces **three protocol methods**; `skills/list` and
`skills/get` are mandatory for any server declaring it; and enumeration is a method, not an index
resource.

| Finding | Anchor | Source |
| --- | --- | --- |
| The extension identifier and the two method names the protocol cases exercise. | `SKILLS_EXTENSION_ID`; `SKILLS_LIST_METHOD`; `SKILLS_GET_METHOD` | mcp/src/agents_remember/models/skill_resources.py:31-32; mcp/src/agents_remember/mcp/registration/skills_extension.py:69-70 |
| The SEP entry shape the entry cases assert. | `entry_document` | mcp/src/agents_remember/models/skill_resources.py:115-130 |

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture world and the synthetic corpus (including its nested skill) every hermetic case is built from. | `World`; `_synthetic_corpus` | mcp/tests/test_capsule_serving.py:308-308; mcp/tests/test_capsule_serving.py:419-419; mcp/tests/test_capsule_serving.py:423-551 |
| The admission guarantees: no role acquisition by string, no caller-selected source, no write to the read tree. | `test_a_caller_changing_the_role_string_cannot_acquire_another_role`; `test_the_manifest_decides_the_source_set_not_the_caller`; `test_the_capsule_operation_writes_nothing_to_the_tree_it_reads` | mcp/tests/test_capsule_serving.py:639-639; mcp/tests/test_capsule_serving.py:651-651; mcp/tests/test_capsule_serving.py:690-690; mcp/tests/test_capsule_serving.py:655-673; mcp/tests/test_capsule_serving.py:694-706; mcp/tests/test_capsule_serving.py:643-652 |
| Altitude admission is pinned across every role the document can carry, so a hardcoded role fails. | `test_altitude_admission_admits_every_role_the_document_can_carry_and_refuses_the_rest` | mcp/tests/test_capsule_serving.py:1410-1450 |
| The re-read and the refusal are separate, correctly-named behaviours. | `test_a_moved_task_document_is_read_again_and_the_capsule_carries_the_new_digest`; `test_a_recorded_admission_whose_bytes_moved_is_refused` | mcp/tests/test_capsule_serving.py:705-705; mcp/tests/test_capsule_serving.py:737-737; mcp/tests/test_capsule_serving.py:709-738; mcp/tests/test_capsule_serving.py:741-779 |
| The guards that round 1 found unpinned, each now driven directly by its own case. | `test_a_catalog_record_that_escapes_its_skill_directory_is_refused`; `test_the_index_reader_refuses_while_a_skill_cannot_be_served`; `test_a_skill_whose_directory_name_disagrees_with_its_name_is_recorded_not_served`; `test_the_extension_declaration_is_installed_once_per_server` | mcp/tests/test_capsule_serving.py:1321-1321; mcp/tests/test_capsule_serving.py:1348-1348; mcp/tests/test_capsule_serving.py:1366-1366; mcp/tests/test_capsule_serving.py:1389-1389; mcp/tests/test_capsule_serving.py:1325-1349; mcp/tests/test_capsule_serving.py:1352-1367; mcp/tests/test_capsule_serving.py:1370-1390; mcp/tests/test_capsule_serving.py:1393-1407 |
| The SEP entry contract and this server's own index shape, asserted separately. | `test_every_sep_2640_entry_is_complete_and_carries_verbatim_frontmatter`; `test_this_servers_own_index_resource_keeps_the_agent_skills_discovery_shape` | mcp/tests/test_capsule_serving.py:1008-1008; mcp/tests/test_capsule_serving.py:1040-1040; mcp/tests/test_capsule_serving.py:1044-1075; mcp/tests/test_capsule_serving.py:1012-1041 |
| Nesting is published flat like any other skill. | `test_a_nested_skill_is_published_flat_like_any_other` | mcp/tests/test_capsule_serving.py:1496-1542 |
| The serving guarantees: origin and revision kept, revision re-checked, no grant, no body in the listing. | `test_a_served_skill_keeps_its_origin_and_revision`; `test_a_read_refuses_a_body_whose_bytes_changed_since_the_catalog`; `test_reading_a_skill_does_not_grant_the_tools_its_frontmatter_names`; `test_the_discovery_registry_is_not_the_model_visible_catalog` | mcp/tests/test_capsule_serving.py:783-783; mcp/tests/test_capsule_serving.py:796-796; mcp/tests/test_capsule_serving.py:811-811; mcp/tests/test_capsule_serving.py:882-882; mcp/tests/test_capsule_serving.py:787-797; mcp/tests/test_capsule_serving.py:800-812; mcp/tests/test_capsule_serving.py:815-849; mcp/tests/test_capsule_serving.py:886-912 |
| The two real-process conformance cases: the exchange (capabilities, both methods, resources, refusal) and the traversal refusal. | `test_a_real_client_and_server_exchange_over_the_installed_sdk`; `test_the_server_process_never_serves_a_file_outside_a_skill_directory` | mcp/tests/test_capsule_serving.py:1195-1195; mcp/tests/test_capsule_serving.py:1268-1268; mcp/tests/test_capsule_serving.py:1198-1268; mcp/tests/test_capsule_serving.py:1271-1302 |
| The case that keeps the seeded-mutation evidence honest. | `test_the_mutation_harness_can_actually_fail` | mcp/tests/test_capsule_serving.py:1305-1317 |
| The evidence-lane row this module is selected by. | "mcp/tests/test_capsule_serving.py" | mcp/tests/test-evidence-lanes.toml:23-23 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_capsule_serving.py" repointed to mcp/tests/test-evidence-lanes.toml:24-24. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_capsule_serving.py" repointed to mcp/tests/test-evidence-lanes.toml:23-23. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_altitude_admission_admits_every_role_the_document_can_carry_and_refuses_the_rest` repointed to mcp/tests/test_capsule_serving.py:1410-1450. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_a_nested_skill_is_published_flat_like_any_other` repointed to mcp/tests/test_capsule_serving.py:1496-1542. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_the_mutation_harness_can_actually_fail` repointed to mcp/tests/test_capsule_serving.py:1305-1317. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_capsule_serving.py" repointed to mcp/tests/test-evidence-lanes.toml:21-21. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass**: rewrote this card against the
  settled candidate. **Removed the round-1 rejection banner** and replaced it with a "Repair history"
  section recording *what the repairs fixed* rather than a warning against citing the module. Corrected
  the population from 21 to **30 collected items (28 unit + 2 integration)** in a 1,535-line module,
  re-derived every fixture and case line number, and documented the cases the rounds added: the SEP
  entry contract, this server's own index shape (asserted separately from the enumeration surface), the
  four previously-unpinned guards each driven by its own case, altitude admission across every role the
  document can carry, the split of the old mislabelled case into a re-read case and a refusal case, and
  nested-skill flat publication. Recorded that the exchange case now exercises **both extension
  methods** including the `-32602` refusal on an absent URI, and that the protocol cases take the method
  names as constants rather than importing them from the module under test. Verification metadata
  remains closeout-owned; no acceptance claim is made.

- 2026-09-16T11:50+02:00 — 260915-CAPS-L4 curator, post-verdict correction (superseded): added the
  round-1 coverage banner listing the four seeds that survived all 21 cases and the mislabelled cases
  (`F-L4-07`, `F-L4-08`). Those defects were repaired in the following rounds, so the banner is replaced
  above by the repair history.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator: created the card for the new test module.
  Recorded the 21-item population split (19 unit, 2 integration), the fixture-own-bytes assertion rule,
  the two independent-SDK-client conformance cases and what they observe, the three shipped-corpus cases
  that would catch packaging drift, and the open owner-level case-budget finding this module's cost
  contributes to without owning.
