# skills/l-01-agent-lifecycles/reference/curator/publication-report.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The Curator's rules for reading an authored-knowledge ingest report before claiming publication.

## Code Commentary

Without `--commit`, ingest plans and validates without writing; `--commit` authorizes file writes only, never a Git commit or acceptance. The Curator reads the actual report state (`written`, `planned` or `refused`), written paths, record and entry identifiers and refusals. A refused ingest wrote nothing and names each problem; a partial handover stays visibly partial; exit zero covers both a plan and a write; and even `written` with no written paths establishes no publication. A correct-input write refusal follows `refused-write.md`. A target without its rationale is refused as `realization_rationale_absent`, and the writer requires converted memory.

## Evidence

- `--commit` authorizes file writes, never a Git commit or acceptance. [1]
- The report state, paths, identifiers and refusals decide what was written; exit zero and `written` alone prove no publication. [2]
- Correct-input refusals go to the same-tool procedure; a missing rationale is refused by name. [3]
