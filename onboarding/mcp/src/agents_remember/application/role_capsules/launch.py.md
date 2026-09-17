# mcp/src/agents_remember/application/role_capsules/launch.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/role_capsules/launch.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T09:10+02:00 |
| lastVerifiedCommitHash | `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
| lastVerifiedCommitDate | 2026-09-17T09:06:38+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l15-ar` uncommitted source (17 dirty paths); base `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
| governingOverview | `../overview.md` |

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
(`routed_admission_for`). The operation is `orientation`, the registered compile operation's own
default.

## Code Commentary

### Logic

**Two admittances, resolved together.** `_compile_admitted_task` resolves the five facts every carrier
needs **at once** into `AdmittedTaskSeat` — role, document reference, enclosure selector, the
repository root the document's own `repo` field resolves to, and the document's repository name —
because resolving them apart is how two carriers end up binding to two different enclosures. The task
document the launch already holds is resolved by the task layer (`TaskDocumentTopology.resolve`), and
the enclosure that admits it by the control plane's own reader
(`WorktreeContractReader().find_task_contract`): a leaf document by its leaf id, any other document by
its task's own series contract. Nothing is taken from a caller's string.

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

**One authority for the repository root (D13's second half).** `_registered_repository_root` reads the
root for the repository the document itself declares out of the server's configuration — and
`application/skill_resources/capsule.py` carries the same resolved root onto `AdmittedEnclosure` so the
task projection resolves against it instead of re-deriving (or failing to derive) one of its own. Both
halves were required; the projection half refused with `projection-binding-unresolved` in any tree whose
repository does not sit directly under the workspace.

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
  (`routed_admission_for`), one admission operation, one `orientation` default.
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
- **No Codex launch's cwd moves.** The Codex carrier admits no workspace, so `session_workspace` is
  `None` there and the rule returns the server's workspace. Free agents and every legacy launch keep
  `config.workspace_root` unchanged.
- **This module compiles; it does not decide modes.** The `capsule`/`legacy`/`refused` decision belongs
  to `serving/launch_capsule.py`; this module is only ever called for a seat that gate already admitted.

### Todos

The declared successor obligation **(A)** — a typed taskless admission in the frozen
`CapsuleAdmittedFacts` with per-consumer cases — is carried by the owning seat into the master's
obligation ledger for L11's verification. It is not this leaf's work.

## Docs References

No Domain Documentation source is configured in the resolved source registry for this pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| How a taskless seat's absent task plane is spelled once, and why it cannot be mistaken for a task path. | `FREE_AGENT_TASK_REFERENCE_PREFIX` | mcp/src/agents_remember/application/role_capsules/launch.py:83-89 |
| The work branch of a taskless seat whose workspace is not a git work tree. | `UNVERSIONED_WORK_BRANCH` | mcp/src/agents_remember/application/role_capsules/launch.py:92-96 |
| Where a launch's eve carrier is written, and why it is outside every workspace. | `EVE_CARRIER_ROOT` | mcp/src/agents_remember/application/role_capsules/launch.py:99-105 |
| The five facts a task-attached seat resolves together so two carriers cannot bind two enclosures. | `AdmittedTaskSeat` | mcp/src/agents_remember/application/role_capsules/launch.py:109-123 |
| The frozen DTO's absent task plane, minted once here; the digest is the admission's own content address. | `FreeAgentSeatAdmission`; `FreeAgentSeatAdmission.digest`; `FreeAgentSeatAdmission.admitted_facts` | mcp/src/agents_remember/application/role_capsules/launch.py:126-196 |
| The altitude comes from the composition manifest and the workspace identity from the workspace's own Git facts. | `free_agent_seat_admission` | mcp/src/agents_remember/application/role_capsules/launch.py:199-230 |
| The repository identity a taskless seat is admitted under, and the branch fallback. | `workspace_identity`; `_registered_repository_for` | mcp/src/agents_remember/application/role_capsules/launch.py:233-247; mcp/src/agents_remember/application/role_capsules/launch.py:249-264 |
| The entry point the launch points reach through the serving port, and its own role refusal. | `compile_launch_capsule` | mcp/src/agents_remember/application/role_capsules/launch.py:273-295 |
| The task-attached path: document resolution, the registered root, the enclosure lookup, and the named refusals. | `_compile_admitted_task` | mcp/src/agents_remember/application/role_capsules/launch.py:297-360 |
| The eve carrier path, including the admitted-workspace read-back out of the artifact the consumer re-verifies. | `_compile_eve_task` | mcp/src/agents_remember/application/role_capsules/launch.py:362-405 |
| The free-agent path, and the named refusal of an eve free agent. | `_compile_free_agent` | mcp/src/agents_remember/application/role_capsules/launch.py:407-448 |
| The delivered value and its per-run record; the two carriers are set exclusively. | `_capsule_launch` | mcp/src/agents_remember/application/role_capsules/launch.py:450-488 |
| The enclosure lookup goes through the control plane's one contract reader. | `_enclosure_contract` | mcp/src/agents_remember/application/role_capsules/launch.py:522-537 |
| The carrier directory is per seat and derived from the task path. | `_carrier_directory` | mcp/src/agents_remember/application/role_capsules/launch.py:552-557 |
| The one routing rule for a seat addressed by role and operation, which a taskless launch also uses. | `routed_admission_for` | mcp/src/agents_remember/application/skill_resources/capsule.py:515-554 |
| The same operation the registered MCP tool answers, and the resolved repository root that D13's second half carries onto the projection request. | `compile_task_capsule`; `AdmittedEnclosure`; `AdmittedEnclosure.code_repository_root` | mcp/src/agents_remember/application/skill_resources/capsule.py:205-259; mcp/src/agents_remember/application/skill_resources/capsule.py:186-202; mcp/src/agents_remember/application/skill_resources/capsule.py:262-289 |
| L7's produce side, which the eve path calls rather than adding a second carrier format. | `materialize_eve_binding` | mcp/src/agents_remember/application/eve_capsule/__init__.py:147-206 |
| The taskless seat class the developer's free-agent ruling admits. | `TASKLESS_SEAT_ROLES` | mcp/src/agents_remember/serving/task_binding.py:1-120 |
| The cases pinning the named absence, the identity-moves-with-the-seat rule, and the registered boundary. | `test_the_free_agent_admission_names_its_absent_task_plane`; `test_the_free_agent_capsule_identity_moves_with_the_seat` | mcp/tests/test_capsule_launch_wiring.py:920-944; mcp/tests/test_capsule_launch_wiring.py:946-974 |
| The production-chain acceptance for a task-attached seat and for a free agent, read from each session's own first prompt. | `test_a_task_attached_seat_reads_its_compiled_capsule_out_of_its_own_first_prompt`; `test_a_free_agent_reads_its_compiled_capsule_out_of_its_own_first_prompt` | mcp/tests/test_capsule_launch_wiring.py:484-528; mcp/tests/test_capsule_launch_wiring.py:530-575 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-17T09:10+02:00 — 260915-CAPS-L15 curator: **created this card** (the census reported it
  missing, `integrity.missing_onboarding`). Records the module as the compiler connection the severed
  chain lacked: the two admittances resolved together into `AdmittedTaskSeat`, the free agent's **named
  absence** (`free-agent:<role>`, refused by the task layer's own parser) as convention (B) with
  successor obligation (A) routed to L11, the two carriers the master already built, the eve
  admitted-workspace read-back that is the `L15R-1` fix, the one routing rule that keeps a taskless
  launch from re-deriving a source set, and the named refusals every unresolvable half returns.
  Verification metadata pins the leaf's base `15fa0e2c`; the candidate is deliberately uncommitted, so
  the governed closeout stamps the real code commit and no hash or fingerprint was invented here.
