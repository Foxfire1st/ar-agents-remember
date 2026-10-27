# mcp/tests/test_paseo_catalog_fresh.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Checks fresh catalog questions, durable successful answers, current-operation sharing and direct host choice matching.

## Code Commentary

The tests use temporary runtime homes and a recording fake bridge. Views replace changed choices with a fresh answer. Failed parts reuse only their own saved successes, including their original read times after a new Python process starts. Without a fresh or saved answer, configured choices pass through unchecked. IDs are matched before labels without case, and conflicts are decided using the host’s IDs. A start asks metadata followed by only the selected model’s features after precedence and label resolution. Operation-local answers are shared inside a nested question scope and discarded at its end.

## Invariants And Boundaries

Successful provider/model inventories may retire parts they no longer name; failures preserve prior parts. Reclamation cases compare two inventory sizes and repeated stable states. Saved-only reads are guarded against network, lock and snapshot writes, and cannot admit a start without a fresh question. Concurrent-process cases check preservation of disjoint successful parts. These source assertions are not a new execution or timing result.

## Evidence

### Repo-Internal References

- A later view asks again and displays the changed host answer. [1]
- A new process recovers successful saved parts with their original read time. [2]
- A failed part retains its saved value while independently successful parts become fresh. [3]
- With neither fresh nor saved answers, configured values pass through unchecked. [4]
- Host IDs and labels match without case, and distinct resolved tier IDs conflict. [5]
- Nested operation scopes share one answer; another scope or later call asks again. [6]
- Successful smaller or empty inventories reclaim retired parts; failures preserve them at both tested sizes. [7]
- Start resolution asks metadata then only the final selected model’s features, sharing both inside the operation. [8]
- An unavailable selected-feature answer uses saved data or passes the unknown value through. [9]
- Saved reads neither query nor write; a start cannot treat that snapshot as its fresh answer. [10]
- Concurrent processes retain their disjoint successful catalog parts. [11]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
