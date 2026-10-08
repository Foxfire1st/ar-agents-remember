# mcp/src/agents_remember/application/task_docs/task_retirement_projection.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

A sprint's closeout-queue projection after a retirement that was completed late. A fresh retirement publishes the sprint edit and refreshes the sprint's projection in the same publication; a process that dies after the folder moved never reaches that refresh. The completing request looks at the stored projection itself and refreshes it when it no longer reflects the task documents.

## Code Commentary

`refresh_stale_projection` rebuilds the sprint's projection when `_stale` finds it behind the documents; `preview_stale_projection` answers what a dry run would refresh. A current projection, or a sprint from which none can be built, is left alone, so a repeated request with nothing to do changes nothing.

## Evidence

- A late completion refreshes a sprint's stored closeout-queue projection only when it no longer reflects the task documents. [1]
- A current projection, or a sprint with no buildable projection, is left unchanged by a repeated request. [2]
