# core/loop.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The **three-party loop doctrine** — its single home. OWNER → BUILDER → REVIEWER → owner at every
level that owns work, the review tiers, the round model, the criteria-catalog binding, and the
requirement-compilation gate that precedes task topology.

## Code Commentary

### Logic

The opening rule is the separation that makes the loop work: **the owner never self-approves, the
builder never lands, the reviewer never decides — verdicts are evidence.** The level table assigns owner,
builder, and reviewer per altitude (leaf, master, portfolio plan).

`## Review is opt-in and explicit` states that independent route review runs **only** when the developer
or the approved task/role brief requests it and that closeout and integration never require or launch it;
every review is dispatched with an explicit `reviewMode=baseline` or `reviewMode=fix-verification`, and
independence requires **another agent**, never builder self-review. Evidence must match the requirement's
class — evidence of the wrong class is verdict laundering, not a pass.

`## Complexity-scored tiers` scores blast radius × novelty × size into `direct`, `builder-verified`, or
`full loop`, records the leaf's loop mark on the leaf doc with a decision-log entry, and states that the
knobs tune depth but **never create a review when none was requested**. `## Rounds and convergence` caps a
governed review at three rounds, restricts successor rounds to the sealed listed issues, and requires
explicit developer authorization for any further round.

`## Criteria catalogs`, `## Per-level agent sets`, and `## Requirement compilation precedes task topology`
complete the block: the baseline runs its type's standing catalog under the promotion ratchet, each level
runs its loop with its own configured agent set, and every independently falsifiable obligation becomes a
stable-ID + version packet before any task document exists.

### Conventions

Role files reference this file; they do not restate it. A change to the loop rule belongs here and
nowhere else.

### Invariants And Boundaries

- The owner never self-approves; the builder never lands; the reviewer never decides.
- Review is created only by an explicit request — never by a closeout or integration step.
- A governed review has at most three rounds; extra rounds need explicit developer authorization.
- Reviews 2 and 3 verify only the original listed issues; an outside-list matter goes to the developer.
- Requirement compilation precedes task topology, and a review cannot pass with a rejected requirement.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

| The owner/builder/reviewer separation and the per-altitude table. | `# Core — The Three-Party Loop (one home — this file owns the loop doctrine)` | skills/l-01-agent-lifecycles/core/loop.md:1-15 |
| Review is opt-in and explicit, and independence requires another agent. | `## Review is opt-in and explicit` | skills/l-01-agent-lifecycles/core/loop.md:17-26; skills/l-01-agent-lifecycles/core/loop.md:14-14 |
| The three review tiers and the rule that knobs never create a review. | `## Complexity-scored tiers (per leaf, at dispatch, when review is requested)` | skills/l-01-agent-lifecycles/core/loop.md:28-49; skills/l-01-agent-lifecycles/core/loop.md:25-25 |
| The three-round cap, the convergence rule, and the simple review rule. | `## Rounds and convergence` | skills/l-01-agent-lifecycles/core/loop.md:51-83; skills/l-01-agent-lifecycles/core/loop.md:46-46 |
| The criteria-catalog binding and the promotion ratchet. | `## Criteria catalogs (the reviewer as test bench)` | skills/l-01-agent-lifecycles/core/loop.md:85-93; skills/l-01-agent-lifecycles/core/loop.md:78-78 |
| Requirement compilation precedes task topology; packets are version-addressed and cold-readable. | `## Requirement compilation precedes task topology` | skills/l-01-agent-lifecycles/core/loop.md:99-115; skills/l-01-agent-lifecycles/core/loop.md:94-94 |

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
