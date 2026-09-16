# mcp/src/agents_remember/serving/eve_runtime_launch.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/eve_runtime_launch.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `c1dbebf883f22710b71d40a66ec92c1ac134918f` |
| lastVerifiedCommitDate | 2026-09-16T13:48:06+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Resolve the AR-owned eve runtime application and compose its one launch environment. The adapter
never shells out to a user-supplied command and never reads ambient credentials: every value that
reaches the runtime is derived here from the adapter's own launch spec, the settings-resolved
selection, and an explicitly named runtime root.

## Code Commentary

### Logic

**Root resolution order is fixed** so a source checkout and an installed wheel work without a second
code path:

1. `AR_EVE_RUNTIME_ROOT` when the operator sets it (the development escape hatch);
2. the runtime application shipped inside this package's own data (`package_data/runtime/eve-agent`),
   materialized to a temporary directory when the package is a zip;
3. the `eve_runtime` directory beside the repository root, for a checkout that has not synced package
   data yet.

A root that does not contain `package.json` and `agent/agent.ts` is refused naming **every path
tried**; it is never silently replaced by a different application.

`stage_runtime_root` gives one epoch its own application directory with the installed dependencies
symlinked, because eve resolves its application root from the process working directory and keeps one
development server per resolved root — two live runtimes of the same authored application collide
without it. Staging is idempotent, which is what lets an epoch restart without rebuilding its tree.

`resolve_runtime_spec` builds the `EveRuntimeLaunch` and carries the **caller's interpreter choice
verbatim** as `node_executable` (`AR_EVE_NODE`). Reading the selector here rather than at spawn is what
makes a bad path fail with the path the operator actually named; the executable search, the
minimum-major check and the refusal that advertises both candidates stay with the transport that
spawns, so the search remains lazy and a deterministic test transport can consume a spec without an
installed interpreter.

`build_runtime_env` composes the child environment from the operator's base plus this adapter's owned
values, and **owned values always win** over an inherited value of the same name, so an ambient
`AR_EVE_MODEL` can never silently redirect a launch the settings selection already fixed. It also
**pops `AR_EVE_RUNTIME_ROOT` and `AR_EVE_NODE` from the child environment**: both are resolved into
the launch object before this point, so leaving them inherited would let a stale ambient value point
the process at a different application than the adapter resolved.

`eve_launch_knobs` is how eve spells its model/effort selection: entirely through the environment,
with empty `argv` and empty owned argv/config options. eve has no argv vocabulary for a model — it is
a compiled application value — so the selection rides the environment the adapter composes.

`resolve_node_executable` tries the newest nvm runtime under `$HOME/.nvm` first, then the first
`node` on `PATH`, and refuses naming every candidate and its version rather than starting eve under an
unsupported runtime.

`runtime_default_model` (255) answers the question a **pre-session** capability read has no launch to
answer: which model does this runtime actually run with? It reads the pinned application's own
`agent/agent.ts` (`AGENT_SOURCE`) and extracts the `?? <literal>` fallback with
`MODEL_FALLBACK_PATTERN`, rather than mirroring the value as a second constant. A runtime whose source
declares no fallback refuses with a message saying a pre-session read cannot name the model — it does
not guess.

`launch_spec_selection` (366) now falls back to `runtime_default_model` when the launch spec carries no
settings-derived `AR_EVE_MODEL`, instead of refusing. The reason is stated in the code: the runtime is
about to compile its authored application, whose own fallback is then the model that really runs, so
reading it keeps the reported catalog and the running process on one value rather than refusing a read
the dashboard needs or advertising a model nothing would use.

### Conventions

- Environment names this adapter owns are the `AR_EVE_*` group plus the three AR binding names;
  `OWNED_ENV_PREFIX` documents that grouping.
- `DEFAULT_RUNTIME_PORT = 0` means "reserve a free loopback port at launch"; `choose_runtime_port`
  binds and closes a socket so a collision fails the launch loudly instead of silently serving on a
  port the adapter cannot address.
- `launch_spec_selection` reads the selection the runner already applied to the launch spec, so the
  launch spec — not ambient process state — is the authority.
- `_checkout_root` walks up for the sibling `eve_runtime` directory rather than counting path levels,
  so moving this module inside the package cannot silently repoint the lookup.

### Invariants And Boundaries

- **This module carries the AR binding; it does not compile or select a capsule.**
  `EveWorkspaceBinding` only transports `AR_WORKSPACE_ROOT`, `AR_BINDING_REF` and
  `AR_CAPSULE_DIGEST`. Where those values come from is the capsule/workspace leaf's scope.
- **`AR_EVE_RUNTIME_ROOT` and `AR_EVE_NODE` are live selectors, not advisory names.** The root is
  honoured at resolution and the interpreter is carried onto the launch; both are then popped from the
  child environment so the process cannot re-resolve itself elsewhere. Documenting them without
  reading them is the defect this rule exists to prevent.
- **The launch carries the interpreter the caller asked for.** A resolved spec's `node_executable` is
  whatever `AR_EVE_NODE` named (or `None` when unset); the search and its refusal happen at spawn, not
  here.
- `EVE_PINNED_VERSION = "0.56.0"` is stated here **for the refusal message only**. The authoritative
  pin is `eve_runtime/package.json`; if the two ever disagree, the package pin wins and this constant
  is the stale one.
- **`MINIMUM_NODE_MAJOR` is no longer declared here: it is imported from the kernel readiness module
  and re-exported.** One floor, two readers — detection and this launch path — so the two cannot
  contradict. A second literal `24` anywhere on this path is a regression against that ownership.
- `package-lock.json` is copied into a staged root when present, so a staged epoch installs from the
  same resolved graph as its source.
- **The runtime root is still an application, not a command — but it now has a curated registry row.**
  eve is a settings-vocabulary row in `kernel/harnesses.py`, detected through its readiness probe; it
  is still not a terminal program, and terminal launch refuses it by name.

### Todos

None known. Packaging the runtime into `package_data/runtime/eve-agent` is the packaging leaf's scope;
resolution order 2 already anticipates the packaged location, and the readiness probe reads it first.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; Node's engines contract and eve's own `engines` field are the external authorities, cited from the runtime package. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The launch spec, identity and workspace binding are AR's existing control-wire types. | `LaunchSpec`; `ControlIdentity` | mcp/src/agents_remember/models/conversations/control_wire.py:58-79; mcp/src/agents_remember/models/conversations/control_wire.py:82-90 |
| The launch knobs are AR's existing capability-port type, which is why eve participates in the same launch-vocabulary contract as the other harnesses. | `LaunchKnobs` | mcp/src/agents_remember/serving/harness_capabilities.py:136-148 |
| The declared pins and the operator-facing environment contract are documented beside the application they govern. | `dependencies`; environment table | eve_runtime/package.json:14-20; eve_runtime/README.md:10-46 |
| The authored application applies the binding this module carries at `session.started`. | `defineDynamic`; `session.started` | eve_runtime/agent/instructions/ar-binding.ts:1-1; eve_runtime/agent/instructions/ar-binding.ts:11-11 |
| The adapter is the only consumer that resolves a spec, hands it to a transport, and verifies the effective selection it produced. | `EveSessionAdapter._resolve_spec`; `_verify_effective_selection` | mcp/src/agents_remember/serving/eve_adapter.py:660-700; mcp/src/agents_remember/serving/eve_adapter.py:892-904 |
| The factory recovers the applied selection by probing a `LaunchSpec` through this module's reader, so the values that reached the child are the ones verified. | `_eve_expected_selection`; `launch_spec_selection` | mcp/src/agents_remember/serving/harness_control_factories.py:105-130; mcp/src/agents_remember/serving/eve_runtime_launch.py:366-393 |
| The node floor is owned by the readiness module and re-exported here, so detection and launch read one number. | `KERNEL_MINIMUM_NODE_MAJOR`; `MINIMUM_NODE_MAJOR` | mcp/src/agents_remember/serving/eve_runtime_launch.py:38-38; mcp/src/agents_remember/serving/eve_runtime_launch.py:48-52; mcp/src/agents_remember/kernel/eve_runtime_readiness.py:55-60 |
| The runtime's own model fallback, read from the authored application rather than mirrored as a constant. | `runtime_default_model`; `AGENT_SOURCE`; `MODEL_FALLBACK_PATTERN` | mcp/src/agents_remember/serving/eve_runtime_launch.py:96-96; mcp/src/agents_remember/serving/eve_runtime_launch.py:99-99; mcp/src/agents_remember/serving/eve_runtime_launch.py:255-276 |
| The capability catalog consumes this fallback so a pre-session read names the model the runtime would really use. | `HarnessCapabilityCatalog` | mcp/src/agents_remember/serving/harness_capability_catalog.py:84-212 |
| The case pinning that the advertised model is the one the runtime would use. | `test_the_advertised_model_is_the_one_the_runtime_would_use` | mcp/tests/test_eve_product_integration.py:985-997 |
| The launch-vocabulary contract holds the new harness without an edit to the parametrized test, and now includes the environment carrier eve uses. | `_knob_values`; `test_every_harness_carries_a_clean_selection_into_its_own_launch_vocabulary` | mcp/tests/test_harness_launch.py:173-185; mcp/tests/test_harness_launch.py:188-196 |
| The OS-level start-failure seed is an operator naming a nonexistent `AR_EVE_NODE`, which only fails because this module reads the selector as given. | `START_FAILURES`; `failureType` | mcp/tests/live_eve_native_fixture.py:83-89; mcp/tests/live_eve_native_fixture.py:1085-1085 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pinned `eve` release and its Node `>=24` engine requirement come from the published package, not from a sibling Agents Remember repository. | `engines`; exact dependency pins | eve_runtime/package.json:7-8; eve_runtime/package.json:15-20; eve_runtime/README.md:3-8 |

## Update History
- 2026-09-16T11:42:38+00:00: Generated citation repair: `LaunchKnobs` repointed to mcp/src/agents_remember/serving/harness_capabilities.py:136-148. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: **the node floor moved to one owner, and a
  pre-session read can now name the model.** `MINIMUM_NODE_MAJOR` is no longer a second literal here:
  it is imported from `kernel/eve_runtime_readiness.py` as `KERNEL_MINIMUM_NODE_MAJOR` and re-exported,
  because detection has to answer the same question and two numbers could contradict. Added
  `runtime_default_model`, which reads the pinned application's own `agent/agent.ts` fallback through
  `MODEL_FALLBACK_PATTERN` rather than mirroring the value as a constant, and `launch_spec_selection`
  now uses it when no settings-derived `AR_EVE_MODEL` reached the launch — so the catalog the dashboard
  reads and the process that actually runs agree on one model instead of the read being refused or a
  value being invented. Corrected the stale Todo and the boundary that said eve "deliberately has no
  row in the developer-curated terminal harness set": it has one now, and is still not a terminal
  program. Verification metadata moves to the leaf's synced base `ff97072c`; the candidate is
  deliberately uncommitted, so the governed closeout stamps the real code commit and no hash or
  fingerprint was invented here.

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): the two launch selectors became
  **live**. `resolve_runtime_spec` now carries the caller's interpreter choice verbatim onto
  `EveRuntimeLaunch.node_executable` (`AR_EVE_NODE`), so a bad path fails at spawn naming the path it
  was given; `build_runtime_env` now pops `AR_EVE_RUNTIME_ROOT` and `AR_EVE_NODE` from the child
  environment so a staged epoch cannot re-resolve itself. This **supersedes** the previous invariant
  that "a resolved `EveRuntimeSpec` carries `node_executable = None` until a real process starts":
  until this round both names were documented but inert, which is why the leaf's OS-level start-failure
  seed could not fail. Body, that superseded invariant, and all three citation tables were updated;
  tables rewritten into the `Finding | Anchor | Source` shape. Verification metadata moves to the
  leaf's current base `e9300687`; the candidate remains uncommitted, so the governed closeout stamps
  the real code commit and no hash was invented here.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: created this card for a file added by the native
  eve session-adapter change set. Records the fixed three-step root resolution, the owned-env-wins
  rule, the per-epoch staging requirement, the environment-only launch vocabulary, and the explicit
  boundary that this module carries a capsule binding without compiling or selecting one.
  Verification metadata is pinned to the leaf's base commit `67b21aeb` because the candidate is
  deliberately uncommitted — the governed closeout stamps the real code commit, and no hash or
  fingerprint was invented here.
