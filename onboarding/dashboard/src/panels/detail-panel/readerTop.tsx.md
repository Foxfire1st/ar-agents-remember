# dashboard/src/panels/detail-panel/readerTop.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Render only the task-body loading/unavailable notice. Complete reader head/objective composition belongs to taskReader.tsx.

## Code Commentary

TaskBodyNotice is presentation-only; the former OverviewTop composition is no longer exported here.

TaskBodyNotice names loading as a status region and unavailable as a summary fallback; other states draw nothing. It is a presentation component, not the identity-bound body fetch/hydration owner. Header, Objective and fixed Markdown mechanisms remain in their shared owners.

## Evidence
