# mcp/src/agents_remember/memory/knowledge/detection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/detection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T21:50:00+02:00 |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc` |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The generation a detection write requires, and the generation refusal that carries the observed and required versions as facts without migrating anything. | `REQUIRED_DETECTION_GENERATION`; `require_detection_generation` | mcp/src/agents_remember/memory/knowledge/detection.py:86-90; mcp/src/agents_remember/memory/knowledge/detection.py:199-229 |
| **Requirement 7.1 as a structural refusal: real-path identity of the detection store against every assessed database, refused with `detection_self_reference` before any row is written.** | `require_separate_from_assessed` | mcp/src/agents_remember/memory/knowledge/detection.py:230-266 |
| The write path: the four gates in order, the exclusive candidate lock, and the one immediate transaction. | `record_detection_run` | mcp/src/agents_remember/memory/knowledge/detection.py:271-299; mcp/src/agents_remember/models/knowledge/result.py:105-105 |
| **Requirement 7.1 as a structural refusal: real-path identity of the detection store against every assessed database, refused with `detection_self_reference` before any row is written.** | `require_separate_from_assessed` | mcp/src/agents_remember/memory/knowledge/detection.py:230-266 |
| The write path: the four gates in order, the exclusive candidate lock, and the one immediate transaction. | `record_detection_run` | mcp/src/agents_remember/memory/knowledge/detection.py:271-299 |
| **The envelope write and the reason its governing-route association is left unset: the route lives in the assessed namespace and a copied association would be a second authority.** | `_EnvelopeWrite`; `_write_envelope` | mcp/src/agents_remember/memory/knowledge/detection.py:301-323; mcp/src/agents_remember/memory/knowledge/detection.py:366-419 |
| The run's binding as one value: identity, namespace, assessed namespace, route, sides and the two published versions. | `DetectionRunAssembly`; `build_detection_run` | mcp/src/agents_remember/memory/knowledge/detection.py:133-183 |
| **The sequence write: one `detection_run_signal` row per ordinal, in the order the walk produced the signals.** | `_write_run` | mcp/src/agents_remember/memory/knowledge/detection.py:324-365 |
| The authority home read from the store's own repository row rather than accepted from a caller. | `_authority_home` | mcp/src/agents_remember/memory/knowledge/detection.py:426-441 |
| **The agreement check that keeps the two-place version publication true: namespace, order, policy version, extractor version, declared input set and condition.** | `require_run_signal_agreement`; `_signal_disagreement` | mcp/src/agents_remember/memory/knowledge/detection.py:446-531 |
| **The read path: the recorded order from the sequence table, and the seal recheck that reports an altered payload as a damaged store.** | `read_detection_run`; `_decode_payload`; `_require_intact_revision` | mcp/src/agents_remember/memory/knowledge/detection.py:582-704; mcp/src/agents_remember/models/knowledge/result.py:106-106 |
| **The run-identity listing a composing reader addresses its per-run reads by: identities only, in identity order, decoding nothing — so a damaged run does not make the listing unreadable.** | `recorded_run_ids`; `_RECORDED_RUN_IDS` | mcp/src/agents_remember/memory/knowledge/detection.py:565-581; mcp/src/agents_remember/memory/knowledge/detection.py:118-124 |
| **The one composing reader this listing exists for, and the per-record guard it composes with the read above.** | `_detection_signals`; `_read_signal_runs` | mcp/src/agents_remember/application/review_evidence_records.py:305-331; mcp/src/agents_remember/application/review_evidence_records.py:366-391 |
| **Reproducibility as two ordered sequences plus every differing input or version, writing nothing.** | `compare_detection_runs`; `_run_differences` | mcp/src/agents_remember/memory/knowledge/detection.py:705-761 |
| The per-side differences: snapshot logical digest, code tree and selector digest. | `_side_differences` | mcp/src/agents_remember/memory/knowledge/detection.py:768-814 |
| **Currentness marks a run stale from the version comparison alone and returns no signal to reinterpret.** | `run_currentness` | mcp/src/agents_remember/memory/knowledge/detection.py:815-848 |
| The retention answer, delegated to the manifest's own resolution so there is one definition of retained. | `resolve_manifest_reference` | mcp/src/agents_remember/memory/knowledge/detection.py:849-863 |
| The declared input set vocabulary as a value, and the payload digest helper. | `declared_input_set_members`; `detection_payload_digest` | mcp/src/agents_remember/memory/knowledge/detection.py:864-869; mcp/src/agents_remember/memory/knowledge/detection.py:870-875 |
| The run's exact inputs as one canonical identity, and the digest over it that a mounted caller names to bind a reported run. | `detection_input_identity`; `detection_input_digest` | mcp/src/agents_remember/memory/knowledge/detection.py:876-915; mcp/src/agents_remember/memory/knowledge/detection.py:916-925 |
| The envelope seam every written payload passes through, which is the only place a write path decides admissibility. | `validate_record_payload` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:236-280 |
| The composition this module's generation comes from — one anchor, one source, because a row naming several anchors across several files cannot resolve to a single extent. | `_compose_generation_4` | mcp/src/agents_remember/memory/knowledge/schema_generations.py:327-335 |
| **The two immutability triggers that seal a recorded detection sequence — the reason a later code path that forgot the rule still cannot reorder or shorten it.** | `APPENDED_TRIGGERS` | mcp/src/agents_remember/memory/knowledge/schema_v4.py:106-116 |
| The revision draft, row tuple and digest the detection write and read reuse rather than re-implementing. | `RecordRevisionDraft`; `record_revision_row`; `record_revision_digest` | mcp/src/agents_remember/memory/knowledge/facet_records.py:86-96; mcp/src/agents_remember/memory/knowledge/facet_records.py:193-207; mcp/src/agents_remember/memory/knowledge/facet_records.py:209-230 |
| The two operation members and the one refusal code only a detection write can reach. | `record_detection_run`; `read_detection_run`; `detection_self_reference` | mcp/src/agents_remember/models/knowledge/result.py:202-212; mcp/src/agents_remember/models/knowledge/result.py:186-186; mcp/src/agents_remember/models/knowledge/result.py:97-97; mcp/src/agents_remember/models/knowledge/result.py:106-106; mcp/src/agents_remember/models/knowledge/result.py:105-105; mcp/src/agents_remember/models/knowledge/result.py:220-220; mcp/src/agents_remember/models/knowledge/result.py:230-230 |
| The two operation members and the one refusal code only a detection write can reach. | `record_detection_run`; `read_detection_run`; `detection_self_reference` | mcp/src/agents_remember/models/knowledge/result.py:88-106; mcp/src/agents_remember/models/knowledge/result.py:163-212; mcp/src/agents_remember/models/knowledge/result.py:220-220; mcp/src/agents_remember/models/knowledge/result.py:230-230 |
| The store the write runs inside, its immediate-transaction helper and its exclusive candidate lock. | `OpenedKnowledgeStore` | mcp/src/agents_remember/memory/knowledge/store.py:96-120 |
| **The cases that measure the ordered round trip, the two-place versions, the self-reference refusal and the sealed sequence.** | "test_a_recorded_run_reads_back_in_its_recorded_order_with_two_place_versions"; "test_a_detection_write_into_an_assessed_database_is_refused"; "test_a_recorded_detection_sequence_cannot_be_reordered_or_shortened" | mcp/tests/test_knowledge_detection_runs.py:909-945; mcp/tests/test_knowledge_detection_runs.py:946-980; mcp/tests/test_knowledge_detection_runs.py:769-799 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-21T21:50:00+02:00 — 260921-ICR-L14 curator (uncommitted change set on `ar/260921-icr-l14`, production line `d80a0513e928ef29a973527d09597c82c96fde87`): **this owner gained one read, and a Conventions count on this card became false with it.** `recorded_run_ids` (`memory/knowledge/detection.py:565-581`) answers every recorded detection-run identity in this namespace, in identity order, over the new `_RECORDED_RUN_IDS` statement — identities only, decoding nothing — because `ICR-R14@v1`'s composing reader must address its per-run reads by identity and must **not** grow a second reader of the same tables. The Logic section now states why the listing and the read are different questions with different failure behaviour: the listing can be served while one of the runs it names is damaged, which is what lets the composing reader name that run and still supply its siblings' signals; and an unreadable listing table surfaces `KnowledgeStorageError` rather than an empty tuple standing for "no runs". The Conventions bullet that enumerated **six** module-level SQL constants now says seven and names `_RECORDED_RUN_IDS` — the count had been measured before this leaf and was corrected rather than left stale. An Invariants bullet records the listing/read split and forbids asking this module for a second reader. **No reader, writer, refusal or precondition moved**: the change is one additive read and its statement, so the write path, the read path's own body and every existing case are untouched. **Citation accounting:** every range into this file was re-derived from each construct's own declaration extent in the candidate rather than shifted, because this leaf's insertions moved everything below `:117` — `REQUIRED_DETECTION_GENERATION` `84-86`→`86-90`, `require_detection_generation` `191-219`→`199-229`, `require_separate_from_assessed` `222-256`→`230-266` (and the second row that cited its extent as `18-256` now cites the same declaration rather than a whole-file span), `record_detection_run` `263-289`→`271-299`, `_EnvelopeWrite`/`_write_envelope` `292-313`/`358-409`→`301-323`/`366-419`, `DetectionRunAssembly`/`build_detection_run` `124-173`→`133-183`, `_write_run` `316-355`→`324-365`, `_authority_home` `418-431`→`426-441`, `require_run_signal_agreement`/`_signal_disagreement` `438-521`→`446-531`, the read path `557-673`→`582-704`, `compare_detection_runs`/`_run_differences` `680-734`→`705-761`, `_side_differences` `741-785`→`768-814`, `run_currentness` `788-819`→`815-848`, `resolve_manifest_reference` `822-834`→`849-863`, `declared_input_set_members` `844-847`→`864-869`, `detection_payload_digest` `850-853`→`870-875`, `detection_input_identity` `856-893`→`876-915` and `detection_input_digest` `896-905`→`916-925`. Two rows were **added**: the listing with its statement, and the one composing reader it exists for with the per-record guard it composes. No claim was re-worded beyond the corrected count and the new paragraph, and no row was dropped. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` now name the **production line this reading was against** — `d80a0513e928ef29a973527d09597c82c96fde87`, the master line's current tip and this leaf's base — replacing the previous pair rather than leaving a stamp no reading in this pass measured; the candidate is uncommitted, so no commit contains the content a stamp would claim to have verified, and the governed closeout's own metadata refresh re-stamps the card against the code commit its transaction creates.
- 2026-09-20T05:26+02:00 — 260915-KS-L41 curator (uncommitted change set on `ar/260915-ks-l41-ar`, code base `756c47b3` at this leaf's cut and `f79f4db745ad00b908d6ce4871d0b4ab2320207c` after the L39 sync, memory base `da33325c` at the cut and `37d0787571bfbf92890049ee0614fa159012be39` after it): **body update for the input-identity pair this leaf adds, which is the half of the exact-binding finding that belongs to this module.** `detection_input_identity` (`memory/knowledge/detection.py:856-893`) returns a run's inputs as one canonical JSON value — namespace, assessed namespace, registered route, the three versions, the declared input sets and, per side, the snapshot logical digest, the optional code tree and root, the task reference and the selector digest and policy — and `detection_input_digest` (`:896-905`) hashes it. The Logic section now says that under *Identities are derived rather than drawn*, the Invariants list gained the property that the identity is a function of the recorded run and of nothing else, and the Boundary entry now states that this module does not decide which recorded run in a scope gets reported. Both functions are on the reference table. One deliberate semantic choice is recorded on the card rather than presented as settled: the run's own `run_id` travels inside the identity, so two executions over identical inputs carry two digests — the digest names the execution and not only the input pair — and the review owns that question. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained as recorded; the candidate is uncommitted and the governed closeout owns the real stamp, and no stamp was advanced or invented.
- 2026-09-18T19:56:02+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document** (one table row, two anchors). The row cited `593-640` and `732-768`, two earlier regions, for the self-reference refusal case and the sealed-sequence case. Those two nodes are defined at `909-945` and `946-980` in the same file, so the two cells cite their definitions now; the ordered-round-trip range at `769-799` and the claim are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `_compose_generation_4` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:327-335. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `declared_input_set_members`; `detection_payload_digest` repointed to mcp/src/agents_remember/memory/knowledge/detection.py:864-869; mcp/src/agents_remember/memory/knowledge/detection.py:870-875. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `validate_record_payload` repointed to mcp/src/agents_remember/memory/knowledge/record_envelope.py:236-280. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `_compose_generation_4` repointed to mcp/src/agents_remember/memory/knowledge/schema_generations.py:316-324. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 2 claim(s) here (2 x citation_provenance_invalid). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 2 generated projection bullet(s) by hand while resolving the memory sync** — `validate_record_payload`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T06:30:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `15fe8678`): **re-read each of this card's reopened claims against the construct as the merged line now stands, confirmed the cited range is current, and retired 1 generated projection bullet(s) by hand** — `_compose_generation_4`. A mechanically projected range is unverified evidence, which is exactly why the check kept these claims reopened until an agent had read the construct they point at; the claims' wording is retained because each states what the construct does, and the ranges are the declarations the claims are about. Verification metadata advances to the merged base commit `15fe8678`.

- 2026-09-18T03:15:00+00:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): created this one-to-one card for the detection record module. It records the four gates and their order (scope, generation, separation, agreement) and that all of them run before the lock and before any row is written; requirement 7.1 as the real-path identity check that refuses `detection_self_reference` when the detection store *is* one of the datasets the run measured, with the self-invalidation reason stated rather than implied; the one immediate transaction that writes the run, its signals and one order row per ordinal; the **unset envelope governing-route association** and its reason (the route lives in the assessed namespace, and copying it into the detection store would be a second authority) together with the fact that the route stays a required validated field on the run and on every signal, so nothing became optional; the read's recorded order and its content-digest recheck that reports an altered payload as a damaged store; the comparison and currentness answers that write nothing and cannot hold a re-interpretation; and the manifest retention answer that reports an unresolved reference with what would resolve it. Verification metadata is the leaf's base commit `4264dcc9`: the code commit does not exist yet and closeout owns that stamp.
