# mcp/src/agents_remember/models/tools/tool_answer_short_fields.py

## Governing Overview

[Models overview](../overview.md)

## Purpose

Selects the typed values that callers of specific tools need from an over-bound answer and fits them into the shared short form.

## Code Commentary

The field declaration uses the tool name and its Boolean outcome. Each declared path is read from the validated whole result and admitted only with its expected type. The declaration accepts selected nested strings, an integer count mapping, a list of bases and a Boolean repair indicator.

The fitter considers declared values in order and keeps each fitting value whole. If a value is too large, its path and measured token size enter `cut.omittedFields` when the notice fits. Each kept value or notice reserves its space before the next field is tried. The complete result remains available through the locator when recording succeeded.

## Relationships

The application answer guard supplies the tool identity and validated whole result. The short-form model supplies the measured envelope and presents fitting outcome and action fields ahead of the reserved locator.

## Evidence

- The declaration selects and type-checks the supported paths for each tool outcome. [1]
- The fitter measures whole values and reserves each fitting omission notice before the next field. [2]
- The delivered mapping places fitting declared outcome and action fields before the result locator. [3]
- The application supplies the validated result, tool name and exact result location to the overflow model. [4]
