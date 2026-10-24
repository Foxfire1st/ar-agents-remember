# mcp/tests/test_tool_answer_table_measure.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The final-measure and partial-write cases of the tool-answer log: the guard measures what is actually delivered, and a short write is detected rather than claimed.

## Code Commentary

The measure cases attach the log location to an answer near its token bound and require the delivered mapping to be re-guarded, so bookkeeping cannot push a delivered answer over silently. They require the observer's count to match the delivered answer, two late line failures to keep the first error and recount, an ordinary near-edge answer with a line failure to be re-guarded, the full short form to fit including the bookkeeping, a cut answer whose late failure is re-guarded at the short ceiling, and a line-failure overflow to stay inside the bound with the two counts agreeing. The partial-write cases recover a short write, require a partial then stalled prefix not to join the next record, require concurrent writers never to interleave records, require a stalled writer to leave its neighbour parseable, count a concurrent stall on the next persisted line, and drop and count a stuck write.

## Invariants And Boundaries

The measured quantity is the final delivered mapping, after the location and the log line were attached; measuring the pre-log answer would be a different claim. A short write is never claimed as a whole record, and a dropped write is counted rather than silently lost.

## Evidence

### Repo-Internal References

- A near-edge answer is re-guarded after its log location is attached, and the observer's count matches what was delivered. [1]

- A short or stalled write is detected, never joined to the next record, and a stuck write is dropped and counted. [2]
