# mcp/src/agents_remember/application/reviewer_worklist_child.py

## Governing Overview

[application route overview](overview.md)

## Purpose

The two ends of the reviewer's isolated worklist computation. `isolated_leaf_worklist` is the parent's
side: it sends one request through the kernel's process owner and takes the answer and its read evidence.
`main` is the child's side, run as `python -P -m agents_remember.application.reviewer_worklist_child`: it
reads one request from standard input, runs the one worklist implementation `leaf_worklist` on the trees
it was given, and writes one reply to standard output. The module holds no second worklist implementation
and no cache.

## Code Commentary

### Parent side

- `isolated_leaf_worklist(contract, candidate=..., base=..., processes=None)` builds the payload from the
  contract's fields, the `CandidateTrees` and the `CapturedBase`, with every path as a POSIX string. The
  build identity comes from this process's serving build (`process_serving_build`) through
  `build_identity`.
- The request goes to `processes.compute`. A caller that passes no owner uses the module's own
  `DIRECT_WORKLIST_PROCESSES`, which is shut down at interpreter exit (`atexit`). The dashboard passes the
  owner it composed and shuts it down itself.
- The reply's `reads` are replayed into the caller's recording block (`replay_reads`) before anything
  else, so the parent's currentness check sees every row the child recorded, also when the computation
  failed.
- A reply with an `error` raises `WorklistProcessError("reviewer worklist computation failed: ...")`.
  Otherwise the function returns the reply's `document`: a worklist document, or `None` when no worklist
  applies.
- The function never computes a worklist in the calling process.

### Child side

- `main` arms the child's lifetime first (`arm_child_lifetime`), switches the cyclic garbage collector
  off, loads the request and writes the reply as JSON. A `WorklistBuildMismatch` is printed to standard
  error and ends the child with exit status 75 (`EXIT_BUILD_MISMATCH`).
- `_run` checks the request before it computes: the operation name, and that the request's digest is the
  digest of the rest of the request. It derives its own build identity the same way the parent does and
  raises `WorklistBuildMismatch` when it differs from the one in the request.
- `_contract` rebuilds the `WorktreeContract` from the payload. The payload must name exactly the
  contract's fields; path-typed fields become `Path`, tuple-typed fields become tuples.
- The computation is `leaf_worklist(contract, persist=False, candidate=candidate, base=base)` inside
  `recorded_reads()` and `shared_blob_reads()`. With `candidate` and `base` given, the worklist reads the
  two candidate trees and the comparison's base commits as they are: it captures no worktree and pairs no
  memory commit, and an unconverted before memory is read from the already converted tree it was handed
  instead of being converted again. Nothing is persisted.
- An exception of the computation does not end the child. The reply then carries `document: null` and
  `error` as `"<type>: <message>"`, together with the rows recorded up to the failure.
- The reply has the keys `operation`, `request`, `source`, `module` (this file's resolved path), `pid`,
  `document`, `reads` and `computation` (the monotonic start and end of the computation) and `error`.

## Evidence

- The default owner for callers without one, stopped at interpreter exit. [1]
- The parent side: payload, build identity, one compute call, replayed reads, error or document. [2]
- The contract is rebuilt from exactly its own fields. [3]
- The child side: request and build checks, the one worklist call under both recorders, the reply. [4]
- The entry point: lifetime, collector, request, reply, and exit status 75 on a build mismatch. [5]
- The process owner's compute call and its reply validation. [6]
- The child's document, reads and body equal the in-process computation at two sizes; the child does no second capture, pairing or conversion. [7]
- The bytes the child consumed reach the parent for a changed-and-restored, a twice-read, an absent and an unreadable task document. [8]
- A child that exits with the build-mismatch status, or answers with another source, asks for a dashboard restart. [9]
