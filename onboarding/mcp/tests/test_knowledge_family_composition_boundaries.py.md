# mcp/tests/test_knowledge_family_composition_boundaries.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The composition leaf's **boundary suite**: eight cases that measure the leaf's own claims against the
thing the leaf must not move. Every case protects a clause of `KS-R17@v1` §7 and §8, and the
load-bearing ones are boundary cases rather than traversals:

- **The retrieval read is untouched.** The composition table is not consulted for selection, and the
  cases measure that **twice** — by value (the same dataset and seed produce the same selected items,
  counts, revision groups, advertised frontier and manifest digest with composition edges present and
  absent), and by the call-site derivation the packet's own Open Truth Gap asks for.
- **The traversal is a different operation.** Following declared edges under a policy version builds a
  scope and reports the version it executed under; it never changes what `read_knowledge_scope`
  selects, and it refuses rather than truncating.
- **The projection reports stored facts.** A missing link, route or context is reported absent, and
  nothing is reconstructed from a label, a path, a member or the joint guarantee.
- **The escalation is recorded and not activated.** The R07 proposal exists as a named artifact with
  its subject and effect scope, so the edge cannot be forgotten and cannot be read as a retirement.

The preservation comparisons are **by value and by digest, never by inspection**: the shipped read's
own output model and the sealed family-revision `payload_digest` are the things compared.

## Code Commentary

### Logic

- `test_a_composition_graph_leaves_the_shipped_selection_exactly_as_it_was` — copies the real fixture
  dataset, adds two composition edges, and compares every preserved field by value across two seeds,
  with table counts confirming the edges are the only difference.
- `test_no_shipped_read_path_consults_the_composition_table` — the derivation half: `READ_PATH_SOURCES`
  names the read-path modules, and the case asserts the selection statements carry no composition
  table reference and that `family_view.py` never imports the traversal. The set is stated in one
  place so a later leaf that adds a read path has one place to extend.
- The **traversal cases** assert that a traversal reports the policy identity and version it executed
  under and widens nothing else; that an unknown, a malformed and a not-permitted policy are each
  refused **by name**; and that a traversal which would exceed its declared bound is **refused, not
  truncated**.
- `test_every_pre_existing_family_revision_keeps_its_payload_digest` — the seal is unchanged: the
  payload version constant and every pre-existing revision's `payload_digest` are asserted after the
  new tables exist.
- `test_the_r07_escalation_proposal_is_recorded_with_its_subject_and_effect_scope` — the escalation
  artifact must exist and state its subject, so an accidentally deleted escalation fails the suite.
- `test_the_application_seam_is_read_only_carries_the_operation_and_moves_no_selection` — the one
  case that drives the read-only seam end to end: the projection reports the recorded link with its
  policy version, the traversal carries `follow_family_composition` as its own operation, a refused
  traversal leaves the file **byte-identical**, and a family revision this namespace does not hold is
  a typed refusal rather than an empty report. The projection's absent-state assertions are driven
  here too, inside this case, rather than by separate cases of their own.

### Conventions

- Hermetic where it can be, integration where it must be: the selection-preservation case uses the
  registered read-scope fixture, and the boundary cases compare **digests and bytes** rather than
  describing behaviour.
- **Always run with `-o "filterwarnings=ignore"` on this host** — a pre-existing host condition, not
  this leaf's.
- The suite is a **consumer** of `knowledge-read-scope-cases`, `knowledge-facet-cases` and
  `knowledge-generation-cases`; it registers **no** new contract and **no** new artifact, so the
  catalogue's counts stay at **13 contracts / 54 artifacts**.

### Invariants And Boundaries

- **The escalation is recorded, not activated.** The case asserts the artifact's existence and its
  required content; it does not assert that the shipped read changed, because it must not.
- **Nothing here is a retirement.** No case deletes, skips, deselects or weakens a shipped assertion.
- **Boundary.** The write shape and the generation are the sibling module's; this one owns the
  boundary between the composed graph and the retrieval selection.

### Todos

None recorded. The R07 escalation awaits a developer ruling; nothing about the shipped read changes
until then.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The case that compares the shipped selection by value with composition edges present and absent, over two seeds.** [1]
- **The call-site derivation, stated as one extendable set so a later leaf that adds a read path has one place to extend.** [2]
- **The case that proves no shipped read path consults the composition table.** [3]
- **The case that proves a traversal reports its declared version and widens nothing else.** [4]
- **The case that proves an unknown, a malformed and a not-permitted policy are each refused by name.** [5]
- **The case that proves a traversal past its declared bound is refused rather than truncated.** [6]
- **The case that asserts every pre-existing family revision keeps its sealed `payload_digest`.** [7]
- **The case that asserts the escalation artifact exists and states its subject and effect scope.** [8]
- **The end-to-end seam case: the recorded link is reported, the refusal leaves the file byte-identical, and a missing revision is refused rather than reported empty.** [9]
- The contract whose consumer list this module joined for its read-scope fixture. [10]
- The lane row this module is registered under. [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
