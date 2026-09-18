# mcp/src/agents_remember/models/knowledge/registered_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/registered_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:02+02:00 |
| lastVerifiedCommitHash |  `9f88a6de572dc15bbed1802cf08b77c1193fb24c`|
| lastVerifiedCommitDate |  2026-09-18T14:21:49+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l16` uncommitted staged source; base `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

The registered review scope's frozen vocabulary: the declaration a construction is asked over, the
recorded edges it followed, the membership it resolved, the manifest it produced and the refusal that
names the one declared input it could not resolve. **This module declares shapes and refuses states; it
performs no construction.** No query, no store handle, no traversal call and no filesystem access
appears in it — the storage half is `mcp/src/agents_remember/memory/knowledge/registered_scope.py`, whose
own card carries the resolution order. It defines no detection schema, no assessment schema and no
composition schema, and it redefines nothing the shipped selective read owns.

## Code Commentary

### Logic

**One construction version and three closed vocabularies, each bound to a field.**
`SCOPE_CONSTRUCTION_VERSION` names *how* a scope is built — the shipped policy-constant idiom, declared
beside `KNOWLEDGE_READ_POLICY_VERSION` and `DETECTION_POLICY_VERSION` and deliberately not the traversal
policy's identity, which is an authored registry row resolved from the store. `ScopeSnapshotSide` with
`SCOPE_SIDES` is the declared pair (`base`, `candidate`); `ScopeEdgeKind` with `SCOPE_EDGE_KINDS` is the
three followed kinds in declared order, the first two being recorded repository links and the third an
*authored* composition edge that is followed only under a declared policy version; and
`ScopeMissingInputKind` is the closed four-member set of declared inputs a construction refusal may name
(`declared_snapshot`, `declared_changed_path`, `seed_family_revision`, `traversal_policy`). **The sides
and the edge kinds are each spelled twice — as the `Literal` and as an ordered tuple — so a caller can
iterate exactly the set the type admits, and all three vocabularies are the declared type of a field, so
a member outside them is a validation failure rather than a new state.**

**One side's declaration is an exact identity, and one followed edge keeps the snapshot it was read
from.** `ScopeSnapshotDeclaration` carries a `SnapshotIdentity` — the whole admission a side has, its
namespace, its declared schema version and the logical digest of its content — plus the
`selector_policy_version` the declaration was read under, because which records a side *contributes* is
a property of that policy. `FollowedScopeEdge` adds the recorded row's own `edge_id`, the two endpoints
it joined and a **required** `mapping_side`: an edge with no recorded side would be a claim about the
union of two snapshots that no single snapshot supports. Its `policy_identity` is the resolved
`(policy_id, policy_version_id, declared_version)` triple and is admissible on a composition edge and
nowhere else; `_require_the_policy_half_to_match_the_kind` enforces both directions, so a recorded
lookup cannot claim a traversal that never ran and a composition edge with no recorded policy — the
widened-without-a-policy state this leaf refuses — is not expressible as a followed edge at all.

**Membership is a record of resolved identities and nothing else.** `RegisteredScopeMembership` holds
five tuples — invariant revisions, family revisions, realization claims, source anchors and the
`recorded_reference_refs` the reached records themselves declare — and `size()` is their summed length,
which is what a caller reports as the scope's size. No entry is derived from a name, a prefix, a folder,
a symbol or a route's name, and the docstring measures why there is no evidence-claim channel here: the
substrate's dedicated `EvidenceClaim` record group does not exist yet
(`mcp/src/agents_remember/memory/knowledge/record_envelope.py:16` records that those categories "are
later leaves"), so a construction collects the reference channel the reached records actually carry
instead of a field no record could ever populate.

**The declaration is the whole input list, and three validators keep it unambiguous.**
`RegisteredScopeRequest` carries the paired snapshots, the changed paths whose registered links are
looked up, the seed family revisions a declared traversal may start from, the optional policy identity
and the construction version. It admits **at most one snapshot per declared side** and at least one
(`Field(min_length=1)`), so an ambiguous common base is refused where the caller can still fix the
declaration rather than resolved arbitrarily; `_require_unique_nonblank_entries` refuses a blank or
repeated path/seed, because a repeated entry is not a second input and would make the record of the
construction's own inputs wrong; and `_require_a_declared_policy_to_name_both_halves` refuses half a
policy identity and refuses a seed family revision with no policy at all, since a seed is a traversal's
starting point and a construction with no declared policy follows no composition edge. `declared_side()`
is the lookup the construction uses to find one side's declaration, or `None` when that side was not
declared.

**The manifest holds the scope and nothing derived from it.** `RegisteredScopeManifest` is the declared
snapshots, the declared changed paths, the *resolved* `policy_identity` the construction executed under,
the followed edges and a required membership — with no unresolved-input list (that is the refusal),
no frontier, no selection counts and no conclusion about any member. Two validators refuse the states
that would make it unreadable: an edge whose `mapping_side` names a side the scope did not declare, and
a composition edge whose policy identity is not the scope's own resolved identity (which would report
two traversals as one). `followed_composition_ids()` narrows the edge list to the composition edges by
their recorded identities.

**The refusal names the exact missing input, and its typed half must agree.** `ScopeConstructionRefusal`
carries the `missing_input_kind`, the missing input's recorded identity, prose detail and the shipped
`KnowledgeRefusal`; `_require_the_refusal_to_name_the_same_input` refuses a wrapper whose typed refusal
records a different input in either of its two identity slots, on the ground that a refusal naming two
different inputs names neither, and `next_action()` returns the shipped next action the typed refusal
advertises. `scope_path_is_recorded` is the module's one ordinary function: it trims, maps `\` to `/`,
and refuses a blank, `/`- or `:`-prefixed, `..`-bearing or over-`PATH_MAX_LENGTH` spelling, so a
declared changed path stays an identity the lookup can compare by exact equality instead of a spelling
that could be normalised, globbed or resolved. It is not listed in `__all__`, and in this candidate its
only caller is the module's own test.

### Conventions

Every shape derives from the shipped `KnowledgeModel` (`extra="forbid"`, `frozen=True`), so an
undeclared field — a verdict, a count, a frontier, a second authorship — is a validation failure rather
than a silent passenger, and an immutable declaration is safe to compare and deduplicate by value. All
bounds come from the shipped base constants (`LABEL_MAX_LENGTH`, `REFERENCE_MAX_LENGTH`,
`PROSE_MAX_LENGTH`, `PATH_MAX_LENGTH`) rather than from new numbers declared here, and blank-after-trim
is refused with a message that states which declaration rule the value broke.

`__all__` names the published vocabulary — the three value constants, the three type aliases and the
five models — so the module's public surface is a declaration rather than whatever happens to be
importable. Imports stay inside the models layer (`models.knowledge.base`, `.candidate`, `.result`); no
memory-layer module is imported, which is why the shapes can be read without a store. Each model-level
validator carries a docstring stating the state it refuses and each field validator raises a message
naming the declaration rule the value broke, so the reason for a refusal is readable beside the check
that produces it.

The docstring idiom is this leaf's: the module docstring states the five structural properties and the
`## Forbidden Overreach` rule that **no identity is minted here**, so the vocabulary is read as a
contract rather than as a description of a flow.

### Invariants And Boundaries

- **Membership is recorded, never inferred.** No field and no validator derives a member from prose, a
  display label, a folder name, a path prefix, a symbol or a route's name; a path prefix compared
  against a stored anchor path is a resolution fact and is not representable in this module at all.
- **A policy-less widening is not representable.** A composition edge without a policy identity does not
  validate, a declaration carrying half a policy identity is refused, and a seed family revision with no
  declared policy is refused: absence never widens.
- **Construction is total or it is a refusal.** There is no partial scope and no unresolved-input list —
  the refusal is the record for that state — so a scope that silently held less than it declared cannot
  be expressed.
- **The scope's identity is its declared `scope_id`.** No content address, logical digest or fingerprint
  of the scope itself exists here; `policy_identity` is the resolved traversal triple, and a
  `scope_manifest_ref` elsewhere points at the declared `scope_id` and at nothing derived from it.
- **No read-frontier field can exist here.** A selected revision set, a page cursor, a count of items
  remaining or an advertised expansion have no slot in any record this module declares, so the §8 scope
  and the R07 read are kept apart by the shape of the records rather than by a rule a caller remembers.
- **The typed refusal carried is the shipped one.** `ScopeConstructionRefusal` is a wrapper whose
  `refusal` field is the shipped `KnowledgeRefusal` from `models/knowledge/result.py`; the wrapper adds
  the named missing input and its kind, and adds no code to the shipped refusal vocabulary.
- **The only callables are checks and accessors.** `size()`, `declared_side()`,
  `followed_composition_ids()`, `next_action()`, `scope_path_is_recorded()` and the validators — no
  method here reads a store, runs a traversal or resolves a reference.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The construction version, declared in the shipped policy-constant idiom beside the read's and the detector's own versions. | `SCOPE_CONSTRUCTION_VERSION`; `KNOWLEDGE_READ_POLICY_VERSION`; `DETECTION_POLICY_VERSION` | mcp/src/agents_remember/models/knowledge/registered_scope.py:76-76; mcp/src/agents_remember/models/knowledge/read.py:87-87; mcp/src/agents_remember/models/knowledge/detection.py:101-101 |
| The two declared sides, spelled once as a literal and once as the ordered tuple. | `ScopeSnapshotSide`; `SCOPE_SIDES` | mcp/src/agents_remember/models/knowledge/registered_scope.py:81-81; mcp/src/agents_remember/models/knowledge/registered_scope.py:83-83 |
| The two closed vocabularies a caller branches on: the three followed edge kinds, and the four declared inputs a refusal may name. | `ScopeEdgeKind`; `SCOPE_EDGE_KINDS`; `ScopeMissingInputKind` | mcp/src/agents_remember/models/knowledge/registered_scope.py:88-88; mcp/src/agents_remember/models/knowledge/registered_scope.py:90-94; mcp/src/agents_remember/models/knowledge/registered_scope.py:99-104 |
| One side's declaration as an exact snapshot identity plus the selection policy version it was read under. | `ScopeSnapshotDeclaration` | mcp/src/agents_remember/models/knowledge/registered_scope.py:107-120 |
| The followed edge with its required snapshot provenance, and the validator that admits its resolved policy half on a composition edge and nowhere else. | `FollowedScopeEdge`; `_require_the_policy_half_to_match_the_kind` | mcp/src/agents_remember/models/knowledge/registered_scope.py:123-139; mcp/src/agents_remember/models/knowledge/registered_scope.py:141-163 |
| The membership as recorded identities only, with `size()` reporting the counted members and the reference channel being the origin references the reached records carry. | `RegisteredScopeMembership`; `recorded_reference_refs`; `size`; `are later leaves` | mcp/src/agents_remember/models/knowledge/registered_scope.py:166-187; mcp/src/agents_remember/models/knowledge/registered_scope.py:189-198; mcp/src/agents_remember/memory/knowledge/record_envelope.py:16-16 |
| The stored origin references a reached record declares for itself, which the membership collects and decides nothing about. | `origin_refs` | mcp/src/agents_remember/models/knowledge/authorship.py:48-48 |
| The declaration itself — paired snapshots, changed paths, seeds, optional policy — and the refusal of a blank or repeated path/seed. | `RegisteredScopeRequest`; `_require_unique_nonblank_entries` | mcp/src/agents_remember/models/knowledge/registered_scope.py:201-229; mcp/src/agents_remember/models/knowledge/registered_scope.py:231-242 |
| The declaration's three remaining checks: an ambiguous common base refused where the caller can still fix it, a policy that must be both halves or neither, a seed without a policy refused as a widening — plus the one-side lookup. | `_require_one_declared_pair`; `_require_a_declared_policy_to_name_both_halves`; `declared_side` | mcp/src/agents_remember/models/knowledge/registered_scope.py:244-266; mcp/src/agents_remember/models/knowledge/registered_scope.py:268-284; mcp/src/agents_remember/models/knowledge/registered_scope.py:286-292 |
| The constructed scope: declared snapshots and paths, resolved policy triple, followed edges and the required membership — and the composition-edge identities it followed. | `RegisteredScopeManifest`; `followed_composition_ids` | mcp/src/agents_remember/models/knowledge/registered_scope.py:295-312; mcp/src/agents_remember/models/knowledge/registered_scope.py:341-346 |
| The two states a manifest refuses: an edge attributed to a side the scope did not declare, and a composition edge naming a policy other than the scope's own. | `_require_every_edge_to_name_a_declared_side`; `_require_one_policy_for_every_followed_composition_edge` | mcp/src/agents_remember/models/knowledge/registered_scope.py:314-326; mcp/src/agents_remember/models/knowledge/registered_scope.py:328-339 |
| The refusal naming the exact missing input, the validator that keeps its typed half naming the same input, and the advertised next action. | `ScopeConstructionRefusal`; `_require_the_refusal_to_name_the_same_input`; `next_action` | mcp/src/agents_remember/models/knowledge/registered_scope.py:349-361; mcp/src/agents_remember/models/knowledge/registered_scope.py:363-376; mcp/src/agents_remember/models/knowledge/registered_scope.py:378-381 |
| The one ordinary function: a declared changed path is refused unless it is a plain repository-relative spelling within the shipped path bound. | `scope_path_is_recorded`; "if len(cleaned) > PATH_MAX_LENGTH:" | mcp/src/agents_remember/models/knowledge/registered_scope.py:384-403; mcp/src/agents_remember/models/knowledge/base.py:27-27 |
| The frozen, extra-forbidding base every shape derives from, the snapshot identity a side is declared as, and the shipped typed refusal the construction wrapper carries. | `model_config`; `SnapshotIdentity`; `KnowledgeRefusal` | mcp/src/agents_remember/models/knowledge/base.py:34-37; mcp/src/agents_remember/models/knowledge/candidate.py:185-194; mcp/src/agents_remember/models/knowledge/result.py:235-245 |
| The read path's own selection counts — including items remaining and advertised expansions — none of which any record in this module has a slot for. | `KnowledgeReadCounts`; `primary_items_remaining` | mcp/src/agents_remember/models/knowledge/read.py:404-429 |
| The sibling pipeline vocabulary that consumes a scope, and which states in its own docstring that it redefines none of the records it composes. | "redefines none of theirs" | mcp/src/agents_remember/models/knowledge/family_review.py:1-6 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A scope declaration, its edge provenance and
its refusal vocabulary are properties of one namespace's own stored records, every identity they carry is
store-local, and the module imports nothing outside `agents_remember.models.knowledge`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T14:02+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): created this one-to-one card for the registered review scope's frozen vocabulary. It records the four closed vocabularies and the construction version, the declaration's one-snapshot-per-side and both-halves-of-a-policy rules, the followed edge that must carry the snapshot it was read from and may carry a policy only when it is a composition edge, the membership as recorded identities with no evidence-claim channel at this base, and the deliberate absences (no partial scope, no frontier field, no inferred member, no minted identity, no refusal code of its own). This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
