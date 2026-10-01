# mcp/src/agents_remember/memory/knowledge/durable_evidence.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Publishing durable evidence, and the post-cleanup read-back that is the only proof it survived. This
module moves bytes to a named destination, records the reference a later reader needs, and reports
what it found when it read them back — a publication mechanism, not a claim about the artifact's
content.

## Code Commentary

### Logic

`publish_durable_evidence` builds its destination **from the task root only** — `_TASK_RELATIVE_REPORTS`
is `("notes", "reports")` under the task root, following the shipped curator-coherence route — hashes
the bytes and returns a `DurableEvidencePublication` carrying the exact destination, the digest, the
byte count and the file name; `reference` and `digest` are the machine-readable publication reference.
`_require_one_file_name` refuses any name that is not one plain file name, so `../escape.md`,
`sub/dir.md`, `..` and `""` are unrepresentable rather than merely discouraged.

`read_back_evidence` re-reads the destination and returns an `EvidenceReadBack` with a **state** —
`matched`, `missing`, `mismatched` or `unreadable` — rather than a boolean, because "the bytes are not
there" and "the bytes are different" are different facts and neither is "published". `blocked_reason`
renders the destination, the expected digest and the observed state for the failure direction.
`enclosure_reports_removed` is the read-back of the enclosure-local directory after cleanup.

`durable_reports_root(task_root)` is the **root itself, exported as a decision rather than a
convenience** (`:58-69`). The single-file publication above stays the route for one artifact; a producer
whose evidence is a **directory** of related files roots that directory here instead of restating the
path, because "the enclosure root and `<worktree_group>/` are both removed by cleanup, so a second module
that spelled this path for itself would be a second place where 'durable' could drift away from the one
that is". Its first consumer is the durable comparison generation, which publishes one directory per
generation under `<task_root>/notes/reports/comparison-generations/<leaf>/<generation-id>`; the function
returns exactly `Path(task_root).joinpath("notes", "reports")`, the same `_TASK_RELATIVE_REPORTS` value the
publisher builds its destination from, so the two cannot diverge.

### Invariants And Boundaries

- **The durable root has exactly one definition, and it is exported.** `durable_reports_root` returns
  `_TASK_RELATIVE_REPORTS` joined onto the task root, and it is the same value the single-file publisher
  builds its destination from; a directory-shaped producer (the comparison generation) roots itself here
  rather than spelling `notes/reports` again. Calling it does not publish anything and grants no name
  validation — that stays with `_require_one_file_name` on the publication path.
- **The destination is `<task_root>/notes/reports/`**, outside the enclosure root and outside
  `<worktree_group>/` by construction. `DURABLE_EVIDENCE_REFUSED_DESTINATIONS` names the two places a
  retention claim may not rest on — the enclosure's own `reports/` (removed at cleanup for a leaf
  contract) and the terminal enclosure archive (fixed content set) — so neither is reachable by
  accident and a case can assert neither is ever produced.
- **Retention is proven by a read-back, not by code inspection.** The measurement is mandatory rather
  than reassuring, which is why the publication records the digest *with* the destination.
- **A failed or mismatching read-back is a blocked terminal state**, never reported as published.
- Nothing here decides *what* the evidence says.

### Todos

- The terminal half of this module's own contract is an owning-seat operation: the post-cleanup
  read-back of a real leaf must be run after cleanup, which no code path can perform for itself. The
  seed half — publication, and the read-back mechanism in both directions — is measured by this
  leaf's cases.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The two destinations a retention claim may not rest on, named so neither is reachable by accident.** [1]
- **The durable root, exported as the one decision a directory-shaped producer must root itself at.** [2]
- **Its first consumer: the comparison generation, which derives its whole layout from this root rather than restating it.** [3]
- **The publication record a later reader is given: the exact destination, the digest, the byte count and the machine-readable reference.** [4]
- **The publication itself: the destination built from the task root and the digest hashed from the bytes written.** [5]
- **The read-back result, whose state distinguishes "the bytes are not there" from "the bytes are different", and the blocked reason that renders the failure direction.** [6]
- **The read-back operation itself.** [7]
- The destination rule that makes a traversal or a nested name unrepresentable. [8]
- The enclosure-local read-back the cleanup direction is measured with. [9]
- The shipped curator-coherence route that owns "leaf evidence parked where it survives". [10]
- The cleanup that removes an enclosure-local `reports/` directory, which is why that path is refused. [11]
- The terminal archive's fixed content set, which is why it is not widened. [12]
- **The boundary cases that measure both directions: a published artifact reads back matched, a missing destination is blocked, and changed bytes are mismatched.** [13]
- The boundary case that proves the destination is outside the enclosure and the archive by construction. [14]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The destination is a path under the
coordination task root, which is outside both the code and the memory repository.

No meaningful cross-repo references found.
