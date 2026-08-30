# l-01-agent-lifecycles/templates/architect-brief.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/architect-brief.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T12:04+02:00 |
| lastVerifiedCommitHash |  `f9f92ca793811b6cb738d7e302dfecdf8636e96e`|
| lastVerifiedCommitDate |  2026-08-30T14:26:46+02:00|

## Purpose

Packaged runtime copy of the canonical architect dispatch packet. The root
`skills/l-01-agent-lifecycles/templates/architect-brief.md` owns the content;
`scripts/sync-skills.py` installs and checks this artifact byte-for-byte.

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

- 2026-08-30T12:04+02:00 — 260821-ARSPAWN-L3 created onboarding for the packaged architect brief.
  Verification metadata remains blank until governed closeout stamps the first source commit.
