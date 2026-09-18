# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-11T10:26:37+02:00 |
| lastVerifiedCommitHash | `65e3791bce458eb6265f752889435a1bcaac5f2e` |
| lastVerifiedCommitDate | 2026-09-18T06:16:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns status, prepare, publish, and validate dispatch plus crash-safe, idempotent compare-and-swap
publication of curator-coherence generations and optional attempt snapshots. Since KS-R24@v1 the
`prepare` response also **states the complete publication input set**, derived from the request model's
own member declaration rather than from a second handwritten list.

## Code Commentary

### Logic

`prepare` returns all current identities and the raw stable-authority predecessor digest, and its
summary is `publication_input_statement()` read from the request model's declaration: it names the
per-candidate judgments and every publication member, and marks the two members it does not derive
(`semantic_requirement_revision`, `delivery_attempt`) as caller-supplied delivery identities. The text
is a pure function of that declaration, so a member appended to it reaches this response with no edit
here. `prepare` still invents neither identity and the response still carries no value for either.
`publish` validates caller-supplied expectations and exact judgments before entering the short task
publication lock. Inside the lock it rereads the contract, rechecks predecessor, source identities,
and evidence bytes, atomically installs a deterministic content-addressed record/report directory,
optionally freezes the attempt pointer, rechecks again, and writes the stable authority last.
`validate` delegates to the shared currentness validator. Publication fingerprints contain all
semantic input, so exact retries converge even after a crash left a generation but not the pointer.

Under CCR-R03@v1 `_record` now builds the immutable record's `curator-coherence/v1` dependency
declaration from the observed code/memory candidate trees, task-topology fingerprint,
digest-bearing task intent, attestation and report digests, every judgment evidence digest, and the
predecessor authority digest — so the published generation is a declared content-addressed consumer
of exactly its inputs cit:([`_record`], mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:352-451).

### Conventions

Only the exact leaf curator or owning sprint architect may publish. Content-addressed generations
are immutable; a byte collision is a developer-decision failure rather than overwrite permission.
Dependency declarations are built with the shared evidence-dependency encoding, exactly as the
currentness validator re-derives them.

### Invariants And Boundaries

- The stable authority is written only after a complete generation and final CAS checks.
- No partial generation can become live.
- Malformed predecessor bytes are replaceable only through an exact prepared digest.
- No clock value enters canonical content, preserving retry identity.
- Snapshot naming uses delivery attempt plus record digest; it cannot version the requirement.
- Publication never invents semantic judgments, and `prepare` never invents a delivery identity: it
  states that the caller must supply them.
- The `prepare` text is derived from the request model's `PUBLICATION_MEMBERS` declaration, never from a
  copy that can drift out of step with the validator.
- The declared dependency set is part of the generation installed under CAS: it binds the published
  record to the exact candidate, topology, intent, attestation, and evidence inputs, and no
  unrelated change can stale it.

### Todos

None recorded.

## Docs References

No external documentation governs this local transaction.

| Finding | Anchor | Source |
| --- | --- | --- |
| The publication transaction is repository-owned. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public action dispatcher keeps one tool surface. | `curator_coherence_action` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:88-98 |
| **The prepare response composes its summary from the request model's publication declaration, so it states every publication input.** | `_prepare` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:145-160 |
| **The statement `prepare` carries, defined on the request-model route rather than here.** | `publication_input_statement` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:386-411 |
| Publication rechecks contract, predecessor, candidates, attestation, topology, and evidence before selecting authority. | `_publish` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:144-219 |
| Immutable generation installation is directory-atomic and collision-safe. | `_publish_generation` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:593-628 |
| Attempt snapshots point at immutable generation artifacts. | `_publish_snapshot` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:631-664 |
| R03 record construction binds the declared dependency set. | `_record` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:352-451 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The task publication lock this route once consulted was deleted with the whole lock plane (commit `1a0919c1`); publication no longer takes a CAS mutex. | — | — |

## MCAR-L03 Pair-Bound Publication

The immutable record, observation identity, publication fingerprint, race check, prepared/published
payloads, and validation checklist all include the exact pair. A pair change therefore invalidates
publication and idempotent replay even when candidate files are otherwise valid.

## 260831-CCR-R03 Dependency-Declared Publication

Publication now stamps the record's `curator-coherence/v1` dependency declaration from the exact
observed inputs before CAS installation (worker handover:
notes/reports/260902-CCR-L03-worker-delivery.md).

## KS-R24@v1 Prepare States The Publication Inputs

`_prepare` composes its summary from `publication_input_statement()`, so the prepared response states
the inputs `publish` requires instead of only the judgments. The shipped sentence named the judgments
and stopped; a caller who followed the documented `prepare` → supply a judgment per candidate →
`publish` flow supplied the seven members `prepare` echoes, was refused, re-read `prepare`, learned
nothing, and could only discover the ninth and tenth members by reading the validator — which is how
two leaves of this master recorded a wrong impossibility claim against the tool
(`notes/DISCLOSURES.md` D-11).

Two properties of the text matter and both are asserted by cases in
`mcp/tests/test_final_full_memory_coherence_certification.py`:

- **It is derived, not copied.** The statement reads the request model's `PUBLICATION_MEMBERS` at call
  time; a member appended to that declaration appears in the response with no second edit here.
- **It attributes the two identities to the caller.** `semantic_requirement_revision` and
  `delivery_attempt` are statements about the delivery attempt and stay the caller's to author, so the
  text marks them as caller-supplied delivery identities `prepare` does not derive from the observation
  it returns. `_prepare` still returns no value for either and cannot publish on its own; `_publish` is
  untouched by this requirement and only the summary string changed in this module.

## KS-R15@v1 Assessment Publication And Evidence Bytes

The publication path now accepts the assessment collection and publishes its cited bytes, and the two
additions are wired so that neither can succeed half-way.

`_exact_review_assessments` stamps authorship from the **authenticated caller** — the author and role
the publication path already holds — onto each submitted revision, so the stored record's author is
whatever the publication path supplied and never caller text. `_published_evidence_bytes` publishes
each assessment's cited bytes to the task-root destination
`<task_root>/notes/reports/evidence/<assessment_id>/<filename>` through
`curator_assessment_evidence.publish_assessment_evidence_bytes`, which **opens every byte again before
it returns**; a failed read-back is a blocked state carrying the destination, the expected digest and
the observed state, and it is never reported as published.

The record's own edge to a stored assessment is written from this side, which is why the assessment's
binding never declares the record it lives in. Publishing an assessment leaves the shipped exact-
coverage obligation `_judgments_cover_candidates_exactly` exactly as it was: the assessment collection
is content beside `judgments`, and the coverage rule still relates judgments to source candidates and
nothing else.

## Update History
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): **re-read this card against the changed source and recorded the two extensions the leaf made, then retired the generated projection bullets that were holding its claims open.** `_exact_review_assessments` stamps an assessment's authorship from the authenticated caller, and `_published_evidence_bytes` publishes each cited byte to the task-root destination and opens every one again by its recorded path and digest before it returns, reporting a failed read-back as a blocked state rather than as published. The record's own `review-record` edge per stored assessment is written from this side, which is why the assessment's binding never declares the record it lives in. Every claim in this card whose cited range the leaf's edits moved was re-cited to the construct it is about rather than accepted from the mechanical projection — `curator_coherence_action` `:88-98`, `_prepare` `:145-160`, `publication_input_statement` `:386-411`, `_publish_generation` `:593-628`, `_publish_snapshot` `:631-664` and `_record` `:352-451` — and the body above records the extension rather than only its coordinates. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-18T03:15+02:00 — 260915-KS-L24 curator (uncommitted change set on `ar/260915-ks-l24`, base `9c12e8b1`): **re-read this card against the changed source and recorded what `prepare` now says.** `_prepare` composes its summary from `publication_input_statement()` — the request model's own declaration — so the prepared response names the per-candidate judgments **and** all nine publication members and marks the two it does not derive; the Purpose, Logic and Invariants sections of this card say so, and a new section states the two properties that carry the requirement (derived rather than copied, and the identities still the caller's to author) together with the wrong-impossibility record (`notes/DISCLOSURES.md` D-11) that the shipped sentence produced twice. The reference table was re-derived from the current file while re-reading it: `curator_coherence_action` is `:64-74`, `_publish` `:144-219`, `_publish_generation` `:452-487`, `_publish_snapshot` `:490-523` and `_record` `:222-314`, each corrected from the pre-leaf coordinates this card carried, and `_prepare` gained its own row. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_publish_generation` repointed to mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:451-486. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_publish_snapshot` repointed to mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:489-522. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: retired the evidence row citing the deleted `task_publication_lock.py` and recorded that publication no longer takes a CAS mutex. Verification metadata remains pinned because only the cut-affected reference was reconciled; source documentation only, no acceptance claim.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the dependency declaration built by `_record` during publication; prior CAS, retry-identity, and pair publication prose preserved.

- 2026-08-29T21:46+02:00 — MCAR-L03: bound publication, CAS/race identity, and validation output
  to the exact code/memory pair. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Created for deterministic, exact-CAS, crash-safe coherence authority
  publication. Verification remains closeout-owned.