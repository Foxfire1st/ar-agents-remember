# mcp/src/agents_remember/memory/knowledge/managed_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/managed_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T15:30+02:00 |
| lastVerifiedCommitHash | `a7076008db4772554123794392f84b51143004ec` |
| lastVerifiedCommitDate | 2026-09-18T16:14:01+02:00 |
| reviewedWorkingCandidate | `ar/260915-ks-l20` uncommitted staged source; base `9f88a6de572dc15bbed1802cf08b77c1193fb24c` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The managed, staged, non-destructive write path into a destination the substrate does not own:
`ManagedProjectionWriter` is the shipped `ProjectionWriter` port, and each of `Doc13:269`'s eight
vault-safety clauses is one behaviour here rather than a policy a caller has to remember — the
manifest is the only ownership authority and the destination is never enumerated, confinement is a
resolved comparison rather than a string prefix, collisions are refused before either artifact is
written, an escaping link is never followed for a write or for a delete, publication is a
stage-then-rename, a deletion needs both halves of the unchanged test, no recursive clean exists, and
an externally edited file is reported by kind and preserved. **It deliberately has no `rmtree`, no
recursive clean, no destination enumeration, no second authority on ownership, no string-prefix
confinement test and no renderer**: a writer instance is stateless between calls and re-reads the
destination's own manifest, it writes the bytes a caller already rendered, and the only route past an
external edit is the explicit per-path authorization the plan carries.

## Code Commentary

### Logic

**The manifest is the only authority on what the substrate owns, and the destination is never
enumerated.** `_read_prior_manifest` reads `PROJECTION_MANIFEST_NAME` from the resolved root, and
`ProjectionManifest` answers every ownership question through `output_for`, `retained_for` and
`recorded_digest_for`; no code path in this module lists the destination or walks it for candidates,
so a file the manifest does not list — the packet's own `user-notes/` example — is unreachable by
construction rather than by a filter somebody remembered to write. An unreadable manifest is
`MANIFEST_UNREADABLE`, refused rather than treated as absent, because treating it as absent would
silently abandon the ownership record and make every prior output look unowned; a manifest that is a
symbolic link is `ESCAPING_LINK` instead. `_DestinationState` computes each prior path's standing once
through `observe`, and `_Observation` classifies it as `file`, `link`, `absent`, `replaced` or
`unreadable` with a digest for the readable case, so one description of the destination is read by
every decision in the run. There is also no recursive clean: `_discard_staging` removes the staging
directory's own files and then the directories under it, never the destination, which is why the
module docstring can state that `rmtree` does not appear in it at all.

**Confinement is resolved, not string-matched.** `resolve_inside_destination` resolves the real path
of the output's parent through `os.path.realpath` and proves that parent is inside the resolved root,
then resolves the joined path itself and proves that is inside too, so a `..` segment, a symlinked
intermediate directory, a case-folded alias and a final component that is itself a link are all caught
by two comparisons rather than a prefix test — the module names `/vault/agents-remember-backup` as the
path that carries the configured root's text as a prefix and is not inside it. The syntactic half is
`require_confined_relative_path` in the vocabulary module, which refuses an absolute path, a
drive-qualified path, an empty or padded path, any `..`, `.` or empty segment, and a path naming the
staging directory; `_first_escape` runs that check first and re-stamps its refusal with the same
resolved root the resolving half names, so a caller always learns both the offending path and the root
requirement 5.2 asks for. A path that escapes is `destination_escape`, and nothing is staged.

**Collisions are reported before either artifact exists.** `detect_destination_collisions` groups the
plan's outputs by `canonical_destination` — the NFC-normalized, casefolded destination — and returns a
`Collision` carrying both destination-relative paths, the canonical form they share and both stable
identities; two records projecting to one identical path are reported through the same channel rather
than as one record's artifact overwriting the other's. `_first_collision` runs inside `write` before
staging and before the prior manifest is consulted, and returns a `DESTINATION_COLLISION` refusal
whose detail names the canonical form and whose `next_action` records that the substrate does not
invent a disambiguating suffix. The property is that the whole plan is refused rather than one of the
two being chosen, overwritten or renamed.

**An escaping link is never followed, for a write or for a delete.** `_crosses_a_link` asks whether the
destination entry itself is a symbolic link and whether any intermediate segment is one, then re-asks
the resolved-confinement question, so a link inside the destination that points inside it is still not
followed for a write. `_stage` reports such an output as a `ProjectionOutcome` in state `reported` and
continues with the remaining outputs, which is the packet's own acceptance case: one hostile
destination entry does not block the rest of the projection. `_remove_unchanged` refuses to delete a
path that is a link or is not a regular file, and `_read_prior_manifest` refuses a symlinked manifest
outright, so the same rule covers publication, retirement and the manifest itself.

**Publication is a rename inside one filesystem.** Every artifact is rendered into
`STAGING_DIRECTORY_NAME` by `_write_staged`, which creates only that artifact's own parents, and
`_publish` moves each staged file into place with one `os.replace` per output; the manifest goes
through the same discipline in `_publish_manifest`, written from `_manifest_bytes`, whose canonical
JSON (`sort_keys=True`, `ensure_ascii=False`, one trailing newline) makes two runs at one state
byte-identical. An interruption between staging and the first rename therefore leaves the prior
generation intact rather than a half-written mixture, and `_stage_and_publish` discards the staged
bytes on any `BaseException` before re-raising, so recovery is to re-run the projection rather than to
repair a partial state.

**A deletion needs both halves of the unchanged test.** `_retire` walks the prior manifest's own
outputs and skips every path the new projection still produces — even when the write to it was
withheld, because that path keeps its prior entry so the next run detects the same external edit
instead of forgetting it — and for the rest requires `_Observation.unchanged_from` (state `file` and
digest equal to the recorded digest) before calling `_remove_unchanged`. A path whose file has changed
is reported `retained-with-reason`, with its kind supplied by `_discrepancy_kind` (`modified`,
`replaced`, `deleted`, `unreadable`) when the path left the plan and by `_retention_reason` when it
stayed; an unchanged file that could not be removed is retained with reason `unreadable` rather than
reported as removed. `_unchanged_prior` is the separate question publication asks — whether a freshly
published artifact is byte-identical to what the prior manifest recorded — which is what lets an
outcome read `unchanged` instead of `published`.

**An externally edited file is reported by kind and preserved, and the only overwrite route is a
per-path authorization.** `_partition` asks, for every output the prior manifest records, whether the
file on disk still matches the recorded digest; when it does not, the output is not written and the
caller receives a `ProjectionOutcome` in state `reported` plus a `Discrepancy` carrying the recorded
digest, the observed digest and the observation's own detail — the four kinds exist because they call
for different caller action. `ProjectionPlan.authorized_overwrites` is the sole exception: a path
listed there is writable even though it disagrees with the manifest, and `_next_manifest` records
`authorized_overwrite` on the resulting `ManagedOutput` entry so the authorization is a recorded fact
about one path rather than a mode. Preservation is itself a state with memory:
`RetainedOutput.recorded` carries the prior generation's whole `ManagedOutput` rather than a reduced
digest, and `_carried_retentions` carries a prior retention forward while its file is still on disk,
because a retained path dropped from the manifest would become unowned and the generation after that
would be free to write over a user's edit — the exact file loss the retention state exists to prevent.

**The safety contract is testable rather than asserted, and the next generation is derived from one
value.** `ProjectionHooks.before_publish` is the single seam `_publish` calls at the exact instant
between staging and the first rename, its default being `_no_hook`; that is the packet's Open Truth
Gap answered — whether checkpoint 4 can be induced deterministically — because it can, without a
sleep, a thread or a signal. `_next_manifest` composes `ProjectionManifest` from one `_ManifestInputs`
value (renderer version, published outputs, retentions, preserved paths, authorized paths), increments
`generation`, carries the prior entry of every preserved path forward so the file on disk stays
detectably different from what the substrate last wrote, and sorts both tuples by destination path for
a stable manifest. `refusal_report` is the other end of the same contract: it renders the report of a
projection that wrote nothing, naming the destination root, the renderer version and the refusal, with
`manifest_generation=None` because no generation was written.

### Conventions

Every shape this module constructs derives from `KnowledgeModel`, so `extra="forbid"` and `frozen=True`
are what refuse a payload arriving with an undeclared field — a second owner for one path, an output
carrying no identity. Bounded text reuses the base constants rather than literals: `PROSE_MAX_LENGTH`
for details and next actions, `REFERENCE_MAX_LENGTH` for paths, canonical forms and identities,
`LABEL_MAX_LENGTH` for record kinds, formats and renderer versions. Declarations that must agree are
one declaration: `DIGEST_ALGORITHM` is the single spelling of the algorithm the recorded entry and the
computed digest share; `STAGING_DIRECTORY_NAME` is one value read by `_write_staged`, `_stage`,
`_publish_manifest`, `_discard_staging` and, in the vocabulary module,
`require_confined_relative_path`; and `ProjectionRefusalCode` is a namespace of literals whose members
the `RefusalCode` union repeats, deliberately kept out of the shipped dataset refusal vocabulary
because a filesystem fact about a directory the substrate does not own is not a dataset operation.
Module-private helpers and values carry a leading underscore (`_no_hook`, `_observations`,
`_Observation`, `_ManifestInputs`, `_next_manifest`), `__all__` names the four public names this module
adds — `ManagedProjectionWriter`, `ProjectionHooks`, `refusal_report`, `resolve_inside_destination` —
and every vocabulary, model and predicate that belongs to another leaf is imported rather than
re-declared: the eighteen names taken from `models/knowledge/projection_manifest.py` include the port a
writer implements, the plan and report vocabulary, the refusal vocabulary, and the two predicates
`detect_destination_collisions` and `require_confined_relative_path` that this module consumes rather
than restates.

### Invariants And Boundaries

- **The destination is never enumerated.** Every path this module touches is either named by the plan,
  taken from the prior manifest, or inside the staging directory; a destination entry no manifest lists
  is not reachable, and `_require_destination` is the only code that even looks at the root itself.
- **An unreadable manifest refuses the run.** `_read_prior_manifest` answers `MANIFEST_UNREADABLE` for
  a manifest that cannot be read, is not a JSON object or does not declare
  `PROJECTION_MANIFEST_FORMAT`, and `ESCAPING_LINK` for a symlinked one; `write` returns
  `refusal_report(...)` with `manifest_generation=None` and stages nothing.
- **Confinement is resolved in both halves, and the two escape cases stay distinct.** A path that is
  itself unconfined refuses the whole plan through `_first_escape`, while a clean destination-relative
  request that lands on a link is reported for that one output and the remaining outputs continue.
- **A collision refuses the whole plan.** Detection runs over all the plan's outputs before staging,
  neither candidate is written, and no disambiguating suffix is invented.
- **Publication is one rename per artifact, and a failure discards the staged bytes.** `_publish`
  publishes under `STAGING_DIRECTORY_NAME` with `os.replace`, and `_stage_and_publish` calls
  `_discard_staging` on any `BaseException` before re-raising, leaving the destination in its prior
  state.
- **A deletion requires both halves of the unchanged test and never follows a link.**
  `_Observation.unchanged_from` requires state `file` and an equal digest, and `_remove_unchanged`
  returns `False` for a symlink or a non-file, so a link is neither deleted nor traversed.
- **There is no recursive clean and no `rmtree`.** `_discard_staging` touches only the staging
  directory the writer itself created, and `rmtree` appears nowhere in the module.
- **The only overwrite route is an explicit per-path authorization, and it is recorded.**
  `ProjectionPlan.authorized_overwrites` is a list of destination-relative paths, and the resulting
  `ManagedOutput` entry carries `authorized_overwrite`; nothing else bypasses the digest comparison.
- **A writer holds no state between calls and no path of its own.** Every fact about the destination is
  re-read from the destination's manifest at the start of a write, so "what it wrote last time" cannot
  become a second, unrecorded authority, and this module reads and writes nothing besides the
  destination and the artifacts it is handed.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

This module is one half of a pair: the vocabulary of the projection — the plan, the outputs, the
manifest, the refusal codes, and the two confinement and collision predicates — lives in
`models/knowledge/projection_manifest.py`, and the vault-safety behaviour that uses it lives here. The
rows below cite the behaviour in this file, the declarations it consumes, and the shared base whose
frozen, forbidding configuration every shape in both modules derives from.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the eight vault-safety clauses, including that the destination is never enumerated, that confinement is resolved, and that no recursive clean or rmtree exists here. | `rmtree`; `_discard_staging` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:1-37; mcp/src/agents_remember/memory/knowledge/managed_projection.py:712-730 |
| The four public names this module adds: the writer, the hook record, the refusal report and the resolved-confinement helper. | `__all__` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:69-74 |
| The one publication seam: the default no-op hook and the frozen hook record a test interrupts publication with. | `_no_hook`; `ProjectionHooks` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:77-85 |
| The report of a projection that wrote nothing, naming the destination root and carrying no manifest generation. | `refusal_report` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:88-97 |
| Resolved confinement: the parent's real path and the joined path's own real path must both be inside the resolved root. | `resolve_inside_destination` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:100-123 |
| The syntactic half of confinement and the collision predicate, both consumed from the vocabulary module rather than restated. | `require_confined_relative_path`; `detect_destination_collisions` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:491-516; mcp/src/agents_remember/models/knowledge/projection_manifest.py:448-488 |
| The staging directory's declared name, and the single staged-artifact write that creates only that artifact's own parents. | `STAGING_DIRECTORY_NAME`; `_write_staged` | mcp/src/agents_remember/models/knowledge/projection_manifest.py:92-94; mcp/src/agents_remember/memory/knowledge/managed_projection.py:130-136 |
| The destination as one computed description, and the five-way observation each recorded path is classified into. | `_DestinationState`; `_Observation`; `_observe` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:146-159; mcp/src/agents_remember/memory/knowledge/managed_projection.py:163-178; mcp/src/agents_remember/memory/knowledge/managed_projection.py:181-200 |
| The prior manifest as the only ownership authority, with its unreadable and symlinked cases refused rather than treated as absent. | `_read_prior_manifest`; `MANIFEST_UNREADABLE`; `ProjectionRefusal` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:203-257; mcp/src/agents_remember/models/knowledge/projection_manifest.py:137-151 |
| The writer's entry point and its guard order — destination, manifest, collision, escape — before anything is staged. | `ManagedProjectionWriter`; `write`; `_require_destination` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:260-288; mcp/src/agents_remember/memory/knowledge/managed_projection.py:292-323 |
| The collision refusal: both paths, both identities and the canonical form they share, with no disambiguating suffix invented. | `_first_collision`; `Collision` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:325-347; mcp/src/agents_remember/models/knowledge/projection_manifest.py:404-413 |
| The escape refusal, where the syntactic refusal is re-stamped with the same resolved root the resolving half names. | `_first_escape`; `DESTINATION_ESCAPE` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:349-379; mcp/src/agents_remember/models/knowledge/projection_manifest.py:105-123 |
| One call's whole order: partition, stage, publish, retire, derive the next manifest, publish it. | `_stage_and_publish`; `_next_manifest`; `_publish_manifest` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:383-432; mcp/src/agents_remember/memory/knowledge/managed_projection.py:744-779; mcp/src/agents_remember/memory/knowledge/managed_projection.py:782-790 |
| The partition that preserves an externally edited file by kind, and the per-path authorization that is the only way past it. | `_partition`; `authorized_overwrites`; `ManagedOutput` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:434-478; mcp/src/agents_remember/models/knowledge/projection_manifest.py:197-208; mcp/src/agents_remember/models/knowledge/projection_manifest.py:211-229 |
| A link in the way of a write is reported for that one output, and the same rule is asked from both the staging and the deletion side. | `_stage`; `_crosses_a_link` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:480-506; mcp/src/agents_remember/memory/knowledge/managed_projection.py:682-697 |
| One rename per output, and the manifest's canonical bytes written through the same staging discipline. | `_publish`; `_manifest_bytes` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:508-548; mcp/src/agents_remember/memory/knowledge/managed_projection.py:139-143 |
| The deletion rule's both halves, and the retention that keeps a prior generation's whole entry so a retained path never becomes unowned. | `_retire`; `unchanged_from`; `_remove_unchanged`; `_carried_retentions`; `RetainedOutput` | mcp/src/agents_remember/memory/knowledge/managed_projection.py:550-622; mcp/src/agents_remember/memory/knowledge/managed_projection.py:163-178; mcp/src/agents_remember/memory/knowledge/managed_projection.py:700-709; mcp/src/agents_remember/memory/knowledge/managed_projection.py:625-646; mcp/src/agents_remember/models/knowledge/projection_manifest.py:232-249 |
| The frozen, forbidding base every shape in both modules derives from, with the bounded-length constants the fields reuse. | `KnowledgeModel`; `PROSE_MAX_LENGTH`; `REFERENCE_MAX_LENGTH` | mcp/src/agents_remember/models/knowledge/base.py:24-37 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The projection writes one local
destination the caller configured, every identity it records is a store-local stable identity or a
content digest, and nothing here reads another repository, another dataset or a remote.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): created this one-to-one card for the managed projection writer. It records the eight vault-safety clauses as behaviours rather than intentions — the manifest as the only ownership authority with no destination enumeration, confinement by real-path resolution, collisions refused before either artifact is written, an escaping link never followed for a write or a delete, publication as a stage-then-rename, a deletion requiring both halves of the unchanged test, no recursive clean and no `rmtree` anywhere, and an externally edited file reported by kind and preserved behind a recorded per-path authorization — plus the `ProjectionHooks.before_publish` seam that makes checkpoint 4 inducible without a sleep, the `RetainedOutput.recorded` carry, `_carried_retentions`, `_next_manifest` and `refusal_report`. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
