# mcp/src/agents_remember/application/read_files_briefs.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Adds current file knowledge and brief pointers to eligible read_ar_files rows.

## Code Commentary

The batch assembles each brief from the current memory selection and reads the saved brief's header to report its freshness. Both actions leave the memory folder untouched. It fits richer rows in request order and uses a compact row for every path when the minimum full-row reply exceeds the budget. The compact rows keep each available brief path and its disk age. A caller with a missing or older file can read the full brief after a covering write renews it. When fitting counts-only rows, `BatchBriefs._fit` checks whether every counts-only brief is current on disk and passes `all_current` to `counts_notice` so `briefsLeftOut` never tells callers to open missing or older brief files; compact overflow uses `COMPACT_NOTICE` directing callers to open each current brief.

## Evidence

- The batch preserves each path, brief address, freshness data, and the `all_current` honesty check for `briefsLeftOut` when a full row cannot fit. [1]
