# skills/l-01-agent-lifecycles/templates/architect-brief.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/templates/architect-brief.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T12:04+02:00 |
| lastVerifiedCommitHash |  `f9f92ca793811b6cb738d7e302dfecdf8636e96e`|
| lastVerifiedCommitDate |  2026-08-30T14:26:46+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

## Governing Overview

[lifecycle overview](../overview.md)

## Purpose

This is the canonical, self-contained session start compiled by an identity-free developer-facing
launcher for the architect of one canonical sprint. It replaces fixture prose and caller-visible
spawn/readiness/brief sequencing with one exact `dispatch_agent` request.

## Code Commentary

### Logic

The launcher fills every placeholder from current durable sprint truth, then supplies the canonical
sprint document, role `architect`, and the complete bytes in one public call. Absence of
plane-injected hosted identity selects ambient-launcher authority; the request has no caller field.
The control plane chooses the settings-owned profile, creates the canonical seat, proves readiness,
and pins the exact brief before returning `dispatched` or `dispatch-queued`. Either result is a
handoff point, never permission to send another brief.

The packet carries canonical scope, developer rulings, preservation boundaries, trust and retrieval
facts, and the architect's opening move. It also tells the newly hosted architect that subsequent
child dispatches are plane-authorized and that a plane refusal must never fall back to ambient.

### Conventions

- Fill every placeholder immediately before dispatch from durable task, requirement, decision,
  contract, and report artifacts.
- Use the sprint task document, never a branch, leaf, runtime id, or transcript link, as the seat
  address.
- The canonical packet is authored here and synchronized into package and harness skill trees.

### Invariants And Boundaries

- The launcher calls `dispatch_agent` once and never calls an internal session primitive.
- The exact brief is the architect's entire session start; no second capsule is synthesized later.
- Target-document, role-altitude, settings, launch, lineage, and persistence refusals remain
  actionable refusals, not fallback triggers.
- Semantic decisions remain agent/developer-owned; the template only transports durable truth.

## Docs References

No external domain source governs this repository-owned dispatch packet.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The launcher submits one complete identity-free architect dispatch. | `# Template — Architect Brief` | skills/l-01-agent-lifecycles/templates/architect-brief.md:1-10 |
| The resulting architect uses plane-hosted child authority without ambient fallback. | "This architect seat is now plane-hosted." | skills/l-01-agent-lifecycles/templates/architect-brief.md:54-60 |
| Placeholder, canonical-address, durable-handoff, and refusal recovery rules are explicit. | "Compiler notes for the launcher." | skills/l-01-agent-lifecycles/templates/architect-brief.md:72-84 |

## Cross-Repo References

No sibling-repository contract defines this template.

## Update History

- 2026-08-30T12:04+02:00 — 260821-ARSPAWN-L3 created the canonical architect-brief onboarding.
  Verification metadata remains blank until governed closeout stamps the first source commit.
