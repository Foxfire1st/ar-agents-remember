# 04 — Control Plane: Interaction Back Into The System

| Field | Value |
| --- | --- |
| Topic | Two-way communication: acting on attention items from the dashboard; architecture posture (3.0) |
| Status | Requirement fixed by developer; mechanism design open; **no conservative fixation — MCP/tool changes explicitly allowed** |
| Sources | Issue #43, #53 comments (async direction), developer notes 2026-06-10 |

## Developer Direction (the two fixed points)

1. **The dashboard must not be a pretty toy.** A dashboard you pull up once
   because GitHub showed it, then forget, has no return value. Its value is
   (a) visibility into the inner workings — especially after long
   "things just worked, now it's broken, how do I look at the state?" gaps —
   and (b) a surface to *interact* with the running system. "A cockpit is quite
   useless if all you can do is watch."
2. **Architecture supports the dashboard, not vice versa.** Do not contort the
   dashboard around today's tool assumptions to avoid touching the MCP. Plan
   with tool changes in mind; a jump to **3.0** is justified by the dashboard
   alone. (Repo has 23 stars; discipline yes, compatibility paralysis no.)
   Conservative preservation would mean building "runtime" code on today's
   assumptions and rewriting it anyway.

## The Core Interaction Requirement

When an item asks for attention, the user must be able to **react to it inside
the same UX** — without switching back to whichever harness runs that process.
First-class examples (rough order of value):

- approve / reject / request-revision on a **commit gate** (the canonical case)
- answer a **question** / make a **decision** an agent is blocked on
- acknowledge an **alarm** (master-caution stays lit until acknowledged)
- retry a failed provider setup phase (`retryArgs` already exist in setup-progress)
- cleanup a stale worktree group; restart a degraded provider

## The Hard Problem: The Return Channel

Acting on a gate writes durable state. But the *agent* lives in a harness chat
the system cannot see or push to. Honest options, not mutually exclusive:

1. **Durable gate state + agent polling (the #43 MVP slice).** Gates are
   first-class `input-required` records (on the lifecycle entity, note 01).
   Dashboard POST flips gate state; mutating MCP tools **enforce** gate state
   (e.g. `worktree_closeout_apply` refuses unless approved); the blocked agent
   polls or simply proceeds on next attempt. Pros: durable, auditable, works in
   every harness. Cons: agent latency = poll interval.
2. **Request inbox** (observer branch precedent: "reverse-channel request
   inbox"): dashboard writes request records; skills teach agents to check the
   inbox at phase boundaries. Cheap, harness-agnostic, eventually consistent.
3. **Harness-native push** (e.g. hooks / notifications where a harness supports
   it): optional acceleration layer, never the source of truth.

Lean: (1) is the backbone — gate truth lives in the system, not in any chat.
(2) generalizes it to non-gate interactions. (3) is sugar per harness.

## On A2A

The label was technically off, the *requirement* behind it stands: bidirectional
communication, multiple clients (dashboard, possibly other agents) talking to
the same control plane about the same lifecycle/gate entities. Decision posture:
design the **entities and their state machine first** (lifecycle, gate, request,
event); whether the wire protocol is bespoke HTTP+SSE, MCP-served, or a real A2A
implementation is a later, swappable choice. Do not let a protocol acronym drive
the entity design.

## What 3.0 Plausibly Contains (scope sketch, not commitment)

- Lifecycle entity + ambient id propagation (server-side auto-tagging; note 01)
- Event emission at the `_tool_payload` choke point + skill-side declared events (note 02)
- Gate records as durable, enforced, dashboard-writable state
- The observer/projection component + its serving layer (SSE; note 09 §transport)
- Possibly `read_source_packet` carrying lifecycle-id (note 05)
- Breaking changes allowed: ambient lifecycle attribution server-side (explicit
  `lifecycle_id` only as an override, never model-managed; only
  `switch_lifecycle` carries a target), response envelopes gaining attribution,
  contract front-matter v2

## Invariants (must survive 3.0)

- **Implementation approval ≠ commit approval** — the dashboard makes gates more
  convenient, never weaker. Every gate flip is attributed (who/when/from where)
  and append-only in history.
- Mutating tools enforce gate state server-side; UI affordances are never the
  enforcement (precomputed action availability, note 02 §4).
- Local-first: this is a cockpit for the developer's own machine; no cloud
  dependency. (Auth story for localhost: open question, note 11.)
