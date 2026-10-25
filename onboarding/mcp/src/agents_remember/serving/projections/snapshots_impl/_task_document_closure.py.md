# mcp/src/agents_remember/serving/projections/snapshots_impl/_task_document_closure.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Compute the incremental task projection's transitive document dependency closure over retained payloads: changed documents, folder masters, their explicitly listed children, execution-graph consumers and cross-document subtask joins. Avoiding under-approximation is standing intent. This closure returns a set and skips invalid/unresolved links; it does not signal ambiguity or request full projection. The caller chooses full refresh for incomplete/empty wake paths, first use or pending retry.

## Code Commentary

Compute the incremental task projection's transitive document dependency closure over retained payloads: changed documents, folder masters, their explicitly listed children, execution-graph consumers and cross-document subtask joins. Avoiding under-approximation is standing intent. This closure returns a set and skips invalid/unresolved links; it does not signal ambiguity or request full projection. The caller chooses full refresh for incomplete/empty wake paths, first use or pending retry.

The file-link closure admits every explicit nonempty subTasks[].file, including same-folder names, normalizes its suffix to .json and resolves it lexically against retained payload paths. A listed sibling is therefore reprojected when its master is reached: Order graph and both dependency directions can change after a sibling edit. This adds no filesystem read or unrelated corpus enumeration.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence



- Computes changed/folder-master/explicitly-listed-child/graph-consumer/file-join transitive closure from retained payloads. Avoiding under-approximation is standing intent, not an implemented general ambiguity detector: invalid/unresolved links are skipped. Caller full refresh is selected by incomplete wake paths, first use or pending retry. [1]



- Explicit same-folder and cross-folder listed children join the retained-payload fixpoint so sibling-derived Order display is recomputed; resolution normalizes listed paths to JSON and performs no filesystem read. [2]
