# l-01-agent-lifecycles/roles/architect.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/architect.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T17:40+02:00 |
| lastVerifiedCommitHash |                                            `cff3e8f9a64258ea3e7d3007e2153b22c01e273b`|
| lastVerifiedCommitDate |                                            2026-07-14T14:23:24+02:00|
| governingOverview      | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The portable **architect** lifecycle: the developer-facing owner seat for the `l-01-agent-lifecycles`
stack. It owns the design conversation, drawing-board rounds, decision pacing, and durable rulings
back to backend seats. It is a sync-propagated (`scripts/sync-skills.py`) package-data copy of the
canonical `skills/l-01-agent-lifecycles/roles/architect.md`.

## Code Commentary

### Logic

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [architect.md](agents-remember/skills/l-01-agent-lifecycles/roles/architect.md) |
| The l-01 spine that registers architect as the developer-facing owner seat and owns role-seat immutability. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md) |
| The backend orchestrator seat that receives architect dispatches and returns developer-worthy items through the relay. | n/a | [orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md) |
| The design hat the architect wears inline when shaping intent or task docs. | n/a | [designer.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/designer.md) |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## 260712-TRH-L4 Generated-Copy Doctrine

This sidecar describes the generated runtime copy, not canonical ownership. The source is synchronized from the canonical l-01-agent-lifecycles doctrine by the skill-sync process. L4 defines spawned-unbriefed → harness-ready → briefed: spawn is creation only, exact-session readiness proves the target harness is ready, and one durable dispatch-brief advances the seat only with delivered plus harness-log-confirmed proof. Spawned-only or not-ready is not active work; sessionCommands remain launch configuration and promptKeywords apply once after readiness.


### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History
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
