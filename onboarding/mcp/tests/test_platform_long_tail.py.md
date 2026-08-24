# mcp/tests/test_platform_long_tail.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_platform_long_tail.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Long-tail regression collection for refusal, parser, cache, fingerprint, inbox, and terminal boundaries.

## Code Commentary

### Logic

Inbox renewal now preserves or replaces `subjectTaskDocumentRef` plus seat role, and terminal-open refusal fixtures use canonical task-document identity. The remaining cases protect their independent fail-closed and tolerance behaviors.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the registered or owning seam directly.

### Invariants And Boundaries

Renewal changes only explicitly restated fields; structural task identity remains repository-qualified and no retired leaf field is synthesized.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card after the pure decision-role tests moved to the direct cohort. | `ReadFilesRangeTests` | mcp/tests/test_platform_long_tail.py:68-90 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## L23 Extracted Spawn Refusals

The long-tail opener tests now call the application-owned refusal translator
with `OpenTerminalResult`, preserving their public payload assertions after the
builder left `terminal_tools.py`.

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260824-PDLS Cohort Extraction

The known and misspelled decision-role coercion assertions moved unchanged to the bounded direct
cohort. This long-tail integration module no longer needs to import that pure vocabulary helper;
its remaining platform contracts are unchanged.

## Update History

- 2026-08-24T21:23+02:00 — Moved two decision-role assertions to the bounded direct cohort.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: reconciled the extracted terminal refusal boundary in long-tail coverage; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Reconciled `test_platform_long_tail.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` row with an exact
  anchor (deleting the unresolvable directory row); exact non-fixing check returns zero findings.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  long-tail guard suite. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.
