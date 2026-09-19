# l-01-agent-lifecycles/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `d0c1d1cfa9b576fd117ac2a0c05c5defe0089678` |
| lastVerifiedCommitDate | 2026-09-19T12:15:35+02:00|
| governingOverview      | `../../../../../../overview.md` |

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

## Docs References

No external domain documentation is configured for this repository-local lifecycle doctrine.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The packaged source carries the launcher, approval-gated strategist, architect-custody, and parallel-by-default invariants. | `# l-01-agent-lifecycles — The Agent Lifecycles`; `## Which Lifecycle Am I? (the router — exactly three conditions, in order)`; `## The Role Registry` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:6-180 |
| Canonical skills are propagated into package data and harness mirrors by the sync script. | `CANONICAL_SKILLS`; `sync_targets`; `TARGETS`; `sync_target`; `check_targets` | scripts/sync-skills.py:15-15; scripts/sync-skills.py:43-55; scripts/sync-skills.py:136-177; scripts/sync-skills.py:179-191; scripts/sync-skills.py:204-205 |
| The packaged source carries the launcher, approval-gated strategist, and parallel-by-default invariants as pointers, not as doctrine. | `# l-01-agent-lifecycles — The Agent Lifecycles`; `## Which Lifecycle Am I? (the router — exactly three conditions, in order)`; `## The Role Registry` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:6-6; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:24-24; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:67-67 |
| The router declares its own boundary — it routes, and every rule lives in exactly one other file — and names the ten-role registry plus the ambient launcher as a routing condition rather than an invented role. | `This file routes. It does not carry doctrine.`; `## Composition Map (how a capsule is assembled)`; `Exactly ten roles.` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:13-13; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:89-89; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:82-82 |
| The tenth registry row this leaf added, and the reachability sentence it carries. | "**bootstrap**"; "reachable before any task document exists" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:80-80 |
| Doctrine moved out of the router: shared rules to `core/`, procedures to `operations/`, rationale and superseded rulings to `reference/`, and routing metadata to the prose-free manifest. | `## Companion Files`; `## settings.json Orchestration Block` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:126-144; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:162-175 |
| The enabled corpus stays self-contained: the shipped check fails on a role that leaks a sibling's duties, on a manifest that names a missing source, and on any relative path the corpus cites that does not resolve. | `SANCTIONED_SIBLING_REFERENCES`; `test_every_role_source_is_a_capsule_shaped_function`; `test_manifest_reports_a_missing_source_instead_of_accepting_it`; `test_every_relative_path_the_corpus_cites_resolves` | mcp/tests/test_role_instruction_corpus.py:105-116; mcp/tests/test_role_instruction_corpus.py:409-494; mcp/tests/test_role_instruction_corpus.py:495-535; mcp/tests/test_role_instruction_corpus.py:536-559 |

## Cross-Repo References

No sibling repository evidence is needed for this doctrine file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

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

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: `# l-01-agent-lifecycles — The Agent Lifecycles`; `## Which Lifecycle Am I? (the router — exactly three conditions, in order)`; `## The Role Registry` repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:6-180; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:24-66; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:67-88. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. SOURCE UNCHANGED BY THIS LEAF; card prose falsified by CAPS-R18@v1. Updated the lifecycle-contract paragraph so the curator's duty reads as the complete memory-quality operation carried as a prerequisite rather than scoped checks.
- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: **body rebased on the tenth role this leaf added**
  (`CAPS-R13@v1`). The registry is now ten roles and nine operations: the Purpose's registry and
  operation counts, the Logic's launcher sentence ("not a tenth role" → "not a role") and the frozen
  operation-vocabulary count, and the Invariants' registry count were all updated, and the new
  `bootstrap` row is recorded — the new user's first-hour seat for one repository, reachable before
  any task document exists, and a **free agent** rather than a fourth routing condition. Added the
  invariant that `bootstrap` must not become a fourth condition and that its absent task altitude is
  its shape. Every Repo-Internal range was re-derived against the 180-line router (the previous ranges
  were measured against the 179-line pre-extension file, and the `Exactly nine roles.` anchor no longer
  existed at all — it now reads `Exactly ten roles.`), which also cleared this card's
  `citation_anchor_absent_from_range` family. Verification metadata is left at the leaf base commit
  because the source is uncommitted — the governed closeout stamps the real code commit.
- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: **governing-link repair, and a correction of the L1 entry below.** This card's `governingOverview` and its `## Governing Overview` link had been changed by 260915-CAPS-L1 from `../../../../../../overview.md` (six steps) to `../../../../../overview.md` (five), reasoning that the shorter path reached the nearest route-local overview. Both paths were tested against the filesystem on this pass and the reasoning is inverted: `onboarding/mcp/src/agents_remember/package_data/runtime/` is the directory that exists — the `skills/` segment does not — so this card's directory is **five** real levels below `onboarding/`, and the six-step path resolves to `onboarding/mcp/overview.md`, which is exactly what the link text names. The five-step path resolves to `onboarding/mcp/src/overview.md`, which does not exist. Metadata field and link are both corrected back to `../../../../../../overview.md`. Found while creating this leaf's cards for the same `l-01-agent-lifecycles` directory, whose governing links carried the identical defect. No body content changed and no verification stamp advanced — the source is uncommitted, so the stamp stays closeout-owned.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **body rewritten for the corpus consolidation.**
  The canonical `skills/l-01-agent-lifecycles/SKILL.md` became a 179-line router (was 620) and gave up
  all doctrine: `core/` (six shared blocks), `operations/` (eight operation blocks),
  `reference/rationale.md` + `reference/rulings.md`, and the prose-free `composition-manifest.json`
  now hold the rules this card used to describe through the router. Updated Purpose (the
  routes-but-carries-no-doctrine boundary), Logic (three routing conditions, the decision edge cases,
  the composition map and its frozen eight-operation vocabulary, the settings section's deliberate
  removal of the worked JSON example), Conventions (adding a rule here re-creates the removed
  duplication), Invariants (nine-role registry, no cross-role reading, the shipped check that fails on
  a leaked sibling reference), and Repo-Internal References (the old `:6-416` citation replaced by
  current anchors plus rows for `mcp/tests/test_role_instruction_corpus.py` and the sync-script
  targets). Added the consolidation map above so the preserved task-delta sections resolve to their
  live homes. **Metadata repair:** this card's `governingOverview` pointed at
  `../../../../../../overview.md`, which resolves to the repository root overview while its own link
  text said "MCP package overview"; corrected to `../../../../../overview.md`
  (`onboarding/mcp/overview.md`, the actual nearest route-local overview for this generated tree).
  Verification metadata remains closeout-owned — the source is uncommitted, so no stamp was advanced
  and no commit hash was invented.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): corrected the range
  quoted in this card's own earlier entry — the added super-branch note occupies `:596-598`, not
  `:592-595`. The substantive router/registry citation (`:6-416`) still holds. Verification metadata
  remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md` changed since
  the recorded verification commit. Re-read the card against the frozen on-disk source and
  re-checked its claims and cited ranges: nothing this card asserts is falsified by the change, so
  no wording changed. Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (a super-branch note was added at `:596-598`). Re-read the card
  against the current source: its claims cite the router/registry sections at `:6-416`, which are
  unchanged, and no claim depends on the added paragraph. No wording changed; verification metadata
  remains closeout-owned.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: The lifecycle doctrine now distinguishes baseline from fix-verification review, seals issue IDs, forbids outside-list review resets, and places atomic-child route review at canonical-master integration. Three rounds are the ordinary maximum; any extra round requires explicit developer authorization.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: synchronized the
  malformed-role refusal and polymorphic reviewer parent contract into the packaged onboarding.
  Verification remains closeout-owned.

- 2026-08-30T12:57+02:00 — 260821-ARSPAWN-L3 review correction: synchronized the
  canonical-seat convergence and no-manual-replacement boundary for explicit task-seat takeover.
  Verification remains closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 synchronized the one-call architect launcher,
  separated ordinary bootstrap from explicit named-role takeover, recorded resumable lineage
  conflicts, and kept structural role rows outside settings. Verification remains closeout-owned.

- 2026-08-28T11:32+02:00 — No content impact: synchronized projection payload changed with the
  canonical one-primary requirement doctrine; projection ownership and byte-identity rules remain
  unchanged.

- 2026-08-27T22:15+02:00 — Synchronized the pre-handoff correction versus post-handoff rejection
  contract from canonical lifecycle/task doctrine.

- 2026-08-27T21:53+02:00 — Synchronized review-handoff-only attempts, separate protocol events,
  and lightweight content-addressed journal semantics from canonical lifecycle doctrine.

- 2026-08-27T18:06+02:00 — M40-M45: synchronized the complete Requirement Attempt Journal contract
  and explicit non-gating summary boundary from canonical sources.

- 2026-08-27T14:04+02:00 — Clarified the synchronized M39 projection with immutable
  version-addressed packets and packet-local durable corpus approval.
- 2026-08-27T13:32+02:00 — M39@v1: requirement compilation now precedes task topology; canonical
  packets carry stable ID + version, pass a transcript-free cold read, and receive developer corpus
  approval before filtered task projection. Downstream evidence remains bound to that exact
  revision. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 — M38: recorded the synchronized per-ID acceptance contract and its
  separation from durable-evidence promotion. Verification metadata stays pinned until governed
  closeout stamps the PDLS commit.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15: the three-party-loop paragraph now states the reviewer
  seat is never the author seat and requirement verdicts must cite their evidence class
  (mounted-UI / operation-level / artifact-level proof). Verified at code commit de3a0fd9.
- 2026-08-15T04:32+02:00 — 260815-DAG-L2: synchronized dependency-aware execution topology and
  its authority/quality-altitude rules into the packaged lifecycle root. Verification remains
  closeout-owned.
- 2026-08-14T06:32+02:00 — L23 synchronized runtime doctrine: the lifecycle roof carries
  Dagger-only acceptance, manager lineage preflight, and candidate-bound independent route review
  before curation or lifecycle exit. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented lineage admission in the packaged dispatch sequence; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `SKILL.md` as the exact synchronized runtime artifact of its current canonical document/role contract; removed obsolete leaf-key and runtime-id ownership implications.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded sprint-qualified command-seat dispatch and the
  all-subordinate liveness contract in the packaged lifecycle skill. Verification metadata remains
  pinned until closeout stamps the code commit.

- 2026-08-09T13:59+02:00 — 260713-TES-L5 curator completion round 2: refreshed this synced
  runtime copy for the judgment-demolition doctrine (fact-relay supervision; ladder retired);
  verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-02T16:46+02:00 — 260731-EFA-L6 curator W1-B03: repaired 2 citation rows with exact anchors and source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-15T23:16+02:00 — 260714-ACPUI-L2 curator: documented the synchronized dynamic
  model-gated launch doctrine, complete role examples, native per-harness launch channels,
  provenance-only spawn env, and the no-normalized-paste boundary; final-audited the nearest MCP
  governing overview backlink. Verification metadata remains pinned until closeout stamps the L2
  code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-10T15:48+02:00 — 260707-HFX2-L17 generated-runtime doctrine delta: documented
  task-seat identity as `(qualified leaf key, seat role)`, made developer-declared takeover pass
  and verify the claimed role with the qualified leaf, and recorded same-pair-only live collision.
  Sync-propagated bundle copy; verification metadata remains pinned until closeout stamps the L17
  commit.

- 2026-07-10T02:39+02:00 — HFX3/L14 combined curation: reconciled the free-chat launcher,
  settings-owned architect spawn, propose-first strategist approval, sanctioned-skip Job O path,
  architect terminal custody, and dependency-graph parallel-by-default invariant. Added the
  governing overview and required reference/boundary sections. Verification metadata remains
  pinned until closeout stamps the eventual two-parent code commit.

- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 (spawn settings authority): the lifecycle skill spine now
  states that ordinary spawned seats use settings as the spend surface, with role/level declared on
  `spawn_agent_session`; legacy caller spend fields and maintained harness-native spend/env keys
  refuse with `spend-override-unsupported`. Sync-propagated bundle copy of the canonical skill.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L10 commit.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L5 (doctrine rewrite, active vigilance → passive
  process-and-ack): Shared Invariants section gains the new "Notify-and-stop is safe by design"
  paragraph — ending a turn once the artifact is written is never a liveness gap because the
  HFX2-L2 sweep + HFX2-L4 escalation ladder supervise silence; states the watcher ban
  (uniform-mechanism ruling 2026-07-07) and the passive-duty inversion every role file now carries.
  Doctrine-only change set (5 canonical `skills/` files, propagated by `scripts/sync-skills.py` to 9
  downstream package copies, 0 Python); sync-propagated bundle copy of the canonical
  `skills/l-01-agent-lifecycles/SKILL.md`. Verification metadata pinned until closeout stamps the
  260707-HFX2-L5 commit.

- 2026-07-08T15:45+02:00 — 260707-HFX2-L7 doctrine refinement: Developer Clarification Triage now
  explicitly reads the active queue before choosing note-only handling; a small clarification that
  plainly fits the same task/current diff is a strong immediate-implementation signal, true future
  queue is recorded durably, and unclear fit asks the developer directly. Sync-propagated bundle
  copy of the canonical `skills/l-01-agent-lifecycles/SKILL.md`.

- 2026-07-08T15:27+02:00 — 260707-HFX2-L6 (task-seat takeover + delegated authority
  doctrine): added Developer-Declared Task-Seat Takeover, Developer Clarification Triage, and
  Delegated Series Authority sections to the lifecycle router. A developer-declared role takeover
  anchors on the named task leaf and verifies dashboard terminal attachment before lifecycle work.
  Close/current/small developer clarifications that fit the active leaf are implemented now rather
  than filed as future notes. Accepted orchestrated series authority lets owning seats close out,
  integrate, finalize, and clean up subordinate edges without repeated developer formality, while
  final super/PR-carryover, raised human-pinned gates, scope changes, red checks outside scope, and
  quo-vadis decisions remain developer stops. Doctrine-only change set propagated by
  `scripts/sync-skills.py`; no runtime attachment path changed. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L6 commit.

- 2026-07-08T02:10+02:00 — 260707-HFX-L11 curator activation: Companion Files template registry
  gains `curator-brief` (new file, R1/R4) with its header-consistent description. Doctrine-only
  change set (7 canonical `skills/` files across 6 edits + 1 new template, synced to 9 mirrors, 0
  Python touched); sync-propagated bundle copy of the canonical `skills/l-01-agent-lifecycles/SKILL.md`.
  Verification metadata pinned — no commit yet on `ar/260707-hfx-l11-curator-activation`
  (working-tree change, synced onto the landed HFX-L7 base).

- 2026-07-08T01:00+02:00 — 260707-HFX-L7 (provider degradation protocol): the role registry table
  gains the `system-specialist` row (backend provider-degradation investigator; spawn value
  `system-specialist`; points at the new `roles/system-specialist.md`); frontmatter `description`
  and the Companion Files sentence both now say nine role lifecycles (was eight); the escalation
  ladder bullet gains a standalone `system-specialist -> orchestrator` clause beside the existing
  worker->manager->orchestrator->architect->developer chain; the settings-block worked example
  gains a `system-specialist` roles entry (`claude`/`fable`/`high`). Sync-propagated bundle copy of
  the canonical `skills/l-01-agent-lifecycles/SKILL.md`. Verification metadata pinned until
  closeout stamps the HFX-L7 commit.
- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: added curator to the
  l-01 registry/settings example as the fresh per-leaf onboarding writer, and recorded the
  manager -> builder -> reviewer -> curator closeout chain. Sync-propagated bundle copy.
  Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: added the
  architect role to the registry and router; condition 3 now routes developer-facing sessions
  to `roles/architect.md`; condition 2 is fresh-session role briefs only; the orchestrator is
  a spawned backend seat; escalation is worker -> manager -> orchestrator -> architect ->
  developer; dashboard-owned role-seat immutability and the minimal one-at-a-time decision-item
  relay over the existing operator inbox are doctrine. Sync-propagated bundle copy. Verification
  metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): the settings.json Orchestration
  Block example gains the `strategist` free-form row (`effort: ultracode` + `promptKeywords`), the
  `reviewer` economics row, and the `rolesPerLevel` block; the roles comment names the three-layer
  knob model (validated harness/model/effort · free-form launchArgs/promptKeywords/sessionCommands);
  the as-built paragraph becomes L13+L16 — the knob chain now APPLIES at the harness boundary
  (per-harness argv mapping via the effective registry, dispatch-time effort refusal, the session
  vehicle for `ultracode`, the `level` dispatch input with provenance, `orchestration.harnesses`
  openness) with `docs/reference/harnesses.md` as the manual. Sync-propagated bundle copy of the
  canonical skill. Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-06T22:56+02:00 — 260703-L13 (settings unification): the settings.json
  Orchestration Block section re-homes the knobs to the global agentic settings file with
  repo-local override (fixing the authority-file contradiction), the example uses registry
  harness ids and gains `orchestration.spawn`, and the as-built paragraph documents the
  kernel loader (per-use reads, fail-loud family), the boot-snapshot gateDelegation with
  legacy fallback, and the spawn resolution chain. Sync-propagated bundle copy of the
  canonical `skills/l-01-agent-lifecycles/SKILL.md`. Verification metadata pinned until
  closeout stamps the L13 commit.

- 2026-07-06T17:35+02:00 — 260703-L12 round 2 (L12R-4 ripple): the loop home's direct-tier gloss now names the level's ordinary build channel (hands-on at session scale; the leaf's worker under a manager) instead of the ambiguous "owner implements". Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:35+02:00 — 260703-L12 (three-party loops): the strategist joins the role registry (spawn-first, mandatory pre-run, spawn value `strategist`); a new The Three-Party Loop section becomes the loop doctrine's single home (tiers · 3-full-round cap · delta-verify/builder-resume · convergence rule · quo-vadis · criteria catalogs · per-level agent sets); Companion Files list 10 templates + the `criteria/` catalogs; the settings paragraph documents `orchestration.loops`. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-05T19:55+02:00 - L8 builder cycle 7: Companion Files template registry gains the manager-brief row — all 9 on-disk templates listed (AR4-5). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the takeover pointer names the real section (Profile check (takeover), The Event Loop). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:20+02:00 - L8 seam-ruling remediation (cycle 4): router edge cases written; six signals enumerated; variant rung removed; at-seams flag documented as wired. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 - L8 de-harnessing pass: per-harness variant layer removed from the resolution order; registry overlay mentions dropped. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:15+02:00 - L8 orchestrator routes rework: registry row marks the designer as a hat the orchestrator pulls (separate chair optional); router condition 1 notes AR_SPAWN_ROLE=designer as the same hat in another chair; router condition 3 states solo = the three jobs with hats collapsed, task doc first. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - L9 lifecycle convergence: SKILL.md is now the unified-skill spine (router + minimal frame + shared invariants); body rewritten accordingly; supersedes the two retired skill spines. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T13:16+02:00 — 260703-L6 documented the adversarial seam procedures end to end: manager
  spawn at master-exit, orchestrator spawn at super-exit, `notes/reports/` verdict placement,
  `reviewer-verdict` gate evidence refs, policy-required verdict evidence, and block-to-fix-leaf routing
  back to the owning manager/orchestrator. Verification metadata pinned until closeout stamps the L6
  commit.
- 2026-07-04T13:03+02:00 — 260703-L5 expanded the frame's super integration branch topology from a
  summary into doctrine: super branches from main, masters branch from super, leaves branch from their
  master, C-11 is universal at every edge, dependent managers dispatch only after dependencies
  integrate into super, independent masters reconcile a moved super base, master-to-super integration
  runs in an orchestrator worktree, conflict resolution is either up-front foundation-master extraction
  or post-hoc super-worktree dedup with memory single-siding, leaf moves carry decision-log entries,
  and the final super-to-main PR includes main-memory carry-over plus push. Also recorded the
  260630-derived master finalize/archive and parallel-master reconcile items as sequenced follow-ups,
  not implemented behavior. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-07-04T11:00+02:00 — Created file-level onboarding for the new `l-02-agent-orchestration` skill
  (leaf 260703-L1), the developer-invoked, never-self-spawning frame that houses the five
  orchestration-family jobs via the four thin contact points (context → job selection → housed job
  execution → wrap-up). Captured the frame doctrine, the job registry, the coordination-leaf
  convention, the escalation ladder + orchestrator-only spirit test, the two adversarial seams, the
  gate-delegation doctrine (enforcement deferred to L4), the knob block + per-harness variant
  resolution, the settings.json orchestration schema block (schema doc only; parsing deferred to L4),
  the super integration branch topology summary (full topology owned by L5), the comms protocol
  (substrate implemented in L3), and the credits; noted `spawn_agent_session` is the L2 tool (not yet
  implemented). Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-02-agent-orchestration/SKILL.md`. Verification metadata pinned until closeout stamps the L1
  commit.
