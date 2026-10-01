# mcp/tests/test_capsule_serving.py

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

## Evidence

### Docs References

The exchange cases are conformance evidence for the MCP skills extension. Its operative facts for a
reader of this module: the extension introduces **three protocol methods**; `skills/list` and
`skills/get` are mandatory for any server declaring it; and enumeration is a method, not an index
resource.

- The extension identifier and the two method names the protocol cases exercise. [1]
- The SEP entry shape the entry cases assert. [2]

Canonical live reference: <https://github.com/modelcontextprotocol/modelcontextprotocol> (the skills
extension specification, SEP-2640).

### Repo-Internal References

- The fixture world and the synthetic corpus (including its nested skill) every hermetic case is built from. [3]
- The admission guarantees: no role acquisition by string, no caller-selected source, no write to the read tree. [4]
- Altitude admission is pinned across every role the document can carry, so a hardcoded role fails. [5]
- The re-read and the refusal are separate, correctly-named behaviours. [6]
- The guards that round 1 found unpinned, each now driven directly by its own case. [7]
- The SEP entry contract and this server's own index shape, asserted separately. [8]
- Nesting is published flat like any other skill. [9]
- The serving guarantees: origin and revision kept, revision re-checked, no grant, no body in the listing. [10]
- The two real-process conformance cases: the exchange (capabilities, both methods, resources, refusal) and the traversal refusal. [11]
- The case that keeps the seeded-mutation evidence honest. [12]
- The evidence-lane row this module is selected by. [13]

### Cross-Repo References

No meaningful cross-repository reference applies.
