# mcp/src/agents_remember/memory/conversion/crossing_writer.py

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Preserves writer attribution and admissible review evidence as a memory crossing selects or combines content.

On a stripped tie (when the merged record equals both sides' records without `writer` and legacy typed `status` words), `stamp_merged_records` stores the sole side whose stored bytes differ from the base (absence at base counts as changed on both sides), else the sole side in state form (no legacy typed `status` word and a stored `writer` field), else `own`. That chosen side becomes the crossing-selection source, and `tied` is the stripped equality, so a stamp-only tie joins both sides' admissible reviews and writes no `crossingSelections` row when both lines share their selection history.

## Evidence

- The merge selects record meaning before attaching writer provenance. [1]

- The crossing binds retained content to admissible evidence from its selected side. [2]

- On a stripped tie, stored bytes keep the sole side changed from base, else the sole state-form side (no legacy typed status word and a stored writer), else own. [3]
- Crossing selection uses the chosen side and passes stripped equality as `tied`, joining admissible reviews on a stamp-only tie and omitting `crossingSelections` on shared selection history. [4]
