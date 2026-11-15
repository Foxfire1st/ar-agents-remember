# mcp/tests/test_tool_answer_table_guards.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The answer guard's shaping, overflow and cut cases (MIK-R108 rule 1): what passes unchanged, what is shortened, and what a shortened answer is still allowed to say.

## Code Commentary

The cases require a small answer to pass through unchanged and an over-bound one to get the short form, with a refusal keeping its code and error in that form. The short form is measured at its boundaries: five hundred short fields, a fifty-thousand-character error, the fixed part and the location with the longest code, and six hundred multi-token characters of error. An exact recorded location survives even when it is longer than the bound, and the final cut hint names the same file. Overflow shaping uses the common 400-token target even when the original row bound is lower. An invalid code is not passed on to the caller while the original whole answer is kept in the detail file, and every surveyed product code is asserted valid. Through the choke point the cases require both the shape and the short form to apply on a shaped row, a failed detail write to answer a log error with the result-kept mark false, the envelope stripped from every answer, and an over-budget root path to be handled. Cutting keeps a list's count and first entries, descends into retained items rather than into dropped ones, and has the answer's next field carry the one following call.

`EntryPointOverflowGuardTests` calls the real registered `direct_execution_grant` route with an intentionally long unsupported action. It requires an ordinary refusal with `overflow`, a final `cut` naming the saved whole result, the complete action in that file, no answer-only `cut` in the saved whole, and refusal classification by the independent sweep. This is an intentionally overflowing route case, not a new tool bound or guard.

## Invariants And Boundaries

Every bound asserted here is measured on a payload, not copied from the table. When detail recording succeeds, the whole original stays in the detail file whenever the caller's copy was shortened or a code was replaced.

## Evidence

### Repo-Internal References



- An answer under its bound passes unchanged and one over it gets the short form with its code and error. [1]





- The cases measure the short form and require an over-bound recorded location to remain exact, with the cut hint last. [2]





- Cutting keeps names, counts and the first entries, and the answer's next field carries the following call. [3]
