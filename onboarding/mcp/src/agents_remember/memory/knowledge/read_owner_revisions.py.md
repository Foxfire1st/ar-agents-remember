# mcp/src/agents_remember/memory/knowledge/read_owner_revisions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/read_owner_revisions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80` |
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l18` uncommitted source; base `e963a01c` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Observe one recorded prose owner revision against the memory object store, and report which fact it is
without ever turning the observation into a promotion.

## Code Commentary

### Logic

`OwnerRevisionResolver.observe` addresses exactly one object — the one whose identity the binding
already stored, spelled `<object_id>^{blob}` — through the shipped `run_git` runner, and returns an
`OwnerRevisionObservation` carrying the recorded identity, the path it was recorded at and a status.
`read_recorded_bytes` is the separate, explicit fetch used only when a caller has asked to compare a
written key against the recorded bytes, so a read page stays a facts packet rather than a document
dump. `_root_is_usable` decides the one non-object outcome: with no memory repository requested the
observation is `recorded_object_unavailable` rather than an exception, so "no repository" has a
declared answer instead of an accidental one. `render_owner_revision_basis` renders the recorded basis
(path, identity, state) for the failure direction, and `owner_revision_resolver_for` is the one
constructor.

### Invariants And Boundaries

- **No fallback to the working tree, to `HEAD`, to a branch name, or to a path.** A document that has
  moved on, been rewritten or been deleted is *not* re-read from disk and is not re-resolved from its
  path: the recorded revision is either in the object store or it is not, and the second case is a
  reported state rather than a lookup that quietly succeeds against different bytes.
- **No content is returned for the resolution itself**; the bytes are fetched separately and only
  when a caller has asked to compare a key against them.
- **The stored identity is preserved on every outcome**, including the failures — a missing revision
  is never a reason to retire a stored attribution.
- `OWNER_REVISION_STATES` declares the two states this module can report, so a case can assert it
  reports nothing outside the vocabulary the closure counts.
- **The difference from the shipped anchor reader is what they look at, not a second authority.**
  `read_anchors` resolves a recorded *path* inside a requested tree and reports whether that tree holds
  the recorded blob — the code side, where a path can have moved. Here the identity *is* the address,
  so there is no path to look up and nothing to relocate. The shipped literals are reused verbatim
  anyway, because the facts coincide exactly.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The declared states this observation can report, so "no memory repository was requested" has a declared answer.** | `OWNER_REVISION_STATES` | mcp/src/agents_remember/memory/knowledge/read_owner_revisions.py:50-55 |
| **The one fact about one recorded owner revision: what was addressed, and what answered.** | `OwnerRevisionObservation` | mcp/src/agents_remember/memory/knowledge/read_owner_revisions.py:56-69 |
| The one rendering of the recorded basis, used for the failure direction. | `render_owner_revision_basis` | mcp/src/agents_remember/memory/knowledge/read_owner_revisions.py:71-80 |
| **The resolver: the one recorded object addressed, and the object-store observation with no path fallback.** | `OwnerRevisionResolver` | mcp/src/agents_remember/memory/knowledge/read_owner_revisions.py:95-153 |
| The separate byte fetch, used only when a caller compares a written key against the recorded revision. | `read_recorded_bytes` | mcp/src/agents_remember/memory/knowledge/read_owner_revisions.py:116-131 |
| The one constructor. | `owner_revision_resolver_for` | mcp/src/agents_remember/memory/knowledge/read_owner_revisions.py:155-158 |
| **The recorded owner revision this module resolves — repository, confined document path and the recorded object identity, referenced rather than minted.** | `ProseOwnerRevision` | mcp/src/agents_remember/models/knowledge/citation.py:144-192 |
| **The shipped identity the recorded revision is spelled in: the class that declares the one v1 source identity, and the module-level alias the same name carries — which is why this card names both sites.** | `GitBlobIdentity` | mcp/src/agents_remember/models/knowledge/source.py:28-38 |
| The shipped Git runner the object lookup goes through. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:150-160 |
| The shipped anchor reader whose refusal this module's no-fallback rule follows. | `observe_anchor` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:101-139 |
| **The boundary case that proves a document present on disk at its recorded path still reports unavailable when the object store cannot produce the recorded revision.** | `test_an_owner_revision_the_object_store_cannot_obtain_is_reported_as_unavailable` | mcp/tests/test_knowledge_citation_boundaries.py:353-394 |
| The unit case that asserts every recorded binding reports exactly one state from the declared vocabulary. | `test_the_enumeration_returns_every_recorded_binding_with_exactly_one_state` | mcp/tests/test_knowledge_citation_bindings.py:538-565 |
| The unit case that asserts this module reports only declared states. | `test_the_closed_vocabulary_agrees_with_its_facts_and_with_every_producing_surface` | mcp/tests/test_knowledge_citation_bindings.py:258-262 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The object store it reads is the memory
repository's, and the recorded identity is the only address it ever uses.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T01:02+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 2 enforced citation rows this card carried (citation_claim_reopened, citation_anchor_absent_from_range). Both were the same table row, naming `test_the_owner_revision_observation_reports_only_declared_states`, which no longer exists anywhere in the tree: commit 7e6936c0 folded that case into `test_the_closed_vocabulary_agrees_with_its_facts_and_with_every_producing_surface`, which carries the same declared-state reading (`for state in OWNER_REVISION_STATES`), so the Anchor cell now names that case. The cited `mcp/tests/test_knowledge_citation_bindings.py:258-262` already contains its declaration and was left untouched, as was the claim wording; renaming the anchor also retires the 2026-09-18 generated-repair bullet that named the removed case. No other range was touched and no verification stamp was advanced.
- 2026-09-20T00:29+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `read_owner_revisions.py.md:84` (test_the_enumeration_returns_every_recorded_binding_with_exactly_one_state) — re-read the claim against the module: the named case is gone and the successor's own docstring states the behaviour.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_an_owner_revision_the_object_store_cannot_obtain_is_reported_as_unavailable` repointed to mcp/tests/test_knowledge_citation_boundaries.py:353-394. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:06:32+00:00: Generated citation repair: `test_the_owner_revision_observation_reports_only_declared_states` repointed to mcp/tests/test_knowledge_citation_bindings.py:258-262. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): created this one-to-one card for the owner-revision observation. The card records the one rule that makes the binding's revision fact trustworthy — **the identity is the address**: the resolver asks the object store for the exact recorded object and never falls back to the working tree, to `HEAD`, to a branch name or to the recorded path, so a rewritten or deleted document cannot be silently re-read as if it were the recorded revision. It records that the resolution returns no content (the bytes are a separate, explicit fetch) and that the stored identity survives every outcome including the failures. It also records why this is not a second authority over the shipped anchor reader: `read_anchors` resolves a recorded *path* inside a requested tree — the code side, where a path can have moved — while a binding's owner revision is already an exact object identity with no path to look up; the shipped literals are reused verbatim because the facts coincide exactly. Verification metadata advances to the leaf's base commit `e963a01c` because every cited construct was re-read against the working tree; the code commit does not exist yet and closeout owns that stamp.
