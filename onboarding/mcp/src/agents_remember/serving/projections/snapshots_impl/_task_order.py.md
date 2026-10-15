# mcp/src/agents_remember/serving/projections/snapshots_impl/_task_order.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Adapt derived ordinary-master Order and both direct dependency directions into task-document projection fields, using named inputs rather than a corpus walk on demand.

## Code Commentary

The corpus adapter uses its already-read document map and only each ordinary master’s listed file paths. Matching child waitsFor supplies predecessors; reverse links are derived from the same Order population. No Order means no added fields. The render-ready graph omits fileless nodes, retains state/cycle annotations and carries predecessor reasons; leaf dependency facts can retain gone/fileless targets. _graph materializes ready_ids as one set per graph construction, then uses set membership for each task rather than repeated tuple scans. This is a local indexing property, not a whole-reader complexity or timing guarantee.

The reference adapter copies ID and title from the supplied derived MasterOrderTask, maps its abandoned status to gone, otherwise preserves its status, and derives a document path only when its file exists. Missing-reference discovery and child-title versus row-name selection are upstream population-builder responsibilities, not decisions made by this adapter.

The on-demand adapter uses the requested ordinary master, or the requested leaf’s master/default task path, then explicitly listed children; missing/invalid/sprint masters return no fields. It does not enumerate unrelated masters. RF01 newly read owner and child dicts are passed to projected_document only after payload.get("schema") == TASK_DOCUMENT_SCHEMA. Missing/wrong-schema owners stop before child reads; missing/wrong-schema children are skipped, leaving indexed row facts to the population builder. Schema-bearing payloads retain tolerant parsing. Historically, F01 cc238585 lacked those raw-schema checks and the model’s schema default could admit a schema-less input; that defect is not the operative RF01 behavior and does not relax the schema-bearing admission promise. The adapter neither stores waves nor decides start permission.

## Evidence

- Named ordinary-master/listed-child reads derive informational dependency fields, explicitly filter newly read dicts by raw task schema before tolerant parsing, and index graph ready membership once. These predicates are not universal body-byte parity or start authority. [1]
