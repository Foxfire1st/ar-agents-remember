# mcp/src/agents_remember/serving/eve_runtime_launch.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/eve_runtime_launch.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:15+02:00 |
| lastVerifiedCommitHash | `609756111eb3c239d0563d8631bfd564645bc9d1` |
| lastVerifiedCommitDate | 2026-09-16T10:25:13+02:00|
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
- `EVE_PINNED_VERSION = "0.56.0"` and `MINIMUM_NODE_MAJOR = 24` are stated here **for the refusal
  message only**. The authoritative pins are `eve_runtime/package.json`; if they ever disagree, the
  package pins win and this constant is the stale one.
- `package-lock.json` is copied into a staged root when present, so a staged epoch installs from the
  same resolved graph as its source.
- The runtime root is an **application**, not a command, which is why the adapter registers through
  the protocol factory and deliberately has no row in the developer-curated terminal harness set.

### Todos

None known. Packaging the runtime into `package_data/runtime/eve-agent` and adding an `eve` row to
the curated harness registry are the packaging leaf's scope; resolution order 2 already anticipates
the packaged location.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; Node's engines contract and eve's own `engines` field are the external authorities, cited from the runtime package. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The launch spec, identity and workspace binding are AR's existing control-wire types. | `LaunchSpec`; `ControlIdentity` | mcp/src/agents_remember/models/conversations/control_wire.py:1-200 |
| The launch knobs are AR's existing capability-port type, which is why eve participates in the same launch-vocabulary contract as the other harnesses. | `LaunchKnobs` | mcp/src/agents_remember/serving/harness_capabilities.py:1-120 |
| The declared pins and the operator-facing environment contract are documented beside the application they govern. | `dependencies`; environment table | eve_runtime/package.json:14-20; eve_runtime/README.md:10-46 |
| The authored application applies the binding this module carries at `session.started`. | `defineDynamic`; `session.started` | eve_runtime/agent/instructions/ar-binding.ts:1-31 |
| The adapter is the only consumer that resolves a spec, hands it to a transport, and verifies the effective selection it produced. | `EveSessionAdapter._resolve_spec`; `_verify_effective_selection` | mcp/src/agents_remember/serving/eve_adapter.py:660-700; mcp/src/agents_remember/serving/eve_adapter.py:890-915 |
| The factory recovers the applied selection by probing a `LaunchSpec` through this module's reader, so the values that reached the child are the ones verified. | `_eve_expected_selection`; `launch_spec_selection` | mcp/src/agents_remember/serving/harness_control_factories.py:105-130; mcp/src/agents_remember/serving/eve_runtime_launch.py:328-353 |
| The launch-vocabulary contract holds the new harness without an edit to the parametrized test, and now includes the environment carrier eve uses. | `_knob_values`; `test_every_harness_carries_a_clean_selection_into_its_own_launch_vocabulary` | mcp/tests/test_harness_launch.py:173-196 |
| The OS-level start-failure seed is an operator naming a nonexistent `AR_EVE_NODE`, which only fails because this module reads the selector as given. | `START_FAILURES`; `failureType` | mcp/tests/live_eve_native_fixture.py:83-100; mcp/tests/live_eve_native_fixture.py:1070-1090 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pinned `eve` release and its Node `>=24` engine requirement come from the published package, not from a sibling Agents Remember repository. | exact pins; `engines` | eve_runtime/package.json:6-20 |

## Update History

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
