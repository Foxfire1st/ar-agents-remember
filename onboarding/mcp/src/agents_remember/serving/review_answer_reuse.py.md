# mcp/src/agents_remember/serving/review_answer_reuse.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Keep a recorded comparison's reviewer answers for as long as the exact inputs they are a function of
hold, and serve them unchanged — the same bytes a fresh computation of the same inputs produces. The
store is bounded in size and age, and it never serves an answer whose inputs it could not read.

## Code Commentary

### Three rules bound what may be served

A hit is served only when every observed input still carries the stamp it had when the answer was
computed; one unreadable input is a miss, never an agreement. At most `capacity` answers are kept,
least recently used first out, and none is served after `max_age_seconds`. A value is kept only when
one observation of its inputs taken before the computation equals one taken after it, so an answer
composed while its inputs moved is never kept.

### Concurrency and lifetime

`answer` runs the producing read with no lock held, so one slow read never delays another's answer;
`_fresh` decides the hit, `_keep` records it and `_expire` drops what the age bound no longer allows.
The default bounds are 64 answers and 900 seconds, and both are owned here rather than by a caller.

## Invariants And Boundaries

- The key is the exact question; the sources are the exact inputs, each with its own stamp.
- A changed or unreadable input invalidates the kept answer; nothing is served on doubt.
- The bounds are size and age, and an answer never outlives either.
- This store writes no file and reads no working tree of its own; its sources are supplied by the
  composition that owns them.

## Evidence

- A kept answer is returned only while every observed input carries the stamp it had at production. [1]
- An answer is kept only when the observations before and after its computation agree, so a value composed while its inputs moved is dropped. [2]
- The age bound drops every answer past it. [3]
- The size bound evicts the least recently used answer. [4]
