# mcp/tests/test_knowledge_gate_routes.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Tests of the invariant gate at every public route that commits or records a leaf's memory. Each route test
enters through the route's own entry point, so removing that route's gate call makes it fail: the worktree
closeout, direct landing apply and preview, record landing, and the master and checkpoint landing. The
module also holds the tests of the gate's read set, its memo key and its treatment of Git failures. All
of them use the gate module's fixture world (`Gated`).

## Code Commentary

### Routes

- A leaf history file that was closed by hand is refused at closeout validation and at record landing.
- The worktree closeout refuses an invalid candidate, restores the history file it had closed, and commits
  the file closed once the candidate is valid.
- Record landing, the master and checkpoint landings, and direct landing preview and apply each refuse
  through their own entry.
- Direct landing: an input conflict or a failed create restores the closed file; an exact retry of a
  generation in flight reaches it before the gate; cancelling restores the file the generation closed but
  never a file edited since; another generation's request never replaces a kept closing; a closing kept by
  a call that ended before the create is restored at the next apply; an unreadable closing receipt is a
  named refusal; an unwritable receipt restores the file and admits nothing; a closing the memory line
  already holds is never restored.
- The exact tree is checked again after the closeout and the direct landing have closed the leaf's file. A
  sibling's file that was closed in the base is not checked again at a leaf route. A hand-committed closed
  file with a subject that does not exist is refused at master landing.

### Inputs and failures

- `test_every_file_read_is_in_the_read_set_and_a_conflicting_read_is_never_kept` calls
  `trace_context(world.contract)` inside a recording block and checks the rows exactly: the memory
  worktree's `system/settings.md` is recorded as `absent`, the contract is recorded with the SHA-256 of its
  bytes, and the coordination root's `system/settings.md` has no row, because the resolution stopped
  before it opened that file. The test then shows that a path recorded at two identities becomes a
  conflict, that a verdict with a conflicting read takes no memo slot, and that a kept verdict is not
  served after a recorded file changed.
- `test_the_memo_key_holds_the_parent_tip`: the same trees against another parent tip are another key, and
  three evaluations over two tips compute twice.
- A Git read that fails inside a predicate or the validator is never a verdict. A marker probe that Git
  cannot answer is never read as unconverted memory. A timed-out blob read or an unverifiable entry
  refuses a master landing.
- A recorded blob that the store lacks is named as unavailable where it is raised; a Git failure while
  asking for a recorded blob is `incomplete`, is never kept, and is named by the trees and by the lane.
- Record landing on unconverted memory does not read the landed commit. A record the leaf wrote before
  is judged as new against the parent line, whose tip the route reads itself.

## Evidence

- The module docstring: every route test enters through the route's own entry. [13]
- The closeout refuses, restores the file and commits it closed once valid. [14]
- Record landing refuses through its route entry. [15]
- Direct landing preview and apply refuse through their entry. [16]
- The recorded rows of the settings resolution, and a conflicting read that is never kept. [17]
- Another parent tip is another evaluation. [18]
- A failed Git read inside the gate is never a verdict. [19]
- A marker probe Git cannot answer is never unconverted memory. [20]
- The settings resolution whose rows the read-set test checks. [21]
