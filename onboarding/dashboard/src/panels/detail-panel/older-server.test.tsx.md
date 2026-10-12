# dashboard/src/panels/detail-panel/older-server.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin recovery on genuine recorded older task-document payloads and the matching current producer payload.

## Code Commentary

Recorded summaries enter through the stream and recorded bodies through the task-document endpoint mock. The base recording has no review state at all: task and master omit review/count without throwing while retaining their existing content. Current recordings show the required whole-round count. Recording metadata identifies the producer and source documents; the stream frame around the records is not itself a recorded older envelope.

## Boundaries

This card describes the executable assertions and fixture seams of this module. It does not turn a mocked or seeded unit observation into system-wide acceptance. Keep fixture provenance, controlled time and actual producer opportunities explicit when extending the cases.

## Evidence

- The module owns the regression assertions and fixture boundaries described above. [1]
