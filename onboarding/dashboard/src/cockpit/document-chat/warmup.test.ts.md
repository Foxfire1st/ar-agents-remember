# dashboard/src/cockpit/document-chat/warmup.test.ts

## Governing Overview

[governing overview](../../overview.md)

## Purpose

Exercise the readWarmupStatus fetch adapter directly with stubbed responses and fetch rejection.

## Code Commentary

Direct calls to `readWarmupStatus` with stubbed `fetch` check the running line and pending list; parsed per-agent states and reasons, omission of the invalid state, and the in-flight list; a status with null line and no pending agents when loading ends; and null after fetch rejection. These cases do not mount a warmup owner or exercise selection, and establish no installation acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence


- Direct readWarmupStatus calls with stubbed fetch check the running line/pending list, parsed agent states/reasons and in-flight list, a completed status with null line/empty pending, and null after fetch rejection. These cases do not mount the warmup owner or exercise selection. [1]

