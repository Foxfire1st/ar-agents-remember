# mcp/src/agents_remember/application/role_capsules/launch.py

## Governing Overview

[application overview](../overview.md)

## Purpose

**The module the severed chain was missing: compile the capsule one launch must supply, through the
compiler every seat already uses.** Until it existed the compiler (L2), the admission and MCP surface
(L4), the Codex carrier (L5) and the eve carrier (L7) were each individually proven and **no production
launch point supplied a capsule to anything** — a dispatched seat and a free agent both launched with
no instructions at all, and every test hand-supplied the intermediate value, which is exactly why no
leaf's suite could see the gap.

It is the `application`-rank (21) implementation behind `serving.launch_capsule`'s resolver port, and
it adds **no second routing rule**: a task-attached seat goes through `compile_task_capsule` — the same
operation the registered `role_capsule_compile` MCP tool answers — and a seat with no task document
goes through `compile_admitted_capsule` with the routed source set built by the same manifest rule
(`routed_admission_for`). The default operation remains `orientation`, the registered compile operation's own
default; an explicit operation is narrowed before compilation and carried through admission.

Compiles admitted role instruction capsules for existing launch paths.

## Code Commentary

### Logic

**Task admission, resolved together.** `_compile_admitted_task` resolves the launch's canonical
task through `TaskDocumentTopology.resolve` and `_admit_task_document`. `AdmittedTaskSeat` carries
role, narrowed operation, document reference, enclosure selector, contract path, the contract-declared
canonical repository root, and the document's repository name together. A registered MCP entry proves
repository authorization; its possibly scoped worktree path is not the canonical repository identity.
The control-plane contract reader resolves leaf admission by leaf ID and other enclosed tasks through
their series contract. Without an enclosure, only an explicitly admitted orchestrator/sprint or
manager/master Projects launch can use `ProjectTaskSeatAdmission`; every leaf retains enclosure admission.

Each unresolvable half is a **named** refusal, not a crash: `task-binding-unresolved`,
`repository-not-registered`, `enclosure-not-found` (whose detail tells the operator to run
`worktree_start` and dispatch again), `eve-carrier-refused`, `capsule-not-compiled`.

**The free agent, and the one convention this module had to define.** A free agent — a role, no task
document; `bootstrap` is admitted to that class by `TASKLESS_SEAT_ROLES` — has no task plane at all. The
frozen `CapsuleAdmittedFacts` has no typed absence for it (all four identity fields are non-blank
strings), so the absence is minted **once, here**, by `FreeAgentSeatAdmission`:

- `task_reference` is `free-agent:<role>` (`FREE_AGENT_TASK_REFERENCE_PREFIX`), a canonical,
  self-describing value that deliberately **does not parse as a task reference** — the task layer's own
  parser requires `<repository>/<path>.json` and therefore refuses it loudly rather than resolving it to
  a document that does not exist;
- the digest covers the admission the launch actually performed (canonical JSON over role, operation,
  altitude, repository id, work branch, and `taskDocument: null`), so the same seat in the same
  workspace compiles to the same capsule identity and a different seat or workspace does not;
- `free_agent_seat_admission` reads the two facts that do exist from their owners: the altitude from the
  composition manifest the compiler will read again, and the workspace identity
  (`workspace_identity`) from the workspace's own Git facts — the registered repository containing it
  when one does, otherwise the directory's own name, with `UNVERSIONED_WORK_BRANCH` when the workspace
  is not a git work tree.

This is convention **(B)** from the leaf's ruling: option (A) — a typed taskless admission in L2's
frozen contract — is the right end-state shape but edits a DTO two leaves downstream of its owner and
ripples into the compiler's digest lines, `diagnostics.py`, `capsule_delivery_from` and the task
projection parser. **(A) is a successor obligation carried to L11's ledger, not done here and not
presented as done.**

**The two carriers are the ones the master already built.**

- **Codex**: `_compile_admitted_task` → `compile_task_capsule` → `_capsule_launch` →
  `capsule_delivery_from(result)` onto `LaunchCapsule.codex_delivery`.
- **eve**: `_compile_eve_task` → L7's own produce side `materialize_eve_binding` (with the carrier
  directory `_carrier_directory` writing under `EVE_CARRIER_ROOT` = `runtime/eve-carriers`, outside
  every workspace by construction, so the instructions the runtime applies are not a file the model can
  rewrite), and the carrier's admitted workspace is **read back out** of the artifact —
  `Path(bound.carrier.workspace.root)` — and carried on the resolved capsule as `session_workspace`.
  That read-back is the fix for the sealed finding `L15R-1`: the launch runs where its capsule admits,
  so the cwd, the settings selection and `AR_WORKSPACE_ROOT` are one value instead of three that have
  to agree.
- An **eve free agent refuses by name** (`eve-carrier-requires-admitted-worktree`): the eve carrier
  binds a runtime to the admitted git worktree of a task enclosure and a taskless seat has none.

**Canonical repository root and scoped tool access.** `_registered_repository_root` checks that
the task document's repository is registered. For an enclosed task, `_admit_task_document` then reads
`contract.code_repo_path` as the canonical repository root; a scoped MCP worktree path remains the
reader's code root. The same resolved canonical identity is carried onto `AdmittedEnclosure` so task
projection does not derive another repository from workspace placement. The earlier D13 projection
failure explains why that identity must remain explicit.

**`_admitted_surfaces`** reads the enclosure's own `reports` directory and memory worktree out of the
contract the enclosure lookup already resolved, so a carrier declares the surfaces that exist rather
than the surfaces this module would have liked.

### Conventions

- The per-run record keys (`mode`, `role`, `operation`, `semanticDigest`, `taskReference`,
  `instructionCount`, `instructionBytes`, plus `eveCarrier`/`sessionWorkspace` when they exist) are
  wire-visible: they are published verbatim as `instructionMode`. A rename is a transport change.
- Refusal statuses are lowercase hyphenated strings carried on `LaunchCapsule.refusal_status` and
  surfaced by the launch points (`capsule-unavailable` at both wired launch points).
- Rank discipline: this module may import `serving` for the carrier value types, and `serving` may not
  import it back — the port exists for exactly that reason.

### Invariants And Boundaries

- **Nothing here re-implements selection.** One compiler, one routing rule
  (`routed_admission_for`), a narrowed operation carried through admission, and the existing `orientation` default.
- **`FreeAgentSeatAdmission` is the only producer of a taskless `CapsuleAdmittedFacts`.** No other site
  may mint that value, and no consumer may read `free-agent:<role>` as a task path.
- **A role that is not in the frozen `CAPSULE_ROLES` vocabulary never reaches the compiler** — it is
  refused by name, so "unknown role" can never become a silent legacy launch.
- **A launch point resolves before any host side effect.** A refusal returns before
  `open_terminal_session`, before the opener, and the opener refuses one defensively as well.
- **The admitted workspace is read from the carrier, never computed.** The value comes out of the
  artifact the consumer re-verifies; `verify_capsule_binding`, `_require_admitted_git_worktree` and
  `launch_spec_binding` are untouched by this leaf, and no second enclosure or worktree lookup was
  added.
- **The retained terminal Codex carrier admits no workspace.** `session_workspace` is `None` for
  that carrier, so the terminal workspace rule returns the server's workspace. Paseo role launch folder
  placement is owned separately by `role_launch_preparation`. Free agents and legacy terminal launches
  keep `config.workspace_root` unchanged.
- **This module compiles; it does not decide modes.** The `capsule`/`legacy`/`refused` decision belongs
  to `serving/launch_capsule.py`; this module is only ever called for a seat that gate already admitted.

### Todos

The declared successor obligation **(A)** — a typed taskless admission in the frozen
`CapsuleAdmittedFacts` with per-consumer cases — is carried by the owning seat into the master's
obligation ledger for L11's verification. It is not this leaf's work.

### Role Runtime and Scope

Task-attached admission separates the contract-declared canonical repository identity from the scoped MCP code root. compile_launch_capsule accepts an explicitly narrowed operation; the role-aware launcher may admit real sprint/master tasks at the configured Projects workspace only through allow_project_task_binding. That path uses canonical task bytes and no invented taskless identity or worktree. Leaf admission keeps enclosure authority.

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved source registry for this pass.

No configured live documentation source was available for this pass.

### Repo-Internal References

- How a taskless seat's absent task plane is spelled once, and why it cannot be mistaken for a task path. [1]
- The work branch of a taskless seat whose workspace is not a git work tree. [2]
- Where a launch's eve carrier is written, and why it is outside every workspace. [3]
- The five facts a task-attached seat resolves together so two carriers cannot bind two enclosures. [4]
- The frozen DTO's absent task plane, minted once here; the digest is the admission's own content address. [5]
- The altitude comes from the composition manifest and the workspace identity from the workspace's own Git facts. [6]
- The repository identity a taskless seat is admitted under, and the branch fallback. [7]
- The entry point the launch points reach through the serving port, and its own role refusal. [8]
- The task-attached path: document resolution, the registered root, the enclosure lookup, and the named refusals. [9]
- The eve carrier path, including the admitted-workspace read-back out of the artifact the consumer re-verifies. [10]
- The free-agent path, and the named refusal of an eve free agent. [11]
- The delivered value and its per-run record; the two carriers are set exclusively. [12]
- The enclosure lookup goes through the control plane's one contract reader. [13]
- The carrier directory is per seat and derived from the task path. [14]
- The one routing rule for a seat addressed by role and operation, which a taskless launch also uses. [15]
- The same operation the registered MCP tool answers, and the resolved repository root that D13's second half carries onto the projection request. [16]
- L7's produce side, which the eve path calls rather than adding a second carrier format. [17]
- The taskless seat class the developer's free-agent ruling admits. [18]
- The cases pinning the named absence, the identity-moves-with-the-seat rule, and the registered boundary. [19]
- The production-chain acceptance for a task-attached seat and for a free agent, read from each session's own first prompt. [20]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

No meaningful cross-repo references found.

### Runtime Source References

- Frozen implementation of compile_launch_capsule supporting the stated file behavior. [21]
- Frozen implementation of _admit_task_document supporting the stated file behavior. [22]
- Frozen implementation of ProjectTaskSeatAdmission supporting the stated file behavior. [23]
