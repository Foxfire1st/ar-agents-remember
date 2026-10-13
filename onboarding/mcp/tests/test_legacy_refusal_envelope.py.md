# mcp/tests/test_legacy_refusal_envelope.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Source-level public-entry tests of the MIK-R46 legacy refusal envelope on disposable Git worlds. A three-unconverted-side memory merge refuses with the central legacy-format message naming preSyncHead, sourceCommit and merge base; the series case preserves absent activation, contract bytes and observed refs/worktree/index state. A converted landed candidate on a legacy line is not classified legacy and reaches its own validator. Public start still admits unconverted memory and returns memoryFormat: legacy-format with the first-conversion command in memoryFormatProcedure. These assertions are not execution or certification evidence. Byte snapshots exclude loose Git objects; index-path observations are not universal raw-index-file identity proof.

## MIK-R46 R8: quality refusal includes its projected keys

`test_memory_quality_check_unconverted_refusal_answer_validates` constructs an actual unconverted external-memory `QueueFixture`, runs the quality sync request, and checks `ok=false`/`code=unconverted-memory`. `quality_result_answer(dict(whole))` must agree with the whole on `status=failed`, `blockingCount=0` and `nextAction=worktree_sync`. Every delivered key outside the existing `ROW_CASE_FRAMEWORK_KEYS` is present in the whole. The test validates that refusal envelope, not quality certification, successful scanning or converted-memory readiness. The earlier refusal cases remain; the new test is additive.


## Evidence

These are source assertions, not a claim of fresh execution or certification.

### Current Source-Inspection References

- Divergent series legacy sync refuses with judged sides/conversion, leaves absent activation, contract bytes and observed state unchanged. [1]
- Converted candidate not legacy; public rejection equals direct validator refusal on identical request; observed state unchanged. [2]
- All-three-legacy merge refuses with preSyncHead/sourceCommit/merge base; refs/worktree/index-path observations unchanged. [3]
- Public start RETURNED; memoryFormat legacy-format; memoryFormatProcedure names conversion command. [4]

- An actual unconverted quality request returns refusal keys equal to its delivered projection, except the established framework-key convention. [5]
