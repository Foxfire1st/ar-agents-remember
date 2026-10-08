# mcp/src/agents_remember/application/review_comparison_generation.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Decode retained historical comparison JSON and preserve its exact source identities, artifact references and archival ownership. Normal reviews bind code/memory trees; no new canonical dataset generation is published here.

## Code Commentary

### Logic

The manifest validates recorded bindings, the seal and derived identity. `read_manifest` additionally checks agreement with its containing directory. Retained knowledge bindings remain historical metadata and authorize no canonical snapshot read. Discovery lists readable records without guessing damaged fields.

Deletion-record reads/writes stay bounded to the task root and distinguish a missing record from an unreadable one. These archive operations preserve the historical generation identity, not the current availability of its former datasets.

### Invariants And Boundaries

No new dataset freeze/publication route is provided. Tampered source records are refused rather than retargeted. Current memory trees never replace historical unavailable knowledge halves. Source and artifact identities remain independently inspectable.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in this module's own docstring and functions, in the four sibling
modules that produce, retain, reclaim and resolve a generation, and in the cases that measure the whole
journey. Three details a reader should carry: the durable root is **asked of its owner**
(`durable_evidence.durable_reports_root`) rather than restated; the id is re-derived from the seal *and*
checked against the directory name; and `recorded_at` is outside the seal on purpose, which is what
makes an exact retry converge.

- The module's own statement of what it owns (the record, the layout, the deletion record) and of the separate responsibility next door. [1]
- The published surface: version, layout literals, the eleven models, the path helpers, the reads and the discovery functions. [2]
- **The layout, named once**, and the two typed-absence spellings with their reason for being distinct from a failure. [3]
- **The fields the seal does not cover, and why each is excluded.** [4]
- **One retained snapshot: a generation-relative path, the digest of the bytes written, and the deletion owner plus bounded scope that may delete it.** [5]
- **The validator that makes the packet's non-conforming example unconstructible: identity and bytes travel together, and a non-retained side states its reason.** [6]
- **The source binding: the capture owner's own identity carried verbatim, the custody measurement, the names it was measured against, and the pin's agreement with the custody.** [7]
- **The scope binding: the owner-produced inventory's state, digest and population, plus the selection that must name its selector.** [8]
- One cited owner-produced artifact as a task-relative, digest-bearing reference. [9]
- **The records binding, which asserts what the composition supplied and deliberately not whether an owner published none or could not be read (R14's fact).** [10]
- Every policy version as a constant its owner declares, never a version derived here. [11]
- **The lineage: one predecessor named by id *and* manifest digest, plus the two optional owner digests.** [12]
- **The record itself, the seal it carries, and the four self-agreement checks including the re-derived generation id.** [13]
- **The unavailable-history record an explicit deletion writes, including the custody measured *before* a pin was released.** [14]
- **The whole layout, derived from the one durable root owner.** [15]
- **The derived generation id, and the one function that seals and validates a field set together.** [16]
- **The two-statement read: the record's own validation plus the containing directory's agreement with the id it claims.** [17]
- **The deletion reads and the canonical-bytes write, with "present but unreadable is not absence" stated in the code.** [18]
- **Discovery: the one list of published-looking directories, and the pass that skips an unreadable record instead of guessing its fields.** [19]
- **The one durable-root owner this module asks instead of restating `<task_root>/notes/reports`.** [20]
- The R05 constant imported rather than re-spelled, so the accepted spelling and the recorded one cannot drift. [21]
- The owners whose values the manifest carries rather than re-derives: the capture identity, the resolved pair, the inventory and the comparison identity. [22]

- Historical source is preserved without reading a canonical dataset; tampered source is refused rather than retargeted. [23]


The following declarations carry the changed boundary.

- Counts and optional assessment availability remain separate recorded facts. [24]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The record is published under the coordination
task root, which is outside both the code and the memory repository, and the repository it *names* is a
path the source binding records rather than something this module resolves.

No meaningful cross-repo references found.
