# l-01-agent-lifecycles/roles/architect.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-15T04:32+02:00 |
| lastVerifiedCommitHash | `20cfd54cb0a3d425424afdfbb6d8c97f669cdcc4` |
| lastVerifiedCommitDate | 2026-08-15T05:12:01+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The portable **architect** lifecycle: the developer-facing owner seat for the `l-01-agent-lifecycles`
stack. It owns the design conversation, drawing-board rounds, decision pacing, and durable rulings
back to backend seats. It is a sync-propagated (`scripts/sync-skills.py`) package-data copy of the
canonical `skills/l-01-agent-lifecycles/roles/architect.md`.

## Code Commentary

### Spawn Doctrine And tools.md (260731-EFA-L16)

Two developer rulings landed here. First, the immutability clause now binds role-seat creation to
`spawn_agent_session` explicitly — a role seat is never a native sub-agent — and native sub-agent
fan-out is scoped to the one mode where this seat does hands-on work: solo build under the worker
discipline (developer correction). Once orchestration runs, analysis goes to spawned role seats.
Second, the Opening Move gained a standing read of the resolved `system/tools.md` — as the repo's
tool INVENTORY, not merely the quality gate — phrased generically (whatever test/lint/build/
smoke-check, discovery, and repo-local command notes that repository actually provides), because
the role files ship with the package across repos whose memory layers name different tools
(developer ruling: this role file never named the file at all; the solo-build bullet also names
the wrapper as its checks authority). Third, the drawing-board phase now names its shared
doctrine: `tasks/AGENTS.md` (task-collaboration doctrine) governs HOW the problem gets
decomposed before planning — reviewable reframing (surface request vs deeper objective vs
highest-leverage framing), explicit assumptions/truth gaps/invariants/non-goals, typed evidence
plan, examples before risky change, and an implementation plan derived from the framing sections
rather than substituted for them.

### Logic

The packaged architect lifecycle now arrives as a sprint-local command seat launched by free chat.
Its backend spool-up is scoped to the same repository+sprint binding, so decision custody and
orchestrator ownership cannot drift onto an architect from another concurrent sprint. The
developer-facing launcher remains outside that named-seat identity.

The file defines the HFX-L6 architect/orchestrator split. The initial developer-facing free chat is
a launcher, not this seat; it spawns a clean architect with the settings-owned profile for
role-shaped work. Once spawned, the architect owns the developer conversation and the backend
orchestrator never talks to the developer directly. Opening move:
read workspace instructions, resolve active Agents Remember context, run the trust checkpoint,
read portfolio state plus pending architect-addressed inbox items, and say back state before asking
the developer to decide.

Event routing maps developer shaping to **Design** (wear `roles/designer.md` inline), backend
`decision-item` rows to **Decision relay**, approved portfolio execution to horizontal role spawns,
no-state-change asks to research-only exit, and small unspawned work to architect-only solo/flat
hat-collapse. Since 260707-HFX2-L7, developer clarifications during an active task first run the
shared Developer Clarification Triage rule: if queue context shows the clarification is
close/current/small, the architect folds it into the active task surface and implements under the
current owner hat; if it is future queue, it is recorded durably for later planning; unclear fit is
asked back to the developer directly. Role-seat immutability is explicit: dashboard-owned architect
sessions stay architect; pasted role briefs are refused/escalated through the inbox; roles expand
horizontally by new chats; sub-agents drill vertically for analysis only.

The minimal decision-item relay uses the existing operator inbox, not a new queue schema. Backend
seats post one `messageKind: decision-item` at a time with decision/options/consequences/evidence
refs. The architect presents one item, records the ruling durably in `openQuestions`, decision logs,
or notes, then returns one `messageKind: decision-ruling` row referencing the durable ruling. Vague
items get a clarification row instead of a guessed decision.

The architect can spawn backend roles with refs to durable state (`AR_SPAWN_ROLE=orchestrator`,
`strategist`, `designer`, `manager`, `worker`, `reviewer`). It proposes the strategist pass as a
developer question and never auto-runs it; it likewise proposes the short root when work is truly
tiny. Solo/flat hat-collapse is reserved here:
the architect may wear backend/build hats only when no spawned role owns that work, and
owner-never-self-approves still holds.

### Invariants And Boundaries

- The initial developer-facing session is a free-chat launcher; the spawned architect then owns the
  developer conversation, while the orchestrator remains backend-only.
- Strategist dispatch and the tiny-work short root are explicit developer decisions proposed by
  the architect, never silent defaults.
- Escalation terminal custody belongs to the architect; the developer is an authority, not a row
  address.
- Dashboard-owned role seats are immutable for the session lifetime.
- Decision relay is one item at a time over existing inbox rows; durable ruling comes back before
  backend action.
- Solo/flat hat-collapse is allowed only for the architect owner seat.
- Spawned roles receive durable refs, not transcript state, and never become the architect.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical architect role is defined in the cited source file. | `# Lifecycle — Architect` | skills/l-01-agent-lifecycles/roles/architect.md:1-264 |
| The l-01 spine that registers architect as the developer-facing owner seat and owns role-seat immutability. | "design conversation, decision-item relay, and drawing board" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:99-99 |
| The backend orchestrator seat that receives architect dispatches and returns developer-worthy items through the relay. | `# Lifecycle — Orchestrator` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:1-14; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:22-38; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:429-448 |
| The design hat the architect wears inline when shaping intent or task docs. | `# Lifecycle — Designer` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/designer.md:1-18 |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.

## 260713-TES-L5 Current Delta — Mailbox Custody, Not Ladder Rungs (synced copy)

This synced runtime copy now says rows whose entire owner chain is dead surface to the
architect as a mailbox (the timed escalation ladder is retired), rows land at the architect's
turn boundary (the system acks), and `operator_inbox_consume` is an optional attribution
marker. The developer remains an authority, not an address.

## L23 Thematic Master Recovery

The packaged architect role treats a resumed master falling behind super as a
normal synchronization condition. It routes the contract-addressed recovery
through the backend and retries the same canonical master seat; it does not
invent a “part 2” master or burden agents with commit ancestry.

## 260815-DAG-L2 Planning Authority

The architect requires a complete current `executionGraph` and explicit `executionNature` for
every commanded master before backend execution. It proposes—never auto-dispatches—the strategist,
owns the initial and runtime plan-review loop, and rules the resulting artifact before orchestrator
adoption. Recommending a skip requires a complete plan whose dependency, route, seam,
classification, and priority assumptions remain valid; mere existence is insufficient.

## Update History

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: synchronized explicit topology admission and
  architect-owned strategist/reviewer authority. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented replacement-safe thematic-master sync recovery; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Recorded `architect.md` as a synchronized runtime artifact of the current canonical lifecycle doctrine; it introduces no independent role contract.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: aligned the packaged architect lifecycle with
  sprint-qualified custody and spool-up. Verification metadata remains pinned until closeout
  stamps the code commit.

- 2026-08-09T13:59+02:00 — 260713-TES-L5 curator completion round 2: refreshed this synced
  runtime copy for the custody doctrine (mailbox surface; ladder retired; attribution-only
  consume); verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-05T23:30+02:00 — 260731-EFA-L16 curator: recorded the drawing-board doctrine naming — the Design And Drawing Board section now points at `tasks/AGENTS.md` (task-collaboration doctrine) as the decomposition discipline for the phase: reviewable reframing, explicit assumptions/truth gaps/invariants/non-goals, typed evidence plan, examples before risky change, plan derived from the framing (developer ruling; corrected from an initial whether-a-task-is-needed misreading). Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-05T22:10+02:00 — 260731-EFA-L16 curator: recorded the spawn-doctrine binding (role seats only via `spawn_agent_session`; native fan-out scoped to solo build per the developer correction) and the Opening-Move `system/tools.md` standing read — as the repo's tool inventory, phrased generically because the shipped role files span repos whose memory layers name different tools; widened from the solo-build-only naming after the developer noted tools.md is not just the quality gate. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: restored canonical/package-data source ownership
  citations and removed the unsupported hosted-cutover impact section.
- 2026-08-01T17:40+02:00 — 260731-EFA-L4 markdown repair: removed a leaked diff marker. A body section (heading plus paragraph) had been pasted into this Update History list on 260712-TRH-L4 carrying the diff's `+`. Because `+##` has no space after the plus, markdown rendered it as literal text, so the heading was not a heading and the surrounding bullet list was broken. The same section already existed correctly earlier in the file; where the pasted copy said more, its wording was promoted into that section before the paste was deleted. No claim changed. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-10T02:39+02:00 — HFX3 retro curation: reconciled the architect card with the free-chat
  launcher, settings-owned clean spawn, propose-first strategist and short-root questions, and
  architect terminal custody. Added the governing-overview backlink. Verification metadata remains
  pinned until closeout stamps the eventual two-parent code commit.

- 2026-07-08T15:45+02:00 — 260707-HFX2-L7 doctrine refinement: event routing now tells the
  developer-facing architect to run Developer Clarification Triage before choosing note-only
  handling. Close/current/small clarifications fold into the active task and implementation; future
  queue is recorded durably; unclear fit asks the developer which route they intend.
- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: created onboarding
  for the new developer-facing architect lifecycle, including design ownership, role-seat
  immutability, one-at-a-time decision-item relay over the existing operator inbox, backend
  role spawning, and architect-only solo/flat hat-collapse. Verification metadata is blank until
  closeout stamps the first commit containing this new package-data source file.
