# mcp/tests/test_durable_store_contract.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

In-process durable-store exclusion, rewrite and strict-read contracts.

## Code Commentary

### Logic

Real threads prove per-log exclusion, same-thread reentrancy and dismissal preservation during prune. A non-excluding flock double causes append refusal until locking works. Future-major rows block authority reads while projection retains readable rows. Compaction reports dropped records, unlocked replace refuses and interrupted rewrite preserves the old log without temp leftovers.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Thread mutex behavior is explicit rather than inferred from a shared file descriptor. Fault injection stays at the locking or atomic OS seam; it does not replace store logic.

### Todos

No file-local implementation change is requested by this reconciliation.

The dismissal/prune negative assertion follows an observed failed nonblocking acquisition of the actual held thread mutex by the dismisser. The rewrite remains parked until this contention is witnessed, then release allows the existing receipt and durable-dismissal assertions to run.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- A second thread is kept out of a log that is already held. [1]
- Taking a logs exclusivity twice on one thread does not deadlock. [2]
- A dismissal is not lost to a prune sweeping on another thread. [3]
- A store refuses the append itself and recovers once the lock works. [4]
- A future row stops the authority read and only costs projection a tick. [5]
- Compact drops what keep rejects and reports the count. [6]
- Replace records refuses an unlocked caller and changes nothing. [7]
- An interrupted rewrite cleans up too. [8]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.

- Actual mutex contention precedes the negative dismissal assertion. [9]
