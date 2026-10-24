# mcp/tests/test_tool_answer_table_guards.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The answer guard's shaping, overflow and cut cases (MIK-R108 rule 1): what passes unchanged, what is shortened, and what a shortened answer is still allowed to say.

## Code Commentary

The cases require a small answer to pass through unchanged and an over-bound one to get the short form, with a refusal keeping its code and error in that form. The short form is measured at its boundaries: five hundred short fields, a fifty-thousand-character error, the fixed part and the location with the longest code, and six hundred tokens of multi-token error. A location over the fixed bound is omitted rather than replaced, and the short-form bound ignores a lower row bound. An invalid code is not passed on to the caller while the original whole answer is kept in the detail file, and every surveyed product code is asserted valid. Through the choke point the cases require both the shape and the short form to apply on a shaped row, a failed detail write to answer a log error with the result-kept mark false, the envelope stripped from every answer, and an over-budget root path to be handled. Cutting keeps a list's count and first entries, descends into retained items rather than into dropped ones, and has the answer's next field carry the one following call.

## Invariants And Boundaries

Every bound asserted here is measured on a payload, not copied from the table. The whole original stays in the detail file whenever the caller's copy was shortened or a code was replaced, so a shortened answer is never the only record.

## Evidence

### Repo-Internal References

- An answer under its bound passes unchanged and one over it gets the short form with its code and error. [1]

- The short form holds at its measured boundaries, and a location over the fixed bound is omitted rather than substituted. [2]

- Cutting keeps names, counts and the first entries, and the answer's next field carries the following call. [3]
