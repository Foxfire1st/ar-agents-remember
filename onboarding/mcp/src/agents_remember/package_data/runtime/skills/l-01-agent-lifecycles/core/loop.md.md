# core/loop.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/core/loop.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `997305a9ced4caea67edb826224bf0351264fd56` |
| lastVerifiedCommitDate | 2026-09-17T19:54:27+02:00|
| governingOverview      | `../../../../../../../overview.md` |

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

## Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| The owner/builder/reviewer separation and the per-altitude table. | `# Core — The Three-Party Loop (one home — this file owns the loop doctrine)` | skills/l-01-agent-lifecycles/core/loop.md:1-15 |
| Review is opt-in and explicit, and independence requires another agent. | `## Review is opt-in and explicit` | skills/l-01-agent-lifecycles/core/loop.md:17-26 |
| The three review tiers and the rule that knobs never create a review. | `## Complexity-scored tiers (per leaf, at dispatch, when review is requested)` | skills/l-01-agent-lifecycles/core/loop.md:28-49 |
| The three-round cap, the convergence rule, and the simple review rule. | `## Rounds and convergence` | skills/l-01-agent-lifecycles/core/loop.md:51-83 |
| The criteria-catalog binding and the promotion ratchet. | `## Criteria catalogs (the reviewer as test bench)` | skills/l-01-agent-lifecycles/core/loop.md:85-93 |
| Requirement compilation precedes task topology; packets are version-addressed and cold-readable. | `## Requirement compilation precedes task topology` | skills/l-01-agent-lifecycles/core/loop.md:99-115 |

## Cross-Repo References

No sibling-repository contract defines this instruction file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **dead governing-overview body link repaired, and the field brought into agreement with it.** The field named `../../../../../../../overview.md` — which resolves, but only under the onboarding root rather than against this card's own route — while the body link named `../../../../../overview.md` and resolved card-relative to nothing, so a reader clicking it landed nowhere and the two declarations disagreed. Both now name `../../../../../../../overview.md`, the route-local overview of this card's own directory, so the field and the link agree by construction. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-09-17T12:55+02:00 — 260915-CAPS-L14 curator: **D3 dead governing-overview link repaired.** This card's `governingOverview` was one directory level short, so it resolved to a path that does not exist instead of the `mcp/` route overview. The card directory sits seven levels below `onboarding/`, so seven `../` steps reach `onboarding/` and the correct target is `../../../../../../../overview.md` (→ `onboarding/mcp/overview.md`). Reversed here: `../../../../../overview.md` (which resolved to the nonexistent `mcp/src/agents_remember/overview.md`) or `../../../../../../overview.md` (→ the nonexistent `mcp/src/overview.md`) → **`../../../../../../../overview.md`**. The body's own `[mcp/overview.md](…)` link was re-pointed with it. No prose, anchor, range or verification stamp was otherwise changed.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: created this card for `skills/l-01-agent-lifecycles/core/loop.md` — a file added by the role-instruction corpus consolidation. The canonical source is a shared core block composed into every role capsule (loop).; the packaged copy is produced by `scripts/sync-skills.py` and is not hand-edited. Verification metadata is left at the leaf base commit because the source is uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
