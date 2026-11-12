# mcp/src/agents_remember/serving/review_answer_reuse.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Keep recorded-comparison answers only while their exact observed inputs, age/size bounds and caller admission predicate permit reuse.

## Code Commentary

A hit requires every supplied input to retain its original readable stamp. A changed or unreadable input drops the kept answer. Fresh production is admitted only when complete observations taken before and after it agree.

The optional `keep` predicate can refuse fresh values even with stable inputs. A refused value is returned once and not stored, so an answer naming a failed read is recomputed on the next request. Omitting keep admits every value that meets the observation constraints.

The default capacity is 64 answers and age is 900 seconds; callers can configure both. Kept and returned values are deep-copied. Producing reads run outside the lock, so concurrent misses can compute twice; lock-protected bookkeeping maintains LRU eviction, expiry and diagnostic retained count.

## Invariants And Boundaries

The caller supplies the exact question key and input set. This store writes no file and chooses no working tree or selection policy of its own. Stable stamps do not override an explicit caller refusal to retain a failed answer.

## Evidence

- Stable hits are copied; fresh values also pass the optional keep predicate and matching before/after observations. [5]
- Every supplied input must be readable and match its admitted stamp.
- LRU capacity and finite age bound stored answers. [7]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/review_answer_reuse.py:92-115 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 3104b78bb309a8e1a912503557adb08599b52ef0. Retired means the anchor no longer stands, not that the cited subject was deleted.
