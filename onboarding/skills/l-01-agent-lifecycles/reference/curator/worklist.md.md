# skills/l-01-agent-lifecycles/reference/curator/worklist.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The Curator's rules for answering the persisted leaf worklist: pointers to the writer's row and evidence procedures, and the meaning of the returned worklist and gate blocks.

## Code Commentary

The first section links the hand-off templates at each action: the writer's input sections before answering a history row or grouping changed paths, reconsideration of a rejected alternative before answering a reconsideration candidate, invariant entries before attaching a document-local invariant, replacing evidence or authoring a test proof, and realization rationale and role before correcting a target in a rerun (which replaces this leaf's entry while keeping its identifier). The hand-off ingestion template links back to the response-block section.

The persisted worklist and the full memory-quality result in its log are read together; the bounded MCP answer names artifacts rather than inlining the blocks. `knowledgeWorklist` summarizes the computed worklist (`state`, `path`, `digest`, `itemCount` of all items including satisfied ones, `itemsByKind`, `incomplete` inputs) and is not proof that items are answered; an absent block is neither a pass nor an empty result. `knowledgeGate` judges the exact paired candidate and current satisfying rows and reports `state` (`pass` or `refused`), owner, worklist identity and finding, open-item, incomplete, violation and report-only counts. Its subtotals are not summed into a verdict, report-only observations are not blocking, a closeout refusal is `knowledge-gate-refused`, and a changed candidate needs its own exact-tree check.

## Evidence

- Row, reconsideration, invariant-entry and rationale-correction procedures are reached through the hand-off templates. [1]
- The worklist block summarizes the computed worklist and is not a verdict; an absent block is not a pass. [2]
- The gate block's fields, and the rule against summing subtotals or counting report-only observations. [3]
- The hand-off ingestion template links the response-block section. [4]
