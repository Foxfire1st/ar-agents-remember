# dashboard/src/test/fixtures/documentChat.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Shared document-tree fixtures for the document chat tests: a sprint, its commanded master, one leaf and the matching series projection.

## Code Commentary

The fixture builds the exact three-level shape the binding walks — a sprint whose `orchestrates` names the master, a master a sprint commands, and a leaf of that master — plus the series node that carries the leaf row. Tests use it to assert the role table for each selection kind without depending on live projection data.

## Evidence

- The sprint fixture commands the master used by the other fixtures. [1]
- The master and leaf fixtures model a commanded master and its leaf. [2]
- The series projection carries the leaf row the binding needs. [3]
