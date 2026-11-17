# scripts/instruction_renewal/plan.py

## Governing Overview

[Overview](../../overview.md)

## Purpose

Combines instruction-derived facts and declared distribution copies into one replacement plan.

## Code Commentary

Planning derives manifest metadata, digest bindings, pointer wording and budget measurements before collecting changed carriers. Package copies use the prospective canonical bytes, so regenerated facts and their copies belong to the same plan. The copy plan also projects `mcp/certification-profile-v1.json`, copies canonical `docs/tool-details.md` into packaged runtime docs, and schedules extra declared-target files for deletion. Publication unlinks those deletion entries, writes other replacements in order and attempts to restore original bytes in reverse order after an OSError; restoration can itself fail, so this is not an atomic filesystem transaction.

## Relationships

The CLI supplies a RenewalRequest. The existing sync-skills module remains the declaration and copy-projection owner; this planner loads it rather than maintaining another target inventory. The plan also carries the canonical tool-details document into its declared runtime location.

## Evidence

- All fact planners run before the final replacement list is returned. [1]

- Publication attempts reverse restoration after a write failure. [3]

### Repo-Internal References (renewed)

- Package carriers reuse the copy owner and prospective canonical bytes; they also project the certification profile, copy tool details and remove extra target files. [2]
