# mcp/tests/test_tool_answer_rows_quality.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Derives quality answer-row cases from real sync/start/poll runs and complete blocking populations.

## Code Commentary

The added mounted FastMCP witness uses real `tool_call_context` for sync, start and completed poll. A live-invariant fixture and then an empty converted tree require computed proof counts in both bounded answers and full retained logs. The source compares `blockingCount` with `curatorActionableCount`, excludes proof coverage from blocking finding kinds, keeps full checks in the log rather than the answer, and requires no overflow within the declared token bound. This describes fixture assertions only: no server, asynchronous run, proof publication or acceptance was performed here.

The largest sync case seeds converted missing-path anchor sidecars with matching Markdown markers and asserts the exact 54-finding error sentence, at least 25 blockers and ten projected entries. Other cases retain clean parentless coherence takeover, live asynchronous admission and completed-polling assertions; these source expectations are not new execution results. Every not-ok answer must retain code, one error sentence and next action. Blocking projection covers missing-only, stale-only, census-only and mixed populations in repair order. Registry settling is fixture control rather than substitute whole-memory certification.

## Evidence

- Mounted sync and completed poll retain computed proof counts and the actual blocking count in bounded answers while full checks remain in the retained log. [2]


No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.


### Current Source-Inspection References


- Source cases assert sync/start/poll row shapes and bounded blocking samples; converted missing-anchor sidecars seed the largest sync expectation. [1]
