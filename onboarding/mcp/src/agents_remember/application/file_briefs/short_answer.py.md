# mcp/src/agents_remember/application/file_briefs/short_answer.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Fits assembled file-brief facts into the bounded read_ar_files reply.

## Code Commentary

The fitter reserves a row for every requested path before expanding rows in request order. When the first candidate's whole row fails to fit, it keeps as many leading rule statements as possible. If a later whole row fails, it leaves that row and the remaining candidates counts-only. The caller switches to compact rows if the minimum projection overflows.

Short-answer notices reflect whether the saved disk brief is current: when `location.current` is false, `whole` emits `IN_THE_FILE_NOT_CURRENT` directing callers to `knowledge_read` rather than opening the stale or missing brief file, `without_rule_texts` and `_named_only` emit `LEFT_OUT_NOT_CURRENT` and `RULE_LEFT_OUT_NOT_CURRENT`, and `counts_notice(..., all_current=False)` instructs callers to open only briefs marked current.

## Evidence

- The fitter reserves minimum rows, adds whole rows in request order and clips rule text only in the first candidate. [1]

- Short-answer and counts-only notices distinguish current from missing or older disk briefs and direct callers to `knowledge_read` when a saved brief is not current. [2]
