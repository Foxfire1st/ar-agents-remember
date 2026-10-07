# mcp/src/agents_remember/application/knowledge_gate/memo.py

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

The bounded in-process memo of the invariant gate's verdicts. `evaluate_leaf_gate` asks it before it
computes and offers every computed verdict to it. A verdict is kept under a key of exact identities and
together with every row the evaluation recorded outside the Git trees, and it is served again only while
all of those rows still hold. The worktree layer's gate port (`KnowledgeGate.leaf_refusal` in
`adapter.py`) and the memory-quality controller both call `evaluate_leaf_gate`, so they share these
verdicts.

## Code Commentary

### The key

`memo_key(contract, candidate, parent_memory_tip, leaf_memory_head)` returns a `GateMemoKey`, or `None`
when an input cannot be identified; the gate then computes without the memo. The key holds:

- the candidate's code tree and memory tree;
- the contract's path and the SHA-256 of its bytes;
- the parent line's memory tip and the leaf's own memory `HEAD`;
- the SHA-256 of the leaf's task document, found through the strict lookup `strict_leaf_doc` (an empty
  digest input when the leaf has no document);
- the build stamp (`measuring_build_stamp`) as sorted JSON.

An unreadable contract, a leaf document that cannot be established, or a build stamp that cannot be
produced gives no key.

### Serving and keeping

- `remembered(key)` returns the kept verdict only when it is at most `MAX_AGE_SECONDS` old and
  `_Kept.still_read_the_same()` holds. That check is `changed_observations` over the kept rows: every
  recorded path resolution and existence probe is repeated first, and recorded files are hashed again
  only when all of those still give the recorded answer. A requirement packet whose locator resolves to
  another file at the time of the check is therefore a miss even when the other file has the same bytes,
  and the bytes behind the other target are not read for the check. A manifest that appeared or vanished, a newly approved
  version and edited settings are misses as well.
- `remember(key, result, reads)` keeps a verdict only when `result.memoisable` is true and the rows hold
  no failed observation (`has_failed_observation`: a conflict, or an unreadable row). A verdict behind
  which an input could not be read, or was read at two identities, is returned to the caller and computed
  again at the next evaluation. A refused verdict over complete inputs is kept like a pass.

### Bounds

`GATE_MEMO` is a `BoundedMemo` of `CAPACITY` 16 verdicts, least recently used first out, and
`MAX_AGE_SECONDS` is 900.

## Evidence

- The module docstring: what the key names, the inputs outside the trees, the bounds, what is never kept. [10]
- The two bounds. [11]
- The key's fields. [12]
- A kept verdict is current when no recorded observation changed. [13]
- The key from contract bytes, the strict task lookup and the build stamp. [14]
- A kept verdict is served only when young enough and unchanged. [15]
- Only a memoisable verdict without a failed observation is kept. [16]
- The gate asks the memo, records its reads and offers the verdict. [17]
- A warm pass becomes the refusal when the packet locator is retargeted to a file with the same bytes. [18]
- The gate's verdict follows the packet in both directions, and a repeated evaluation gives the same verdict. [19]
- A verdict behind an unreadable contract read keeps its answer and occupies no memo slot. [20]
- Every file read is in the read set and a conflicting read is never kept. [21]
- The same trees against another parent tip are another key and another evaluation. [22]
- The worktree layer's gate port calls the gate. [23]
