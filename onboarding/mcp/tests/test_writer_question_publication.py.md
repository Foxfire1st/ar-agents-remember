# mcp/tests/test_writer_question_publication.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Describes keyed reconsideration-question publication through the native task-document owner and its rollback/concurrency boundaries.

## Code Commentary

Fixtures author a real enclosing master and question port. Assertions distinguish dry run, keyed append/reword and an intervening question; returned master-sync failures and settings-root mismatches must refuse without memory publication. Multi-raise uses one validated keyed batch, retaining foreign questions on failure and rewording keys on retry. A memory failure after successful question publication has its separately admitted keyed recovery. Native copy-refresh failure must reject nested publication and restore sources; a waiting foreign writer completes only after that failed batch restores its own changes. The competing-thread control observes its first lock attempt with `try_file_lease`, asserts exclusion while the owning batch holds the lease, and then enters the unchanged native exclusive lock. `HANG_GUARD_SECONDS` bounds event waiting and joining; a short elapsed-time delay is no longer the exclusion oracle.

## Invariants And Boundaries

Do not conflate refused question publication (no own append/replacement) with the explicit later memory-write-failure exception. Thread/event and injected-failure fixtures protect named opportunities, not universal timing or transaction acceptance, and none is executed by reading this card.

## Evidence Scope

No test execution, CODE/MEMORY grade, new producer capability or landing is claimed. No Domain Documentation source is configured for this slice.

## Evidence


- Describes keyed reconsideration-question publication through the native task-document owner and its rollback/concurrency boundaries. Do not conflate refused question publication (no own append/replacement) with the explicit later memory-write-failure exception. Thread/event and injected-failure fixtures protect named opportunities, not universal timing or transaction acceptance, and none is executed by reading this card. [1]
