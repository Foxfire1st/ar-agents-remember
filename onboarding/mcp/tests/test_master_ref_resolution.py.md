# mcp/tests/test_master_ref_resolution.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Static and fixture witnesses of one named-master resolver across the task writers.

## Code Commentary

The fixture checks extensionless task, task.md and task.json resolution and refusal of missing, escaping or nested named masters. Master sync, finalizer and reopen share the resolver; an unnamed leaf retains its folder-master fallback. Helper/in-place assertions do not execute every complete writer transaction, and source reading is not a fresh test execution.

## Evidence

- MasterRefResolutionTests: qualified source contract. [1]
