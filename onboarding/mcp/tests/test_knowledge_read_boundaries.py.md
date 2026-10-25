# mcp/tests/test_knowledge_read_boundaries.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The read's real boundaries: a real Git tree, a real snapshot identity, a real publication.** Twenty
nodes in `integration` (row `mcp/tests/test-evidence-lanes.toml:414`) — the properties the ordinary unit
path cannot fail from outside, because they need real committed bytes, a real database file and a real
publication to exist at all.

The historical path split moved cases to `mcp/tests/test_knowledge_read_paths.py` rather than
waiving the 1,200-line rail. Its recorded 941-line size describes that earlier split, not a current
source census or collected-case result.

## Code Commentary

### Logic

The fixtures use text-backed index projections, not a canonical knowledge database.
An index is keyed by its tree, so a second identical fixture cannot supply a foreign
namespace. `foreign_context` names a different namespace in both the context and its
snapshot; refusal still names the expected and observed identities and leaves the
row counts and logical digest unchanged; raw file bytes are not measured. Unsupported-locator setup uses the normalized `support`
role and finds its projected claim by the creation outcome ID. Selection-reason
checks use the fixture's single subject revision.


**The seven anchor observations, against real committed bytes** (`:203`–`:515`):

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

**The snapshot, namespace and schema refusals** (`:551`–`:625`, `:825`–`:903`): a context naming another
namespace refuses and names both identities; a context whose logical digest is not the file's refuses; an
**absent database refuses as an unavailable input rather than as empty knowledge**; and a context
declaring another schema generation refuses before a page is built — the node that also asserts the
digest-only variant, which is what shows why the digest comparison cannot stand in for the schema
comparison.

**The continuation-binding family, each with its own positive control** (`:628`–`:969`, with the schema pair at `:825`–`:903` described separately): another selector,
another context or policy, **another manifest** (with the walk asserting at every step that the
continuation a page hands back carries the manifest that page declared), a position past the end of the
selection, an altered declared snapshot, and the control that a continuation against its own snapshot
continues the same manifest. **No one of these returns a partial page.**

**The no-persisted-change property** (`:972`–`:1004`): namespace and page-budget refusals
leave row counts and logical digest unchanged. `_digest` (`:1103`–`:1108`) reads
`logical_digest` through a read-only handle; that mechanism is not a before/after
raw-file byte hash or equality assertion.

**The task-free baseline read** (`:518`–`:548`): a context with `task_ref=None` serves a page and reaches the whole
selected scope — planning can read recorded knowledge with no leaf and no enclosure.

### Conventions

- `pytestmark = pytest.mark.integration`. The module's registration is a precondition: an unregistered
  `test_*.py` module makes `load_lane_manifest` refuse the repository, which the collection hook turns into
  a collection error.
- The real Git tree is built in `tmp_path`; no case touches the checkout or the network.
- A refusal node asserts the **code** and, where the code alone would be ambiguous, the detail's named
  comparison.

### Invariants And Boundaries

- **Controlled lookup-exit coverage is distinct from natural-path reachability.** No
  path spelling on the described host naturally produces the non-zero `ls-tree` exit.
  The historical L9/A6 mutation kill was withdrawn because the same assertion killed
  with the production line untouched; it is not coverage evidence. The current path
  suite independently stages exit 128 in
  `test_a_lookup_that_answered_non_zero_is_unavailable_rather_than_an_absent_path`
  (`mcp/tests/test_knowledge_read_paths.py:579-680`), delegates the availability probe
  to the real runner, and asserts `recorded_object_unavailable` and the exact exit-status
  detail. This is a source-inspected controlled producer witness, not a new mutation
  kill or fresh execution result. The `OSError` producer has its separate case at
  `mcp/tests/test_knowledge_read_paths.py:471-576`.
- **Boundary.** This is a test module. It declares one lane, asserts behaviour and owns no production
  contract.

The selection-reasons/manifest-identity case compares the complete selected result against a
version with its reasons stripped and retains its positive controls. The repaired fixture passes
`subject_revision_id`, not the removed `base_revision_id`; this pointer repair is not a new mutation
verdict and does not reinstate the withdrawn A6 claim.

### Todos

None recorded. The historical withdrawn mutation attribution remains withdrawn; the current controlled producer assertion belongs to the separate path suite.

## Evidence

- Foreign context names both namespaces; unsupported-locator setup uses a normalized role and projected claim ID. [11]

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


- Schema-generation and digest-only guards assert their distinct refusal identities and no page. [6]

- **The continuation-binding nodes, each with its own control, and the manifest node that verifies every page's own cursor.** [7]

- Namespace and page-budget refusals preserve row counts and logical digest; the read-only digest handle is not a raw-byte measurement. [8]



- Controlled non-zero lookup exit asserts unavailable resolution and exit-status detail; historical withdrawn kill and natural-path nonreachability are separate. [9]






> Retained earlier citation wording: - The read boundary module occupies the integration lane row; registration is not execution evidence. [10]




### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

- The read boundary module occupies the integration lane row; registration is not execution evidence. [10]
