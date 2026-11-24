# mcp/src/agents_remember/memory/carryover_apply.py

## Governing Overview

[Memory area overview](overview.md)

## Purpose

Implements converted carryover’s worktree-only transaction after the caller admits and prepares selected units.

## Code Commentary

### Payload confinement

The write extent accepts onboarding Markdown/JSON pairs, including pairs under dot directories, and admitted knowledge record units. Paths must be canonical relative paths. The shared predicate rejects derived route indexes. The transaction also rejects symlinks and nonregular files. A record JSON may stand alone. An onboarding document needs the Markdown and JSON pair.

### Conflict and retry safety

Already-equal bytes are accepted even if dirty or staged. Divergent local changes and existing differing records are conflicts. The engine rechecks the complete submitted payload batch before writes and refuses that batch on any conflict; caller-side candidate skipping is a separate boundary.

### Validation and restoration

Apply writes prepared units, regenerates route indexes with explicit target storage, validates the exact tree against official code and the receiving leaf's recorded memory base, converting an old-format base through the existing converter. It establishes that base as a readable ancestor of the receiving memory HEAD before writing and uses it for the worklist too. An unestablished base yields `carryover-failed` before writing. The validator separates refusals from report-only findings. On refusal/error it restores the pre-call knowledge/onboarding bytes, modes, caches and directory topology, including local edits, not HEAD.

### Publication boundary

Worklist recomputation uses persist=False. Success reports carried-into-worktree or nothing-to-carryover with written/payload paths, violations, index refresh and worklist. The engine does not stage or commit Git, move refs, carry history, refresh ledger or persist task artifacts; curator rows and leaf closeout remain separate.

## Evidence

- Payload confinement covers canonical relative onboarding pairs, including pairs under dot directories, and admitted knowledge record units. The shared predicate rejects derived route indexes. The transaction rejects symlinks and nonregular files. A record JSON may stand alone, while an onboarding document needs both files. [1]

- Before writing, apply establishes the receiving leaf’s recorded memory base. It validates the resulting tree against that base and official code, and recomputes the worklist against the same base. An unavailable base returns carryover-failed before writes. Validator refusals or later failures restore the owned pre-call bytes, modes, and directory topology. [3]


- Publication boundary: Worklist recomputation uses persist=False. Success reports carried-into-worktree or nothing-to-carryover with written/payload paths, violations, index refresh and worklist. The engine does not stage or commit Git, move refs, carry history, refresh ledger or persist task artifacts; curator rows and leaf closeout remain separate. [4]



- Conflict and retry safety: Already-equal bytes are accepted even if dirty or staged. Divergent local changes and existing differing records are conflicts. The engine rechecks the complete submitted payload batch before writes and refuses that batch on any conflict; caller-side candidate skipping is a separate boundary. [2]
