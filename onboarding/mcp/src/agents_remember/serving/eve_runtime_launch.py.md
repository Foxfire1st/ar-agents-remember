# mcp/src/agents_remember/serving/eve_runtime_launch.py

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
without it. Staging the same **complete** destination twice is idempotent, which is what lets an epoch
restart without rebuilding its tree.

**The install is checked before anything is copied (defect D20, repaired by 260915-CAPS-L15).** Staging
used to copy the application surface first and only then discover that the runtime's dependencies were
missing, so a refused launch left a half-staged directory behind and the **next** staging call in the
same process found it populated and returned early — passing without the install. A refusal a retry can
turn into a pass is not a refusal. Now the `source/node_modules` check happens before `destination` is
touched, so a second call refuses identically and by name, and the early return is guarded by
`_staged_application(destination)`, which requires **both** halves — the authored surface *and* the
dependency link — so a half-staged tree is repaired rather than trusted. The measured shape of the
defect is the reason it matters: L16's environment-gated failures were not stable (which case failed,
and how many, moved between runs) because whichever case staged first paid the refusal and every later
stager in that process passed.

`resolve_runtime_spec` builds the `EveRuntimeLaunch` and carries the **caller's interpreter choice
verbatim** as `node_executable` (`AR_EVE_NODE`). Reading the selector here rather than at spawn is what
makes a bad path fail with the path the operator actually named; the executable search, the
minimum-major check and the refusal that advertises both candidates stay with the transport that
spawns, so the search remains lazy and a deterministic test transport can consume a spec without an
installed interpreter.

**Admission precedes the process.** `resolve_runtime_spec` calls `verify_capsule_binding` first — before
an application root is staged or a port is reserved — and carries the verified carrier onto
`EveRuntimeSpec.capsule` so a caller reports what was *actually applied* rather than re-deriving it from
the environment it just wrote.

`verify_capsule_binding` (447) is the launch-time proof, an all-or-nothing gate with **six refusals,
each naming its defect**: a partly declared binding (`AR_BINDING_REF`, `AR_CAPSULE_PATH` and
`AR_CAPSULE_DIGEST` must arrive together — a bound launch names all three or none); a carrier that
cannot be read; a carrier whose bytes are not the declared digest (a capsule that changed after
admission); a carrier written for another binding (`require_identity`); a carrier whose admitted
workspace is not this launch's workspace; and a workspace that is not the admitted git worktree.
An entirely undeclared binding returns `None` — an **unbound** launch stays unbound and is started
without a binding, which the runtime refuses at its session routes rather than executing without
admitted instructions.

`_require_admitted_git_worktree` (499) reads the workspace's own git metadata through `_read_git_head`
(529) and compares: on a branch, `HEAD` must be the admitted work branch; detached, `HEAD` must be the
admitted base commit. It deliberately does not shell out to git. The distinction matters because *a
directory that exists at the admitted path is not the admitted worktree* — a sibling task's checkout, a
copied tree and a detached checkout all satisfy "the path exists" while executing somewhere nobody
admitted.

`build_runtime_env` composes the child environment from the operator's base plus this adapter's owned
values, and **owned values always win** over an inherited value of the same name, so an ambient
`AR_EVE_MODEL` can never silently redirect a launch the settings selection already fixed. It also
**pops `AR_EVE_RUNTIME_ROOT` and `AR_EVE_NODE` from the child environment**: both are resolved into
the launch object before this point, so leaving them inherited would let a stale ambient value point
the process at a different application than the adapter resolved. For the same reason it now also pops
**`AR_BINDING_REF`, `AR_CAPSULE_PATH` and `AR_CAPSULE_DIGEST`**: the runtime treats a complete set of
those names as an admitted capsule, so one inherited from the operator's shell would be a binding
nobody verified. They are re-set below strictly from the binding this launch declares.

`launch_spec_binding` (430) reads **only the launch spec**: an ambient `AR_BINDING_REF` in the server's
own environment is not this launch's binding, and treating it as one would let the operator's shell
decide which seat a runtime runs as.

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

- Environment names this adapter owns are the `AR_EVE_*` group plus the four AR binding names
  (`AR_BINDING_REF`, `AR_CAPSULE_PATH`, `AR_CAPSULE_DIGEST`, `AR_WORKSPACE_ROOT`, imported from the
  carrier module); `OWNED_ENV_PREFIX` documents the `AR_EVE_*` grouping.
- `DEFAULT_RUNTIME_PORT = 0` means "reserve a free loopback port at launch"; `choose_runtime_port`
  binds and closes a socket so a collision fails the launch loudly instead of silently serving on a
  port the adapter cannot address.
- `launch_spec_selection` reads the selection the runner already applied to the launch spec, so the
  launch spec — not ambient process state — is the authority.
- `_checkout_root` walks up for the sibling `eve_runtime` directory rather than counting path levels,
  so moving this module inside the package cannot silently repoint the lookup.

### Invariants And Boundaries

- **This module carries the AR capsule binding and now *proves* it; it still does not compile or
  select a capsule.** `EveWorkspaceBinding` transports `AR_WORKSPACE_ROOT`, `AR_BINDING_REF`,
  `AR_CAPSULE_PATH` and `AR_CAPSULE_DIGEST`, and `verify_capsule_binding` (447) turns a declared
  binding into verified carrier bytes **before a process exists**. Where those values come from — which
  seat, which task, which compiled capsule — remains the capsule/workspace seam's scope, and
  `materialize_eve_binding` is that seam's producer.
- **`AR_EVE_RUNTIME_ROOT` and `AR_EVE_NODE` are live selectors, not advisory names.** The root is
  honoured at resolution and the interpreter is carried onto the launch; both are then popped from the
  child environment so the process cannot re-resolve itself elsewhere. Documenting them without
  reading them is the defect this rule exists to prevent.
- **A refusal is not undoable by a retry (D20).** The dependency install is checked before the
  destination is touched, and the idempotent early return requires a complete staged application
  (surface **and** dependency link). A half-staged destination is repaired, never trusted.
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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

No configured `Domain Documentation` source; Node's engines contract and eve's own `engines` field are the external authorities, cited from the runtime package.

### Repo-Internal References

- The launch spec, identity and workspace binding are AR's existing control-wire types. [1]
- The launch knobs are AR's existing capability-port type, which is why eve participates in the same launch-vocabulary contract as the other harnesses. [2]
- The declared pins and the operator-facing environment contract are documented beside the application they govern. [3]
- The authored application applies the binding this module carries at `session.started`, and the channel's own AR binder is the route gate that refuses an unbound launch before any model work. [4]
- The launch-time proof itself, and the git-identity requirement behind it, whose six refusals each name their defect. [5]
- The carrier format and environment names this module verifies against, declared in the models tier so the reader and the writer share one spelling. [6]
- The D20 repair: the install is checked before the destination is touched, and the early return requires a complete staged application. [7]
- The case pinning the repaired refusal: a first refusing call followed by a second in the same process refuses identically. [8]
- The produce side of the same seam, which writes the carrier this module reads — and which **now has a production caller**: `application/role_capsules/launch.py::_compile_eve_task` materializes it for a wired launch point, verified from the consumer's side by `E8`. [9]
- The cases pinning the launch-time verification in both directions, including a workspace checked out on another branch. [10]
- The adapter is the only consumer that resolves a spec, hands it to a transport, and verifies the effective selection it produced. [11]
- The factory recovers the applied selection by probing a `LaunchSpec` through this module's reader, so the values that reached the child are the ones verified. [12]
- The node floor is owned by the readiness module and re-exported here, so detection and launch read one number. [13]
- The runtime's own model fallback, read from the authored application rather than mirrored as a constant. [14]
- The capability catalog consumes this fallback so a pre-session read names the model the runtime would really use. [15]
- The case pinning that the advertised model is the one the runtime would use. [16]
- The launch-vocabulary contract holds the new harness without an edit to the parametrized test, and now includes the environment carrier eve uses. [17]
- The OS-level start-failure seed is an operator naming a nonexistent `AR_EVE_NODE`, which only fails because this module reads the selector as given. [18]

### Cross-Repo References

- The pinned `eve` release and its Node `>=24` engine requirement come from the published package, not from a sibling Agents Remember repository. [19]
