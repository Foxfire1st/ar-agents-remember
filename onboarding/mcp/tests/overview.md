# mcp/tests

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/tests/` |
| doc_type | `route-local-overview` |
| lastUpdated            | 2026-09-17T10:20:31+00:00 |
| lastVerifiedCommitHash | `a29a20c6eefea424a7e0321a54fcda2ed1b35098` |
| lastVerifiedCommitDate | 2026-09-17T14:23:47+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l7-ar` uncommitted source; base `23cc7a7218b96da5147146f9796557bedfcf1d11` |
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
| The refusal before any host effect, the mode gate, the byte-identical legacy payload, the single-carrier bound and the site enumeration. | `test_an_uncapsulable_role_refuses_by_name_before_any_host_effect`; `test_the_mode_gate_names_capsule_legacy_and_refused_for_every_seat_class`; `test_the_legacy_launch_payload_is_byte_identical_to_the_pre_capsule_payload`; `test_the_delivered_payload_carries_the_capsule_once_and_no_task_context`; `test_every_production_launch_request_site_is_wired_or_declares_its_legacy_chain` | mcp/tests/test_capsule_launch_wiring.py:577-607; mcp/tests/test_capsule_launch_wiring.py:615-657; mcp/tests/test_capsule_launch_wiring.py:659-710; mcp/tests/test_capsule_launch_wiring.py:712-759; mcp/tests/test_capsule_launch_wiring.py:761-801 |
| The declared legacy exclusion, the free agent's admission, and the two defect pins. | `test_the_declared_legacy_reopen_names_why_it_cannot_carry_a_capsule`; `test_the_free_agent_admission_names_its_absent_task_plane`; `test_the_free_agent_capsule_identity_moves_with_the_seat`; `test_the_registered_capsule_operation_resolves_a_repository_through_its_schema`; `test_a_refused_stage_refuses_again_in_the_same_process` | mcp/tests/test_capsule_launch_wiring.py:803-814; mcp/tests/test_capsule_launch_wiring.py:919-944; mcp/tests/test_capsule_launch_wiring.py:945-968; mcp/tests/test_capsule_launch_wiring.py:975-1022; mcp/tests/test_capsule_launch_wiring.py:1028-1059 |
| The production-chain evidence the module's in-process cases complement. | `L15 FIX ROUND 1 — E8: THE PRODUCTION CHAIN` | notes/reports/260915-CAPS-L15-evidence/E8-fix-r1-production-chain.txt:1-41 |

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
| The fixture world and the synthetic corpus every hermetic case is built from. | `World`; `_synthetic_corpus` | mcp/tests/test_capsule_serving.py:308-308; mcp/tests/test_capsule_serving.py:419-419 |
| The admission guarantees: no role acquisition by string, no caller-selected source, no write to the read tree. | `test_a_caller_changing_the_role_string_cannot_acquire_another_role`; `test_the_manifest_decides_the_source_set_not_the_caller`; `test_the_capsule_operation_writes_nothing_to_the_tree_it_reads` | mcp/tests/test_capsule_serving.py:639-639; mcp/tests/test_capsule_serving.py:651-651; mcp/tests/test_capsule_serving.py:690-690 |
| The guards the repairs pinned, each driven directly by its own case. | `test_a_catalog_record_that_escapes_its_skill_directory_is_refused`; `test_the_index_reader_refuses_while_a_skill_cannot_be_served`; `test_the_extension_declaration_is_installed_once_per_server`; `test_a_nested_skill_is_published_flat_like_any_other` | mcp/tests/test_capsule_serving.py:1321-1321; mcp/tests/test_capsule_serving.py:1348-1348; mcp/tests/test_capsule_serving.py:1389-1389; mcp/tests/test_capsule_serving.py:1489-1489 |
| The SEP entry contract, asserted separately from this server's own index shape. | `test_every_sep_2640_entry_is_complete_and_carries_verbatim_frontmatter`; `test_this_servers_own_index_resource_keeps_the_agent_skills_discovery_shape` | mcp/tests/test_capsule_serving.py:1008-1008; mcp/tests/test_capsule_serving.py:1040-1040 |
| The two independent-SDK-client exchanges, including both extension methods and the `-32602` refusal. | `test_a_real_client_and_server_exchange_over_the_installed_sdk`; `test_the_server_process_never_serves_a_file_outside_a_skill_directory` | mcp/tests/test_capsule_serving.py:1195-1195; mcp/tests/test_capsule_serving.py:1268-1268 |
| The case that keeps the seeded-mutation evidence honest. | `test_the_mutation_harness_can_actually_fail` | mcp/tests/test_capsule_serving.py:1301-1301 |
| The lane row that selects this module into the unit population. | "mcp/tests/test_capsule_serving.py" | mcp/tests/test-evidence-lanes.toml:19-19 |

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
| Candidate and protected-ref safety | `test_git_command.py`, `test_integration_branch_authority.py` | Real Git identity, private commits, hooks and race preservation. The former `test_integration_ref_transaction.py` was deleted with the removed mid-crash ref-recovery capability. |
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
| Producer census and the one renderer | `test_memory_attribution_producers.py` | Five memory-content producers and zero untrailered, measured from source: the trailer key identifier and its interpolation appear in exactly one production module, no production module spells the trailer as a quoted literal, each of the five producers reaches a shared renderer entry, and a hostile multi-paragraph caller body survives byte for byte with the trailer appended as its own final block. The two non-closeout producers are driven end to end through the public `memory_carryover_apply` and `memory_baseline_adopt`. Source census plus real-repository cases. **Superseding the note this row used to carry: the module's `unit-regression` lane row now exists** (`mcp/tests/test-evidence-lanes.toml:69`, added by the commit that landed L4), so the manifest loads. |
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
the dated `## Update History

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
| The launch-binding fixture that makes the adapter suite's launches verifiable. | `fixture_launch_binding` | mcp/tests/eve_adapter_test_support.py:335-364 |
| The trace's effective-prompt key, which the live capsule scenarios assert against. | `FixturePlan.trace` | mcp/tests/eve_fixture_model.py:63-88 |
| The live end-to-end capsule scenarios, which are the whole-seam proof rather than a unit claim. | `_scenario_capsule_binding`; `_scenario_capsule_execution` | mcp/tests/live_eve_native_fixture.py:1758-1813; mcp/tests/live_eve_native_fixture.py:1680-1757 |
| The lifecycle catalog registration for the shared support module, with its four derived consumers. | `path = "mcp/tests/eve_capsule_test_support.py"` row | mcp/tests/evidence-lifecycle.toml:714-724 |

## Repo-Internal References

These current source and policy ranges establish the development/certification distinction and the
existing memory preparation surfaces. A citation is source evidence, not a recorded test execution.

| Finding | Anchor | Source |
| --- | --- | --- |
| Development commands, budgets, diagnostic metrics and isolation. | `# Python test policy and commands` | docs/design/python-pytest-bootstrap.md:1-50 |
| Certifying publication and accepting consumers. | `# Python Test Evidence Authority` | docs/design/python-test-evidence.md:1-65 |
| Exact contract scope, full check and curator worklist publication. | `_resolve_execution`; `_execute_memory_quality`; `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality/controller.py:308-328; mcp/src/agents_remember/application/memory_quality/controller.py:331-383; mcp/src/agents_remember/application/memory_quality/controller.py:413-550 |
| Interactive catalog names missing authority without eligibility. | `_attach_final_full_catalog` | mcp/src/agents_remember/application/memory_quality/controller.py:553-589 |
| Final memory adapter requires the selected four-code-terminal prefix. | `PreparedMemoryCertificationAdapter` | mcp/src/agents_remember/application/prepared_certification.py:749-813 |
| Finalization consumes original selected fifth-certificate inputs. | `PreparedCloseoutContinuation` | mcp/src/agents_remember/worktrees/integration/closeout/preparation/continuation.py:20-68 |
| The citation index's exclusion register, its ruled caps and its reported-skip behaviour, defended case by case. | `TheExclusionRegisterIsHonouredFromEachSourceIndependently`; `TheRuledCapsSkipAndReportRatherThanRefuse`; `TheQualitySurfaceCannotBeBricked`; `TheRegisteredCitationSurfaceCarriesTheCallerExcludes`; `TheCapsThatStayAsTheyWere` | mcp/tests/test_citation_index_resilience.py:207-415; mcp/tests/test_citation_index_resilience.py:418-557; mcp/tests/test_citation_index_resilience.py:560-665; mcp/tests/test_citation_index_resilience.py:668-707; mcp/tests/test_citation_index_resilience.py:710-720 |
| The divergence between the register's re-inclusion rule and Git's, measured on both sides. | `test_the_register_admits_a_negated_file_under_an_excluded_directory_where_git_does_not` | mcp/tests/test_citation_index_resilience.py:334-374 |
| The consumer of record for the three new `scripts/e2e_harness` governed artifacts, and the fixture/scenario shape it pins. | `FreshUserFixtureShapeTests`; `FreshUserScenarioContractTests` | mcp/tests/test_fresh_user_harness.py:110-186; mcp/tests/test_fresh_user_harness.py:189-235 |
| The lane rows that admit both L14 modules to the `unit-regression` lane. | "mcp/tests/test_citation_index_resilience.py"; "mcp/tests/test_fresh_user_harness.py" | mcp/tests/test-evidence-lanes.toml:27-27; mcp/tests/test-evidence-lanes.toml:62-62 |
| The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. | `path = "scripts/e2e_harness/fresh_user_fixture.py"`; `path = "scripts/e2e_harness/fresh_user_scenario.py"`; `path = "scripts/e2e_harness/run_fresh_user.py"` | mcp/tests/evidence-lifecycle.toml:1266-1285; mcp/tests/evidence-lifecycle.toml:1286-1304; mcp/tests/evidence-lifecycle.toml:1305-1320 |
| The live public-surface inventory contract for the advertised MCP tool tuple. | `PublicSurfaceInventoryTests` | mcp/tests/test_tools.py:220-341 |
| The advertised roster the inventory comparison uses, in its new zero-import `models` leaf. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-86 |
| The worktree surface's declared next move and the membership validator this route's new module pins. | "# The next-move triple, declared here so the worktree surface's guidance is part of"; "def _require_registered_public_next_tool" | mcp/src/agents_remember/models/worktree.py:322-329; mcp/src/agents_remember/models/worktree.py:355-363 |
| The L32 module itself: archive-ready reachability for both cleanup verbs, the declarations, and the validator in both directions. | `test_archive_ready_status_names_the_accepted_cleanup_operation`; `test_next_tool_must_name_a_registered_public_tool` | mcp/tests/test_worktree_status_terminal_next_tool.py:175-219; mcp/tests/test_worktree_status_terminal_next_tool.py:231-244 |
| The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane. | "mcp/tests/test_memory_backfill.py" | mcp/tests/test-evidence-lanes.toml:70-70 |
| The contract-scoped activation record: one record per series contract, keyed by the contract fingerprint rather than a source pair. | "def contract_fingerprint("; "def activation_path(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-142 |
| The L36 cross-master forcing module: both masters stay ready, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks nobody, a conflicting or stale publication is refused at the pair, and a master that reconciles with a landed sibling completes through ordinary closeout and final integration. | `test_two_unfinished_masters_share_one_source_pair_and_both_stay_ready`; `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible`; `test_a_conflicting_publication_cannot_overwrite_master_b`; `test_master_a_resumes_reconciles_and_completes_after_master_b_landed`; `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters`; `test_a_dependent_master_still_waits_for_its_unfinished_predecessor` | mcp/tests/test_cross_master_concurrency.py:131-162; mcp/tests/test_cross_master_concurrency.py:409-456; mcp/tests/test_cross_master_concurrency.py:473-507; mcp/tests/test_cross_master_concurrency.py:509-568; mcp/tests/test_cross_master_concurrency.py:754-822; mcp/tests/test_cross_master_concurrency.py:722-750 |
| The L36 lane registration the fail-closed manifest requires. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:153-153 |
| The L37 stop boundary proof: the public pause, the measured world, the ten independently-failing cases and the four refusal shapes. Its never-selected case asserts the already-vacant success rather than a refusal, and the two L38 cases added after it pin the unreadable record and the vacant foreign record. | `PauseStopsAnAtomicMasterTests`; `_world`; `test_pausing_a_master_moves_no_ref_and_creates_no_commit`; `test_a_paused_master_hands_the_turn_back_with_no_next_call`; `test_pausing_a_master_that_was_never_selected_succeeds_and_writes_nothing`; `test_an_unreadable_record_is_refused_not_reported_stopped`; `test_a_record_naming_another_master_is_refused_not_released` | mcp/tests/test_pause_stop_only_end_to_end.py:86-556; mcp/tests/test_pause_stop_only_end_to_end.py:150-168; mcp/tests/test_pause_stop_only_end_to_end.py:203-234; mcp/tests/test_pause_stop_only_end_to_end.py:236-263; mcp/tests/test_pause_stop_only_end_to_end.py:265-317; mcp/tests/test_pause_stop_only_end_to_end.py:445-471; mcp/tests/test_pause_stop_only_end_to_end.py:473-526 |
| The L37 structural half: the pause's import closure is disjoint from every publication module. | `PUBLICATION_MODULES`; `test_the_pause_cannot_reach_any_publication_module` | mcp/tests/test_pause_is_not_publication.py:37-52; mcp/tests/test_pause_is_not_publication.py:165-202 |
| The L37 lane registrations the fail-closed manifest requires, one per new module (the pause suite's row at `:162` is unaffected by the later insertions; the AST-only guard's row moved `:193` → `:194` → `:195`). | "mcp/tests/test_pause_stop_only_end_to_end.py"; "mcp/tests/test_pause_is_not_publication.py" | mcp/tests/test-evidence-lanes.toml:170-170; mcp/tests/test-evidence-lanes.toml:205-205 |
| The ordered lifecycle playthrough that is the regression proof for the deleted atomic-series child-admission seal: master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf commanded after the landing still starts. | `LifecyclePlaythroughTests`; `test_the_lifecycle_plays_through_from_an_unstarted_master_to_a_resumed_one` | mcp/tests/test_lifecycle_playthrough_end_to_end.py:62-173; mcp/tests/test_lifecycle_playthrough_end_to_end.py:117-173 |
| The lane registration the fail-closed manifest requires for that module. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:164-164 |
| The L4 census module's lane row, which closed the gap the L4 route section recorded. | "mcp/tests/test_memory_attribution_producers.py" | mcp/tests/test-evidence-lanes.toml:69-69 |
| The L5 binding module's lane registration, added by the same change set that created it. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:161-161 |
| The L23 registration-order proof: the observed chain with the terminated-row read carrying its own batch-commit state, the partial-proof singleton, the raising registrar that stops the pass, the restart that re-registers and loses nothing, and the fast-path exclusion measured in both directions. | `test_due_sweep_registers_committed_terminated_rows_before_compaction`; `test_partial_registration_compacts_only_the_proven_rows`; `test_registration_failure_prevents_compaction_and_leaves_rows_retryable`; `test_restart_after_registration_before_compaction_reregisters_and_loses_nothing`; `test_starting_fast_path_neither_registers_nor_compacts_while_the_due_sweep_does` | mcp/tests/test_terminal_liveness_registration_order.py:154-246; mcp/tests/test_terminal_liveness_registration_order.py:248-278; mcp/tests/test_terminal_liveness_registration_order.py:280-310; mcp/tests/test_terminal_liveness_registration_order.py:312-358; mcp/tests/test_terminal_liveness_registration_order.py:360-403 |
| The L23 lane registration the fail-closed manifest requires, inserted between two alphabetically adjacent rows so no other entry moved. | "mcp/tests/test_terminal_liveness_registration_order.py" | mcp/tests/test-evidence-lanes.toml:123-123 |
| The L27 pane-authority proof, its fixture import from the sibling sweeper suite, and the lane registration the fail-closed manifest requires. | `PaneDiagnosticAuthorityTests`; `_PANE_AUTHORITY_FIELDS`; `_pane_authority_offenders` | mcp/tests/test_terminal_liveness_pane_authority.py:243-598; mcp/tests/test_terminal_liveness_pane_authority.py:56-69; mcp/tests/test_terminal_liveness_pane_authority.py:233-240; mcp/tests/test-evidence-lanes.toml:188-188 |
| The shared fixtures the L27 module imports instead of rebuilding. | `_Clock`; `_FakeHost`; `_entry`; `_snapshot`; `_ready_snapshot` | mcp/tests/test_terminal_liveness.py:44-104 |
| **260913-LCA-L8:** the new module's lane registration, added by the same change set that created it — integration, because it drives the public landing, integration and finalization routes over real temporary repositories and worktrees. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/test-evidence-lanes.toml:186-186 |
| **260913-LCA-L8:** the L6 shape finalizes on the first call, a real permission failure blocks with its own reason and refuses identically on retry, and the two invariant owners are driven directly. | `test_a_torn_down_provider_runtime_finalizes_on_the_first_call`; `test_a_provider_runtime_that_cannot_be_torn_down_blocks_with_its_own_reason`; `test_a_reasonless_provider_result_is_named_instead_of_becoming_a_null_reason`; `test_an_unnameable_blocker_reason_is_refused_at_its_own_source` | mcp/tests/test_terminal_blocker_reasons.py:116-161; mcp/tests/test_terminal_blocker_reasons.py:164-220; mcp/tests/test_terminal_blocker_reasons.py:223-243; mcp/tests/test_terminal_blocker_reasons.py:246-259 |
| **260913-LCA-L8:** the only construction path for a terminal blockage, and the operator-language answer for a reasonless or malformed result item. | `_blocker`; `_blocked_reason` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:639-655; mcp/src/agents_remember/worktrees/modules/terminal_validation.py:624-636 |
| **260913-LCA-L8:** the producer whose result could answer `removed: False` with no reason, now naming every non-removal. | `remove_tree` | mcp/src/agents_remember/application/provider_runtime.py:289-326 |
| **260913-LCA-L8:** the nine exact-consumer rows the new module's change set adds to the evidence registry. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/tests/evidence-lifecycle.toml:304-304; mcp/tests/evidence-lifecycle.toml:379-379; mcp/tests/evidence-lifecycle.toml:423-423; mcp/tests/evidence-lifecycle.toml:553-553; mcp/tests/evidence-lifecycle.toml:592-592; mcp/tests/evidence-lifecycle.toml:631-631; mcp/tests/evidence-lifecycle.toml:943-943; mcp/tests/evidence-lifecycle.toml:1000-1000; mcp/tests/evidence-lifecycle.toml:1026-1026 |
| **260913-LCA-L8:** the declaration that gives the new module ownership of the ambient-role runner for targeted selection. | "mcp/tests/test_terminal_blocker_reasons.py" | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:82-82 |
| The removed case's scenario, now refused by design: the guard that makes a task root with no master document unbindable. | `_require_bindable_leaf_authoring` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:619-649 |
| The refusal the two corrected closeout fixtures had to satisfy. | `require_current_leaf_enclosure_binding` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:205-256 |
| **The mid-flight reporting boundary:** a completed pass beside a reconciling selection is not this call's success, and a refusal left beside one leads with the mid-flight state. | `ReconcilingResultTests`; `test_a_completed_pass_beside_a_mid_flight_selection_is_not_success`; `test_a_refusal_that_left_a_record_mid_flight_leads_with_that_state`; `_reconciling_result` | mcp/tests/test_atomic_series_activation.py:231-297; mcp/tests/test_atomic_series_activation.py:255-274; mcp/tests/test_atomic_series_activation.py:276-297; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:280-294 |
| The rewritten contract-scoped activation forcing suite and its shared-source-pair fixture. | `class ActivationFixture`; `test_contracts_sharing_one_source_pair_hold_independent_selection`; `test_another_contracts_record_can_never_be_adopted` | mcp/tests/test_atomic_series_activation.py:63-111; mcp/tests/test_atomic_series_activation.py:122-145; mcp/tests/test_atomic_series_activation.py:179-214 |
| The registered admission refusal now addresses only the addressed contract's own state. | `test_registered_sync_refusal_addresses_only_this_contracts_own_state` | mcp/tests/test_activation_admission_registered.py:178-221 |
| The sync fixture's official-memory mapping, which both the fast-forward case and the retained-conflict case drive. | `map_official_memory` | mcp/tests/test_worktree_sync.py:107-107 |

Current working-candidate evidence for this route:

| Finding | Anchor | Source |
| --- | --- | --- |
| Public closeout exercises the actual pair, attribution and cache-independent delivery. | `test_public_closeout_commits_code_and_memory_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:211-318 |
| Cache damage cannot change the accepted integration pair or block ref publication. | `test_cache_damage_cannot_change_the_accepted_pair_or_block_its_ref_move` | mcp/tests/test_integration_branch_authority.py:172-213 |
| The migration acceptance proof reads only committed trailers. | `test_the_trailers_alone_preserve_every_pairing_the_ledger_file_recorded` | mcp/tests/test_memory_backfill.py:467-550 |

## Docs And Cross-Repo References

No Domain Documentation entries are configured in the resolved memory root. Current local policy and source owners are cited above; no live external system or sibling repository is used to grant authority.

## Update History
- 2026-09-17T14:15+02:00 — 260915-CAPS-L19 curator: **Field-name warrant corrected — `ready-for-closeout` read as *never* a value of the combined `checklistStatus`.** That absolute sentence was written by 260915-CAPS-L10's curator as the warrant for this card's `D35` correction, and `CAPS-R19` (`260915-CAPS-L19`) measures it **literally false** (`application/memory_quality/controller.py:685-687` leaves the combined field at its incoming `ready-for-closeout` value on the success path, with `closeoutReady=true`). The card now states the three-path model instead: the raw `qualityChecklistStatus` is the repair loop's gate; the combined `checklistStatus` is rewritten to `coherence-required` **only when the coherence record is then missing or stale**; and `closeoutReady` becomes true only once that validation passes. Corrected under `CAPS-R19`'s revision note (2026-09-17T13:55), which is the authority for this change. The field-name correction itself stands and attribution is complementary — `260915-CAPS-L10` corrected the onboarding cards, `CAPS-R19` corrected the shipped sources (the five loop-gate carriers, their nine generated copies, the guard registry's docstring) and brought `docs/reference/mcp-tools.md` into the loop-gate census and the guard's `LOOP_GATE_DOCUMENTS`. The earlier entries below are left exactly as written: they record what L10 did, and this entry is the correction of their warrant. No verification stamp advanced — the candidate is uncommitted and the governed closeout owns the real commits.
- 2026-09-17T13:45+02:00 — 260915-CAPS-L10 curator: **corrected a landed defect (`D35`)** in the CAPS-L18 section — `ready-for-closeout` is never a value of the combined `checklistStatus`; the curator repair loop's gate is the **raw** `qualityChecklistStatus`, the combined field then reports `coherence-required`, and `closeoutReady` follows validation (`application/memory_quality/controller.py:664,671,678,687`). **No test-surface change:** this leaf's code delta is zero, it adds no module and touches no lane row, so this route's population, its budgets and its `D9` residual are unchanged (`D9` remains L11's six historical modules). Verification metadata is left alone: the candidate is uncommitted and the governed closeout stamps the real code commit.
- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: this route gained **one module** —
  `test_capsule_experiment_install.py`, 19 cases — plus two rows in `test_sync_runtime.py`. The
  section above records what the population protects, that the module is not a seventh `D9` row,
  and that its two `evidence-lifecycle.toml` consumer rows are this leaf's whole catalog delta.
  Verification metadata is left at this leaf's synced base `933b011b`; the candidate is
  deliberately uncommitted.

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: the complete-curation doctrine reaches this route. The canonical sources on this route now state that the full `memory_quality_check` operation is part of every leaf's curation, that a subset never stands in for it, and that closeout and integration carry the completed result as a prerequisite while invoking nothing. Body updated as above; no verification stamp advanced because the sources are uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T11:50+02:00 — 260915-CAPS-L14 curator: this route gained **two modules** and the reference rows and lane/catalog citations that go with them. `test_citation_index_resilience.py` defends the citation index's shared exclusion register per source, the ruled caps' skip-and-report behaviour, and the quality surface's reported states — with the register's deliberate divergence from Git measured on both sides; `test_fresh_user_harness.py` is the **consumer of record** for the three new `scripts/e2e_harness` governed artifacts and pins the fixture shape and the scenario contract (a step that cannot run is `blocked` by name, never `completed`). Added the corresponding rows, the two `unit-regression` lane rows, and the three `[[artifact]]` rows the leaf registers. **Repaired two stale claims on this route**: the final memory adapter citation still pointed at `worktrees/integration/closeout/prepared_certification.py:721-785`, a path that no longer exists — the adapter moved to the application rank in `806649b9`, so the row now reads `application/prepared_certification.py:749-813`. Verification metadata is left at this leaf's synced base `0346da9c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code commit.

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

- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`, base
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


- 2026-09-15T15:02+02:00 — 260831-LOCR-L18 curator (uncommitted test change set on `ar/260831-locr-l18`,
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

- 2026-09-15T14:10+02:00 — 260831-LOCR-L11 curator (uncommitted test-only change set on
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

- 2026-09-15T13:36+02:00 — 260831-LOCR-L27 curator (uncommitted change set on `ar/260831-locr-l27`,
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

- 2026-09-15T13:20+02:00 — 260831-LOCR-L23 curator (uncommitted change set on `ar/260831-locr-l23`,
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
- 2026-09-15T13:15+02:00 — 260831-LOCR-L10 curator: recorded the route's new state-signal crash/restart recovery executor (`test_state_signal_restart_recovery.py`, unit-regression row `:101`) — a route-table row plus a section carrying the durable order it forces, the seven cases, the non-vacuity witness, and the review verdict's coverage limit that the fence's reachable route is the boundary drain rather than the generic finder. Route purpose, lane membership accounting and every other module's coverage claim are unchanged by this leaf.
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

- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: **route meaning changed**, so this overview gained a
  section rather than a no-impact entry. Added the L5 test population — `test_codex_capsule_delivery.py`
  at **28 collected cases and no `integration` marker**, registered under **`provider-conformance`** at
  entry row 216 — plus the two expiry fixtures it reads (`codex_app_server_instruction_channels.json`
  and `codex_app_server_model_page.json`), naming the `turn/start` instruction-field absence the
  lifetime design rests on and why a captured `model/list` page replaced hand-written drafts. Recorded
  the module's two deliberate doublings (transport, transient discoverer) and the live case's
  skip-not-pass guard. Verification metadata stays pinned to the last committed source (`c1dbebf8`).

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

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: **route body updated** for the task-context projection's coverage module. Added § 260915-CAPS-L3 Task-Context Projection Coverage: the new module and its 9 collected cases, the anti-vacuity rule its docstring states as contract, the three cases that carry more weight than their size (the structural import-surface walk, the byte-identical non-mutation case, and the two-way compiler-seam case), the remaining six properties, the fixture-topology trap that took three rounds to mirror (`CAPS-L3-EV5`–`EV7`, chiefly that an internal memory root silently wins over an external coordination hint), the task-local `M01`–`M20` falsifiability probe and its self-caught vacuous seed (`CAPS-L3-EV10`), and the pre-existing pytest-unresolvable pyright condition. **Also recorded a scoped blocker for the owning seat**: this module has no evidence-lane row, and `load_lane_manifest` is fail-closed, so the manifest does not load as the candidate stands; the same gap exists for the three modules from `CAPS-R01@v1`/`CAPS-R02@v1`, making the correct repair a four-row change. That finding is derived from the loader's source, not executed — this seat has Python 3.10 and the repository requires `>=3.13,<3.14`. Verification metadata remains closeout-owned: the source is uncommitted, so no stamp was advanced and no commit hash was invented.
- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): **route body updated** for the native eve adapter's test population. Added § 260915-CAPS-L6 Native eve Adapter Test Population, which states the distinction this route now depends on: two of the five new modules are pytest-collected suites and three are support or explicit-run scripts, so "the suite protects this scenario" is proved by collection for the former and by a `--report-dir` artifact for the live fixture. Also records the A2 strengthening (the production client driven through a mock transport, the bounded replay window, the request-shaped cancel observation) and the `_knob_values` env carrier that holds the launch-vocabulary contract at four harnesses. Verification metadata remains closeout-owned: the source is uncommitted, so no stamp was advanced and no commit hash was invented.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **route body updated** for the lifecycle-corpus consolidation. Added § 260915-CAPS-L1 Role-Instruction Corpus Contract, which places the new shipped module `test_role_instruction_corpus.py` in this route and states the properties it protects (nine-role registry, the six-section readable order, the frozen eight-operation vocabulary, a prose-free manifest, every cited relative path resolving, a missing manifest source reported rather than accepted, and the `SANCTIONED_SIBLING_REFERENCES` independence rule). A new card was created for the module in this route. Verification metadata remains closeout-owned: the source is uncommitted, so no stamp was advanced and no commit hash was invented.

- 2026-09-15 — Preserved the following dated pre-takeover review notes from the parent working tree. They describe that earlier candidate; current behavior is documented above. Exact original files and patches are retained in the master cutover report.

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

- 2026-09-15 — LCA L9 terminal-cache retirement and abandon-preview correction: refreshed this route with the shared cache-removal owner and its regression coverage.


- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Rewrote current test-route expectations for cache independence and preserved old scenario histories as historical; removed stale assertion citations. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.


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
- 2026-09-11T22:39:01+00:00: Generated citation repair: `PreparedMemoryCertificationAdapter` repointed to mcp/src/agents_remember/worktrees/integration/closeout/prepared_certification.py:721-785. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
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
- 2026-09-09T12:22:46+00:00: Generated citation repair: `PreparedMemoryCertificationAdapter` repointed to mcp/src/agents_remember/memory_quality/prepared_certification.py:721-785. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
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

Recorded the current private preparation/publication ownership from source. Existing verification identity is retained; this entry does not claim tests, certification or acceptance.

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


- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec: route coverage adds three status-wait test cards (outcomes, registration, store) and refreshes dispositions/conformance/evidence-lane cards; route index regenerated.


- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass (route impact): recorded the six standalone CCR-R13 diagnostic suites (four unit-regression, two integration) and their `test-evidence-lanes.toml` lane registrations. File-level detail lives in the new test cards. Verification stamp is the full leaf code commit `4ba18bb23ba90e201bb37341d61c0efc64161fcf` (tree `631145bf3e0d5899b1dcbccf8c0d4a8257821f0d`).


- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5 memory pass (route impact): added the CCR-L16
  section for the six durable gate-and-rail telemetry suites
  (`test_telemetry_models.py`, `test_telemetry_projection.py`, `test_telemetry_projection_edges.py`,
  `test_telemetry_store.py`, `test_telemetry_validation.py`, `test_telemetry_validation_edges.py`)
  registered in the `unit-regression` lane. Verification metadata stays pinned until closeout
  stamps the leaf code commit.


- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: recorded the new generation-coherent projection suite and the refreshed lifecycle/test suites. File-level detail in the mcp/tests sidecars.


- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass (route impact): added the CCR-L12 section for the host-authority suite, the five-gate/authority rework of the clean-quality group, and the Gate-5-order closeout regressions. Verification metadata stays pinned until closeout stamps the leaf code commit.


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
