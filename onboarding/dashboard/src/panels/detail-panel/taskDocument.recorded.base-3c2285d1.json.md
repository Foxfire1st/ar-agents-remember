# dashboard/src/panels/detail-panel/taskDocument.recorded.base-3c2285d1.json

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Keep immutable task-document producer recordings for the older-server component recovery seam.

## Code Commentary

The recording retains input documents, summary and body output, and recordedFrom provenance identifying the build, producer, command and script. Inputs are explicitly made-up sandbox tasks written through that build's own task writer; summary and body nodes are actual producer output, not a manually typed TaskDocNode. Older-producer payloads omit form/head additions and the entire review state; their genuine absence is the recovery opportunity, not an undefined or malformed present count.

The matching test uses an existing shared stream frame around these nodes: the document payloads are recorded, the older stream envelope is not. Regenerate or replace a recording through its producer instrument with explicit provenance, never by filling absent newer fields by hand. Treat the recorded build label as historical identity, not as evidence of the live synced tree.

## Boundaries

The recording exercises read-only dashboard recovery, not native task acceptance, mutation or browser geometry. No new guard entry follows solely from using a supported payload; existing guard authority remains with its owner.

## Evidence

- Stored inputs, producer outputs and historical provenance define the payload's exact recovery opportunity. [1]
