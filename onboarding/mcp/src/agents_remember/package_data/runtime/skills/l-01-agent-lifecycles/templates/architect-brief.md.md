# l-01-agent-lifecycles/templates/architect-brief.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/architect-brief.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash |  `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03`|
| lastVerifiedCommitDate |  2026-09-17T10:09:37+02:00|
| governingOverview | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../overview.md)

## Purpose

Packaged runtime copy of the canonical architect dispatch packet. The root
`skills/l-01-agent-lifecycles/templates/architect-brief.md` owns the content;
`scripts/sync-skills.py` installs and checks this artifact byte-for-byte.

The canonical template gained the single-source marker in 260915-CAPS-L1: **it feeds inputs and does not
author rules** — the architect's duties live in `../roles/architect.md`, the launcher's in
`../core/launcher.md`, and the dispatch transaction in `../core/authority.md`, and if a value in the
packet disagrees with those files they win. The rows carry this sprint's *values* for those contracts.

## Code Commentary

### Logic

An identity-free launcher fills the packet from current durable sprint truth and calls
`dispatch_agent` once with the canonical sprint document, role `architect`, and these complete
bytes. The control plane selects the settings profile, creates and readies the seat, and pins the
brief before returning a durable result. The hosted architect then uses plane authority for
documented children; a plane refusal never retries through ambient mode.

### Conventions

Edit the canonical template and run the skill synchronization mechanism. Installed runtimes must
receive the exact packet, not a package-local launcher variant.

### Invariants And Boundaries

- This packaged artifact remains byte-identical to the canonical template.
- The public request carries the target address and exact brief, never caller or runtime identity.
- `dispatched` and `dispatch-queued` are both durable handoff states; no second brief is sent.
- No compatibility filename, session primitive, or plane-to-ambient fallback exists.

## Docs References

No external domain source governs this synchronized projection.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The packaged packet carries the same one-call launcher contract. | `# Template — Architect Brief` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/architect-brief.md:1-10 |
| The hosted child-authority and no-fallback boundary is embedded in the brief. | "This architect seat is now plane-hosted." | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/architect-brief.md:54-60 |
| The canonical skill tree is synchronized into package data and harness mirrors. | `CANONICAL_SKILLS`; `sync_targets` | scripts/sync-skills.py:15-15; scripts/sync-skills.py:195-203 |

## Cross-Repo References

No sibling-repository contract defines this synchronized projection.

## Update History

- 2026-09-17T12:55+02:00 — 260915-CAPS-L14 curator: **D3 dead governing-overview link repaired.** This card's `governingOverview` was one directory level short, so it resolved to a path that does not exist instead of the `mcp/` route overview. The card directory sits seven levels below `onboarding/`, so seven `../` steps reach `onboarding/` and the correct target is `../../../../../../../overview.md` (→ `onboarding/mcp/overview.md`). Reversed here: `../../../../../overview.md` (which resolved to the nonexistent `mcp/src/agents_remember/overview.md`) or `../../../../../../overview.md` (→ the nonexistent `mcp/src/overview.md`) → **`../../../../../../../overview.md`**. The body's own `[mcp/overview.md](…)` link was re-pointed with it. No prose, anchor, range or verification stamp was otherwise changed.

- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **first real body update since creation.** The
  canonical architect brief gained the single-source marker naming `../roles/architect.md`,
  `../core/launcher.md`, and `../core/authority.md` as the rule owners; this card's Purpose now records
  that marker and the values-vs-rules boundary. **Metadata repair:** `governingOverview` was absent from this card (the c-05 content model requires the field and its `## Governing Overview` section); added as `../../../../../overview.md`, the `onboarding/mcp/overview.md` route-local overview that governs this generated tree. Verification metadata remains closeout-owned — the source is uncommitted, so no stamp was advanced and no commit hash invented.


- 2026-08-30T12:04+02:00 — 260821-ARSPAWN-L3 created onboarding for the packaged architect brief.
  Verification metadata remains blank until governed closeout stamps the first source commit.
