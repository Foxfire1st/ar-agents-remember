# mcp/src/agents_remember/application/knowledge_worklist/generated_copies.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Read the repository candidate's generated-copy declaration and attach each declared payload's canonical path and byte-equality fact to the knowledge worklist. This is candidate-owned evidence, not a lookup of installed runtime package data or an exemption for arbitrary equal files.

## Code Commentary

### Logic

`generated_copy_facts` obtains the candidate blob inventory and symlink set, then asks `CodeObjects.tree_entry_mode` for the exact raw `generated-copies.json` entry **before** consulting the filtered blob map. A present declaration must have regular-file mode `100644` or `100755`; a directory, empty tree, tree of empty subtrees, symlink or gitlink is a named `CodeReadError`, not canonical absence. This check runs even with no requested payload paths or equal base/candidate trees. True declaration absence returns no suppression facts. Invalid JSON/schema data and unreadable declaration objects are named errors; the full worklist's caller reports incomplete input.

For each supplied path under a declared target, the parser's ignore-name and ignore-suffix rules are applied. The target root itself is not a payload. The relative payload path maps to the declaration's canonical source directory. `matches` requires both candidate blobs, exact blob identity and neither side being a symlink; it does not follow a link or classify an ordinary undeclared document as a generated copy. A declared divergent payload retains its canonical binding with `matches: false`.

Full worklist production suppresses only equal declared copies. When equal-change grouping coalesces paths, it retains each member's generated-copy binding and both source/base blob populations rather than depending on whether the representative happens to be a generated copy. This module supplies facts; the worklist's grouping and suppression consumers own those uses.

### Invariants And Boundaries

- Declaration presence comes from the raw exact entry, not the recursive leaf-only inventory. The shared recursive tree reader is not broadened globally to include trees.
- A malformed or nonregular declaration is incomplete input even when there is no incremental code change; only genuine absence is the unchanged no-declaration path.
- Equal blob IDs on symlink entries are insufficient: generator output is not the link's target-text blob.
- No installed package declaration or manually supplied observation becomes the candidate's authority.
- The source fixtures below describe executable predicates; this card does not claim to have run or independently accepted them.

### Todos

None recorded for this source contract. The nonrecursive presence check is the implemented empty-tree repair, not deferred work.

## Evidence

No Domain Documentation source is configured for this repository. The governing design is MIK-R55@v1 rule11 and the L54 round3 C12 repair; task evidence is not presented as a code-tree directory.

- Raw declaration mode is checked before filtered blob lookup, then per-payload canonical/equality facts are derived from the candidate. [1]
- One bounded nonrecursive Git entry read observes even a tree with no recursive leaves. [2]
- Full worklist fixtures retain canonical and ordinary changes, suppress only equal declared copies and restore a divergent copy's obligation. [3]
- Grouped members keep their canonical bindings and complete source/base populations regardless of the representative. [4]
- Both source-side and target-side symlinks retain full worklist obligations even when their link blobs compare equal. [5]
- Invalid JSON, nonempty directories and symlink declarations are named incomplete; true absence supplies no suppression. [6]
- A gitlink declaration is incomplete in both changed and equal-tree cases. [7]
- Native empty-tree and nested-empty-tree fixtures use equal base/candidate trees and require named refusal plus an incomplete full worklist. [8]
