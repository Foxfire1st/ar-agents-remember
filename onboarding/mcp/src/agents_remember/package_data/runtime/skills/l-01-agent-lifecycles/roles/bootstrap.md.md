# l-01-agent-lifecycles/roles/bootstrap.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The portable **bootstrap** lifecycle: the tenth canonical role in the `l-01-agent-lifecycles`
registry, and the free agent for a new user's first hour. It establishes what Agents Remember is
and what the developer has to decide, then takes one repository from *nothing usable* to *a memory
root that resolves* through the surfaces that own each step — memory root, spear branch, first
onboarding, first attributed baseline, indexing — and reports what actually happened.

It is a sync-propagated (`scripts/sync-skills.py`) package-data copy of the canonical
`skills/l-01-agent-lifecycles/roles/bootstrap.md`. A `role=bootstrap` session opens it through the
shared deterministic compiler like every other role; it is not a second instruction tree.

## Code Commentary

### Logic

The role is a **free agent**, and that is a developer ruling rather than a description: *"It is not
a task related agent. Can't be. It needs to be free agent. All what it needs is that can 'call'."*
A regular agent — the developer's own session in the AR dashboard is the intended caller — starts it
by **opening a session with this role and no task document**. There is no task document, no leaf, no
worktree, no gate, no requirement packet and no dispatch brief, and their absence is normal rather
than an error to repair.

Two consequences the text states as its own shape, not as gaps:

- **It has no task altitude, deliberately.** `bootstrap` is absent from the task layer's
  sprint/master/leaf role sets and from the structural-seat admission rules. Adding one is the wrong
  fix: an altitude is what would make it the task-coupled seat the ruling removed.
- **It is not reachable by `dispatch_agent`.** That transaction addresses a seat by canonical task
  document and dispatches rather than opens. It belongs to the task-bound pipeline; this seat is
  correctly outside it.

The gate admits it **by name**: `serving/task_binding.py` keeps one exported, commented set of roles
for which no document is required, and `260921-ICR-L32` changed the **membership** of that set on the
developer's 2026-09-24 ruling rather than its shape — it is now
`TASKLESS_SEAT_ROLES = {"chat", "terminal", "bootstrap", "curator"}` — while
`serving/terminal_task_assignment.py` reads the same set rather than restating it. This seat is one of
the four names in it, and a taskless `curator` session is another (see the seat-policy note below).
Without that admission a `role=bootstrap` call would be refused `task-binding-required` before any
session was created. Being taskless also means the structural **altitude check does not run** for the role, with
or without a document: there is no altitude to validate against. A supplied document is still
resolved, so a bad reference is still refused as `task-binding-invalid`.

**Its instructions are its compiled capsule, and nothing else.** A task seat is booted by the brief
its dispatcher pins; this agent has no dispatcher and no brief, so the compiled capsule for
`(bootstrap, bootstrap)` is its instruction source. The five composed blocks are
`core:acceptance`, `core:authority`, `core:invariants`, `role:bootstrap`, `operation:bootstrap`, in
the registry's composition order, and the manifest declares the role with `altitude: "free-agent"`
and no templates or criteria catalogs.

**Its subject is the first hour, and it points rather than restates.** The ordered workflow and the
failure-state inventory live in `operations/bootstrap.md`; the steps themselves belong to the skills
that own them (`c-00-initialize-memory-repo`, `c-03-repo-bootstrap`, `c-10-adopt-memory-baseline`,
`c-02-memory-quality-control`, `c-08-ar-coordination-context-resolver`, `c-13-install-and-onboard`).
The role is explicitly **not** a general maintenance posture: once a repository has a resolving
context, ordinary work belongs to the lifecycle roles, and a later request to "tidy" a working
installation is refused with the owning skill named. It is also not a thin alias for the free-chat
launcher and not a fourth router condition.

**Role-seat immutability applies**: the session stays bootstrap for its lifetime, and a pasted brief
for another role is refused and reported rather than absorbed.

### Conventions

- The role file keeps the corpus's readable order — purpose and authority → required inputs →
  normal workflow → permitted writes and actions → stop and escalation cases → completion and
  handoff — followed by its machine-readable knob block, and declares its shared sources with a
  single `**Inherits:**` line instead of restating them.
- Editing it means editing the canonical `skills/l-01-agent-lifecycles/roles/bootstrap.md` and
  running `python scripts/sync-skills.py`; the nine generated copies are never hand-edited.
- Its permitted surface is a positive list, and it is deliberately narrow: the setup surfaces, the
  read-only resolution/retrieval surfaces, native reads, and exactly one artifact — its own report.
  Everything task-shaped (`worktree_*`, `task_doc`, `lifecycle_*`, `gate_*`, `dispatch_agent`,
  `closeout_*`, `direct_landing`, the inbox role tools) is named as *not* this seat's machinery.
- Each step is read back from the tools after every mutating call: a step is complete when a
  follow-up call says so, not when the call returned without raising.

### Invariants And Boundaries

- **A free agent is not a task seat.** No card, projection, notifier expectation or lifecycle badge
  may present `bootstrap` as a task-bound role, and the absent task altitude must not be "fixed".
- **Delivery of its capsule is another leaf's work, and this card claims no delivery.** A session
  started with `AR_SPAWN_ROLE=bootstrap` reaches the runtime with its role and hosted identity and is
  then booted with **no instructions at all** until the capsule is delivered to a launch; the
  session-start directive expects a brief that nothing sends. Name that gap wherever readiness is
  reported; do not describe the seat as ready when it cannot be instructed.
- **Its report is its only handoff.** A free agent has no lifecycle row and no terminal state, so
  `lifecycle_finalize_task`, `worktree_cleanup`, closeout/integration and the deliverable-evidence
  hold point have nothing to act on. That is the designed outcome, and it forbids inventing a
  "bootstrap completed" projection or inferring completion from a process exit.
- **The role does not duplicate a `c-*` procedure.** A copy of a procedure here would drift from its
  owner, so the text carries none.
- **No onboarding documentation inside code** (the packet's boundary): the setup knowledge lives in
  the instruction corpus and the capsule, and code-resident setup prose is a pointer at the corpus.
- **The capsule is delivered in argv.** Its rendered size counts against the OS argument limit, so
  this seat is one of the consumers of the stated compiled-capsule size bound.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local role file.

No relevant documentation found after checking live sources.

### Repo-Internal References

- Canonical source this package-data copy is sync-propagated from. [1]
- The role declares no inherited core blocks — it is a free agent, not a task seat, and is started by a call. [2]
- The role's start is a call rather than a dispatch: nothing dispatches this agent, and nothing names its report path. [3]
- The seat sits outside the task-dispatch transaction as its shape: a task document, gate, packet, or compiled brief is not an input, and its absence is not an error. [4]
- The role's instructions are the capsule itself — this page plus the bootstrap operation — and its brief is not a brief. [5]
- The permitted-write surface, the stop-and-report cases, and the report's own inline shape, which no template file owns. [6]
- The operation block the role carries: workflow, failure inventory and authority gates. [7]
- The manifest entry declaring the free-agent altitude, its five tools and its three operations. [8]
- The named taskless-seat admission this role's existence depends on, whose membership `260921-ICR-L32` changed on the developer's 2026-09-24 ruling. [9]
- The second reader of the same set, so the policy has one spelling. [10]
- The frozen vocabulary extension that publishes the role and its operation. [11]
- The shipped checks: free-agent shape, taskless admission, no altitude, and the manifest declaration. [12]
- The corpus shape checks every role file must satisfy, this one included. [13]
- The generated copies this file is one of, proved current by the generator's own check. [14]

### Cross-Repo References

No sibling-repository contract defines this role file.

No meaningful cross-repo references found.

## 260921-ICR-L27 The First-Hour Seat Reaches The Knowledge Foundation And Authors Nothing

`260921-ICR-L27` (`ICR-R27@v1`) gives this role the half of the knowledge bootstrap that exists **before
a task does**. The role's step 5 makes it the carrier that reads the state at the declared knowledge
location, reports it, and hands the authoring to a curator — on a task document for a real task, or
through the taskless writer an instructed session holds — while authoring no records itself. The reason
is the opener's gate, stated in the role file in the product's own vocabulary: a session opened for the
curator **with no task document is refused** (`task-binding-required`), while this seat is admitted
taskless.
> **Seat-policy note at L27's bytes (dated 2026-09-24).** This records the policy of the candidate that curation read: code base `06ed70cfcde7e3860ee5b53435727e7512e4335c` plus that leaf's working-tree delta, where a document-less `curator` session was refused `task-binding-required` because `TASKLESS_SEAT_ROLES` was `{"chat", "terminal", "bootstrap"}`. That was true of those bytes and is **superseded** — whether `curator` joined the set was then a product decision under revision, and it was taken in `260921-ICR-L32`.
>
> **Seat-policy note at these bytes (L32 curation, dated 2026-09-24T17:20+02:00).** At the bytes this curation read — code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus this leaf's working-tree delta — `TASKLESS_SEAT_ROLES` is `{"chat", "terminal", "bootstrap", "curator"}`: a document-less `curator` session is **admitted** and receives the curator capsule, while every other role is still refused `task-binding-required`. Read the sentences above as the policy **at these bytes**, not as a permanent property of the product.

Three smaller edits carry the same obligation: step 2 adds `c-14-knowledge-bootstrap` to the skills this
seat points at rather than restating; step 3 adds the **commit word** for the foundation as a decision
that is asked for rather than assumed; and the Outputs template gains a
`Knowledge foundation: <not-recorded | recorded at <identity> | unusable: <code and path> | not run, and
why>` line, with a matching self-check row. The prohibition list gains "Never author knowledge records
either", and the step states plainly that **a repository whose knowledge is not recorded is not reported
as ready** — the onboarding and the baseline can both be complete while the foundation is still absent,
and those are separate facts rather than one verdict.

**This card describes a generated copy**, propagated from `skills/l-01-agent-lifecycles/roles/bootstrap.md`
by `scripts/sync-skills.py` into this package-owned copy and the eight harness starter packages.
