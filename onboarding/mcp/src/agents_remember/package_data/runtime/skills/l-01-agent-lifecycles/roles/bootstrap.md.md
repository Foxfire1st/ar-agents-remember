# l-01-agent-lifecycles/roles/bootstrap.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/bootstrap.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-16T17:59+02:00 |
| lastVerifiedCommitHash | `0dd1df9a950d59ac9622e5fb54250e528df08fa5` |
| lastVerifiedCommitDate | 2026-09-16T20:47:18+02:00|
| governingOverview      | `../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../overview.md)

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
for which no document is required — `TASKLESS_SEAT_ROLES = {"chat", "terminal", "bootstrap"}` — and
`serving/terminal_task_assignment.py` reads the same set rather than restating it. Without that
admission a `role=bootstrap` call would be refused `task-binding-required` before any session was
created. Being taskless also means the structural **altitude check does not run** for the role, with
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

## Docs References

No external or domain documentation governs this repository-local role file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this package-data copy is sync-propagated from. | `# Lifecycle — Bootstrap` | skills/l-01-agent-lifecycles/roles/bootstrap.md:6-6 |
| The `**Inherits:**` line declaring the core blocks and operations this role composes from. | `**Inherits:**` | skills/l-01-agent-lifecycles/roles/bootstrap.md:12-13 |
| The ruling, the one-call start, and the absent-altitude statement. | `How this agent is started: one call, no task.`; `It has no task altitude, deliberately.` | skills/l-01-agent-lifecycles/roles/bootstrap.md:41-41; skills/l-01-agent-lifecycles/roles/bootstrap.md:66-66 |
| The seat is correctly outside the task-dispatch transaction, and that is stated as its shape rather than a gap. | `Not reachable by`; `and that is not a gap.` | skills/l-01-agent-lifecycles/roles/bootstrap.md:71-79 |
| The capsule-is-the-only-instruction-source statement, including the not-yet-delivered half. | `Its instructions are its capsule, and nothing else.` | skills/l-01-agent-lifecycles/roles/bootstrap.md:57-65 |
| The permitted-write surface, the stop/escalation cases, and the report template the seat writes. | `## 4 — Permitted Writes And Actions`; `## 5 — Stop And Escalation Cases`; `## 6 — Completion And Handoff`; `# Bootstrap Report — <repository>` | skills/l-01-agent-lifecycles/roles/bootstrap.md:116-116; skills/l-01-agent-lifecycles/roles/bootstrap.md:142-142; skills/l-01-agent-lifecycles/roles/bootstrap.md:159-159; skills/l-01-agent-lifecycles/roles/bootstrap.md:183-183 |
| The operation block the role carries: workflow, failure inventory and authority gates. | `# Operation — Session Bootstrap` | skills/l-01-agent-lifecycles/operations/bootstrap.md:1-1 |
| The manifest entry declaring the free-agent altitude, its five tools and its three operations. | `"altitude": "free-agent"`; `"bootstrap"` | skills/l-01-agent-lifecycles/composition-manifest.json:451-477 |
| The named taskless-seat admission this role's existence depends on. | `TASKLESS_SEAT_ROLES` | mcp/src/agents_remember/serving/task_binding.py:60-83 |
| The second reader of the same set, so the policy has one spelling. | `TASKLESS_SEAT_ROLES` | mcp/src/agents_remember/serving/terminal_task_assignment.py:12-12; mcp/src/agents_remember/serving/terminal_task_assignment.py:159-161 |
| The frozen vocabulary extension that publishes the role and its operation. | `CAPSULE_ROLES`; `CAPSULE_OPERATIONS` | mcp/src/agents_remember/models/role_capsules/vocabulary.py:82-96; mcp/src/agents_remember/models/role_capsules/vocabulary.py:98-111 |
| The shipped checks: free-agent shape, taskless admission, no altitude, and the manifest declaration. | `test_the_bootstrap_role_is_a_free_agent_and_has_no_task_altitude`; `test_without_a_task_document_only_the_taskless_seat_roles_are_admitted`; `test_no_task_altitude_set_in_the_source_names_bootstrap`; `test_the_manifest_declares_no_task_altitude_for_the_free_agent` | mcp/tests/test_memory_branch_authority.py:346-364; mcp/tests/test_memory_branch_authority.py:366-394; mcp/tests/test_memory_branch_authority.py:421-446; mcp/tests/test_memory_branch_authority.py:592-618 |
| The corpus shape checks every role file must satisfy, this one included. | `test_every_role_source_carries_the_readable_order_and_knob_block`; `ROLE_ORDER` | mcp/tests/test_role_instruction_corpus.py:404-466; mcp/tests/test_role_instruction_corpus.py:32-43 |
| The generated copies this file is one of, proved current by the generator's own check. | `CANONICAL_SKILLS`; `check_targets` | scripts/sync-skills.py:15-15; scripts/sync-skills.py:179-191 |

## Cross-Repo References

No sibling-repository contract defines this role file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: created this card for the tenth canonical role
  the leaf added (`CAPS-R13@v1`). It records the free-agent shape and its two stated consequences (no
  task altitude, not dispatchable), the named `TASKLESS_SEAT_ROLES` admission that makes a
  `role=bootstrap` call open instead of refusing, the capsule-only instruction source **with the
  delivery gap stated rather than smoothed**, the first-hour subject with its point-don't-restate
  rule, and the report-as-sole-handoff consequence of having no lifecycle row. Companion card:
  `operations/bootstrap.md.md`. Verification metadata is left at the leaf base commit because the
  source is uncommitted — the governed closeout stamps the real code commit, and no hash or
  fingerprint was invented here.
