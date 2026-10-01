# mcp/src/agents_remember/memory/knowledge/detection.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Mechanical detection's records: the run's assembly, its write path, its read path, its comparison
against the versions now in force, and the manifest reference's own retention answer.**

This module owns the **record** half of `KS-R14@v1`. The walk that decides *which* recorded facts match
which declared condition is `memory/knowledge/detection_walk.py`; the two are split along the property
each one protects — the classification, and the record's own refusals — rather than along a call
boundary. Nothing here re-selects anything: the selection is the read policy's and the union is the diff
policy's, and neither is restated.

Five properties are enforced here rather than documented:

- **Nothing here publishes, archives or deletes.** A signal records its manifest reference, its
  retention state and the destination that was checked; a reference that cannot be resolved is reported
  `unresolved` with what would resolve it, never as an empty manifest. The durable publication route
  belongs to a later leaf.
- **A detection write never enters the assessed dataset's measurement transaction.** Requirement 7.1 is
  enforced as a refusal with its own code (`detection_self_reference`): the request names the databases
  it measured, and a detection store that *is* one of them is refused **before any row is written**, so
  a detector cannot move the identity of the dataset it just digested.
- **A recorded run's order is sealed.** The signals are written into `detection_run_signal` under
  generation 4's composite keys, and generation 4's triggers refuse reordering or shortening them — so
  "never overwrites the recorded one" holds against a later code path that forgot it as well as against
  this one.
- **A read is verified against its recorded seal.** The stored revision's own content digest is
  recomputed on the way out, so a payload altered behind its identity is reported as a damaged store
  rather than served as a recorded run.
- **The envelope's governing-route association stays unset.** A signal's governing route names a route
  in the *assessed* repository's namespace, and this record group's chosen home is a store that is not
  the assessed dataset. Binding the column would require copying the assessed route into the detection
  store, and a second copy of one fact is a second authority. The route is therefore still **required**:
  it is a validated `governing_route_id` field on the run and on every signal, both of which fail
  construction without it.

## Code Commentary

### Logic

**Generation gate and separation gate, in that order.** `record_detection_run` refuses before it writes
anything, and the order of the four gates is deliberate — scope, generation, separation, agreement:

1. `scope_refusal` — the request's repository must be the store's namespace.
2. `require_detection_generation` — the dataset's own declared generation is compared against
   `REQUIRED_DETECTION_GENERATION`, and a dataset that predates generation 4 is refused with
   `unsupported_schema` carrying **both** numbers as facts. Nothing is migrated, widened or written
   through; a dataset that predates the table is not repaired into having it.
3. `require_separate_from_assessed` — the detection store and every assessed database are resolved to
   their real paths, and an overlap is refused with `detection_self_reference`. This is the dataset's own
   file identity rather than a promise.
4. `require_run_signal_agreement` — the run's namespace, its declared order, and for every signal its
   namespace, policy version, extractor version, declared input set and condition must agree with the
   run it is presented on.

Only then does `record_detection_run` take the store's exclusive candidate lock and run `_write_run`
inside one immediate transaction. `_write_run` writes the run's envelope, then each signal's, then one
`detection_run_signal` row per ordinal via `enumerate`, so the recorded order **is** the sequence the
walk produced. `_write_envelope` validates every payload through `validate_record_payload` even though
the typed request already produced it, because that function is the only place a write path decides
whether a payload is admissible and a second path that skipped it would be a second decision. The
envelope's `governing_route_id` column is passed as `None` with the reason written beside it;
`authority_home` is read from the store's own repository row rather than accepted from a caller, and the
lifecycle is the constant `DETECTION_RECORD_LIFECYCLE`.

**The read answers the recorded order, not the row order.** `read_detection_run` re-checks the
generation, reads the run row and refuses a missing identity with `missing_expected_row`, then reads the
ordered signal identities from `detection_run_signal` and decodes each one. `_decode_payload` recomputes
the stored revision's own content digest through `record_revision_digest` and compares it with the
stored value — a mismatch raises `KnowledgeStorageError` naming stored and recomputed digests and
telling the reader to treat the store as damaged. It also refuses a stored `record_schema` that is not
the one the operation resolved, and resolves the model from the envelope registry rather than from the
caller.

**A caller that needs *every* run is given the identities, and each run's signals are then read through
this same reader — never through a second reader of the same tables** (`ICR-R14@v1`).
`recorded_run_ids(store)` answers the recorded run identities in identity order: the `kind` filter is the
module's own `DETECTION_RUN_KIND`, the repository scope is the store's namespace, and the answer is
identities only — no envelope, no payload, no decode. It exists because "which runs does this namespace
record" and "what did this run measure" are different questions with different failure behavior: the
listing can be served while one of the runs it names is damaged, which is what lets a composing reader
name that one run and still supply its siblings' signals. The order is the recorded identities' own, so
two reads of one namespace answer the same sequence, and the function writes nothing and refuses
nothing it cannot read — a store whose table is unreadable surfaces `KnowledgeStorageError` to the
caller rather than an empty listing, because an unreadable listing is not "no runs".

**Reproducibility, currentness and retention are read-only answers.** `compare_detection_runs` compares
a recorded run with its re-execution and names **every** axis that differs: the three versions, the
declared input sets, the recorded conditions, and per side the snapshot logical digest, the code tree
and the selector digest. It writes nothing: a re-execution that differs is reported as two distinct runs
and the recorded one is untouched. `run_currentness` marks a run `current` or `stale` from the version
comparison alone and returns no signal. `resolve_manifest_reference` delegates to the manifest's own
`resolve`, so there is one definition of "retained".

**Identities are derived rather than drawn.** `_revision_id_of` is a `uuid5` over
`ar-detection-revision/v1/<kind>/<record_id>`, so a record's first revision identity is a function of
the record rather than a fresh UUID, and `detection_payload_digest` hashes a canonical payload for a
caller comparing two recorded payloads.

**A run's inputs are an identity and a digest over it, so a caller can name the exact execution it
wants reported.** `detection_input_identity(run)` returns the run's inputs as one JSON value: the
namespace and assessed namespace it was bound to, its registered `governing_route_id`, the policy,
extractor and condition-vocabulary versions it ran under, the declared input sets, and — per side —
the exact logical digest, the optional code tree and repository root, the task reference, and the
selector digest and policy version that read it. `detection_input_digest(run)` is
`sha256_digest(detection_input_identity(run))`. Nothing is read from the clock, the filesystem or the
caller, so two runs with different inputs get different digests and one run always gets the same one —
which is what lets the mounted integrity check take a caller's `inputDigest` as a **binding** rather
than a hint, and report the run it actually read. The run's own `run_id` travels inside the identity as
well, so two executions over identical inputs still carry two digests: the digest stands for the
execution, not merely for the input pair. This is a deliberate, reviewable choice rather than an
incidental one, and it is recorded as an open question the review owns: a caller wanting "the digest of
these inputs regardless of which run measured them" is asking a different question from the one this
function answers, and the two are not interchangeable.

### Conventions

- The module's SQL is seven module-level statement constants (`_RECORD_INSERT`, `_REVISION_INSERT`,
  `_SEQUENCE_INSERT`, `_RUN_ROW`, `_RUN_REVISION`, `_SEQUENCE_ROWS`, and `_RECORDED_RUN_IDS` — the
  identity listing the run collection is read from), so no statement is built by string interpolation
  at a call site.
- Every refusal is built through the shipped `refusal`/`scope_refusal` helpers with `RefusalFacts`
  carrying `expected`, `observed` and the table, and every refusal ends with a `next_action` that says
  what to do and whether anything was written.
- **The module is split from the walk by protected property, not by call boundary.** The walk owns the
  classification and no SQL; this module owns the store's refusals and the transaction. Neither imports
  the other.
- `DetectionRunAssembly` is a frozen dataclass, so the run's binding travels as one value: a builder
  handed the identities separately could be handed one run's identity with another run's assessed
  repository.

### Invariants And Boundaries

- **Refuse before writing, and say so.** Every gate runs before the lock is taken, and the refusals'
  `next_action` states that nothing was written; the self-reference refusal names the detection store
  and the assessed candidate it collided with.
- **The write is one transaction.** Run, signals and sequence rows are written inside
  `store.within_immediate`, so a partial detection record cannot exist.
- **The recorded sequence is immutable at the database, not only here.** Generation 4's two triggers are
  what refuse a later reorder or shortening; the operation's own preconditions are what return a typed
  refusal.
- **Nothing in this module publishes, archives, deletes or re-runs.** A re-execution is compared, never
  merged; a manifest is referenced, never materialized.
- **An input identity is a function of the recorded run and of nothing else.** `detection_input_identity`
  reads the run's own bound fields — namespace, assessed namespace, registered route, the three
  versions, the declared input sets, and each side's snapshot, optional tree and selector — and never
  consults the dataset the run sits in, the clock or the caller; `detection_input_digest` hashes that
  value through the shared `sha256_digest` helper, so the same run always answers the same digest and
  two runs recorded in one scope over different snapshots, trees or selectors do not collide. The run id
  is inside the identity, which means the digest distinguishes two executions over identical inputs —
  the digest names the execution, not only its input pair.
- **The listing and the read are two questions, and the listing answers only its own.**
  `recorded_run_ids` returns identities and decodes nothing, so a damaged run does not make the
  listing unreadable; reading each identity is `read_detection_run`'s job, and a caller that wants a
  per-record guard composes the two rather than asking this module for a second reader. An unreadable
  listing table is a `KnowledgeStorageError`, never an empty tuple standing for "no runs".
- **Boundary.** It does not select records, classify conditions or author prose: selection is the read
  policy's, the union is the diff policy's, classification is `detection_walk.py`, and the two detail
  renderings live in `models/knowledge/detection.py`. It also does not decide *which* recorded run in a
  scope should be reported: that selection belongs to the mounted tool, and this module only supplies
  the identity that lets a caller name one exactly.

### Todos

None recorded. The manifest's resolution is exercised as a recorded state transition against a supplied
destination observation rather than against a real published archive, because the durable publication
route does not exist on this branch; the packet declares that forward reference, and requirement 4.5
asks this module for exactly the behaviour it has — record the reference, its retention state and the
destination that was checked.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The generation a detection write requires, and the generation refusal that carries the observed and required versions as facts without migrating anything. [1]
- **Requirement 7.1 as a structural refusal: real-path identity of the detection store against every assessed database, refused with `detection_self_reference` before any row is written.** [2]
- The write path: the four gates in order, the exclusive candidate lock, and the one immediate transaction. [3]
- **Requirement 7.1 as a structural refusal: real-path identity of the detection store against every assessed database, refused with `detection_self_reference` before any row is written.** [4]
- The write path: the four gates in order, the exclusive candidate lock, and the one immediate transaction. [5]
- **The envelope write and the reason its governing-route association is left unset: the route lives in the assessed namespace and a copied association would be a second authority.** [6]
- The run's binding as one value: identity, namespace, assessed namespace, route, sides and the two published versions. [7]
- **The sequence write: one `detection_run_signal` row per ordinal, in the order the walk produced the signals.** [8]
- The authority home read from the store's own repository row rather than accepted from a caller. [9]
- **The agreement check that keeps the two-place version publication true: namespace, order, policy version, extractor version, declared input set and condition.** [10]
- **The read path: the recorded order from the sequence table, and the seal recheck that reports an altered payload as a damaged store.** [11]
- **The run-identity listing a composing reader addresses its per-run reads by: identities only, in identity order, decoding nothing — so a damaged run does not make the listing unreadable.** [12]
- **The one composing reader this listing exists for, and the per-record guard it composes with the read above.** [13]
- **Reproducibility as two ordered sequences plus every differing input or version, writing nothing.** [14]
- The per-side differences: snapshot logical digest, code tree and selector digest. [15]
- **Currentness marks a run stale from the version comparison alone and returns no signal to reinterpret.** [16]
- The retention answer, delegated to the manifest's own resolution so there is one definition of retained. [17]
- The declared input set vocabulary as a value, and the payload digest helper. [18]
- The run's exact inputs as one canonical identity, and the digest over it that a mounted caller names to bind a reported run. [19]
- The envelope seam every written payload passes through, which is the only place a write path decides admissibility. [20]
- The composition this module's generation comes from — one anchor, one source, because a row naming several anchors across several files cannot resolve to a single extent. [21]
- **The two immutability triggers that seal a recorded detection sequence — the reason a later code path that forgot the rule still cannot reorder or shorten it.** [22]
- The revision draft, row tuple and digest the detection write and read reuse rather than re-implementing. [23]
- The two operation members and the one refusal code only a detection write can reach. [24]
- The two operation members and the one refusal code only a detection write can reach. [25]
- The store the write runs inside, its immediate-transaction helper and its exclusive candidate lock. [26]
- **The cases that measure the ordered round trip, the two-place versions, the self-reference refusal and the sealed sequence.** [27]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
