# mcp/src/agents_remember/tasks/task_intent.py

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

## Evidence

### Docs References

The configured Domain Documentation registry is empty; no external documentation claim is made.

### Repo-Internal References

- Strict allowlisted v1 projection model. [1]
- Normative slot allowlists for the document and nested models, since MIK-R11 including `expectedKnowledgeEffects` and its three nested fields. [2]
- The optional declared-effects slot; absent is absent, so digests are unchanged. [3]
- The declaration projected into the leaf intent, and dropped from a master's. [4]
- Projection entry point refusing masters and translating taxonomy failures. [5]
- Canonical digest production from the projection. [6]
- Currentness/staleness assertion for owners. [7]
- Allowlist/taxonomy symmetry enforcement. [8]
- Requirement text/packet handling and the v2-cutover refusal. [9]
- The shared exhaustive field-effect taxonomy consumed here. [10]
- The typed slot/identity models imported from the sibling model module. [11]

## CCR-R02@v2 Normative Task-Intent Identity

This module is the projection/identity half of CCR-R02@v2. Its canonical packet
(`requirements/CCR-R02-v2-normative-task-intent-identity.md`) requires closeout evidence to bind
a separate versioned normative task-intent identity that changes only for obligation/plan changes.
The allowlist + shared-taxonomy rule and the "decision prose is audit-only" rule are implemented
here. The L25 delivery verified at `99dc249b` carries the sealed L02 Attempt-10 candidate per
`notes/reports/260831-CCR-L25-worker-delivery.md`.
