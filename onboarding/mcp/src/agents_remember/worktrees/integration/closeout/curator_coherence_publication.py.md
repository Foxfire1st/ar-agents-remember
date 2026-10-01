# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns status, prepare, publish, and validate dispatch plus crash-safe, idempotent compare-and-swap
publication of curator-coherence generations and optional attempt snapshots. Since KS-R24@v1 the
`prepare` response also **states the complete publication input set**, derived from the request model's
own member declaration rather than from a second handwritten list. Since KS-R23@v1 it also resolves a
bare leaf-document caller name against the addressed contract, names the demanded path shape in the
refusal that rejects one, and copies the bound memory-quality attestation into the surviving task tree
beside the record.

## Code Commentary

### Logic

After exact judgment admission and predecessor checks, `_publish` retains the original judgment bytes through the existing custody owner. Once the immutable record/projection and attestation copy exist, their shared generation integrity read must succeed before the stable canonical pointer is replaced. Alias, foreign-path or corrupt-evidence rejection leaves the prior canonical authority intact. Live source and original-input checks remain part of the CAS window.

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
of exactly its inputs cit:([`_record`], mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:363-464).

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

## Evidence

### Docs References

No external documentation governs this local transaction.

The publication transaction is repository-owned.

### Repo-Internal References

- The public action dispatcher keeps one tool surface. [1]
- **The prepare response composes its summary from the request model's publication declaration, so it states every publication input.** [2]
- **The statement `prepare` carries, defined on the request-model route rather than here.** [3]
- Publication rechecks contract, predecessor, candidates, attestation, topology, and evidence before selecting authority. [4]
- Immutable generation installation is directory-atomic and collision-safe. [5]
- Attempt snapshots point at immutable generation artifacts. [6]
- R03 record construction binds the declared dependency set. [7]

The following declarations carry the changed boundary.

- Full generation integrity is proved before canonical authority replacement. [8]

### Cross-Repo References

No meaningful cross-repository reference applies.

The task publication lock this route once consulted was deleted with the whole lock plane (commit `1a0919c1`); publication no longer takes a CAS mutex.

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

## KS-R23@v1 The Caller Refusal States The Shape It Demands

D-26 measured the cost of leaving the caller's path shape unsaid: `caller.task_document_ref.path` has to
be the task-root-relative document path (`<task-slug>/<leaf-document-file>`), and nothing said so — not
the refusal, not `status`/`prepare`, not the contract — so the only way to learn it was the refused call
the schema exists to prevent.

Three things changed, and the third is what makes the first two safe.

- `_CALLER_PATH_SHAPE` (`:463-470`) declares the demanded shape once, beside the function that refuses on
  it. `_caller_refusal_detail` (`:530-546`) composes the refusal from it: the shipped sentence —
  `publish requires the exact leaf curator or owning sprint architect` — is kept and followed by the
  shape **and this contract's exact expected value** (the canonical `path` in its `repository`, and the
  bare file name that is equally acceptable), plus the value actually received, so the correction is
  readable without a second refused call.
- `_authorize_publisher` became `_authorized_publisher` (`:473-511`). It no longer authorizes and
  discards: it returns the **resolved** `DeclaredCaller`, and the refusal it raises carries
  `expected`/`observed` (role plus both refs), which `application/curator_coherence._domain_refusal`
  projects onto the wire.
- `_resolve_caller_ref` (`:513-528`) resolves a **bare** file name (no `/`) against the addressed
  document, and only when the repository matches and the name is exactly that document's own file name.
  The contract already identifies the leaf unambiguously, so that name cannot mean another document; a
  bare name for any other document is refused rather than resolved.

The resolved caller is what the record and the assessments carry: `_publish` passes it to
`_exact_review_assessments` (`:176`) and to `_record` (`:203`), whose `publishedBy` is
`f"{caller.role}@{caller.task_document_ref.key}"` built from the **resolved** ref (`:452`) rather than
the caller's spelling. A successful bare-name publication therefore carries the canonical identity in
the record and in an assessment's author alike, and `publish` still admits exactly the leaf curator or
the owning sprint architect.

## KS-R23@v1 The Bound Attestation Survives The Enclosure It Is Bound In

The same cleanup that closes the standalone `validate` window — `lifecycle_finalize_task`'s automatic
collection of the enclosure root — destroys the evidence a publication binds to: the record's
`attestationPath` is enclosure-local, `os.path.exists` is False for it on every landed leaf, and
`attestationSha256` therefore committed to bytes recoverable nowhere.

Publication now copies those exact bytes into the surviving task tree and records the path on the
record. `_publish_attestation_copy` (`:548-615`) reads the bound file, **re-verifies the bytes against
`observation.attestation_sha256`**, and writes the content-addressed copy
(`CuratorCoherencePaths.attestation_copy` — `<leaf>/attestations/<sha256>.json`, the location the
resolver card names) through `_write_fsynced` + `atomic_replace`, reclaiming the temporary on any
failure. It runs before the record is built (`:199-201`), its task-relative path rides
`_RecordPublication.attestation_copy_path`, and it is recorded as
`CuratorCoherenceRecord.attestationCopyPath`. Three typed refusals guard it, none of which existed
before: `curator-coherence-attestation-unreadable` (the bound file, or an existing copy, cannot be
read), `curator-coherence-attestation-stale` (the bytes moved between observation and the copy, reported
with both digests) and `curator-coherence-content-address-collision` (a content-addressed path already
holds different bytes).

The record is therefore not asked to stand in for the attestation's content: the bytes a reader would
have read are still readable, and a second publication over unchanged bytes reuses the same immutable
copy instead of rewriting it.
