# mcp/src/agents_remember/errors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/errors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:14:14+00:00 |
| lastVerifiedCommitHash | `95e61fdc2c29191f051afafc33dc2d6910c66a9c` |
| lastVerifiedCommitDate | 2026-09-04T10:18:42+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[Governing route overview](../../overview.md)

## Purpose

Defines the common typed failure vocabulary used by certification, memory, lifecycle, authority, and harness boundaries. The base remains a ValueError, while subclasses preserve the distinctions callers need to refuse unsafe work, present bounded diagnostics, or determine whether a retry could duplicate an operation.

## Code Commentary

### Logic

`CertificationContractError` recursively freezes findings, including nested mappings and sequences. Profile admission, unavailable executor prerequisites, contradictory readiness, and invalid shared Dagger authority remain separate subclasses with stable statuses. `DaggerRuntimeAuthorityError` covers invalid declarations, connection-only inspection failures, authority conflicts and live-owner transition barriers before executor launch.

Task-intent failures carry an explicit next action. Seat occupancy, dispatch evidence, dispatch locking and structural routing retain separate error types. Configured-contract authority errors expose the failing authority cell; reread errors retain a closed reason and bounded expected/observed facts rather than leaking backend exception input.

`CuratorCoherenceError`, `MemoryCandidatePairError`, `CuratorCoherencePairError` and `FinalCertificationError` have distinct public response fields. Pair errors preserve the exact failing field and recovery arguments; the coherence adapter forwards the shared pair diagnosis. Final certification uses `certificationStatus`, while pair validation uses `pairStatus` and `pairField`.

Harness errors distinguish a request that sent no bytes, one that may have been sent, a busy adapter that proved zero bytes were sent, request-id conflicts, stale bridge epochs and non-pending interaction responses. Tokenizer and grammar failures remain explicit integrity failures; native-history unavailability does not automatically invalidate the harness adapter.

### Conventions

Raise the narrow typed family rather than a generic exception when a domain contract is known. Expected and observed dictionaries are copied at response boundaries; only certification findings are recursively frozen.

### Invariants And Boundaries

- Preserve certification refusal codes and ownership details; do not flatten them into successful or generic lifecycle output.
- A busy-adapter error means zero operation bytes were sent. Generic disconnects cannot establish that retry safety.
- Pair, coherence and final certification errors report missing authority; constructing an error does not validate or repair that authority.
- Grammar and tokenizer failures never silently replace the configured parser or vendored vocabulary.

### Todos

No additional source change is performed by this documentation pass.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The cited source establishes the current contracts and boundaries described above. Source verification is documentation evidence, not acceptance of the implementation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Certification findings and distinct pre-execution error statuses | `CertificationContractError`; `CertificationProfileError`; `CertificationExecutorPrerequisiteError`; `CloseoutReadinessContractError`; `DaggerRuntimeAuthorityError` | mcp/src/agents_remember/errors.py:22-81 |
| Bounded configured-contract authority and reread errors | `ConfiguredContractAuthorityError`; `ConfiguredContractRereadError` | mcp/src/agents_remember/errors.py:119-161 |
| Separate coherence, exact-pair and final-certification response shapes | `CuratorCoherenceError`; `MemoryCandidatePairError`; `CuratorCoherencePairError`; `FinalCertificationError` | mcp/src/agents_remember/errors.py:176-314 |
| Composition, integrity, harness retry safety and history failures | `ConversationCompositionError`; `TokenizerVocabularyError`; `GrammarUnavailableError`; `HarnessAdapterDisconnectedError`; `NativeHistoryLimitExceeded` | mcp/src/agents_remember/errors.py:321-457 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-05T06:14:14+00:00 — Reconciled the shared error family across cumulative CCR changes, including readiness and final-memory failures; retained the harness retry-safety and authority-boundary distinctions.

  Historical-reference repair: the five source references in the July 31 entry below are inert provenance, preserving the labels and coordinates recovered from memory commit `139cda0f751466a3ab859ad51897da959b8e3947` (recorded source verification `cfd0938103b1392e471144b6997c51a41591ad2b`). That later card had already changed the original July coordinates. The original entry remains in memory commit `bfdbc6dd6717cd842ecd6190471c34852f1f95ea`, with recorded source verification `abc7cbcc74921cdcb57a61529445f61641e919e7`. Neither historical stamp certifies the recovered coordinates against current code. Current error-family evidence is in Repo-Internal References above.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the new `DaggerRuntimeAuthorityError` subclass (status `dagger-runtime-authority-invalid`) that types every host-level shared Dagger authority refusal before any Dagger command starts.

- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: recorded the CCR-R08
  `FinalCertificationError` family (status/detail/expected/observed/next_action, bounded
  `response_fields` projection, direct `AgentsRememberError` member outside the frozen-findings
  certification-contract family) and re-anchored every errors.py citation the +33-line insertion
  shifted (tokenizer 284-292 to 317-325, native-history 390-410 to 423-443). Verification
  metadata pinned to the owning commit 16d1a4d6.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: re-anchored every
  shifted errors.py citation against the current source (structural family 80-93, future-code
  154-159, authority 96-115, tokenizer 284-292, native-history 390-410, freeze helpers
  22-31/56-67). Verification remains pinned to the pre-commit source history until closeout.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the two new profile-admission subclasses -- CertificationProfileError (certification-profile-invalid) and CertificationExecutorPrerequisiteError (certification-executor-prerequisite-failed) -- extending CertificationContractError.

- 2026-09-01T03:11+02:00 — Added the deeply immutable certification contract failure family and
  repaired every onboarding citation shifted by its insertion. Verification remains
  closeout-owned.

- 2026-08-29T21:46+02:00 — MCAR-L03: added the canonical exact-pair failure and coherence adapter
  with shared response projections. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Added the typed curator-coherence failure family with structured CAS
  diagnostics and recovery guidance. Verification remains closeout-owned.

- 2026-08-29T04:55+02:00 — MCAR-L02: added the central typed future-code candidate refusal,
  documented its explicit status boundary, and repaired shifted source citations. Verification
  metadata remains pinned until closeout stamps the real code commit.

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2: added and documented the typed structural
  occupancy, dispatch-evidence, dispatch-lock, and routing failure family; corrected the legacy
  evidence table shape. Verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-11T15:20+02:00 — Replaced multiply occurring error-class anchors with the two unique
  runtime/resolver declarations whose bodies implement the stated refusals.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: rebound the tokens row to the
  real definitions and corrected the native-history range to `150-170`; exact non-fixing check
  returns zero findings.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: corrected raiser ownership and failure modes:
  `_verify_vendored_vocabulary` raises for absence/unknown encoding and digest mismatch before the
  cache context changes the environment. The new range is explicit `:1-1` curator input.

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: repaired 3 table citations and 6 prose citations; left the stale tokenizer-cache ownership claim unresolved as Tier 3.

- 2026-08-02T01:42+02:00 — 260731-EFA-L6 debt this leaf created, now cleared: three L6 workers split six oversized `serving/` classes while this memory tree was being edited, and every line range in this document that pointed into them went out of bounds the instant the sources shrank (`citation_range_out_of_bounds`). Ranges were re-derived by READING the cited construct at its current location, never by scaling or subtracting a delta — the splits moved code between files rather than shifting it uniformly. Where a construct left the file the row names, the Source Path moved with the range into its own row rather than being silently re-pointed. Verification metadata pinned until closeout stamps the L6 code commit.

- 2026-07-31T20:56+02:00 — 260731-EFA-L3 curator: body updated for the typed error this leaf added.
  Documented historical source: ``[`TokenizerVocabularyError`], mcp/src/agents_remember/errors.py:284-292`` in Purpose and Logic as a build-integrity family
  — the vendored tiktoken vocabulary is absent or not the one shipped — raised instead of letting
  tiktoken download it on the server's import-time startup path, and added the invariant that it
  must stay a raise rather than become a download or a silent degrade. Repaired 2 citations into
  files this leaf changed. (1) The census row's whole-file `L1-L226` → `L126-L205`, which actually
  contains the three claimed raisers: `_untracked_source_candidates` re-raising `lstat` failures
  historical source: ``[`_untracked_source_candidates`], mcp/src/agents_remember/kernel/route_index_census.py:126-156``,
  `_require_repository_root` raising `AuthorityError`
  historical source: ``[`_require_repository_root`], mcp/src/agents_remember/kernel/route_index_census.py:159-179``, and `_run_git`
  converting `TimeoutExpired`/`OSError` `from error`
  historical source: ``[`_run_git`], mcp/src/agents_remember/kernel/route_index_census.py:189-205``; the file is now 229 lines, so the
  old range was both stale and unanchored. (2) The native-history delta's own-file
  historical source: ``[`NativeHistoryUnavailable`; `NativeHistoryLimitExceeded`; "materialization-limit"], mcp/src/agents_remember/errors.py:390-410``:
  inserting `TokenizerVocabularyError` above pushed `NativeHistoryUnavailable` to the current
  class range and `NativeHistoryLimitExceeded`, with its `code="materialization-limit"`,
  `actual_bytes` and `limit_bytes`, to the same exact source range. Added a `models/tokens.py` row for
  the verified vocabulary path. The `harness_control_client.py`, `harness_submission_authority.py` and
  `serving/conversation/runtime.py` ranges were left alone — this leaf touched none of those files.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation that moved when the command queue became a facade. `harness_control_queue.py` (227 lines) now only forwards to `HarnessSubmissionAuthority`, so the disconnect-evidence row was repointed to `harness_submission_authority.py` (`_send_and_settle` branching on `may_have_sent` L865-L892, `_certified_pre_send_busy` requeue L1051-L1061, `_possible_send_failure`/`_set_unknown_locked` L1082-L1117) and the claim reworded to say requeued-or-`unknown` rather than rejected-or-unknown.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: documented typed native-history
  unavailability and bounded-materialization byte evidence as child-local outcomes distinct from
  shared transport/protocol failure. Verification metadata remains pinned while uncommitted.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented `ConversationCompositionError` as
  the typed conversation runtime composition failure, distinct from the identity/authorization
  `AuthorityError` family. Verification metadata remains pinned until closeout stamps the
  candidate commit.

- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: documented `RouteIndexCensusError` as the typed
  post-authority census failure, distinct from root and official-settings `AuthorityError`.

- 2026-07-17T21:39+02:00 — FEUI-L5: documented typed busy certificate, id-conflict, and epoch-
  mismatch errors used by the reliable submit boundary.

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the client-side first-byte
  ambiguity type and its retry-safe versus reconcile-required evidence boundary.

- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the error-sidecar body for the negotiated protocol
  failure wording change.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: documented the typed Codex app-server
  protocol failure addition. Verification remains pinned until the leaf code commit exists.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator refresh: documented typed control-contract and
  ambiguous-disconnect errors used by the new bridge surfaces.

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
