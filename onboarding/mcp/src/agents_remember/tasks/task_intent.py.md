# mcp/src/agents_remember/tasks/task_intent.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/task_intent.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-09T14:45+02:00|
| lastVerifiedCommitHash | `46ca74302e76cf40fb6370ea9ece16d8fa719f00` |
| lastVerifiedCommitDate | 2026-09-30T00:07:49+02:00|
| governingOverview      | `overview.md`                             |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Canonical normative task-intent projection and identity for one leaf task document (CCR-R02@v2).
The module turns an already-resolved task document into a strict `task-intent/v1` projection
containing only explicitly allowlisted normative slots, hashes that canonical JSON into the
SHA-256 intent digest, and provides the single currentness assertion
(`require_current_task_intent`) that closeout, door, and lifecycle consumers call before any
evidence reuse.

## Code Commentary

### Logic

The projection operates on `ResolvedTaskDocument` (never on raw paths or prose) and reads the
shared exhaustive field taxonomy from `document_field_effects.py`:

- `TaskIntentV1` (line 94) is the strict frozen projection: `schema: task-intent/v1`, the leaf
  identity, objective, requirement texts or approved packet refs, design, allowed step/substep
  obligation text, normative code examples, `codeExamplesNote`, and typed acceptance obligations.
  Generic freeform sections, comments, notes, decisions, progress, lifecycle, and audit fields are
  never projected; `canonical_value` (line 112) emits the by-alias JSON for hashing.
- `_ROOT_FIELDS` (line 119) / `_NESTED_FIELDS` (line 137) enumerate exactly which
  `TaskDocument`/nested-model fields task-intent/v1 consumes; `_validate_allowlisted_classifications`
  (line 287) refuses both a slot missing its normative taxonomy membership and a taxonomy-normative
  slot outside the projection, so projecting can never silently drop a newly classified field.
- `task_intent_projection` (line 148) refuses a master (`task-intent-leaf-required`), requires
  the supported schema version, and translates taxonomy failures into
  `task-intent-schema-unclassified`.
- `task_intent_identity` (line 197) hashes the canonical projection with
  `json.dumps(sort_keys=True, separators=(",", ":"))` into a 64-hex digest, producing
  `TaskIntentIdentity`.
- `require_current_task_intent` (line 244) reuses the model-layer rejection seam and raises
  `{owner}-task-intent-stale` when the observed identity differs from the current one, with the
  owner-chosen `next_action`.
- `_requirements` (line 307): exact text must be non-blank, and `task-intent/v1` refuses a
  packet-ref replacement of exact task text (`task-intent/v2-cutover-required`). An approved
  packet ref resolves task-root-relative, must be a Markdown file inside the task root, must be
  readable, and its structured `Stable ID`/`Version` metadata must match exactly
  (`_approved_packet_ref` line 331, `_packet_metadata` line 364); duplicate metadata fields
  refuse as ambiguous.
- `_acceptance_obligations` (line 396) projects only questions typed as
  `AcceptanceObligationQuestion`.
- **`expectedKnowledgeEffects` (MIK-R11), an optional slot.** `TaskIntentV1.expectedKnowledgeEffects` is a
  tuple of `TaskIntentExpectedKnowledgeEffect` (`subject`, `effect`, `requirementRef`) or `None`;
  `_expected_effects` (line 384) projects the leaf's declaration. `canonical_value` **drops the key when it
  is `None`**, and `task_intent_master_projection` drops it for a master, so a document that declares
  nothing projects exactly as before. The field is in `_ROOT_FIELDS`, and `ExpectedKnowledgeEffect`'s three
  fields are in `_NESTED_FIELDS`, matching their `NORMATIVE` classification. A declaration therefore changes
  the leaf's intent digest, and clearing it (`null`) restores the former digest.

### Conventions

The projection is never a whole-document hash and never a digest of decision prose. New normative
slots require both a schema revision and a taxonomy classification; the pair is enforced at
projection time.

### Invariants And Boundaries

- Only allowlisted normative slots change the digest; step status, decisions, timestamps, audit
  prose, lifecycle id, enclosures, evidence, and status notes are excluded by construction.
- An approved requirement packet ref is authoritative only after confined path/readability,
  unambiguous metadata, and exact id/version checks; approval-like prose alone cannot create a
  typed reference.
- Integration generations do not carry leaf task intent; this module is leaf-only.
- **An absent `expectedKnowledgeEffects` leaves every existing task-intent digest unchanged** (MIK-R11).
  Candidate invariant; realized by the key-dropping `canonical_value` and the master projection's `pop`;
  proved by `test_the_field_is_optional_normative_intent_settable_and_refuses_malformed_declarations` and
  by the worker's and reviewer's byte-identical preservation runs over every real task document (597 and
  889 documents).

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty; no external documentation claim is made.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Strict allowlisted v1 projection model. | `TaskIntentV1` | mcp/src/agents_remember/tasks/task_intent.py:94-116 |
| Normative slot allowlists for the document and nested models, since MIK-R11 including `expectedKnowledgeEffects` and its three nested fields. | `_ROOT_FIELDS`; `_NESTED_FIELDS` | mcp/src/agents_remember/tasks/task_intent.py:119-145 |
| The optional declared-effects slot; absent is absent, so digests are unchanged. | `TaskIntentExpectedKnowledgeEffect`; `canonical_value` | mcp/src/agents_remember/tasks/task_intent.py:88-91; mcp/src/agents_remember/tasks/task_intent.py:112-116 |
| The declaration projected into the leaf intent, and dropped from a master's. | `_expected_effects`; "leaf-only; masters project as before" | mcp/src/agents_remember/tasks/task_intent.py:384-393; mcp/src/agents_remember/tasks/task_intent.py:235-236 |
| Projection entry point refusing masters and translating taxonomy failures. | `task_intent_projection` | mcp/src/agents_remember/tasks/task_intent.py:148-194 |
| Canonical digest production from the projection. | `task_intent_identity` | mcp/src/agents_remember/tasks/task_intent.py:197-210 |
| Currentness/staleness assertion for owners. | `require_current_task_intent` | mcp/src/agents_remember/tasks/task_intent.py:244-262 |
| Allowlist/taxonomy symmetry enforcement. | `_validate_allowlisted_classifications` | mcp/src/agents_remember/tasks/task_intent.py:287-304 |
| Requirement text/packet handling and the v2-cutover refusal. | `_requirements`; `_approved_packet_ref` | mcp/src/agents_remember/tasks/task_intent.py:307-328; mcp/src/agents_remember/tasks/task_intent.py:331-361 |
| The shared exhaustive field-effect taxonomy consumed here. | `TaskDocumentFieldEffect`; `fields_with_effect` | mcp/src/agents_remember/tasks/document_field_effects.py:55-64; mcp/src/agents_remember/tasks/document_field_effects.py:527-537 |
| The typed slot/identity models imported from the sibling model module. | `TaskIntentIdentity`; `ApprovedRequirementPacketRef` | mcp/src/agents_remember/models/task_intent/__init__.py:55-59; mcp/src/agents_remember/models/task_intent/__init__.py:22-36 |

## CCR-R02@v2 Normative Task-Intent Identity

This module is the projection/identity half of CCR-R02@v2. Its canonical packet
(`requirements/CCR-R02-v2-normative-task-intent-identity.md`) requires closeout evidence to bind
a separate versioned normative task-intent identity that changes only for obligation/plan changes.
The allowlist + shared-taxonomy rule and the "decision prose is audit-only" rule are implemented
here. The L25 delivery verified at `99dc249b` carries the sealed L02 Attempt-10 candidate per
`notes/reports/260831-CCR-L25-worker-delivery.md`.

## Update History
- 2026-09-29T21:49:50+00:00: Generated citation repair: `task_intent_identity` repointed to mcp/src/agents_remember/tasks/task_intent.py:197-210. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:49:50+00:00: Generated citation repair: `require_current_task_intent` repointed to mcp/src/agents_remember/tasks/task_intent.py:244-262. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:49:50+00:00: Generated citation repair: `_validate_allowlisted_classifications` repointed to mcp/src/agents_remember/tasks/task_intent.py:287-304. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:49:50+00:00: Generated citation repair: `_requirements`; `_approved_packet_ref` repointed to mcp/src/agents_remember/tasks/task_intent.py:307-328; mcp/src/agents_remember/tasks/task_intent.py:331-361. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** Added the Logic bullet on the optional `expectedKnowledgeEffects` slot (key dropped when absent, and from a master's projection) and the Invariants bullet that an absent field leaves every existing digest unchanged. **The reopened `_NESTED_FIELDS` claim was re-read and reworded** (the allowlists now include the declaration) and re-measured. The prose line hints of the Logic list were brought to the current lines. Two rows added; other rows were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `require_current_task_intent` repointed to mcp/src/agents_remember/tasks/task_intent.py:225-243. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `_validate_allowlisted_classifications` repointed to mcp/src/agents_remember/tasks/task_intent.py:268-285. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  created this card for the new canonical task-intent projection module (`task_intent_projection`,
  `task_intent_identity`, `require_current_task_intent`, allowlist/taxonomy symmetry checks,
  approved-packet resolution); documented the leaf-only and never-a-whole-document-hash boundaries.
  Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.
