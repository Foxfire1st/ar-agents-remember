# mcp/src/agents_remember/application/reviewer_worklist_child.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Own the parent wrapper and child entry point for exact-tree worklist computation and its accompanying review facts. The kernel process owner still owns execution/coalescing and reply admission; this module does not introduce a second worklist implementation or a persistent result cache.

## Code Commentary

`isolated_leaf_worklist` serializes the contract, candidate trees and captured base, derives the serving build identity, and optionally adds a `review` payload when supplied `trees`. It calls the supplied process owner or the module’s default owner (registered for shutdown at interpreter exit). Returned read observations are replayed **before** the error check. A computation error raises `WorklistProcessError`; otherwise a non-None review result is merged into `(document or {})` under `_review`. Thus a review-facts adjunct can exist without a worklist-state field; that is not an invented complete worklist. Without the adjunct, the original document/None is returned.

`_contract` requires exactly the dataclass’s declared fields and reconstructs paths/tuples from their type hints. `_run` verifies operation/request digest and child-versus-request build before its computation try-block. Under recorded reads plus scoped shared-blob/Git-object/tree-observation/classification contexts, it reconstructs optional review trees. A recorded comparison reads the persisted leaf worklist; a live/no-review request calls the existing `leaf_worklist` owner with `persist=False` and the supplied candidate/base. If review trees exist, `leaf_facts` is computed in the same recording context.

Caught computation exceptions return `document: null` and a typed-name/message error with observations up to failure. Request/build/contract failures before that try-block are not promised this conversion. The reply explicitly includes operation, request, source, module, pid, document, **review**, reads, computation interval and error. `main` arms lifetime, disables cyclic GC, reads/writes JSON and maps `WorklistBuildMismatch` to the imported dedicated exit status.

Actual BASE/current source adds optional review input/result, recorded/live branching and scoped sharing contexts. The old “document only”, “always recompute leaf_worklist” and “no cache of any kind” wording is superseded; the complete previous account is retained historically. This card gives no new process protocol, suite, performance or memory-acceptance grade.

## Evidence

No domain documentation source is configured. Current repository source establishes these local claims; former test/timing accounts below remain historical only.

- Default process ownership, optional review input, read replay before error and document/adjunct return. [10]
- Exact contract fields and typed path/tuple reconstruction. [11]
- Request/build validation, shared recorded computation, recorded/live owner branch and explicit reply fields.
- The one child entry point owns lifetime, JSON framing and dedicated build-mismatch exit.

## Historical predecessor account

The full previous text is preserved below with nested headings and inert prose citations. Superseded signatures, old read/return paths and past execution observations are not current assertions.

### mcp/src/agents_remember/application/reviewer_worklist_child.py

#### Governing Overview

[application route overview](overview.md)

#### Purpose

The two ends of the reviewer's isolated worklist computation. `isolated_leaf_worklist` is the parent's
side: it sends one request through the kernel's process owner and takes the answer and its read evidence.
`main` is the child's side, run as `python -P -m agents_remember.application.reviewer_worklist_child`: it
reads one request from standard input, runs the one worklist implementation `leaf_worklist` on the trees
it was given, and writes one reply to standard output. The module holds no second worklist implementation
and no cache.

#### Code Commentary

##### Parent side

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

##### Child side

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

#### Evidence

- The default owner for callers without one, stopped at interpreter exit. (historical reference 1)
- The parent side: payload, build identity, one compute call, replayed reads, error or document. (historical reference 2)
- The contract is rebuilt from exactly its own fields. (historical reference 3)
- The child side: request and build checks, the one worklist call under both recorders, the reply. (historical reference 4)
- The entry point: lifetime, collector, request, reply, and exit status 75 on a build mismatch. (historical reference 5)
- The process owner's compute call and its reply validation. (historical reference 6)
- The child's document, reads and body equal the in-process computation at two sizes; the child does no second capture, pairing or conversion. (historical reference 7)
- The bytes the child consumed reach the parent for a changed-and-restored, a twice-read, an absent and an unreadable task document. (historical reference 8)
- A child that exits with the build-mismatch status, or answers with another source, asks for a dashboard restart. (historical reference 9)

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/reviewer_worklist_child.py:104-151 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit c702e1c2e111ec6e07c6b68a78a5d05add8aceab; mcp/src/agents_remember/application/reviewer_worklist_child.py:154-167 - the region it cited is not in the file at the candidate and no re-point was possible. Retired means the anchor no longer stands, not that the cited subject was deleted.
