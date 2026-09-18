# mcp/src/agents_remember/memory_quality/style/finding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/finding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `../overview.md` |

## Governing Overview

[overview](../overview.md)

## Purpose

Shared finding record for memory-layer style checks.

## Code Commentary

### Logic

Module-level surface:

- `QualityFinding` (class, lines 14-43) — The shared record. `report_only` keeps a finding counted and rendered but out of `ok`; `closeout_owned` marks a row no curator edit can discharge (an anchor that resolves more than once in the cited file), so the stamp decision is closeout's — the flag travels with the finding so the routing is one structural fact rather than a message match at the reporting layer, and `to_dict` publishes it as `closeoutOwned` only when set.
- `check_result` (function, lines 46-68) — Package findings into the uniform runner result ``memory_quality.check`` expects.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `QualityFinding` (lines 14-43). | `QualityFinding` | mcp/src/agents_remember/memory_quality/style/finding.py:14-43 |
| Defines the function `check_result` (lines 46-68) — Package findings into the uniform runner result ``memory_quality.check`` expects.. | `check_result` | mcp/src/agents_remember/memory_quality/style/finding.py:46-68 |

## Update History

- 2026-09-18T19:21+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded the capability this change adds, which the card did not carry. `QualityFinding` gains a defaulted `closeout_owned` flag — a row no curator edit can discharge, because an anchor resolving more than once in the cited file cannot be made unique by narrowing a range or splitting a row — and `to_dict` publishes it as `closeoutOwned` only when it is set, so the routing to closeout is one structural fact rather than a message match at the reporting layer. The flag is set by `claim_reopen` and consumed by its `_gate_result` split (item 17). Documentation only: no source byte was touched by this pass. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are NOT advanced — these sources are uncommitted, so no commit carries their bytes; the candidate is named in the `reviewedWorkingCandidate` metadata row and the governed closeout owns the real commits.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
