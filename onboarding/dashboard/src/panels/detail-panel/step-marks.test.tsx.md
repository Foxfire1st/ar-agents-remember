# dashboard/src/panels/detail-panel/step-marks.test.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Declare cached major-step mark and pointer-rest detail assertions across task-reading surfaces.

## Code Commentary

A fabricated five-major/eight-child fixture asserts major-only counts and marks on master Now, task Steps and the sidebar, while retaining the full nested step list. Pure state cases promote an unfinished major for begun/done children without uncompleting a done major.

Fake-timer hover cases run only on master/task lines: details appear after rest, preserve ordered child states, leave no tab stop and close on pointer leave. This file does not demonstrate sidebar/bar-mode hover, live projection acquisition or no-fetch behavior merely by using cached fixtures. No test execution or assembled browser verdict is asserted here.

## Evidence

- Seeded major-mark assertions retain nested lists; bounded hover cases cover only master/task pointer-rest details. [1]
