# mcp/src/agents_remember/application/review_comparison_reopen.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Reopens one immutable comparison generation and reports its current source custody, historical channel availability and retained evidence.

## Code Commentary

Source channels measure whether the exact recorded objects and pins resolve now; recorded release history is a separate fact. `_knowledge_channel` does not open a historical canonical dataset: an explicit deletion is unavailable-history, otherwise the historical dataset is legacy-unavailable. Evidence channels independently read their confined retained references and hashes. No current candidate substitutes for a missing historical object. The former unavailable_channels helper and dataset measurement promise are retired. Snapshot reclamation ordering is owned by review_comparison_reclamation, not inferred from this reader.

## Evidence

### Repo-Internal References

- `reopen_comparison_generation` owns the current boundary described above. [23]
- `_source_channel` owns the current boundary described above. [24]
- `_knowledge_channel` owns the current boundary described above. [25]
- `_evidence_channel` owns the current boundary described above. [26]
