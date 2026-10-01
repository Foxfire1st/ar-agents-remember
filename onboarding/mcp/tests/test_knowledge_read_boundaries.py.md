# mcp/tests/test_knowledge_read_boundaries.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The read's real boundaries: a real Git tree, a real snapshot identity, a real publication.** Twenty
nodes in `integration` (row `mcp/tests/test-evidence-lanes.toml:157`) — the properties the ordinary unit
path cannot fail from outside, because they need real committed bytes, a real database file and a real
publication to exist at all.

941 lines. It held the path cases until fix round 2 pushed it past the 1 200-line limit, at which point the
path cases moved to `mcp/tests/test_knowledge_read_paths.py` rather than the limit being waived.

## Code Commentary

### Logic

**The seven anchor observations, against real committed bytes** (`:157`–`:464`):

- the fixture's tree really holds the blobs its anchors record (the premise, measured as a fact rather than
  asserted from prose);
- `exact_recorded_blob` when the requested tree holds the recorded blob;
- `recorded_blob_mismatch` when the path changed, **with the old claim never promoted**;
- `path_absent` for a path the requested tree does not carry, **with the recorded claim and its blob
  identity preserved**;
- `not_requested` when no tree was named, **still carrying every recorded identity**;
- `recorded_object_unavailable` for an unavailable tree, substituting nothing;
- `unsupported_locator` remaining visible while the blob is still observed, and a non-blob tree entry
  reported **as an entry** and never read as source bytes.

**The snapshot, namespace and schema refusals** (`:498`–`:575`, `:763`–`:826`): a context naming another
namespace refuses and names both identities; a context whose logical digest is not the file's refuses; an
**absent database refuses as an unavailable input rather than as empty knowledge**; and a context
declaring another schema generation refuses before a page is built — the node that also asserts the
digest-only variant, which is what shows why the digest comparison cannot stand in for the schema
comparison.

**The continuation-binding family, each with its own positive control** (`:576`–`:892`): another selector,
another context or policy, **another manifest** (with the walk asserting at every step that the
continuation a page hands back carries the manifest that page declared), a position past the end of the
selection, an altered declared snapshot, and the control that a continuation against its own snapshot
continues the same manifest. **No one of these returns a partial page.**

**The read-only property, measured on a real file** (`:893`): a refused read of a real database leaves the
file byte-identical.

**The task-free baseline read** (`:465`): a context with `task_ref=None` serves a page and reaches the whole
selected scope — planning can read recorded knowledge with no leaf and no enclosure.

### Conventions

- `pytestmark = pytest.mark.integration`. The module's registration is a precondition: an unregistered
  `test_*.py` module makes `load_lane_manifest` refuse the repository, which the collection hook turns into
  a collection error.
- The real Git tree is built in `tmp_path`; no case touches the checkout or the network.
- A refusal node asserts the **code** and, where the code alone would be ambiguous, the detail's named
  comparison.

### Invariants And Boundaries

- **The one honestly unasserted branch is disclosed, not counted.** `read_anchors._tree_entry`'s
  **non-zero-exit** branch is reachable by no input on this host and is an explicitly disclosed unasserted
  defensive branch (L9 ledger **A6**). A published claim that a mutation made it reachable was **withdrawn**
  by the leaf's evidence erratum, because the kill that appeared to prove it also appears with the
  production line untouched. **Do not read that branch as coverage.** The `OSError` half is driven by a
  case in `mcp/tests/test_knowledge_read_paths.py:539`.
- **A guard that is reachable and verdict-changing but has no killing node is reported, not claimed.** This
  module reports the one such line it knows of through the ledger rather than presenting it as protection.
- **Boundary.** This is a test module. It declares one lane, asserts behaviour and owns no production
  contract.

### Todos

None recorded. The disclosed non-zero-exit branch above is L9's, not this module's to close by assertion.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The premise node: the fixture tree really holds the blobs its anchors record. [1]
- **The four blob-observation nodes (`exact`, `mismatch`, `path_absent`, `not_requested`).** [2]
- **The unavailable-tree and unsupported-locator nodes, and the non-blob entry node.** [3]
- **The task-free baseline read node.** [4]
- **The namespace, digest and absent-database refusal nodes.** [5]
- **The schema-generation node, which also asserts the digest-only variant.** [6]
- **The continuation-binding nodes, each with its own control, and the manifest node that verifies every page's own cursor.** [7]
- **The read-only property, measured on a real database file.** [8]
- **The disclosed unasserted defensive branch this module does not count as coverage.** [9]
- The lane row this module occupies. [10]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
