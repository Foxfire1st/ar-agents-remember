# mcp/tests/test_review_answer_reuse.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Guard the recorded-answer reuse store's promises: a second read of unchanged inputs is served, that
answer is byte-identical to a fresh computation, a changed or unreadable input invalidates it, and
the age and size bounds evict it. The store is exercised directly with a controlled clock, so the
bounds are measured rather than raced.

## Code Commentary

### Parity, not just a hit

`test_a_second_read_of_the_same_inputs_is_served_from_the_kept_answer` counts the producing reads, so a
second read over unchanged inputs is served rather than recomputed, and
`test_a_kept_answer_is_byte_identical_to_a_fresh_computation` shows the value a store returns matches a
fresh computation over the same inputs. The two are separate: the parity case runs one `answer` call in
a fresh store and compares it with `produce()`, so it does not exercise a served hit. The clock is a
callable the cases advance, which is what makes the age boundary an assertion instead of a sleep.

### Invalidation is a miss, not a stale answer

`test_a_changed_input_invalidates_the_kept_answer` moves one input's stamp and
`test_an_unreadable_input_is_never_kept_or_served` makes one input unreadable; both require a new
native production. `test_an_answer_is_not_served_after_the_age_bound` and
`test_the_size_bound_evicts_the_least_recently_used_answer` measure the two bounds the store declares.

### Scope

These cases assert the store's own contract with synthetic sources. They do not speak for an
installed server, a review's latency, or the recorded reads that supply real sources.

## Evidence

- An answer a fresh store returns is byte-identical to a fresh computation of the same inputs. [1]
- A changed input is never served from the kept answer. [2]
- An answer is not served after the declared age bound. [3]
