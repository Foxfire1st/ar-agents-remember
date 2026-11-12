# mcp/src/agents_remember/memory/carryover_apply.py

## Governing Overview

[Memory area overview](overview.md)

## Purpose

Implements converted carryover’s worktree-only transaction after the caller admits and prepares selected units.

## Code Commentary

### Payload confinement

Only onboarding Markdown/JSON pairs and schema record units enter the write extent. Paths must be canonical relative paths; derived indexes, hidden parents, symlinks and nonregular files are refused. Record JSON may omit an absent Markdown companion; onboarding units may not.

### Conflict and retry safety

Already-equal bytes are accepted even if dirty or staged. Divergent local changes and existing differing records are conflicts. The engine rechecks the complete submitted payload batch before writes and refuses that batch on any conflict; caller-side candidate skipping is a separate boundary.

### Validation and restoration

Apply writes prepared units, regenerates route indexes with explicit target storage, validates the exact tree against official code and the paired memory base (converting an old-format base through the existing converter), and splits refusing from report-only findings. On refusal/error it restores the pre-call knowledge/onboarding bytes, modes, caches and directory topology, including local edits, not HEAD.

### Publication boundary

Worklist recomputation uses persist=False. Success reports carried-into-worktree or nothing-to-carryover with written/payload paths, violations, index refresh and worklist. The engine does not stage or commit Git, move refs, carry history, refresh ledger or persist task artifacts; curator rows and leaf closeout remain separate.

## Evidence

- Payload confinement: Only onboarding Markdown/JSON pairs and schema record units enter the write extent. Paths must be canonical relative paths; derived indexes, hidden parents, symlinks and nonregular files are refused. Record JSON may omit an absent Markdown companion; onboarding units may not. [1]
- Conflict and retry safety: Already-equal bytes are accepted even if dirty or staged. Divergent local changes and existing differing records are conflicts. The engine rechecks the complete submitted payload batch before writes and refuses that batch on any conflict; caller-side candidate skipping is a separate boundary. [2]
- Validation and restoration: Apply writes prepared units, regenerates route indexes with explicit target storage, validates the exact tree against official code and the paired memory base (converting an old-format base through the existing converter), and splits refusing from report-only findings. On refusal/error it restores the pre-call knowledge/onboarding bytes, modes, caches and directory topology, including local edits, not HEAD. [3]
- Publication boundary: Worklist recomputation uses persist=False. Success reports carried-into-worktree or nothing-to-carryover with written/payload paths, violations, index refresh and worklist. The engine does not stage or commit Git, move refs, carry history, refresh ledger or persist task artifacts; curator rows and leaf closeout remain separate. [4]
