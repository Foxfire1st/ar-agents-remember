# l-01-agent-lifecycles/SKILL.md

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

Packaged runtime copy of the consolidated lifecycle **router**. The canonical source at
`skills/l-01-agent-lifecycles/SKILL.md` owns the routing contract; `scripts/sync-skills.py` replaces
and checks this artifact byte-for-byte for installed runtimes.

The artifact's own boundary is load-bearing: **this file routes and does not carry doctrine.** It
holds the three routing conditions, the ten-role registry, the composition map, and the diagnostic
pointer sections; every doctrine rule now lives in exactly one other file — `core/` (shared, authored
once), `roles/<role>.md` (one self-contained lifecycle per seat), `operations/` (the nine
operation-scoped procedures), `composition-manifest.json` (routing metadata, no prose), and
`reference/` (rationale, provenance, superseded rulings). At 180 lines it is the thin router the
consolidation requires, down from the 620-line spine that used to double as the doctrine home.

## Code Commentary

### Logic

The router selects exactly one of three conditions, in order: plane-injected `AR_SPAWN_ROLE` →
`roles/<value>.md`; a fresh session whose first message is a `templates/*-brief.md`-shaped role brief
→ that role's lifecycle; otherwise the developer-facing **ambient launcher**, which is routing
condition 3 and deliberately not a role (its own obligations are `core/launcher.md`). The registry
row this leaf added is `bootstrap` — the new user's first-hour seat for one repository, reachable
before any task document exists and stating so when it is not reachable; it is a **free agent**, so
it is a registry member reached through condition 1, not a fourth condition.

For ordinary role-shaped work the launcher compiles `templates/architect-brief.md` from current
durable sprint truth and calls `dispatch_agent` once on the canonical sprint document; an explicit
developer-declared task-seat takeover targets the named role at its canonical altitude instead. The
one-call contract, the two dispatcher caller kinds, the idempotent retry, and the
`source-lineage-stale` / `source-lineage-unavailable` recovery moved to `core/authority.md`; the
router carries only the state-back summary and points there.

Edge cases are decided in the router itself: an unresolvable `AR_SPAWN_ROLE`, a role env without its
matching plane-injected hosted identity, or hosted identity without its matching role is malformed
plane identity and fails closed — it never falls through to a pasted brief or free-chat routing. A
valid role-env session whose brief never arrives announces itself and waits rather than improvising a
task. `AR_SPAWN_ROLE=orchestrator` is valid only as a spawned backend seat or a backend takeover
chair: the developer still talks to the architect. The spool-up chain is self-driving, and only two
spool-up decisions return to the developer (the propose-first strategist pass and the short root).

The router's `## Composition Map` is the human-readable counterpart of `composition-manifest.json`:
assembled order is **core → role → operation → explicitly admitted repository specialization**, task
facts travel as a separate context channel, the operation vocabulary is frozen at nine names and an
unknown operation is an explicit error, and composition invariants forbid truncating a required
obligation to meet a size target.

The `## settings.json Orchestration Block` section deliberately no longer restates a worked JSON
example; it states the layering and precedence and points at `docs/reference/settings-json.md` and
`docs/reference/harnesses.md` for the typed shape, with the seat-visible rules in
`core/invariants.md` § Knob resolution and capability doctrine.

### Conventions

Edit the canonical skill and run the sync process; never hand-author independent packaged doctrine.
The corpus has exactly one source per instruction: `core/` is authored once and a role file states
only its own seat's side of a shared rule. Adding a rule to this router re-creates the duplication
the consolidation removed, so a new doctrine rule belongs in `core/`, `roles/`, or `operations/` and
this file keeps only the pointer.

### Invariants And Boundaries

- This artifact must remain byte-identical to the canonical lifecycle SKILL.
- The router carries no doctrine: every rule resolves through exactly one `core/`, `roles/`,
  `operations/`, or `reference/` file.
- The role registry is exactly ten roles, and the ambient launcher stays routing condition 3 rather
  than an invented role. `bootstrap` is the tenth and is the only free agent among them: it is
  reached through condition 1 and carries no task altitude, which is its shape rather than a gap.
- `bootstrap` is not a fourth routing condition. The router still selects exactly one of three, and
  a reader must not add a condition to make the free agent easier to reach.
- No role is defined by reference to another role's lifecycle, and no role file sends its reader to a
  sibling's prose to learn its own obligations. A sanctioned sibling reference exists only for wearing
  that hat or dispatching that seat, and `mcp/tests/test_role_instruction_corpus.py` fails on any
  other one.
- Task-document-plus-role is seat identity; runtime occupant identity stays plane-private, and the
  full dispatch/takeover/recovery contract lives in `core/authority.md`.
- A queued structural dispatch is durable and follows the notifier retry path without duplicate
  briefs or respawn.
- Malformed hosted role identity is a refusal, not an ambient/free-chat fallback.
- Installed runtimes receive the same doctrine as the canonical tree, not a compatibility variant.

### Todos

None recorded.


## CCR-R12@v5 Transaction Boundary

Current lifecycle contract: workers run relevant targeted checks after changes and fixes and before handoff; curators update affected onboarding and run the complete memory-quality operation with honest failed or not-run status, repairing or escalating every curator-actionable finding with its exact returned code. Closeout and integration then perform the authorized Git transaction, whose commit legs suppress automatic quality and test hooks while ordinary explicit Git hook policy outside the transaction remains unchanged. Curation is never deferred: the curator always runs the full operation and its completed result is carried as a closeout and integration prerequisite, while full code quality, full tests, certification, and independent review run only after an explicit developer request. When review is requested, its sealed three-round monotonic finding-set rule remains in force.

## Evidence

### Docs References

No external domain documentation is configured for this repository-local lifecycle doctrine.

No relevant external documentation found.

### Repo-Internal References

- The packaged source carries the launcher, approval-gated strategist, architect-custody, and parallel-by-default invariants. [1]
- Canonical skills are propagated into package data and harness mirrors by the sync script. [2]
- The packaged source carries the launcher, approval-gated strategist, and parallel-by-default invariants as pointers, not as doctrine. [3]
- The router declares its own boundary — it routes, and every rule lives in exactly one other file — and names the ten-role registry plus the ambient launcher as a routing condition rather than an invented role. [4]
- The tenth registry row this leaf added, and the reachability sentence it carries. [5]
- Doctrine moved out of the router: shared rules to `core/`, procedures to `operations/`, rationale and superseded rulings to `reference/`, and routing metadata to the prose-free manifest. [6]
- The enabled corpus stays self-contained: the shipped check fails on a role that leaks a sibling's duties, on a manifest that names a missing source, and on any relative path the corpus cites that does not resolve. [7]

### Cross-Repo References

No sibling repository evidence is needed for this doctrine file.

No meaningful cross-repo references found.

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is
synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process.
Creation, exact-session readiness, and exact initial-brief delivery remain private phases inside
one public `dispatch_agent` transaction; callers do not sequence or address those phases.
Spawned-only or not-ready is not active work; `sessionCommands` remain launch configuration and
`promptKeywords` apply once during the private readiness-to-brief transition.


### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## 260713-TES-L5 Current Delta — Fact-Relay Supervision Doctrine (synced copy)

This synced runtime copy now teaches the fact-relay supervision model: the agent-notifier
sweep evaluates seat-state facts on its mechanical tick and relays them to owners
(turn-ended/completed state-signals, compound-idle, non-reaction residue); the timed
escalation ladder (renudge → skip-level → architect custody, then respawn) is retired, and no
role watches or nudges on its own initiative.

## L23 Dispatch Admission

Packaged lifecycle dispatch now resolves task-derived source lineage before
process creation. Managers require current super-to-master ancestry;
worker/reviewer/curator seats require the full code/external-memory chain. A
lineage refusal creates no child and is recovered by the ordered contract path,
never by asking an agent for branch or occupant ids.

## L23 Final Candidate Disposition

The packaged lifecycle roof now treats current task-derived lineage, exact-candidate independent
route review, and Dagger-only acceptance as shared lifecycle signals. Roles observe task-addressed
durable operations; they never carry private job or commit identifiers between turns.

## 260815-DAG-L2 Synchronized Execution Topology

This packaged copy carries the fact/judgment split, architect-owned portfolio-plan loop,
organizational direct-super lineage, atomic isolated-block lineage, and one-full-check-per-master
completion boundary. It remains byte-identical to the canonical skill across every installed
target; the runtime package is distribution, not a parallel doctrine authority.

## 260815-DAG-L15 Review-Doctrine

The Three-Party Loop paragraph now makes review independence explicit: the reviewer seat is never
the author/implementer seat itself (no self-review of one's own leaf), and every requirement
verdict must cite evidence of the requirement's class — rendering/visibility needs mounted-UI
proof, scheduling/ordering needs operation-level proof, data-model needs artifact-level proof.
Evidence of the wrong class is verdict laundering, not a pass.

## M38 Per-Requirement Acceptance Projection

This installed file is the synchronized projection of the canonical exact-set acceptance contract.
It requires one worker evidence envelope and one independent reviewer adjudication for every stable
requirement ID, rejects aggregate completion, and keeps the durable-evidence promotion hold point
separate. It owns no package-local variant of that doctrine.
Approved packets are immutable version-addressed files and carry the durable corpus ruling that
every downstream seat verifies before accepting evidence.

## M40-M45 Requirement Attempt Journal Projection

This packaged copy now carries immutable candidate-bound worker attempts, separate independent
reviewer records, closed failure classes, owner-recorded bounded invalidation, and
leaf-authoritative/rebuildable non-gating master summaries. The canonical root skill remains the
only doctrine owner.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.

## CCR-L42 current candidate

The lifecycle doctrine now distinguishes baseline from fix-verification review, seals issue IDs, forbids outside-list review resets, and places atomic-child route review at canonical-master integration. Three rounds are the ordinary maximum; any extra round requires explicit developer authorization.

## 260915-CAPS-L1 Consolidation — Where The Former Router Sections Went

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation scripts/sync-skills.py:204-205 in the row 91 of this card; the repetition added no pooled evidence
The router was rewritten from a 620-line spine that doubled as the doctrine home into a 179-line
router. This card's older task-delta sections below are **preserved as history**, not deleted; each
one's live rule is still in force and now resolves to a new single home. Read them against this
table rather than as separate current doctrine:

| Former section in this card | Live rule, current home |
| --- | --- |
| `## CCR-R12@v5 Transaction Boundary`; `## L23 Final Candidate Disposition`; `## M38 Per-Requirement Acceptance Projection`; `## M40-M45 Requirement Attempt Journal Projection`; `## 2026-08-27 Attempt Boundary Clarification` | `core/acceptance.md` — completion truth vs owner acceptance, the per-seat handoff-artifact table, per-ID acceptance envelopes, attempt lineage, the durable-evidence promotion hold point |
| `## CCR-L42 current candidate`; `## 260815-DAG-L15 Review-Doctrine` | `core/loop.md` (loop doctrine, tiers, rounds and convergence, criteria catalogs) and `operations/review.md` (the exact baseline / fix-verification mode contract, including atomic-child deferral) |
| `## L23 Dispatch Admission`; `## 260712-TRH-L4 Generated-Copy Doctrine` | `core/authority.md` § Dispatch is one structural transaction, and § Developer-declared task-seat takeover |
| `## 260713-TES-L5 Current Delta — Fact-Relay Supervision Doctrine` | `core/authority.md` § Notify-and-stop is safe by design, and `core/invariants.md` |
| `## 260815-DAG-L2 Synchronized Execution Topology` | `core/invariants.md` (the task-doc → branch → worktree spine) and `roles/orchestrator.md` (the topology, which that role file owns and only there) |
| `### 260713-PHA-L5 Reviewed Hosted Cutover Impact` | Superseded in relevance: the hosted-session readiness/delivery contract is plane-owned and the corpus no longer describes adapter-level liveness |

Note that a card section can stay true while its **cited anchor** stops resolving — that is what the
citation re-open findings on this document report. Where a section above still carried a citation into
the old router body, the citation was rebased to the new home or dropped as superseded.
