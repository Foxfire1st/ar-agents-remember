# mcp/src/agents_remember/memory/knowledge/composition_policies.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/composition_policies.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:12+02:00 |
| lastVerifiedCommitHash | `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate | 2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l17` uncommitted source; base `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The **declared traversal policy** as an append-only version set: one policy identity, sealed version
rows, and the resolution that refuses rather than defaults.

A composition edge may name a policy, and a policy is what makes a set of declared edges into a
traversable scope. This module owns the policy record and nothing else: it does not walk an edge
(`composition_traversal.py` does), it does not decide whether a policy is *admissible* to the
registered review scope (the traversal does, by name), and it does not author an edge
(`compositions.py` does).

**The policy defaults to off, and that is the whole point of the split.** An edge that names no
policy is stored, readable and **not traversable**. There is no resolution to a default policy, no
fallback to the only version stored, and no implicit "any declared policy". A reader that finds an
edge with no policy has found a recorded relationship that nobody has declared a traversal for, and
this module says so rather than supplying one.

## Code Commentary

### Logic

- `insert_policy_version` — inserts the policy identity if it is new and then the sealed version row.
  The version is immutable once written; re-spelling a version is a new version row, which is why
  `policy_version_id` (the immutable row identity an edge cites) and `declared_version` (the author's
  own spelling) are separate fields.
- `get_policy_version` and `list_policy_versions` — the two reads. A version is addressed by
  `(policy_id, policy_version_id)`; a list is ordered by the declared version spelling.
- `require_declared_policy` — the resolution, and its two refusals are **two different facts**:
  an unknown policy *identity* and an unknown *version of a known identity* are refused separately,
  each naming what it looked for and, for the version, the versions that identity does declare. It
  never resolves to a default and never picks the only version stored.
- `policy_identity` — returns `(policy_id, policy_version_id, declared_version)`, the triple a
  traversal's result carries so a result constructed under one version is never readable as one
  constructed under another.

### Conventions

- Validation happens in **two places on purpose**: at the value boundary (`FamilyCompositionPolicyDraft`
  in `models/knowledge/composition.py` refuses a half-declared policy) and at the table's own `CHECK`
  constraints in `schema_v6.py`. A malformed policy is therefore unrepresentable *and* unwritable,
  which is what makes "malformed policies do not exist" a fact about the store rather than a habit of
  one code path.
- The four declared `CHECK`s are `declared_version <> ''`, a closed direction vocabulary, a depth
  bound of at least one, and a non-empty widened scope. A policy that permits no direction would
  permit nothing, and a policy with no bound would not be a scope.
- A traversal policy **may only widen a named scope**. The one registered scope is
  `REGISTERED_REVIEW_SCOPE` in `models/knowledge/composition.py`; a later leaf that builds another
  scope adds a member there and states what it widens, and nothing else can widen anything.

### Invariants And Boundaries

- **No default and no fallback.** `require_declared_policy` returns a typed refusal for an
  undeclared identity or version; it never returns a substitute policy.
- **A version row is immutable.** Generation 5's triggers refuse a rewrite and a delete, and the
  operation's preconditions return the typed refusal first.
- **Provenance is required on the identity and on every version.**
- **Boundary.** This module decides nothing about edges. Whether a particular edge may be followed
  under a particular policy version is the traversal's question, and it is refused *by name* there.
- **Not admissible, recorded so it is not re-proposed:** storing the policy as two nullable columns
  on `family_composition`. That shape makes identity-without-version and version-without-identity
  representable states; the composite foreign key to `(repository_id, policy_id, policy_version_id)`
  refuses them structurally instead.

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
| The version write: identity first if new, then the sealed version row. | `insert_policy_version` | mcp/src/agents_remember/memory/knowledge/composition_policies.py:87-87 |
| The version read addressed by the immutable row identity. | `get_policy_version` | mcp/src/agents_remember/memory/knowledge/composition_policies.py:162-162 |
| The version list ordered by the author's own version spelling. | `list_policy_versions` | mcp/src/agents_remember/memory/knowledge/composition_policies.py:187-187 |
| **The resolution that refuses an unknown identity and an unknown version of a known identity as two different facts, and never resolves to a default.** | `require_declared_policy` | mcp/src/agents_remember/memory/knowledge/composition_policies.py:200-200 |
| The policy-identity triple a traversal's result carries. | `policy_identity` | mcp/src/agents_remember/memory/knowledge/composition_policies.py:81-81 |
| **The value-boundary half of the two-place validation, where a half-declared policy is refused before it can reach a store.** | `FamilyCompositionPolicyDraft` | mcp/src/agents_remember/models/knowledge/composition.py:83-83 |
| **The one registered scope a policy may widen, and nothing else.** | `REGISTERED_REVIEW_SCOPE` | mcp/src/agents_remember/models/knowledge/composition.py:45-45 |
| The closed direction vocabulary, which is a rule rather than a hint: it decides which endpoints a traversal may step through. | `FOLLOW_DIRECTIONS` | mcp/src/agents_remember/models/knowledge/composition.py:51-51 |
| **The case that proves an undeclared policy reference is refused and no row is written.** | "test_an_undeclared_policy_reference_is_refused_and_no_row_is_written" | mcp/tests/test_knowledge_family_composition.py:454-454 |
| **The case that proves an edge with no declared policy is stored, readable and not traversable — the default is off.** | "test_an_edge_with_no_declared_policy_is_stored_readable_and_not_traversable" | mcp/tests/test_knowledge_family_composition.py:428-428 |
| The case that proves an unknown, a malformed and a not-permitted policy are each refused by name. | "test_an_unknown_a_malformed_and_a_not_permitted_policy_are_each_refused_by_name" | mcp/tests/test_knowledge_family_composition_boundaries.py:334-334 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_an_undeclared_policy_reference_is_refused_and_no_row_is_written" repointed to mcp/tests/test_knowledge_family_composition.py:454-454. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "test_an_edge_with_no_declared_policy_is_stored_readable_and_not_traversable" repointed to mcp/tests/test_knowledge_family_composition.py:428-428. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:30:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 2 generated projection bullet(s) by hand** — `test_an_edge_with_no_declared_policy_is_stored_readable_and_not_traversable`, `test_an_undeclared_policy_reference_is_refused_and_no_row_is_written`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.

- 2026-09-18T04:12:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): created this one-to-one card for the declared-policy module. It records the two sentences this leaf's remit fixes: **the policy defaults to off** — an edge with no declared policy is stored, readable and not traversable, and `require_declared_policy` never resolves to a default or to the only version stored — and the policy is **validated in two places**, at the value boundary and at the table's own `CHECK`. It records why the policy is an append-only version set rather than a nullable column pair on the edge, why an unknown identity and an unknown version of a known identity are two different refusals, and that a policy may only widen a *named* scope. Verification metadata is the leaf's base commit `e963a01c`: the code commit does not exist yet and closeout owns that stamp.
