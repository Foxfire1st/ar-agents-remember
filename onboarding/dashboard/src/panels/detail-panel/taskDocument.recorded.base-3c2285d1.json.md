# dashboard/src/panels/detail-panel/taskDocument.recorded.base-3c2285d1.json

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Keep an immutable historical task-document producer recording and its provenance. The current older-server component suite reads this recording only for provenance; native L168 entry recordings supply its rendered recovery cases.

## Code Commentary

The recording retains input documents, summary and body output, and recordedFrom provenance identifying the build, producer, command and script. Inputs are explicitly made-up sandbox tasks written through that build's own task writer; summary and body nodes are actual producer output, not a manually typed TaskDocNode. Older-producer payloads omit form/head additions and the entire review state; their genuine absence is the recovery opportunity, not an undefined or malformed present count.

`older-server.test.tsx` imports this recording but uses the two old recordings only to inspect the base build label, absence of review state in the base output and equality of their input documents. The mounted cases instead serve `taskEntries.recorded.l168.json` (`nativeBuild.optionalAbsent` and `nativeBuild.reviewPresent`) through the shared stream-frame helper; they do not put these historical summary/body nodes into that frame. Regenerate or replace a recording through its producer instrument with explicit provenance, never by filling absent newer fields by hand. Treat the recorded build label as historical identity, not as evidence of the live synced tree.

## Boundaries

This recording preserves the historical producer payload, not a current rendered recovery witness. The native L168 recording now supplies the read-only dashboard recovery cases. Neither this historical recording nor those seeded cases establish native task acceptance, mutation or browser geometry. No new guard entry follows solely from using a supported payload; existing guard authority remains with its owner.

## Evidence

- Stored inputs, producer outputs and historical provenance define the archived payload; the current suite uses the old recordings only for provenance and renders the native L168 recording. [1]
