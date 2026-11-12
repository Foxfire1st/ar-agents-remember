# dashboard/src/panels/detail-panel/page-look.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin the form-shared head, table grammar, whole-round counts and navigable Markdown of task pages.

## Code Commentary

Assertions cover identity/facts/header notes followed by one objective outside the complete head, the primary requirement link without repeated text, step and work-in-progress cells, and whole-round review counts when the preview omits the last finding. Report requests use a task-root-relative document reference; register links, hidden cells, nested skip reasons and reference labels keep actual navigation. These seeded component checks are not pixel-colour or first-screen browser measurements. The Steps fixture has four major steps and two nested rows; its heading counts only majors (`1 of 4 done`) and asserts exactly four `[data-step-dot]` marks while preserving nested step rendering. The counts are supplied by the fixture, not produced by a backend writer in this suite.

## Boundaries

This card describes the executable assertions and fixture seams of this module. It does not turn a mocked or seeded unit observation into system-wide acceptance. Keep fixture provenance, controlled time and actual producer opportunities explicit when extending the cases.

## Evidence


- Seeded head/table/review/navigation assertions; the Steps case preserves nested rows but requires a 1-of-4 major heading and four marks. [1]
