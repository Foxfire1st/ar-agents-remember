# mcp/src/agents_remember/models/tools/tool_answer_short_fields.py

## Governing Overview

[Models overview](../overview.md)

## Purpose

Selects the typed values that callers of specific tools need from an over-bound answer and fits them into the shared short form.

## Code Commentary

The tool name and wire Boolean select the declared fields. Each path is read from the validated whole result and admitted only with its expected type. For recorded and would-record landing, the fitter considers state, a next-step sentence and tool, a stale-entry count and the first 20 record keys in that order.

The fitter considers declared values in order and keeps each fitting value whole. If a value is too large, its path and measured token size enter `cut.omittedFields` when the notice fits. Each kept value or notice reserves its space before the next field is tried. Landing count and record keys share a nested object, and each field has its own fit check. The count stays only if it fits alongside the exact locator and any retained state and next step. Once fitted, the count stays if the keys are dropped, even if their omission notice also fails to fit. When the count does not fit, the short answer omits the staleEntries mapping and the named detail holds the whole debt.

## Relationships

The application answer guard supplies the tool identity and validated whole result. The short-form model supplies the measured envelope and presents fitting outcome and action fields ahead of the reserved locator.

## Evidence


- The declaration selects and type-checks the supported paths. Landing outcomes admit one next-step object, an independent count and capped record keys. [1]


- The fitter preserves sibling fields, fits each whole value and reserves any fitting omission notice with the rejected field size. [2]

- The delivered mapping places fitting declared outcome and action fields before the result locator. [3]
- The application supplies the validated result, tool name and exact result location to the overflow model. [4]
