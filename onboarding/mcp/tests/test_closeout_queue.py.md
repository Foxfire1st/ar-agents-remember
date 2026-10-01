# mcp/tests/test_closeout_queue.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Disposable task, door and projection fixture shared by lifecycle tests.

## Code Commentary

### Logic

`QueueFixture.close_contract` is removed: fixture users cannot create code, memory, and ledger
commits through that obsolete convenience method. The constructor still seeds a tracked cache
into isolated history. That starting state supports migration and old-history operation checks;
real current closeout behavior belongs to the operation exercised by each consumer.

QueueFixture creates real code and optional external-memory repositories, task topology, contracts and shared priority/judgment data. Its helpers declare doors and construct the source/projection conditions required by consumers. The file contains no retained standalone queue tests.

Since 260831-LOCR-L36 the fixture also authors and starts canonical leaves the way the workflow does.
`author_unstarted_leaf` cit:([`author_unstarted_leaf`], mcp/tests/test_closeout_queue.py:319-369)
commands one more canonical leaf **without starting any of its work**: the master's subtask row and
the leaf's own task document are written — an atomic master's review scope has to resolve every
commanded leaf's document — and the leaf's judgment and priority register rows are added, but no
enclosure contract, branch or worktree exists yet. The commanded id is recorded on
`QueueFixture.unstarted_leaf_a`. `start_leaf` cit:([`start_leaf`], mcp/tests/test_closeout_queue.py:371-441) then starts one authored leaf from its
master's branches **as they now stand** (a real enclosure, leaf document, worktrees and branches,
based on the master's current tips rather than the base it had when the leaf was first commanded),
publishes the lifecycle operation location and writes curator evidence. `declare_leaf`
cit:([`declare_leaf`], mcp/tests/test_closeout_queue.py:626-655) declares the closeout door for a leaf that is not yet the
master's current one, reading its own canonical grade from the priority register it was authored with
and naming the master whose command it executes.

### Conventions

This card describes the current uncommitted LCA-L9 fixture candidate. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Synthetic upstream curator evidence in the convenience declaration is fixture-only; producer-backed memory tests call the real door owner with actual coherence instead. No helper declaration grants production acceptance.

**`_leaf` must carry both derived fields, and that is a correction rather than a convenience.** Since
260913-LCA-L5 a leaf document with an exact enclosure address but no `seriesContractPath` refuses
closeout by name (`task-enclosure-binding-master-link-missing`, raised by
`worktrees/task_leaf_binding.py` — see that card). The fixture previously withheld the field, which
modelled the damage state start repairs rather than the document `task_doc` actually writes against a
leaf contract; four unrelated closeout cases began refusing until it was corrected. Any future fixture
that authors a started leaf must bind `seriesContractPath` (and `enclosures[]`) for the same reason, and
a test that deliberately omits it is testing the refusal, not the happy path.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Retired the unused three-commit close_contract helper while retaining historical cache seeds and task/door fixture behavior. [1]
- The retired three-commit `close_contract` convenience method is gone; what remains is the fixture class the non-queue lifecycle suites build their task, door and projection state from. [2]
- Master. [3]
- The master builder writes a canonical atomic master document with the given execution nature and one commanded subtask row. [4]
- Leaf, carrying both derived fields exactly as `task_doc` stamps them against a leaf contract. [5]
- Judgment row. [6]
- The judgment-row builder renders one canonical judgment register row for a candidate and priority. [7]
- Priority row. [8]
- The priority-row builder renders one canonical priority register row for a candidate and priority. [9]
- Judgment table. [10]
- Priority table. [11]
- Grade. [12]
- The grade builder returns the priority and judgment id pair the register rows reference. [13]
- Queuefixture. [14]
- The retained task/door/projection fixture class that non-queue lifecycle suites construct. [15]
- Command a canonical leaf with no work started: subtask row, leaf document, judgment and priority rows only. [16]
- Start an authored leaf from its master's current tips, creating the enclosure, worktrees and branches. [17]
- Declare the closeout door for a leaf that is not yet the master's current one, with its own authored grade. [18]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
