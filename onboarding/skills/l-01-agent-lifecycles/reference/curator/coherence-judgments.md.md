# skills/l-01-agent-lifecycles/reference/curator/coherence-judgments.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The Curator's rules for preparing a coherence judgment: what the full catalog projection means, which gates belong to the leaf, and the requirement, delivery and disposition fields.

## Code Commentary

In a full `memory_quality_check` answer, `finalFullCatalog` is the projection for later certification (affected closure, census certification, `finalizationEligible`) and not a leaf gate; the leaf's memory gates are closeout readiness, current coherence and integrity. A `curator_coherence` publication sets `semantic_requirement_revision` to the leaf's primary requirement as `<ID>@v<N>`, `delivery_attempt` to the Worker's attempt identifier, and each judgment's `evidenceRef` to one existing file with its namespace. Dispositions describe what happened to the artifact: `reconciled` (content corrected, one history row; a citation pointing elsewhere changes content, a refreshed hash of the same anchor does not), `extended` or `superseded` (cite the governing requirement or decision), `preserved`, `no-content-impact` and `no-route-impact` (bytes unchanged), `contradicted` (reported to its owner as a blocker) and `capture-candidate` (reported, never closing a judgment alone).

## Evidence

- The full catalog projection is not a leaf gate. [1]
- Publication binds the requirement revision, delivery attempt and per-judgment evidence file. [2]
- The disposition table defines each judgment outcome. [3]
