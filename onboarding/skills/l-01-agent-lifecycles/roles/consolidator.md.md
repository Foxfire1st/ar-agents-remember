# skills/l-01-agent-lifecycles/roles/consolidator.md

## Governing Overview

[overview](overview.md)

## Purpose

Defines the Consolidator role charter, permitted edits, hard seat boundaries, and on-demand detail reference index for a single consolidation leaf seat.

## Code Commentary

Establishes the Consolidator as the sole writer seat on a consolidation leaf (no Worker or Curator): it begins from code tree, memory tree, and `consolidationList` (stopping and reporting to Manager if absent), scopes MCP calls by target (`task_context`, `workspace.memoryRoot` with `knowledge_read` `impact`/`search`/`records`, or leaf contract), and notes that `knowledge_write(commit=True)` writes files without committing to Git. It sets the core examination doctrine (family-together reading; age/likeness/use as hints only; named or newly-linked proof tests only; code tree identical to base), the three outcome categories (`stands`, corrected, `unresolved`) with mandatory proof evidence, and the exact allow-list of memory edits (rule text/conditions/exclusions, family members/guarantee, card realization/proof entries and sentences, stale decision text, missing title; never setting product-owned state except `status: retired`, never writing tests or code). `Boundaries` enforces single-writer lane discipline (no helper writers), forbids code edits, Git writes, role starts, fake hashes, and model/harness keys, caps repeated failed repairs at 3 before escalating to Manager, requires `worktree_sync` + retest if master moves, and marks a step `done` via `task_doc(set_step)` if present. `Reference index` provides detail pointers for knowledge tools, pass/worklist rules, ingestion/publication/families, coherence/messaging, and sync/escalation.

## Relationships

Registered as a leaf-altitude launchable role (`roles.consolidator`) in `skills/l-01-agent-lifecycles/composition-manifest.json` with 13 admitted tools, operations `["orientation", "consolidation", "recovery"]`, template `curator-handoff-ingestion.md`, and criterion `onboarding-memory.md`; packaged into `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/consolidator.md`. Composed with `operations/consolidation.md` at capsule compile time and points to `reference/consolidation-pass.md` for step-level procedure.

## Evidence

- The role body defines the Consolidator's leaf mission, MCP call scoping, family-first code-and-proof examination, three outcome rules, mandatory proof evidence, and allowed memory-only edits. [1]

- `## Boundaries` enforces single-writer discipline, forbids code edits, Git writes, role starts, fake hashes, and model/harness keys, caps failed repairs at 3 per item, and governs `worktree_sync` and `task_doc(set_step)`. [2]
- `## Reference index` maps pass, knowledge, write/family, coherence/message, and sync/escalation triggers to their detail pointers, including `reference/consolidation-pass.md`. [3]
