# l-01-agent-lifecycles/templates/architect-brief.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

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

## Evidence

### Docs References

No external domain source governs this synchronized projection.

### Repo-Internal References

- The packaged packet carries the same one-call launcher contract. [1]
- The hosted child-authority and no-fallback boundary is embedded in the brief. [2]
- The canonical skill tree is synchronized into package data and harness mirrors. [3]

### Cross-Repo References

No sibling-repository contract defines this synchronized projection.
