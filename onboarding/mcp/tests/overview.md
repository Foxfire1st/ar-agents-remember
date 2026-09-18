# mcp/tests

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/tests/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-18T10:48+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l13` uncommitted staged source; base `f031314345b674d0733c4619fe34d78c1b02ba26` |
| governingOverview | `../overview.md` |

## 260915-CAPS-L9 Experiment-Installation Test Population

`mcp/tests/test_capsule_experiment_install.py` is **new** in this leaf: **19 cases** driving the real
installer entry points against scratch coordination roots, and reading the resulting tree, the
returned run record and the compiled capsule text. It is **not** a seventh `D9` module — the
fail-closed lane loader still names exactly the same six at this tip as at the clean base — and its
manifest row plus its two `evidence-lifecycle.toml` consumer rows are the whole catalog delta this
leaf contributes.

What the population is for, stated so the route is not read as more than it is: the cutover pair with
the disabled run as its positive control and the removal half; the documented way back executed as a
run; the selection surface (request-then-environment precedence and `selectionSource`) driven through
the **registered payload builder**; fail-closed refusals that name the capability **and** create no
coordination root; three separately-labelled screens (received startup material on disk, the
delivered capsule from the production compile route, and the installed root's corpus read as authored
source); the run record compared against the pinned `package.json`; the rendered rollback rows; the
install's confinement to its destination; and the **no-persistence guard**, which content-digests
every regular file under the coordination root before and after the selected run and demands that
every hit be a byte-identical authored asset — the root-scoped reading that replaced a first revision
whose `rglob("*.json")` guard was blind to a `.toml`, a `.txt` or an extension-less switch.

`test_sync_runtime.py` gained two cases (two methods → four): the per-target ignore rule and the
refusal to report an absent canonical source in sync.

## Governing Overview

[MCP package overview](../overview.md)

## 260915-CAPS-L15 Launch-Wiring Test Population

One new module, `mcp/tests/test_capsule_launch_wiring.py`, **14 cases**, and it is the acceptance test
this master lacked: every earlier capsule case hand-supplied the intermediate value, so none of them
could have failed if no production launch point supplied a capsule at all. This module drives the
production path and reads the artifact from the **consumer's own side**.

| Case group | What it pins |
| --- | --- |
| the acceptance pair | a task-attached seat through the spawn primitive, and a free agent (`bootstrap`, no task document) through the dashboard route — the runner argv the launch point itself built is parsed back out of the base64 the child would exec, the real runner preparation and adapter factory run, and the capsule is read from the session's own `thread/start`, compared against the compiler's own result |
| the production-chain pair (fix round 1) | the route's own `TerminalSessionSpec` (cwd **and** env) fed to `parse_runner_config` → `_prepare_controlled_launch` → `launch_spec_binding` → `verify_capsule_binding`, and the spawn side's agreement with its own capsule — **replacing a deleted hand-supplied case** (`L15R-2`'s evidence class) |
| the mode gate and the refusals | every seat class's answer, and an un-compilable role refusing by name with `host.ensured == []` |
| behaviour 6 | the capsule-free payload byte-identical to the pre-capsule one |
| the payload bound (`D12`) | exactly one `trustedInstructions` key, and no task context in argv |
| the enumeration guard | every `TerminalLaunchRequest(` site is wired or declares its legacy chain, and the site **set** cannot change silently |
| `D13` / `D20` | the registered operation resolves a repository through its declared schema; a first refusing stage refuses again in the same process |
| the free agent's admission | the named absence, and an identity that moves with the seat |

Its lane row is `unit-regression` (`mcp/tests/test-evidence-lanes.toml:19`) — the cases run in process
with the vendor boundary recorded and the tmux host doubled — and it made three governed artifacts gain
a consumer row, which is why `evidence-lifecycle.toml`'s byte pin moved at this leaf's tip without any
population changing. **The live system-block half of the evidence is not here**: it is
`notes/reports/260915-CAPS-L15-evidence/E8-fix-r1-production-chain.txt`, which starts a real eve runtime
from the production chain's own captured cwd and env.

| Finding | Anchor | Source |
| --- | --- | --- |
| The acceptance pair, read out of each started session's own first prompt. | `test_a_task_attached_seat_reads_its_compiled_capsule_out_of_its_own_first_prompt`; `test_a_free_agent_reads_its_compiled_capsule_out_of_its_own_first_prompt` | mcp/tests/test_capsule_launch_wiring.py:483-526; mcp/tests/test_capsule_launch_wiring.py:529-574 |
| The production-chain pair that replaced the hand-supplied case. | `test_a_production_eve_launch_runs_where_its_capsule_admits_and_the_consumer_accepts`; `test_the_spawn_launch_agrees_with_its_capsule_about_the_workspace` | mcp/tests/test_capsule_launch_wiring.py:816-872; mcp/tests/test_capsule_launch_wiring.py:874-918 |
| The refusal before any host effect, the mode gate, the byte-identical legacy payload, the single-carrier bound and the site enumeration. | `test_an_uncapsulable_role_refuses_by_name_before_any_host_effect`; `test_the_mode_gate_names_capsule_legacy_and_refused_for_every_seat_class`; `test_the_legacy_launch_payload_is_byte_identical_to_the_pre_capsule_payload`; `test_the_delivered_payload_carries_the_capsule_once_and_no_task_context`; `test_every_production_launch_request_site_is_wired_or_declares_its_legacy_chain` | mcp/tests/test_capsule_launch_wiring.py:577-607; mcp/tests/test_capsule_launch_wiring.py:615-657; mcp/tests/test_capsule_launch_wiring.py:659-710; mcp/tests/test_capsule_launch_wiring.py:712-759; mcp/tests/test_capsule_launch_wiring.py:761-801; mcp/tests/test_capsule_launch_wiring.py:805-844 |
| The declared legacy exclusion, the free agent's admission, and the two defect pins. | `test_the_declared_legacy_reopen_names_why_it_cannot_carry_a_capsule`; `test_the_free_agent_admission_names_its_absent_task_plane`; `test_the_free_agent_capsule_identity_moves_with_the_seat`; `test_the_registered_capsule_operation_resolves_a_repository_through_its_schema`; `test_a_refused_stage_refuses_again_in_the_same_process` | mcp/tests/test_capsule_launch_wiring.py:803-814; mcp/tests/test_capsule_launch_wiring.py:919-944; mcp/tests/test_capsule_launch_wiring.py:945-968; mcp/tests/test_capsule_launch_wiring.py:975-1022; mcp/tests/test_capsule_launch_wiring.py:1028-1059; mcp/tests/test_capsule_launch_wiring.py:847-856; mcp/tests/test_capsule_launch_wiring.py:1072-1104 |
| The production-chain evidence the module's in-process cases complement. | `resolve_runtime_spec`; `verify_capsule_binding` | mcp/src/agents_remember/serving/eve_runtime_launch.py:312-348; mcp/src/agents_remember/serving/eve_runtime_launch.py:466-515 |

## 260915-CAPS-L5 Codex Capsule-Delivery Test Population

One module and two fixtures join this route. `test_codex_capsule_delivery.py` collects **28 cases**
(`pytest --collect-only -m ""` → `28 tests collected`; the default selection collects the same 28 — the
module carries **no `integration` marker**), registered in `test-evidence-lanes.toml` under
**`provider-conformance`** at entry row 216, between `test_codex_app_server_adapter_turns.py` and
`test_harness_control_claude.py`. That lane is its behaviour-preserving one: its subject is the vendor
app-server's instruction channel — a schema fixture generated from the installed `codex-cli 0.151.0`,
one live native case, and the Codex adapter/session seam — exactly like its sibling
`test_codex_app_server_*` modules.

Two fixtures arrive with it, both **expiry artifacts pinned to the installed CLI version**:

- `codex_app_server_instruction_channels.json` — the independent side of the wire comparison: the
  instruction fields per thread-open request (`baseInstructions` + `developerInstructions` on
  `thread/start`, `thread/resume`, `thread/fork`; **none** on `turn/start`, which is the fact the whole
  lifetime design rests on) and the response's `instructionSources`. Read by the test, never imported
  from the module under test.
- `codex_app_server_model_page.json` — one captured real `model/list` page, because the leaf's first
  hand-written drafts were rejected by the production parser. The durable answer was to capture the
  vendor's real reply and pin it.

The module's shape is worth naming: it drives **production** seams and doubles only two things — the
transport (so wire shape is asserted without a vendor process) and the transient capability-preflight
discoverer (so the launch-boundary case does not start a second vendor process); the real adapter in
those cases still comes from the production factory. Its load-bearing cases are noted on its sidecar.
The live case is gated by a `skipif` version check, so a skip is never a pass.

## 260915-CAPS-L4 Capsule And Skill-Serving Test Population

One module joins this route: `test_capsule_serving.py`, **30 collected items** — **28 in the unit
population and 2 marked `integration`** — registered in `test-evidence-lanes.toml` under
`unit-regression` at entry row 19. It grew from 21 to 30 items across the leaf's two repair rounds.

Its shape is worth naming because two different kinds of case live in one module:

- **Twenty-eight hermetic cases** over a `World` fixture: a disposable coordination root with a contract
  and leaf/master task documents, plus a synthetic skills corpus whose bytes the cases can predict
  (including a nested skill). They cover capsule admission and refusal (the role string cannot acquire
  another role, an unknown role gets its own status, a task path escaping the task root is refused, the
  manifest decides the source set rather than the caller, a moved task document is **re-read** while a
  recorded admission whose bytes moved is **refused**, the operation writes nothing to the tree it
  reads, and altitude admission is pinned across **every** role the document can carry so a hardcoded
  role fails) and skill serving (origin and revision kept, a body whose bytes changed since the catalog
  refused, reading grants none of the tools the frontmatter names, a resource read leaves the tool
  surface and response registry unchanged, same-named skills from two servers stay distinct, the
  discovery registry is not the model-visible catalog, a skill body is not composed into the instruction
  stream, a non-conforming skill directory is recorded not served).
- **Two real-process exchanges**, the only `integration` members: the shipped entry point is started as
  its own process and driven by the **installed SDK's own client** (`mcp.client.stdio` +
  `ClientSession`) — an implementation independent of the server code under test. The exchange observes
  the negotiated capabilities, the resource list, the index, a selected body, a supporting file, a
  refusal, **and both extension methods** (`skills/list`, plus `skills/get` with an absent URI refused
  `-32602`); the other attempts a traversal path from the live process and requires the read to be
  refused.

The cases the repairs added are the ones worth naming here, because they are what makes the module's
coverage claim honest rather than self-derived: `test_every_sep_2640_entry_is_complete_and_carries_verbatim_frontmatter`,
`test_this_servers_own_index_resource_keeps_the_agent_skills_discovery_shape` (this server's own index
shape, asserted separately from the enumeration surface),
`test_a_catalog_record_that_escapes_its_skill_directory_is_refused`,
`test_the_index_reader_refuses_while_a_skill_cannot_be_served`,
`test_a_skill_whose_directory_name_disagrees_with_its_name_is_recorded_not_served`,
`test_the_extension_declaration_is_installed_once_per_server`, and
`test_a_nested_skill_is_published_flat_like_any_other`. Each drives one previously-unpinned guard
directly instead of asserting from a neighbouring surface.

Three cases run against the **shipped corpus** rather than the synthetic one (the corpus parses and
every served skill has a root revision, the composition manifest declares the skill that is served, the
index document is the expected shape); those are the cases that would catch packaging drift between the
canonical root `skills/` tree and the served copy. The module also carries
`test_the_mutation_harness_can_actually_fail`, which is what keeps the leaf's seeded-mutation evidence
honest.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture world and the synthetic corpus every hermetic case is built from. | `World`; `_synthetic_corpus` | mcp/tests/test_capsule_serving.py:308-308; mcp/tests/test_capsule_serving.py:419-419; mcp/tests/test_capsule_serving.py:423-551 |
| The admission guarantees: no role acquisition by string, no caller-selected source, no write to the read tree. | `test_a_caller_changing_the_role_string_cannot_acquire_another_role`; `test_the_manifest_decides_the_source_set_not_the_caller`; `test_the_capsule_operation_writes_nothing_to_the_tree_it_reads` | mcp/tests/test_capsule_serving.py:639-639; mcp/tests/test_capsule_serving.py:651-651; mcp/tests/test_capsule_serving.py:690-690; mcp/tests/test_capsule_serving.py:655-673; mcp/tests/test_capsule_serving.py:694-706; mcp/tests/test_capsule_serving.py:643-652 |
| The guards the repairs pinned, each driven directly by its own case. | `test_a_catalog_record_that_escapes_its_skill_directory_is_refused`; `test_the_index_reader_refuses_while_a_skill_cannot_be_served`; `test_the_extension_declaration_is_installed_once_per_server`; `test_a_nested_skill_is_published_flat_like_any_other` | mcp/tests/test_capsule_serving.py:1321-1321; mcp/tests/test_capsule_serving.py:1348-1348; mcp/tests/test_capsule_serving.py:1389-1389; mcp/tests/test_capsule_serving.py:1489-1489; mcp/tests/test_capsule_serving.py:1325-1349; mcp/tests/test_capsule_serving.py:1352-1367; mcp/tests/test_capsule_serving.py:1393-1407; mcp/tests/test_capsule_serving.py:1496-1542 |
| The SEP entry contract, asserted separately from this server's own index shape. | `test_every_sep_2640_entry_is_complete_and_carries_verbatim_frontmatter`; `test_this_servers_own_index_resource_keeps_the_agent_skills_discovery_shape` | mcp/tests/test_capsule_serving.py:1008-1008; mcp/tests/test_capsule_serving.py:1040-1040; mcp/tests/test_capsule_serving.py:1044-1075; mcp/tests/test_capsule_serving.py:1012-1041 |
| The two independent-SDK-client exchanges, including both extension methods and the `-32602` refusal. | `test_a_real_client_and_server_exchange_over_the_installed_sdk`; `test_the_server_process_never_serves_a_file_outside_a_skill_directory` | mcp/tests/test_capsule_serving.py:1195-1195; mcp/tests/test_capsule_serving.py:1268-1268; mcp/tests/test_capsule_serving.py:1198-1268; mcp/tests/test_capsule_serving.py:1271-1302 |
| The case that keeps the seeded-mutation evidence honest. | `test_the_mutation_harness_can_actually_fail` | mcp/tests/test_capsule_serving.py:1305-1317 |
| The lane row that selects this module into the unit population. | "mcp/tests/test_capsule_serving.py" | mcp/tests/test-evidence-lanes.toml:23-23 |

## 260915-CAPS-L20 The Governing-Overview Guard And Its Wiring

This route gained one module and one case, and they protect two halves of one defect that were
separately invisible.

`tests/test_governing_overview_resolution.py` guards
`memory_quality/integrity/governing_overview_resolution.py`'s **discrimination**. Its single case
seeds, in one temporary tree, a card with a live field and a dead body link (`D3`'s shape), a card
whose field resolves under no base and which is broken in the body too (`D16`'s shape — the card the
per-declaration rule exists for), and both observation shapes, beside a clean card and a route
overview that must stay green. It asserts the **identity** of the finding set as `(card, code)` pairs
rather than a total, because a count cannot show that both representations were reported, and it
asserts `unresolvedField` and `unresolvedLink` separately so a first-match-wins regression cannot hide
behind a sum. It also pins the walk population, so a widened root would red it.

The second half lives in `tests/test_memory_quality_runs.py`, because the silence was the product
defect: `test_a_dead_governing_overview_reaches_the_gated_repair_set` drives
`_attach_curator_checklist` with a real onboarding tree holding one card whose body link resolves to
nothing, and asserts the finding arrives in the gated repair set the curator's loop reads — its code
exactly `["governing-overview-link-unresolved"]`, and the published `unresolvedLinkCount` beside it. A
correct checker whose findings never reach `repair_findings` still reports a clean
`curatorActionableCount`, which is exactly how 41 dead declarations passed every gate.

Both new modules are registered in this route's `test-evidence-lanes.toml`, so the fail-closed lane
loader stays complete: the new test module is its own row, and the extended module keeps its existing
one. The unit population moved 11 → 12 cases in `test_memory_quality_runs.py` and gained this leaf's
one new module case — a net **+2** against the leaf's measured base.

## Purpose

Terminal cleanup and abandonment exclude the computed root ledger cache from memory dirtiness and discard only that cache before ordinary Git worktree removal. Actual code/memory edits and branch ancestry remain protected. Abandon preview passes its preview state to result validation. The existing Git and public-terminal tests cover these boundaries.

This route retains a small behavior-oriented verification population plus shared fixtures. The
terminal-evidence cursor suite is a focused unit-regression module for no-loss deque envelopes,
unsupported-harness refusal, bounded Pi continuation, and liveness failure containment. A file
named `test_*.py` may still contain only builders; its filename and historical sidecar do not
establish current test coverage. Read the current file card and source before claiming a scenario
is protected or restoring an old matrix.

## 260915-CAPS-L6 Native eve Adapter Test Population

Five modules join this route for the native eve session adapter (`CAPS-R06@v1`), and their shapes
differ in a way a reader must not flatten: **two are collected suites and three are support or
explicit-run scripts.**

- `test_eve_protocol.py` (collected) — wire-contract conformance, nine classes. Beyond the original
  framing/parsing/routing faces it now carries `EveReplayWindowTests` (the bounded replay window's
  eviction, size-1, id-less and non-positive cases), `EveWireBodyTests` (create *and* follow-up both
  spell the queued policy), and `EveWireRequestTests`, which drives the **production**
  `EveRuntimeProcess` through `httpx.MockTransport` so the sent request is asserted instead of
  inferred from a double.
- `test_eve_adapter.py` (collected) — ten case classes, one per named scenario, driving the real
  adapter and mapper through the transport seam; only the eve process is replaced.
- `eve_adapter_test_support.py` (not collected) — the deterministic **transport** double, shared by the
  adapter suite. It is not an adapter double; replacing the adapter there would make every case
  vacuous. Its cancel observation records the `(session_id, turn_id)` pair so a wrong-turn cancel can
  fail.
- `eve_fixture_model.py` (not collected) — a deterministic OpenAI-compatible model **provider** the
  live fixture starts as a child process.
- `live_eve_native_fixture.py` (not collected, run explicitly) — the live proof against a real eve
  process, real HTTP and a real durable stream. It needs Node ≥ 24 and an installed dependency tree,
  which is exactly why it must not join the default suite; its JSON artifacts are the evidence, not a
  pytest exit code.

`test_harness_launch.py` is extended rather than joined: `_knob_values` now collects `knobs.env`
beside argv and session config, because eve's model and effort are compiled application values with no
argv spelling. The parametrized launch-vocabulary contract therefore covers four harnesses, driven
from `sorted(BUILTIN_PROTOCOL_HARNESSES)` — the registry the factory itself consults.

Route consequence: "the suite protects this scenario" now depends on `test_*.py` collection for the
two adapter/protocol suites and on an explicit `--report-dir` run for the live fixture. A live
scenario is only proved by its artifact, and a blocked run is not a pass.

## 260915-CAPS-L2 Role-Capsule Compiler And Admission Coverage

Two new modules cover the deterministic role-capsule compiler, split by the boundary they exercise.
`test_role_capsule_compiler.py` holds **49 test functions (50 collected)** on the compiler's
observable properties, built on an in-memory fixture that mirrors the canonical manifest schema so a
case varies exactly one fact; `test_role_capsule_admission.py` holds **43 test functions (54
collected)** covering the frozen vocabulary, the manifest parser, source admission, the shipped
corpus end to end, the routing agreement between each role's own file and the compiled capsule, and
the carried skill channel. Together: **104 passed**. Unit population 885 → **989** against a budget
of 1000; integration 225 of 250 and unchanged — no integration case was added.

**Three boundaries carry the review repairs.** First, **routing agreement**: the admission module
now cross-checks each role's own canonical source against the manifest it routes from, over every
declared operation, so a manifest that quietly disagrees with the prose it routes to fails. Second,
**the carried skill channel**: a declared skill produces exactly one reference per declaration with
a revision that follows the admitted bytes; a role declaring none gets an empty tuple; a missing or
unknown skill is refused rather than dropped. Third, **source-value integrity**: revision-equals-
digest, decodes-to-nothing, and non-UTF-8 are refused in the compiler module, and
`test_a_source_that_is_not_utf8_text_is_refused` is the only case proving the `source-not-utf8` code
is reachable.

**The two capability channels are asserted separately, and that is deliberate.** Tool ids are
policy-narrowed — a request outside the admitted snapshot is refused. Skill references are carried —
**no permission assertion exists over a skill reference anywhere in either module**, because the
implementation makes no policy call for them. Merging the two into one "capability" case would hide
exactly the distinction the code draws.

The split is deliberate and worth preserving. The compiler module must **not** read the real corpus:
a fixture that mirrors the shipped tree can only be mutated by editing the thing under test, which
is how a vacuous assertion gets written. `test_role_capsule_admission.py` is therefore the only
role-capsule test that reads the real tree, and its 9-way parametrization is what makes "every
shipped role compiles from disk twice to one digest" a corpus claim rather than a single-role claim.

Two cases carry more weight than their size suggests. `test_the_role_and_operation_literals_agree_with_their_runtime_tuples`
guards a **deliberate duplication**: the frozen registry is declared twice — a PEP 695 literal for
the type checker and a runtime tuple for selection — because PEP 695 `type` aliases do not answer
`get_args`, so the ruff-preferred alias form silently produced an *empty* runtime registry. The
duplication is the fix, and this case is its guard.
`test_every_tool_the_shipped_manifest_requests_exists_in_the_public_roster` holds every tool id the
manifest declares against the published roster, so a typo is an error rather than an inert request.

The determinism assertions must stay **falsifiable**. An order-insensitive or input-insensitive
digest would make the whole determinism group vacuous, which is exactly what a seeded-mutation probe
found in an early candidate: the case then compared one fixed order with itself. Two cases were
added as the repair — order is identity, and a real binding change moves the digest — and the
structure-only guard `test_the_compiler_modules_import_no_network_client` sits beside the behavioral
`test_composition_succeeds_with_network_and_model_access_denied`.

Independent falsifiability for these cases came from a task-local probe (seeds M01–M10, `all 10
seeded mutations were caught`) that is **not** a product artifact and is deliberately not promoted
into `mcp/tests/`; it lives in the coordination task tree and expires on the next change to
`mcp/tests/test_role_capsule_*.py`, at which point these shipped cases are its executable
replacement.

## 260915-CAPS-L3 Task-Context Projection Coverage

One new module covers the task-context projection: `test_task_projection.py` holds **9 test
functions (9 collected)**, all unit, built on a synthetic coordination tree that mirrors the real
enclosure's topology. Unit population 989 → **998** against a budget of 1000; integration 10
deselected and untouched — no integration case was added, because no boundary under test is
integration-only.

**The module's docstring states the anti-vacuity rule as contract:** every case derives its expected
side from a source the projection does not feed — the fixture files written to disk, the task
layer's own frozen vocabularies, or an independently parsed copy of the projection's output. A
comparison whose two sides both came from the projection would be vacuous, and this repository's
reviews have rejected that class twice. Hold a new case to the same rule.

**Three cases carry more weight than their size suggests.** The **import-surface case** parses every
module in the package and asserts no writer, transport or task-JSON import appears — that is what
makes "task truth is read only through the owners" and "the projection is read-only" checkable
properties rather than prose claims. The **byte-identical case** digests the whole synthetic task
tree before and after both a successful projection *and* every refusal, which is the observable
consequence of the read-only contract. The **seam case** runs the projection through the compiler
protocol and then forges a digest to prove the compiler refuses it, so the seam is shown to be
two-way rather than decorative.

**The remaining six own one property each:** cross-task isolation (two leaves never leak each
other's private content), altitude scope (a sprint's decision log reaches an orchestrator but is
never injected for a leaf), operation specificity (each frozen operation selects its own channels and
document), the failure taxonomy (each unresolvable input returns its own status), three-plane
separation (a historical record and a proposal never read as a current obligation), and no
truncation (an obligation is carried verbatim while a section the packet lacks is a reported gap).

**A fixture trap worth not repeating.** The synthetic tree took three rounds (`CAPS-L3-EV5`–`EV7`)
to mirror the real topology: a leaf enclosure needs `kind: leaf` *with* a `leaf_id`, an
external-memory contract needs its ledger leg, and — the subtle one — **an internal memory root
silently wins over an external coordination hint**, so a fixture with an internal memory root
searched the task tree in the wrong place. A new fixture that does not reproduce the external
topology will exercise the wrong resolution path and still look green.

Independent falsifiability for these cases came from a task-local probe (seeds `M01`–`M20`, `all
seeded mutations were caught`, `vacuous: 0`) that is **not** a product artifact and is deliberately
not promoted into `mcp/tests/`; it lives in the coordination task tree and expires on the next change
to `mcp/src/agents_remember/application/task_projection/**` or `mcp/tests/test_task_projection.py`, at
which point these shipped cases are its executable replacement. That probe found a vacuous seed in
its own first run (`CAPS-L3-EV10`: a planted "silent fallback" was blocked by a second guard, so the
target case passed for the wrong reason); the probe now fails on a vacuous seed by design.

**Pyright reports exactly one finding for this module** — `Import "pytest" could not be resolved` —
which is this repository's pre-existing condition for every pytest-importing test module, reproduced
on the untouched shipped `test_role_capsule_compiler.py` as the control. No scoping change and no
`# type: ignore` was added to hide it.

**This module has no evidence-lane row, and the route must not be read as if it did.** The
fail-closed loader `load_lane_manifest` derives the expected test population from the
tracked-and-untracked modules under `testpaths = ["mcp/tests"]` and raises `LaneManifestError` for any
test file without an explicit lane, so `test_task_projection.py`'s absence from
`test-evidence-lanes.toml` means the manifest **does not load** as this candidate stands — the
`pytest_collection_modifyitems` hook that calls the loader and `code_quality/check.py` both turn that
into a failure. This is a code-side gap for the owning seat, not an onboarding one, and it is **not
this leaf's alone**: `test_role_capsule_compiler.py` and `test_role_capsule_admission.py` (from
`CAPS-R02@v1`) and `test_role_instruction_corpus.py` (from `CAPS-R01@v1`) are missing from both
manifests too, so the correct repair is a four-row change. Derived from the loader's source rather
than executed: this curation seat runs Python 3.10 and the repository requires `>=3.13,<3.14`, so
`import tomllib` fails and the loader could not be run here.

## Hot Path Summary

For the ledger retirement, start with transaction-only delivery, direct landing, integration/checkpoint concurrency, memory ledger projection and backfill tests. Assertions distinguish cache-only conditions from actual content, ancestry, ref and ownership failures. The retained producer census checks every active attributed memory writer; no scenario expects a third ledger commit.

Start with the distinct failure or user operation, then locate its retained owner. Checkout isolation, Dagger registry locking, private Git preparation, protected-ref recovery, durable-store races, submission authority and native framing each retain concrete behavioral protection. Compiler/certificate fixtures establish library contracts; they are not live Dagger, Codex or final-memory execution evidence. Preparation checks can guide memory repair before certification without becoming Gate 5.

For the knowledge substrate, start with the five knowledge modules and their two shared support artifacts: `test_knowledge_store.py` (invariant identity and lineage), `test_knowledge_family_revision.py` (family revisions and the family lineage), `test_knowledge_relation_rules.py` (anchors, memberships and claims, including the anchored-claim transaction), `test_knowledge_graph_reads.py` (the two relation directions compared by identity) and `test_knowledge_revision_seals.py` (the sealed predecessor field on both payloads, which exists because round 1 could not kill it). Both support modules are registered contracts in `mcp/tests/evidence-lifecycle.toml` with exact consumer lists, and all five modules are unit-regression rows in `mcp/tests/test-evidence-lanes.toml`. **The read half adds three more** and one shared support artifact:
`test_knowledge_read_scope.py` (unit-regression — the selection policy, the corrected page counts, revision
grouping, budget, the execution bound and typed absence), `test_knowledge_read_boundaries.py` (integration —
the seven anchor observations against a real committed Git tree, the snapshot/namespace/schema refusals and the
continuation bindings) and `test_knowledge_read_paths.py` (integration — what a *path* is to this read: an
address, not a pattern), all three consuming the governed artifact `read_scope_test_support.py` under contract
`knowledge-read-scope-cases`.

**The schema-generation and envelope half is its own pair plus one shared support module.**
`test_knowledge_schema_generations.py` covers the generation registry: that generation 1's fingerprint
recomputes byte-identically to its pinned constant and that the gate **raises** when one recorded
generation-1 field is perturbed (one DDL string, one trigger body, one column tuple — a pin observed only
passing is a comment), that the artifact key lookup is type-strict so `1.0`, `"1"` and `true` are refused
while the integer `1` resolves, that an unregistered version is refused by the open path, that creating a
store declares generation 2 while opening a generation-1 file reports generation 1 **with generation 1's
recorded fingerprint**, and the acceptance check a partial fix fails: adding and populating a
generation-2 table **changes** the generation-2 logical digest.
`test_knowledge_merge_generations_and_envelope.py` covers the mixed-generation preflight and the payload
seam: a v1/v1/v2 merge refused before any session exists with its positional role and expected/observed
versions and all three inputs byte-identical afterwards, **a v1/v1/v1 merge on this generation-2 build
passing** with generation 1's ten tables attached, an envelope payload refused with `invalid_payload` and
no row written, and the route hierarchy cases. `generation_test_support.py` is their shared harness: it
builds a **real generation-1 dataset from generation 1's own recorded DDL**, which is what every case
asserting a generation-1 fact must use — a fixture created by the build is generation 2, so a digest or
context built from the literal `"ar-knowledge-sqlite/v1"` describes a dataset the fixture does not hold.
`test_knowledge_routes.py` adds eighteen cases over the route *write* layer: confinement refusals for every
refused path form, an existing route returned for an already-authored path rather than a second row, an
unauthored parent refused, a three-node cycle refused with the rollback restoring the hierarchy, the
association's four refusals, idempotent re-statement, and `None` for an explicitly ungoverned row.

**The candidate and snapshot half now has its own pairs.** `test_candidate_batch_transaction.py` and
`test_candidate_batch_commands.py` cover the batch boundary and its command union (sharing
`candidate_batch_test_support.py` as their registered harness, with `test_knowledge_label_operations.py` existing
for the standalone label guard the batch path could not see), and `test_knowledge_candidate_workspace.py` and
`test_knowledge_snapshot_publication.py` cover the candidate lifecycle and the publication contract, sharing
`snapshot_lifecycle_test_support.py` — registered as `knowledge-snapshot-lifecycle-cases` with an exact
two-consumer list. **That support module's evidence node is
`test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not`, and the node is chosen for its
subject rather than its convenience:** the suite's load-bearing claim is that a published snapshot is *closed*,
which is only measurable by showing a committed-but-WAL-resident batch surviving into the published file while a
bare main-file copy of the same database does not carry it. The lifecycle suite's two durability nodes are its
other distinctive protection: one reaches the live-reader state that the removed unconditional WAL/SHM peer unlink
destroyed, and one uses a **real child interpreter** that exits with an uncommitted write transaction open. All
four modules registered by L3 and L4, and both support harnesses, are unit-regression rows with registered
contracts; a test-shaped module missing from either registry fails the load rather than passing quietly.

## 260915-CAPS-L1 Role-Instruction Corpus Contract

`test_role_instruction_corpus.py` is the focused check the lifecycle-corpus consolidation added to this
route. It is a **shipped repository test**, not a task-local fixture, and it protects the corpus's shape
rather than its prose: every role in the registry has exactly one readable source; every role source
carries the agreed six-section order, its `**Inherits:**` line, and its knob block after the handoff
section; the composition manifest resolves every role, operation, core block, template, and criteria
catalog it names; the registry is exactly nine roles with the ambient launcher as a routing condition
rather than a tenth role; the manifest carries no instruction prose; every relative path the corpus cites
resolves; and a manifest entry pointing at a missing source is **reported rather than silently accepted**.

Its `SANCTIONED_SIBLING_REFERENCES` table makes the corpus's independence rule executable — a role file
may name a sibling role file only to wear that hat or dispatch that seat, and anything else fails the
check by design. Because the assertions are property-based on the corpus's shape, they stay valid as role
prose changes; only a corpus shape change should require editing the module.

## 260915-CAPS-L18 Complete Curation Reaches This Route

`test_role_instruction_corpus.py` was extended (6 → 14 cases) with `CurationIsCompleteOnEveryLeafTests`
and `CurationGuardTeethTests`, which read the new `testing/curation_doctrine.py` registry and sweep the ten
shipped surfaces. CAPS-R18@v1 inverted the optional/narrow-curation doctrine in the shipped instruction sources. The
sentences that presented the full `memory_quality_check` operation and the `curator_coherence`
certification as developer-request-only diagnostics, "never routine closeout/integration prerequisites",
are gone. The rule is now normative: **curation is complete on every leaf** — the full operation runs at
the leaf's contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every
curator-actionable finding is repaired or escalated as blocked with its exact returned code, and the
operation is re-run after every repair until `curatorActionableCount=0` and the **raw**
`qualityChecklistStatus=ready-for-closeout`. The **combined** `checklistStatus` is rewritten to
`coherence-required` **only when the coherence record is then missing or stale** — that is the coherence
gate, cleared by publishing the `curator_coherence` authority with `prepare` → `publish` → `validate`.
On the success path, where the record is already current, the combined field is **not rewritten** at all
and keeps its incoming `ready-for-closeout` value, with `closeoutReady=true`; `ready-for-closeout` is
therefore observable in the combined field once the whole pipeline is already complete. **Field-name
correction (`D35`, made by 260915-CAPS-L10):** this sentence previously named
`checklistStatus=ready-for-closeout` as the loop's termination condition; read the raw field to end the
loop and the combined field to decide the coherence gate
(`application/memory_quality/controller.py:664`, `:671`, `:678`, `:685-687`).

**Warrant corrected by `CAPS-R19` (leaf `260915-CAPS-L19`).** The `D35` correction above originally rested
on the sentence *"`ready-for-closeout` is never a value of the combined field."* That absolute claim is
**literally false**, and `CAPS-R19`'s revision note records it as superseded by the three-path model now
stated here. The field-name correction it supported still holds; only its stated warrant was wrong.
**Attribution is complementary and both halves hold:** `260915-CAPS-L10`'s curator corrected the
**onboarding cards** that carried the wrong form, while `CAPS-R19` corrected the **shipped sources** — the
five loop-gate carriers, their nine generated copies, and the guard registry's own docstring — and brought
`docs/reference/mcp-tools.md` into both the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`.

Two corrections the inversion must not collapse, both preserved: closeout still owns only the Git
transaction and **invokes** nothing — it **carries** the completed curation as a prerequisite; and the
rule is about the completeness of curation, not about unscoped runs, so "complete" always means the whole
operation at the leaf's contract scope. The ruling is forward-looking: the already-landed and finalized
leaves are not re-curated, and whole-layer completeness is discharged by L11's full-scope run at the
frozen tip.

## CCR-R12@v5 Transaction-Only Delivery Route

`test_transaction_only_worktree_delivery.py` exercises real public closeout and paired integration. It checks actual code/memory refs and the memory-content `Code-Commit:` trailer, source movement refusals, configured-hook behavior, interrupted recovery and cache rebuilds. Missing, malformed or changed cache bytes do not create commit objects or gate delivery. The suite retains real content/ref failures instead of replacing them with cache checks. This overview describes coverage, not a current aggregate test result.

## Retained Behavioral Routes

| Concern | Current starting point | Boundary |
| --- | --- | --- |
| Checkout/host lock composition | `test_checkout_coordination_isolation.py`, `test_dagger_registry_lock.py` | Real path/lock refusal with temporary state; host authority does not open coordinator writes. |
| Durable state and event-loop liveness | `test_durable_store_contract.py`, `test_cross_store_lock_order.py` | Thread/process ordering and actual store outcomes, bounded by watchdogs. |
| Candidate and protected-ref safety | `test_git_command.py`, `test_integration_branch_authority.py` | Real Git identity, private commits, hooks and race preservation. The former `test_integration_ref_transaction.py` was deleted with the removed mid-crash ref-recovery capability.; mcp/tests/test-evidence-lanes.toml:166-201 |
| Terminal liveness cadence and readiness | `test_terminal_liveness.py` | Controlled-clock sweeper checks preserve the configured full-sweep interval and the one-second starting-row path with its four-row cap; lifecycle production wiring remains a separate candidate proof. |
| Serving-owned steady-state observation and pass-failure isolation | `test_serving_observation_loop.py` | The real `_serving_lifespan` finalizer under a virtual event-loop clock with no HTTP route registered: the completion-relative `DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS` sleep after each attempt (including a failed one), attempt non-overlap when a pass outruns its tick, the sweeper's retained ten-second full-sweep limit, observation continuing while `agent_notifier.enabled` is false, the off-loop refresh through the drained helper, exactly one observer task cancelled at teardown, and a failed pass that neither marks success nor changes cadence. Its `ServingObservationFailureIsolationTests` half then pins the failure boundary itself on the real task collection: one unexpected pass failure leaves the owner scheduled and the five sibling loops plus an in-process ASGI request alive, publishes nothing durable (with a control proving a *successful* pass does change the tree), and retries on the cadence alone from the current persisted catalog while rows, the emitted-signal marker and the workspace cursor survive; cancellation still ends the task because the boundary is `except Exception` and `CancelledError` is a `BaseException`. This module also owns the **shared serving fixture**: `_ServingFixture` is imported by `test_serving_startup_prime.py`, and its `startup` witness plus its `_Gate` parkable probe `inner` are a shared contract — **call 1 of a lifespan timeline is the pre-serve prime and call 2 is the recurring owner's own first pass**, so a case that parks or fails invocation 1 addresses the prime rather than the owner. Unit lane; the sweeper's own cadence files stay the owners of their clocks. The notifier's pre-existing inline refresh, any structured observer-failure *publication* surface, and the prime's own ordering contract are out of this proof. |
| Startup observation prime before projection and recurring loops | `test_serving_startup_prime.py` | The `LOCR-R18@v1` half of the same serving seam, driving the real `_serving_lifespan` through the shared fixture imported from `test_serving_observation_loop.py`: exactly one observation prime at the head of the timeline, dispatched off-loop through the drained helper and parked while event-loop timers keep firing, positioned before `runtime.projector.prime()`, before every recurring task and before the lifespan yield; the seeded `ready` row committed as the adapter's `unsupported` verdict and read back by both the captured initial projection and the captured first notifier sweep; a prime taken with a real `GET /api/terminal/sessions` route registered and never dispatched and with the notifier loop started but never sweeping; and the committed entry equal to one reference canonical pass over an identical seed, so no startup-only reader, cursor or write path took part. A raised prime is contained — startup, the projection prime and the recurring owner all survive and the owner retries on its first cadence. Unit lane, hermetic, ordinary test source; it asserts no health or readiness payload, and its ordering witness does not constrain prime-versus-migration/compaction (that edge rests on the production straight-line order). |

| Deferred terminal work | `test_terminal_liveness_deferred_work.py` | Real catalog/sweeper proof that hosted-interaction syncs and turn callbacks run after commit, aborted batches dispatch nothing, and post-commit failures preserve durable truth. Caller ownership remains adjacent lifecycle work. |
| Terminal catalog liveness | `test_terminal_liveness.py` | Fake-clock host/control-read hysteresis, restart continuity, and successful reset against existing production transitions. This row is the LOCR-R21 hysteresis proof only: cadence (`R12`) and sweep non-overlap (`R22`) cases for the same module are still in their own unlanded worktrees, so the composed module's case count and extents will be larger than this leaf's four cases. |

| Terminal catalog batch and sweep non-overlap | `test_terminal_catalog.py`, `test_terminal_liveness.py` | Counted `_write_disk` replacements (zero clean, one dirty, one dirty-partial) and real-thread sweep contention returning the committed snapshot without a second probe; cadence (`R12`) and hysteresis (`R21`) values stay with their leaves. |
| Candidate and protected-ref safety | `test_git_command.py`, `test_integration_branch_authority.py`, `test_integration_ref_transaction.py` | Real Git identity, private commits, hooks, race preservation and exact recovery. |
| Registry/certificate semantics | `test_certification_rail_registry.py`, `test_gate_certificate_authority.py` | Typed plan/result contracts and dependency-aware reuse, not a live producer claim. |
| Memory preparation and repair | `test_memory_quality_runs.py`, `test_citation_document_transaction.py`, `test_memory_citation_fix_scopes.py` | Exact-pair revalidation, document isolation, conflict refusal and preserved evidence. |
| State-signal structural routing | `test_state_signal_relay.py` | Action-time current-manager replacement, per-subject topology refusal, no-row/no-marker behavior while an owner is absent, and no owner wake while a seat's own turn is still open. |
| State-signal boundary delivery | `test_state_signal_boundary_delivery.py` | Row persisted before the emitted marker, zero adapter submission while the target is `working`, and delivery of that same durable row at the target's next admissible boundary across occupant replacement, fresh notifier context, and failed submission. |
| State-signal crash and restart recovery | `test_state_signal_restart_recovery.py` | The durable order row persisted → marker stamped → delivery attempted across a failed marker write, a stop after the marker, and a same-seat structural rebind: one pending row per exact seat/evidence identity, zero adapter submissions while that source marker is unstamped, and an action-time fence on the shared delivery action that state-signal recovery alone may lift. Seven cases, each rebuilt from the durable files through new store objects. |
| Curator turn owner wake | `test_state_signal_curator_wake.py` | The curator seat's own canonical terminal turn reaches the same shared role predicate and current-manager routing as the worker seat, with the durable payload carrying the curator role, the subject leaf document, the mechanical outcome and the terminal evidence identity — all derived by the real liveness sweep and the real agent-notifier sweep, never written by a curator post. A `completed` ending and an `interrupted` ending each mint exactly one durable signal and never a second on re-observation; `failed` reaches terminal truth and emits nothing while leaving the seat eligible; a curator seat whose own master has no current manager fails closed instead of routing to another master's manager; and the wake neither validates nor declares curator coherence or memory readiness. Unit-regression, one new module, no production byte changed. |
| Parked external-await separation | `test_parked_external_await_separation.py` | The parked open-turn external-await design stays out of the ended-turn relay: no `waiting` expectation kind is parseable, no wait-registration tool is advertised, and no wait/recheck/check-descriptor machinery ships. Absence guard only, not relay behavior evidence. |
| Reviewer turn owner wake | `test_lifecycle_owned_completion_relay_reviewer.py` | The reviewer role's own production-wiring relay: a short-lived reviewer seat's canonical terminal truth, produced by a real observation pass rather than a seeded row, wakes the reviewer's **current** manager as one durable inbox row — with no completion post from the reviewer and no dependence on the terminal-session read route. Six cases pin the boundaries separately. The row is truthless before the pass (`turn_state`, `terminal_outcome` and `terminal_evidence_id` all absent) and carries `completed` plus its evidence identity after it; the durable row holds while the owner is mid-turn with zero submissions and lands exactly once at the owner's next boundary. Liveness, a ready `control_state` and even a pane whose own diagnostic reads `turn-ended` authorize nothing, with a control proving the identical row does wake once canonical evidence exists — so the silence is about missing evidence, not an inert fixture. An `interrupted` turn is reported as `interrupted` with `interrupted_by=unknown`, no verdict vocabulary and a byte-unchanged leaf document. The wake is addressed by current occupancy, so a recorded `spawned_by_session` naming an exited manager generation receives nothing while the live manager gets the one row. Re-observing the same evidence identity mints no second signal even after the first row has landed and can no longer absorb a repeat by coalescing. And `failed` — production-reachable with a real evidence identity, since the pi projector settles `stopReason="error"` into it — is refused while leaving the seat eligible, so a later canonical turn still wakes the manager. Unit lane: a temporary coordination root, a scripted single-seat adapter endpoint and a tmux double at the process boundary; the lift, the outcome and the evidence identity are production's, and the relay's own structural rules stay `test_state_signal_relay.py`'s contract. |
| Worker turn owner wake | `test_state_signal_worker_wake.py` | A worker is not required to author a second completion message, so the wake must arrive on its own: an owned `worker` row whose **catalog terminal evidence** says `completed` or `interrupted` becomes a state-signal finding and the notifier persists and routes exactly one durable row to the leaf's **current** manager through the existing inbox path. Seven cases pin the boundaries separately. No inbox row is created for the worker at all, and the whole store is asserted rather than its state-signal subset, so a worker-authored row would be visible rather than filtered out. The eligible-outcome set is pinned from both sides: `completed` and `interrupted` wake the manager, and `failed` or `unknown` must not however real the evidence identity is — with a final leg re-reporting the same seat and evidence identity as `completed` and requiring the wake, which makes the empty store a measured refusal rather than an inert relay. Per-turn dedupe is pinned in both directions too: the same evidence identity projected twice mints one row, and a **second distinct terminal turn** on the same seat mints its own wake instead of being swallowed by the first turn's marker. An `interrupted` turn travels with its origin and is not mislabelled as completed; a report on disk is not terminal evidence, so the adapter evidence identity is the discriminator; the leaf and master documents are captured around the sweep and compared byte for byte, because reporting a seat turn never closes task work; and a worker below a managerless master wakes nobody, stamps no marker and guesses no global owner while staying eligible for the next sweep. An empty live terminal-session read is a measured zero on a host the delivery path demonstrably reached, because `_RecordingHost` counts every contact the sweep makes. Unit lane: a temporary coordination root with real task documents, a real catalog file, a real inbox log and the real durable stores; no HTTP request, no server, no process. The relay's own structural rules stay `test_state_signal_relay.py`'s contract, and the pre-existing dead-upstream supervision row the same sweep separately raises is outside this module's assertions. |
| Incremental memory scope | `test_memory_incremental_scope_compiler.py` | Dependency-complete work and exact reuse remain non-accepting with final-full pending. |
| Native submission and IPC | `test_harness_submission_authority.py`, `test_harness_control_ipc.py` | One request authority, idempotence, withdrawal races and ambiguous receipt reconciliation. |
| Conversation projection and assets | `test_conversation_active_service.py`, `test_conversation_control_attachments.py` | Ordering, honest pagination, one-use assets and unknown-outcome retention. |
| Canonical terminal-evidence mapping | `test_terminal_evidence_mapping.py`, `test_conversation_native_ingestion.py` | Native projectors remain the terminal-outcome authority; malformed or open frames make no terminal claim and do not hide a later canonical outcome. |
| Protocol framing | `test_codex_native_history.py`, `test_pi_rpc_process.py` | Bounded paging/correlation and real fixture subprocess behavior. |
| L38 actionable admission and closeout transport | `test_activation_admission_registered.py`, `test_worktree_closeout_route_review_transport.py` | Registered response-shape and refusal-projection checks, including bounded malformed-contract parser detail, for the frozen candidate. The activation admission is contract-scoped: a refusal carries no `classification`/`blocking`/`sourcePair*` key and never names a foreign master as blocker or retry precondition. Preparation evidence only. |
| CCR-R12 transaction-only delivery | `test_transaction_only_worktree_delivery.py` | Public code/memory delivery, interruption recovery, source/ref safety, hooks, memory attribution and cache-only no-op behavior. |
| Ledger attribution and the projected source ledger | `test_memory_ledger.py`, `test_worktree_sync.py` | Git-only computed rows, cache misses/malformed bytes and hand edits, attributed source history, and cache-independent synchronization. |
| Producer census and the one renderer | `test_memory_attribution_producers.py` | Five memory-content producers and zero untrailered, measured from source: the trailer key identifier and its interpolation appear in exactly one production module, no production module spells the trailer as a quoted literal, each of the five producers reaches a shared renderer entry, and a hostile multi-paragraph caller body survives byte for byte with the trailer appended as its own final block. The two non-closeout producers are driven end to end through the public `memory_carryover_apply` and `memory_baseline_adopt`. Source census plus real-repository cases. **Superseding the note this row used to carry: the module's `unit-regression` lane row now exists** (`mcp/tests/test-evidence-lanes.toml:69-98`, added by the commit that landed L4), so the manifest loads. |
| Leaf document master-link binding | `test_leaf_doc_master_link_binding.py` | The derived master link, end to end on real repositories: a leaf authored through `task_doc` with no series contract acquires `seriesContractPath` and its one `enclosures[]` ref when it is started; an already-damaged document (`lifecycleId` stale, no link) is repaired by its next start with objective, requirements, steps and title unchanged; a leaf under a task root with no master document is refused with `seriesContractPath`, the exact missing `task.json` and the remedy, writing nothing; and the planning flow (master plus two leaves, no start) still succeeds, still unstamped. Integration lane: one disposable code repository and one external memory repository per case. The restamp decision table is the unit half in `test_task_document_application_1.py`. |
| Closeout recovery attribution | `test_transaction_only_worktree_delivery.py` | Interrupted closeout proves actual journaled code/memory commits and refuses forged output evidence; cache state is immaterial. |
| Closeout auto-carry and parked candidate | `test_source_lineage.py` (`CloseoutSourceLineageHealTests`), `test_sync_parked_candidate.py` | The closeout boundary carries a settleable stale break, refuses a preview without mutating, escalates an unprovable break, and returns a parked dirty candidate through the sync transaction (restore on completed/resume/cancel, kept unmerged-index refusal); transaction-level detail lives in the new unit-lane module. |
| Memory-history trailer backfill | `test_memory_backfill.py` | Disposable history rewrite selection, loss reporting, byte-faithful objects, trailer-only acceptance, idempotence and multi-ref CLI publication. |

| Terminal evidence cursors | `test_terminal_evidence_cursors.py` | Focused deque envelope validation, no-advance refusal, bounded Pi continuation, and liveness containment; unit evidence only. |
| Public tool-surface inventory | `test_tools.py` (`PublicSurfaceInventoryTests`) | Live registration order against a probe `FastMCP` equals `PUBLIC_TOOLS`, and the advertised names have response models that validate. Two further cases pin the advertised **text** rather than the roster: the checkpoint landing's description must present a partial publication and deny being the pause (L36), and `worktree_pause`'s must present a stop that publishes NOTHING, name the checkpoint as the separate publication, carry no refusal the verb no longer performs, and still name the release it does perform (L37, extended by L38). Hermetic inventory contract: the probe starts no server and touches no provider. |
| Worktree next-move typing and enforcement | `test_worktree_status_terminal_next_tool.py` | The `terminal-archive-ready` branch of `worktree_status` names the accepted cleanup operation, its emitted args bind to the real tool signature (checked with `inspect.signature(...).bind`), the envelope declares `nextAction`/`nextTool`/`nextArgs`, and the `PUBLIC_TOOLS` membership validator is driven in both directions. Integration lane: real worktree services and a real repository under `tmp_path`. First coverage of that branch. |
| Stop-only pause, and the pause/publication split | `test_pause_stop_only_end_to_end.py`, `test_pause_is_not_publication.py` | The public `worktree_pause` stops an atomic master over one real temporary Git world holding two masters: it releases only this contract's activation record to `vacant`, leaves the other master's record byte-identical and still `active`, moves no ref and creates no commit (both repositories' tips, complete object databases, coordination tree, both worktrees, the enclosure and every task document measured identical before and after), reports `paused: true` with **no** `nextTool`/`nextArgs`/`nextOperation` at the top level or inside `nextStep`, reports a never-selected master as the explicit `atomic-series-already-vacant` success (that case asserted a refusal before the 260831-LOCR-L38 change set) — naming in its summary that no selection was held, and carrying an observation with no `record` where a released pause carries the one its own release wrote — and keeps the four refusal shapes apart without writing anything: a leaf contract (`pause-requires-atomic-master`), a record this contract does not own and an unreadable record (both `atomic-series-activation-release-unreadable`), and a **vacant** record naming another master (`atomic-series-activation-selected-contract-mismatch`), which is the only foreign shape that reads `vacant` and therefore the only one that could be mistaken for the success — an *active* foreign record is refused one step earlier by the observation, so the two cases prove different guards. It is idempotent, and resumes through `worktree_sync` with nothing published. Its sibling is the structural half: `test_pause_is_not_publication.py` (architecture-fitness) asserts the pause module's static import closure is disjoint from all twelve publication modules — measured 60 modules including the root, 5 direct imports, 54 beyond them — with non-vacuity assertions and named witnesses so a walker stopping at the direct imports fails rather than passes, so the stop cannot become the checkpoint publication. `worktree_checkpoint_landing` is the separate, explicitly requested publication and no case here reaches it. Integration + architecture-fitness lanes. |
| Checkpoint landing plan/apply parity | `test_checkpoint_landing_end_to_end.py` | Public unfinished-master checkpoints, actual paired refs, idempotent retry, cache independence, and real source/content/ref-race refusal parity. |
| Sub-task index reachability across a writer skew | `test_task_documents_graph_projection.py` (`SubTaskIndexReachabilityTests`) | Projection-only unit evidence that a completed leaf whose durable JSON carries a field this reader's schema does not know stays reachable from the master's sub-task index, an unstarted row keeps resolving, and a document with a required field deleted is still withheld. `_index_doc` reproduces the dashboard's own index rule (`sliceForRef`) rather than approximating it. Hermetic temporary task root; one case, one helper, no lane change. |
| Cross-master concurrency on one protected source pair | `test_cross_master_concurrency.py`, `test_atomic_series_activation.py` | One sprint commands every atomic master from its own source branches, so two atomic masters share one protected source pair; each keeps its own activation record. Both masters stay ready and progress, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks no sibling (the same statement the stop-only pause now makes as a real public operation, `worktree_pause`, proved separately in `test_pause_stop_only_end_to_end.py`), a conflicting or stale publication is refused at the pair (`blocked-non-ff`, `atomic-series-checkpoint-candidate-moved`), and a master that reconciles with a landed sibling finishes through ordinary public closeout and final integration rather than a checkpoint. A graph-less sprint serializes nothing — `executionGraph=None` resolves to the `atomic-sequential` sprint shape (every commanded master executes atomically, no dependency is declared) and both masters hold their own activation concurrently with no waiting reason. Only a real sprint-graph wave edge still gates (`predecessor-incomplete:`). Integration lane: real temporary Git repositories and the public operations. |
| Capacity refusal source classification | `test_closeout_projection_source_classification.py` | The three states of a projected source stay distinct on the code its own raiser published. `graph_context` refuses a sprint whose authored graph is one node past `MAX_CLOSEOUT_MASTERS` with `closeout-queue-master-capacity-exceeded` — its own declared code, read back from the refusal rather than retyped — and that code classifies `invalid`, because the source was read and is past its bound; `contract-unreadable` and `atomic-series-contract-unreadable` still report `unreadable`; and the ordinary projected source stays readable with no problems and classifies `active`. The classifier tests membership of `closeout_queue_errors.py`'s `CAPACITY_REFUSAL_CODES` instead of the substring `cap-exceeded`, which neither surviving capacity code contains. Integration lane: real temporary Git repositories through `QueueFixture` and the production graph admission path. |
| Registration before compaction | `test_terminal_liveness_registration_order.py` | The full sweep's post-commit order, pinned where it happens: the traced terminated-row read records the batch-commit state observed **at the read**, so the chain `batch-enter → batch-exit → enumerate[include_terminated=True, batch=closed] → register → compact` fails if the enumeration moves inside or ahead of the observation batch. The registrar's returned proved-id set is the only argument `compact` receives, an absent registrar yields the empty proved set (so a task-bound leaf row survives), a raising registrar stops the pass before `compact`, a crash after registration re-registers idempotently on the next pass, and the starting-row fast path does neither stage. Hermetic unit lane; no production byte changes for this contract. |
| Terminal observer health | `test_terminal_observer_health.py` | The observer stage's own health reading (`LOCR-R17@v1`), sixteen cases in three classes: the exact atomic v1 record and its writer (constant-size row, no partial document, the failed-write source of truth being the persisted row rather than the newer in-memory accumulator), the status ladder `initializing`/`degraded`/`healthy`/`stale` at exactly `6 ×` the configured sweep interval, omission-and-no-repair for every unusable source (missing, unreadable, wrong marker, extra or missing key, wrong type, naive stamp, prior-lifetime stamp, above-ceiling counter), the bounded ordered secret-safe failure vocabulary, publication on the observer CALL for success and failure alike through the real lifespan, the fixed write-failure log line with retry, and the served tail driven through the real `_state_response` handler and `stream_events` generator (additive key, untouched ETag/304 path, health on the snapshot and none on a delta, plus the packet's cross-read rows including "healthy beside a fresh notifier"). Unit lane: no HTTP transport, no server, no real second. |
| Terminal blocker reasons | `test_terminal_blocker_reasons.py` | A cleanup or finalize blockage always names the component it stopped on and a non-empty reason. The L6 shape — terminal archive proven, provider runtime already gone — finalizes on the first call with an empty `notRemoved` inventory; a real permission failure on the provider tree blocks with `remove_tree`'s own `permission denied: ...` reason, closes nothing and refuses identically on retry; and both invariant owners are driven directly (`_blocker` refuses a missing, blank or non-string reason, and `remove_tree` names a reason whenever it reclaimed nothing). The L6 payload is reproduced through the provider port boundary, not by re-enacting the original physical event. Integration lane; one new module, no deleted module. |
| Pane diagnostics are non-authoritative for turn truth | `test_terminal_liveness_pane_authority.py` | The pane's own reading is persisted only as `control_raw["paneDiagnostic"]`; adapter snapshots plus the canonical terminal projection own `turn_state`, terminal outcome/identity, interruption origin and state-signal eligibility. Ten cases pin the boundary: contradictory pane/adapter readings in both directions, **readiness** (an adapter `control="disconnected"`/`"failed"` snapshot with a `working` pane keeps the adapter's `control_state`, activity/acceptance `unknown`, turn `stale`), below-threshold retention with the `controlReadFailures` counter, the R21 third failure owning `disconnected`/`stale`, alive-starting retention, the legacy no-`control_endpoint` `unsupported`/`stale` projection proved never to consult the control surface, a failed terminal page advancing nothing, startup-prime and steady-pass sharing one boundary (`host.calls == 3` discriminates the fast path), a four-reading pane-independence matrix, and a negative AST source guard over `terminal_liveness.py` itself. This module is a **deliberate split** from the 574-line `test_terminal_liveness.py`, which it leaves byte-unchanged and from which it imports its fixtures; an in-place extension had reached the coding-guidelines 900-1200 band, so the two cards must not be merged. The source guard is defence-in-depth over behaviour, not the sole pin: it is measured blind to a pane-derived constant inside an enclosing `if`, to positional writer arguments and to `CatalogTurnEvidence(state=…)`, all three of which stay caught behaviourally. Integration lane; one new module, no production byte changed. |

| Observer-to-notifier handoff latency | `test_serving_notifier_handoff.py` | `LOCR-R04@v1`'s completion-relative relay proof, eight cases over one disposable world that enters the real `_serving_lifespan` under a deadline-correct virtual clock, so the real observation loop, the real `TerminalCatalogLivenessSweeper.refresh`, the real catalog commit boundary and the real `run_agent_notifier_sweep` are what is measured. The two loops share no wake-up channel: the observer polls every `P` (1.0 s) after each attempt returns and the sweeper admits one full sweep per `F` (10.0 s) from the previous full sweep's **start**, while the notifier evaluates the durable catalog and sleeps `N` (10.0 s) after its pass returns — so the delivered worst phase is `F + P + R_observer + D_commit + N + R_notifier`, 21.0 s of logical scheduling for the default knobs plus only measured overrun. Each case asserts the bound **and** its decomposition from measured terms, and each protects one clause: the nominal phase, the previous full sweep's own overrun, a starting-row fast-path overrun, a notifier pass in flight at the commit (whose interval starts at its own completion, not at the commit), committed-truth-only reads (a read attempted before the commit and returned after it carries the committed rows in the notifier's own `include_terminated=True` scope), coalesced missed ticks for both loops, a live pass that did not observe the fact being unable to satisfy the stage, and notifier disablement with in-place re-enabling. The oracle documents three relations it deliberately does **not** assert — the telescoping decomposition, the observer phase's maximum, and `bound` as the sum — because each holds in every reachable state; an assertion that cannot fail is not evidence. Unit lane: no HTTP request, no server, no process. |

## 260831-LOCR-L04 Overrun-Accounted Observer-To-Notifier Handoff

`test_serving_notifier_handoff.py` (unit-regression, manifest row `:97`) is the proof half of a
**preservation** requirement. `LOCR-R04@v1` requires zero production change, so the leaf's entire
deliverable is the timing oracle and its evidence envelope and `mcp/src` is byte-unchanged by the change
set; the two support modules that carry the instrument — `_handoff_clock.py` (the deadline-correct
virtual timeline plus `_Gate` and `_Sequence`) and `_serving_handoff.py` (the disposable world and the
oracle's terms) — take no manifest row, by the same rule that keeps this directory's other support
modules out of it.

**What the oracle states.** The serving lifetime owns two independently scheduled loops and neither can
be woken by the other, so the relay is correct only if their cadences compose into a bounded handoff:

```
observer_release = max(previous_full_sweep_start + F,
                       completion of any observer refresh() still holding the shared sweep lock there)
consuming_sweep  = the first lifecycle poll at or after observer_release, at most P later
commit           = the consuming full sweep's own durable catalog commit
next_notifier    = last_notifier_pass_end + N

worst phase      = F + P + R_observer + D_commit + N + R_notifier
```

`R_observer` is the remaining duration, measured at eligibility, of any refresh holding the shared sweep
lock — the previous full sweep **or** a starting-row fast-path pass; `D_commit` is the consuming sweep's
own duration up to its commit; `R_notifier` the remaining duration of a notifier pass already in flight
at that commit. For the default knobs the fixed part is 21.0 s of logical scheduling; everything beyond it
is a measured overrun rather than an allowance, and a case that met the bound by a different
decomposition still fails because the decomposition is asserted, not illustrated.

**Why each case exists.** The nominal phase; the previous full sweep's own overrun, where the sweep is
parked inside its batch after it already read the evidence row unarmed; a starting-row fast-path overrun
with a nonzero commit duration, where the observed latency is exactly the oracle's sum; a notifier pass in
flight at the commit, whose interval starts at its own completion; committed-truth-only reads, where the
read is attempted before the commit and returns after it carrying the committed rows; coalesced missed
ticks for both loops, so three expiring ticks behind a parked pass queue nothing; a negative control in
which rate-limited polls and a live notifier pass exist while the fact is readable and none of them is the
consuming pass; and notifier disablement, where observation keeps sweeping and commits with signal
derivation off, the loop re-parks without running a pass, and in-place re-enabling reaches the
already-committed truth on the next completion-relative pass.

**Two design properties, recorded because a passing run cannot show them.** Case 1's strict
observer-phase assertion (`observer_term < F + overrun`) is a constraint on **that case's arming
scenario** — it arms the fact `P / 2` after the previous sweep's start — and not a claim about production
behaviour; its failing state is the tight arming the other cases use, and the arithmetic identity that
would restate the arming constant has no such state, so it is not asserted. And `assert_oracle` documents
three relations it deliberately does not assert — the telescoping decomposition, the observer phase's
maximum, and `bound` defined as the sum it is compared against — because each holds in every reachable
state, reachable or not; asserting them would add lines that cannot fail rather than evidence.

**The lane-row insertion moved citations, not just a row.** The new module's row sits at `:97`, above
every previously-latest unit-regression row, so every manifest line at or after it shifted by one —
`test_serving_observation_loop.py` `:97` → `:98`, `test_serving_startup_prime.py` `:98` → `:99`, L17's
`test_terminal_observer_health.py` `:122` → `:123`, and every later lane key with them. The 59 live
citations into the manifest were therefore re-derived against the current file rather than carried, and
the dated `## KS-R15@v1 Lane Registrations And The Citation Shift


Two modules joined the lane manifest this leaf: the unit module `mcp/tests/test_review_assessments.py`
in the **unit-regression** lane and the integration module
`mcp/tests/test_curator_review_assessment_publication.py` in the **integration** lane. Both are
registered in `mcp/tests/test-evidence-lanes.toml`, and one consumer row for the integration module was
added to `mcp/tests/evidence-lifecycle.toml`.

Because both rows were inserted at the head of their lanes' lists, **every lane row cited in this
overview from the insertion points down moved**, and the affected claims in this card were re-derived
from the current file rather than accepted from the mechanical projection: the integration rows for the
knowledge read/diff boundary and path modules are now `:165`, `:166` and `:167`, the L37 pause-suite
and AST-only-guard rows are now `:203` and `:240`, and the knowledge-diff scope row stays at `:81`.
The parenthesised "row N at that leaf; row M now" notes in those claims were corrected with them, and
one stale `:162` mention was dropped rather than restated.

The route's own composition is unchanged: no lane was added, removed or re-classified, and the
fail-closed manifest still requires one classification per new module.

## 260915-KS-L15 The Assessment Populations

Two modules joined this route's populations and the route's lane composition is unchanged: the unit
module `test_review_assessments.py` in the **unit-regression** lane and the integration module
`test_curator_review_assessment_publication.py` in the **integration** lane. The unit module protects
the record's decidable content — which fields a stored assessment must carry, that the three
dispositions are not interchangeable, that a relocated input with identical content is not equivalent,
that absence is never rendered as a favourable disposition, and that the `knowledgeReview` section
moves no count. The integration module drives the **production** publication against a real
external-memory leaf enclosure and is the only place a survival claim is made, because it reads every
recorded byte back by its recorded path and digest, including after the enclosure's `reports`
directory is removed.

One consumer row was added to `evidence-lifecycle.toml` for the shared support module owned by
`curator-coherence-test-port`; no contract and no artifact was added, so the catalogue's counts are
unchanged at 13 contracts and 54 artifacts while its digest moves. Both lane rows were inserted at the
head of their lists, which moved **every lane row cited below the insertion points in this overview**
and is why the affected claims here were re-derived from the current manifest rather than accepted
from a mechanical projection. The case budgets are unchanged: this leaf's own candidate leaves both
the unit and the integration ceilings under their declared limits, so it raised neither.

the dated `## Update History
- 2026-09-18T08:30+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 2 generated projection bullet(s) by hand** — `mcp/tests/test_knowledge_family_composition.py`, `mcp/tests/test_knowledge_family_composition_boundaries.py`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.
- 2026-09-17T11:20+02:00 — 260915-CAPS-L15 curator: the suite gained one module, 14 cases, and this
  card records what it is *for* rather than only that it exists: the acceptance test the master lacked,
  driving both production launch points and reading the capsule from each started session's own first
  prompt, with the expected side being the compiler's own result. A declared section lists the case
  groups — including the production-chain pair that **replaced a deleted hand-supplied case**
  (`L15R-2`'s evidence class) — and states where the live system-block half of the evidence lives
  instead. Five reference rows added. Verification metadata moves to this leaf's base `15fa0e2c`; the
  candidate is deliberately uncommitted, so the governed closeout stamps the real code commit and no
  hash or fingerprint was invented here.
` entries below were left as written because they are as-of records of earlier
candidates. No case budget is quoted or changed here: `pyproject.toml` is the authority, and this leaf
adds no collected case to any capped population.

**Boundaries.** No case edits or imports a production module's internals; every case measures production
through the harness's recordings. The oracle claims the two loops compose within the bound — not the
sweeper's internals beyond its retained ten-second full-sweep limit, not the notifier's internal predicate
set, and not the catalog's on-disk format. Lane membership is classification, not execution or acceptance
evidence, and the verification stamps remain closeout-owned.

## 260831-LOCR-L10 State-Signal Crash And Restart Recovery

`test_state_signal_restart_recovery.py` (unit-regression, manifest row `:101`) is the executor for the
relay's restart idempotency contract that no earlier module forced: for one exact catalog seat plus its
`terminal_evidence_id`, retries and process restarts converge on **one** durable state-signal row and
one emitted marker, in the order row persisted → marker stamped → delivery attempted. Seven cases,
each building one temporary durable world and then re-reading it through brand-new catalog/store/context
objects: a marker write that raises leaves exactly one pending unmarked row, zero adapter submissions
and a restart that renews that same row id before delivering once; the two competing finders' findings
(the generic redelivery finder run over that generation, and the boundary-drain finder) are both fenced
at the shared action with no delivery-state mutation before state-signal recovery stamps and delivers in
the same sweep; a stop after the marker leaves one *marked* pending row that the ordinary pending-row
path lands once; a same-seat rebind between row persistence and marker retry renews and re-addresses the
original row id instead of minting a sibling; two distinct seat ids sharing document, role, outcome and
evidence hold two rows that never renew each other; a later evidence identity re-arms the seat as a
successor row while the older row still delivers; and the non-state preservation control keeps the
structural coalescing key and its occupant-blind behavior. Reverting the three source hardenings turns
six of the seven red, with that preservation control the single pass — the module is sensitive to the
ordering it claims, not to its own scaffolding.

**The fence's reachable route is the boundary drain, not the generic finder.** Case two obtains the
competing findings by calling each finder and acting the finding, because the sweep's *generic*
redelivery path cannot select such a row by construction: `state_signals.state_signal_held_on_boundary`
excludes a non-landed state-signal row whose target seat is alive. The reachable caller is
`evaluate_predicates` → `evaluate_boundary_drain_findings` → `_drain_boundary` → the shared `_redeliver`,
which carries no held-on-boundary filter; the independent baseline review reproduced that route on a
real sweep and observed the skip (`('boundary-drain', 'skipped', 'state-signal source marker not
stamped')`, zero submissions, row untouched) with recovery then stamping and landing the same row. A
future touch of this module would be stronger with that real-sweep drain-fence assertion recorded as a
case; it is not authorized scope for this leaf. Case inventory, helpers and the contract narrative live
on `test_state_signal_restart_recovery.py.md`.

| Terminal catalog reads are side-effect free | `test_serving_terminal_catalog_read.py` | The real registered `GET /api/terminal/sessions` route driven over `fastapi.testclient.TestClient` and the real composed `create_app`: one hundred requests produce one hundred equivalent answers with every ledger at zero; probe, cursor advance, row mutation and compaction each fail on their **own** instrument rather than as one aggregate; the no-adapter-probing clause is pinned at the readers themselves, by name **and** by object identity, so a route-side read bound through a module-level `import … as` alias is counted too; a catalog change between two reads is attributable to the background observer, and an observer that has failed still serves the stored snapshot instead of being repaired by the request; and path, declared model, conditional-key behaviour and status semantics are unchanged through the composed app. Integration lane, one new module, no production route behaviour beyond removing the handler's sweep. Two limits are recorded rather than papered over: a reader reached through anything that is not a module global (a function default, closure cell, class attribute, dict entry or instance attribute) stays outside the reader ledger, and the 100-GET case is content-vacuous on its own, so content is pinned by the composed-app and failed-observer cases. |

## 260831-LOCR-L07 Curator Turn Owner Wake

`test_state_signal_curator_wake.py` (unit-regression, manifest row `:102`) is the executor for the
curator half of the terminal-turn wake: a curator's durable output is its structured coherence
authority rather than a chat message, so the curator must not have to hand-author a completion post
for its manager to resume. The module starts where production starts — the adapter's own evidence
frames — and lets the real `TerminalCatalogLivenessSweeper` derive the catalog turn truth before the
real agent-notifier sweep relays it, so no row in any scenario is written with a turn claim, a
terminal outcome or an evidence identity, no terminal-session GET is issued, and no curator-authored
completion row exists. Five cases: a `completed` ending wakes the **current** manager of the
curator's own master with exactly one durable signal carrying the curator role, the subject leaf
document, the outcome and the evidence identity, and re-observing that same terminal evidence mints
no second signal and no second row; an `interrupted` ending carries interruption truth
(`outcome interrupted`, `interrupted_by=developer`) and is re-emission-guarded on that path exactly
as the completed one is; `failed` is the negative control that keeps the two-outcome boundary honest
from the outside — the seat does reach terminal truth, and the relay still emits nothing, leaving the
seat eligible so a later canonical outcome can still wake; a completed ending appends no verdict —
the payload equals the canonical `state_signal_ask` / `state_signal_response` derivation, contains
none of the acceptance vocabulary, and the coordination root read **after** the sweep is the same
population as the premise, so a relay that wrote its own coherence or readiness artifact would show
up there and nowhere else; and a curator seat whose own master has no current manager fails closed
instead of routing to a live other-master manager, with the seat left eligible rather than consumed.

Two things are deliberately *not* claimed. The wake is terminal-truth relay only: it neither
validates nor declares curator coherence, memory readiness or closeout acceptance — the manager opens
and validates the canonical curator authority itself, and `accepted` is a transport fact here rather
than a verdict about the curator's memory. And the stale spawn-ancestry address registered on the
curator row is never selected: routing resolves the owner from the task hierarchy, so the cases
assert the manager the topology names rather than the session the seat was spawned from. Case
inventory, helpers and the fixture contract live on `test_state_signal_curator_wake.py.md`.

## 260915-KS-L12 Two Supporting-Record Case Modules, And A Shared Fixture That Is Registered Evidence

`KS-R12@v1` adds two case modules to the `unit-regression` lane — `test_knowledge_evidence_claims.py`
and `test_knowledge_evidence_observations.py`, twenty cases each, both carrying
`pytestmark = pytest.mark.evidence_unit` — and one **shared support module**,
`evidence_test_support.py`, that both build on. The cases cover the claim contract and the observation
contract in the order the requirement states their clauses: the typed aggregates under the shipped
envelope, the structural subject and coverage kinds, the resolved links and their five endpoint kinds, the
required limitations field served visibly, the opaque assessment references, the verbatim command identity,
the artifact digest measured against real bytes, the closed five-member execution result, the run
environment, the generation gate in both directions, and the read projections that report facts and no
verdict.

**The support module is registered evidence, not an unregistered helper.** It is
`contract:knowledge-evidence-cases` with an owning contract row and a `shared-support` artifact row in
`mcp/tests/evidence-lifecycle.toml` — authority `internal-canonical`, category `unit-regression`, fidelity
`in-process`, cadence `affected`, `introduced_by = "260915-KS-L12"`, lifetime `permanent`, and
`consumer_scope = "exact"` naming exactly its two consuming modules. Its executable evidence node is
`test_knowledge_evidence_claims.py::test_a_claim_reads_back_with_every_field_including_an_empty_limitations`.
Its permanence rationale is the reason it is shared rather than copied: an evidence claim resolves four
links across two subject kinds and two coverage kinds, so a per-module copy of that topology would let the
two modules disagree about which identity is the facet revision and which is the invariant revision, which
is exactly the property the refusal cases assert. The fixture holds **real bytes** under a temporary root,
because a digest checked against bytes at write time is only meaningful against real bytes.

The route's file-size rail bit here as it has elsewhere: the shared refusal module sat four lines from the
1200-line limit, so this leaf's three refusal factories live in `evidence_refusals.py` beside their own
record group rather than in the shared module — whose own diff is empty.

## Fixture Roles And Claims

`test_agent_notifier.py` and `test_agent_notifier_ladder.py` supply row/topology builders. `test_codex_app_server_adapter.py` and `test_codex_adapter_thread_demux.py` supply transport/observation helpers. `test_closeout_queue.py`, `test_closeout_projection_member_helpers.py`, `test_final_codex_models.py`, `test_gate_certification_evidence.py`, `test_memory_citation_fix.py` and `test_observer_projection.py` likewise retain shared setup rather than their former standalone matrices.

**The citation fixtures now build real Git provenance (260831-LOCR-L33).** The continuity rule the
leaf introduced — a tree-wide relocation is admitted only when no cited file survives and the anchor
existed in a cited file at the document's `lastVerifiedCommitHash` with the same extent kind — is
only expressible against a real repository, so `test_memory_citation_fix.py`'s shared `Tree` gained
`history()`, `stamp()` and `remove_source()`, and its `document()`/`card()` accept a `stamp` that
lands a `lastVerifiedCommitHash` row **inside** the metadata table (never below the citation header,
where it would parse as another claim). `Tree.row()` locates a citation row by its table header
rather than a fixed index, so card metadata cannot shift it. `test_citation_document_transaction.py`'s
`Scenario` carries the same stamp and its fixture commits the verified tree before deleting both
cited files; the TypeScript move fixtures in `test_memory_citation_grammars.py` and the
`_two_failing_cards` helper in `test_memory_citation_fix_scopes.py` were given provenance the same
way. The previously pinned relocation tests therefore still test the legitimate kind-preserving move
instead of having their expectations relaxed, and `test_memory_citation_resolution.py` adds
`MechanicallyProjectedRangeTests`, which pins that a range written by the mechanical projection is
surfaced with the support question rather than an assertion that the citation is current.

Preserve useful shared fixtures only for real consumers. Fake inspectors, synthetic profile inputs, hand-built report payloads and pending finalizers must stay labeled as such. A source-range citation proves the described assertion exists; only a retained execution record proves it ran. Whole-master review and aggregation must assess actual protection rather than historical test names or counts.

## Isolation And Collection

Root test conftest sets candidate imports and disposable home/config/data/cache paths, removes inherited credentials and live-provider opt-ins, and restores owned global state. Ordinary units do not automatically bootstrap application composition; tests request `worktree_services` when that boundary matters. Integration-only modules are skipped before import during unit runs. Collection budgets inspect already selected items without nested pytest or a second repository scan.

## Deliberate Test Inventory Reduction

The test route was reduced on purpose, and a card that cites a name which no longer exists is
evidence of that reduction, not evidence of a lost or damaged file. Commit `d3610903` ("Reduce test
inventory and make coverage diagnostic", 2026-09-06) is the large one: 594 files changed, 604
insertions against 235,366 deletions, stating that it reduced Python test/support code by 79% and
that it replaced coverage floors with collected-case budgets. Four later cuts removed specific
named surface as well: `173bb01e` (2026-09-10) deleted the detached lifecycle worker and drove every
fixture onto the synchronous path; `b06b3a27` (2026-09-10) removed the master route-review gate that
integration never consulted, under an explicit developer ruling that quality is checked focused
within the leaves; `6982c6a7` (2026-09-10) cut the door-operation-journal plane and deleted the
`closeout_door` tool entry point; and `2ec5d244` (2026-09-11) deleted the tests its own remaining
failures exposed as dead. Recover a deletion's cause with `git log -S '<symbol>' -- mcp/tests` (or
`git log --diff-filter=D -- mcp/tests`) before treating a missing test name as an accident. A
shrinking coverage table therefore belongs in the card as recorded negative knowledge, with the
removing commit where it can be proven, and never as a silently shorter list.

## Historical Context

The original milestone narratives documented substantially larger cohorts. Their counts, deleted symbols, source-pinning assertions and percentage-driven repair obligations are retired as current guidance. Relevant incident reasoning survives in the retained cards and source comments. The preserved history below records what earlier waves did without instructing future agents to reconstruct those waves.
## Development And Certification Policy

Ordinary Python development is supported directly through `mcp/.venv/bin/python -m pytest`; four workers run the isolated unit population. `-m integration` selects the small real-boundary population and `-m ""` selects both. Focused file/node execution, including serial debugging, is valid development work and does not acquire certification authority. The repository declares budgets of 1,100 unit and 300 integration parametrized collected cases (the integration ceiling was raised from 200 to 250 by 260831-LOCR-L37 and from 250 to 300, with the unit ceiling 1,000 -> 1,100, by 260831-LOCR-L24 on the explicit developer tradeoff recorded in `pyproject.toml`, so any earlier 150, 200 or 250 figure in this card's history is stale). Extend or consolidate distinct behavior protection before adding cases; do not restore deleted matrices, private-branch tests or unused fixture machinery because an old milestone names them.

Coverage, including changed-line coverage, is diagnostic only. No percentage floor requires additional tests. Production-only CRAP retains 20 as a review trigger, not a delivery blocker; tests and verification support are excluded. Lint, formatting, typing, structural rules and test failures still enforce. Diagnostic-tool execution errors remain visible failures distinct from metric findings. There is no coverage baseline, score-exception registry or ratchet.

Only genuine Dagger admission and the existing lifecycle owners can issue immutable candidate-bound certifying evidence. A host pytest pass, copied report, green helper result or use of Dagger alone is insufficient. Reuse the existing shared engine and preserve process identity, disposable state, credential isolation, exact candidate and publication ownership. Full-suite execution and whole-master independent review belong to the master aggregation boundary under the current execution policy; this overview does not impose either on every leaf. Focused development evidence remains useful without pretending to be final acceptance.
## Memory Preparation And Final Certification

Memory quality is useful before gate admission: a contract-scoped full request observes the exact code/memory pair and candidate trees, runs quality checks, and builds an enclosure-local curator worklist covering repair findings, commit-owned findings, missing onboarding, stale route indexes and source drift. Use that worklist to perform the authorized semantic onboarding updates before entering the expensive certification sequence. It is not necessary to obtain code-gate certificates merely to discover the memory work.

Preparation does not grant a final certificate. The interactive catalog projection explicitly lacks affected-closure and code-prefix authority. The existing prepared-memory adapter consumes the selected four original code terminals and exact prepared candidate, runs the final memory producer, publishes its physical result and selects Gate 5 through the normal owner. Finalization requires that selected original fifth certificate and its bound memory inputs. MCAR continues from these existing owners; this overview does not declare the unfinished master accepted or create a second final proof path.

Candidate capture uses an isolated add-all index and stable observed HEAD, leaving the user's real index unchanged. External-memory identity binds configured repositories, worktree roots, branches, bases, onboarding root and contract digest; the cache path is informational. A changed pair or candidate must refuse stale publication. Metadata stamping and cache refresh cannot substitute for substantive memory repair.

The frozen L38 candidate added two registered integration checks to the retained population; the two L38 integration cards above describe admission/status projection and route-review transport. The current manifest records 224 test-shaped modules: 130 unit-regression, 2 public-contract, 62 integration, 17 architecture-fitness and 13 provider-conformance, with stress-durability and migration empty (the landed master added 260831-LOCR-L06's `test_lifecycle_owned_completion_relay_reviewer.py` to unit-regression at entry row 68 and this leaf adds `test_serving_notifier_handoff.py` to that lane at entry row 98, so both insertions moved every later manifest line; 260831-LOCR-L17 had added `test_terminal_observer_health.py` to that lane at entry row 122, now row 124) (260831-LOCR-L32 added one integration member — `test_worktree_status_terminal_next_tool.py` — 260831-LOCR-L34 added `test_checkpoint_landing_end_to_end.py`, 260831-LOCR-L36 added `test_cross_master_concurrency.py`, 260831-LOCR-L37 added two: `test_pause_stop_only_end_to_end.py` to integration and `test_pause_is_not_publication.py` to architecture-fitness, and the 260831-LOCR seal-removal change set added `test_lifecycle_playthrough_end_to_end.py` to integration; the declared collected-case budgets are 1,100 unit and 300 integration, the integration ceiling having been raised from 200 by L37 and to 300 by L24 with the explicit tradeoff block in `pyproject.toml`). That population was repaired, not merely recounted. The authorized repair restored three CCR landing-debt registrations that commit `8885939e` created but omitted from this manifest (`test_review_state.py`, `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py`), all three in `unit-regression`: those modules previously ran unmarked, and the integration lane sits at its 200-collected-case cap, so an `integration` row for them pushed full-suite collection past the cap and failed collection. The same cap reason moved this route's own `test_terminal_liveness_deferred_work.py` row from integration to `unit-regression`; the module is hermetic. The remaining new unit-regression row is the parked-external-await separation guard in the route table above. Every restored module already had its file card. Membership remains selection and cost classification only; it is not execution or acceptance evidence, and it does not restore any retired matrix.

**Superseded counts (260913-LCA-L5 curator, measured at the current change set):** the sentence above records the
pre-L4 population. The manifest now holds 204 modules on disk and 204 entries — 115 unit-regression,
2 public-contract, 58 integration, 16 architecture-fitness, 13 provider-conformance, with
stress-durability and migration empty — the growth being L4's `test_memory_attribution_producers.py`
(row 68, unit-regression) and L5's `test_leaf_doc_master_link_binding.py` (row 152, integration). The
`test-evidence-lanes.toml` card carries the per-lane brackets and is the owner of record.d it does not restore any retired matrix.

**Current counts (260913-LCA-L7 curator, measured at the current change set):** the L5 paragraph
above is superseded. The manifest now holds 205 modules on disk and 205 entries — 115
unit-regression (entry rows 5-120), 2 public-contract (122-124), 59 integration (126-185), 16
architecture-fitness (187-203), 13 provider-conformance (205-218), with stress-durability and
migration empty. The single addition is this leaf's `test_closeout_projection_source_classification.py`,
registered in the **integration** lane at row 137 by the same change set that created it: it composes
the real `QueueFixture` over temporary Git repositories and drives the production graph admission and
projection path, so that is its behaviour-preserving lane. The `test-evidence-lanes.toml` card owns the
per-lane brackets; membership is selection and cost classification only, never execution or
acceptance evidence.

**Current counts (260913-LCA-L8 curator, measured at the current change set):** the L7 paragraph
above is superseded. The manifest now holds 206 modules on disk and 206 entries — 115 unit-regression
(entry rows 5-120), 2 public-contract (122-124), 60 integration (126-186), 16 architecture-fitness
(188-204), 13 provider-conformance (206-219), with stress-durability and migration empty. The single
addition is this leaf's `test_terminal_blocker_reasons.py`, registered in the **integration** lane at
entry row 177 by the same change set that created it: it drives the public landing, integration and
`lifecycle_finalize_task` routes over real temporary repositories and worktrees, so that is its
behaviour-preserving lane. The `test-evidence-lanes.toml` card owns the per-lane brackets;
membership is selection and cost classification only, never execution or acceptance evidence.

**Current counts (260831-LOCR-L23 curator, measured at the current change set):** the L8 paragraph
above is superseded. The manifest now holds 208 modules on disk and 208 entries — 117 unit-regression
(entry rows 5-122), 2 public-contract (123-126), 60 integration (127-188), 16 architecture-fitness
(189-206), 13 provider-conformance (207-221), with stress-durability (222-223) and migration (224-225)
empty. The single addition is this leaf's `test_terminal_liveness_registration_order.py`, registered in
the **unit-regression** lane at entry row 118 by the same change set that created it: it drives the
real `TerminalCatalog` over `tempfile` catalogs and the real
`TerminalCatalogLivenessSweeper.refresh` with in-process registrar/compactor doubles and no
`worktree_services`, so it is hermetic and the default unit lane is its behaviour-preserving
classification — the same lane as the sibling `test_terminal_liveness_deferred_work.py` at row 117. The
insertion sits between two alphabetically adjacent rows, so it moved no other entry. The
`test-evidence-lanes.toml` card owns the per-lane brackets; membership is selection and cost
classification only, never execution or acceptance evidence.

260831-LOCR-L30 registered eight more members and, in doing so, repaired a manifest that could not
load. `load_lane_manifest` is fail-closed — it derives the repository's actual test modules and
refuses a manifest that omits one — so the seven tracked modules that declared no lane (one of them,
`test_record_landing.py`, shipped by the immediately preceding leaf) were a hard load failure rather
than a silent default. The leaf's own `test_checkpoint_landing.py` joined them. Detail lives in the
`test-evidence-lanes.toml` card, which is the owner of record for lane membership.

The same leaf's follow-up added three more forcing cases, one per behaviour the checkpoint state had
to teach, and this route gained two new file cards with them:

- `test_post_integration_cleanup_guidance.py::test_a_checkpointed_series_keeps_working_instead_of_being_told_to_integrate`
  — a checkpointed contract projects `worktree-started` + `continue_work` + `worktree_status`, not
  `integration-pending` + `worktree_integrate` (the tool that refuses while the series is open).
- `test_record_landing.py::RecordLandingTests::test_a_checkpointed_series_is_not_upgraded_into_a_reclaimable_integration`
  — the pull-request route reports `already-recorded` for a checkpointed contract and leaves both cells
  as the checkpoint wrote them.
- `test_closeout_kept_rules_pins.py::test_r3_closeout_accepts_the_source_head_a_checkpoint_landed`
  — the ancestry validator accepts the commit a checkpoint recorded as its own landed head, with
  `test_r3_closeout_refuses_when_the_source_branch_moved` still refusing foreign movement.

The latter two modules had no file card before this pass and are now covered
(`test_post_integration_cleanup_guidance.py.md`, `test_closeout_kept_rules_pins.py.md`). All three
cases were proven non-vacuous by temporary production mutation, which is why each is documented as the
assertion set that failed without its fix. Lane membership is unchanged: all three files were already
registered, so no manifest row moved.
The current evidence-lifecycle registry declares both registered consumers in each shared
closeout-input and curator-coherence support row. Registry SHA
`15bea1c01f402c382dad1667dec601313bb8aabfc511bb8cedac66076287606a1` and validator PASS42 are
source/diagnostic evidence only; they do not establish execution or acceptance.
## Public-Surface Inventory Contract

`test_tools.py::PublicSurfaceInventoryTests` (260831-LOCR-L29) is the executor of a
surface-agreement invariant that had none. `server_info` reports `PUBLIC_TOOLS` itself, so the
comparison it made possible was self-referential; `worktree_record_landing` shipped registered by
`mcp/registration/closeout.py`, advertised by FastMCP, and absent from both `PUBLIC_TOOLS` and
`TOOL_RESPONSE_MODELS`, and every existing case stayed green while the tool could not return a
payload.

The two cases register `TOOL_REGISTRARS` against a probe `FastMCP("inventory-probe")` and compare
the live `asyncio.run(server.list_tools())` order to `PUBLIC_TOOLS`, then drive one
`finalize_tool_response("worktree_record_landing", ...)` call so a missing registry row fails here
rather than at a caller. `_permissive_registration_config()` only has to satisfy registrars that
close over the config without reading it during registration, so these cases stay about the
inventory rather than about building a runtime; the probe is hermetic and reaches no network.

`test_worktree_status_terminal_next_tool.py` (260831-LOCR-L32) is the same shape of executor one layer
down: the *advertised vocabulary of one surface* had no enforcement. `PUBLIC_TOOLS` moved from
`mcp/tools/base.py` to the zero-import `models` leaf `models/tools/public_roster.py`
cit:([`PUBLIC_TOOLS`], mcp/src/agents_remember/models/tools/public_roster.py:22-86) so that
`models/worktree.py::WorktreeCommandResponse` could read it, declare `nextAction` / `nextTool` /
`nextArgs`
cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:323-323), and refuse a `nextTool` outside the roster
(`_require_registered_public_next_tool`
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:354-365)). Before that the envelope was `extra="allow"` and
declared none of the keys, so `application/worktree_status.py::_project_terminal_contract_status`'s
write crossed the wire verbatim and unchecked. The suite reaches the real `terminal-archive-ready`
state for both `worktree_cleanup` and `worktree_abandon`, binds the emitted args against the real
builder signature, and pins the validator in both directions — including that the registered but
non-public `session_retire` is refused on the worktree surface while the `task_doc` surface still
accepts it. That branch had **zero** coverage before this module.

## Historical milestone context: Checkpoint Landing Plan/Apply Parity

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

`test_checkpoint_landing_end_to_end.py` (260831-LOCR-L34) is the boundary executor for the rule the
leaf is really about: **a preview that plans an operation does not enforce it, and the two surfaces
must be maintained as one.** The seam-level checkpoint suite proved each gate in isolation; this
module drives the registered public operations over one real temporary Git world per case and asserts
that the pair agrees.

It is deliberately not a duplicate of the seam suite:

- it starts from the state the deadlock made unreachable — a master whose `closeout_status` is still
  `not-started`, asserted rather than fabricated — and verifies both destination refs and the ledger
  mapping after a successful checkpoint, so the route is proven reachable end to end rather than only
  eligible;
- it exercises refusal parity by iterating `(dry_run=True, dry_run=False)` for each divergent ledger
  and asserting the same refusal text and the same unmoved refs on both surfaces, which is what
  catches a preview and an apply implemented separately;
- it drives the **public** `worktree_checkpoint_landing_tool` and the public closeout preview/apply
  tools, because the original defect lived in the tool surface a caller actually reaches.

The invariant, its full instance inventory (five fixed, two reported-not-fixed, one adjacent
verdict/state-string shape) and the reasons for each disposition are recorded on the
`worktrees/overview.md` route and summarized in `memory_quality/overview.md`. The module also carries
the only recorded `UNREPRODUCED FLAKE` of this leaf — seen once on a mutated build, never on the real
tree — documented on its own card.

## Historical milestone context: 260913-LCA-L2 Ledger Attribution Coverage

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

The ledger's source became the memory commits' own `Code-Commit:` attribution, and this route carries
the proof for both halves of that sentence.

`test_memory_ledger.py` grew a second fixture world and ten cases. `_AttributedWorld` builds a line
where each mapping is two commits — the content commit carrying the trailer and the ledger commit
pinning the row into `memory.md` and carrying none — with one code commit attributed twice (the
superseding pair the ledger keeps both copies of) and one memory commit carrying no trailer. The
closed-loop case asserts the projection equals the rows the tracked table carried at **every**
checkpoint of that line; the hand-edit case writes a row into the table under a matching header and
asserts the projection does not move; the remaining cases cover the pre-trailer blob fallback, the
bootstrap source that contributes no rows, `exclude` selecting a branch's own commits, the
last-block-wins parse that ignores a body mention, the trailer naming a commit the code repository
lacks, a multi-trailer final block read by key, a mapping that arrived through a merge, and the round
trip that proves the writer's key and the reader's key are one key. The six pre-existing projection
cases in the same file still hold because they reach the reader through the per-commit blob fallback,
which is why that fallback cannot be removed without losing their rows.

**The literal `Code-Commit` text in these test modules is a deliberate independent oracle.** A case
that read `CODE_COMMIT_TRAILER_KEY` would follow a wrong constant instead of catching it, so the
trailer-parse and trailer-round-trip cases spell the key out and must not be "corrected" to import the
constant. The one case that does touch the constant —
`test_the_rendered_trailer_is_the_one_the_reader_parses` — uses it to prove the *writer* renders the
key the reader parses, and proves it through a real commit rather than by comparing two literals.

`test_worktree_sync.py` gained the suite's first coverage of the mid-cycle refusal: a code tip the
official memory line does not map returns `blocked` with `official line is mid-cycle`, leaves the work
branch at its pre-sync head, and syncs once the pair is completed. That refusal is produced by the
**named-ref** ledger read in `sync_transaction_authority.preflight_official_pair`, not by the
projected source ledger, so the case is the regression guard that this leaf's reader change left the
detection where it was.

## Historical milestone context: 260913-LCA-L4 Producer Census And The One Renderer

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

`test_memory_attribution_producers.py` is the leaf's new module and the census that makes the trailer
transition total. A memory commit with no `Code-Commit:` trailer contributes no ledger row, and the
projected ledger cannot tell that apart from a producer that kept the old shape, so the surface is either
complete or silently holey. The module holds five cases: a one-definition census (the key identifier and
its interpolation appear in exactly one production module, and no module spells the trailer as a quoted
literal), a producer census (five producers, each asserted to reach a shared renderer entry), a dialect
case (a hostile multi-paragraph body survives byte for byte with the trailer as its own final block), and
two end-to-end cases driving the public `memory_carryover_apply` and `memory_baseline_adopt` on real
disposable repositories.

The census is measured at base `5bb124d4` and **corrects** the master's 2026-09-13T22:05 decision in two
places: `worktrees/queue/closeout_recovery.py:209` is the recovery route's CODE leg, not a producer, and
the producer the first census missed is `preparation/memory_output.py:92`. The corrected result is 5
memory-content producers and 0 untrailered — `closeout_external.py:165`,
`direct_landing_execution.py:270`, `preparation/memory_output.py:92` (memory-content leg only),
`carryover.py:846`, `baseline.py:210` — with every trailerless site carrying a recorded reason: each
ledger leg, `closeout_recovery.py:209` as a code commit, `sync_transaction_git.py:304`/`:333` memory merge
commits (two memory parents, no single code commit to name), and carryover's nothing-to-carry path, which
creates no commit.

Two durable rules the module enforces from source: the trailer key is declared once and must never be
spelled as a quoted literal in a second production module, and the trailer is **appended as its own final
block** rather than woven into the caller's body — because carryover and baseline take that body as a
public argument of another tool and a caller may pass a multi-paragraph message whose last paragraph is
itself `Key: value` lines.

`test_transaction_only_worktree_delivery.py` gained the behavioural half for the route that has no memory
commit site of its own: `test_closeout_recovery_attributes_the_memory_commit_it_still_owed` interrupts a
real public closeout after its code commit, resumes it through the journalled recovery cell (a wrong cell
is asserted to refuse first), and reads both documented git readers against the resumed shas. The leaf
also moved one import in `test_memory_ledger.py` — `CODE_COMMIT_TRAILER_KEY` now comes from
`kernel.memory_attribution`, because the writing model stopped naming it — and registered the new module
as an exact consumer of two shared-support artifacts in `mcp/tests/evidence-lifecycle.toml`; no case and
no assertion in `test_memory_ledger.py` changed.

## 260913-LCA-L5 Leaf Master-Link Binding, And The Fixture Correction It Forced

The change set's new module is `test_leaf_doc_master_link_binding.py` (integration lane, row 152): the
derived master link proven end to end, plus the fail-closed half — a leaf under a task root with no master
document is refused with its remedy. Its focused decision-table half is the new
`LeafDocMasterLinkBindingTests` class in `test_task_document_application_1.py`.

**One test was removed and must not be restored as it stood.**
`test_task_document_application_1.py`'s `test_create_writes_both_files` authored a bare leaf through
`task_doc` under a task root with no master document; the authoring plane now refuses exactly that
scenario, because nothing would ever bind the leaf's derived `seriesContractPath`/`enclosures[]`. The
file-write behavior it asserted survives in `test_leaf_create_syncs_parent_master_row` and in the new
end-to-end module.

Four existing test modules gained a prerequisite the refusal made mandatory, and each is a fixture
correction rather than a weakened assertion:

- `test_task_document.py` — shared `ApplicationTests._create` now ensures a parent master exists
  (`_ensure_parent_master`), keeping every leaf operation on the flow the plane allows.
- `test_task_doc_review_public.py` — `_create` writes the task root's master document first, because the
  review API is exercised on a leaf.
- `test_closeout_queue.py` — `_leaf` now binds `seriesContractPath` alongside `enclosures[]`.
- `test_transaction_only_worktree_delivery.py` — `_bind_task_without_review` does the same.

The last two are the load-bearing part, and they are why the fixture change is not cosmetic: a leaf
document with an exact enclosure address but no `seriesContractPath` now **refuses closeout by name**
(`task-enclosure-binding-master-link-missing`, raised by `worktrees/task_leaf_binding.py`) where it
previously read as `present` and passed silently. Those two fixtures had been modelling the damage state
that a start repairs, so four unrelated closeout cases began refusing until they carried the field
`task_doc` actually stamps. That is an intended consequence of the change, not an accident.

Lane membership was reconciled against the current manifest in the same change set: 204 modules on disk
and 204 manifest entries, 115 unit-regression, 2 public-contract, 58 integration, 16 architecture-fitness
and 13 provider-conformance, with stress-durability and migration empty. `load_lane_manifest` stays
fail-closed, and both new-module rows (the L4 census and this leaf's binding suite) exist, so the
manifest loads. Detail lives on the `test-evidence-lanes.toml` card, the owner of record for lane
membership.

## 260913-LCA-L10 Sub-Task Index Reachability

The projection reads durable task documents written by other, independently versioned processes, so one
of them may carry a field this reader's schema has never heard of. Until this leaf each of the reader's
five parse sites caught `ValueError` and **dropped the whole document**, so a completed leaf written by a
newer build disappeared from `analytics.taskDocuments` and the dashboard's sub-task row rendered as dead
text while unstarted rows stayed live — a version skew that presented as a status filter. The read edge
now tolerates exactly that skew (purely `extra_forbidden` keys pruned and re-validated) and nothing else.
Authoring did not move: `write_task_doc` still takes a validated `TaskDocument`, so it must refuse such a
document.

`test_task_documents_graph_projection.py` carries the behavioural proof. Its new
`SubTaskIndexReachabilityTests::test_completed_leaf_written_by_another_build_stays_reachable_from_the_index`
builds one master with three rows over a temporary task root, republishes the completed leaf's durable
JSON with an unknown field at the step level, writes a second document with a required field deleted, and
asserts through `read_task_documents`: the skewed completed row resolves with its real identity and
progress (`("01_DONE", "Completed", 1, 1)`), the unstarted row resolves as before, and the broken row is
`None`. The helper `_index_doc` reproduces the dashboard's own index rule (`sliceForRef`) rather than
approximating it, so the assertion is the property the projection owes an authored row; reverting the
single tolerant condition fails exactly this case.

Two mechanics a future reader must not "fix": the skewed JSON is written with `Path.write_text`, not
`write_task_doc`, precisely because `write_task_doc` must refuse it; and the unknown field is spelled
`checkpoint` on a step, mirroring where the live skew landed (`step.note`, `tasks/document.py:121`)
without depending on a field this reader may later learn. The module gained one case and one helper,
its lane row is unchanged, and no budget moved.

## Historical milestone context: 260913-LCA-L11 The Rebuild Outranks The Ledger File: Three Modules Grew Cases, None Was Added

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

**No new test module and no deleted module.** The change set is seven modified files, three of them
test modules, and this route's module population and lane membership are unchanged. What grew is
coverage of a rule that changed direction.

`test_checkpoint_landing_end_to_end.py` is the behavioural proof and six of its cases were rewritten.
Three changed **direction** and now assert an ACCEPTANCE rather than a refusal — a reordered source
region, a reversed superseding pair, and the interleaved projection on the leaf route — because the
file-preservation rule that refused them is gone. Each keeps its scenario and asserts the landing (the
leaf case by measuring that both destination refs really moved), which is the difference between a
relaxed rule and a rule that stopped running; a case that only asserted the surviving refusal would
read as if the file rule were still in force, and a deleted case would hide the change entirely. The
reversal case is the leaf's central piece of negative knowledge: reversing a superseding pair for one
code commit now lands and **nothing at the landing reports it**, so it carries the hazard in its
docstring and points at the transaction card's record of it as a gap pending a decision.
`test_a_unioned_master_line_still_refuses_a_content_difference` narrowed to the untrue row (the
`dropped`/`duplicated` corruptions are deleted with a comment saying why, and the reorderings are
asserted as landing below the refusal), and
`test_a_hand_edited_master_ledger_is_refused_by_the_preview_and_the_apply` kept its fabricated row
precisely so the refusal is attributed to the new row-truth rule rather than to an earlier gate.

`test_integration_branch_authority.py` carries the clause inventory, and this is where the
removed-and-unwitnessed gaps were closed. The landing's four surviving promises now each have their
own case: the mapping clause (including a table that names the landing's code commit with *different*
memory content), the **conditional** source-ancestry clause with a divergent source line the fixture
asserts is really divergent, row truth against both repositories, and the header. Two shapes the old
rule refused — a dropped source row and a duplicated one — are **asserted as accepted** rather than
deleted, and two new module-level cases drive `_require_true_rows` directly over a minimal contract so
the two row-truth clauses are witnessed without a whole enclosure.

`test_memory_ledger.py` gained the reader's two failure-shaped cases: a source row whose memory commit
the source cannot carry is excluded at the read with its reason and its count instead of vanishing,
and a partially trailered line still reads its pre-rule rows. The second is the reader's second,
independent defect — a 479-row source with one trailered commit read as a ONE-ROW source, which is the
"looks like no attribution exists" failure in its most expensive form. The `_content_commit` helper
exists because a row's memory cell must now name a commit git can resolve.

## Historical milestone context: The Sync Half Of The Ledger Rule And The Mid-Flight Result

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

**The sync half of the same ruling is proved in the transaction.** `test_worktree_sync.py` gained
`test_a_descendant_memory_ledger_that_dropped_a_source_row_is_current`
(`:206-243`): it commits a memory content commit, rewrites `memory.md` so its one row maps the code
base to that newer content commit — the stale-duplicate shape a recomputed table produces — and
asserts the public `sync_result` returns `already-current` with no `dropped parent mapping` text
anywhere in the payload and the memory work branch unmoved. Under the removed rule the source's own
row had to survive in the resolution, which is why that same thirteen-row shape left a correctly
closed master permanently unsyncable. The case is the transaction's regression guard; the
projection's own exclusion reporting stays with `test_memory_ledger.py`.

`test_atomic_series_activation.py` gained `ReconcilingResultTests` (`:231-297`) and two cases that
drive `_reconciling_result`, the reporting boundary the public selecting operation composes, against
a mid-flight `reconciling` record. The first asserts a `synced` pass is **not** reported as success:
return code 2, state `atomic-series-reconciling`, the activation observation attached unchanged, and
a summary naming the master's task-document ref and contract path, its publication time, its
revision, both `worktree_sync` exits, and the pass's own message last. The second uses a `blocked`
refusal and asserts the mid-flight identity is stated **before** the refusal's own words, so the
caller reads the state it must resolve rather than the symptom. Neither addition created a module or
moved a lane: both files already carried their rows.

## 260913-LCA-L8 A Cleanup Blocker Always Names Its Reason

**One new module, no deleted module, no lane moved.** The leaf's new module is
`mcp/tests/test_terminal_blocker_reasons.py`, registered in the **integration** lane at entry row 177
by the same change set that created it.

The defect was an operator-facing contradiction. `lifecycle_finalize_task` on one leaf's enclosure
answered `state: cleanup-blocked` with `blockers: [{"provider": "providerRuntime", "reason": null}]`,
while the same payload proved the terminal archive, reported the providers `torn-down` with their
runtime already removed, and said in its own summary that enclosure deletion may continue. Cleanup
stopped on that blockage anyway, preserved the citation-source index with `terminal-operation-failed`,
and left the leaf un-finalized; an immediate retry reclaimed two worktrees, two branches, the reports
directory and the enclosure root, and finalized the edge. Read from source, the **first call was
wrong**, not a real cause the retry re-observed as resolved: the blocker was constructed in
`worktrees/modules/terminal_validation.py`, where a result dict with no `reason` key became `None` and
the item still counted as blocked, and the only producer able to hand it `{"removed": False}` with no
reason at all was `application/provider_runtime.py::remove_tree`'s post-reclaim "still present"
branch — every other non-removal path already named a reason.

The change makes a reasonless blocker impossible to emit rather than merely unlikely.
`terminal_validation._blocker(component, reason)` is now the only construction path for a terminal
blockage and raises `RuntimeError` naming the component when the reason is missing, blank or not a
string; `_blocked_reason(item)` answers a reasonless or malformed item in operator language
(`no reason reported by the terminal result`, `invalid-result`); and every call site routes through
both. `TerminalResult` and `TerminalExpectation` bundle the outputs with preview-versus-real, which is
also what lets the dry-run path read preflight previews as previews and replaced the five-keyword
builder signature with one bundle argument at every call site; the change set adds no `# noqa` and no
per-file ignore. On the producer side, `remove_tree` sets a non-empty reason on every
`removed: False` result. This adds no teardown capability: a genuinely blocked teardown still blocks,
with its own reason.

The module holds seven cases in two groups. The whole-tool cases build a real landed leaf through the
shared external-memory authority fixture, complete the integration through the public
`worktree_integrate_tool`, and call the public `lifecycle_finalize_task_tool`: the L6 shape — provider
runtime already gone, the port answering `already-absent` — must finalize on the **first** call with
an empty `notRemoved` inventory, both worktrees and the enclosure root really gone and the leaf
document `Completed`; and a real permission failure on the provider-runtime tree must refuse as
`cleanup-blocked` / `blocked` with `remove_tree`'s own `permission denied: ...` reason as its single
blocker, close nothing, and refuse identically on the retry. **The L6 payload is reproduced through
the provider port boundary rather than by triggering the original physical event**: the case
substitutes the teardown answer the port would return, so it pins the decision the tool makes given
that answer. The remaining cases drive the two invariant owners directly — the reasonless
`{"removed": False}`, a blank producer reason, an unnameable reason refused at its own source, the
`remove_tree` result shape, and the post-reclaim branch that could answer silently.

The module is a declared exact consumer of nine `mcp/tests/evidence-lifecycle.toml` artifacts —
`closeout_input_test_support.py` (`:331`), `curator_coherence_test_support.py` (`:391`),
`integration_branch_authority_test_support.py` (`:435`), `repository_profile_test_support.py`
(`:565`), the two `repository_profiles/node` fixture files (`:604`, `:643`),
`gate_certification_test_support.py` (`:955`), `source_selection_test_support.py` (`:1012`) and
`selected_lifecycle_test_support.py` (`:1038`) — and of the ambient-role runner in
`dependency_ownership.py` (`:82`). Consumer declarations are ownership accounting only; they are not
execution or acceptance evidence.

## Historical milestone context: 260913-LCA-L3 The Trailer Backfill's Own Contract

This section preserves the earlier milestone account. Its ledger-commit and cache-validation behavior was superseded by the current two-output Git transaction described above; it is not an instruction for current closeout or integration.

**One new module, no deleted module, one lane row added.** The leaf's new module is
`mcp/tests/test_memory_backfill.py`, registered in the **unit-regression** lane at
`mcp/tests/test-evidence-lanes.toml:69` by the same change set that created it. It declares no
`mcp/tests/evidence-lifecycle.toml` consumer row, and that is correct rather than an omission: its
only imports are the production modules under test plus stdlib, so it reaches no
`consumer_scope = "exact"` shared support artifact. `mcp/tests/test_git_command.py` was migrated
with it — the stalled-command timeout case and the raw-commit stdin case now build
`GitRunnerOptions(...)` instead of passing keyword arguments, which is the only change either case
carries.

The leaf delivers the migration **tool** and its measurements, not a rewritten history, and an
external review found two defects that are now fixed. The pre-fix backfill had been applied on this
master's own memory line, verified, and then **reverted by developer ruling**: rewriting the shared
ancestors renumbered them, so the master's memory line and its super branch shared no common ancestor
and the plane's lineage gate refused everything downstream. The fixed tool has **not** been applied to
any real repository; its evidence is fixtures plus a read-only plan measurement. The backfill is an
explicit step at this master's integration into IAS, and the shared source line `7317108b` still
carries **0** `Code-Commit:` trailers. The worker's re-measurement also replaced the leaf
document's census, and this route records the measured values: 474 tracked rows and 419 distinct code
commits at the shared line are exact, while "104 duplicate rows" is 55 (every one sharing a code sha
with another row and naming a different memory commit), "513 trailers" is 419 at the shared line and
428 at the master's tip, and "10 skips" is 67 and 44 under the superseded vocabulary.

**The first reviewed defect was the selection, and the cases pin the fixed rule from both sides.**
The rule is a decision the code makes and therefore a decision a test has to pin, and it has two
halves: a maximum matching, so no code commit is left unnamed while a memory commit that could have
named it stands empty — code commits offered most-constrained-first, a tie between two equally
constrained claims going to the older row read off the table — and then a fill giving every memory
commit the matching did not reach its own oldest row, because a matching is symmetric and the format
is not. `test_every_recorded_pairing_that_can_be_carried_gets_its_own_trailer` asserts both pairings of
one code commit keep a trailer, which is what the fill exists for;
`test_the_winner_does_not_depend_on_hash_order` swaps two rows in the same table and asserts the
bottom-most row's owner wins in both, which is the defect stated directly; and
`test_a_contested_memory_commit_names_the_oldest_claim_and_reports_the_loss` asserts the loser through
`lost_claims` with its `winner` named and the plan not empty. The skip vocabulary is now closed at five
literals split into holes and declines, and the two declines are asserted apart:
`test_a_declined_row_names_whether_it_is_a_duplicate_or_a_lost_mapping` holds the two tables a single
count cannot tell apart, and only `lost_code_commits` separates a decline that cost nothing from one
that lost a mapping. A plan that lost a mapping is asserted to be non-empty and to carry a different
digest from a plan that did not, because the digest is what an apply is pinned to.

Idempotence is proved twice — the second plan over a migrated line is empty with the branch tip
unmoved, and the rewrite itself replays tree, both identities, both dates and the subject, so a rebuilt
commit differs from its original in its trailer block alone and an untouched commit reproduces its own
object id.

**The acceptance proof changed shape, and that is the second half of the first defect.**
`test_the_trailers_alone_preserve_every_pairing_the_ledger_file_recorded` reads the rewritten tip
through `_ABSENT_LEDGER`, a declared path no commit carries, so the table contributes nothing and the
mapped historical pairings are compared against Git-parsed trailers by set equality — failing if any
carryable pairing is omitted and asserting the one that cannot be carried as a reported loss. The
earlier proof read the table the migration carries forward, and because `read_ledger_source` unions
table rows into trailer rows it proved the table had survived rather than that the trailers preserve
the pairings, which is how 60 omissions passed a green suite.
`test_a_content_bearing_duplicate_that_would_be_dropped_fails_the_proof` reproduces the documented
drop shape against the trailer-only read.

**The second reviewed defect was on the command path, so the command path has its own class.**
`MemoryBackfillCliTests` drives `run` through the same parser the console script builds against a real
leaf contract whose memory work branch is a NAME: a rescue set built from a name and read back as a
hash can never compare equal, so the reviewed code wrote its rescue refs and then refused, and the
retry tripped the existing-ref check on refs its own predecessor had created.
`test_the_cli_applies_a_branch_name_tip_and_survives_its_own_retry` asserts the first apply completes
from a name, moves the branch and leaves the rescue ref on the pre-rewrite tip, and that a second
apply returns 0 having moved neither the ref nor the branch. Every fixture is a throwaway pair of Git
repositories under `tempfile`; nothing here reads or writes the coordination tree, the installed
memory repository, or any shared ref. The module makes no claim that a backfill has been applied to
the real memory repository — that sequencing decision belongs to the master's integration step, not to
this route's evidence.

## 260915-CAPS-L7 The Eve Capsule/Workspace Binding Evidence

This route gained three modules proving the eve capsule/workspace binding seam, split by what each can
actually observe:

- `eve_capsule_test_support.py` — **shared support, not a test module.** It builds a real git repository
  with real `git worktree` checkouts, a real coordination root with a sprint/master/leaf document and an
  enclosure contract, and an authored composition corpus. It is the reason the route's other two modules
  can compare against something the code under test does not feed: the workspace identity is compared
  against `git` itself, the carrier digest is recomputed from disk, the task facts against the fixture's
  own task document. Its frozen role/operation vocabularies are deliberately **spelled rather than
  imported** — a fixture that imported what the compiler enforces could not disagree with it.
- `test_eve_capsule_binding.py` — **unit-regression.** The Python half. Most of its cases assert a
  **named refusal** rather than merely that something raised, because an over-strict verifier that
  refused everything would otherwise pass the whole refusal group.
- `test_eve_capsule_runtime.py` — **integration.** The TypeScript half, which no Python case can observe:
  it executes the **shipped** `eve_runtime/agent/lib/*.ts` under the same Node a launch would pick, with
  a `node:module` loader hook supplying only the eve compiler's `./x.js`-for-`.ts` specifier convention.
  Carrier and launch defects are declared as **data** carrying the exact refusal code they must produce.

Two fixture changes in this route belong to the same seam and are recorded here rather than only in the
individual cards. `eve_adapter_test_support.py` gained `fixture_launch_binding()`, because the launch
path is production even when the transport is a double: it now verifies the carrier and the admitted
worktree before a process would exist, so `test_eve_adapter.py`'s launches take their `cwd` and
environment from a real worktree, commit and carrier instead of hand-written values. And
`eve_fixture_model.py`'s trace gained a **`messages`** key carrying the provider's own view of the
request — the only place the *effective prompt* is observable, which is what makes the live fixture's
"the binding reaches the model" assertion a measurement instead of a restatement.

Whole-seam boundary a reader of this route should carry: the live end-to-end claim is
`live_eve_native_fixture.py`'s two capsule scenarios, which drive the real pinned eve runtime. The
produce side they exercise still has **no production caller**, and wiring one is `CAPS-R15@v1`'s
obligation under an explicit transfer.

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared fixture world the seam's cases are built on, and the one place the produce side is currently called. | `FixtureWorld`; `build_world`; `fixture_carrier_for` | mcp/tests/eve_capsule_test_support.py:396-455; mcp/tests/eve_capsule_test_support.py:457-549; mcp/tests/eve_capsule_test_support.py:565-620 |
| The Python half, whose refusal cases assert a named defect. | `test_launch_verification_refuses_every_declared_defect`; `test_carrier_refuses_a_workspace_scope_that_is_not_its_workspace` | mcp/tests/test_eve_capsule_binding.py:364-395; mcp/tests/test_eve_capsule_binding.py:179-196 |
| The TypeScript half, executing the shipped modules under a real Node. | `RuntimeProbe`; `CarrierDefect`; `test_runtime_verifier_refuses_each_declared_defect` | mcp/tests/test_eve_capsule_runtime.py:58-75; mcp/tests/test_eve_capsule_runtime.py:76-180; mcp/tests/test_eve_capsule_runtime.py:267-288 |
| The launch-binding fixture that makes the adapter suite's launches verifiable. | `fixture_launch_binding` | mcp/tests/eve_adapter_test_support.py:407-436 |
| The trace's effective-prompt key, which the live capsule scenarios assert against. | "the provider's own view of the effective prompt" | mcp/tests/eve_fixture_model.py:63-88 |
| The live end-to-end capsule scenarios, which are the whole-seam proof rather than a unit claim. | `_scenario_capsule_binding`; `_scenario_capsule_execution` | mcp/tests/live_eve_native_fixture.py:1758-1813; mcp/tests/live_eve_native_fixture.py:1680-1757 |
| The lifecycle catalog registration for the shared support module, with its four derived consumers. | "path = \"mcp/tests/eve_capsule_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:1434-1434 |

## 260915-CAPS-L11 `D9`'s Six Historical Modules Register, And The Route Closes Its Own Gap

This route's `D9` residual is **closed**. Six historical test modules had been unregistered in
`mcp/tests/test-evidence-lanes.toml` while the fail-closed loader reported each one by name; L11
registered all six in `unit-regression` — `test_eve_adapter`, `test_eve_protocol`,
`test_role_capsule_admission`, `test_role_capsule_compiler`, `test_role_instruction_corpus`,
`test_task_projection` — and `load_lane_manifest` now returns `LANE-REGISTRY-OK 243 0` with no
unregistered-module finding.

**Two properties make the registration load-bearing rather than decorative, and both are asserted.**
Each of the six carries its own row and **collects** (198 cases under the unit selection, 0 under
`-m integration`), and the seed `S-D9-lane-row-removed` deletes one row and makes the loader
**refuse by name** rather than fall back to a default classification. Rows added by this master's
other leaves are unchanged, and no module was moved between lanes by name.

**The route's lesson, worth keeping because the leaf lost time to it:** a manifest fingerprint must
be **asked of the product**, never rebuilt by hand. An intermediate draft recomputed the digest from
its own rendering — `file:`-prefixed, merged-sorted terms — and produced a self-consistent value
(`bfbd21af…`) that described no artifact; the product's own `LaneManifest.digest` for this candidate
is `61f9fba8…` over 243 files / 0 overrides. Counts and lane dispositions were never in question;
only the fingerprint was.

## Repo-Internal References

These current source and policy ranges establish the development/certification distinction and the
existing memory preparation surfaces. A citation is source evidence, not a recorded test execution.

| Finding | Anchor | Source |
| --- | --- | --- |
| Development commands, budgets, diagnostic metrics and isolation. | `# Python test policy and commands` | docs/design/python-pytest-bootstrap.md:1-50 |
| Certifying publication and accepting consumers. | `# Python Test Evidence Authority` | docs/design/python-test-evidence.md:1-65 |
| Exact contract scope, full check and curator worklist publication. | `_resolve_execution`; `_execute_memory_quality`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality/controller.py:308-328; mcp/src/agents_remember/application/memory_quality/controller.py:331-383; mcp/src/agents_remember/application/memory_quality/controller.py:413-550 |
| Interactive catalog names missing authority without eligibility. | `_attach_final_full_catalog` | mcp/src/agents_remember/application/memory_quality/controller.py:600-636 |
| Final memory adapter requires the selected four-code-terminal prefix. | `PreparedMemoryCertificationAdapter` | mcp/src/agents_remember/application/prepared_certification.py:721-785 |
| Finalization consumes original selected fifth-certificate inputs. | `PreparedCloseoutContinuation` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/continuation.py:20-68 |
| The citation index's exclusion register, its ruled caps and its reported-skip behaviour, defended case by case. | `TheExclusionRegisterIsHonouredFromEachSourceIndependently`; `TheRuledCapsSkipAndReportRatherThanRefuse`; `TheQualitySurfaceCannotBeBricked`; `TheRegisteredCitationSurfaceCarriesTheCallerExcludes`; `TheCapsThatStayAsTheyWere` | mcp/tests/test_citation_index_resilience.py:207-415; mcp/tests/test_citation_index_resilience.py:418-557; mcp/tests/test_citation_index_resilience.py:560-665; mcp/tests/test_citation_index_resilience.py:668-707; mcp/tests/test_citation_index_resilience.py:710-720 |
| The divergence between the register's re-inclusion rule and Git's, measured on both sides. | `test_the_register_admits_a_negated_file_under_an_excluded_directory_where_git_does_not` | mcp/tests/test_citation_index_resilience.py:334-374 |
| The consumer of record for the three new `scripts/e2e_harness` governed artifacts, and the fixture/scenario shape it pins. | `FreshUserFixtureShapeTests`; `FreshUserScenarioContractTests` | mcp/tests/test_fresh_user_harness.py:110-186; mcp/tests/test_fresh_user_harness.py:189-235 |
| The lane rows that admit both L14 modules to the `unit-regression` lane. | "mcp/tests/test_citation_index_resilience.py"; "mcp/tests/test_fresh_user_harness.py" | mcp/tests/test-evidence-lanes.toml:27-27; mcp/tests/test-evidence-lanes.toml:62-69; mcp/tests/test-evidence-lanes.toml:24-31; mcp/tests/test-evidence-lanes.toml:67-67 |
| The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. | "path = \"scripts/e2e_harness/fresh_user_fixture.py\"" | mcp/tests/evidence-lifecycle.toml:1550-1550 |
| The live public-surface inventory contract for the advertised MCP tool tuple. | `PublicSurfaceInventoryTests` | mcp/tests/test_tools.py:220-341 |
| The advertised roster the inventory comparison uses, in its new zero-import `models` leaf. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-86 |
| The worktree surface's declared next move and the membership validator this route's new module pins. | "# The next-move triple, declared here so the worktree surface's guidance is part of"; "def _require_registered_public_next_tool" | mcp/src/agents_remember/models/worktree.py:322-329; mcp/src/agents_remember/models/worktree.py:355-363 |
| The L32 module itself: archive-ready reachability for both cleanup verbs, the declarations, and the validator in both directions. | `test_archive_ready_status_names_the_accepted_cleanup_operation`; `test_next_tool_must_name_a_registered_public_tool` | mcp/tests/test_worktree_status_terminal_next_tool.py:175-219; mcp/tests/test_worktree_status_terminal_next_tool.py:231-244 |
| The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane (row 77 after the KS-L3 insertions). | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:112-112 |
| The contract-scoped activation record: one record per series contract, keyed by the contract fingerprint rather than a source pair. | "def contract_fingerprint("; "def activation_path(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-134; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:137-142 |
| The L36 cross-master forcing module: both masters stay ready, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks nobody, a conflicting or stale publication is refused at the pair, and a master that reconciles with a landed sibling completes through ordinary closeout and final integration. Anchor N is the node whose span is range N. | `test_two_unfinished_masters_share_one_source_pair_and_both_stay_ready`; `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible`; `test_a_conflicting_publication_cannot_overwrite_master_b`; `test_master_a_resumes_reconciles_and_completes_after_master_b_landed`; `test_a_dependent_master_still_waits_for_its_unfinished_predecessor`; `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters` | mcp/tests/test_cross_master_concurrency.py:131-165; mcp/tests/test_cross_master_concurrency.py:409-472; mcp/tests/test_cross_master_concurrency.py:473-508; mcp/tests/test_cross_master_concurrency.py:509-684; mcp/tests/test_cross_master_concurrency.py:722-753; mcp/tests/test_cross_master_concurrency.py:754-847 |
| The L36 lane registration the fail-closed manifest requires (row 154 after the KS-L2 and KS-L3 insertions). | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:216-216 |
| The L37 stop boundary proof: the public pause, the measured world, the eight independently-failing cases and the refusals. Its never-selected case now asserts the already-vacant success rather than a refusal. | `PauseStopsAnAtomicMasterTests`; `_world`; `test_pausing_a_master_moves_no_ref_and_creates_no_commit`; `test_a_paused_master_hands_the_turn_back_with_no_next_call`; `test_pausing_a_master_that_was_never_selected_succeeds_and_writes_nothing` | mcp/tests/test_pause_stop_only_end_to_end.py:84-436; mcp/tests/test_pause_stop_only_end_to_end.py:148-166; mcp/tests/test_pause_stop_only_end_to_end.py:201-232; mcp/tests/test_pause_stop_only_end_to_end.py:234-261; mcp/tests/test_pause_stop_only_end_to_end.py:263-284 |
| The L37 structural half: the pause's import closure is disjoint from every publication module. | `PUBLICATION_MODULES`; `test_the_pause_cannot_reach_any_publication_module` | mcp/tests/test_pause_is_not_publication.py:37-52; mcp/tests/test_pause_is_not_publication.py:165-202 |
| The L37 lane registrations the fail-closed manifest requires, one per new module, with the lane each one landed in — re-read by this leaf's curator against the settled registry, because this leaf's own two lane rows were inserted above them and moved both. | "mcp/tests/test_pause_stop_only_end_to_end.py"; "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:213-213; mcp/tests/test-evidence-lanes.toml:250-250; mcp/tests/test-evidence-lanes.toml:228-235; mcp/tests/test-evidence-lanes.toml:265-272 |
| The ordered lifecycle playthrough that is the regression proof for the deleted atomic-series child-admission seal: master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf commanded after the landing still starts. | `LifecyclePlaythroughTests`; `test_the_lifecycle_plays_through_from_an_unstarted_master_to_a_resumed_one` | mcp/tests/test_lifecycle_playthrough_end_to_end.py:62-173; mcp/tests/test_lifecycle_playthrough_end_to_end.py:117-173 |
| The lane registration the fail-closed manifest requires for that module (row 165 after the KS-L2 and KS-L3 insertions). | "mcp/tests/test_lifecycle_playthrough_end_to_end.py"; "mcp/tests/test_pause_stop_only_end_to_end.py"; "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:205-227; mcp/tests/test-evidence-lanes.toml:205-233; mcp/tests/test-evidence-lanes.toml:205-272 |
| The L37 lane registrations the fail-closed manifest requires, one per new module (the pause suite's row at `:162` is unaffected by the later insertions; the AST-only guard's row moved `:193` → `:194` → `:195`). | "mcp/tests/test_lifecycle_playthrough_end_to_end.py"; "mcp/tests/test_pause_stop_only_end_to_end.py"; "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:205-227; mcp/tests/test-evidence-lanes.toml:205-233; mcp/tests/test-evidence-lanes.toml:205-272 |
| The L4 census module's lane row, which closed the gap the L4 route section recorded (row 76 after the KS-L3 insertions). | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:111-111 |
| The L5 binding module's lane registration, added by the same change set that created it (row 162 after the KS-L2 and KS-L3 insertions). | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:226-226 |
| **260913-LCA-L8:** the new module's lane registration, added by the same change set that created it — integration, because it drives the public landing, integration and finalization routes over real temporary repositories and worktrees. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:112-112 |
| The L36 cross-master forcing module: both masters stay ready, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks nobody, a conflicting or stale publication is refused at the pair, and a master that reconciles with a landed sibling completes through ordinary closeout and final integration. | `test_two_unfinished_masters_share_one_source_pair_and_both_stay_ready`; `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible`; `test_a_conflicting_publication_cannot_overwrite_master_b`; `test_master_a_resumes_reconciles_and_completes_after_master_b_landed`; `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters`; `test_a_dependent_master_still_waits_for_its_unfinished_predecessor` | mcp/tests/test_cross_master_concurrency.py:131-162; mcp/tests/test_cross_master_concurrency.py:409-456; mcp/tests/test_cross_master_concurrency.py:473-507; mcp/tests/test_cross_master_concurrency.py:509-568; mcp/tests/test_cross_master_concurrency.py:754-822; mcp/tests/test_cross_master_concurrency.py:722-750 |
| The L36 lane registration the fail-closed manifest requires. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:216-216 |
| The L37 stop boundary proof: the public pause, the measured world, the ten independently-failing cases and the four refusal shapes. Its never-selected case asserts the already-vacant success rather than a refusal, and the two L38 cases added after it pin the unreadable record and the vacant foreign record. | `PauseStopsAnAtomicMasterTests`; `_world`; `test_pausing_a_master_moves_no_ref_and_creates_no_commit`; `test_a_paused_master_hands_the_turn_back_with_no_next_call`; `test_pausing_a_master_that_was_never_selected_succeeds_and_writes_nothing`; `test_an_unreadable_record_is_refused_not_reported_stopped`; `test_a_record_naming_another_master_is_refused_not_released` | mcp/tests/test_pause_stop_only_end_to_end.py:86-556; mcp/tests/test_pause_stop_only_end_to_end.py:150-168; mcp/tests/test_pause_stop_only_end_to_end.py:203-234; mcp/tests/test_pause_stop_only_end_to_end.py:236-263; mcp/tests/test_pause_stop_only_end_to_end.py:265-317; mcp/tests/test_pause_stop_only_end_to_end.py:445-471; mcp/tests/test_pause_stop_only_end_to_end.py:473-526 |
| The lane registration the fail-closed manifest requires for that module. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:229-229 |
| The L4 census module's lane row, which closed the gap the L4 route section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:111-111 |
| The L5 binding module's lane registration, added by the same change set that created it. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:226-226 |
| The L23 registration-order proof: the observed chain with the terminated-row read carrying its own batch-commit state, the partial-proof singleton, the raising registrar that stops the pass, the restart that re-registers and loses nothing, and the fast-path exclusion measured in both directions. | `test_due_sweep_registers_committed_terminated_rows_before_compaction`; `test_partial_registration_compacts_only_the_proven_rows`; `test_registration_failure_prevents_compaction_and_leaves_rows_retryable`; `test_restart_after_registration_before_compaction_reregisters_and_loses_nothing`; `test_starting_fast_path_neither_registers_nor_compacts_while_the_due_sweep_does` | mcp/tests/test_terminal_liveness_registration_order.py:154-246; mcp/tests/test_terminal_liveness_registration_order.py:248-278; mcp/tests/test_terminal_liveness_registration_order.py:280-310; mcp/tests/test_terminal_liveness_registration_order.py:312-358; mcp/tests/test_terminal_liveness_registration_order.py:360-403 |
| The L23 lane registration the fail-closed manifest requires, inserted between two alphabetically adjacent rows so no other entry moved. | "mcp/tests/test_terminal_liveness_registration_order.py" | mcp/tests/test-evidence-lanes.toml:176-176 |
| The L27 pane-authority proof, its fixture import from the sibling sweeper suite, and the lane registration the fail-closed manifest requires. | `PaneDiagnosticAuthorityTests`; `_PANE_AUTHORITY_FIELDS`; `_pane_authority_offenders` | mcp/tests/test_terminal_liveness_pane_authority.py:243-598; mcp/tests/test_terminal_liveness_pane_authority.py:56-69; mcp/tests/test_terminal_liveness_pane_authority.py:233-240; mcp/tests/test-evidence-lanes.toml:188-188 |
| The shared fixtures the L27 module imports instead of rebuilding. | `_Clock`; `_FakeHost`; `_entry`; `_snapshot`; `_ready_snapshot` | mcp/tests/test_terminal_liveness.py:44-104 |
| **260913-LCA-L8:** the new module's lane registration, added by the same change set that created it — integration, because it drives the public landing, integration and finalization routes over real temporary repositories and worktrees. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| The lane registration the fail-closed manifest requires for that module (row 165 after the KS-L2 and KS-L3 insertions). | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:229-229 |
| The L5 binding module's lane registration, added by the same change set that created it (row 162 after the KS-L2 and KS-L3 insertions). | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:226-226 |
| **260913-LCA-L8:** the new module's lane registration, added by the same change set that created it — integration, because it drives the public landing, integration and finalization routes over real temporary repositories and worktrees. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| **260913-LCA-L8:** the L6 shape finalizes on the first call, a real permission failure blocks with its own reason and refuses identically on retry, and the two invariant owners are driven directly. | `test_a_torn_down_provider_runtime_finalizes_on_the_first_call`; `test_a_provider_runtime_that_cannot_be_torn_down_blocks_with_its_own_reason`; `test_a_reasonless_provider_result_is_named_instead_of_becoming_a_null_reason`; `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` | mcp/tests/test_terminal_blocker_reasons.py:116-161; mcp/tests/test_terminal_blocker_reasons.py:164-220; mcp/tests/test_terminal_blocker_reasons.py:223-243; mcp/tests/test_terminal_blocker_reasons.py:246-259 |
| **260913-LCA-L8:** the only construction path for a terminal blockage, and the operator-language answer for a reasonless or malformed result item. | `_blocker`; `_blocked_reason` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:639-655; mcp/src/agents_remember/worktrees/modules/terminal_validation.py:624-636 |
| **260913-LCA-L8:** the producer whose result could answer `removed: False` with no reason, now naming every non-removal. | `remove_tree` | mcp/src/agents_remember/application/provider_runtime.py:289-326 |
| **260913-LCA-L8:** the nine exact-consumer rows the new module's change set adds to the evidence registry. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:112-112 |
| The L36 cross-master forcing module: both masters stay ready, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks nobody, a conflicting or stale publication is refused at the pair, and a master that reconciles with a landed sibling completes through ordinary closeout and final integration. | `test_two_unfinished_masters_share_one_source_pair_and_both_stay_ready`; `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible`; `test_a_conflicting_publication_cannot_overwrite_master_b`; `test_master_a_resumes_reconciles_and_completes_after_master_b_landed`; `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters`; `test_a_dependent_master_still_waits_for_its_unfinished_predecessor` | mcp/tests/test_cross_master_concurrency.py:131-162; mcp/tests/test_cross_master_concurrency.py:409-456; mcp/tests/test_cross_master_concurrency.py:473-507; mcp/tests/test_cross_master_concurrency.py:509-568; mcp/tests/test_cross_master_concurrency.py:754-822; mcp/tests/test_cross_master_concurrency.py:722-750 |
| The L36 lane registration the fail-closed manifest requires. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:216-216 |
| The L37 stop boundary proof: the public pause, the measured world, the ten independently-failing cases and the four refusal shapes. Its never-selected case asserts the already-vacant success rather than a refusal, and the two L38 cases added after it pin the unreadable record and the vacant foreign record. | `PauseStopsAnAtomicMasterTests`; `_world`; `test_pausing_a_master_moves_no_ref_and_creates_no_commit`; `test_a_paused_master_hands_the_turn_back_with_no_next_call`; `test_pausing_a_master_that_was_never_selected_succeeds_and_writes_nothing`; `test_an_unreadable_record_is_refused_not_reported_stopped`; `test_a_record_naming_another_master_is_refused_not_released` | mcp/tests/test_pause_stop_only_end_to_end.py:86-556; mcp/tests/test_pause_stop_only_end_to_end.py:150-168; mcp/tests/test_pause_stop_only_end_to_end.py:203-234; mcp/tests/test_pause_stop_only_end_to_end.py:236-263; mcp/tests/test_pause_stop_only_end_to_end.py:265-317; mcp/tests/test_pause_stop_only_end_to_end.py:445-471; mcp/tests/test_pause_stop_only_end_to_end.py:473-526 |
| The L37 lane registrations the fail-closed manifest requires, one per new module — re-read by this leaf's curator at the settled registry, since the row accumulated several superseded line numbers across the insertions that followed it and only the current pair is the fact. | "mcp/tests/test_pause_stop_only_end_to_end.py"; "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:213-213; mcp/tests/test-evidence-lanes.toml:250-250; mcp/tests/test-evidence-lanes.toml:228-235; mcp/tests/test-evidence-lanes.toml:265-272 |
| The lane registration the fail-closed manifest requires for that module. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:229-229 |
| The L4 census module's lane row, which closed the gap the L4 route section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:111-111 |
| The L5 binding module's lane registration, added by the same change set that created it. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:226-226 |
| The L23 registration-order proof: the observed chain with the terminated-row read carrying its own batch-commit state, the partial-proof singleton, the raising registrar that stops the pass, the restart that re-registers and loses nothing, and the fast-path exclusion measured in both directions. | `test_due_sweep_registers_committed_terminated_rows_before_compaction`; `test_partial_registration_compacts_only_the_proven_rows`; `test_registration_failure_prevents_compaction_and_leaves_rows_retryable`; `test_restart_after_registration_before_compaction_reregisters_and_loses_nothing`; `test_starting_fast_path_neither_registers_nor_compacts_while_the_due_sweep_does` | mcp/tests/test_terminal_liveness_registration_order.py:154-246; mcp/tests/test_terminal_liveness_registration_order.py:248-278; mcp/tests/test_terminal_liveness_registration_order.py:280-310; mcp/tests/test_terminal_liveness_registration_order.py:312-358; mcp/tests/test_terminal_liveness_registration_order.py:360-403 |
| The L23 lane registration the fail-closed manifest requires, inserted between two alphabetically adjacent rows so no other entry moved. | "mcp/tests/test_terminal_liveness_registration_order.py" | mcp/tests/test-evidence-lanes.toml:176-176 |
| The L27 pane-authority proof and its fixture import from the sibling sweeper suite. | `PaneDiagnosticAuthorityTests`; `_PANE_AUTHORITY_FIELDS`; `_pane_authority_offenders` | mcp/tests/test_terminal_liveness_pane_authority.py:243-598; mcp/tests/test_terminal_liveness_pane_authority.py:56-69; mcp/tests/test_terminal_liveness_pane_authority.py:233-240 |
| The architecture-fitness lane registration the fail-closed manifest requires for that proof. | "mcp/tests/test_terminal_liveness_pane_authority.py" | mcp/tests/test-evidence-lanes.toml:253-253 |
| The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane (row 77 after the KS-L3 insertions). | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:112-112 |
| The contract-scoped activation record: one record per series contract, keyed by the contract fingerprint rather than a source pair. | "def contract_fingerprint("; "def activation_path(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-134; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:137-142 |
| The L36 cross-master forcing module: both masters stay ready, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks nobody, a conflicting or stale publication is refused at the pair, and a master that reconciles with a landed sibling completes through ordinary closeout and final integration. Anchor N is the node whose span is range N. | `test_two_unfinished_masters_share_one_source_pair_and_both_stay_ready`; `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible`; `test_a_conflicting_publication_cannot_overwrite_master_b`; `test_master_a_resumes_reconciles_and_completes_after_master_b_landed`; `test_a_dependent_master_still_waits_for_its_unfinished_predecessor`; `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters` | mcp/tests/test_cross_master_concurrency.py:131-165; mcp/tests/test_cross_master_concurrency.py:409-472; mcp/tests/test_cross_master_concurrency.py:473-508; mcp/tests/test_cross_master_concurrency.py:509-684; mcp/tests/test_cross_master_concurrency.py:722-753; mcp/tests/test_cross_master_concurrency.py:754-847 |
| The L36 lane registration the fail-closed manifest requires (row 154 after the KS-L2 and KS-L3 insertions). | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:216-216 |
| The L37 stop boundary proof: the public pause, the measured world, the eight independently-failing cases and the refusals. Its never-selected case now asserts the already-vacant success rather than a refusal. | `PauseStopsAnAtomicMasterTests`; `_world`; `test_pausing_a_master_moves_no_ref_and_creates_no_commit`; `test_a_paused_master_hands_the_turn_back_with_no_next_call`; `test_pausing_a_master_that_was_never_selected_succeeds_and_writes_nothing` | mcp/tests/test_pause_stop_only_end_to_end.py:84-436; mcp/tests/test_pause_stop_only_end_to_end.py:148-166; mcp/tests/test_pause_stop_only_end_to_end.py:201-232; mcp/tests/test_pause_stop_only_end_to_end.py:234-261; mcp/tests/test_pause_stop_only_end_to_end.py:263-284 |
| The L37 structural half: the pause's import closure is disjoint from every publication module. | `PUBLICATION_MODULES`; `test_the_pause_cannot_reach_any_publication_module` | mcp/tests/test_pause_is_not_publication.py:37-52; mcp/tests/test_pause_is_not_publication.py:165-202 |
| The L37 lane registrations the fail-closed manifest requires, one per new module (both rows moved again with the KS-L2 and KS-L3 insertions: the pause suite to row 171 and the AST-only guard to row 204); **the current pair is the pause suite at `:204` in `integration` and the AST-only guard at `:240` in `architecture-fitness`.** | "mcp/tests/test_pause_stop_only_end_to_end.py"; "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:204-211; mcp/tests/test-evidence-lanes.toml:240-240; mcp/tests/test-evidence-lanes.toml:246-248; mcp/tests/test-evidence-lanes.toml:209-211; mcp/tests/test-evidence-lanes.toml:211-211; mcp/tests/test-evidence-lanes.toml:228-235; mcp/tests/test-evidence-lanes.toml:265-272 |
| The ordered lifecycle playthrough that is the regression proof for the deleted atomic-series child-admission seal: master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf commanded after the landing still starts. | `LifecyclePlaythroughTests`; `test_the_lifecycle_plays_through_from_an_unstarted_master_to_a_resumed_one` | mcp/tests/test_lifecycle_playthrough_end_to_end.py:62-173; mcp/tests/test_lifecycle_playthrough_end_to_end.py:117-173 |
| The lane registration the fail-closed manifest requires for that module (row 165 after the KS-L2 and KS-L3 insertions). | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:229-229 |
| The L4 census module's lane row, which closed the gap the L4 route section recorded (row 76 after the KS-L3 insertions). | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:111-111 |
| The L5 binding module's lane registration, added by the same change set that created it (row 162 after the KS-L2 and KS-L3 insertions). | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:226-226 |
| **260913-LCA-L8:** the new module's lane registration, added by the same change set that created it — integration, because it drives the public landing, integration and finalization routes over real temporary repositories and worktrees. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| **260913-LCA-L8:** the L6 shape finalizes on the first call, a real permission failure blocks with its own reason and refuses identically on retry, and the two invariant owners are driven directly. | `test_a_torn_down_provider_runtime_finalizes_on_the_first_call`; `test_a_provider_runtime_that_cannot_be_torn_down_blocks_with_its_own_reason`; `test_a_reasonless_provider_result_is_named_instead_of_becoming_a_null_reason`; `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` | mcp/tests/test_terminal_blocker_reasons.py:116-161; mcp/tests/test_terminal_blocker_reasons.py:164-220; mcp/tests/test_terminal_blocker_reasons.py:223-243; mcp/tests/test_terminal_blocker_reasons.py:246-259 |
| **260913-LCA-L8:** the only construction path for a terminal blockage, and the operator-language answer for a reasonless or malformed result item. | `_blocker`; `_blocked_reason` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:639-655; mcp/src/agents_remember/worktrees/modules/terminal_validation.py:624-636 |
| **260913-LCA-L8:** the producer whose result could answer `removed: False` with no reason, now naming every non-removal. | `remove_tree` | mcp/src/agents_remember/application/provider_runtime.py:289-326 |
| **260913-LCA-L8:** the nine exact-consumer rows the new module's change set adds to the evidence registry. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:112-112 |
| The L36 cross-master forcing module: both masters stay ready, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks nobody, a conflicting or stale publication is refused at the pair, and a master that reconciles with a landed sibling completes through ordinary closeout and final integration. | `test_two_unfinished_masters_share_one_source_pair_and_both_stay_ready`; `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible`; `test_a_conflicting_publication_cannot_overwrite_master_b`; `test_master_a_resumes_reconciles_and_completes_after_master_b_landed`; `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters`; `test_a_dependent_master_still_waits_for_its_unfinished_predecessor` | mcp/tests/test_cross_master_concurrency.py:131-162; mcp/tests/test_cross_master_concurrency.py:409-456; mcp/tests/test_cross_master_concurrency.py:473-507; mcp/tests/test_cross_master_concurrency.py:509-568; mcp/tests/test_cross_master_concurrency.py:754-822; mcp/tests/test_cross_master_concurrency.py:722-750 |
| The L36 lane registration the fail-closed manifest requires. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:216-216 |
| The L37 stop boundary proof: the public pause, the measured world, the ten independently-failing cases and the four refusal shapes. Its never-selected case asserts the already-vacant success rather than a refusal, and the two L38 cases added after it pin the unreadable record and the vacant foreign record. | `PauseStopsAnAtomicMasterTests`; `_world`; `test_pausing_a_master_moves_no_ref_and_creates_no_commit`; `test_a_paused_master_hands_the_turn_back_with_no_next_call`; `test_pausing_a_master_that_was_never_selected_succeeds_and_writes_nothing`; `test_an_unreadable_record_is_refused_not_reported_stopped`; `test_a_record_naming_another_master_is_refused_not_released` | mcp/tests/test_pause_stop_only_end_to_end.py:86-556; mcp/tests/test_pause_stop_only_end_to_end.py:150-168; mcp/tests/test_pause_stop_only_end_to_end.py:203-234; mcp/tests/test_pause_stop_only_end_to_end.py:236-263; mcp/tests/test_pause_stop_only_end_to_end.py:265-317; mcp/tests/test_pause_stop_only_end_to_end.py:445-471; mcp/tests/test_pause_stop_only_end_to_end.py:473-526 |
| The L37 lane registrations the fail-closed manifest requires, one per new module (the pause suite's row at `:162` is unaffected by the later insertions; the AST-only guard's row moved `:193` → `:194` → `:195`); **the current pair is the pause suite at `:204` in `integration` and the AST-only guard at `:240` in `architecture-fitness`.** | "mcp/tests/test_pause_stop_only_end_to_end.py"; "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:204-204; mcp/tests/test-evidence-lanes.toml:240-240; mcp/tests/test-evidence-lanes.toml:246-248; mcp/tests/test-evidence-lanes.toml:209-209; mcp/tests/test-evidence-lanes.toml:211-211; mcp/tests/test-evidence-lanes.toml:228-235; mcp/tests/test-evidence-lanes.toml:265-272 |
| The lane registration the fail-closed manifest requires for that module. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:229-229 |
| The L4 census module's lane row, which closed the gap the L4 route section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:111-111 |
| The L5 binding module's lane registration, added by the same change set that created it. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:226-226 |
| The L23 registration-order proof: the observed chain with the terminated-row read carrying its own batch-commit state, the partial-proof singleton, the raising registrar that stops the pass, the restart that re-registers and loses nothing, and the fast-path exclusion measured in both directions. | `test_due_sweep_registers_committed_terminated_rows_before_compaction`; `test_partial_registration_compacts_only_the_proven_rows`; `test_registration_failure_prevents_compaction_and_leaves_rows_retryable`; `test_restart_after_registration_before_compaction_reregisters_and_loses_nothing`; `test_starting_fast_path_neither_registers_nor_compacts_while_the_due_sweep_does` | mcp/tests/test_terminal_liveness_registration_order.py:154-246; mcp/tests/test_terminal_liveness_registration_order.py:248-278; mcp/tests/test_terminal_liveness_registration_order.py:280-310; mcp/tests/test_terminal_liveness_registration_order.py:312-358; mcp/tests/test_terminal_liveness_registration_order.py:360-403 |
| The L23 lane registration the fail-closed manifest requires, inserted between two alphabetically adjacent rows so no other entry moved. | "mcp/tests/test_terminal_liveness_registration_order.py" | mcp/tests/test-evidence-lanes.toml:176-176 |
|The L27 pane-authority proof, its fixture import from the sibling sweeper suite, and the lane registration the fail-closed manifest requires.|`PaneDiagnosticAuthorityTests` ; `_PANE_AUTHORITY_FIELDS` ; `_pane_authority_offenders`| mcp/tests/test_terminal_liveness_pane_authority.py:243-598; mcp/tests/test_terminal_liveness_pane_authority.py:56-69 |
|The shared fixtures the L27 module imports instead of rebuilding.|`_Clock` ; `_FakeHost` ; `_entry` ; `_snapshot` ; `_ready_snapshot`| mcp/tests/test_terminal_liveness.py:44-104 |
|**260913-LCA-L8:** the exact-consumer rows `mcp/tests/test_terminal_blocker_reasons.py` adds to the evidence registry under the `synthetic-test-evidence-candidate` contract, one per artifact whose consumer list gained it.|"id = \"synthetic-test-evidence-candidate\""| mcp/tests/evidence-lifecycle.toml:20-20 |
| **260913-LCA-L8:** the declaration that gives the new module ownership of the ambient-role runner for targeted selection. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:84-84 |
| The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane (row 77 after the KS-L3 insertions). | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:112-112 |
| The contract-scoped activation record: one record per series contract, keyed by the contract fingerprint rather than a source pair. | "def contract_fingerprint("; "def activation_path(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-134; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:137-142 |
| The L36 cross-master forcing module: both masters stay ready, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks nobody, a conflicting or stale publication is refused at the pair, and a master that reconciles with a landed sibling completes through ordinary closeout and final integration. Anchor N is the node whose span is range N. | `test_two_unfinished_masters_share_one_source_pair_and_both_stay_ready`; `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible`; `test_a_conflicting_publication_cannot_overwrite_master_b`; `test_master_a_resumes_reconciles_and_completes_after_master_b_landed`; `test_a_dependent_master_still_waits_for_its_unfinished_predecessor`; `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters` | mcp/tests/test_cross_master_concurrency.py:131-165; mcp/tests/test_cross_master_concurrency.py:409-472; mcp/tests/test_cross_master_concurrency.py:473-508; mcp/tests/test_cross_master_concurrency.py:509-684; mcp/tests/test_cross_master_concurrency.py:722-753; mcp/tests/test_cross_master_concurrency.py:754-847 |
| The L36 lane registration the fail-closed manifest requires (row 154 after the KS-L2 and KS-L3 insertions). | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:216-216 |
| The L37 stop boundary proof: the public pause, the measured world, the eight independently-failing cases and the refusals. Its never-selected case now asserts the already-vacant success rather than a refusal. | `PauseStopsAnAtomicMasterTests`; `_world`; `test_pausing_a_master_moves_no_ref_and_creates_no_commit`; `test_a_paused_master_hands_the_turn_back_with_no_next_call`; `test_pausing_a_master_that_was_never_selected_succeeds_and_writes_nothing` | mcp/tests/test_pause_stop_only_end_to_end.py:84-436; mcp/tests/test_pause_stop_only_end_to_end.py:148-166; mcp/tests/test_pause_stop_only_end_to_end.py:201-232; mcp/tests/test_pause_stop_only_end_to_end.py:234-261; mcp/tests/test_pause_stop_only_end_to_end.py:263-284 |
| The L37 structural half: the pause's import closure is disjoint from every publication module. | `PUBLICATION_MODULES`; `test_the_pause_cannot_reach_any_publication_module` | mcp/tests/test_pause_is_not_publication.py:37-52; mcp/tests/test_pause_is_not_publication.py:165-202 |
| The L37 lane registrations the fail-closed manifest requires, one per new module (both rows moved again with the KS-L2 and KS-L3 insertions: the pause suite to row 171 and the AST-only guard to row 204). | "mcp/tests/test_pause_stop_only_end_to_end.py"; "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:202-211; mcp/tests/test-evidence-lanes.toml:238-248; mcp/tests/test-evidence-lanes.toml:211-248; mcp/tests/test-evidence-lanes.toml:265-272 |
| The ordered lifecycle playthrough that is the regression proof for the deleted atomic-series child-admission seal: master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf commanded after the landing still starts. | `LifecyclePlaythroughTests`; `test_the_lifecycle_plays_through_from_an_unstarted_master_to_a_resumed_one` | mcp/tests/test_lifecycle_playthrough_end_to_end.py:62-173; mcp/tests/test_lifecycle_playthrough_end_to_end.py:117-173 |
| The lane registration the fail-closed manifest requires for that module (row 165 after the KS-L2 and KS-L3 insertions). | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:229-229 |
| The L4 census module's lane row, which closed the gap the L4 route section recorded (row 76 after the KS-L3 insertions). | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:111-111 |
| The L5 binding module's lane registration, added by the same change set that created it (row 162 after the KS-L2 and KS-L3 insertions). | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:226-226 |
| **260913-LCA-L8:** the new module's lane registration, added by the same change set that created it — integration, because it drives the public landing, integration and finalization routes over real temporary repositories and worktrees. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| **260913-LCA-L8:** the L6 shape finalizes on the first call, a real permission failure blocks with its own reason and refuses identically on retry, and the two invariant owners are driven directly. | `test_a_torn_down_provider_runtime_finalizes_on_the_first_call`; `test_a_provider_runtime_that_cannot_be_torn_down_blocks_with_its_own_reason`; `test_a_reasonless_provider_result_is_named_instead_of_becoming_a_null_reason`; `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` | mcp/tests/test_terminal_blocker_reasons.py:116-161; mcp/tests/test_terminal_blocker_reasons.py:164-220; mcp/tests/test_terminal_blocker_reasons.py:223-243; mcp/tests/test_terminal_blocker_reasons.py:246-259 |
| **260913-LCA-L8:** the only construction path for a terminal blockage, and the operator-language answer for a reasonless or malformed result item. | `_blocker`; `_blocked_reason` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:639-655; mcp/src/agents_remember/worktrees/modules/terminal_validation.py:624-636 |
| **260913-LCA-L8:** the producer whose result could answer `removed: False` with no reason, now naming every non-removal. | `remove_tree` | mcp/src/agents_remember/application/provider_runtime.py:289-326 |
| **260913-LCA-L8:** the nine exact-consumer rows the new module's change set adds to the evidence registry. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:251-251 |
| The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:112-112 |
| The L36 cross-master forcing module: both masters stay ready, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks nobody, a conflicting or stale publication is refused at the pair, and a master that reconciles with a landed sibling completes through ordinary closeout and final integration. | `test_two_unfinished_masters_share_one_source_pair_and_both_stay_ready`; `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible`; `test_a_conflicting_publication_cannot_overwrite_master_b`; `test_master_a_resumes_reconciles_and_completes_after_master_b_landed`; `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters`; `test_a_dependent_master_still_waits_for_its_unfinished_predecessor` | mcp/tests/test_cross_master_concurrency.py:131-162; mcp/tests/test_cross_master_concurrency.py:409-456; mcp/tests/test_cross_master_concurrency.py:473-507; mcp/tests/test_cross_master_concurrency.py:509-568; mcp/tests/test_cross_master_concurrency.py:754-822; mcp/tests/test_cross_master_concurrency.py:722-750 |
| The L36 lane registration the fail-closed manifest requires. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:216-216 |
| The L37 stop boundary proof: the public pause, the measured world, the ten independently-failing cases and the four refusal shapes. Its never-selected case asserts the already-vacant success rather than a refusal, and the two L38 cases added after it pin the unreadable record and the vacant foreign record. | `PauseStopsAnAtomicMasterTests`; `_world`; `test_pausing_a_master_moves_no_ref_and_creates_no_commit`; `test_a_paused_master_hands_the_turn_back_with_no_next_call`; `test_pausing_a_master_that_was_never_selected_succeeds_and_writes_nothing`; `test_an_unreadable_record_is_refused_not_reported_stopped`; `test_a_record_naming_another_master_is_refused_not_released` | mcp/tests/test_pause_stop_only_end_to_end.py:86-556; mcp/tests/test_pause_stop_only_end_to_end.py:150-168; mcp/tests/test_pause_stop_only_end_to_end.py:203-234; mcp/tests/test_pause_stop_only_end_to_end.py:236-263; mcp/tests/test_pause_stop_only_end_to_end.py:265-317; mcp/tests/test_pause_stop_only_end_to_end.py:445-471; mcp/tests/test_pause_stop_only_end_to_end.py:473-526 |
| The L37 lane registrations the fail-closed manifest requires, one per new module (the pause suite's row at `:162` is unaffected by the later insertions; the AST-only guard's row moved `:193` → `:194` → `:195`). | "mcp/tests/test_pause_stop_only_end_to_end.py"; "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:202-211; mcp/tests/test-evidence-lanes.toml:228-248; mcp/tests/test-evidence-lanes.toml:211-211; mcp/tests/test-evidence-lanes.toml:265-272 |
| The lane registration the fail-closed manifest requires for that module. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:229-229 |
| The L4 census module's lane row, which closed the gap the L4 route section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:111-111 |
| The L5 binding module's lane registration, added by the same change set that created it. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:226-226 |
| The L23 registration-order proof: the observed chain with the terminated-row read carrying its own batch-commit state, the partial-proof singleton, the raising registrar that stops the pass, the restart that re-registers and loses nothing, and the fast-path exclusion measured in both directions. | `test_due_sweep_registers_committed_terminated_rows_before_compaction`; `test_partial_registration_compacts_only_the_proven_rows`; `test_registration_failure_prevents_compaction_and_leaves_rows_retryable`; `test_restart_after_registration_before_compaction_reregisters_and_loses_nothing`; `test_starting_fast_path_neither_registers_nor_compacts_while_the_due_sweep_does` | mcp/tests/test_terminal_liveness_registration_order.py:154-246; mcp/tests/test_terminal_liveness_registration_order.py:248-278; mcp/tests/test_terminal_liveness_registration_order.py:280-310; mcp/tests/test_terminal_liveness_registration_order.py:312-358; mcp/tests/test_terminal_liveness_registration_order.py:360-403 |
| The L23 lane registration the fail-closed manifest requires, inserted between two alphabetically adjacent rows so no other entry moved. | "mcp/tests/test_terminal_liveness_registration_order.py" | mcp/tests/test-evidence-lanes.toml:176-176 |
|The L27 pane-authority proof, its fixture import from the sibling sweeper suite, and the lane registration the fail-closed manifest requires.|`PaneDiagnosticAuthorityTests` ; `_PANE_AUTHORITY_FIELDS` ; `_pane_authority_offenders`| mcp/tests/test_terminal_liveness_pane_authority.py:243-598; mcp/tests/test_terminal_liveness_pane_authority.py:56-69 |
|The shared fixtures the L27 module imports instead of rebuilding.|`_Clock` ; `_FakeHost` ; `_entry` ; `_snapshot` ; `_ready_snapshot`| mcp/tests/test_terminal_liveness.py:44-104 |
| **260913-LCA-L8:** the nine exact-consumer rows `mcp/tests/test_terminal_blocker_reasons.py` adds to the evidence registry under the `synthetic-test-evidence-candidate` contract. | "id = \"synthetic-test-evidence-candidate\"" | mcp/tests/evidence-lifecycle.toml:20-20; mcp/tests/evidence-lifecycle.toml:304-304; mcp/tests/evidence-lifecycle.toml:379-379; mcp/tests/evidence-lifecycle.toml:423-423; mcp/tests/evidence-lifecycle.toml:553-553; mcp/tests/evidence-lifecycle.toml:592-592; mcp/tests/evidence-lifecycle.toml:631-631; mcp/tests/evidence-lifecycle.toml:943-943; mcp/tests/evidence-lifecycle.toml:1000-1026; mcp/tests/evidence-lifecycle.toml:1026-1026 |
| **260913-LCA-L8:** the declaration that gives the new module ownership of the ambient-role runner for targeted selection. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:82-157 |
| The removed case's scenario, now refused by design: the guard that makes a task root with no master document unbindable. | `_require_bindable_leaf_authoring` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:619-649 |
| The refusal the two corrected closeout fixtures had to satisfy. | `require_current_leaf_enclosure_binding` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:205-256 |
| **The mid-flight reporting boundary:** a completed pass beside a reconciling selection is not this call's success, and a refusal left beside one leads with the mid-flight state. | `ReconcilingResultTests`; `test_a_completed_pass_beside_a_mid_flight_selection_is_not_success`; `test_a_refusal_that_left_a_record_mid_flight_leads_with_that_state`; `_reconciling_result` | mcp/tests/test_atomic_series_activation.py:231-297; mcp/tests/test_atomic_series_activation.py:255-274; mcp/tests/test_atomic_series_activation.py:276-297; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:280-294 |
| The rewritten contract-scoped activation forcing suite and its shared-source-pair fixture. | `class ActivationFixture`; `test_contracts_sharing_one_source_pair_hold_independent_selection`; `test_another_contracts_record_can_never_be_adopted` | mcp/tests/test_atomic_series_activation.py:63-111; mcp/tests/test_atomic_series_activation.py:122-145; mcp/tests/test_atomic_series_activation.py:179-214 |
| The registered admission refusal now addresses only the addressed contract's own state. | `test_registered_sync_refusal_addresses_only_this_contracts_own_state` | mcp/tests/test_activation_admission_registered.py:178-221 |
| **Row corrected against the current source (L2 curator, 260915-KS-L2):** the L2 mid-cycle *test node* this row cited, `test_a_code_tip_with_no_attributing_memory_commit_refuses_by_name`, **no longer exists in the suite** — a source-wide search finds no such node and no fragment of its name, so the documented coverage is stale and this row no longer claims it. What survives and is cited here is the helper the row also named. A successor that wants to re-establish the refusal-by-name coverage must write the node and re-cite it; a plausible-looking range was deliberately not substituted. | `map_official_memory` | mcp/tests/test_worktree_sync.py:107-108 |

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Public closeout exercises the actual pair, attribution and cache-independent delivery. | `test_public_closeout_commits_code_and_memory_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:211-318 |
| Cache damage cannot change the accepted integration pair or block ref publication. | `test_cache_damage_cannot_change_the_accepted_pair_or_block_its_ref_move` | mcp/tests/test_integration_branch_authority.py:172-213 |
| The migration acceptance proof reads only committed trailers. | `test_the_trailers_alone_preserve_every_pairing_the_ledger_file_recorded` | mcp/tests/test_memory_backfill.py:467-550 |
| Cache damage cannot change the accepted integration pair or block ref publication. | `test_cache_damage_cannot_change_the_accepted_pair_or_block_its_ref_move` | mcp/tests/test_integration_branch_authority.py:172-213 |
| The migration acceptance proof reads only committed trailers. | `test_the_trailers_alone_preserve_every_pairing_the_ledger_file_recorded` | mcp/tests/test_memory_backfill.py:467-550 |

## Docs And Cross-Repo References

No Domain Documentation entries are configured in the resolved memory root. Current local policy and source owners are cited above; no live external system or sibling repository is used to grant authority.

---

## 260915-KS-L19 The Requirement-Revision Suites, Their Lane Rows, And One Re-Scoped Seam Case

This leaf added two test modules and one lane registration each, and re-scoped one shipped facet assertion.

- `test_knowledge_requirement_revisions.py` — **17 collected cases from 17 definitions**, flat module-level
  functions with no test class. It is the record group's *internal* boundary: the kind's admissible pair, the
  two declared operations as members of the shipped vocabulary, the state/acceptance consistency rule in both
  directions, the promotion refusal measured as the stored payload being byte-identical afterwards, an
  `accepted` payload stored with the envelope lifecycle still `proposed`, the explanation refused by value, the
  four authorship substitutes refused, and the lineage rules including **a stored cycle forced by dropping the
  `record_revision_no_rewrite` trigger** so the shared `lineage.find_cycle` is what refuses the descendant.
  Two facts worth knowing before reading it: immutability is asserted against **re-read stored bytes** rather
  than a return value, and the two forbidden-name sets are **restated in the suite rather than imported from
  production**, so the absence case cannot pass by an import that quietly stopped covering a name.
- `test_knowledge_requirement_reference_contract.py` — **18 cases**, also flat. It is the boundary with the
  task plane and the derived views: the three owner components, the admitted version spelling, the reference the
  payload deliberately does not police, the forbidden operative-obligation and task-authority names at **both**
  the payload and the schema planes, the real owner's refusals carried verbatim with the stored reference
  byte-identical, route governance, the three-way reference resolution, and the views' rebuildability, totality
  and no-winner rules. It drives the **real** `_approved_packet_ref` rather than a stub, because a stubbed
  resolver cannot catch the second resolver the suite exists to exclude.
- Both modules are registered in the `unit-regression` lane at manifest lines 81 and 82, which is what keeps
  them collectable under a named classification rather than by accident.
- **One shipped assertion was re-scoped, additively.** `test_the_seam_registry_is_exactly_the_eight_declared_subtypes`
  pinned `set(KIND_SCHEMAS)` as the union of the three groups L14 left; the fourth family makes that false, so
  the assertion now unions `REQUIREMENT_RECORD_KINDS` as well. It is **equal in strength rather than weaker**:
  the claim is still *exactly* the union, so a group the registry does not declare still cannot be admitted
  without that line changing, the new group is derived from the registry entry rather than restated, and the
  facet-specific assertions around it are untouched. No case was deleted, skipped or xfailed. The module's own
  `RE-SCOPED` note now records two re-scope generations and is the place a reader learns the envelope registry
  is a shared, append-only surface.

**One code-side gate gap is recorded rather than settled here.** Both new modules import the shared-support
artifacts `knowledge_fixture_test_support.py` and `generation_test_support.py`, and both artifacts declare
`consumer_scope = "exact"` consumer lists in `mcp/tests/evidence-lifecycle.toml`. This leaf added the lane rows
but not those consumer entries, so the repository's own read-only evidence-lifecycle validator reports two
`consumer proof differs from source-derived ownership` findings for this change set. It is reported by this
leaf's curator to the owning seat; it is a code-side fix, not a memory one.

| Finding | Anchor | Source |
| --- | --- | --- |
|**The two new modules' lane rows, registered by the same change set that created them.**|"mcp/tests/test_knowledge_requirement_reference_contract.py" ; "mcp/tests/test_knowledge_requirement_revisions.py"| mcp/tests/test-evidence-lanes.toml:85-87; mcp/tests/test-evidence-lanes.toml:92-100 |
| The record group's internal-boundary suite and the two facts that make its immutability and absence claims measurements. | "test_a_promotion_attempt_is_refused_and_no_stored_byte_changes"; "test_a_payload_carrying_an_operative_obligation_field_is_refused" | mcp/tests/test_knowledge_requirement_revisions.py:247-276; mcp/tests/test_knowledge_requirement_reference_contract.py:294-310 |
| **The re-scoped seam case that pins the registry as the union of all four groups.** | "test_the_seam_registry_is_exactly_the_eight_declared_subtypes" | mcp/tests/test_knowledge_facets.py:183-247 |
| The two shared-support artifacts both new modules consume, whose exact consumer lists are the gate gap recorded above. | `make_authorship`; `create_current_generation_store` | mcp/tests/knowledge_fixture_test_support.py:189-220; mcp/tests/generation_test_support.py:86-120 |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_capsule_serving.py" repointed to mcp/tests/test-evidence-lanes.toml:23-23. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "path = \"mcp/tests/eve_capsule_test_support.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1434-1434. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_attach_final_full_catalog` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:600-636. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "path = \"scripts/e2e_harness/fresh_user_fixture.py\"" repointed to mcp/tests/evidence-lifecycle.toml:1550-1550. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:253-253. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:251-251. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:112-112. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:106-106. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:25-25. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-graph-case-support\"" repointed to mcp/tests/evidence-lifecycle.toml:30-30. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:25-25. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_label_operations.py" repointed to mcp/tests/test-evidence-lanes.toml:93-93. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"candidate-batch-case-harness\"" repointed to mcp/tests/evidence-lifecycle.toml:35-35. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-identity-branching-fixture\"" repointed to mcp/tests/evidence-lifecycle.toml:25-25. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1273-1273. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1273-1273. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:190-190. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `build_read_scope_fixture`; "id = \"knowledge-read-scope-cases\"" repointed to mcp/tests/read_scope_test_support.py:266-283; mcp/tests/evidence-lifecycle.toml:65-65. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:98-98. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:98-98. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `build_diff_fixture`; "id = \"knowledge-diff-cases\"" repointed to mcp/tests/diff_scope_test_support.py:189-233; mcp/tests/evidence-lifecycle.toml:60-60. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_shipped_seed_page_is_byte_identical_and_the_facet_page_is_its_own_policy" repointed to mcp/tests/test_knowledge_facets.py:1194-1194. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" repointed to mcp/tests/test_knowledge_facets.py:1246-1246. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-facet-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:55-55. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_facets.py" repointed to mcp/tests/test-evidence-lanes.toml:89-89. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_detection_runs.py" repointed to mcp/tests/test-evidence-lanes.toml:85-85. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_detection_signals.py" repointed to mcp/tests/test-evidence-lanes.toml:86-86. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1382-1382. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1402-1402. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1273-1273. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1382-1382. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1402-1402. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_citation_bindings.py" repointed to mcp/tests/test-evidence-lanes.toml:84-84. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_composition.py" repointed to mcp/tests/test-evidence-lanes.toml:90-90. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_composition_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:91-91. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "id = \"knowledge-facet-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:55-55. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "replacement_contract = \"contract:knowledge-read-scope-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1402-1402. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" repointed to mcp/tests/test_knowledge_facets.py:901-901. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged" repointed to mcp/tests/test_knowledge_facets.py:1045-1045. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "integration_case_budget = 400" repointed to pyproject.toml:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1161-1161. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1161-1161. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:170-170. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "integration = [" repointed to mcp/tests/test-evidence-lanes.toml:170-170. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `build_read_scope_fixture`; "id = \"knowledge-read-scope-cases\"" repointed to mcp/tests/read_scope_test_support.py:266-283; mcp/tests/evidence-lifecycle.toml:1274-1274. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `build_diff_fixture`; "id = \"knowledge-diff-cases\"" repointed to mcp/tests/diff_scope_test_support.py:189-233; mcp/tests/evidence-lifecycle.toml:1269-1269. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_the_shipped_seed_page_is_byte_identical_and_the_facet_page_is_its_own_policy" repointed to mcp/tests/test_knowledge_facets.py:1157-1157. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" repointed to mcp/tests/test_knowledge_facets.py:1208-1208. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1290-1290. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1310-1310. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1161-1161. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-diff-cases" repointed to mcp/tests/evidence-lifecycle.toml:1290-1290. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1310-1310. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "contract:knowledge-read-scope-cases" repointed to mcp/tests/evidence-lifecycle.toml:1310-1310. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "id = \"knowledge-facet-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1207-1207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "replacement_contract = \"contract:knowledge-read-scope-cases\"" repointed to mcp/tests/evidence-lifecycle.toml:1310-1310. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" repointed to mcp/tests/test_knowledge_facets.py:866-866. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged" repointed to mcp/tests/test_knowledge_facets.py:1009-1009. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 2 claim(s) here (2 x citation_claim_reopened). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:99-99. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:194-194. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:205-205. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:98-98. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:202-202. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:227-227. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_pane_authority.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_store.py" repointed to mcp/tests/test-evidence-lanes.toml:93-93. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_label_operations.py" repointed to mcp/tests/test-evidence-lanes.toml:80-80. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "contract:common-base-merge-cases" repointed to mcp/tests/evidence-lifecycle.toml:1159-1159. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "integration = [" repointed to mcp/tests/test-evidence-lanes.toml:168-168. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_scope.py" repointed to mcp/tests/test-evidence-lanes.toml:85-85. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_facets.py" repointed to mcp/tests/test-evidence-lanes.toml:76-76. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_composition.py" repointed to mcp/tests/test-evidence-lanes.toml:77-77. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_family_composition_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:78-78. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "integration_case_budget = 400" repointed to pyproject.toml:323-323. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 137 generated projection bullet(s) by hand while resolving the memory sync** — `test_the_shipped_seed_page_is_byte_identical_and_the_facet_page_is_its_own_policy`, `test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables`, `test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged`, `mcp/tests/test_memory_backfill.py`, `mcp/tests/test_cross_master_concurrency.py`, `mcp/tests/test_lifecycle_playthrough_end_to_end.py`, `mcp/tests/test_memory_attribution_producers.py`, `mcp/tests/test_leaf_doc_master_link_binding.py` and 28 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T04:50:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): recorded the **requirement-revision suites, the lane rows they obliged and the one shipped assertion they re-scoped**, and corrected two stale citations this card carried in the route table above. The section states the two things a reader would otherwise have to reconstruct from the cases — that immutability is asserted against re-read stored bytes and that the forbidden-name sets are restated in the suite rather than imported from production, so the absence cases cannot pass by an import that stopped covering a name — and it records the re-scope as **equal in strength rather than a weakening**, with the reason: the assertion is still *exactly* the union, so a fifth group cannot be admitted without that line changing, and the new group is derived from the registry rather than restated. It also records a **code-side gate gap** this leaf left open, which the curator reported to the owning seat rather than absorbing: both new modules consume two `consumer_scope = "exact"` shared-support artifacts whose consumer lists do not name them, so the repository's own evidence-lifecycle validator reports two findings for this change set. The two corrected citations were in the `mcp/tests/test_knowledge_family_revision.py` row, whose range had drifted with the lane insertions and whose anchor now resolves at `:74`. Verification metadata advances to the leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 54 generated projection bullet(s) by hand** — `mcp/tests/test_memory_backfill.py`, `mcp/tests/test_cross_master_concurrency.py`, `mcp/tests/test_pause_stop_only_end_to_end.py`, `mcp/tests/test_pause_is_not_publication.py`, `mcp/tests/test_lifecycle_playthrough_end_to_end.py`, `mcp/tests/test_memory_attribution_producers.py`, `mcp/tests/test_leaf_doc_master_link_binding.py`, `mcp/tests/test_terminal_blocker_reasons.py` and 16 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read this route overview against the current source and repaired the citation ranges the leaf's addition moved.** It added the **supporting-record cases** route section — two unit-regression modules, the registered `shared-support` fixture and its exact consumer scope, and the three re-scoped facet cases that no longer spell the shared substrate's membership as a closed list. The body above is the substantive update; the route's own source scope moved because the leaf both adds modules to it and appends two entries to the registry it documents.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 16 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_memory_backfill.py"` → `mcp/tests/test-evidence-lanes.toml:94-94`; `"mcp/tests/test_cross_master_concurrency.py"` → `mcp/tests/test-evidence-lanes.toml:187-187`; `"mcp/tests/test_lifecycle_playthrough_end_to_end.py"` → `mcp/tests/test-evidence-lanes.toml:198-198`; `"mcp/tests/test_memory_attribution_producers.py"` → `mcp/tests/test-evidence-lanes.toml:93-93`; `"mcp/tests/test_leaf_doc_master_link_binding.py"` → `mcp/tests/test-evidence-lanes.toml:195-195`; `"mcp/tests/test_terminal_blocker_reasons.py"` → `mcp/tests/test-evidence-lanes.toml:220-220`; `"mcp/tests/test_terminal_blocker_reasons.py"` → `mcp/tests/test-evidence-lanes.toml:220-220`; `"mcp/tests/test_memory_backfill.py"` → `mcp/tests/test-evidence-lanes.toml:94-94`; `"mcp/tests/test_cross_master_concurrency.py"` → `mcp/tests/test-evidence-lanes.toml:187-187`; `"mcp/tests/test_lifecycle_playthrough_end_to_end.py"` → `mcp/tests/test-evidence-lanes.toml:198-198`; `"mcp/tests/test_memory_attribution_producers.py"` → `mcp/tests/test-evidence-lanes.toml:93-93`; `"mcp/tests/test_leaf_doc_master_link_binding.py"` → `mcp/tests/test-evidence-lanes.toml:195-195`; `"mcp/tests/test_terminal_liveness_registration_order.py"` → `mcp/tests/test-evidence-lanes.toml:151-151`; `"mcp/tests/test_knowledge_store.py"` → `mcp/tests/test-evidence-lanes.toml:88-88`; ``integration`` → `mcp/tests/test-evidence-lanes.toml:162-162`; `"integration = ["` → `mcp/tests/test-evidence-lanes.toml:162-162`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read this route against the changed manifest and wrote the section above. Two modules joined the populations (one unit, one integration), one consumer row was added to `evidence-lifecycle.toml`, and both lane rows were inserted at the head of their lists so **every lane row cited below the insertion points moved**; the affected claims here were re-derived from the current manifest rather than accepted from the mechanical projection — the integration rows for the read/diff boundary and path modules are now `:165`, `:166` and `:167`, the L37 pause-suite and AST-only-guard rows `:203` and `:240`. The case budgets are unchanged and no ceiling was raised. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): recorded the **citation-binding suites and the registry rows they obliged**, because this route is the one that governs the changed test modules. The section states each module's lane and why — the vocabulary suite is hermetic and therefore unit-regression; the boundary suite opens a real store and builds a real Git repository in most of its cases and is therefore integration — and what each group of cases actually protects, including the two that a superficial reading would miss: the resolution cases are **fallback catchers** that fail if the resolver ever falls back to the working tree, and the write cases measure a refusal *and* its consequence rather than the refusal alone. It records the registry touch-points this leaf paid and the one it did not: two lane rows in `mcp/tests/test-evidence-lanes.toml` (an insertion into the alphabetical knowledge run and the opening row of the integration lane, which between them move every later line of that file — the mechanical reason a batch of this route's citations into it needed re-pointing in the same change), **five** `consumers` rows in `mcp/tests/evidence-lifecycle.toml`, the deliberately re-pinned catalog digest in `test_dependency_ownership_ast_helpers.py`, the two modules registered as `REPOSITORY_TEST_INPUT_CONSUMERS` of the ambient role runner — and **no new artifact and no new contract**, because both modules reuse the already-registered fixtures, so the counts stay at **13 contracts and 54 artifacts**. It also records the rule this leaf's evidence teaches — a path *string* in a test is a dependency edge in **two** registries with two derivations, so adding one is never a no-op — and the second additive re-scope of the seam-registry facet case, which now names this leaf's own group constant instead of trimming the expectation back, while the generation case asserts the sequence as the structural fact (contiguous `1..N`, `ar-knowledge-sqlite/vN` names, register order) that is stronger than the literal list it replaced. No verification stamp is advanced over unreviewed content: the body was re-read against the current source and the closeout owns the commit fields.

- 2026-09-18T03:15:00+00:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): recorded the **detection suites and the registry rows they obliged**, because this route is the one that governs them. The section states the two new unit-regression modules and their populations (28 collected cases from 20 definitions in the signal suite, 19 in the run suite), the one case that drives a **real** two-snapshot comparison through the shipped application seam rather than a shape invented beside it, and the three registry touch-points a new test module obliges — of which this leaf paid **two**: a two-line lane insertion in `mcp/tests/test-evidence-lanes.toml` (which is why every later line of that file shifted and other routes' citations to it moved) and two `consumers` rows in `mcp/tests/evidence-lifecycle.toml`, with the catalog digest in `test_dependency_ownership_ast_helpers.py` **re-pinned deliberately** and the reason written beside it. It records the one touch-point this leaf did **not** pay and why: the two detection modules use the already-registered `diff_scope_test_support` and `read_scope_test_support` fixtures, so no artifact and no contract was added and the counts stay at **13 contracts / 54 artifacts**. It also records the **two shipped facet cases this candidate falsified and re-scoped rather than deleted**, with the replacement fact each gained, and the pre-existing `test_static.py`/`anyio` collection defect the literal combined command hits — reported with both facts (1312 pass + 4 collection errors without the override; 1637 pass with it) instead of one. Verification metadata advances to this leaf's base commit `4264dcc9` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T01:00:00+00:00 — 260915-KS-L24 curator (uncommitted change set on `ar/260915-ks-l24`, base `9c12e8b1`): recorded the **certification suite's 18 new publication-input cases and the budget pair this candidate moved**, because this route is the nearest governor of the changed test module. The section states what the cases protect and why a message is the requirement — `publish` demanded nine non-`None` members while `semantic_requirement_revision` and `delivery_attempt` looked optional, were not echoed by `prepare`, and were not named by the refusal, which is the defect two earlier leaves of this master read as an impassable blocker (`notes/DISCLOSURES.md` D-11) — and it names the file-size rail the module is now close to (1190/1200). It also re-read the two budget-dependent claims this candidate falsified: the L11 section's present-tense "1250 against `unit_case_budget = 1250`" is now marked as that leaf's own measurement with the current pair named, and the ceiling row cites the pinned `"unit_case_budget = 1500"` literal, because **`unit_case_budget` occurs four times in `pyproject.toml`** (three inside the comments explaining the raises) and cannot anchor a unique claim. Nothing else in this 2900-line route was re-read in this pass. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-17T22:25:00+00:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): recorded the **facet suite and the governed harness it shares** — `test_knowledge_facets.py` (unit-regression, `:71`, **17 hermetic nodes** over in-process databases built through the production seam) and `facet_test_support.py` (artifact `knowledge-facet-cases`, one exact consumer, owning one **admitted** candidate and one **recorded** generation-2 dataset whose page and result digests were measured on the base revision before this leaf existed). The section states plainly that **the case ceiling is why the module carries loops rather than parametrizations** — the unit population had twenty slots left and the repository's record forbids a KS leaf from raising it — with the cost named (no independent failure attribution between variants of one property) and the population measured (**1250 against `unit_case_budget = 1250`**, integration 322). It records that this leaf is what makes the earlier byte-identity claim checkable as a before/after observation rather than self-consistency, the **three registry touch-points** a new test module obliges (lane row, artifact consumer list, catalog digest re-pin `19ed0525…` at **13 contracts / 54 artifacts**) plus the new artifact's contract row, and the **two honest limits** that travel with the suite: the combined run needs this host's documented `-W "ignore::DeprecationWarning"` override (the pre-existing D-7 defect routed to L9) with both facts stated rather than one, and the contract-scoped memory-quality operation and `--certify` were not run. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_the_mutation_harness_can_actually_fail` repointed to mcp/tests/test_capsule_serving.py:1305-1317. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_capsule_serving.py" repointed to mcp/tests/test-evidence-lanes.toml:21-21. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `fixture_launch_binding` repointed to mcp/tests/eve_adapter_test_support.py:407-436. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_memory_backfill.py" repointed to mcp/tests/test-evidence-lanes.toml:86-86. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_cross_master_concurrency.py" repointed to mcp/tests/test-evidence-lanes.toml:180-180. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:193-193. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_memory_attribution_producers.py" repointed to mcp/tests/test-evidence-lanes.toml:85-85. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:190-190. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_terminal_liveness_registration_order.py" repointed to mcp/tests/test-evidence-lanes.toml:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_terminal_blocker_reasons.py" repointed to mcp/tests/test-evidence-lanes.toml:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:11:00+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): **route meaning changed** — the knowledge suite gained two modules and one shared harness for a schema that stopped being a build-time singleton. The body now records the generation-registry pair (`test_knowledge_schema_generations.py`: the pinned generation-1 fingerprint recomputed and the gate exercised in the **failing** direction on three independent perturbations, the type-strict artifact key lookup, the unregistered-version refusal on the open path, creation declaring generation 2 while a generation-1 file still reports generation 1 with its recorded fingerprint, and the acceptance check a partial fix fails — adding and populating a generation-2 table **changes** the generation-2 digest), the preflight/envelope pair (`test_knowledge_merge_generations_and_envelope.py`: the v1/v1/v2 refusal before any session with byte-identical inputs, **the v1/v1/v1 merge on the generation-2 build passing** with generation 1's ten tables attached, and `invalid_payload` with no row written) and `test_knowledge_routes.py`'s eighteen cases over the route write layer. It records the harness rule a later case must not break: `generation_test_support.py` builds a real generation-1 dataset from generation 1's own recorded DDL, because a fixture created by the build is generation 2 and a digest or context built from the literal `ar-knowledge-sqlite/v1` then describes a dataset the fixture does not hold. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: added the section above — the route's new governing-overview guard and the wiring case beside it, the two halves of one defect, plus the lane row that keeps the fail-closed loader complete. Verification metadata advanced to this leaf's frozen code base.
- 2026-09-17T16:02+02:00 — 260915-CAPS-L11 curator (**final-verification leaf**): **this route's `D9` residual is closed.** L11 registered the six historical modules the fail-closed loader had been naming — `test_eve_adapter`, `test_eve_protocol`, `test_role_capsule_admission`, `test_role_capsule_compiler`, `test_role_instruction_corpus`, `test_task_projection` — all `unit-regression`; the loader now returns `LANE-REGISTRY-OK 243 0` and each module collects (198 unit / 0 integration). The new section above records that, the `S-D9-lane-row-removed` seed proving the rows are load-bearing, and the route-level lesson that a manifest fingerprint must be asked of the product rather than rebuilt by hand. This entry exists because the route body itself changed: the three governed sources on this route (`test-evidence-lanes.toml`, `test_capsule_launch_wiring.py`, `test_role_capsule_admission.py`) all moved, and an external-memory refresh requires updated route content rather than a metadata-only stamp. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits. The earlier entries below are left exactly as written, including L10's and L19's field-model entries, whose ordering is a dated record rather than an assertion of current doctrine.
- 2026-09-17T14:15+02:00 — 260915-CAPS-L19 curator: **Field-name warrant corrected — `ready-for-closeout` read as *never* a value of the combined `checklistStatus`.** That absolute sentence was written by 260915-CAPS-L10's curator as the warrant for this card's `D35` correction, and `CAPS-R19` (`260915-CAPS-L19`) measures it **literally false** (`application/memory_quality/controller.py:685-687` leaves the combined field at its incoming `ready-for-closeout` value on the success path, with `closeoutReady=true`). The card now states the three-path model instead: the raw `qualityChecklistStatus` is the repair loop's gate; the combined `checklistStatus` is rewritten to `coherence-required` **only when the coherence record is then missing or stale**; and `closeoutReady` becomes true only once that validation passes. Corrected under `CAPS-R19`'s revision note (2026-09-17T13:55), which is the authority for this change. The field-name correction itself stands and attribution is complementary — `260915-CAPS-L10` corrected the onboarding cards, `CAPS-R19` corrected the shipped sources (the five loop-gate carriers, their nine generated copies, the guard registry's docstring) and brought `docs/reference/mcp-tools.md` into the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`. The earlier entries below are left exactly as written: they record what L10 did, and this entry is the correction of their warrant. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-17T13:45+02:00 — 260915-CAPS-L10 curator: **corrected a landed defect (`D35`)** in the CAPS-L18 section — `ready-for-closeout` is never a value of the combined `checklistStatus`; the curator repair loop's gate is the **raw** `qualityChecklistStatus`, the combined field then reports `coherence-required`, and `closeoutReady` follows validation (`application/memory_quality/controller.py:664,671,678,687`). **No test-surface change:** this leaf's code delta is zero, it adds no module and touches no lane row, so this route's population, its budgets and its `D9` residual are unchanged (`D9` remains L11's six historical modules). Verification metadata is left alone: the candidate is uncommitted and the governed closeout stamps the real code commit.
- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: the complete-curation doctrine reaches this route. The canonical sources on this route now state that the full `memory_quality_check` operation is part of every leaf's curation, that a subset never stands in for it, and that closeout and integration carry the completed result as a prerequisite while invoking nothing. Body updated as above; no verification stamp advanced because the sources are uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: this route gained **one module** —
  `test_capsule_experiment_install.py`, 19 cases — plus two rows in `test_sync_runtime.py`. The
  section above records what the population protects, that the module is not a seventh `D9` row,
  and that its two `evidence-lifecycle.toml` consumer rows are this leaf's whole catalog delta.
  Verification metadata is left at this leaf's synced base `933b011b`; the candidate is
  deliberately uncommitted.

- 2026-09-17T11:50+02:00 — 260915-CAPS-L14 curator: this route gained **two modules** and the reference rows and lane/catalog citations that go with them. `test_citation_index_resilience.py` defends the citation index's shared exclusion register per source, the ruled caps' skip-and-report behaviour, and the quality surface's reported states — with the register's deliberate divergence from Git measured on both sides; `test_fresh_user_harness.py` is the **consumer of record** for the three new `scripts/e2e_harness` governed artifacts and pins the fixture shape and the scenario contract (a step that cannot run is `blocked` by name, never `completed`). Added the corresponding rows, the two `unit-regression` lane rows, and the three `[[artifact]]` rows the leaf registers. **Repaired two stale claims on this route**: the final memory adapter citation still pointed at `worktrees/integration/closeout/prepared_certification.py:721-785`, a path that no longer exists — the adapter moved to the application rank in `806649b9`, so the row now reads `application/prepared_certification.py:749-813`. Verification metadata is left at this leaf's synced base `0346da9c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code commit.

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `mcp/tests/test_knowledge_read_paths.py` in the row 1186 of this card from mcp/tests/test-evidence-lanes.toml:158 to mcp/tests/test-evidence-lanes.toml:160, the extent of the construct the claim is about (the checker named line(s) [160] as its live location); re-pointed `mcp/tests/test_pause_is_not_publication.py` in the row 795 of this card from mcp/tests/test-evidence-lanes.toml:171-171 to mcp/tests/test-evidence-lanes.toml:232, the extent of the construct the claim is about (the checker named line(s) [232] as its live location); re-pointed `mcp/tests/test_pause_is_not_publication.py` in the row 809 of this card from mcp/tests/test-evidence-lanes.toml:170-170 to mcp/tests/test-evidence-lanes.toml:232, the extent of the construct the claim is about (the checker named line(s) [232] as its live location); re-pointed `mcp/tests/test_pause_is_not_publication.py` in the row 795 of this card from mcp/tests/test-evidence-lanes.toml:204-204 to mcp/tests/test-evidence-lanes.toml:232, the extent of the construct the claim is about (the checker named line(s) [232] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): stamped the untimestamped Update History entries with this document's own commit clock; stamped the untimestamped Update History entries with this document's own commit clock

- 2026-09-17T01:31:11+00:00 — **Historical stamp carried from the incoming official line** (merge HEAD `12bd7fd3`; the live stamp for this file is the later synced value in the metadata table above, which closeout re-stamps): `lastUpdated` 2026-09-15T20:42+02:00; `lastVerifiedCommitHash` `806649b91bdce18f7b915bfbbf6727967f4e7a88`; `lastVerifiedCommitDate` 2026-09-16T12:23:53+02:00; `reviewedWorkingCandidate` `ar/260831-locr-l18` uncommitted source; base `d868486c07ac14d8af6d0d5555dbda4f3b737785`.

- 2026-09-17T01:15:00+00:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): recorded the **comparison half's two suites and the governed support artifact they share** — `test_knowledge_diff_scope.py` (unit-regression, `:76`, 13 hermetic nodes over two in-process snapshots and two local committed trees) and `test_knowledge_diff_boundaries.py` (integration, `:159`, 15 nodes that **drive the production Git probe**, a real candidate write and the serialized response), with `diff_scope_test_support.py` registered as the artifact `knowledge-diff-cases`. The paragraph states the **three registry touch-points a new test module obliges** — all three paid twice, plus the two consumer rows the read-scope artifact gained — and the measured merged numbers: **52 artifacts / 11 contracts** (digest `4cf81f10…`) and **243 declared lane entries against 243 modules on disk**. **The coverage-rule reason is recorded with the direction each rule was measured in** (rule 1 load-bearing alone; rule 2 a short-circuit whose family half is unexercised because the fixture authors 0 family edges — a stated gap; rule 3 load-bearing in the forced-present direction, with variant `C` surviving 28/28 and the `2 failed` belonging to `G`), together with the statement that **collapsing the rules turns a missing selection into a real absence** — the reverse of the leaf's first claim. It also carries the **three evidence rules this leaf's history teaches** and states the four non-kill classes as disclosures with their closers, so a reader never reads the comparison as fully covered. **The `M25`/`M26` citations in this route's cards are the measured ones for the frozen 779-line module, and the card says explicitly that the ledger is authoritative for the contested pair** and that the leaf's documentation debt was carried to `KS-R09`/`L9` (ledger **A9**/**A10**). Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.

- 2026-09-16T21:50:00+00:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): recorded the **read half's three suites and the governed support artifact they share**. The section gives the lane and the reason for each module (the unit module hermetic over in-process databases; the boundaries module over a real committed Git tree and a real published database; the paths module measuring Git's own `ls-tree` behavior with its own subprocess calls), names the split as a **file-size decision** — fix round 2 pushed the boundaries module past the 1 200-line limit and the cases moved rather than the limit being waived — and states the three registry touch-points a new test module obliges, all of which this leaf paid (lane row, support-artifact `consumers` list, catalog digest re-pin `461121ca…` with counts 10/51), because missing any one is a **hard collection error rather than a quiet gap**. **The path contract is recorded in the form the review corrected it**: pathspec magic is the leading-`:` family plus `..`, absolute paths, `~`, drive/UNC spellings, backslashes and NUL, while `*`, `?` and `[` are **literal characters** to `ls-tree` and a legitimate anchor containing them must be authorable, seedable and resolvable — round 1's over-broad refusal reported a file the tree really holds as `path_absent`. **Two honest limits travel with the suites and neither is coverage**: the **withdrawn** mutation claim over `_tree_entry`'s non-zero-exit branch, which stays an explicitly disclosed unasserted defensive branch (L9 **A6**), and `_manifest_digest`'s composition as a reachable covered gap (L9 **A4**). The entry also records the rule about what a survivor means — **a sweep must run on the frozen bytes it describes** — and the forward constraint that **L8 must split the 1 163-line unit module before adding cases**. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l07`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.

- 2026-09-16T20:42+02:00 — 260915-CAPS-L7 curator: this route gained three modules and two fixture
  changes for the eve capsule/workspace binding seam, recorded in the new
  `## 260915-CAPS-L7 The Eve Capsule/Workspace Binding Evidence` section. The section explains the
  three-way split by what each module can actually observe — real-git/uxtree support, the Python half
  whose refusal cases assert a **named** defect, and the TypeScript half that executes the shipped
  modules under a real Node through a loader hook supplying only the eve compiler's specifier convention
  — and records the two fixture changes that belong to the same seam: `fixture_launch_binding()` in the
  adapter support, needed because the launch path is production even when the transport is a double, and
  the trace's new `messages` key, which is the only place the **effective prompt** is observable and so
  is what keeps the live "the binding reaches the model" claim a measurement. It also records the
  whole-seam boundary: the live capsule scenarios are the end-to-end proof, and the produce side they
  exercise still has **no production caller** — wiring one is `CAPS-R15@v1`'s obligation under an
  explicit transfer. Verification metadata moves to the leaf's synced base `23cc7a72`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.
- 2026-09-16T15:45:00+00:00 — 260915-KS-L6 curator (uncommitted change set on `ar/260915-ks-l06`, base `7db50f8f`): recorded the portable half's pair of suites and the reason they are split — **the 1200-line hard limit**, not classification, so the boundary module imports the roundtrip module's helpers and the two are one evidence set with one definition of an artifact and a refusal. The paragraph states what each node protects (the consolidated completeness/refusal-inertness/preservation groups, the deterministic-artifact node, the recomposition through L5's merge, and the five boundary properties including the whole-document canonical form with all seven header types and the staged sealed-aggregate read), and it records the rule this leaf's evidence teaches rather than leaving it to be rediscovered: **a reachable guard with no killing node is reported, not claimed** — the header namespace-binding check at `export_portable.py:911` is written up as an observation for **L9** with its mutation and reachability proof. It also records that the final fix round extended these cases rather than adding one, so the integration population stayed at 255, and the three consumer lists the two modules were added to. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l06`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.

- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: **route meaning changed**, so this overview gained a
  section rather than a no-impact entry. Added the L5 test population — `test_codex_capsule_delivery.py`
  at **28 collected cases and no `integration` marker**, registered under **`provider-conformance`** at
  entry row 216 — plus the two expiry fixtures it reads (`codex_app_server_instruction_channels.json`
  and `codex_app_server_model_page.json`), naming the `turn/start` instruction-field absence the
  lifetime design rests on and why a captured `model/list` page replaced hand-written drafts. Recorded
  the module's two deliberate doublings (transport, transient discoverer) and the live case's
  skip-not-pass guard. Verification metadata stays pinned to the last committed source (`c1dbebf8`).

- 2026-09-16T11:45:00+00:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): recorded the merge half's own pair of suites and the reason they are split — the unit population sits exactly at its declared ceiling after this leaf, so the merge's whole contract is five unit cases and every scenario needing its own three-commit Git world went to the integration lane. The paragraph states what each node is the mutation target for, and it records the two rules this leaf's evidence teaches rather than leaving them to be rediscovered: **a broken mutation is not a killed guard** (the first matrix scored a `NameError` as a kill; the harness now refuses to score a crash, and the re-derived headline is 17 of 21 killed with four named non-experiments) and **a guard whose call site is unreachable is described as one** rather than presented as coverage. It also records the new governed harness (`common-base-merge-cases`, exact two-consumer list) and, as its load-bearing design fact, that its `shape` callback runs before the commits are built. Verification metadata remains closeout-owned.

- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass**: refreshed this route section
  against the settled candidate. Corrected the population from 21 to **30 collected items (28 unit + 2
  integration)**, re-derived every fixture and case line number against the current 1,535-line module,
  and named the cases the two repair rounds added — the SEP entry contract, this server's own index
  shape asserted separately from the enumeration surface, and the four previously-unpinned guards each
  driven by its own case. Recorded that the exchange case now exercises **both extension methods**,
  including `skills/get` on an absent URI refused `-32602`, and dropped the reference to a helper the
  module no longer carries. Verification metadata remains closeout-owned; no acceptance claim is made.

- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator (uncommitted change set on `ar/260915-caps-l4`,
  base `b00a4ac2`): **route body updated** — added § 260915-CAPS-L4 Capsule And Skill-Serving Test
  Population, placing the new `test_capsule_serving.py` in this route and stating the properties it
  protects (19 hermetic admission/serving cases over a `World` fixture and a synthetic corpus, 2
  real-process exchanges driven by the installed SDK's own client, and 3 shipped-corpus cases that
  would catch packaging drift between the canonical root `skills/` tree and the served copy). A new
  card was created for the module in this route. Recorded that the module is registered in
  `test-evidence-lanes.toml` under `unit-regression` at entry row 19, and that the default unit
  selection on this branch refuses collection at 1083 collected cases against a 1000 ceiling (64 of
  that overage predating this leaf) — a current-state fact about the route's verification population,
  left un-repaired because raising a declared budget is an owner decision. Verification metadata
  remains closeout-owned: the source is uncommitted, so no stamp was advanced and no commit hash was
  invented.

- 2026-09-16T09:30:00+00:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): recorded the candidate and snapshot half's own pairs — the batch suite plus its command-union sibling and the standalone label guard, and the new candidate-lifecycle and publication suites sharing one registered harness (`knowledge-snapshot-lifecycle-cases`, exact two-consumer list). The paragraph states why that harness's evidence node is `test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not`: the claim being protected is that a published snapshot is *closed*, and only a comparison against a bare main-file copy measures it. It also names the lifecycle suite's two distinctive nodes — the live-reader state the removed WAL/SHM peer unlink destroyed, and a real child interpreter that exits with an uncommitted write transaction open — and re-states that a module missing from either registry fails the load rather than passing quietly. Verification metadata remains closeout-owned.

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: **route body updated** for the task-context projection's coverage module. Added § 260915-CAPS-L3 Task-Context Projection Coverage: the new module and its 9 collected cases, the anti-vacuity rule its docstring states as contract, the three cases that carry more weight than their size (the structural import-surface walk, the byte-identical non-mutation case, and the two-way compiler-seam case), the remaining six properties, the fixture-topology trap that took three rounds to mirror (`CAPS-L3-EV5`–`EV7`, chiefly that an internal memory root silently wins over an external coordination hint), the task-local `M01`–`M20` falsifiability probe and its self-caught vacuous seed (`CAPS-L3-EV10`), and the pre-existing pytest-unresolvable pyright condition. **Also recorded a scoped blocker for the owning seat**: this module has no evidence-lane row, and `load_lane_manifest` is fail-closed, so the manifest does not load as the candidate stands; the same gap exists for the three modules from `CAPS-R01@v1`/`CAPS-R02@v1`, making the correct repair a four-row change. That finding is derived from the loader's source, not executed — this seat has Python 3.10 and the repository requires `>=3.13,<3.14`. Verification metadata remains closeout-owned: the source is uncommitted, so no stamp was advanced and no commit hash was invented.
- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): **route body updated** for the native eve adapter's test population. Added § 260915-CAPS-L6 Native eve Adapter Test Population, which states the distinction this route now depends on: two of the five new modules are pytest-collected suites and three are support or explicit-run scripts, so "the suite protects this scenario" is proved by collection for the former and by a `--report-dir` artifact for the live fixture. Also records the A2 strengthening (the production client driven through a mock transport, the bounded replay window, the request-shaped cancel observation) and the `_knob_values` env carrier that holds the launch-vocabulary contract at four harnesses. Verification metadata remains closeout-owned: the source is uncommitted, so no stamp was advanced and no commit hash was invented.

- 2026-09-16T08:10:00+00:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base
  `27242ecb`): recorded the candidate-batch suite and the guard a passing suite could not see — three new
  unit-lane modules (the transaction boundary's 27 nodes, the union and receipt's 9, and a 6-node label-operations
  suite that exists because the batch path carries an independent copy of the label expectation rule and stayed
  green when the CAS was deleted, sealed finding `260915-KS-L3-RV-4`), one new governed support module registered
  as `candidate-batch-case-harness` with an explicit artifact row, a real evidence node and exactly two declared
  consumers, and the branching fixture's consumer list gaining this leaf's label suite. Also recorded the two
  reusable rules the evidence teaches: a node named for a mechanism must discriminate it (the "database-caught"
  and "context digest" nodes were both split for that reason), and a green suite is not a preservation proof (one
  upstream node was added because 54 cases passed while `create_invariant`'s answer had changed).
  Verification metadata remains closeout-owned.

- 2026-09-16T06:24:00+00:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base
  `60e0820e`): recorded the graph suite and the two registry changes it forced — four new unit-lane modules
  (family revision rules, relation rules, graph reads, and a fix-verification seal module whose existence is the
  outcome of sealed finding `260915-KS-L2-RV-1`), one new governed support module registered as
  `knowledge-graph-case-support` with three exact consumers, and a **correction** to the branching fixture's
  declared consumer list, which named one module while five now import it. Also recorded the reusable rule the seal
  module teaches (a test named for a sealed field must vary only that field, and dropping it must fail that node).
  Verification metadata remains closeout-owned.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **route body updated** for the lifecycle-corpus consolidation. Added § 260915-CAPS-L1 Role-Instruction Corpus Contract, which places the new shipped module `test_role_instruction_corpus.py` in this route and states the properties it protects (nine-role registry, the six-section readable order, the frozen eight-operation vocabulary, a prose-free manifest, every cited relative path resolving, a missing manifest source reported rather than accepted, and the `SANCTIONED_SIBLING_REFERENCES` independence rule). A new card was created for the module in this route. Verification metadata remains closeout-owned: the source is uncommitted, so no stamp was advanced and no commit hash was invented.

- 2026-09-15T20:40:00+00:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base
  `67b21aeb`): recorded the new knowledge-storage suite and its governed fixture — the 22-node unit-lane
  registration that the certifying collection path requires to start, the fixture's registered contract in
  `mcp/tests/evidence-lifecycle.toml`, and the load-bearing reason the fixture lives under `mcp/tests/**` rather
  than `mcp/test_support/**`. Verification metadata remains closeout-owned.

- 2026-09-15T19:40:00+00:00 — 260831-LOCR-L05 curator, **re-dispatch** (uncommitted change set on
- 2026-09-15T21:40+02:00 — 260831-LOCR-L05 curator, **re-dispatch** (uncommitted change set on
  `ar/260831-locr-l05`, pair code base `67c91534`, memory base `309110f8`): the route gained the
  worker-role wake, so the retained-route table was extended rather than annotated. New row for
  `test_state_signal_worker_wake.py` — an owned worker seat's canonical catalog terminal evidence
  (`completed` or `interrupted`) wakes its leaf's **current** manager as exactly one durable inbox
  row, with no completion post from the worker and no live terminal-session read; the eligible-outcome
  set pinned from both sides (`failed`/`unknown` refused while leaving the seat eligible); per-turn
  dedupe pinned in both directions (same evidence identity mints one row, a second distinct terminal
  turn mints its own); the `interrupted` outcome preserved with its origin; task documents proven
  byte-unchanged; the evidence identity — not a report on disk — as the discriminator; and a worker
  below a managerless master refused without a marker or a guessed global owner. Re-derived the six
  citations in this card whose anchored manifest rows moved by one line when the module's
  `unit-regression` row landed at file line `:105` (`:122`→`:123`, `:152`→`:153`, `:160`→`:161`,
  `:163`→`:164`, `:169`→`:170`, `:185`→`:186`, plus the second module in the shared L37 row
  `:204`→`:205`). Also corrected one pre-existing wrong citation in the retained-route table that this
  leaf did not cause: the L4 census module's lane row is at `:69`, not the `:68` the row recorded
  after L06's own insertion moved it. Records source documentation only; it makes no execution,
  acceptance or certification claim, and verification metadata remains closeout-owned.

- 2026-09-15T19:25:00+00:00 — 260831-LOCR-L04 curator (uncommitted change set on `ar/260831-locr-l04`,
- 2026-09-15T21:25+02:00 — 260831-LOCR-L04 curator (uncommitted change set on `ar/260831-locr-l04`,
  base `e9678c56`, `mcp/tests/test-evidence-lanes.toml` +1/−0 and three new test-side modules): this
  route gained the leaf's completion-relative observer-to-notifier handoff proof,
  `test_serving_notifier_handoff.py` (eight cases, unit-regression at manifest row `:97`), plus the two
  support modules that carry its instrument (`_handoff_clock.py`, `_serving_handoff.py` — support, so no
  manifest row, matching this directory's other support modules). The retained-behavioral-routes table
  gained the row above, and the population sentence now records **215** test-shaped modules and **122**
  unit-regression entries. The module enters the real `_serving_lifespan` under a deadline-correct
  virtual clock and measures the real observation loop, the real sweeper, the real catalog commit
  boundary and the real notifier sweep, with no HTTP request, no server and no process. Because the new
  lane row was inserted at `test-evidence-lanes.toml:97` — above every previously-latest unit row — every
  later manifest line moved one line, so this card's lane citations were re-derived against the current
  file rather than carried (`test_cross_master_concurrency.py` `:151` → `:152`,
  `test_leaf_doc_master_link_binding.py` `:159` → `:160`, the playthrough `:162` → `:163`,
  `test_pause_stop_only_end_to_end.py` `:164` → `:169`, `test_pause_is_not_publication.py` `:197` → `:204`,
  `test_terminal_blocker_reasons.py` `:184` → `:185`, `test_terminal_liveness_registration_order.py`
  `:121` → `:122`, `test_terminal_liveness_pane_authority.py` `:183` → `:184`); the same re-derivation was
  applied to the lane card and fourteen sibling cards, 59 live citations in all, while dated
  `## Update History` entries were left as written. Two of the pause pair's citations were already stale
  before this leaf and were corrected to the lines that carry them rather than shifted. `LOCR-R04@v1` is a
  preservation requirement: `mcp/src` is byte-unchanged by this change set, and no case budget is quoted
  or raised — `pyproject.toml` is the authority. Verification metadata remains closeout-owned; no stamp
  advanced.

- 2026-09-15T19:21:00+00:00 — 260831-LOCR-L06 curator, **re-dispatch** (uncommitted change set on
- 2026-09-15T21:21+02:00 — 260831-LOCR-L06 curator, **re-dispatch** (uncommitted change set on
  `ar/260831-locr-l06`, pair code base `e9678c56`, memory base `ee93a0fc`): the route gained the
  reviewer role's own relay proof, so the retained-route table was extended rather than annotated.
  New row for `test_lifecycle_owned_completion_relay_reviewer.py` — canonical reviewer terminal truth
  produced by observation wakes the current manager as one durable row with no completion post; the
  eligibility boundary that refuses liveness, control readiness and a self-reporting pane; the
  `interrupted` outcome preserved as itself; addressing by current occupancy past a departed manager
  generation; one signal per evidence identity; and the `failed` negative control that keeps the
  eligible set (`completed`/`interrupted`) a claim rather than an accident. The inserted row lands
  inside the alphabetical unit-regression run **above** the manifest rows this card's reference table
  cites, so nine citations here were re-derived against the candidate rather than carried:
  `test_memory_attribution_producers.py` `:68` → `:69`, `test_memory_backfill.py` `:69` → `:70`,
  `test_terminal_liveness_registration_order.py` `:121` → `:122`, `test_cross_master_concurrency.py`
  `:151` → `:152`, `test_leaf_doc_master_link_binding.py` `:159` → `:160`,
  `test_lifecycle_playthrough_end_to_end.py` `:162` → `:163`, the two L37 registrations `:164` → `:169`
  and `:197` → `:204`, and `test_terminal_blocker_reasons.py` `:184` → `:185`. The manifest population
  is now **215** modules (122 unit-regression / 2 public-contract / 62 integration /
  16 architecture-fitness / 13 provider-conformance), not the 214 this card carried. Verification
  metadata remains closeout-owned; no stamp advanced.

- 2026-09-15T19:19:00+00:00 — 260831-LOCR-L07 curator (uncommitted change set on `ar/260831-locr-l07`,
- 2026-09-15T21:19+02:00 — 260831-LOCR-L07 curator (uncommitted change set on `ar/260831-locr-l07`,
  base `e9678c56`): the route gained the curator turn owner wake (`LOCR-R07@v1`), so the
  retained-route table was extended rather than annotated, immediately below the crash/restart
  recovery row it shares its family with. New row and new section for
  `test_state_signal_curator_wake.py` (the curator seat reaching the same shared role predicate and
  current-manager routing as the worker seat; the durable payload carrying the curator role, the
  subject leaf document, the mechanical outcome and the terminal evidence identity off the real
  liveness sweep and the real agent-notifier sweep; one durable signal and never a second on
  re-observation for both `completed` and `interrupted`; `failed` reaching terminal truth and
  emitting nothing while the seat stays eligible; no verdict appended and no coherence/readiness
  artifact written, with the coordination root read after the sweep compared against the premise;
  and the fail-closed refusal when the curator's own master has no current manager). The manifest
  row citations this card carries were re-derived against the manifest as it now stands, because the
  leaf's new unit-regression row at `:102` moves every cited row from `:102` down by one; three of
  them — the L34, L36 and L37 registrations — were already adrift of the source before this leaf.
  This is a preservation leaf: `mcp/src` is unchanged and no case budget was touched. Lane membership
  and its brackets live on the `test-evidence-lanes.toml` card, the owner of record. Verification
  metadata remains closeout-owned; no stamp advanced.

- 2026-09-15T18:42:00+00:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`, base
  `99534dc5`): the route gained the observer-health proof, so the retained-route table was extended
  rather than annotated. New row for `test_terminal_observer_health.py` (the exact atomic v1 record and
  its writer, the `initializing`/`degraded`/`healthy`/`stale` ladder at exactly six configured sweeps,
  omission-and-no-repair for every unusable source, the bounded ordered secret-safe failure
  vocabulary, publication on the observer CALL for both outcomes through the real lifespan, and the
  served tail driven through the real `_state_response` handler and `stream_events` generator with the
  packet's cross-read rows). Two stale figures were corrected in the same pass: the declared case
  budgets are 1,000 unit and **250** integration (the 150 recorded here predates L37's authorized
  raise), and the manifest population is **214** modules (121 unit-regression / 2 public-contract / 62
  integration / 16 architecture-fitness / 13 provider-conformance), not the 202 this card carried.
  Verification metadata remains closeout-owned; no stamp advanced.

- 2026-09-15T13:02:00+00:00 — 260831-LOCR-L18 curator (uncommitted test change set on `ar/260831-locr-l18`,
  base `d868486c`): the route gained the `LOCR-R18@v1` startup-prime proof, so this overview's
  retained-route table was extended rather than annotated. New row for
  `test_serving_startup_prime.py` (one pre-serve observation prime, off-loop through the drained
  helper, before the projection prime / the recurring tasks / the yield; committed truth read back by
  the initial projection and the first notifier sweep; no GET, dashboard or model message; a raised
  prime contained with the owner retrying on its cadence; the committed entry equal to one reference
  canonical pass). The existing `test_serving_observation_loop.py` row was corrected in place, because
  that module's meaning changed twice in this change set: it now owns the **shared serving fixture**
  imported by the new module, so its `startup` witness and `_Gate` are a shared contract with
  **call 1 = the pre-serve prime and call 2 = the recurring owner's own first pass**, and nine of its
  landed cases were re-anchored by that one-call shift (a pure index shift, no assertion relaxed,
  dropped or made conditional — the detail is on the module's own card). Its closing exclusion was
  widened to also exclude the prime's own ordering contract, which is now the sibling module's.
  Both modules are ordinary version-controlled test source in the `unit-regression` lane; lane
  membership and its brackets live on the `test-evidence-lanes.toml` card, the owner of record. No
  case budget was raised. Verification metadata remains closeout-owned; no stamp advanced.

- 2026-09-15T12:10:00+00:00 — 260831-LOCR-L11 curator (uncommitted test-only change set on
  `ar/260831-locr-l11`, base `163ba8a9`): route impact confined to the existing
  `test_serving_observation_loop.py` row, which this pass retitled and extended rather than
  duplicated. The module gained `ServingObservationFailureIsolationTests` (five cases, anchors
  `594-801`) beside the unchanged seven-case `ServingObservationLoopTests` (`399-591`), so the row now
  records the failure boundary as its own proof: one unexpected pass failure leaves the owner scheduled
  and the five sibling loops plus an in-process ASGI request alive, publishes nothing durable under a
  control proving a *successful* pass does change the tree, retries on the cadence alone from the
  current persisted catalog while rows, the emitted-signal marker and the workspace cursor survive, and
  still propagates cancellation because the boundary is `except Exception` while `CancelledError` is a
  `BaseException`. The row's closing exclusion was widened from the notifier's inline refresh to also
  exclude any structured observer-failure *publication* surface, because a reader must not take this
  module as evidence for an observer-health contract it deliberately does not assert. No production
  byte changed for this contract (`_app_lifespan.py` sha256 `7c36ea83…`, unchanged since L01) and the
  new cases are ordinary version-controlled test source, not a governed evidence artifact. The module's
  lane membership is unchanged and its lane row did not move; the detail lives on
  `test_serving_observation_loop.py.md`. Verification metadata remains closeout-owned.

- 2026-09-15T11:57:00+00:00 — 260831-LOCR-L02 curator (uncommitted change set on `ar/260831-locr-l02`,
- 2026-09-15T13:57+02:00 — 260831-LOCR-L02 curator (uncommitted change set on `ar/260831-locr-l02`,
  base `67b21aeb`): this route gained one integration member, so the `## Retained Behavioral Routes`
  table gained the row *Terminal catalog reads are side-effect free* for
  `test_serving_terminal_catalog_read.py` — the route-projection purity proof, with both of its
  instrument limits stated in the row rather than left implicit. The card's `lastVerifiedCommitHash`
  stays pinned: the candidate is uncommitted and verification metadata is closeout-owned. The facts
  this route already carried — `GET /api/terminal/sessions` and `GET /api/harnesses` are the two
  handlers whose `response_model` is live FastAPI validation, and the exact 52-key AST pin behind
  them — are unchanged and were re-read: the new module asserts the same declaration and the same
  conditional key set, so those historical entries stand as written.
---

- 2026-09-15T13:36+02:00 — 260831-LOCR-L27 curator, **citation repair in an edited document** (same
  change set): corrected the L36 cross-master forcing row's six case ranges, which had drifted
  (`test_cross_master_concurrency.py:131-162;465-512;529-563;565-620;752-780;784-852` →
  `131-162;409-456;473-507;509-568;754-822;722-750`). This was not optional tidying: the last of the
  six pointed past the end of an 847-line module and was an `error`-severity
  `citation_range_out_of_bounds` finding against *this* document. Every range was re-derived from the
  module rather than offset by a delta, because the recorded ranges were internally inconsistent —
  the two module-level helpers `_series` (`:88`) and `_member` (`:94`) sit between the two tests the
  row places at `:465-512`, so no single offset can reconcile them. `_checkpoint_with_candidate`
  (`:825`, a helper, not a test) was dropped as an anchor. The prior pass had explicitly recorded
  this citation as left-as-found and reported rather than repaired; that note now carries this update
  instead of contradicting the table. The two other out-of-bounds citations it recorded
  (`test_checkpoint_landing_end_to_end.py:835-835`, `evidence-lifecycle.toml:1038-1038`) name other
  documents and remain reported, not repaired. No behavior claim changed: only the ranges moved.

- 2026-09-15T11:36:00+00:00 — 260831-LOCR-L27 curator (uncommitted change set on `ar/260831-locr-l27`,
  base `b368b661`): added the route's pane-diagnostic-authority row for the new
  `mcp/tests/test_terminal_liveness_pane_authority.py`. Route meaning genuinely changed here: the
  route had no starting point for the question "may a captured pane reading authorize turn or
  terminal truth", and this module is now that entry point, so a body row was added rather than a
  no-impact marker. The row records the readiness half explicitly (an adapter
  `control="disconnected"`/`"failed"` snapshot with a `working` pane keeps the adapter's
  `control_state`), because that was the one clause the baseline review found unpinned, and it
  records the module's two deliberate properties a future reader would otherwise get wrong: the
  split from the byte-unchanged 574-line `test_terminal_liveness.py` is a size-doctrine decision and
  the two cards must not be merged, and the negative source guard is defence-in-depth whose measured
  blind spots (enclosing-`if` constant, positional writer arguments, `CatalogTurnEvidence(state=…)`)
  stay behaviour-pinned. Two reference rows were added for the same reason (the module's own anchors
  and the fixtures it imports from its sibling). The population sentence in this section still
  records the pre-L4 count and is left as the historical record it declares itself to be; the
  authoritative current lane population (209 modules, 61 integration) and the bracket citations live
  on the `test-evidence-lanes.toml` card, which is the owner of record for lane membership. No
  production byte changed for this contract and the new module is ordinary version-controlled test
  source, not a governed evidence artifact; this route's verification metadata remains
  closeout-owned.

- 2026-09-15T11:20:00+00:00 — 260831-LOCR-L23 curator (uncommitted change set on `ar/260831-locr-l23`,
  base `67b21aeb`): added the route's registration-before-compaction row — the new
  `mcp/tests/test_terminal_liveness_registration_order.py` pins the full sweep's post-commit order by
  instrumenting the terminated-row read itself, so a reorganisation that reads the open batch or reads
  ahead of it fails rather than passing silently — and reconciled the population sentence to the
  measured manifest: 208 modules on disk and 208 entries, 117 unit-regression (entry rows 5-122), 2
  public-contract (123-126), 60 integration (127-188), 16 architecture-fitness (189-206), 13
  provider-conformance (207-221), with stress-durability (222-223) and migration (224-225) empty. The
  insertion sits at entry row 118 between two alphabetically adjacent rows, so no other entry moved and
  no lane changed; no production byte changed for this contract, and this route's own file cards
  (`test-evidence-lanes.toml.md`, the new module's card) carry the detail. The new module is ordinary
  version-controlled test source, not a governed evidence artifact. Membership remains selection and
  cost classification only: it is not execution, certification or acceptance evidence, and this
  route's verification metadata remains closeout-owned.
- 2026-09-15T11:19:00+00:00 — 260831-LOCR-L01 curator (uncommitted change set on `ar/260831-locr-l01`,
- 2026-09-15T13:19+02:00 — 260831-LOCR-L01 curator (uncommitted change set on `ar/260831-locr-l01`,
  base `67b21aeb`): the route gained the leaf's hermetic `test_serving_observation_loop.py`, so the
  retained-behavioral-routes table gained a row for the serving-owned steady-state observation proof
  and the manifest population it registers into is now 208 modules. The module enters the real
  lifespan finalizer and the real sweeper under a virtual clock and issues no HTTP request, so the
  unit lane is its behaviour-preserving classification. The same pass removed one dead reference row
  rather than re-pointing it: the L34 flake note (`"UNREPRODUCED FLAKE, RECORDED 2026-09-13"`) was
  cited at `test_checkpoint_landing_end_to_end.py:835-835`, which is 356 lines past the end of the
  479-line file and no longer contains the literal anywhere — `4164e3d0` retired it — so the claim it
  carried is gone and the row was deleted. Because the new
  lane row was inserted at `test-evidence-lanes.toml:97`, every later manifest row moved one line, so
  this card's lane citations were re-derived against the current file rather than carried
  (`test_cross_master_concurrency.py` `:146` → `:147`, `test_leaf_doc_master_link_binding.py` `:154` →
  `:155`, the playthrough `:157` → `:158`, the pause pair `:163`/`:196` → `:164`/`:197`,
  `test_terminal_blocker_reasons.py` `:178` → `:179`). Three further rows were re-read against their
  sources in the same pass: the L36 cross-master case ranges were rebound to the current function
  extents (`131-162; 409-456; 473-507; 509-568; 754-822; 722-750` — the previous set was stale and its
  last range ended past the end of the 847-line module), the nine `evidence-lifecycle.toml` rows for
  `test_terminal_blocker_reasons.py` were re-pointed to the nine lines that carry it
  (`304, 379, 423, 553, 592, 631, 943, 1000, 1026`; the previous nine were stale and the last was past
  the 1029-line end), and one row whose anchor
  (`test_a_code_tip_with_no_attributing_memory_commit_refuses_by_name`) exists nowhere in the code tree
  was re-worded onto the surviving `map_official_memory` fixture method instead of keeping an unbacked
  claim. The working-candidate table was also rewritten into the canonical `Finding | Anchor | Source`
  shape it was missing. Lane membership is classification only, not
  execution or acceptance evidence; verification metadata remains closeout-owned and no stamp
  advanced.
- 2026-09-15T11:18:00+00:00 — 260831-LOCR-L38 verification envelope (uncommitted change set on
  `ar/260831-locr-l38`, base `67b21aeb`): route impact for the two changed modules, both already in
  this route's table. `test_pause_stop_only_end_to_end.py` went from eight cases to ten and the
  stop route row now records the ten independently-failing cases and the **four** refusal shapes it
  keeps apart — a leaf contract, a record this contract does not own, an unreadable record, and a
  vacant record naming another master (`selected-contract-mismatch`) — plus the guard-order fact that
  an *active* foreign record is refused one step earlier by the observation, so the two foreign cases
  prove different guards. The `test_tools.py` route row gained the description-pin half it was
  missing: both registered descriptions are pinned as text, and the stop's now also pins the removed
  `atomic-series-activation-selection-missing` refusal **out** while keeping the release it does
  perform pinned in. Reference rows re-derived for both modules (the pause proof is now
  `86-556` with the ten case ranges, `_world` `150-168`, the two new cases `445-471` and `473-526`;
  `PublicSurfaceInventoryTests` is `220-341`). **Three pre-existing out-of-bounds citations in this
  document were recorded by that pass as left-as-found and reported, not repaired**, because they
  belong to other leaves' modules and were outside that change set: the recorded flake note
  (`test_checkpoint_landing_end_to_end.py:835-835`, file now 479 lines), the L36 cross-master forcing
  row (`test_cross_master_concurrency.py:784-852`, file now 847) and an L8 evidence-registry row
  (`evidence-lifecycle.toml:1038-1038`, file now 1029). **Update (260831-LOCR-L27 curator): the L36
  row has since been repaired** — it was an `error`-severity finding against *this* document, which
  this leaf was editing, so it was corrected here rather than carried. All six of its ranges were
  re-derived from the module and the module-level `_checkpoint_with_candidate` was dropped as an
  anchor, since it is a helper rather than a test the row claims. The other two remain unrepaired and
  reported: neither names this document, so they stay with their owning leaves. Verification metadata
  remains closeout-owned; no verification stamp advanced and no acceptance claim.

- 2026-09-15T13:18+02:00 — 260831-LOCR-L38 verification envelope (uncommitted change set on
  `ar/260831-locr-l38`, base `67b21aeb`): route impact for the two changed modules, both already in
  this route's table. `test_pause_stop_only_end_to_end.py` went from eight cases to ten and the
  stop route row now records the ten independently-failing cases and the **four** refusal shapes it
  keeps apart — a leaf contract, a record this contract does not own, an unreadable record, and a
  vacant record naming another master (`selected-contract-mismatch`) — plus the guard-order fact that
  an *active* foreign record is refused one step earlier by the observation, so the two foreign cases
  prove different guards. The `test_tools.py` route row gained the description-pin half it was
  missing: both registered descriptions are pinned as text, and the stop's now also pins the removed
  `atomic-series-activation-selection-missing` refusal **out** while keeping the release it does
  perform pinned in. Reference rows re-derived for both modules (the pause proof is now
  `86-556` with the ten case ranges, `_world` `150-168`, the two new cases `445-471` and `473-526`;
  `PublicSurfaceInventoryTests` is `220-341`). **Three pre-existing out-of-bounds citations in this
  document were recorded by that pass as left-as-found and reported, not repaired**, because they
  belong to other leaves' modules and were outside that change set: the recorded flake note
  (`test_checkpoint_landing_end_to_end.py:835-835`, file now 479 lines), the L36 cross-master forcing
  row (`test_cross_master_concurrency.py:784-852`, file now 847) and an L8 evidence-registry row
  (`evidence-lifecycle.toml:1038-1038`, file now 1029). **Update (260831-LOCR-L27 curator): the L36
  row has since been repaired** — it was an `error`-severity finding against *this* document, which
  this leaf was editing, so it was corrected here rather than carried. All six of its ranges were
  re-derived from the module and the module-level `_checkpoint_with_candidate` was dropped as an
  anchor, since it is a helper rather than a test the row claims. The other two remain unrepaired and
  reported: neither names this document, so they stay with their owning leaves. Verification metadata
  remains closeout-owned; no verification stamp advanced and no acceptance claim.
- 2026-09-15T11:15:00+00:00 — 260831-LOCR-L10 curator: recorded the route's new state-signal crash/restart recovery executor (`test_state_signal_restart_recovery.py`, unit-regression row `:101`) — a route-table row plus a section carrying the durable order it forces, the seven cases, the non-vacuity witness, and the review verdict's coverage limit that the fence's reachable route is the boundary drain rather than the generic finder. Route purpose, lane membership accounting and every other module's coverage claim are unchanged by this leaf.

## 260915-KS-L1 The Knowledge Storage Suite And Its Registered Fixture

This route gained one test module and one governed support module, and both are load-bearing for the repository's
own evidence machinery rather than only for the leaf.

`mcp/tests/test_knowledge_store.py` — 23 nodes, all in the **unit-regression** lane and carrying no integration
marker. (The 23rd arrived with `KS-R03`: it pins the identity operation's two-caller repeat contract, which the
candidate-batch refactor had silently changed. See the KS-L3 section below.) It is the executable counterpart of the knowledge requirement's failure list: the divergent-successor
read, identity reuse with differing content, dangling and cross-invariant predecessors, the two-branch lineage
refusal, database-level immutability, the seal covering the predecessor set, the schema-generation validation and
the layer-direction guard. Two of its nodes are enforcement-load-bearing in the sense that disabling the mechanism
makes a named node fail, which is what makes the guard's coverage real rather than apparent.

Its registration matters twice over. `mcp/tests/test-evidence-lanes.toml` gained the module in `unit-regression`
because a test module with no explicit lane makes `load_lane_manifest` refuse the whole repository, which
`evidence_lanes.pytest_collection_modifyitems` turns into a collection error and the quality path swallows into a
run without retry proof. Registering it is therefore a precondition for the certifying collection path to start at
all, and it is classification only — never execution or acceptance evidence.

`mcp/tests/knowledge_fixture_test_support.py` — the shared branching fixture (one repository, one invariant, a base
`I0` and two `v2` successors `I-A`/`I-B`), built through the real typed operations rather than by inserting rows.
It is registered in `mcp/tests/evidence-lifecycle.toml` as contract `knowledge-identity-branching-fixture` with an
explicit `[[artifact]]` row (`shared-support`, `internal-canonical`, `unit-regression`, `in-process`, `permanent`,
`consumer_scope = "exact"`, one observed consumer).

The fixture's **location is part of its contract, not a preference**. `governed_artifact_paths` discovers durable
support under `mcp/tests/**` plus a small fixed root set; `mcp/test_support/**` is not governed, so the same module
at `mcp/test_support/agents_remember_test_support/testing/knowledge_fixture.py` could not be registered at all —
it is refused both as an ungoverned catalogued path and because a module outside the test roots has no derivable
test-consumer proof. This paragraph exists so a later reader does not "tidy" the module back under `test_support/`
and silently break the registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| The knowledge suite and its unit-lane placement (row 74 after the KS-L3 insertions). | "mcp/tests/test_knowledge_store.py" | mcp/tests/test-evidence-lanes.toml:106-106 |
| The suite's one-to-one card, which enumerates what each node protects. | "# mcp/tests/test_knowledge_store.py" | onboarding/mcp/tests/test_knowledge_store.py.md:1-125 |
| The fixture's registered stable contract row and its matching artifact row. | "id = \"knowledge-identity-branching-fixture\"" | mcp/tests/evidence-lifecycle.toml:25-25 |
| The fixture's one-to-one card, including the relocation rationale. | "The shared branching knowledge fixture." | onboarding/mcp/tests/knowledge_fixture_test_support.py.md:19-26 |
| The enforcement-load-bearing nodes a disabled guard fails (re-cited after the KS-L3 node insertion shifted the file). | `test_lineage_guard_refuses_a_candidate_descending_from_a_stored_cycle`; `test_lineage_guard_fires_before_the_candidate_insert` | mcp/tests/test_knowledge_store.py:494-546; mcp/tests/test_knowledge_store.py:590-623 |
| The manifest rule that makes an unregistered module a hard load failure. | `load_lane_manifest` | mcp/test_support/agents_remember_test_support/testing/lane_manifest.py:99-144 |
| The fixture builder the suite composes — re-cited against the working tree, where the same builder gained the graph half. | `build_branching_knowledge_fixture` | mcp/tests/knowledge_fixture_test_support.py:203-263 |

## 260915-KS-L2 The Graph Suite And The Corrected Fixture Registry

This route gained four test modules and one governed support module, and — like the L1 increment — two of them are
load-bearing for the repository's own evidence machinery rather than only for the leaf.

`mcp/tests/test_knowledge_family_revision.py` (9 nodes), `test_knowledge_relation_rules.py` (12 nodes) and
`test_knowledge_graph_reads.py` (6 nodes) are the executable counterpart of the graph requirement's failure list:
a guarantee that must not change behind an existing family revision, the two predecessor refusals on the family
lineage, the two-branch lineage wording, the shared rule the family graph applies, endpoint refusals that leave the
whole-database row counts unmoved, the anchored-claim transaction that leaves no orphan anchor on a refusal path,
pair uniqueness versus identity reuse, the stale-caller removal contract, the database-level payload and foreign-key
enforcement, the namespace sweep, and the identity-set equality of the forward and reverse reads. All are in the
**unit-regression** lane and carry no integration marker.

`mcp/tests/knowledge_revision_seals.py` (5 nodes) is a **fix-verification** module and needs a word of explanation,
because its existence is itself a finding's outcome. The round-1 evidence claimed every guard the leaf added was
load-bearing, but no mutation of the sealed predecessor field was caught by any node in the repository (sealed
finding `260915-KS-L2-RV-1`): the node named for the seal also varied `revision_id`/`display_version`, so its
assertion held for a reason other than the field it named. The repaired node now holds every other sealed field
equal, and this module extends the same isolation to the invariant payload and to the read path on both graphs in
both directions. A future reader should take the general rule from it: **a test named for a sealed field must vary
only that field, and removing the field from the payload must make that named node fail.**

`mcp/tests/knowledge_graph_test_support.py` is the new governed support module, registered in
`mcp/tests/evidence-lifecycle.toml` as contract `knowledge-graph-case-support` with exactly three declared
consumers (the three graph modules; the seals module builds its own seeds and does not import it). It follows the
L1 fixture's design rule — every fixture value is built through the public typed operations — and its two raw
writes exist precisely because the operations *forbid* the state the lineage rule is exercised against: a stored
cycle can only be constructed by hand.

**The fixture's registry row was corrected, not merely extended.** `knowledge_fixture_test_support.py` grew a
graph half inside the same builder (a second and third invariant, two overlapping families with a successor and a
same-label sibling, and three recorded realizations), which made its declared consumer list wrong: the row named
one module while five now import it. The validator derives each governed artifact's actual test importers and
refuses a differing declared set, so this was a real registry defect rather than a thin count. The row now declares
all five, and its source-version and permanence text says the same builder carries both scenarios. The artifact's
`introduced_by` stays `260915-KS-L1`: it was extended in place, not forked — which is the design rule the L1
paragraph above states, now demonstrated.

The lane registration is the same precondition it was at L1: four modules without explicit lanes would make
`load_lane_manifest` refuse the whole repository, which `evidence_lanes.pytest_collection_modifyitems` turns into a
collection error and the quality path swallows into a run without retry proof. Registration is classification only
— never execution or acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
|The four graph modules and their unit-lane rows (rows 69-73 after the KS-L3 insertions).|"mcp/tests/test_knowledge_family_revision.py" ; "mcp/tests/test_knowledge_graph_reads.py" ; "mcp/tests/test_knowledge_relation_rules.py" ; "mcp/tests/test_knowledge_revision_seals.py"| mcp/tests/test-evidence-lanes.toml:79-81; mcp/tests/test-evidence-lanes.toml:87-94; mcp/tests/test-evidence-lanes.toml:95-103 |
| The four graph modules and their unit-lane rows (rows 69-73 after the KS-L3 insertions). | "mcp/tests/test_knowledge_family_revision.py"; "mcp/tests/test_knowledge_graph_reads.py"; "mcp/tests/test_knowledge_relation_rules.py"; "mcp/tests/test_knowledge_revision_seals.py" | mcp/tests/test-evidence-lanes.toml:74-74; mcp/tests/test-evidence-lanes.toml:76-79; mcp/tests/test-evidence-lanes.toml:81-94; mcp/tests/test-evidence-lanes.toml:79-79; mcp/tests/test-evidence-lanes.toml:95-103 |
| The graph case-support contract and its three declared consumers. | "id = \"knowledge-graph-case-support\"" | mcp/tests/evidence-lifecycle.toml:30-30 |
| The corrected branching-fixture row, whose consumer list now names all six importers. | "id = \"knowledge-identity-branching-fixture\"" | mcp/tests/evidence-lifecycle.toml:25-25 |
| The field-isolating seal node and the four read-path nodes that make the seal's evidence honest. | "test_an_invariant_revision_digest_seals_its_predecessor_set"; "test_a_family_revision_read_refuses_after_a_predecessor_edge_is_added" | mcp/tests/test_knowledge_revision_seals.py:63-95; mcp/tests/test_knowledge_revision_seals.py:96-123 |
| The requirement's own falsifier: the two directions compared as identity sets. | "test_two_realizations_resolve_from_either_direction_with_the_same_claim_ids"; "test_overlapping_families_answer_both_directions_with_the_same_member_ids" | mcp/tests/test_knowledge_graph_reads.py:35-65; mcp/tests/test_knowledge_graph_reads.py:66-99 |
| The atomicity nodes: a refusal leaves the whole-database row counts unmoved. | "test_a_new_anchor_and_its_claim_are_one_transaction"; "test_a_membership_endpoint_that_does_not_exist_refuses_and_writes_nothing" | mcp/tests/test_knowledge_relation_rules.py:77-117; mcp/tests/test_knowledge_relation_rules.py:118-159 |
| The node that proves the family graph applies the invariant graph's own lineage rule. | "test_the_family_lineage_rule_matches_the_invariant_rule" | mcp/tests/test_knowledge_family_revision.py:266-324 |
| The graph support module's one-to-one card, which records its owner and consumer set. | "test support, not production code" | onboarding/mcp/tests/knowledge_graph_test_support.py.md:25-26 |
| The corrected fixture card, whose graph-half paragraph records the extension-in-place rule. | "which extends the same fixture" | onboarding/mcp/tests/knowledge_fixture_test_support.py.md:19-26 |

## 260915-KS-L3 The Candidate-Batch Suite, And The Guard A Passing Suite Could Not See

This route gained three test modules and one governed support module, and the fourth is a case where the missing
evidence was itself the defect.

`mcp/tests/test_candidate_batch_transaction.py` (27 nodes) is the requirement's verification evidence: the
all-or-nothing proof (mutating the rollback to a commit fails a named node), the database-caught rollback at a
**non-final** command, the competing-writer refusal, the lane and admission refusals, the preconditions, the
completed-graph lineage rule with a spy that fails when the shared rule is neutered, and the removal receipts.
`mcp/tests/test_candidate_batch_commands.py` (9 nodes) covers the closed union and the receipt's fidelity.
`mcp/tests/test_knowledge_label_operations.py` (6 nodes) exists because the batch path carries an **independent
copy** of the label expectation rule: deleting the CAS in `labels.py` left every batch case green (sealed finding
`260915-KS-L3-RV-4`), so the standalone operations needed their own module before the guard was load-bearing at
all. All three are in the **unit-regression** lane (rows 18-19 and 70).

`mcp/tests/candidate_batch_test_support.py` is the new governed support module, registered in
`mcp/tests/evidence-lifecycle.toml` as contract `candidate-batch-case-harness` with exactly two declared consumers
and an evidence node that is a real passing node. It builds its candidate through the **real seam** — an admitted
destination plus contexts resolved through `resolve_candidate_context` — so a case authors its batch against an
identity the application actually read; and it measures refusals through a **separately opened store**, which is
what makes "nothing was written" a measurement. Its one deliberate raw write exists because the typed operations
forbid the state a duplicate-pair case needs.

Two rules this leaf's evidence teaches, and both are about what a named node proves:

- **A node named for a mechanism must discriminate that mechanism.** The baseline round's "database-caught" node
  actually asserted the concept's own pre-check (removing it left the node green), and the "context digest" node
  asserted the model validator rather than the operation's re-derivation. Each is now split so the mutation that
  removes the mechanism fails the node that names it.
- **A green suite is not a preservation proof.** `test_knowledge_store.py` grew one node
  (`test_a_repeated_identical_invariant_is_no_change_and_a_relabel_refuses`) because 54 upstream cases passed while
  the refactor had silently changed `create_invariant`'s observable answer for an identical repeat.

| Finding | Anchor | Source |
| --- | --- | --- |
|The batch pair's unit-lane rows and the transaction module's atomicity nodes.|"mcp/tests/test_candidate_batch_commands.py" ; "mcp/tests/test_candidate_batch_transaction.py"| mcp/tests/test-evidence-lanes.toml:18-19 |
| The label-operations suite's row and the reason it exists as a separate module. | "mcp/tests/test_knowledge_label_operations.py" | mcp/tests/test-evidence-lanes.toml:93-93 |
| The candidate-batch case-harness contract, its artifact row, evidence node and exact consumer set. | "id = \"candidate-batch-case-harness\"" | mcp/tests/evidence-lifecycle.toml:35-35 |
| The branching fixture's row, whose consumer list gained this leaf's label suite. | "id = \"knowledge-identity-branching-fixture\"" | mcp/tests/evidence-lifecycle.toml:25-25 |
| The node that pins the identity operation's two-caller contract after the refactor broke it. | "test_a_repeated_identical_invariant_is_no_change_and_a_relabel_refuses" | mcp/tests/test_knowledge_store.py:180-217 |
| The two split nodes that keep the database path and the concept guard separately proven. | "test_a_database_refusal_mid_batch_names_the_command_that_actually_failed"; "test_the_membership_guard_refuses_a_pair_the_declared_unique_tuple_would_also_refuse" | mcp/tests/test_candidate_batch_transaction.py:993-1060; mcp/tests/test_candidate_batch_transaction.py:1062-1118 |

## 260915-KS-L5 The Merge Suites, Split By The Budget Their Contract Could Not Fit

This route gained two test modules and one governed support module, and the split between the two modules is a
**budget decision** rather than a classification preference: the unit population sits exactly at its declared
`unit_case_budget` of 1000 collected cases after this leaf, so the merge's whole contract is carried in five unit
cases and every scenario that needs its own world went to the integration lane.

`mcp/tests/test_knowledge_guarded_merge.py` (5 nodes, **unit-regression**, row 73) carries the contract in five
named nodes rather than one per scenario, and each node asserts the **whole** outcome — the state, the identity,
the refusal code, and that every input is byte-identical to what it was. What each node is the mutation target
for: the declared-manifest preflight (seven structural classes plus a reorder, a rename, a weakened trigger body, a
changed `user_version` and an absent or unreadable input); the **silent-omission** class, where a delta built over
a subset of the canonical tables is accepted by SQLite and refused by the coverage comparison *and* the replay; the
conforming merge into a closed, published candidate that carries no verdict field; the refusal taxonomy, including
the exact conflict-key assertion; and base resolution plus input integrity, including a criss-cross history with
two common bases and a side that rewrote a sealed revision in place.

`mcp/tests/test_knowledge_guarded_merge_boundaries.py` (6 nodes, **integration**, row 139) holds the scenarios that
each need their own three-commit Git world: the conflict-row identity on a row that is **not the first** the table
holds, a table carrying an insert alongside a conflicting update, the old-side key rule with the missing-key case,
and the three final-integrity checks — the structural one reachable through a dangling reference all three inputs
carry, and the applied-change and merged-candidate-immutability ones exercised as **policies** because their call
sites cannot be reached by a black-box case at all.

`mcp/tests/merge_case_test_support.py` is the new governed support module, registered in
`mcp/tests/evidence-lifecycle.toml` as contract `common-base-merge-cases` with exactly two declared consumers and
an evidence node that is a real passing node
(`test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate`). It authors every dataset through
the **real store operations** and closes it through SQLite's own backup; it builds a **real three-commit Git
world** in which the base is the two sides' parent, so the common base is a fact of the commit graph rather than of
the fixture's bookkeeping; it materialises each side's file out of its commit rather than from a working tree; and
its `shape` callback runs *before* the commits are built, so a case's unusual state is inside the history the merge
is asked to prove rather than a rewrite afterwards.

Two rules this leaf's evidence teaches, and both are about what a survivor means:

- **A broken mutation is not a killed guard.** The leaf's first matrix scored an `M16` survivor as killed because
  its mutant module raised `NameError` and every node failed; the harness now classifies each failure and refuses
  to score a `NameError`, `ImportError`, `SyntaxError` or collection error as a kill. Re-derived, the headline is
  **17 of 21 killed with four non-experiments**, each with its cause stated.
- **A guard whose call site is unreachable is described as one.** Two of the merge's postcondition guards cannot be
  falsified by a black-box case under this schema, and the freeze's contribution is invisible to a case for the
  same kind of reason. Each is recorded as a non-experiment beside the reason, with its *policy* exercised by a
  direct node, rather than presented as coverage.

| Finding | Anchor | Source |
| --- | --- | --- |
| The five-case unit module, its budget statement and the whole-outcome assertion rule. | "The unit population is at its declared ceiling" | mcp/tests/test_knowledge_guarded_merge.py:1-33 |
| The registered evidence node of `contract:common-base-merge-cases`. | "def test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate(" | mcp/tests/test_knowledge_guarded_merge.py:307-376 |
| The two conflict-identity boundary nodes that regression-guard the corrected old-side key. | "test_a_row_level_conflict_names_the_row_the_engine_refused"; "test_a_table_carrying_an_insert_and_a_conflicting_update_names_the_conflicting_row" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:100-132; mcp/tests/test_knowledge_guarded_merge_boundaries.py:135-162 |
| The reachable structural guard and the two direct-policy nodes for the unreachable call sites. | "test_a_candidate_carrying_a_foreign_key_violation_is_refused_by_the_structural_check"; "test_a_candidate_that_dropped_an_intended_change_is_refused" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:187-226; mcp/tests/test_knowledge_guarded_merge_boundaries.py:229-249 |
| The shared harness: the real three-commit world, the commit-materialised files and the build order. | `build_case`; `build_git_world`; `materialize_commit` | mcp/tests/merge_case_test_support.py:511-571; mcp/tests/merge_case_test_support.py:427-449; mcp/tests/merge_case_test_support.py:474-484 |
|  The governed-artifact registration and exact two-consumer list this leaf added. | "contract:common-base-merge-cases" | mcp/tests/evidence-lifecycle.toml:1273-1273  |
| The lane rows the two modules were registered in, and the budget statement they sit under. | `unit-regression`; `integration` | mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/test-evidence-lanes.toml:162-162; mcp/tests/test-evidence-lanes.toml:166-168; mcp/tests/test-evidence-lanes.toml:190-190 |
|  The governed-artifact registration and exact two-consumer list this leaf added. | "contract:common-base-merge-cases" | mcp/tests/evidence-lifecycle.toml:1273-1273  |
| The lane rows the two modules were registered in, and the budget statement they sit under. | `unit-regression`; `integration` | mcp/tests/test-evidence-lanes.toml:190-190 |
| The two guard docstrings that state their own call site's unreachability. | `require_applied_changes`; `require_immutable_revisions_preserved` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:169-211; mcp/src/agents_remember/memory/knowledge/merge_validation.py:104-152 |

## 260915-KS-L6 The Portable Suites, Split By The 1200-Line Limit

This route gained **two** test modules, both registered in the **integration** lane (rows 140-141), and the split
between them is a **file-size decision** rather than a classification preference: the roundtrip module reached
1155 lines and one file may not exceed the repository's 1200-line hard limit, so the boundary population is a
second module that **imports the first module's helpers** rather than copying them. There is still exactly one
definition of what an artifact, a refusal or a published row count is, and the two modules are one evidence set.

`mcp/tests/test_knowledge_portable_roundtrip.py` (18 nodes) holds the artifact contract and the export/import
population. Its cases are **consolidated by protected property** rather than split one per assertion — the
population has a declared ceiling and each node names the one failure it exists to catch:

- **Completeness** — one node mutates an artifact through thirteen defects (a dropped collection, a truncated
  table, an unknown table, a value the declared type cannot hold, a reordered or renamed column, a repeated key)
  and asserts the check that catches each; the filtered-response pair keeps it honest, because a projection is
  refused *because it is not the format* and a complete projection of the source tables does validate.
- **Refusal without partial acceptance** — the destination's file digest and the destination directory's contents
  are measured after the fact, so "nothing was published" is a measurement rather than a promise.
- **Preservation** — every stored ID, provenance value and relation endpoint is held to the round trip, and the
  `state_at_origin` **value** crosses while nothing promotes it.
- Two nodes make the contract's own claims measurable: the artifact this encoder produces is the one this reader
  accepts (so the round trip is a proof rather than a coincidence), and a dataset that came **through L5's merge**
  is exportable and restorable — the composition the next leaves consume.

`mcp/tests/test_knowledge_portable_boundaries.py` (6 nodes) holds the five properties the ordinary path cannot
fail from outside: the freeze's closure measured on the **published destination**; the canonical form of the whole
document (every non-canonical spelling axis, `canonical_document`'s assertions, and **all seven header keys
respelled with a different JSON type** — each refused, each passing the whole-document gate, which is what proves
the refusal is the header check's); the **staged sealed-aggregate read** with every retained row of both revision
tables tampered and the destination held byte-identical; destination admission before any staging work; and the
typed read of an artifact that is not readable UTF-8 text.

Two rules this leaf's evidence teaches, and both are about what a survivor means:

- **A reachable guard with no killing node is reported, not claimed.** The header's namespace-binding check
  (`export_portable.py:911`) is reachable and verdict-changing — removing it makes a byte-canonical artifact whose
  header names another namespace validate and install — and no node in the leaf's population kills it. It is
  written up as an **observation for L9** with its mutation and reachability proof rather than presented as
  coverage.
- **A non-canonical spelling is a different document, and the cases say which check refused.** The canonical node
  asserts the refusal's identity (`invalid_export`, `record_id == "<canonical document>"`) as well as the verdict,
  and the leaf's final round extended these cases rather than adding a case, so the population stayed at 255
  integration cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| The roundtrip module's three falsified properties, the helper set and the two claims made measurable. | "test_the_artifact_is_one_deterministic_document_of_the_declared_shape"; `artifact_of`; `envelope_of`; `import_into` | mcp/tests/test_knowledge_portable_roundtrip.py:317-342; mcp/tests/test_knowledge_portable_roundtrip.py:119-120; mcp/tests/test_knowledge_portable_roundtrip.py:123-124; mcp/tests/test_knowledge_portable_roundtrip.py:165-168 |
| **The node the leaf's guarantee rests on: the canonical form is the only form the reader accepts, including every header type.** | "test_the_canonical_form_of_the_whole_document_is_the_only_form_the_reader_accepts" | mcp/tests/test_knowledge_portable_boundaries.py:132-258 |
| **The staged sealed-aggregate read, with every retained revision row tampered.** | "test_an_artifact_whose_sealed_payload_contradicts_its_digest_is_refused" | mcp/tests/test_knowledge_portable_boundaries.py:534-582 |
| The import's close/verify step and the freeze's closure on the published destination. | "test_a_stage_opened_in_wal_mode_is_published_as_a_closed_database"; "test_a_frozen_snapshot_of_a_wal_resident_candidate_is_published_closed" | mcp/tests/test_knowledge_portable_boundaries.py:618-650; mcp/tests/test_knowledge_portable_boundaries.py:96-134 |
| The destination-admission and typed-read boundary nodes. | "test_destination_admission_refuses_before_any_staging_work"; "test_an_artifact_that_cannot_be_read_as_text_is_refused_with_a_typed_code" | mcp/tests/test_knowledge_portable_boundaries.py:623-680; mcp/tests/test_knowledge_portable_boundaries.py:686-736 |
| **The guard this leaf reports rather than claims: reachable, verdict-changing, no killing node.** | `bound` | mcp/src/agents_remember/memory/knowledge/export_portable.py:984-1005 |
| The two lane rows this leaf registered, and the three consumer lists it extended. | "integration = [" | mcp/tests/test-evidence-lanes.toml:170-170; mcp/tests/test-evidence-lanes.toml:183-190 |

## 260915-KS-L7 The Read Suites, And The Path Contract They Measure

This route gained **three** test modules and one **governed support artifact**, and the split between them is a
file-size decision as much as a classification one:

- `mcp/tests/test_knowledge_read_scope.py` — **unit-regression** (row `mcp/tests/test-evidence-lanes.toml:75`),
  21 nodes, hermetic: temporary directories, in-process APSW databases built through the public store
  operations, no repository working tree, no network. **It is at 1 163 of the 1 200-line limit, 37 lines of
  headroom, and L8 must split it before adding cases.**
- `mcp/tests/test_knowledge_read_boundaries.py` — **integration** (`:157`), 20 nodes over a real committed Git
  tree, a real published database and real snapshot/namespace refusals.
- `mcp/tests/test_knowledge_read_paths.py` — **integration** (`:158`), 5 nodes that measure Git's own
  `ls-tree` behavior with their own subprocess calls.
- `mcp/tests/read_scope_test_support.py` — the shared fixture, registered as an **artifact**
  (`shared-support` / `internal-canonical` / `unit-regression`) under the new contract
  `knowledge-read-scope-cases`, with the three modules above as its exactly-declared consumers. Fix round 2
  added the path module to that consumer list after splitting the over-limit integration module — a **consumer
  change, not a new artifact**.

**A new test module costs three registry touch-points and this leaf paid all three**: its lane row, its path in
the support artifact's `consumers` list, and the evidence-catalog digest re-pin
(`LIFECYCLE_CATALOG_SHA256` → `461121ca…`, with the contract/artifact counts 10/51) in
`mcp/tests/test_dependency_ownership_ast_helpers.py`. Miss any one and `load_lane_manifest` or the catalog
validator refuses the repository, so the failure is a **hard collection error rather than a quiet gap**.

**The path module is the one the review made load-bearing, and its contract is worth stating here because it
was corrected twice.** Git pathspec **magic** is the leading-`:` family (`:(exclude)`, `:!`, `:(top)`, `:/`)
plus `..`, absolute paths, `~`, drive/UNC spellings, backslashes and NUL; the characters `*`, `?` and `[` are
**literal characters** to `ls-tree` (measured on `git 2.54.0` by the case itself), so a legitimate anchor
containing them must be authorable, seedable and resolvable. Round 1 refused them, which made such an anchor
un-authorable and reported a file the tree really holds as `path_absent` — *a false statement about the
repository rather than a refusal of a malformed spelling*. The module therefore measures the three genuinely
different facts apart (`path_absent`, `unsupported_locator` with the cause in `detail`, and
`recorded_object_unavailable`), and it drives the two producers of the last one separately.

**Two honest limits travel with these suites, and neither is coverage.** `_tree_entry`'s **non-zero-exit**
branch is reachable by no input on this host; a published mutation claim that it was made reachable was
**withdrawn** by the leaf's own evidence erratum, because the kill that appeared to prove it also appears with
the production line untouched — so the branch stays an **explicitly disclosed unasserted defensive branch**
(L9 ledger **A6**) and must never be read as protection. And `_manifest_digest`'s inclusion of each item's
`selection_reasons` is a **reachable covered gap** with no killing node (L9 ledger **A4**).

**One more rule this leaf's evidence teaches, and it is about what a survivor means:** a sweep must run on the
frozen bytes it claims to describe. This leaf's first sweeps ran before the test module's last write, which is
why the published attribution of one kill was off by one line; the correction is in the erratum, and the
practical rule for a successor is to re-run the sweep after **any** edit rather than re-using a result.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The count semantics the review corrected, and the requirement's own non-conformance example.** | "test_a_page_budget_of_one_item_still_advertises_the_second_location" | mcp/tests/test_knowledge_read_scope.py:547-657 |
| **The completeness node that derives the mandatory set from recorded rows rather than from the implementation's own page manifest.** | "test_every_page_declares_the_same_snapshot_and_manifest_and_the_union_equals_the_selection" | mcp/tests/test_knowledge_read_scope.py:658-721 |
| The ordering node the review sealed as HIGH, and the truncated-page node. | "test_the_item_stream_is_ordered_by_stored_identity_and_never_by_an_authored_label"; "test_a_truncated_page_states_that_items_remain_rather_than_claiming_completeness" | mcp/tests/test_knowledge_read_scope.py:722-837; mcp/tests/test_knowledge_read_scope.py:838-871 |
| **The three path facts, and the case that authors, stores, seeds and resolves a path holding glob characters.** | "test_a_stored_path_that_cannot_be_addressed_is_refused_rather_than_reported_absent"; "test_a_path_holding_glob_characters_is_authorable_seedable_and_observed_as_its_blob" | mcp/tests/test_knowledge_read_paths.py:370-444; mcp/tests/test_knowledge_read_paths.py:256-369 |
| The lookup that ran and could not answer, refused as unavailable rather than absent. | "test_a_failed_tree_lookup_is_unavailable_rather_than_an_absent_path" | mcp/tests/test_knowledge_read_paths.py:445-538 |
| The lookup that could not be run at all, reported as the same fact. | "test_a_git_that_cannot_run_is_unavailable_rather_than_an_absent_path" | mcp/tests/test_knowledge_read_paths.py:539-644 |
| The continuation bindings, each with its own control, and the read-only property on a real file. | "test_a_continuation_that_binds_another_manifest_is_refused_and_its_own_is_verified"; "test_a_refused_read_of_a_real_database_leaves_the_file_byte_identical" | mcp/tests/test_knowledge_read_boundaries.py:664-724; mcp/tests/test_knowledge_read_boundaries.py:893-941 |
| The read fixture and its registered contract. | `build_read_scope_fixture`; "id = \"knowledge-read-scope-cases\"" | mcp/tests/evidence-lifecycle.toml:65-65; mcp/tests/read_scope_test_support.py:266-283 |
| The unit-lane row the read's selection module occupies. | "mcp/tests/test_knowledge_read_scope.py" | mcp/tests/test-evidence-lanes.toml:98-98 |
| The two integration-lane rows the read's boundary and path modules occupy. | "mcp/tests/test_knowledge_read_boundaries.py"; "mcp/tests/test_knowledge_read_paths.py" | mcp/tests/test-evidence-lanes.toml:171-171; mcp/tests/test-evidence-lanes.toml:173-175; mcp/tests/test-evidence-lanes.toml:188-197 |
| The read fixture and its registered contract. | `build_read_scope_fixture`; `knowledge-read-scope-cases` | mcp/tests/read_scope_test_support.py:266-284; mcp/tests/evidence-lifecycle.toml:1203-1207; mcp/tests/evidence-lifecycle.toml:1227-1247 |
| The unit-lane row the read's selection module occupies. | "mcp/tests/test_knowledge_read_scope.py" | mcp/tests/test-evidence-lanes.toml:98-98 |
| The two integration-lane rows the read's boundary and path modules occupy. | "mcp/tests/test_knowledge_read_boundaries.py"; "mcp/tests/test_knowledge_read_paths.py" | mcp/tests/test-evidence-lanes.toml:164-164; mcp/tests/test-evidence-lanes.toml:166-175; mcp/tests/test-evidence-lanes.toml:173-173; mcp/tests/test-evidence-lanes.toml:188-197 |
| **The catalog digest re-pin that a new test module obliges.** | `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-65 |

## 260915-KS-L8 The Comparison Suites, And The Evidence Rules They Teach

This route gained **two** test modules and one **governed support artifact**, and the split between them is a
classification rather than a size decision — both are well under the 1 200-line rail (840 and 779):

- `mcp/tests/test_knowledge_diff_scope.py` — **unit-regression** (row `mcp/tests/test-evidence-lanes.toml:76`),
  13 nodes, hermetic: temporary directories, two in-process APSW databases built through the public store
  operations (the candidate copied from the closed baseline and then curated through the store), and two
  local committed Git trees the fixture writes itself.
- `mcp/tests/test_knowledge_diff_boundaries.py` — **integration** (`:159`), 15 nodes over the same real trees
  but **driving the production Git probe** rather than a substitute, plus a real candidate write that moves
  the logical digest and the serialized response the forbidden-overreach case searches.
- `mcp/tests/diff_scope_test_support.py` — the shared two-snapshot fixture, registered as an **artifact**
  (`shared-support` / `internal-canonical` / `integration` / `local-composition`) under the new contract
  `knowledge-diff-cases`, with exactly those two modules as its declared consumers.

**A new test module costs three registry touch-points and this leaf paid all three twice**: its lane row, its
path in the relevant artifact's `consumers` list, and the evidence-catalog digest re-pin
(`LIFECYCLE_CATALOG_SHA256` → `4cf81f10…`, counts **11 / 52**) in
`mcp/tests/test_dependency_ownership_ast_helpers.py`. It also added the two modules to the **read-scope**
artifact's consumer list, because the diff fixture builds on the read fixture — a consumer change, not a new
artifact. The catalog is now **52 artifacts and 11 contracts**, measured by counting the blocks and hashing
the file, and the lane manifest is **243 declared entries against 243 modules on disk**.

**The coverage-rule reason is the most-corrected contract of this leaf, and its direction is measured rather
than argued.** Rule 1 is load-bearing alone (removing it turns a missing selection into a real absence,
`absent_from_snapshot` where `present_outside_selection` is owed). Rule 2 **cannot decide a state its
neighbours do not** — an authored edge is a foreign key into the snapshot that declares it — so it is kept as
a short-circuit, and the case asserts its **invariant** half through the published read surface while stating
that its **family** half is unexercised, because the fixture authors 0 `family_predecessor` rows. Rule 3 is
load-bearing in the direction that forces its answer **present**: forcing it present turns a genuinely
deleted realization into a missing selection (two kills), while forcing it **absent** changes no asserted
state on this population — variant `C` survives all 28 nodes — because the three items it answers for are
really absent. **Collapsing the three into one is wrong because it turns a missing selection into a real
absence**, the reverse of what the leaf first claimed; the `2 failed` an earlier artifact published for `C`
belongs to variant `G`.

**Three evidence rules this leaf's own history teaches, and they are the reason its documentation debt is
carried rather than papered over:**

- **A citation of a frozen file must be regenerated from that file.** This leaf published a `M25`/`M26`
  line-number pair under the words *"regenerated from the frozen file"* that is the **pre-round** file's
  numbering: on the frozen 779-line module `M26`'s node is at **`:603`** and its failing assertion at
  **`:658`**, and `M25`'s at **`:678`** / **`:716`** — not the `565`/`620` and `640`/`678` the artifacts
  republish. It is carried to `KS-R09`/`L9` (ledger **A9**, finding **`L8-W1`**) with the replacement text
  supplied, and **the ledger is authoritative for it**; this route's own cards cite the measured numbers.
- **A row table attributed to the frozen bytes must have been measured on them.** This leaf's row tables were
  measured **before** its own last edit — **the same class as `L7-X6`** and now its **second instance** — and
  every verdict still reproduces on the frozen bytes under the final verification round's own instrument.
- **A survivor needs a hand-run before it is believed.** An `A2` sentinel that fingerprinted
  `repr(code.co_consts)` was a **false positive by construction** (a nested code object's `repr` is a heap
  address) and reported `LOADED-CODE-CHANGED` on a completely unmutated mirror; the leaf withdrew every
  citation of it and adopted the verifier's content-only fingerprint, whose negative control refuses the run
  when the declared target did not move. **A sweep whose sentinel cannot fail is not evidence.**

**Four non-kill classes travel with these suites and none of them is coverage:** `M4`, `M8` and `M27` are
**covered gaps** against this leaf with their closers named, `M23` is a **non-experiment** with its
reachability bound carried rather than resolved, and `M9`, `M12` and `M21` are **equivalent mutants** with
the measurement that proves the equivalence. The corrected taxonomy over `M1`…`M27` is **19 assertion kills,
1 exception death, 3 equivalent mutants, 3 covered gaps, 1 non-experiment = 27**, and **nothing was skipped,
xfailed, deselected, widened or deleted to reach it** — the final round reproduced all of it with its own
instrument (39 mutation applications, 126 scored node runs, 41 assertion kills, 1 exception death, 0 broken
mutations, 0 refusals).

| Finding | Anchor | Source |
| --- | --- | --- |
| **The packet's first non-conforming example, and the node `M1`/`M2` kill.** | "test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union" | mcp/tests/test_knowledge_diff_scope.py:309-342 |
| **The present-outside-versus-absent distinction side by side, and the per-table rule-2 subsumption assertion.** | "test_a_record_the_other_snapshot_holds_but_the_selection_missed_is_not_an_absence" | mcp/tests/test_knowledge_diff_scope.py:424-530 |
| **`M26`'s node on the frozen file: the limitation validator, failing assertion at `:658`.** | "test_a_comparison_that_declares_a_limit_it_did_not_establish_fails_construction" | mcp/tests/test_knowledge_diff_scope.py:603-675 |
| **`M25`'s node on the frozen file: the truncated comparison, failing assertion at `:716`.** | "test_a_truncated_comparison_cannot_be_presented_as_a_complete_one" | mcp/tests/test_knowledge_diff_scope.py:678-739 |
| **The forbidden-overreach case: nine verdict words searched over the serialized response, with a positive control.** | "test_no_field_of_a_comparison_can_carry_a_strengthening_or_harmlessness_verdict" | mcp/tests/test_knowledge_diff_boundaries.py:481-507 |
| **The node that drives a real candidate write and refuses its continuation, and the substituted-snapshot refusal.** | "test_a_candidate_that_changed_after_a_continuation_refuses_the_continuation"; "test_a_side_naming_another_snapshot_of_its_own_file_refuses_before_any_page" | mcp/tests/test_knowledge_diff_boundaries.py:325-363; mcp/tests/test_knowledge_diff_boundaries.py:438-475 |
| The expansion, the visible unattributed gap, and the filter that narrows the display and never the comparison. | "test_the_expansion_names_both_requested_trees_and_every_path_they_differ_at"; "test_a_changed_path_no_recorded_realization_attributes_is_listed_as_a_visible_gap"; "test_a_role_filter_narrows_the_display_and_never_the_comparison" | mcp/tests/test_knowledge_diff_boundaries.py:145-182; mcp/tests/test_knowledge_diff_boundaries.py:185-218; mcp/tests/test_knowledge_diff_scope.py:536-573 |
| **The fixture and the governed contract it is registered under.** | `build_diff_fixture`; "id = \"knowledge-diff-cases\"" | mcp/tests/diff_scope_test_support.py:189-233; mcp/tests/evidence-lifecycle.toml:60-60 |
| **The two lane rows this leaf registered.** | "mcp/tests/test_knowledge_diff_scope.py"; "mcp/tests/test_knowledge_diff_boundaries.py" | mcp/tests/test-evidence-lanes.toml:86-88; mcp/tests/test-evidence-lanes.toml:172-174; mcp/tests/test-evidence-lanes.toml:88-88; mcp/tests/test-evidence-lanes.toml:94-101; mcp/tests/test-evidence-lanes.toml:189-196 |
| **The fixture and the governed contract it is registered under.** | `build_diff_fixture`; `knowledge-diff-cases` | mcp/tests/diff_scope_test_support.py:189-233; mcp/tests/evidence-lifecycle.toml:1198-1202 |
| **The two lane rows this leaf registered.** | "mcp/tests/test_knowledge_diff_scope.py"; "mcp/tests/test_knowledge_diff_boundaries.py" | mcp/tests/test-evidence-lanes.toml:81-88; mcp/tests/test-evidence-lanes.toml:165-174; mcp/tests/test-evidence-lanes.toml:88-88; mcp/tests/test-evidence-lanes.toml:94-101; mcp/tests/test-evidence-lanes.toml:189-196 |
| **The catalog digest re-pin that a new test module obliges.** | `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-65 |

## 260915-KS-L11 The Facet Suite, And The Ceiling It Was Written Against

This route gained **one unit-regression module and one governed support artifact**, and the split between
them is a capability decision rather than a size one:

- `mcp/tests/test_knowledge_facets.py` — **unit-regression** (row `mcp/tests/test-evidence-lanes.toml:71`),
  **17 nodes**, hermetic: temporary directories, in-process APSW databases built through the production
  application seam, and one recorded generation-2 fixture.
- `mcp/tests/facet_test_support.py` — the shared harness, registered as an **artifact**
  (`shared-support` / `internal-canonical` / `unit-regression` / `in-process`) under the contract
  `knowledge-facet-cases`, with exactly one declared consumer. It owns the two things no single case can:
  one **admitted** candidate (whose provenance comes from the admission) and one **recorded** dataset whose
  serialized page and result digests were measured on the base revision **before this leaf existed**.

**The case ceiling is why the module carries loops rather than parametrizations, and that is a cost stated
rather than hidden.** The unit population's declared budget had twenty slots left when this leaf landed and
the repository's own record forbids a KS leaf from raising it, so the per-subtype and per-endpoint-kind
variants are driven *inside* the case that owns their property, with every assertion naming the subtype or
kind it is about. What that costs is independent failure attribution between variants of one property; what
it preserves is every clause, and a population that runs at all — an over-budget population raises
`UsageError` and executes zero tests. The population was then **1250 unit cases against the
`unit_case_budget = 1250`** ceiling, with integration at 322 — the measurement taken at this leaf's own
candidate. The master's owning seat has since raised the pair to `unit_case_budget = 1500` and
`integration_case_budget = 400` at the later `260915-KS-L24` candidate, so the ceiling this section is
titled after no longer reads the same; see that section below.

**This leaf is the one that renders the earlier leaves' byte-identity claim checkable.** The recorded fixture
is built from generation 2's own recorded DDL with fixed identities and a fixed authorship instant, and the
case compares the shipped read's serialized page and result against constants measured before the leaf
existed — so "`KS-R07@v1`'s selection did not move" is a before/after observation rather than a
self-consistency check. The same fixture's dataset digest is asserted equal to its pre-leaf value.

**Three registry touch-points a new test module obliges, and this leaf paid both sides of each:** its lane
row, its path in the relevant artifact's `consumers` list, and the evidence-catalog digest re-pin
(`LIFECYCLE_CATALOG_SHA256` → `19ed0525…`, counts **13 contracts / 54 artifacts**) in
`mcp/tests/test_dependency_ownership_ast_helpers.py`, plus the new artifact's own contract row for the
support module. Missing any one of them is a hard collection error rather than a quiet gap.

**Two honest limits travel with this suite and neither is coverage:**

- **Completeness of the run is host-dependent and was reported as such.** The brief's literal combined
  command does not execute on this host because five anyio-affected modules fail to *import* under
  `filterwarnings = ["error", …]`; the leaf quotes the run **with** the documented `-W
  "ignore::DeprecationWarning"` override (the pre-existing D-7 defect routed to L9) and states both facts
  rather than one. Its own module passes 17/17 without the override.
- **The two checks the leaf did not run are named**: the contract-scoped memory-quality operation with the
  `curator_coherence` authority (the curator seat's step), and `--certify`.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The byte-identity node: the shipped page and result compared against digests measured before this leaf existed.** | "test_the_shipped_seed_page_is_byte_identical_and_the_facet_page_is_its_own_policy" | mcp/tests/test_knowledge_facets.py:1194-1194 |
| **The exact facet page, the empty-but-real selection, the incompleteness refusal and the damaged-seal refusal.** | "test_a_facet_does_not_join_a_shipped_seed_and_the_facet_page_is_exact" | mcp/tests/test_knowledge_facets.py:1246-1246 |
| **The harness that owns the admitted candidate and the recorded fixture.** | `build_admitted_candidate`; `build_recorded_fixture`; `PRE_LEAF_PAGE_DIGEST` | mcp/tests/facet_test_support.py:177-192; mcp/tests/facet_test_support.py:535-658; mcp/tests/facet_test_support.py:96-96 |
| **The governed contract and artifact this leaf registered, with its one declared consumer.** | "id = \"knowledge-facet-cases\"" | mcp/tests/evidence-lifecycle.toml:55-55 |
| The catalog digest re-pin a new test module obliges. | `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-46 |
| The lane row this module is registered under. | "mcp/tests/test_knowledge_facets.py" | mcp/tests/test-evidence-lanes.toml:89-89 |
| **The unit ceiling this route's suites collect against, cited as the pinned key and value — the L11 suite was written against 1250, the `260915-KS-L24` candidate raised it to 1500, this candidate's owning seat raised it again to 1600, and the merge onto the moved super line raised it to 2200 over the merged 2035-case population.** | "unit_case_budget = 2200" | pyproject.toml:214-214 |
| **The refusal an over-budget population raises, which is why the loops live inside their cases.** | `UsageError` | mcp/tests/conftest.py:104-140 |

## 260915-KS-L24 The Coherence Tool States Its Own Publication Inputs

This route's final-certification module is where the curator-coherence request contract is pinned, and
this leaf is the one that made the tool state its own inputs:

- **18 new cases in `mcp/tests/test_final_full_memory_coherence_certification.py`**, which grows 943 ->
  1190 lines. Nine parametrized items drive one omitted publication member each, so no member is
  accidentally satisfied by another's presence; one case drives all nine omitted; a positive control
  asserts the declaration equals the request model's own field order **and** that a nine-member request
  validates; one case drives the real `_prepare` and asserts its summary text; one extends the shared
  declaration in a scratch request model and asserts the new member reaches **both** messages with
  neither text edited; three parametrized items cover `status`/`prepare`/`validate`, plus one
  multi-field forbidden refusal that includes `judgments`; and one pins the byte-identical
  `freeze_snapshot` message.

- **What the cases protect is a message, and the message is the requirement.** `publish` required nine
  non-`None` request members while two of them (`semantic_requirement_revision`, `delivery_attempt`)
  were declared `default=None`, were **not** returned by `prepare`, and were **not** named by the
  refusal. Two leaves of this master read that refusal as an impassable tool defect and carried an
  unpublished coherence authority as an external blocker (`notes/DISCLOSURES.md` D-11). The request
  model now refuses by naming the missing members and the read actions name the publication-only field
  they received, so these cases are what stops the message from drifting back.

- **The suite stayed inside the budget raise this master's owning seat made.** This candidate collects
  **1268 unit cases against `unit_case_budget = 1500`** and **322 integration cases against
  `integration_case_budget = 400`**; the raise is the owning seat's change and not this leaf's delivery,
  and the 18 cases consume 18 of the 250 unit slots it added. The module is at 1190 of the repository's
  1200-line rail, so the next leaf that adds curator-coherence cases there must split it first.

- **The card's own `_affected_plan` / `_coherence` / `_evidence` coordinates moved by this leaf.** The
  three import insertions shifted every definition below them by nine lines; the module's card now
  carries the measured extents rather than the pre-leaf ones.

| Finding | Anchor | Source |
| --- | --- | --- |
| The publish refusal names the one omitted member, for each of the nine. | "test_publish_refusal_names_the_one_missing_publication_member" | mcp/tests/test_final_full_memory_coherence_certification.py:1059-1076 |
| The all-nine refusal names every member in declaration order. | "test_publish_refusal_without_any_member_names_all_nine_in_declaration_order" | mcp/tests/test_final_full_memory_coherence_certification.py:1079-1089 |
| The positive control binds the declaration to the request model's own field order. | "test_publish_with_every_publication_member_validates" | mcp/tests/test_final_full_memory_coherence_certification.py:1092-1108 |
| The prepare text is asserted from the real `_prepare` path. | "test_prepare_states_the_complete_publication_input_set" | mcp/tests/test_final_full_memory_coherence_certification.py:1111-1124 |
| A member added to the declaration reaches both messages with neither text edited. | "test_a_member_added_to_the_declaration_reaches_both_messages" | mcp/tests/test_final_full_memory_coherence_certification.py:1127-1147 |
| The sibling refusal names the supplied member for each read action. | "test_non_publish_actions_name_the_publication_member_they_received" | mcp/tests/test_final_full_memory_coherence_certification.py:1150-1163 |
| The multi-field refusal names every supplied field in model order, `judgments` included. | "test_non_publish_refusal_names_every_supplied_field_in_model_order" | mcp/tests/test_final_full_memory_coherence_certification.py:1166-1180 |
| The freeze branch keeps its own named refusal. | "test_freeze_snapshot_keeps_its_own_named_refusal" | mcp/tests/test_final_full_memory_coherence_certification.py:1192-1192 |

## 260915-KS-L14 The Detection Suites, The Registry Rows They Obliged, And Two Re-Scoped Facet Cases

This route gained **two new unit-regression modules and no new governed artifact**:

- `test_knowledge_detection_signals.py` — **28 collected cases from 20 definitions**, one of them a
  nine-parameter construction table over every required field of a detection signal. It measures a typed
  record's own construction boundary: the declared field-set review against the closed conclusion-name
  list, an extra conclusion-shaped field refused, a verdict written into the prose field refused, the
  closed and versioned condition vocabulary, the granularity refusal that stops a whole-file change
  standing for a span change, the three declared input sets with their three distinct refusals, the
  declaration/omission agreement checked in both directions, retention refused at a destination that
  cannot retain, currentness that marks a run stale without relabelling it, the predating-dataset refusal
  with both generation numbers as facts, and generation 4's additive rule asserted as the prefix equality
  `GENERATION_4.tables[: len(GENERATION_3.tables)] == GENERATION_3.tables`.
- `test_knowledge_detection_runs.py` — **19 cases**. It has two halves and says so: a synthetic half that
  builds union items, family memberships and anchor resolutions so each condition is provoked exactly, and
  a store half that opens a real detection store and drives `record_detection_run`/`read_detection_run`
  through it. One case runs a **real** two-snapshot comparison through the shipped application seam, so
  the walk is shown consuming real comparison output rather than a shape invented beside it.

**The registry touch-points, and the one this leaf did not pay.** A plain test module needs a lane row, and
both modules were added to `unit-regression` in `mcp/tests/test-evidence-lanes.toml` — a two-line insertion
that shifts every later line of that file, which is why this route's and other routes' citations to it
moved. The governed-artifact side is the interesting one: the run module uses the **already-registered**
`diff_scope_test_support` and `read_scope_test_support` fixtures rather than a third support module, so
this leaf added **no artifact and no contract** — only two `consumers` rows in
`mcp/tests/evidence-lifecycle.toml`, and the counts stay at **13 contracts and 54 artifacts**. The pinned
catalog digest in `test_dependency_ownership_ast_helpers.py` therefore had to be **re-pinned deliberately**
(`c6956899…`), with the reason written beside the constant rather than the value changed silently.

**Two shipped facet cases were re-scoped, not deleted.** Appending generation 4 falsified exactly two
assertions in `test_knowledge_facets.py`, both of which stated the *shared* substrate's membership as a
closed list this leaf legitimately grew. Each keeps its protected property and gains the replacement fact:
the seam-registry case now states the three groups the registry declares — the internal conformance kind,
the eight facet kinds and the two detection kinds — and states the facet half *more* precisely than before
by asserting `KIND_SCHEMAS[kind] == {FACET_RECORD_SCHEMAS[kind]}` for each of the eight; and the
generation case now asserts the registry is `[1, 2, 3, 4]` with `GENERATION_3` still a member at
`user_version == 3` and `CURRENT_GENERATION is GENERATIONS[-1]`, so the created generation is named as
"the newest registered one" rather than pinned to a literal the next generation would falsify. Every
generation-3-specific assertion in that case is unchanged. Both carry a `RE-SCOPED for KS-R14@v1`
paragraph in their docstring saying what changed and why.

**One pre-existing defect is reported here rather than worked around.** The literal combined-suite command
`pytest mcp/tests -q` collects four errors in `mcp/tests/test_static.py` from a third-party `anyio`
deprecation escalated by the repository's warning filters; the module is untouched by this leaf, and the
documented `-W "ignore::DeprecationWarning"` override is what makes the same command green (1637 passed,
306 subtests). Both facts are stated in the leaf's worker report rather than one of them.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The signal suite's 28 cases, including the nine-parameter required-field table and the two halves of "a conclusion is unrepresentable".** | "test_the_signal_field_set_is_required_and_carries_no_conclusion_bearing_field"; "test_a_signal_missing_a_required_field_fails_construction"; "test_a_verdict_written_into_the_detail_string_is_refused_as_the_same_defect" | mcp/tests/test_knowledge_detection_signals.py:189-222; mcp/tests/test_knowledge_detection_signals.py:223-246; mcp/tests/test_knowledge_detection_signals.py:265-284 |
| **The generation-4 additive rule asserted as the prefix equality it is, with the appended table, its key tuple and its two triggers.** | "test_generation_4_appends_only_and_the_first_twenty_names_are_generation_3_s" | mcp/tests/test_knowledge_detection_signals.py:724-751 |
| **The run suite's scenario/control case, the case that consumes a real shipped comparison, and the sealed-sequence case.** | "test_a_budget_change_and_a_comments_only_change_produce_the_same_condition_and_signal"; "test_the_walk_consumes_the_shipped_comparison_and_emits_facts_only_signals"; "test_a_recorded_detection_sequence_cannot_be_reordered_or_shortened" | mcp/tests/test_knowledge_detection_runs.py:293-324; mcp/tests/test_knowledge_detection_runs.py:493-540; mcp/tests/test_knowledge_detection_runs.py:769-799 |
| **The run module's lane row.** | "mcp/tests/test_knowledge_detection_runs.py" | mcp/tests/test-evidence-lanes.toml:85-85 |
| **The signal module's lane row.** | "mcp/tests/test_knowledge_detection_signals.py" | mcp/tests/test-evidence-lanes.toml:86-86 |
|**The diff-comparison contract whose consumer list gained the run module (the consumer row is the third entry of that block).**|"contract:knowledge-diff-cases"| mcp/tests/evidence-lifecycle.toml:1382-1382 |
|**The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).**|"contract:knowledge-read-scope-cases"| mcp/tests/evidence-lifecycle.toml:1402-1402 |
| **The deliberately re-pinned catalog digest, with the reason written beside it and the counts unchanged.** | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:45-45 |
| **The two re-scoped facet cases and the `RE-SCOPED for KS-R14@v1` paragraphs that state what changed.** | "test_the_seam_registry_is_exactly_the_eight_declared_subtypes"; "test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged" | mcp/tests/test_knowledge_facets.py:182-227; mcp/tests/test_knowledge_facets.py:901-945; mcp/tests/test_knowledge_facets.py:1038-1045 |
| The L37 lane registrations the fail-closed manifest requires, one per new module (both rows moved again with the KS-L2 and KS-L3 insertions: the pause suite to row 171 and the AST-only guard to row 204). | "mcp/tests/test_pause_stop_only_end_to_end.py"; "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:244-244; mcp/tests/test-evidence-lanes.toml:202-240; mcp/tests/test-evidence-lanes.toml:207-207; mcp/tests/test-evidence-lanes.toml:246-248; mcp/tests/test-evidence-lanes.toml:265-272 |
| The L37 lane registrations the fail-closed manifest requires, one per new module (the pause suite's row at `:162` is unaffected by the later insertions; the AST-only guard's row moved `:193` → `:194` → `:195`). | "mcp/tests/test_pause_stop_only_end_to_end.py"; "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:202-240; mcp/tests/test-evidence-lanes.toml:238-248; mcp/tests/test-evidence-lanes.toml:244-244; mcp/tests/test-evidence-lanes.toml:207-207; mcp/tests/test-evidence-lanes.toml:246-248; mcp/tests/test-evidence-lanes.toml:265-272 |
| The L27 pane-authority proof, its fixture import from the sibling sweeper suite, and the lane registration the fail-closed manifest requires. | `PaneDiagnosticAuthorityTests` ; `_PANE_AUTHORITY_FIELDS` ; `_pane_authority_offenders` | mcp/tests/test_terminal_liveness_pane_authority.py:233-240; mcp/tests/test_terminal_liveness_pane_authority.py:243-598; mcp/tests/test_terminal_liveness_pane_authority.py:56-69 |
| **260913-LCA-L8:** the nine exact-consumer rows `mcp/tests/test_terminal_blocker_reasons.py` adds to the evidence registry under the `synthetic-test-evidence-candidate` contract. | "id = \"synthetic-test-evidence-candidate\"" | mcp/tests/evidence-lifecycle.toml:20-20; mcp/tests/evidence-lifecycle.toml:304-304; mcp/tests/evidence-lifecycle.toml:379-379; mcp/tests/evidence-lifecycle.toml:423-423; mcp/tests/evidence-lifecycle.toml:553-553; mcp/tests/evidence-lifecycle.toml:592-592; mcp/tests/evidence-lifecycle.toml:631-631; mcp/tests/evidence-lifecycle.toml:943-943; mcp/tests/evidence-lifecycle.toml:1000-1000; mcp/tests/evidence-lifecycle.toml:1026-1026 |
| **260913-LCA-L8:** the declaration that gives the new module ownership of the ambient-role runner for targeted selection — the `REPOSITORY_TEST_INPUT_CONSUMERS` entry for that runner, which is the list the claim is about. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:159-159 |
|  The governed-artifact registration and exact two-consumer list this leaf added. | "contract:common-base-merge-cases" | mcp/tests/evidence-lifecycle.toml:1273-1273  |
| The read fixture and its registered contract. | `build_read_scope_fixture`; `knowledge-read-scope-cases` | mcp/tests/read_scope_test_support.py:266-284; mcp/tests/evidence-lifecycle.toml:1203-1207; mcp/tests/evidence-lifecycle.toml:1227-1247; mcp/tests/evidence-lifecycle.toml:1267-1267 |
| The two integration-lane rows the read's boundary and path modules occupy. | "mcp/tests/test_knowledge_read_boundaries.py"; "mcp/tests/test_knowledge_read_paths.py" | mcp/tests/test-evidence-lanes.toml:169-169; mcp/tests/test-evidence-lanes.toml:171-171; mcp/tests/test-evidence-lanes.toml:164-168; mcp/tests/test-evidence-lanes.toml:173-175; mcp/tests/test-evidence-lanes.toml:188-197 |
| **The fixture and the governed contract it is registered under.** | `build_diff_fixture`; `knowledge-diff-cases` | mcp/tests/diff_scope_test_support.py:189-233; mcp/tests/evidence-lifecycle.toml:1198-1202; mcp/tests/evidence-lifecycle.toml:1262-1262 |
| **The two lane rows this leaf registered.** | "mcp/tests/test_knowledge_diff_scope.py"; "mcp/tests/test_knowledge_diff_boundaries.py" | mcp/tests/test-evidence-lanes.toml:170-170; mcp/tests/test-evidence-lanes.toml:81-167; mcp/tests/test-evidence-lanes.toml:172-174; mcp/tests/test-evidence-lanes.toml:189-196 |
| **The diff-comparison contract whose consumer list gained the run module (the consumer row is the third entry of that block).** | "contract:knowledge-diff-cases" | mcp/tests/evidence-lifecycle.toml:1382-1382 |
| **The read-scope contract whose consumer list gained the run module (the consumer row is the third entry of that block).** | "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1402-1402 |
| **The binding suite's generation-5 append, its identity-column scan and the two `CHECK` constraints read as text.** | "test_generation_5_appends_to_generation_4_without_touching_its_twenty_one_tables"; "test_the_binding_table_has_no_content_address_digest_or_fingerprint_column"; "test_the_locator_check_names_exactly_the_shipped_source_locator_union" | mcp/tests/test_knowledge_citation_bindings.py:118-160; mcp/tests/test_knowledge_citation_bindings.py:142-160; mcp/tests/test_knowledge_citation_bindings.py:161-177 |
|**The shipped-literal identity asserted per shared fact, and the same claim asserted in the reverse direction so the shipped vocabulary cannot acquire a citation member.**|`test_every_shared_fact_reports_the_identical_shipped_literal` ; `test_the_binding_vocabulary_extends_the_shipped_one_only_in_one_direction`| mcp/tests/test_knowledge_citation_bindings.py:201-236 |
|**The bound closure refusing with the bound reached and no items and no counts, and the result that states no semantic completeness.**|`test_a_bound_closure_refuses_with_selection_incomplete_and_the_bound_reached` ; `test_the_closure_states_no_semantic_completeness_and_reports_its_declared_coverage`| mcp/tests/test_knowledge_citation_bindings.py:433-522 |
| **The boundary suite's fallback catcher, the rewritten-document case, and the store's own unique-key refusal.** | "test_an_owner_revision_the_object_store_cannot_obtain_is_reported_as_unavailable"; "test_a_rewritten_document_leaves_the_binding_stale_and_never_re_bound"; "test_two_bindings_claiming_one_key_in_one_owner_revision_are_refused_by_the_store" | mcp/tests/test_knowledge_citation_boundaries.py:377-423; mcp/tests/test_knowledge_citation_boundaries.py:275-333; mcp/tests/test_knowledge_citation_boundaries.py:540-572; mcp/tests/test_knowledge_citation_boundaries.py:346-353; mcp/tests/test_knowledge_citation_boundaries.py:241-248; mcp/tests/test_knowledge_citation_boundaries.py:509-516 |
| **The retention cases measuring both directions of the read-back, and the destination proven outside the enclosure and the archive by construction.** | "test_a_published_artifact_reads_back_with_its_published_digest"; "test_a_missing_durable_destination_reads_back_as_a_blocked_state"; "test_the_destination_is_outside_the_enclosure_and_the_archive_by_construction" | mcp/tests/test_knowledge_citation_boundaries.py:650-665; mcp/tests/test_knowledge_citation_boundaries.py:687-707; mcp/tests/test_knowledge_citation_boundaries.py:667-685; mcp/tests/test_knowledge_citation_boundaries.py:628-635 |
| **The unit lane row this leaf inserted into the alphabetical knowledge run.** | "mcp/tests/test_knowledge_citation_bindings.py" | mcp/tests/test-evidence-lanes.toml:84-84 |
| **The integration lane row this leaf opened, and the governed contract whose consumer list gained the boundary module.** | "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1310-1310; mcp/tests/evidence-lifecycle.toml:1395-1402 |
| **The consumer rows the two modules added, the deliberately re-pinned catalog digest whose counts are unchanged, and the provenance paragraph that states the consumer-only change.** | `LIFECYCLE_CATALOG_SHA256` ; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:46-46 ; mcp/tests/test_dependency_ownership_ast_helpers.py:45-45 |
| **The second registry the two modules' path literals registered in: the ambient role runner's declared test-input consumers.** | `REPOSITORY_TEST_INPUT_CONSUMERS` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:56-617 |
| **The seam-registry case re-scoped a second time so the union names this leaf's own group constant rather than being trimmed back, and the generation case re-scoped to the structural sequence.** | "test_the_seam_registry_is_exactly_the_eight_declared_subtypes"; "test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged" | mcp/tests/test_knowledge_facets.py:183-246; mcp/tests/test_knowledge_facets.py:911-960; mcp/tests/test_knowledge_facets.py:1038-1045 |

## Update History
- 2026-09-15T13:15+02:00 — 260831-LOCR-L10 curator: recorded the route's new state-signal crash/restart recovery executor (`test_state_signal_restart_recovery.py`, unit-regression row `:101`) — a route-table row plus a section carrying the durable order it forces, the seven cases, the non-vacuity witness, and the review verdict's coverage limit that the fence's reachable route is the boundary drain rather than the generic finder. Route purpose, lane membership accounting and every other module's coverage claim are unchanged by this leaf.
- 2026-09-15T06:48:46+02:00 — Preserved the following dated pre-takeover review notes from the parent working tree. They describe that earlier candidate; current behavior is documented above. Exact original files and patches are retained in the master cutover report.

- 2026-09-15T06:37:50+02:00 — LCA L9 terminal-cache retirement and abandon-preview correction: refreshed this route with the shared cache-removal owner and its regression coverage.


- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Rewrote current test-route expectations for cache independence and preserved old scenario histories as historical; removed stale assertion citations. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

- 2026-09-15T00:00+02:00 — Preserved the following dated pre-takeover review notes from the parent working tree. They describe that earlier candidate; current behavior is documented above. Exact original files and patches are retained in the master cutover report.

- 2026-09-15T00:00+02:00 — LCA L9 terminal-cache retirement and abandon-preview correction: refreshed this route with the shared cache-removal owner and its regression coverage.


- 2026-09-14T23:55+02:00 — 260913-LCA completed-master review follow-up (same uncommitted change set,
  `ar/260913_ledger-commit-attribution`, base `bb65a207`): the route's L3 section, the
  ledger-attribution coverage row, the memory-backfill coverage row and four reference rows were
  corrected for the review's second pair of defects. The backfill's ref move now travels as one
  `update-ref --stdin` stream of one instruction per line plus exactly one terminating newline
  (`_update_ref_stream`), because a blank line is an EMPTY COMMAND to git and aborted the whole
  transaction for any run that declared two or more branches; `test_two_declared_branches_move_together_in_one_transaction`
  drives two real branches through the public apply route and is recorded in the L3 section and the
  module's reference row. The projection now asks the code half of a row's truth of the source's own
  rows at the boundary where the code repository is in hand, excluding with `code-commit-missing` and
  reporting through `sourceExcludedRows`/`sourceExcludedReasons`, while `LedgerWorld.code_repository`
  widened to optional so a world naming none keeps its rows; the two new `test_memory_ledger.py` cases
  are recorded in this route's `test_memory_ledger.py` paragraph, its coverage row and a new reference
  row. The section's opening now states that two external reviews found four defects, all fixed, and
  keeps the statement that the tool has not been applied to any real repository. Every anchor into the
  two shifted modules and the two shifted test modules was re-derived against the working source:
  `MemoryBackfillApplyTests` 399-629 → 399-676, `MemoryBackfillCliTests` 754-902 → 801-949,
  `is_empty` unchanged, `carry_ledger_cells` 927-972 → 940-985, `read_ledger_source` 302-350 →
  315-363, `test_a_source_row_the_source_cannot_carry_is_reported_not_kept` 495-522 → 496-523,
  `test_a_partially_trailered_source_still_reads_its_pre_rule_rows` 525-552 → 601-628,
  `_AttributedWorld` 345-401 → 346-402, and the ten L2 ledger-attribution ranges 404-431 → 405-432,
  434-453 → 435-454, 456-485 → 457-486, 597-603 → 673-679, 606-622 → 682-698, 625-648 → 701-724,
  651-663 → 727-739, 666-695 → 742-771, 698-733 → 774-809 and 736-766 → 812-842. Verification
  metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the test-inventory
  changes are the frozen ones. Re-read the overview and re-checked its cited ranges: they hold, and
  the new shared-support module is registered in the catalog it names. No wording changed.
  Verification metadata remains closeout-owned.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): `mcp/tests` carries local
  unstaged changes not represented in HEAD. Re-read the card against the frozen on-disk source and
  re-checked its claims and cited ranges: nothing this card asserts is falsified by the change, so
  no wording changed. Verification metadata remains closeout-owned; no verification stamp advanced.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 5
  claim(s) whose anchor no longer sat in its cited range and normalised 12 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). 3 claim(s) were declined as ambiguous or not the subject
  and were left for a reading curator. No claim wording changed; every rewritten range was read back
  at its current position. Verification metadata remains closeout-owned.

- 2026-09-14T18:20+02:00 — 260913-LCA-L3 follow-up (same uncommitted change set on
  `ar/260913-lca-l3-ar`, base `7317108b`): an external review found two defects in the backfill and
  both are fixed, so this route's L3 section, its retained-route row and its reference rows were
  corrected. The section now records that the rule is a maximum matching plus a fill (the fill is
  load-bearing because a matching is symmetric and the format is not), that a conflict resolves on the
  table's recorded order and is proved by swapping two rows, that the skip vocabulary is five literals
  split into holes and declines with `lost_claims` naming each loser and its winner, that a plan which
  lost a mapping is neither empty nor digest-equal to one that did not, and that the acceptance proof
  is now trailer-only — it reads the rewritten tip through `_ABSENT_LEDGER`, whereas the earlier proof
  read the table the migration carries forward and, because `read_ledger_source` unions table rows into
  trailer rows, proved the table had survived rather than the trailers, which is how 60 omissions
  passed a green suite. Added the fifth class: `MemoryBackfillCliTests` drives the real registered
  command path against a branch-name tip and a second apply, because the reviewed second defect — a
  rescue set built from a name and read back as a hash, plus the rescue guard running before the
  empty-plan check — was invisible from every kernel-level case. The route row and the three reference
  rows were rewritten to the current case names and ranges (the L3 module grew 543 → 906 lines and the
  kernel module 686 → 1024), and the section now states plainly that the fixed tool has not been
  applied to any real repository: its evidence is fixtures plus a read-only plan measurement, and the
  rewrite is deferred to this master's integration into IAS. Verification metadata remains
  closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 route impact (curator, uncommitted change set on
  `ar/260913-lca-l3-ar`, base `7317108b`): registered the leaf's new `test_memory_backfill.py` in the
  retained route table and added the route section for it (unit-regression lane at
  `mcp/tests/test-evidence-lanes.toml:69`, and no `evidence-lifecycle.toml` consumer row because its
  only imports are the production modules under test plus stdlib). Records the migration's contract
  as this route's evidence — the one-trailer rule and its reported skips, the closed four-literal skip
  vocabulary, the total old→new identity map, the byte-faithful replay, the second-run no-op, and the
  rescue-ref and digest refusals — and states the reversal plainly: the apply was verified and then
  reverted by developer ruling because rewriting the shared ancestors removed the master's common
  ancestor with its super, so the shared line still carries 0 trailers and the backfill is an explicit
  step at this master's integration into IAS. Records the worker's re-measurement replacing the leaf
  document's census (474 rows / 419 distinct code commits exact; 55 duplicate rows, not 104; 419 at
  the shared line and 428 at the tip, not 513; 67 and 44 skips, not 10) and notes that
  `test_git_command.py`'s two migrated call sites now build `GitRunnerOptions`. Two anchors in the
  L11 reference row were repointed to their current ranges: `read_ledger_source`
  `ledger_projection.py:299-349` → `:302-350`, which this change set moved by adding three lines
  above it, and — inside the same row — the two `test_memory_ledger.py` ranges that already fell short
  of the test functions they name (`:473-502` → `:495-522`, `:503-532` → `:525-552`). Verification metadata
  remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-14T15:05+02:00 — 260913-LCA-L8 curator (uncommitted change set on `ar/260913-lca-l8-ar`):
  registered the leaf's new `test_terminal_blocker_reasons.py` in the retained route table
  (integration lane, entry row 177) — a cleanup or finalize blockage always names its component and a
  non-empty reason, the L6 shape finalizes on the first call, a real permission failure blocks with
  its own reason and refuses identically on retry, and both invariant owners are driven directly —
  added the route section recording the measured defect and its source diagnosis, and reconciled the
  population to the current manifest, measured rather than carried: 206 modules on disk and 206
  entries, 115 unit-regression (5-120), 2 public-contract (122-124), 60 integration (126-186), 16
  architecture-fitness (188-204), 13 provider-conformance (206-219), with stress-durability and
  migration empty. Superseded the L7 paragraph by adding the current counts beside it; the
  `test-evidence-lanes.toml` card remains the owner of record for lane membership. Re-derived every
  manifest anchor in the reference table (the L36 row `:144` → `:145`, the L37 rows `:161`/`:193` →
  `:162`/`:195`, the playthrough `:155` → `:156`, the L5 row `:152` → `:153`) and, while re-deriving,
  corrected three rows whose cited ranges no longer hold their anchors at all: the L34 flake note
  (`1181-1192`), the L2 ledger cases in `test_memory_ledger.py` (all eleven ranges, moved by later
  insertions in that file) and `attributed_commits` in `kernel/memory_attribution.py` (`148-179`).
  Those three are pre-existing drift from other leaves, not consequences of this change. Membership
  is selection and cost classification only; no execution or acceptance claim, and the verification
  stamps remain closeout-owned.

- 2026-09-14T14:20+02:00 — 260913-LCA-L7 curator (uncommitted change set on `ar/260913-lca-l7`):
  registered the leaf's new `test_closeout_projection_source_classification.py` in the retained route
  table (integration lane, entry row 137) — it refuses a sprint whose authored graph is one node past
  the master bound with the raiser's own declared code, proves that code classifies `invalid` rather
  than `unreadable`, keeps the genuinely unreadable codes reporting `unreadable`, and leaves the
  ordinary source readable with no problems — and reconciled the population to the current manifest,
  measured rather than carried: 205 modules on disk and 205 entries, 115 unit-regression (5-120), 2
  public-contract (122-124), 59 integration (126-185), 16 architecture-fitness (187-203), 13
  provider-conformance (205-218), with stress-durability and migration empty. Superseded the L5
  paragraph by adding the current counts beside it; the `test-evidence-lanes.toml` card remains the
  owner of record for lane membership. Membership is selection and cost classification only; no
  execution or acceptance claim, and the verification stamps remain closeout-owned.

- 2026-09-14T13:20+02:00 — The sync half of the ledger ruling and the mid-flight result (curator on the
  landed `ab47182` change set of the 260913 ledger line): **no module was added or deleted and no lane
  row moved.** Added the route section recording two additions — `test_worktree_sync.py`'s
  `test_a_descendant_memory_ledger_that_dropped_a_source_row_is_current`, which proves the transaction
  reports a row its source cannot carry as `already-current` rather than refusing it, and
  `test_atomic_series_activation.py`'s `ReconcilingResultTests`, which pins a completed pass beside a
  mid-flight selection as `atomic-series-reconciling` with the stuck contract, its publication time,
  its revision and both exits named, and a refusal beside one as leading with that state. Added three
  reference rows, corrected the activation suite's stale fixture/case anchors, and noted the sync case
  in the ledger-row of the routing table. Verification metadata remains closeout-owned; no execution
  or acceptance claim and no verification stamp advanced.

- 2026-09-14T11:58+02:00 — 260913-LCA-L11 route impact (curator, uncommitted change set on
  `ar/260913-lca-l11-ar`, base `4214d7a1`): three test modules gained cases and **no module was added
  or deleted**, so the route population and lane membership are unchanged. Added the route section
  recording where the coverage went: three `test_checkpoint_landing_end_to_end.py` cases changed
  **direction** and now assert a landing (a reordered source region, a reversed superseding pair, the
  interleaved projection on the leaf route), with the reversal's hazard carried in the case and
  recorded as a gap pending a decision; `test_integration_branch_authority.py` gained the landing's
  full clause inventory, including the dropped and duplicated source rows now asserted as **accepted**
  and two module-level `_require_true_rows` cases; and `test_memory_ledger.py` gained the excluded-row
  case and the partially-trailered-source case. Corrected the two retained-route rows that described
  the ledger reader's old fallback framing and the checkpoint module's refusal list, and repointed the
  L34 reference row's class extent (`412-1190` → `412-1211`) and its `_closeout_preview` /
  hand-edited-ledger case ranges. Added three reference rows for the new cases. Verification metadata
  remains closeout-owned; no execution, acceptance or certification claim and no verification stamp
  advanced.

- 2026-09-14T10:16+02:00 — 260913-LCA-L10 route impact (curator, uncommitted change set on
  `ar/260913-lca-l10-ar`, base `4214d7a1`): added a route section and a `Retained Behavioral Routes` row
  for the reachability case this change set adds to the existing
  `test_task_documents_graph_projection.py` — `SubTaskIndexReachabilityTests` with its `_index_doc` helper,
  proving through `read_task_documents` that a completed leaf written by a newer build stays reachable
  from the master's sub-task index, that an unstarted row keeps resolving, and that a document with a
  required field deleted is still withheld. Recorded the two mechanics that must not be "fixed" later (the
  direct `Path.write_text` because `write_task_doc` must refuse the skewed document, and the `checkpoint`
  field on a step mirroring where the live skew landed), and recorded for the route that the pre-change
  parse sites **deleted the whole document** rather than skipping it — which is what produced the
  dead-text sub-task rows — while the authoring plane was never loosened. The module
  gained one case and one helper, its lane row (`mcp/tests/test-evidence-lanes.toml:108`) and both case
  budgets are unchanged, and no new module was added. Verification metadata remains closeout-owned; no
  verification stamp advanced and no execution or acceptance claim is made here.

- 2026-09-14T07:05+02:00 — 260913-LCA-L5 route impact (curator, uncommitted change set on
  `ar/260913-lca-l5-ar`, base `52875e7a`): added a route section and a `Retained Behavioral Routes` row
  for the change set's new `test_leaf_doc_master_link_binding.py` (integration lane, row 152) — the
  derived master link end to end, plus the fail-closed half. Recorded that
  `test_task_document_application_1.py`'s `test_create_writes_both_files` was **removed** because its
  scenario is now refused by design, and that four existing modules gained a prerequisite the refusal
  forced (`test_task_document.py._ensure_parent_master`, `test_task_doc_review_public.py._create`'s master
  write, and the `seriesContractPath` binding in `test_closeout_queue._leaf` and
  `test_transaction_only_worktree_delivery._bind_task_without_review`), with the reason the last two are
  load-bearing rather than cosmetic. **Corrected the L4 open item rather than carrying it**: the producer
  census module's `unit-regression` lane row now exists at `mcp/tests/test-evidence-lanes.toml:68`, so the
  fail-closed load failure the L4 row and history entry predicted does not hold. Reconciled the population
  to the measured current manifest (204 modules, 204 entries: 115 unit-regression, 2 public-contract, 58
  integration, 16 architecture-fitness, 13 provider-conformance) in a superseding clause under the stale
  paragraph, and re-derived three shifted lane rows (cross-master concurrency 143 → 144, the pause suite
  159 → 161, the pause architecture guard 191 → 193, the playthrough 153 → 155). Verification metadata
  remains closeout-owned; no execution or acceptance claim and no verification stamp advanced.

- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`, base
  `5bb124d4`): route refresh. Registered the leaf's new module
  `test_memory_attribution_producers.py` (the producer census: one-definition guard, five producers each
  reaching the shared renderer, the append-as-final-block dialect, and the two public-tool end-to-end
  cases) and the recovery case the leaf added to `test_transaction_only_worktree_delivery.py` in a new
  route section and two `Retained Behavioral Routes` rows, recorded the corrected census (5 producers and
  0 untrailered, correcting the master's 2026-09-13T22:05 decision in two places), the trailerless-by-rule
  sites with their reasons, and the two durable rules the census enforces. Also recorded the
  `test_memory_ledger.py` import move (no case or assertion changed) and the new module's registration as
  a consumer in `mcp/tests/evidence-lifecycle.toml`. **Open item recorded, not repaired:** the new module
  still has no lane row, so `load_lane_manifest` fails closed — the measurement and the consequence are in
  the new section above and on the `test-evidence-lanes.toml` card; the repair is code work, not memory
  work. Added a new file card for the new module. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.

- 2026-09-13T23:25+02:00 — 260913-LCA-L2 follow-up (same uncommitted change set): the ledger
  attribution group gained a tenth case, `test_the_rendered_trailer_is_the_one_the_reader_parses`,
  after the writer and the reader were found to hold two separate `Code-Commit` literals (found by
  the L2 curator's first pass and reported to the owner, who fixed the code in the same change set).
  It renders
  through the real writer, commits the message and reads the code commit back out through the real
  reader, so a writer-side key change loses the row and fails that case instead of passing silently.
  Registered it in the route paragraph and the reference row, and recorded the rule a future curator
  needs: the literal `Code-Commit` text in these test modules is a deliberate independent oracle and
  must not be "corrected" to read the constant. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.

- 2026-09-13T23:12+02:00 — 260913-LCA-L2 (uncommitted change set on `ar/260913-lca-l2-ar`):
  registered the nine new `test_memory_ledger.py` cases that prove the ledger's source is the memory
  commits' own `Code-Commit:` attribution — the every-checkpoint closed loop against the tracked
  table, the hand edit that cannot move the projection, the pre-trailer blob fallback, the bootstrap
  source that contributes no rows, `exclude`, the last-block-wins parse, the unknown-code-commit
  drop, the by-key multi-trailer read, and the merged-in mapping — plus the `test_worktree_sync.py`
  case that is the suite's first coverage of the `official line is mid-cycle` refusal, which comes
  from the named-ref ledger read rather than the projected source. Added the route paragraph, the
  retained-route row and the reference rows; recorded that the six pre-existing projection cases in
  the same file still pass only because of the per-commit blob fallback. Verification metadata
  remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): the
  CCR-R12@v5 transaction-only route now also proves the memory attribution — the new
  `_assert_memory_attribution` reader checks the memory-content commit's `%B`, the exactly-one
  `Code-Commit:` count, `git interpret-trailers --parse`, and
  `git log --format=%(trailers:key=Code-Commit)` against the real shas public closeout returned, and
  asserts the `memory.md`-only ledger commit returns `""`; `test_direct_landing.py` carries the same
  checks for the branch-addressed route. Assertions only: no new test module, test function, or
  parametrized case, so the retained population and both case budgets are unchanged. Verification
  metadata remains closeout-owned; no execution, acceptance, or certification claim.

- 2026-09-13T20:42+02:00 — Child-admission seal removal and the already-vacant stop (uncommitted
  260831-LOCR change set on `ar/260831_lifecycle-owned-completion-relay`): registered the new
  `test_lifecycle_playthrough_end_to_end.py` (integration) in the retained route table and the
  reference table, corrected the pause route-table row so it no longer says the stop refuses a
  never-selected master (it now reports `atomic-series-already-vacant`), re-derived the population to
  202 modules with 57 integration members, and shifted the two L37 lane-registration rows
  (`test-evidence-lanes.toml:158` → `:159`, `:190` → `:191`). Verification metadata remains
  closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 curator: registered the leaf's two new modules in the
  retained route table — `test_pause_stop_only_end_to_end.py` (integration; the public stop measured
  against refs, object databases, coordination tree, worktrees, enclosure and every task document, with
  the proposal-free hand-back and every refusal) and `test_pause_is_not_publication.py`
  (architecture-fitness; the import-closure guard that keeps the stop from becoming the checkpoint
  publication) — and re-derived the population and budgets from the manifest: 201 modules, 56
  integration, 16 architecture-fitness, budgets 1000 unit / 250 integration. Corrected the cross-master
  row, which called a pause "an ordinary stop that is no tool call" — the leaf makes the pause a real
  public operation, so that parenthetical is now false and has been replaced. Added three reference
  rows. Membership is selection and cost classification only; no execution or acceptance claim, and the
  verification stamps remain closeout-owned.

- 2026-09-13T15:00:56+02:00 — 260831-LOCR-L36 curator (round 2): registered the new ninth cross-master case `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters` in the `Retained Behavioral Routes` row and in the L36 reference row, and corrected that row's wording — a graph-less sprint serializes nothing, `atomic-sequential` is the sprint shape, and only a real sprint-graph wave edge still gates. Rebound that reference row's four stale cross-master ranges (131-162, 286-321, 338-372, 451-479) and added the graph-less range 483-551. Targeted edits only; unrelated sections are byte-identical. Source-route documentation only: no execution, acceptance or certification claim.

- 2026-09-13T14:46+02:00 — Curator citation repoint: two inline `cit:(...)` references in the public-surface inventory still cited `models/worktree.py:334-340` / `367-376` for the next-move triple and `_require_registered_public_next_tool`; both now resolve at `322-322` and `355-364` after `models/worktree.py` shrank. Claim wording unchanged.

- 2026-09-13T14:20:09+02:00 — 260831-LOCR-L36 curator: added a `Retained Behavioral Routes` row for the contract-scoped cross-master concurrency work (`test_cross_master_concurrency.py` with the rewritten `test_atomic_series_activation.py`) — one protected source pair shared by two sprint-commanded atomic masters, each keeping its own record, with a conflicting or stale publication refused at the pair and only the sprint graph's wave edge still gating — and refreshed the L38 admission row to say the admission is contract-scoped (no `classification`/`blocking`/`sourcePair*`, never a foreign master as blocker). Reconciled the route population to the current manifest (199 modules: 114 unit-regression, 2 public-contract, 55 integration, 15 architecture-fitness, 13 provider-conformance; budgets 1000 unit / 200 integration), added four reference rows, and rebound the seven stale ranges this table carried into `models/worktree.py` and `test_checkpoint_landing_end_to_end.py`. Source-route documentation only: no execution, acceptance or certification claim, and lane membership stays owned by the `test-evidence-lanes.toml` card.

- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.

- 2026-09-13T09:12+00:00 — 260831-LOCR-L34 curator: added a `Retained Behavioral Routes` row and a
  Checkpoint Landing Plan/Apply Parity section for the new integration module
  `test_checkpoint_landing_end_to_end.py`, which drives the public checkpoint and closeout operations
  over real temporary Git repositories and asserts that each divergence refuses at **both** the
  preview and the apply — the boundary executor for the preview/apply parity invariant, whose full
  inventory lives on the `worktrees/overview.md` route. Reconciled the route population to the current
  manifest (198 modules: 114 unit-regression, 2 public-contract, 54 integration, 15
  architecture-fitness, 13 provider-conformance; budgets 1000 unit / 200 integration) and corrected the
  last stale "150-collected-case cap" bound in the same paragraph. Added three reference rows.
  Source-route documentation only: no execution, acceptance or certification claim, and lane
  membership stays owned by the `test-evidence-lanes.toml` card.

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded in the route body that the citation
  fixtures now build real Git provenance (`Tree.history`/`stamp`/`remove_source`, the `stamp`
  metadata row written inside the metadata table, and the header-anchored `Tree.row` locator;
  `Scenario` stamping its verified tree before deleting both cited files), so the previously pinned
  relocation tests still exercise the legitimate kind-preserving move rather than relaxed
  expectations, and recorded the new `MechanicallyProjectedRangeTests`. Content change in the
  Fixture Roles And Claims body, not a range repoint.

- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: added a `Retained Behavioral Routes` row and a
  Public-Surface Inventory Contract paragraph for the new integration module
  `test_worktree_status_terminal_next_tool.py`, which is the first coverage of the
  `terminal-archive-ready` branch and the executor for the worktree surface's advertised next move.
  Reconciled the route population to the current manifest (197 modules: 114 unit-regression, 2
  public-contract, 53 integration, 15 architecture-fitness, 13 provider-conformance; budgets 1000
  unit / 200 integration) and added three reference rows. Source-route documentation only: no
  execution, acceptance or certification claim, and lane membership stays owned by the
  `test-evidence-lanes.toml` card.

- 2026-09-12T04:10+02:00 — 260831-LOCR-L30 follow-up: recorded the three new forcing cases (guidance
  checkpoint projection, the pull-request `already-recorded` guard, the checkpoint landed source
  head) and that two of those modules — `test_post_integration_cleanup_guidance.py` and
  `test_closeout_kept_rules_pins.py` — gained file cards, so this route's covered set grew by two.
  Lane membership is unchanged. Source-route documentation only: no execution, acceptance or
  certification claim.

- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: reconciled the retained population to the current
  manifest (196 modules: 114 unit-regression, 2 public-contract, 52 integration, 15
  architecture-fitness, 13 provider-conformance) and recorded the fail-closed repair that made the
  manifest loadable — seven tracked modules had declared no lane, seven plus this leaf's own new
  module were registered. Source-route documentation only: no execution, acceptance or certification
  claim, and lane membership stays owned by the `test-evidence-lanes.toml` card.

- 2026-09-12T01:41:08+02:00 — 260831-LOCR-L29 public-surface repair: added the
  `PublicSurfaceInventoryTests` row to the retained behavioral routes and a Public-Surface Inventory
  Contract section recording why the advertised/inventoried/registered agreement needed an executor
  (the `server_info` comparison was self-referential), plus its reference row. The probe is
  hermetic; no execution or acceptance claim. No route impact on the other retained behavioral
  routes: no protected scenario changed.

- 2026-09-11T23:05:00+00:00: Recorded the route-wide cause of this route's shrunken inventory as durable negative knowledge. `git log -S` proves the removals: `d3610903` reduced test/support code by 79% (235,366 deletions) and replaced coverage floors with case budgets, `173bb01e` deleted the detached lifecycle worker, `b06b3a27` removed the master route-review gate, `6982c6a7` cut the door-operation-journal plane, and `2ec5d244` deleted the tests its remaining failures exposed as dead. Cards citing a deleted test name now have a route-level home for that fact instead of inventing per-file provenance; a shorter coverage table is deliberate removal, not loss. No route impact for the retained behavioral routes: no protected scenario changed.

- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: four test modules were deleted by the cut and their references removed here — `test_integration_ref_transaction.py` (`173bb01e`, removed with the mid-crash ref-recovery capability), `test_worktree_integrate_quality_gate.py` (`9e1743c1`), and `test_closeout_memory_certification_reuse.py` / `test_prepared_publication_recovery.py` (`2ec5d244`). The candidate/protected-ref row no longer claims exact-recovery coverage it no longer has. Only the deleted-test references were reconciled; the rest of this route was not re-read in this pass, so verification metadata remains pinned. Source documentation only; no execution or acceptance claim.

- 2026-09-10T15:06+02:00 — Closeout auto-carry and parked candidate: registered `test_sync_parked_candidate.py` in the unit-regression lane, added the `CloseoutSourceLineageHealTests` boundary class to `test_source_lineage.py`, and reconciled the retained population to 183 files (99 unit, 55 integration). No case budget was raised. Source-route evidence only; no execution or acceptance claim.

- 2026-09-10T12:23+02:00 — 260831-LOCR-L20 curator post-sync refresh: reconciled this route's
  retained-population account to the post-sync manifest union — 187 files (103 unit-regression,
  2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance). The delta
  from the recorded 186 is L28's landed `test_terminal_liveness_deferred_work.py` proof, which
  registers in `unit-regression`. The two synced conflicts were resolved hunk-by-hunk with the synced
  side authoritative for ranges and structure, and both sides' genuine history entries were retained.
  Classification and preparation evidence only; no execution, Gate 5, or acceptance claim.

- 2026-09-10T11:55:00+02:00 — Post-sync union curation for 260831-LOCR-L03: kept the sibling's richer current-population paragraph and its R28/landing-debt rationale, framed the L38 candidate's own 179-file figure as historical, recorded the lane-manifest card as owner of record for lane membership, and advanced the counts to the union population (187 files: 103 unit-regression) that includes this leaf's own canonical terminal-evidence mapping row. No range was carried over from the stashed side and no history entry was dropped. This records source documentation only and makes no acceptance or certification claim.

- 2026-09-10T11:53+02:00 — 260831-LOCR-L09 curator: resolved this route's sync merge, added the state-signal boundary-delivery route (persist-before-marker, held working target, same-row delivery at the next admissible boundary across replacement/restart/failed submission), and reconciled the merged population to 187 modules (103 unit-regression) including both the LOCR-L28 deferred-terminal-work row and this leaf's boundary-delivery module. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-10T11:52:46+02:00 — 260831-LOCR-L25 curator (route impact, sync advance): resolved the merge with landed LOCR-L28 (`e26b55db`) and re-derived this route's population against the synced manifest, now 187 test-shaped modules (103 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance) because this leaf's own parked-external-await separation guard joins the landed 186. The two population paragraphs that the merge left standing are consolidated into one current account above. Supersedes the 186 / 102 figures recorded by both leaves. No execution, acceptance, or certification claim; verification metadata remains closeout-owned.

- 2026-09-10T11:25:00+02:00 — Re-read this overview's L38 population sentence against the current manifest, framed its 179-file figure as that candidate's historical count, and recorded the lane-manifest card as the owner of record for current lane membership. This records source documentation only and makes no acceptance or certification claim.

- 2026-09-10T11:24+02:00 — 260831-LOCR-L28 curator: re-derived the retained test population against the current evidence manifest after the authorized repair of three missing CCR landing-debt lane registrations (179 → 186 files: 102 unit-regression, 2 public checks, 55 integration, 14 architecture, 13 provider). This leaf's own deferred-work module also moved from integration to unit-regression for the same 150-case integration cap. Body claim only; no execution, certification or acceptance claim is made.

- 2026-09-10T11:22:48+02:00 — 260831-LOCR-L25 curator (route impact, correction): corrected the restored-row classification after the integration lane's 150-case cap rejected the first split. All three CCR landing-debt rows `8885939e` omitted (`test_review_state.py`, `test_task_doc_review_public.py`, `test_transaction_only_worktree_delivery.py`) register as `unit-regression`, so the route now records 186 retained test-shaped modules as 102 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness and 13 provider-conformance, superseding the 100/57 split recorded at 11:04 on the same tree. Source documentation only: no execution, acceptance, or certification claim, and verification metadata remains closeout-owned.

- 2026-09-10T11:04:12+02:00 — 260831-LOCR-L25 curator (route impact, manifest repair): re-derived the manifest population after the developer-authorized repair of the three CCR landing-debt rows that `8885939e` omitted (`test_review_state.py` unit-regression; `test_task_doc_review_public.py` and `test_transaction_only_worktree_delivery.py` integration). The route records 186 retained test-shaped modules in place of the previous 183, and notes that all three restored modules already had file cards. **The integration split in this entry was superseded by the 11:22 correction above.** Source documentation only: no execution, acceptance, or certification claim, and verification metadata remains closeout-owned.

- 2026-09-10T10:55+02:00 — 260831-LOCR-L20 curator manifest refresh: reconciled this route's
  retained-population account to the repaired closed manifest — 186 files (102 unit-regression,
  2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance). The delta
  from the previously recorded 179 is the three CCR transaction-only closeout modules restored by the
  authorized manifest repair plus the focused terminal-evidence cursor module; the restored modules
  are `unit-regression` because they had been running unmarked and the integration lane is at its
  hard cap of 150 collected cases. Classification and preparation evidence only; no execution,
  Gate 5, or acceptance claim.

- 2026-09-10T10:32:23+02:00 — LOCR-R21 curator reconciliation against the synced base (code `6096941f`, memory `71d7f73a`): resolved the re-applied WIP conflict by retaining both landed LOCR-L08 entries and this leaf's own terminal-liveness route entry, and recorded the module's composition boundary. This route records the LOCR-R21 hysteresis proof only; sibling cadence (`R12`) and sweep non-overlap (`R22`) cases are still in their own unlanded worktrees and compose into the same module later. Verification metadata remains closeout-owned.

- 2026-09-10T10:06:31+02:00 — 260831-LOCR-L25 curator (route impact): added the parked-external-await separation guard to the retained behavioral route table, extended the state-signal routing boundary with the open-turn non-wake case, and re-derived the current manifest population (183 files: 99 unit-regression, 2 public-contract, 55 integration, 14 architecture-fitness, 13 provider-conformance) past the frozen L38 snapshot. File-level detail lives in the two changed and one new test cards. This records source documentation only; it makes no execution, acceptance, or certification claim, and verification metadata remains closeout-owned.

- 2026-09-10T09:30+02:00 — 260831-LOCR-L22 curator: added the retained terminal-catalog batch and sweeper non-overlap proof surface to the route map — counted atomic replacements (zero clean, one dirty, one dirty-partial) and real-thread contention returning the committed snapshot without a second probe. Cadence, hysteresis, and cross-store post-commit ownership remain with their leaves; this records source documentation only and claims no execution, acceptance, or certification.

- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ02 preparation recorded the current shared-support consumer declarations and registry/validator identity as non-certifying source evidence; no acceptance claim is made.

- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.

- 2026-09-08T16:17:10+02:00 — CCR-L38 source-grounded preparation: recorded the two frozen registered admission/route-review checks and reconciled the retained test-lane counts from 177 to 179 files. This records candidate behavior and preparation evidence only; formal review and acceptance remain with closeout/aggregation owners.

- 2026-09-08T14:39+02:00 — 260831-LOCR-L20 curator reconciliation: added the focused
  terminal-evidence cursor route and its unit-regression boundary to the current test inventory.
  The module's host result remains development evidence; master review and certification retain
  their existing owners.

- 2026-09-08T14:38:13+02:00 — 260831-LOCR-L08 curator: independently re-read the existing final-catalog and prepared-memory adapter references against current source; retained both claims and corrected their source ranges.

- 2026-09-08T14:35+02:00 — 260831-LOCR-L28 curator: added the deferred-terminal-work route to the retained behavioral map and fixture claims. The new hermetic proof covers sweeper-side commit/release/drain ordering, aborted-pass suppression, row-local quarantine continuation, and unguarded post-commit escape without rollback; caller no-lock ownership and final acceptance remain explicitly outside this route update.

- 2026-09-08T14:30:38+02:00 — Added the L03 canonical terminal-evidence mapping route and its explicit unit-regression inventory entry. The route records diagnostic protection only; execution, lifecycle ownership, certification and acceptance remain with their existing owners.

- 2026-09-08T14:25+02:00 — LOCR-R21 curator: added the current terminal-liveness proof route to the retained behavior map, corrected the two reopened internal source ranges, and preserved the route's development-versus-certification boundary. This leaf changes test proof only; verification metadata remains closeout-owned.

- 2026-09-08T14:23:36+02:00 — 260831-LOCR-L12 curator: recorded the retained terminal-liveness
  cadence/readiness route and its sweeper-local boundary. The route remains a diagnostic test
  surface; lifecycle ownership, production wiring, and master review remain outside this leaf.
  The reviewed memory-quality source anchors were re-derived on the synced base and are recorded
  by the 260831-LOCR-L08 entry above. Verification metadata remains pinned until closeout stamps
  the leaf code commit.

- 2026-09-08T14:22:32+02:00 — 260831-LOCR-L08 curator: added the retained state-signal structural-routing test surface to the route map, covering current-manager replacement and local refusal/retry boundaries without claiming execution evidence.

- 2026-09-06T21:56+00:00 — Reconciled the governing route against IAS d3610903 and retained source/card evidence. Replaced obsolete host-test prohibitions, coverage floors and deleted-suite claims with the current preparation/development/certification boundaries. Existing history and verification pins remain preserved; this is semantic memory preparation, not acceptance.
### 2026-09-06T17:13:06+00:00 — L34 implementation memory

- 2026-09-06T15:08:14+00:00 — Added the current selected-certification/refusal source routes and their precise fixture/model boundaries; corrected stale pending-candidate wording where present. Preserved broader prior verification stamps and all earlier history.

- 2026-09-06T14:06:32+00:00 — L33 candidate route curation: Replaced the stale two-consumer claim with catalog-owned fixture consumers and routed the exact source-selection/environment and component-only closeout boundaries to their existing cards. Prior verification stamps and complete history remain unchanged.

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation: Updated the current projection/refusal expectation, routed actual transaction forcing, and added the four-case full scope regression at private C b34f4a59 without asserting live test/closeout acceptance from fixture classification.

- 2026-09-06T00:38:37+00:00 — L30 independent-review correction: refreshed the four durable-store test class ranges and five owner ranges, including thread_mutex_for in kernel/file_lock.py, against actual C 97e8ed2e1fae21756c3ad995c30613d4fbfcc503. Preserved the existing behavior account and complete prior history.

- 2026-09-06T00:21:02+00:00 — CCR L30 candidate-index recovery: added source-index/R06/R07 composition evidence and its fixture/full-acceptance boundary without changing existing producer or lock evidence.

- 2026-09-05T22:23+00:00 — L30 route-impact review against `6e4ab81f6ae52bce35003377bb3aec7877554ed7`: Routed new lock, immutable-evidence and producer/export regressions; replaced accepted producer-gap assertions while retaining fixture-versus-live and pending L32 boundaries.

- 2026-09-05T07:45+00:00 — L31 cumulative source review at ea35964985f30080488270e71ac81657ac40682b: reconciled current profile selection/refusal, assertion ownership, route counts, library/production evidence limits and exact-intent tests; restored the damaged evidence-table boundary from verified current source and retained its damaged predecessor in the curation report. Verification records source review, not execution or acceptance.

- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass (route impact): recorded the seven standalone CCR-R14 final-codex suites (five unit-regression rows 64-68, two integration rows 291-292) and their test-evidence-lanes.toml lane registrations. File-level detail lives in the new test cards. Verification stamp is the full leaf code commit `54ff803a05209e06f732f2de1f90e2a71a069e08` (tree `aff2e268968397ab8db042a782652957a3600dda`).

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass (route impact): recorded the six standalone CCR-R17 measured-replay suites (unit-regression rows 148-153) and their `test-evidence-lanes.toml` lane registrations. File-level detail lives in the six new test cards. Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass (route impact): recorded the six standalone CCR-R17 measured-replay suites (unit-regression rows 148-153) and their `test-evidence-lanes.toml` lane registrations. File-level detail lives in the six new test cards. Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec: route coverage adds three status-wait test cards (outcomes, registration, store) and refreshes dispositions/conformance/evidence-lane cards; route index regenerated.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec: route coverage adds three status-wait test cards (outcomes, registration, store) and refreshes dispositions/conformance/evidence-lane cards; route index regenerated.

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass (route impact): recorded the six standalone CCR-R13 diagnostic suites (four unit-regression, two integration) and their `test-evidence-lanes.toml` lane registrations. File-level detail lives in the new test cards. Verification stamp is the full leaf code commit `4ba18bb23ba90e201bb37341d61c0efc64161fcf` (tree `631145bf3e0d5899b1dcbccf8c0d4a8257821f0d`).

- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass (route impact): recorded the six standalone CCR-R13 diagnostic suites (four unit-regression, two integration) and their `test-evidence-lanes.toml` lane registrations. File-level detail lives in the new test cards. Verification stamp is the full leaf code commit `4ba18bb23ba90e201bb37341d61c0efc64161fcf` (tree `631145bf3e0d5899b1dcbccf8c0d4a8257821f0d`).

- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5 memory pass (route impact): added the CCR-L16
  section for the six durable gate-and-rail telemetry suites
  (`test_telemetry_models.py`, `test_telemetry_projection.py`, `test_telemetry_projection_edges.py`,
  `test_telemetry_store.py`, `test_telemetry_validation.py`, `test_telemetry_validation_edges.py`)
  registered in the `unit-regression` lane. Verification metadata stays pinned until closeout
  stamps the leaf code commit.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: recorded the new generation-coherent projection suite and the refreshed lifecycle/test suites. File-level detail in the mcp/tests sidecars.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass (route impact): added the CCR-L12 section for the host-authority suite, the five-gate/authority rework of the clean-quality group, and the Gate-5-order closeout regressions. Verification metadata stays pinned until closeout stamps the leaf code commit.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: recorded the new generation-coherent projection suite and the refreshed lifecycle/test suites. File-level detail in the mcp/tests sidecars.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass (route impact): added the CCR-L12 section for the host-authority suite, the five-gate/authority rework of the clean-quality group, and the Gate-5-order closeout regressions. Verification metadata stays pinned until closeout stamps the leaf code commit.

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 route impact: recorded the requirement-route test evidence (integration-lane registration, conformance driver cases, ledger advance, dashboard input-count oracle). File-level detail lives in the new test card and the refreshed conformance/scope cards.

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 route impact: recorded the requirement-route test evidence (integration-lane registration, conformance driver cases, ledger advance, dashboard input-count oracle). File-level detail lives in the new test card and the refreshed conformance/scope cards.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 added the three focused model, reachability, and
  registry-validation edge suites, classified all five certification suites as unit regressions,
  and extended the permanent shared-support ownership to the exact five-consumer set.
  Verification remains closeout-owned.

- 2026-09-01T08:13+02:00 — Final CCR-R01 reconciliation: added the three coverage-edge suites to
  the durable test-route account, bringing the focused regression boundary to eleven and the
  explicit `unit-regression` manifest cohort to nine. Their delivery-attempt changes are test-only;
  production semantics and external review authority remain unchanged.

- 2026-09-01T05:22+02:00 — 260831-CCR-L01 Attempt 9: recorded explicit `unit-regression`
  ownership for the six focused CCR-R01 suites. Their ordinary-test status and the external
  reviewer-owned acceptance boundary remain unchanged; verification remains closeout-owned.

- 2026-09-01T04:34+02:00 — Recorded the certification suites' explicit `unit-regression`
  ownership after the fail-closed closeout census found both declarations absent. No executor,
  product, or test-body behavior changed.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: documented the focused field-taxonomy,
  semantic-topology, graph-scaling, source-plane, and composite-binding regression surface. These
  remain ordinary tests; accepted task evidence stays external. Verification remains closeout-owned.

- 2026-09-01T03:11+02:00 — Added the two focused certification contract suites and their exact
  permanent shared-support ownership boundary. Verification remains closeout-owned.

- 2026-08-31T20:30+02:00 — No route impact: 260831-DER adds one deterministic unit-regression
  module for fresh series, fresh leaf, and retained journal authority classification. Test-route
  ownership remains unchanged.

- 2026-08-31T10:56+02:00 — 260821-ARSPAWN-L5 closeout quality repair: recorded the bounded
  three-test relocation from the oversized structural suite into the existing dispatch-focused
  ambient/plane suite. Both files now satisfy the hard size rail; verification remains
  closeout-owned.

- 2026-08-31T10:33+02:00 — 260821-ARSPAWN-L5 closeout repair: recorded the focused
  regression for strict current-Codex execution-envelope decoding after generation 6 exposed the
  evidence parser at C09. Verification remains closeout-owned.

- 2026-08-31T10:13+02:00 — 260821-ARSPAWN-L5 closeout repair: added exact terminal request-id and
  queued-inbox completion forcing evidence. Verification remains closeout-owned.

- 2026-08-31T09:45+02:00 — 260821-ARSPAWN-L5 closeout repair: added route-level evidence for the
  single tmux namespace shared by the harness, Codex MCP child, liveness probes, and cleanup.
  Verification remains closeout-owned.

- 2026-08-30T16:32+02:00 — ARSPAWN-L4 recorded the public-surface suite's exact transitive
  closeout-input and curator-coherence support edges after the staged lifecycle catalog check
  exposed them; the focused validator passes with 35 governed artifacts.

- 2026-08-30T15:15:36+02:00 — ARSPAWN-L4 added exact-candidate public-surface and eight-starter
  self-update acceptance as explicitly classified integration evidence. Verification remains
  closeout-owned.

- 2026-08-29T21:46+02:00 — MCAR-L03: added the exact-pair forcing surface across memory quality,
  coherence, closeout, and recovery. Dagger verification remains closeout-owned.

- 2026-08-29T20:12+02:00 — Generation-13 repair: reconciled scalar-vocabulary, module-local
  type-parameter, and wrapper-fixture assumptions without weakening the Dagger test population.

- 2026-08-29T19:31+02:00 — Generation-12 repair: aligned legacy external-closeout fixtures with
  the typed reversible-evidence boundary exposed by the Python 3.13 Pyright gate. Verification
  remains closeout-owned.

- 2026-08-29T19:04+02:00 — Added the Python 3.13 named-literal projection-generator forcing case
  discovered by closeout generation 11. Verification remains closeout-owned.

- 2026-08-29T18:29+02:00 — Added forcing coverage for candidate-bound no-impact consumption and
  the preservation of untraced-content refusal.

- 2026-08-29T12:52+02:00 — MCAR-L02 C009 recovery: added the candidate-tree
  observation concurrency forcing boundary exposed by live closeout queue recovery. Verification
  remains closeout-owned.

- 2026-08-29T12:27+02:00 — Clarified that the shared curator-coherence helper owns the complete
  transitive test-consumer set derived through `test_worktree_support.py`, not only its three direct
  importers. Verification remains closeout-owned.

- 2026-08-29T11:41+02:00 — Added the shared structured-coherence fixture owner and documented its
  complete-topology and task-mutation ordering boundary. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Added the lifecycle-owned coherence publication and shared-consumer
  forcing matrix. Verification remains closeout-owned.

- 2026-08-29T07:35+02:00 — Classified the future-code candidate real-Git matrix explicitly as
  integration evidence after targeted Dagger rejected the unmarked test file.

- 2026-08-29T05:17+02:00 — A003 self-review repair: added concurrent-index cleanup,
  closeout-consumption, and immutable-identity coverage to the route summary.

- 2026-08-29T04:55+02:00 — Added the exact future-code candidate mutation/refusal matrix and
  retained the separate lifecycle-operation HEAD-reconciliation boundary. Execution remains
  lifecycle-owned Dagger evidence.

- 2026-08-28T15:45+02:00 — No route impact: the hook repair's fixture extraction restores the
  existing statement budget without adding a test route or changing Dagger acceptance ownership.

- 2026-08-28T14:38+02:00 — No route impact: the scope-reporting regression now pins the existing
  host-hook environment boundary to local/shared `mcp/.venv`; no test route, evidence lane, or
  Dagger-acceptance ownership changed. Verification remains closeout-owned.

- 2026-08-28T06:40+02:00 — Added the six missing focused evidence cards, corrected the lifecycle
  census to 34 artifacts, and preserved Q5-Q8 as non-accepting protocol evidence.

- 2026-08-28T05:10+02:00 — Reconciled Candidate A deletion, seven-assertion preservation, and the
  representative pure/integration/durability measurement owner.

- 2026-08-27T21:10+02:00 — Recorded the retry selector's explicit passing zero-body collection
  proof and preserved the separate missing/uncollected-path refusal.

- 2026-08-27T20:16+02:00 — Recorded the dependency-neutral retry-matrix formatter regression that
  distinguishes a test-tool defect from retry-cache, ownership, or affected-consumer defects.

- 2026-08-27T19:13+02:00 — Added the explicit known-empty retained-context forcing boundary and
  nested wrapper-owned cache setup exposed by the real Dagger matrix.

- 2026-08-27T18:33+02:00 — Recorded explicit retry Coverage.py composition, outer/child quality
  environment isolation, and the full M40-M45 Requirement Attempt Journal structural proof.

- 2026-08-27T17:19+02:00 — Recorded the canonical-collection/affected-execution retry boundary,
  its focused pure forcing suite, and explicit unit-regression lane membership.

- 2026-08-27T13:32+02:00 — M39@v1 and structural-budget repair: added the architect compilation
  proof, exact revision binding, and separately governed MCP tool-signature/Ruff support suite.
  Eight pure doctrine assertions pass; Dagger acceptance remains pending.

- 2026-08-27T12:43+02:00 — M38: added the focused per-requirement acceptance-envelope doctrine
  suite and explicit architecture-fitness manifest registration. The four pure structural tests
  passed locally under the approved diagnostic exception; governed Dagger acceptance remains
  pending.

- 2026-08-26T16:03+02:00 — Post-failure repair: completed deterministic lock setup, duplicate-brief, bounded recovery,
  rollback-seam, and read-only ambiguity forcing; also removed a pre-existing tool-output truncation
  banner. No certifying test execution is claimed.

- 2026-08-26T14:32+02:00 — Added the focused ledger-history regression route and moved the kernel
  round-trip case out of the oversized worktree-support omnibus. No certifying execution claim is
  made.

- 2026-08-26T12:30+02:00 — Reconciled the complete 260821-ARSPAWN-L2 lock, retry, replacement, output,
  and mixed-caller forcing matrix onto the IAS tests overview. Certifying Dagger execution
  remains pending.

- 2026-08-26T08:55+02:00 — Finalized the IAS coordination-evidence label against the frozen
  pass-13 suite inventory.

- 2026-08-26T08:50+02:00 — Rebound the vocabulary-boundary row to the frozen degradation and
  rewrite-healing test names/range.

- 2026-08-26T08:25+02:00 — Repaired the surviving durability-suite reference after the vacuity
  class removal and rebound all three cited classes to the frozen source.

- 2026-08-26T08:15+02:00 — Reconciled the frozen 22-file forcing surface, including six focused
  edge suites and the three paired-source/admission fixture repairs. Acceptance execution remains
  architect-owned; verification metadata awaits the real code commit.

- 2026-08-25T17:21+02:00 — PDLS reconciled the final test/support inventory and bootstrap import
  boundary while retaining Dagger as the sole certifying authority. Verification remains
  closeout-owned.

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: added the canonical published-quality and task-reopen support owners, preserving real evidence/lineage fixtures without promoting test support to product authority. Verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is not Dagger certification.

- 2026-08-25T01:56+02:00 — 260824-PDLS documented the lifecycle catalog, explicit direct cohort,
  fixture-authority splits, single ownership graph, and product-only measurement boundary.

- 2026-08-24T21:23+02:00 — 260824-PDLS added the classifier/runner/bootstrap/firewall/cohort proof
  and moved shared helpers out of the test tree.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: indexed the focused memory-quality, publication/recovery, serving-preflight, and direct-landing forcing sets while preserving concurrent L4 test-route material. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-24T13:51:26+02:00 — No route impact: 260821-DAGQC-L4 reconciled
  existing quality-policy assertions to the diagnostic-versus-acceptance boundary. Preserved the
  concurrent DAGQC-L1 route additions; Dagger acceptance remains architect-closeout-owned.

- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: added the two focused graph-publication/raw-section
  suites and reconciled existing graph identity consumers; recorded that the proposed new
  zero-edge and direct-entry tests are out of scope. Verification metadata remains pinned until
  architect-owned closeout stamps the real code commit.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: no route impact; one existing store-invariant owner gained post-finalization record/journal no-effect forcing without changing the route inventory, against accepted tree `4241908c`. Verification metadata remains closeout-owned.

- 2026-08-21T03:15+02:00 — 260821-ARSPAWN-L1 fix round 1 route impact: the ambient dispatch cohort now lives in `test_dispatch_agent_ambient.py` (extracted from `test_structural_agent_tools.py` by the file-size fix); the structural-seat regression boundary names the new suite. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 route impact: `test_structural_agent_tools.py` gained the 6-test ambient dispatch cohort and `test_spawn_agent_session.py` the caller-kind provenance test. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: ~100 test files updated (import paths to the moved packages, `unittest.main` tail guards removed, new wire-shape suite + coverage tests added). Verified at code commit e5cb139f.

- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: three new forcing suites (serving_preflight, memory_quality_runs, task_execution_topology_l15 split); F8/wait-run_id/judgment-required test additions; orchestration_portfolio test deleted. Verified at code commit de3a0fd9.

- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   L12 adds the graph-render, graph-view, projection-wiring, and title-join forcing suites. Verified at code commit b7f2c8e2.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 route impact: new `test_seat_independent_execution.py`
  and `test_direct_landing.py`; signature-compat updates across the task-document and
  registration-wiring suites; `test_config.py` covers `directExecutionEnabled`. Verified at code
  commit a9d50e08.

- 2026-08-20T05:06+02:00 — 260815-DAG-L14 route impact: new `test_task_sprint_linkage.py` suite
  plus projection tests for `masterRef`/`seats`. Verified at code commit 8071a644.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: five new forcing suites
  (`test_sequential_default_mode.py`, `test_queue_read_degradation.py`, `test_register_scaffold.py`,
  `test_legacy_nature_tolerance.py`, `test_closeout_lane_sync_first.py`) cover the
  scheduling-semantics correction; existing queue/topology/integration suites were adapted to the
  narrowed lane-occupying union, the removed `migrate_execution_topology`, and the
  effective-nature contract. Route purpose unchanged. Verification remains closeout-owned.

- 2026-08-19T04:20+02:00 — Historical DAG-L10 fixture expectations were updated; the unused rich
  simulation generator involved in that pass was later retired by PDLS.

- 2026-08-18T12:00:00+00:00 — No route impact: 260815-DAG-L9 added `inventory_execution_topology` forcing cases to `test_task_execution_topology.py`; route purpose unchanged.

- 2026-08-18T13:00+02:00 — No route impact: 260815-DAG-L8 added the closeout-queue projection surface; route purpose unchanged.

- 2026-08-18T10:30+02:00 — No route impact: 260815-DAG-L7 added the orchestrator portfolio loop; route purpose unchanged.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-18T01:24+02:00 — No route impact: 260815-DAG-L6 added `test_acquire_blocker_refuses_stale_super_tips`; the tests route purpose is unchanged.

- 2026-08-17T12:30+02:00 — No route impact: 260815-DAG-L5 added five organizational-completion test modules; the tests route purpose is unchanged.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-15T13:27+02:00 — No route impact: the closeout Pyright repair adds one test-only
  optional-result narrowing before an unchanged failure assertion.

- 2026-08-15T13:18+02:00 — No route impact: repository Ruff formatting touched the eleven paths
  reported by the closeout hook; all assertions, test ownership, and acceptance altitude remain
  identical.

- 2026-08-15T13:08+02:00 — No route impact: the closeout fast hook requested import ordering,
  a non-overwritten loop binding, and removal of one unused fixture parameter; no assertion,
  production behavior, test owner, or test altitude changed.

- 2026-08-15T12:53+02:00 — L3 targeted-gate route impact: added seven focused queue-owner suites
  and exact atomic/evidence/model/recovery branch matrices after the first full targeted artifact;
  production acceptance policy and test altitude remain unchanged.

- 2026-08-15T11:25+02:00 — L3 static-gate route impact: bound the extracted task-doc queue-scope
  owner to the existing topology suite; no production assertion or test altitude changed.

- 2026-08-15T11:07+02:00 — L3 Dagger-failure route impact: repaired canonical task fixtures,
  real lifecycle ownership, exact stale-evidence diagnostics, post-contract recovery projection,
  structured curator artifacts, graph rollback, and response graph completeness without weakening
  the production queue contract.

- 2026-08-15T10:24+02:00 — L3 file-size route impact: split queue model/ownership checks and
  reopen refusal guards into focused suites while preserving the same production-path assertions.

- 2026-08-15T10:10+02:00 — L3 targeted-gate route impact: bound both split evidence owners
  directly to the primary queue suite without changing production behavior.

- 2026-08-15T09:36+02:00 — L3 fast-hook repair: added forcing for runtime task-reference bounds
  without unsupported projection-schema `maxLength` keywords.

- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: added the behavior, forcing, and
  production-bound queue suites plus adjacent registration/reopen/isolation coverage. Verification
  remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2 route impact: expanded doctrine-plane forcing over the
  complete nature-aware topology, role authority, template shape, no-workbench, and synchronization
  contracts. Verification remains closeout-owned.

- 2026-08-15T03:33:21+02:00 — 260815-DAG-L1 second targeted-Dagger repair: the remaining pytest
  failure was one adjacent legacy expectation, not production or coverage. The application split
  now proves both `orchestrates` and sprint-only `integrationBranch` refuse as partial legacy-master
  edits; the exact artifact already passed CRAP and 423/423 diff coverage.

- 2026-08-15T03:20:17+02:00 — 260815-DAG-L1 independent-review repair: the focused suite now
  verifies the real out-of-root publication targets and poisons a later sprint read to prove
  graph-wave validation and dereference stay bound to one snapshot.

- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: reconciled the obsolete
  implicit-orchestration regression with the explicit migration contract and added deterministic
  malformed-input, confinement, target-kind, missing-target, and diamond-DAG forcing cells from the
  exact failed artifact.

- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: forcing coverage now reaches the
  production create/replace/set-field authoring routes, exact render/projection cells, normalized
  migration failures, master/sprint kind-downgrade refusals, and every supported import spelling
  for the cross-root batch writer.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1 route impact: `test_task_execution_topology.py` forces
  malformed-graph refusals, migration-required legacy visibility, exact command membership,
  preview/apply parity, render/projection output, and rollback on cross-root publication failure.

- 2026-08-14T14:03:04+02:00 — No route impact: R46 removes only an intentionally untaken local
  branch from the existing metrics-shutdown regression by expressing the same timeout assertion
  through `self.assertTrue`. Production, timeout behavior, test authority, and route ownership are
  unchanged; verification remains pinned to the last committed source until closeout.

- 2026-08-14T12:31:43+02:00 — R44 curator: recorded the in-flight metrics-write shutdown race and
  its deterministic worker drain. Verification remains closeout-owned.

- 2026-08-14T12:13:26+02:00 — R43 curator: summarized the candidate, recovery, self-policy,
  executor, and Git-identity forcing repairs. Verification remains closeout-owned.

- 2026-08-14T11:48:55+02:00 — R42 curator: added the two focused suite routes and repointed exact
  scope ownership after the file-size extraction. Verification remains closeout-owned.

- 2026-08-14T11:29+02:00 — R39 curator: summarized the direct-guard, self-policy, altitude, and
  workflow forcing evidence. Verification remains closeout-owned.

- 2026-08-14T09:08+02:00 — No route impact: reopened L23 adds one application regression for the
  existing leaf-only route-review altitude boundary. Test-route ownership and suite structure are
  unchanged; verification provenance remains closeout-owned.

- 2026-08-14T06:25+02:00 — L23 final candidate review: forcing coverage now spans Dagger-only
  startup attestations, fresh-attempt/shared-result quality projection, bounded output/report prune,
  candidate-bound route review, lineage rechecks, failure-atomic integration, and monotonic
  post-claim recovery. Verification provenance remains closeout-owned.

- 2026-08-13T14:32+02:00 — L23 final test-route review: recorded mandatory explicit Dagger diff
  base and generated help, Dagger-only acceptance altitude, diagnostic-only host execution, the
  pytest-inert lineage-launcher deletion, and the focused 26-test/7-line green proof. Verification
  remains closeout-owned.

- 2026-08-13T13:08+02:00 — L23 full-Dagger follow-up: recorded exhaustive coverage for three
  low-branch helpers, the IPC test-only wait-margin correction, and the requirement to run the full
  comparison against the real leaf base. Verification remains closeout-owned.

- 2026-08-13T12:53+02:00 — L23 lineage-fixture repair: recorded real parent series fixtures,
  task-derived source assertions, pre-integration sync refusal after master movement, isolated
  gate-only seams, both post-quality source-tip checks, and explicit replay-helper branch coverage.
  Verification provenance remains closeout-owned.

- 2026-08-13T12:53+02:00 — No route impact: updated the final five-test package-root shape from a
  direct member import to the already-loaded `sys.modules` package record. Test ownership and
  semantics remain unchanged and no Ruff exception exists; this supersedes the 12:26 route note.

- 2026-08-13T12:26+02:00 — No route impact: recorded the direct `__file__` alias used by five
  package-root-sensitive tests. Test ownership, scenarios, and assertions are unchanged and no Ruff
  compatibility configuration was retained; verification provenance remains closeout-owned.

- 2026-08-13T09:27+02:00 — L23 curator: added governing route coverage for the real sibling-
  worktree repository-identity regression; final provenance remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 integration-gate follow-up: the route now covers transitive lineage
  traversal, post-quality closeout refusal before approval claim, integration refusal on source-tip
  movement before memory/merge, and fail-before-host worker/reviewer/curator dispatch when super is
  stale. Import-only test changes follow the runtime and lifecycle model package moves without
  changing their assertions; final provenance remains closeout-owned.

- 2026-08-13T08:47+02:00 — L23 integration-gate repair: reconciled direct transitive-lineage guard coverage, post-quality closeout/integration movement refusals, task-derived parent fixtures, and pre-host worker/reviewer/curator spawn refusal. Verification metadata remains closeout-owned.

- 2026-08-13T00:00+02:00 — L23 post-closeout worker-authority curator repair: paired the worker-entry ordering proof with checkout-isolation proof that `lifecycle-operation` retains live authority but no daemon role. The owner reports 46 focused tests across the two affected files, Ruff clean, and diff-check clean. Verification remains closeout-owned.

- 2026-08-12T23:27+02:00 — L23 Dagger diff-coverage curator follow-up: the route-overview helper suite now proves that source matching still requires an overview outside the supplied memory Git tree while body classification emits no false bucket without comparable memory revision evidence. The owner reports the focused test green, all four previously uncovered branches covered, and exact-file Ruff clean. Verification remains closeout-owned.

- 2026-08-12T23:08+02:00 — L23 Dagger curator follow-up: the Claude late-replay regression now uses a 50ms test-only acceptance window, retaining forced expiry while removing a measured xdist scheduler race; production remains 30 seconds. Evidence improved from one local failure in 100 plus one Dagger gw16 failure to 100/100 one-process repetitions passing. Verification remains closeout-owned.

- 2026-08-12T22:50+02:00 — L23 Dagger curator follow-up: the terminal registry suite now locates tmux `-s` before asserting the custom session name, so optional `-T sync` capability arguments cannot invalidate a semantic name-override proof. The exact focused test passes and Ruff is clean. Verification remains closeout-owned.

- 2026-08-12T22:45+02:00 — L23 curator follow-up: the helper suite now separates generated citation-coordinate-only edits from substantive authored changes: the former may pass without invented history, while metadata-only and untraced changes remain fail-closed. The owner reports 10/10 focused plan tests and 16/16 combined route-overview tests green. Verification remains closeout-owned.

- 2026-08-12T22:36+02:00 — L23 pre-commit type-check curator follow-up: the worktree edge suite now consumes the route-overview helper's full three-value revision contract and typed source evidence, proving ordinary body prose is not citation-coordinate-only. The owner reports 14/14 combined tests and repository-wide Pyright green. Verification remains closeout-owned.

- 2026-08-12T22:25+02:00 — L23 curator follow-up: the helper suite now proves baseline-relative task-edited route overviews enter closeout planning despite unrelated leaf code, while metadata-only overview edits remain stale and refuse. Verification remains closeout-owned.

- 2026-08-12T22:24+02:00 — L23 async-closeout curator follow-up: checkout isolation now proves the exact enclosure report root accepts a self-overwriting operational artifact without opening a sibling coordination escape. The owner reports 14/14 focused tests green. Verification remains closeout-owned.

- 2026-08-12T21:39+02:00 — L23 curator follow-up: added the serving suite's complementary projector drain-failure proof: late worker-thread failure is logged while public cancellation remains `CancelledError`. Verification remains closeout-owned.

- 2026-08-12T21:27+02:00 — L23 curator follow-up: documented the adaptive projector fixture's LIFO cleanup ownership; later async cancellation/await now precedes temporary-root deletion. Production projector behavior is unchanged. Verification remains closeout-owned.

- 2026-08-12T21:18+02:00 — L23 curator follow-up: the platform-subprocess suite now forces deterministic existing-native `$HOME/.local/bin` prepending and real `node` resolution after Windows interop filtering. Verification remains closeout-owned.

- 2026-08-12T20:20+02:00 — L23 curator: documented the final lineage, SQLite ownership, projector, and quality-scratch regression wave; verification remains closeout-owned.

- 2026-08-12T17:27+02:00 — 260731-EFA-L23 final Dagger test-route review: the existing targeted
  code-quality regression now pins explicit progress-report precedence as the complement to its
  environment-fallback assertion. Focused pytest is 1/1; verification provenance remains
  closeout-owned.

- 2026-08-12T16:54+02:00 — 260731-EFA-L23 installed-runtime test-route review: lifecycle tests now
  pair packaged service binding with launcher proof that installed `PYTHONPATH` is preserved and the
  task checkout source root is excluded. Verification provenance remains closeout-owned.

- 2026-08-12T16:52+02:00 — 260731-EFA-L23 packaged-worker test-route review: the lifecycle forcing
  suite now proves the installed CLI builds and binds default worktree services before dispatching
  by task address. Focused proof is green under configuration-owned xdist auto; verification
  provenance remains closeout-owned.

- 2026-08-12T16:28+02:00 — 260731-EFA-L23 final test-route review: the code-quality wrapper suite
  now pins environment-derived enclosure progress-report configuration in the existing targeted
  file-size-arm regression, including explicit optional report arguments. This closes the staged
  diff-coverage branch without changing the route's test ownership; verification provenance
  remains closeout-owned.

- 2026-08-12T15:19+02:00 — L23 curator: added durable lifecycle, Dagger clean-quality, Codex probe, native subprocess, and notifier-addressing forcing groups; verification provenance remains closeout-owned.

- 2026-08-12T09:20+02:00 — No route impact: the 260731-EFA-L20 reopen replaces one unreachable context body with a direct raising-`__enter__` assertion; test-route ownership and safety coverage are unchanged.

- 2026-08-12T08:41+02:00 — No route impact: 260731-EFA-L20 preserves the test route's ownership while deleting unreachable scaffolding, tightening opted-in installed-test failure honesty, and adding direct coverage for the two master CRAP findings.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24: added host-managed
  full-gate and optional explicit-cap regression coverage; pytest remains
  literal `-n=auto`. Verification metadata remains pinned until closeout stamps
  L24.

- 2026-08-12T04:41+02:00 — 260731-EFA-L22 closeout repair: recorded the public settings-update
  branch matrix added to clear the session owner's enforced CRAP finding without weakening the
  threshold.

- 2026-08-12T04:15+02:00 — 260731-EFA-L22 Codex Desktop repair: migrated the shared and composed
  fake initialize responses to the clean-cut current Desktop grammar and recorded the exact client
  suffix gate; no conversation or history behavior changed.

- 2026-08-12T03:31+02:00 — 260731-EFA-L22 closeout repair: recorded the real invalid-byte hook
  regression that distinguishes raw runner surrogateescape from transport-safe facade diagnostics.
  The repair prevents MCP serialization failure without changing the one-runner boundary.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: recorded the three responsibility splits for
  structural identity, citation routing, and quality-runner policy; regenerated split-sensitive
  route citations without reducing coverage.

- 2026-08-12T00:20+02:00 — Corrected the xdist regression description after worker selection
  moved from wrapper argv to root pytest `addopts`. Verification metadata remains pinned until
  closeout.

- 2026-08-12T00:08+02:00 — Recorded worker-private XDG cache isolation and serialization-only
  subtest diagnostics required by the parallel pytest executor. Verification metadata remains
  pinned until closeout.

- 2026-08-11T23:56+02:00 — Recorded the focused command-construction regression that pins
  pytest-xdist `-n auto` alongside derived coverage arguments. Verification metadata remains
  pinned until closeout.

- 2026-08-11T22:28+02:00 — 260731-EFA-L19 final curator pass: recorded the new focused structural
  refusal module, the expanded structural coverage companion, and exact unavailable-runtime skips
  for installed harness and live Node probes. Verification metadata remains pinned until closeout.

- 2026-08-11T20:28+02:00 — 260731-EFA-L19 closeout-gate repair: recorded the `AgentRole`-typed
  seat-lifecycle fixture and the durability harness's type-check-safe, historical-archive-only gate
  import; no production compatibility path was added.

- 2026-08-11T14:40+02:00 — Recorded the enclosure-scope regressions that distinguish temporary leaf
  base comparison provenance from real commit verification and forbid invented provenance on a bare
  official-memory check.

- 2026-08-10T18:31+02:00 — 260731-EFA-L21: added the checkout-coordination isolation regression
  suite and updated global-state tests for the explicit kernel-owned pytest mode. Verification
  metadata remains pinned until approved closeout.

- 2026-08-10T12:46+02:00 — L9 closeout-order repair: recorded focused entity-preflight and
  real-hook/exact-index regression coverage; verification metadata stays pinned until closeout
  stamps the repair commit.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 route impact: recorded the three new suites and the
  baseline fixture. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 route impact: recorded the three new suites and the
  extended closeout/hook/settings/scope-reporting/observer families. Verification metadata stays
  pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 route impact: recorded the in-place test-family splits, the detector/facade-surface/conformance suites, and the count fix. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this route against the frontend-rail change set. No route impact: test_quality_scope_reporting.py was re-scoped to run the real hook with an npm shim; the tests route's meaning is unchanged.

- 2026-08-05T22:30+02:00 — 260731-EFA-L16 route impact: recorded the cross-store lock-order forcing tests (placement, rendezvous ABBA reproduction, offload proofs, anti-vacuity). Verification metadata pinned until closeout stamps the code commit.

- 2026-08-04T14:41:21+02:00 — 260731-EFA-L6 S18-B01 closing same-reviewer correction: narrowed the rich-sim claim to the complete raw-token/unknown_cells and Markdown-bypass relationship under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.

- 2026-08-01T19:40+02:00 — 260731-EFA-L5 curator. The Durable Store Integrity Gate section named
  three properties that make the instrument's output evidence and **was silent about the instrument's
  own defect**, which is the property that failed. Added the fourth: the harness derived its work
  directory — including the reclaimer's **stop flag** — from `root.parent`, and
  `test_controlplane_store_durability.py` passes sibling roots under one `self.tmp`, so all cases
  shared one flag and every case after the first left the tick loop after roughly one tick.
  Measured before the fix: **25 reclaim ticks for the first store and exactly 1 for each of the
  other seven, all eight reporting 0.00% loss**; the forced scenarios additionally shared
  `forced.id` and the `*.err` files, so a case whose appender wrote nothing was scored off its
  predecessor's receipts. Recorded the fix as
  `harness_work_dir(root) = root.with_name(root.name + "-harness")` — a **sibling**, because `root`
  does not name one place (control-plane logs under `root/workspace`, provider logs under
  `root/logs/observer/providers`, `GateStore` also globbing `root/lifecycles/*/gates.jsonl`) while
  the accounting reads that whole tree as raw bytes — and the guard as `MIN_RECLAIM_TICKS = 10`
  raising `VacuousRunError` at the end of `run_stress`, **in the instrument rather than in either
  suite**, so both contract suites and bare `main()` runs share one floor. The floor's evidence is
  recorded with its direction: 22-39 ticks idle, 34-49 under 24-way load, load *raising* the count,
  with 20 rejected because the observed minimum is 22. **The reassuring half is recorded beside
  it:** the documented base-commit rates survived, re-measured at attention 23.91% / gate 9.38% /
  supervisor-signals 8.00% / expectation-rows 7.63% / nudges 7.50% / operator-inbox 0.00% — same
  ordering, same lone survivor — because `main` already built each case a root under its own
  parent. The bug never corrupted the historical measurements; it hollowed out the ongoing
  regression. Those six figures are **labelled as the leaf's four-run means that do not appear in
  the source**, with the source's *ranges* named and located
  (`HarnessSensitivityTests`' class docstring) and each mean checked to fall inside its range. Two
  invariants added: *a measurement must refuse to report a vacuous result*, and *sibling roots under
  one temp directory must remain legitimate* — a guard demanding distinct parents would be the same
  defect rewritten as a convention. **Drift repaired:** the section described the instrument as
  covering six stores and carried the provider adapters as unstaged mid-flight work; they have
  landed, so it now says eight with `CASES` / `PROVIDER_CASES` held apart, and the three record
  classes (`survivor-*` / `decoy-*` / `anchor-keepalive`) are stated because they are what make
  "loss" mean a row nobody decided to drop. The two `_store_durability.py` and
  `test_controlplane_store_durability.py` evidence rows carried ranges from shorter versions of both
  files and were re-derived; rows were added for the instrument's fix/guard and for the provider
  suite. **Citations:** every range was opened and checked against each symbol the row names, ends
  included. `_store_durability.py` (now 1153 lines) and `test_controlplane_store_durability.py` are
  staged with no unstaged edits and are cited by line; `test_provider_store_durability.py` still
  carries unstaged edits and is cited **by symbol name only**, as are all `controlplane/` and
  `providers/` source modules. Verification metadata untouched; closeout owns it.

- 2026-08-01T19:10+02:00 — Measured-claim repair in the Durable Store Integrity Gate section; nothing
  about the instrument's three trustworthiness properties, the torn-line policy, the replay-window
  counterfactual or the mutex was touched, because it was right. The section asserted six
  base-commit loss rates, "127 of 2000", "10 runs per store" and "zero torn lines in every run" as
  measurements, and closed with "0 lost"
  against the current tree. **No base-commit measurement artifact is committed anywhere in the
  tree** — `_store_durability.py::main` can write a JSON payload but none is stored, no test asserts
  a rate, and no committed invocation passes `runs` — so that is now stated once and the rates are
  separated from what *is* checkable. `BASE_COMMIT = e52edaf5` and the `STRESS_PROFILE` literals
  (4 × 50 @2 ms against 1 reclaimer @5 ms) stay asserted, because they are literals in the file.
  31.45% and 11.50% stay asserted, on the authority of four and three independent sites
  respectively. 10.50 / 10.20 / 9.20 / 0.00%, 127 of 2000, "10 runs per store" and the whole-not-torn
  property are attributed to `durable_store.py`'s module docstring, which is the text these cards
  document. **The post-fix claim was overstated on two axes and is corrected against the test
  source, citing the class:** `MultiProcessDurabilityTests` asserts `lost == 0` in all three
  scenarios, but `forced_unlink` iterates `APPEND_CASES` — **five** stores, attention dismissals
  excluded by construction because it has no `append` — and `torn_lines == 0`,
  `append_error_count == 0` and `reclaim_error_count == 0` are asserted in the **`stress` scenario
  only**. Recorded as mid-flight, not as landed: `_store_durability.py` carries unstaged edits
  adding two provider adapters, which do not widen those counts because the working tree keeps
  `CASES` at the six control-plane stores beside a separate `PROVIDER_CASES`. The R14 sentence
  beneath it was already exact and was left alone. The 14:20 entry below
  carried the same six-rate list and was reduced to a pointer at this entry. Verification metadata
  untouched; closeout owns it.

- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator. Nine files in this route changed for one defect —
  measured record loss in the six control-plane JSONL stores — and **four of them are new**, so the
  card gained a section, nine invariants and nine evidence rows. **Durable Store Integrity Gate**
  documents the four new suites with the instrument first, because the numbers depend on it:
  `_store_durability.py` holds no assertion at all, expresses each store through its own shipped
  reclaim entry point rather than a reimplementation, and is trustworthy for three stated reasons —
  real processes via `multiprocessing` fork (the defect is cross-process; the GIL would serialise
  the window), **dual-mode** operation where a script run pins `PYTHONPATH` to exactly one
  `mcp/src` and `_require_source_root` refuses fatally if `agents_remember` resolved elsewhere
  (which is what let it measure a `git archive` of the pristine base commit), and **loss accounting
  that deliberately bypasses every store's own `read`** — a raw tolerant JSON-lines reader counting
  "record lost" and "line torn" separately, so a strict reader cannot turn a measurement into an
  exception and a tolerant one cannot report tearing as loss. Recorded the baseline the sources
  report at `e52edaf5` against the checkable `STRESS_PROFILE` literals (4 appenders × 50 records
  @2 ms against 1 reclaimer @5 ms) — corrected by the 19:10 entry above, which splits those rates by
  corroboration and restates the post-fix claim at its true strength.
  Recorded `test_controlplane_store_durability.py`'s three claims (R10/R8/R14, with loss and
  raising asserted separately because a store that raises instead of losing has moved the failure),
  `test_gate_replay_window.py`'s counterfactual (the whole defence is one appended record; delete
  only the `applied` line and the approval is spendable again — base commit exits 1 with
  `AssertionError: 'approved' != 'applied'`, fixed tree exits 0), and
  `test_durable_store_contract.py`'s in-process axis. **The mutex is documented as what it is and
  not as a race fix:** `flock` already excludes two threads of one process through the open file
  description, that was measured rather than assumed, and `thread_mutex_for` closes the
  *dependence of thread exclusion on where the handle came from* — cache one lockfile handle on the
  store and `flock` silently stops excluding, with nothing in the tree failing. Its
  unsafe-filesystem tests fake the **filesystem** at the `fcntl` boundary, scoped to one module's
  reference, and assert only on raised type, message text and on-disk state. Recorded that the five
  updated suites replaced "the pruned log stops existing" with emptiness (`is_file()` +
  `read_bytes() == b""`), which is strictly stronger since zero bytes proves the records left
  rather than that the file did — and that `test_interaction_retention.py` is the **exception**:
  its assertion had been reading a side effect of the projection tick's physical rewrite, the very
  behaviour the leaf removed, so it was split into two proven claims (the projection leaves the log
  byte-identical — newly asserted — and `GateStore.compact` in the owning process empties it)
  rather than restated. Added nine invariants covering measurement independence, real processes,
  naming the measured tree, emptiness-not-absence, splitting a claim whose evidence was a removed
  side effect, the mutex's exact scope, and faking a platform rather than the code. Added nine
  Repo-Internal rows. **Citations:** every added row's range was opened and checked against each
  symbol the row names, ends included; the four new suites' self-ranges are stable (none of the
  nine test files carries unstaged edits). Six control-plane source modules
  (`durable_store.py`, `store.py`, `attention_dismissals.py`, `expectation_rows.py`,
  `orchestration_nudges.py`, `supervisor_signals.py`) were still being edited in the code worktree
  during this pass, so rows pointing into them are cited **by symbol name** rather than by line
  range; the symbol is the durable anchor and closeout should treat the linked file cards as
  authoritative for line numbers. Verification metadata pinned until closeout stamps the L5 commit.

- 2026-08-01T14:05+02:00 — 260731-EFA-L4 curator (correction pass), one clause. The 00:50 entry below
  said `response_model` "enforces nothing on the 59 handlers that return a `Response`", which
  mis-describes the composition of the 59: **57** of the 61 HTTP routes return a `Response` subclass
  and **2** are SSE async generators feeding an `EventSourceResponse` (`GET /api/stream`,
  `GET /api/events`) — that is the 59 on which the decorator contributes an OpenAPI schema and
  validates nothing. The remaining **2** (`GET /api/terminal/sessions`, `GET /api/harnesses`) return a
  bare `dict` and *are* validated by FastAPI. The conclusion the entry draws was right; only the
  breakdown was wrong. Verified against `serving/response_contract.py` L11-L18 and against this
  card's own body. Nothing else changed.

- 2026-08-01T00:50+02:00 — 260731-EFA-L4 curator. Twenty-one modules in this route changed and
  **three are new**, so the card gained two sections. **Wire-Contract Conformance Gate** documents
  the three new suites as the enforcement half of the leaf, each with its stopping point stated
  rather than implied: `test_serving_response_conformance.py` (drives all 61 HTTP routes because
  `response_model` enforces nothing on 59 of them — **57** whose handler returns a `Response`
  subclass and **2** SSE async generators feeding an `EventSourceResponse`, `GET /api/stream` and
  `GET /api/events`; only `GET /api/terminal/sessions` and `GET /api/harnesses` return a bare `dict`
  and are validated by FastAPI; alias-strict
  `validate_wire`; the AST key-set equality behind the two genuinely-validated `dict` routes, pinned
  at 52 keys; **and the counted ledger — 286 declared `(method, path, status)` pairs, 133 driven,
  153 listed in `UNDRIVEN_DECLARATIONS` with a reason and asserted exactly**, with every one of the
  61 routes driven on at least one status), `test_served_state_conformance.py` (the 200 body
  validates as `ServedWorkspaceProjection` and is required to FAIL as `WorkspaceProjection`; the 304
  is body-less; a `delta` carries none of `SERVED_TAIL_FIELDS`; the tail stays out of
  `latest-state.json`; and `_assert_populated` is what stops the whole file from measuring an empty
  scaffold), and `test_wire_vocabulary_exhaustiveness.py` (three mechanisms of different kinds over
  the contract cells and seven further vocabularies; **the AST scan reads bare string literals only
  and is explicitly not a guarantee on its own** — pyright plus the no-`dataclasses.replace` rule is
  what makes it total, because typeshed types `replace` as `**changes: Any` and produced zero
  diagnostics against a four-member `Literal`). Recorded the measured motivation from the module
  header (165 of 213 `series-contract.md` files, 77.5%, made `context_packet` raise across seven
  gaps) and the route-wide evidence for it: fixtures were writing `"light"` / `"chat"` /
  `"master-series"` / `"master-task"` / `"master"` against a two-member `WorkflowKind`, and nothing
  failed, because `load_contract` degrades and quarantines while the refusal lives at the write
  boundary a markdown fixture bypasses. **Choke-Point And Closeout Gate Coverage** records the
  `TOOL_RESPONSE_MODELS` retyping consequences now pinned (a stale supervisor made every response
  fail its own `model_validate`; the advertised `tokens` excluded `nextStep`/`supervisorBanner`, and
  so did `amb.emit_tool`) and the four new closeout-gate classes (real `derive_scope` into real
  `ruff`; scope-equals-commit-tree as an equality covering the deleted-file mirror; both staging
  refusals asserted as damage that does not happen, with ordering proven by a surviving `MERGE_HEAD`;
  and retry/first-run committed-tree equality). Added ten invariants. **Citations:** all 33
  citation-bearing evidence rows in `Repo-Internal References` were re-checked against the current
  files (range in bounds, and the named symbol read back at the boundary); 2 had moved and were
  repaired — `test_serving.py` L430-L492 → **L441-L503** (the class shifted +11 when `_build_wire`
  was added; the range now runs from
  `test_snapshot_subscription_cannot_lose_an_interleaved_projection` at L441 through the end of
  `test_cancelled_waiting_stream_releases_its_subscription`, which the old range cut off by one
  line) and `test_worktree_closeout_quality_gate.py` L38-L222 → **L49-L369** (the old range covered
  only part of `CodeQualityGateTests` and never reached the `CloseoutCodeQualityGateTests` argument
  spy the claim names; both class statements confirmed at L49 and L248). Added eleven evidence rows.
  Also repaired a rendering defect: five rows in the 3-column `Repo-Internal References` table
  carried only two cells, so their source path was rendering in the Citations column; each gained an
  explicit `n/a` citation cell with no text changed. Verification metadata pinned until closeout
  stamps the commit.

- 2026-07-31T22:30+02:00 — 260731-EFA-L3 curator (re-verification pass after the fix workers).
  **Both new suites were restructured, so every citation into them was re-derived from the current
  files and every one had moved.** `test_git_command.py` (697 lines): `DecoyRepositoryTests`
  L151-L207 (was L84-L140), `SingleRunnerTests` L389-L459 (was L322-L402),
  `BenchmarkRunnerEnvironmentTests` L656-L693 (was L405-L442); each range re-read and confirmed to
  open on the named `class` statement. `test_cold_start.py` (421 lines): `ColdStartTests` L199-L218
  (was L153-L171), `VendoredVocabularyTests` L221-L331 (was L174-L228). `git_command.py` L24-L96
  re-checked and still correct (`GIT_REPOSITORY_SELECTOR_ENV` at L24 through the end of `run_git`).
  Added two evidence rows for the suites that did not exist when the first entry was written:
  `SingleRunnerGuardReachTests` L462-L540 and `TimeoutClassTests` L543-L653;
  `CorruptVendoredVocabularyTests` L334-L417. **Corrected the `.gitattributes` row**, which said the
  file's rule was inert and its regression removed — true of the `blank-at-eol` rule (still L1-L3)
  but no longer of the file: L13's `-text` entry names the shipped vocabulary by filename and
  cit:([`test_the_gitattributes_entry_names_the_shipped_file`], mcp/tests/test_cold_start.py:248-261) is its live regression. Wrote up the
  guard-on-the-guard reasoning (an AST sweep reports a hole and a clean tree identically, so each
  bypass form is planted: `from subprocess import run`, `/usr/bin/git`, `**kwargs` mistaken for
  `env=`), the per-command timeout assertions and their required-keyword recorder, the
  no-module-scope-import discipline via `tokens_module()`, the bounded-join deadlock guard, and
  `CorruptVendoredVocabularyTests` — including that it works on copies, asserts the corrupt file is
  *still there* afterwards, and that CRLF-mangling and truncation were measured to pass silently
  before the digest check moved into `models/tokens.py`. Verification metadata pinned until closeout
  stamps the code commit.

- 2026-07-31T21:05+02:00 — 260731-EFA-L3 curator: two modules joined this route and both are here
  because the property they guard cannot be observed the ordinary way. Added the **Single-Runner Git
  Gate** (`test_git_command.py`: the decoy repository whose `patch.dict` blocks deliberately undo
  `conftest.py`'s selector strip, the `SingleRunnerTests` AST sweep pinning
  `kernel/git_command.py` as the only module that spawns git, the stated blind spot covered by
  `BenchmarkRunnerEnvironmentTests`, the stdin/`input_text` and three-timeout-class contract, the
  `cleanup.py` remote-stall arms, and the pre-push-hook framing of `QualityGateGitTests`) and the
  **Cold-Start Gate** (`test_cold_start.py`: the subprocess probe with cold caches and a
  proven-effective socket block, the warm-versus-cold count equality, and the re-derived vocabulary
  hashes). Qualified the `conftest.py` selector-inventory sentence, which read as coverage and is
  only fixture safety. Recorded that `test_serving.py::BuildInfoTests` now patches
  `serving.build_info.run_git` — patching `subprocess.run` in a consolidated module patches nothing.
  Added two invariants and three evidence rows. Verification metadata pinned until closeout stamps
  the code commit.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 8 cross-file line citations, each re-anchored on a read-back boundary. `test_conversation_control_api.py` L1-L379 (382-line file; also dropped the "seventeen routes" phrase — that count is pinned in `test_conversation_foundation.py`, not here); `test_conversation_runtime_composition.py` L113-L252 (was L106-L260 in a 252-line file); `test_harness_submission_authority.py` L1-L675 (was L1-L687 in a 678-line file); `test_harness_control.py` L1-L1958 (was L1-L1180; the file is 1961 lines and the IPC class runs to L1958); `test_serving_harness_control_api.py` L1-L891 (was L1-L700; extended the claim to name `ControlLivenessMemoRetentionTests` at L779); `test_serving.py` L430-L492 (the three `StreamEventsTests` the claim names, was L395-L457); `test_route_index.py` L199-L907 (fixture through the last test, off the `unittest.main()` guard); `test_static.py` L29-L144.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator, **correcting and completing the mid-leaf entry
  below**. `test_complexity_baseline.py` was deleted along with the whole complexity ratchet and its
  file card removed; `test_gate_scope.py`'s three allowlists were deleted, so the routing paragraph
  and evidence row that described them were wrong and are rewritten. Twenty-two further modules
  joined the route and now have file cards: the gate suites `test_diff_coverage.py` and
  `test_gated_integration_runner.py`; the Pi capability helper `_pi_rpc_capabilities.py` with its
  recording `fixtures/pi_rpc/0.80.7-capabilities.json` (renamed from 0.80.6) and
  `test_pi_rpc_events.py`; the serving suites `test_serving_app_routes.py`,
  `test_serving_app_background_loops.py`, `test_serving_helper_behaviour.py`; the platform suites
  `test_platform_edge_refusals.py`, `test_platform_long_tail.py`,
  `test_packaged_assets_and_context_values.py`, `test_provider_runtime_helpers.py`; the conversation
  suites `test_conversation_control_and_library_helpers.py`,
  `test_conversation_control_projector_edges.py`,
  `test_codex_adapter_thread_routing_and_registry.py`; the harness suites
  `test_harness_control_runner_config.py`, `test_harness_logs_user_message_readers.py`,
  `test_harness_submission_authority_adapter_contract.py`; the worktree suites
  `test_worktree_and_observer_helpers.py`, `test_worktree_edge_paths.py`; plus
  `test_mcp_registration_wiring.py` and `test_onboarding_integrity_edges.py`. Recorded the Pi
  capability anti-drift contract, the branch-coverage CRAP change, and three pre-existing 1:1
  fixture gaps closed. The route index is now strictly 1:1 at 210 files. Verification metadata
  pinned to the leaf's reformat commit until closeout stamps the code commit.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 curator (mid-leaf, partly superseded above): three new test modules joined this route —
  `test_gate_scope.py` (the gate's scope is the tree, asserted against real argument vectors, with
  shrink-only reason-bearing allowlists), `test_complexity_baseline.py` (the shrink-only complexity
  ratchet in all four failing directions plus the `--write` cap asymmetry), and
  `test_sync_harness.py` (drift between `scripts/harness/` and the nine generated trees, content and
  mode). `test_code_quality_check.py` roughly doubled with four classes holding Radon-is-a-report,
  every-enforcing-step-can-fail, scope derivation, and the pytest strictness/marker/warning
  contracts. Rewrote the "local gate" routing paragraph accordingly and added five evidence rows.
  Verification metadata pinned to the leaf's reformat commit until closeout stamps the code commit.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1 curator: replaced the Generated Bundle Whitespace Policy
  Gate with the Dashboard Bundle Placement Gate and added a Static Surface Gate. `test_sync_dashboard.py`
  inverted three fail-open tests into refusals and proves `--check` no longer exists through a real
  subprocess; `GeneratedDashboardWhitespacePolicyTests` was removed because the `.gitattributes`
  exception it policed now names a git-ignored path. Added the new `test_static.py` (both static
  states, deterministic, including method parity against the real `StaticFiles` mount) and recorded
  the three build-dependent rewrites in `test_serving.py`. Recorded the two-test split that holds
  the local gates to the wrapper after the hook tiering, and the closeout-gate argument spy.
  Refreshed the affected hot-path routing and reference rows. Verification metadata remains
  pre-commit.

- 2026-07-30T15:05+02:00 — 260727-CHATS-IM-L4: routed the new real-local-subprocess lifecycle tier for
  Claude (transport ownership release across start -> stop -> start, and the adapter's floor
  probe/re-launch to control readiness over the real transport), and recorded that the live smoke's
  `/cost` arm asserts the still-unimplemented harness slash-command capability owned by an upcoming
  master, so its red state there is expected rather than a regression.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: added the two new native-history
  regression suites and routed measured-size transport, exact probe/fallback, one-shot resource
  bounds, cycle/legacy behavior, typed IPC, selected-child concurrency/continuity, and dashboard
  persisted-focus/retry coverage. Updated active route ownership from two to three. Verification
  metadata remains pinned while uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the sub-agent surface remediation
  regression pins — nine new demux-suite tests (concurrent parent pendings, method-first degrade,
  bounded pending map, load-shed queue), two codex-agents projector tests (concurrent-parent
  projection, singular rotation), one `test_harness_control.py` guard test, and the flipped
  decline-not-fail experimental-request case in `test_codex_app_server_adapter.py`; Hot Path
  Summary and route-impact sections updated. Verification metadata stays pinned (remediation
  uncommitted).

- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: added the harness sub-agent regression set —
  the NEW shared `_agent_wire_fixtures.py` and five NEW focused suites (thread demux, codex
  projector agents, claude projector agents, library agents) plus targeted extensions to
  `test_harness_control.py` (multiplexed respond + plural serialization), `test_harness_control_claude.py`
  (flag floor + relaunch), `test_conversation_active_service.py` (reordered binder pin + per-thread
  dict assertions), and `test_conversation_library_ports.py` (additive agent fetch at the fake
  boundary). New-file sidecars registered; verification metadata stays pinned until L7 closeout
  stamps the candidate commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental CRAP/commit-gate curation:
  added the default-threshold, closeout mutation-order, public-tool-description,
  and Claude public-projector regression contracts. Verification metadata remains
  pre-commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.

- 2026-07-21T12:00+02:00 — 260718-CHATS-L5P curator: body-reviewed against the post-L5 pyright fixup
  (commit `352d5cd`) that changed `test_chats_l5_hardening.py` after the L5 verification (`68b3205`). The
  change is strict-pyright conformance only (protocol-conformant fake-host param naming, an
  `isinstance`-narrowed assertion, an explicit transcript-`state` annotation, a `Mapping` import) — zero
  behavior change, no `type: ignore`, all seven H1/H2/F2/F4 regressions identical in intent — so the
  route's hardening-regression enumeration (H1 quarantine + F2, H2 authority-pin + F4, the projector-tier
  and installed companions, the 10k baseline) is UNAFFECTED and stands as written. No body change;
  verification metadata advanced to `352d5cd` (the enumeration was reviewed this cycle).

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: added the half-time functional regression
  narrative — the NEW `test_chats_l5f_leaks.py` (R5 `SessionLockLeakTests` + `QueueRowsBoundTests`) and
  the R1-R6/R4 additions across `test_conversation_active_projectors.py`, `..._active_service.py`,
  `..._contracts.py`, `..._control_operations.py`, `..._library_gates.py`, `..._library_installed.py`,
  `test_harness_control_evidence.py`, `test_harness_control_client.py`, `test_harness_launch.py`, and
  `test_provider_containment.py`. Corrected no version-lock language in this route's narrative (the R4
  contract-only gate is captured in each test sidecar). The new-file sidecar's verification is blank
  (uncommitted); route index refresh registers it. Verification stays pinned until L5F closeout.

- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: added the evidence-backed hardening regression
  narrative — the new `test_chats_l5_hardening.py` (H1 catalog-sweep quarantine + F2, H2
  authority-pin + F4), the projector-tier H2/F1 companions in `test_conversation_active_service.py`,
  and the F1 installed regression in `test_conversation_control_installed.py` — and noted the 10k
  renderer DOM/interaction baseline lands in the dashboard test tree, not here. New file card
  `test_chats_l5_hardening.py.md` registered in the route index. Verification metadata stays pinned
  until L5 closeout stamps the candidate commit.

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: added the authoritative control-API regression
  set — the shared `_control_plane.py` topology (real bridge/IPC/authority/L0 seam, `NOW`-anchored
  service), the four focused suites (operations incl. Finding 1/2 pi settlement regressions; queue
  incl. the frozen-clock expiry proof; attachments incl. on-disk spool deletion; the seventeen-route
  API over a real wire), and the opt-in installed proof — plus the seventeen-route foundation pin, a
  control coverage reference row, and the corrected "control empty" claim. Verification metadata stays
  pinned until L3 closeout stamps the candidate commit.

- 2026-07-20T15:10+02:00 — 260718-CHATS-L3E curator: added the evidence-truncation settlement
  coverage to the `test_harness_control_evidence.py` description — the `ClipHelperTests` byte-level
  terminal-identity preservation tests plus the giant-scalar drop-whole (256/257 boundary)
  regression, and the new `EvidenceTruncationSettlementIpcTests` oversized-frame end-to-end
  regressions mirroring L3's `_pi_stop_reason` / `_codex_terminal_outcome` reads. Verification
  metadata remains pinned until closeout stamps the candidate commit.

- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: added the native control-plane regression
  set — the contract suite `test_harness_control_plane.py` (interrupt/timeline/asset/recovery and
  client-validation batteries, 25 tests + 35 subtests), the opt-in version-locked installed
  capture `test_harness_control_plane_installed.py`, and the redacted `control-plane/*` fixture
  rows with `enablesCapabilities: false`. Verification metadata remains pinned until closeout
  stamps the candidate commit.

- 2026-07-19T18:25+02:00 — 260718-CHATS-L1 curator (memory rebase): union-merged the landed L2
  library regression-set content with the L1 active regression-set content after the master
  memory branch advanced — both suite families, the merged foundation-pin coverage (active two
  routes + library five routes; control empty), and both reference rows survive. Verification
  metadata remains pinned until L1 closeout stamps the candidate commit.

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: added the active conversation serving
  regression set — four focused suites (canonical status/parity, mapper grammars, engine/store
  with the F1/F2/F3 fix pins, and the real-socket production routes proving identity, cursor
  refusals, epoch-flip gap+close, provenance, parity, and no-PTY authority) plus the foundation
  pin's exact two-route active-child assertion. Verification metadata remains pinned until
  closeout stamps the candidate commit.

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: added the native conversation library
  regression set — six focused suites over doubled boundaries (ASGI status ladder, cursor/scope,
  gates, ports, open arms) plus the opt-in installed-runtime suite proving the live Codex/Pi
  gates, both real end-to-end opens, and the Claude version-mismatch posture — the foundation
  pin's exact five-route library assertion and helper source set, and the observed
  evidence-not-enablement fixture rows. Verification metadata remains pinned until closeout
  stamps the candidate commit.

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: added the native evidence contract suite and
  the opt-in installed-runtime capture — per-harness round-trips with no-leak proofs, buffer and
  continuation bounds, cross-domain/epoch typed rejection, the provenance matrix, the codex resume
  channel, and the redacted version-locked `substrate-evidence/*` fixture rows. Verification
  metadata remains pinned until closeout stamps the candidate commit.

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: added the conversation runtime composition
  and authorization contract suites — install-once/fail-closed composition shapes, per-app
  isolation, no-singleton and no-injected-identity proofs, loopback-only local-operator resolution,
  and cross-principal rejection — plus the one-line `coordination_root` call-shape follows in the
  two harness-control suites. Verification metadata remains pinned until closeout stamps the
  candidate commit.

- 2026-07-18T21:05+02:00 — FEUI-MX-FIX-5 added the real-Git generated-positive/authored-negative
  whitespace regression, the direct shipped-JavaScript `blank-at-eol` boundary, Vite/raw-sync byte
  ownership, the rejected-normalization rationale, retained near-miss checks, and the two-build
  byte/fingerprint determinism proof. Verification metadata remains pinned until closeout stamps
  the candidate commit.

- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: added the deterministic Git/path-rule census matrix,
  regular/linked/contaminated byte-convergence proof, typed failure coverage, and full-apply
  JSON/Markdown carryover-authority refusal/retention matrix with exact zero-mutation assertions.

- 2026-07-18T14:16+02:00 — 260715-FEUI-MX-FIX-1: added route-level coverage for deterministic
  snapshot/subscription handoff, first-recovery full snapshot with build identity, identical-state
  silence, later named delta, and explicit close/cancellation subscriber cleanup. Verification
  metadata remains pinned until closeout stamps the candidate commit.

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the build/static, raw-event, tmux-environment, and
  narrow harness-discovery regression matrix. Verification metadata remains pinned pending
  candidate closeout.

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: documented the hostile normalized-contract
  matrix, exact two-port/three-router topology, repository-only helper resolution, and redacted
  non-enabling runtime fixtures. Added current governing/reference structure; verification remains
  pinned to committed source truth until closeout stamps the candidate.

- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: added the authoritative submit/withdraw
  adversarial matrix, exact-ref and early-completion proofs, safe-retry/first-byte split, raw-free
  status/API bounds, native no-queue guarded-write semantics, and retention/privacy invariants after
  canonical review round 6 PASS.

- 2026-07-16T07:27+02:00 — 260714-ACPUI-L5 curator: added route coverage for the complete Claude
  discovery-selector grammar and normal-launch preservation, plus the explicit-opt-in two-turn
  Codex live advertise/launch/queued-set/retention proof with sanitized evidence recording.
  Verification metadata remains pinned until closeout stamps the L5 code commit.

- 2026-07-16T06:26+02:00 — 260714-ACPUI-L4 curator: added route coverage for install/auth cache
  fencing, failed-refresh quarantine, complete-pair launch, live-reopen/dead-replacement truth,
  cross-process one-process publication, exact-session first-byte ambiguity, request-id idempotency,
  retained reconciliation without resend, raw-free public responses, liveness-first status, and
  shared role-spawn conflict behavior. Verification metadata remains pinned until closeout stamps
  the L4 code commit.

- 2026-07-16T01:34+02:00 — 260714-ACPUI-L3 curator: added route coverage for exact five-value
  setter truth, FIFO/cancellation behavior, Claude correlated terminal and dynamic Fable evidence,
  Codex ordered selection epochs and successful fresh-turn promotion, Pi bounded coherent
  error/clamp readback, 8/64 reclamation scaling, and the transitive 17-module no-paste guard.
  Daemon setter endpoints remain L4. Verification metadata remains pinned until closeout stamps
  the L3 code commit.

- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: added route coverage for the normalized
  launch contract, complete settings fixtures, native per-harness application, Codex selector
  census and roleless defaults, Pi exact identity, Claude mismatch failure, no-paste enforcement,
  and token-free failure/echo evidence. Verification metadata remains pinned until closeout stamps
  the L2 code commit.

- 2026-07-15T20:08+02:00 — 260714-ACPUI-L1 curator: made the 2.1.210 Claude JSONL cohort the
  active fake-transport fixture authority and documented token-free dynamic catalog coverage across
  Claude, Codex, and Pi. Verification metadata remains pinned until closeout stamps the L1 commit.

- 2026-07-14T17:52:13+02:00 — 260713-PHA-L6 curator: added route-level delayed-reply IPC peer-disconnect
  containment and bridge reconciliation evidence.

- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: added route-level Codex completion correlation,
  same-row pending semantics, loud failure cases, replacement-only queue state, and fixture-only pins.

- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the test-route body for structured
  capability negotiation, rolling inbox compatibility, and the deferred R10 boundary.

- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.

- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: added fake protocol, pinned JSONL fixture, and
  credential-safe `/cost` live-smoke coverage for Claude 2.1.207, including failed API-429 semantics.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator: added route coverage for the Codex app-server
  fixture, adapter/protocol fake tests, and credential-safe live smoke. Verification remains pinned
  until closeout stamps the leaf commit.

- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: added governing route coverage for the Pi RPC
  protocol, subprocess, adapter, fixture, and isolated real-smoke regression files. Verification
  metadata remains pinned until closeout stamps the L4 code commit.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: added route-body coverage for the
  bridge conformance suite and its five changed serving regression files.

- 2026-07-12T20:24+02:00 — 260712-PTS-L3 curator: added route coverage for the change-driven
  projection pacing regressions — new `test_change_watcher.py` (roots/filter/pacer/projector/real
  inotify) plus the `test_serving.py` `watch_changes=False` ETag fixture note and the
  `test_dashboard_daemon.py` heartbeat plumbing pins. Verification metadata remains pinned until
  closeout.

- 2026-07-12T20:02+02:00 — 260712-PTS-L2 curator: added route coverage for the shared per-tick
  contract-snapshot regressions in `test_projection_scaling_cs6.py` (one enumeration/parse pass per
  tick, stat-identity cache with ctime hardening, output parity, live-set retention, failure retry).
  Verification metadata remains pinned until closeout.

- 2026-07-12T19:55+02:00 — 260712-PTS-L1 curator: added route coverage for walk-free contract loads
  and the explicit heal sweep (parity, idempotence, dry-run, error tolerance, CLI seam) in
  `test_leaf_ref_resolution.py`. Verification metadata remains pinned until closeout.

- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: added governing route coverage for the new
  inbox-reclamation regression suite and its final PASS delta tests, including event silence and
  corrected persisted removal semantics. Verification metadata remains pinned until closeout.

- 2026-07-12T17:30+02:00 — 260712-TRH-L7: added route coverage for bounded landing observation, no-wait projection, stale rendering, invalid-snapshot containment, and shutdown after observer failure.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator: established governing route coverage for the final candidate.

Recorded the current private preparation/publication ownership from source. Existing verification identity is retained; this entry does not claim tests, certification or acceptance.

## 260915-KS-L17 The Composition Suites, The Registry Rows They Obliged, And Two Re-Scoped Facet Cases

This route gained **two new unit-regression modules and no new governed artifact**:

- `test_knowledge_family_composition.py` — **18 cases**, hermetic over temporary directories and
  in-process APSW databases driven through the real admitted destination. It owns the *write* shape:
  the closed command union and its six record tables, the value-boundary policy refusal, the appended
  generation 5 and `descends_from`, a genuine generation-2 and generation-4 dataset that refuses a
  composition write, the authored edge with **unrepresentable** non-family endpoints, the declared
  unique tuple, the revision-altitude owning route and the explicit ungoverned state, the immutable
  context and its successor, and the one shared cycle rule at both check levels.
- `test_knowledge_family_composition_boundaries.py` — **8 cases**. It owns the *boundary*: the
  shipped selection compared **by value** with composition edges present and absent (two seeds, every
  preserved field equal, table counts confirming the edges are the only difference), the call-site
  derivation that no shipped read path consults the composition table, the declared-policy traversal
  reporting its version and widening nothing else, an unknown/a malformed/a not-permitted policy each
  refused **by name**, a traversal past its declared bound **refused rather than truncated**, every
  pre-existing family revision keeping its sealed `payload_digest`, the R07 escalation artifact's
  recorded subject and effect scope, and the read-only application seam end to end.

**26 collected cases across the two modules**, and one structural fact a reader of the builder's own
narrative would get wrong: the projection's absent-state assertions are driven **inside the seam
case** (`test_the_application_seam_is_read_only_carries_the_operation_and_moves_no_selection`, 8
definitions in that module), not by two separate cases of their own. The case count is what the
collection measures; the case *names* in the leaf's implementation rationale are not a second
population.

**The three registry touch-points a new test module obliges, and which this leaf paid:**

1. a lane row each in `mcp/tests/test-evidence-lanes.toml`, inserted mid-list under
   `unit-regression` — which is **why every later line of that file shifted by two** and other
   routes' citations into it had to move with it;
2. `consumers` rows in `mcp/tests/evidence-lifecycle.toml` — three of them, for
   `knowledge-facet-cases`, `knowledge-generation-cases` and `knowledge-read-scope-cases`, because
   the two modules build their admitted candidate through the facet leaf's helpers and read their
   graphs through the generation and read-scope harnesses rather than through a third fixture of
   their own;
3. the catalogue digest in `mcp/tests/test_dependency_ownership_ast_helpers.py`, **re-pinned
   deliberately** with the reason written beside it.

The counts stay **13 contracts / 54 artifacts**, because this leaf adds **no artifact and no
contract**. The measured digest of `mcp/tests/evidence-lifecycle.toml` on this candidate is
`2505cc7dd6eb52f9ab96bb61b25bf11ed1de50db72371d058524290c419d9eeb` and the constant in the rail
carries exactly that value; **the leaf's own report records a different, stale digest for the same
re-pin, which appears nowhere in the tree** — the file's measured bytes are the authority.

**Two shipped facet assertions were re-scoped upward, not loosened.** `test_knowledge_facets.py`
spelled a *closed list* where the protected property was a *derived* one, twice:

- the command-union case now unions this leaf's published `COMPOSITION_COMMAND_KINDS` and
  `COMPOSITION_WRITABLE_TABLES` instead of restating the members, and asserts
  `len(kinds) == 18 + len(COMPOSITION_COMMAND_KINDS)`. The stronger half is kept exactly:
  `set(_TARGET_CHECKS) == kinds` still fails the moment a command is added without a target check;
- the generation-registry case now asserts
  `[g.user_version for g in GENERATIONS] == list(range(1, len(GENERATIONS) + 1))` and the derived
  schema-name list, instead of `[1, 2, 3, 4]`. Every generation-3-specific assertion in it, including
  `GENERATION_2.fingerprint == PRE_LEAF_GENERATION_2_FINGERPRINT`, is unchanged.

No case was deleted, skipped, deselected, xfailed or weakened, and neither budget moved.

**Populations on this candidate**, measured with the host's required `-o "filterwarnings=ignore"`
override: **unit 1341** against the pinned `"unit_case_budget = 1500"`, **integration 322** against
`"integration_case_budget = 400"`, **combined 1663**. The baseline was 1315 / 322 / 1637, so this
leaf's delta is **+26 unit, +0 integration**, and it **raises no ceiling** and adds no entry to the
budget comment block in `pyproject.toml`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The composition suite's lane row, inserted mid-list under the unit-regression lane. | "mcp/tests/test_knowledge_family_composition.py" | mcp/tests/test-evidence-lanes.toml:90-90 |
| The boundary module's lane row, immediately after it. | "mcp/tests/test_knowledge_family_composition_boundaries.py" | mcp/tests/test-evidence-lanes.toml:91-91 |
| **The facet contract whose consumer list gained both modules.** | "id = \"knowledge-facet-cases\"" | mcp/tests/evidence-lifecycle.toml:55-55 |
| **The read-scope contract whose consumer list gained the boundary module.** | "replacement_contract = \"contract:knowledge-read-scope-cases\"" | mcp/tests/evidence-lifecycle.toml:1402-1402 |
| **The re-pinned catalogue digest, with the reason written beside it and both counts unchanged.** | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:45-45 |
| **The command-union case re-scoped a second time: it now unions this leaf's published constant instead of a literal, and keeps the target-check half exactly.** | "test_the_facet_commands_join_the_closed_union_and_its_dispatch_tables" | mcp/tests/test_knowledge_facets.py:901-901 |
| **The registry case re-scoped to the derived fact the closed list stood in for.** | "test_the_registered_generation_appends_only_and_the_preceding_ones_are_unchanged" | mcp/tests/test_knowledge_facets.py:1045-1045 |
| The unit ceiling this route's suites collect against, cited as the pinned key and value — 2200 since the merge onto the moved super line raised it over the merged line's 2035 collected cases. | "unit_case_budget = 2200" | pyproject.toml:214-214 |
| The integration ceiling, cited as the pinned key and value. | "integration_case_budget = 400" | pyproject.toml:215-215 |

## 260915-KS-L13 The Authored-Effect Suites, The Registry Rows They Obliged, And A Catalogue Pin That Does Not Move

`KS-R13@v1` adds two unit-regression modules for the authored-effect record group — the **change-set**
contract and the **effect-claim** contract — and, unlike the composition leaf before it, it adds **no new
contract and no new artifact**: both suites reach the shipped shared support their neighbours already use,
so the counts stay at **14 contracts / 55 governed artifacts** and only the catalog's *bytes* move.

**The registry touch-points a new test module obliges, measured on this candidate.** A new module needs a
lane row, and a lane member belongs **inside** its lane's own list — which is where the alphabetical
ordering lives — so both rows were inserted mid-file rather than appended, and every absolute line below
them shifted. That is the drift this leaf's own curation carries, and it is inherent to citing an
order-structured registry by line rather than a habit a convention can fix. The two `consumers` additions
are the same shape: a module path belongs inside that artifact's own list, so each insertion moved the
lines below it. Measured here: the lane rows are
`mcp/tests/test_knowledge_change_sets.py` and `mcp/tests/test_knowledge_effect_claims.py`, and the two
consumer lists that grew are the candidate-batch and generation-case shared supports — both **existing**
artifacts whose `consumers` lists gained one row each.

**The catalogue pin moves and the counts do not.** `LIFECYCLE_CATALOG_SHA256` was re-pinned against the
merged catalogue measured on this candidate, while `LIFECYCLE_CONTRACT_COUNT` and
`LIFECYCLE_ARTIFACT_COUNT` are unchanged at 14 and 55 precisely because no contract and no artifact was
added. A reader who saw the digest move and inferred a new artifact would be reading the wrong fact: what
moved is the artifact **records' contents**, not the set.

**The two shipped facet assertions re-scoped again.** A new member of the command union and a new
generation both land on cases that pin a closed set, and the shipped remedy is to re-derive them against
the merged union rather than to loosen them — each keeps its stronger half, and no case was deleted,
skipped or consolidated to make room. The unit and integration ceilings are unchanged (1600 / 400): this
leaf's own case counts stay under them and the merged line does too.

## Update History — 260915-KS-L13
- 2026-09-18T13:27+02:00 — 260915-KS-L13 curator (range-closure pass): **the two `unit_case_budget = 1600` rows on this route were re-read against the merged declaration and given the source they were missing.** Both carried an Anchor and an EMPTY Source cell, and both quoted a value the file no longer declares: `pyproject.toml` now reads `unit_case_budget = 2200` (raised at the merge from the ias line's 2000 over 2035 measured unit cases), so each row's anchor was corrected to `unit_case_budget = 2200`, its wording updated to the merge that raised it, and its Source cell filled with `pyproject.toml:214-214`. The two rows are the L11 facet section's ceiling row and the L17 composition section's ceiling row; neither claim was deleted or softened. No verification stamp advanced: the source is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T10:48+02:00 — 260915-KS-L13 curator (uncommitted change set on `ar/260915-ks-l13`, base `b5a74aee`): **added the L13 section** — the two authored-effect unit-regression modules, the four registry touch-points a new test module obliges (two lane rows inserted mid-list, two `consumers` rows added to **existing** artifacts) and why the drift they cause is inherent, the catalogue digest re-pinned against the merged bytes **with the counts unchanged at 14 / 55** because no artifact and no contract was added, and the re-scoped shipped facet assertions that were re-derived upward rather than loosened. The metadata block above now names this leaf's candidate as what was read; the body was changed substantively and this entry is the history record, not a metadata-only refresh.
- 2026-09-18T06:40+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): recorded the **composition suites and the registry rows they obliged**, because this route governs them. The section states the two new unit-regression modules and their populations (**18 and 8 collected cases, 26 in total**), the write/boundary split each owns, the **three registry touch-points** a new test module obliges (two lane rows inserted mid-list — which is why every later line of that file shifted and other routes' citations into it moved — three `consumers` rows, and a deliberate catalogue digest re-pin) and the counts that stay at **13 / 54** because no artifact and no contract was added. It records the **measured** digest and states that the leaf's own report carries a different, stale value that appears nowhere in the tree, so the file's bytes are the authority. It records the **two shipped facet assertions re-scoped upward rather than loosened**, with the stronger half each kept, and the measured populations on this candidate (**1341 unit / 322 integration / 1663 combined**, delta **+26/+0**, ceilings unmoved). It also records one correction to the builder's narrative: the projection's absent-state assertions are driven inside the boundary module's seam case rather than by separate cases of their own. Verification metadata advances to this leaf's base commit `e963a01c` because the body was re-read against the current source; the code commit does not exist yet and closeout owns that stamp.
