# mcp/src/agents_remember/errors.py

| Field                  | Value                                 |
| ---------------------- | ------------------------------------- |
| repository             | agents-remember                    |
| path                   | `mcp/src/agents_remember/errors.py`   |
| doc_type               | `file-level-onboarding`               |
| lastUpdated | 2026-09-01T03:11+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview      | `../../overview.md`                   |

## Governing Overview

[agents_remember overview](../../overview.md)

## Purpose

Defines the shared typed error family for Agents Remember. It distinguishes route-index census
failures from authority failures while retaining the harness-control contract, adapter disconnect,
Codex protocol, and client-side first-byte ambiguity families. 260718-CHATS-L0 adds the
conversation-composition family: `ConversationCompositionError` marks a violated app-scoped
conversation runtime composition contract, kept distinct from `AuthorityError`, which remains the
type for identity/authorization refusals such as the conversation resolver's loopback ruling.
260731-EFA-L3 adds `TokenizerVocabularyError`: a build-integrity family for a packaged asset the
server needs before it can finish starting. ARSPAWN-L2 adds one coherent structural family:
`SeatOccupancyError` for duplicate canonical-seat claimants, `StructuralDispatchError` for
contradictory durable brief evidence, `StructuralDispatchLockError` for serializer
setup/acquisition failure, and `StructuralRoutingError` for absent or ambiguous structural routes.
MCAR-L02 adds `FutureCodeCandidateError` for typed capture and stale-input outcomes at the exact
future-code identity boundary.
The certification contract adds `CertificationContractError`, whose recursively frozen findings
preserve stable rail/plan/result failure codes, paths, details, owners, and evidence references
without allowing a caller to mutate the accepted diagnostic snapshot.

## Code Commentary

### Logic

`AgentsRememberError` remains the package base and a `ValueError`. `HarnessControlClientError`
extends `HarnessControlError` with `may_have_sent`: failures before the Unix socket accepts a byte
remain retryable, while failures after the first accepted byte must be reported as unknown and
reconciled under the same request id. `HarnessAdapterDisconnectedError` carries the equivalent
native-adapter ambiguity plus optional vendor correlation. Codex-specific subclasses preserve
app-server method/code evidence. `RouteIndexCensusError` identifies a validated-root census failure
without conflating it with `AuthorityError`, which remains the type for a root mismatch or missing
write authority. `FutureCodeCandidateError` carries the stable status of a leaf-only future-code
capture or currentness refusal without moving Git logic into the error module.
`ConversationCompositionError` identifies a conversation runtime composition bug —
retrieval before installation, a second install, a foreign object on the reserved state key, or
construction missing a required authority — that must fail at startup or request entry, never
silently at first use. cit:([`TokenizerVocabularyError`], mcp/src/agents_remember/errors.py:256-264) marks the one packaging failure the
token counter cannot paper over: the tiktoken vocabulary it needs is not the one vendored into
`package_data/tiktoken`. It is raised in place of letting tiktoken download the file it cannot
find, because the counter is constructed while the MCP tool surface is still importing — a
download there is a network round trip on the server's startup path, which is what made a cold
container, an offline machine, and a hermetic CI job unable to start at all.
The four structural errors remain direct `AgentsRememberError` members. Lower owners raise their
own type; public adapters translate only when their status vocabulary differs, and notifier
boundaries may contain the typed routing/occupancy failure to the affected row.
`CertificationContractError` converts each supplied JSON-like finding into mapping proxies and
tuples recursively. Unsupported mutable/object values and non-string mapping keys are rejected so
typed certification failure evidence cannot degrade into a generic mutable exception payload.

### Conventions

Classes name one failure category and inherit from the nearest family member. Ambiguity evidence is
an explicit constructor argument, not inferred later from exception text.

### Invariants And Boundaries

- `AgentsRememberError` must keep subclassing `ValueError` so existing
  `except ValueError` handlers and the FastMCP error surface keep working
  unchanged. Do not reparent it to `Exception` or `RuntimeError`.
- Every domain error in the package should subclass `AgentsRememberError` (or a
  member of the family) rather than raising bare `ValueError` / `RuntimeError`,
  so the public surface stays one coherent contract.
- Structural occupancy, evidence, serializer, and route failures remain distinct types; callers
  must not reconstruct those categories by parsing exception text.
- This module holds only error-type declarations and small evidence constructors. It imports no
  package internals and stays safe at the bottom of the dependency graph.
- `CodexAppServerError` identifies malformed, incompatible, or boundedness failures at the pinned
  Codex app-server protocol boundary; disconnect errors preserve possible-send state for reconcile.
- `may_have_sent=True` is never permission to retry; it is evidence that the same request id must be
  reconciled.
- Route-index root/official-settings refusal remains `AuthorityError`; Git record, command, or path
  classification failure after authority is established remains `RouteIndexCensusError` with the
  original cause attached.
- Future-code capture/currentness refusal remains `FutureCodeCandidateError`; callers consume its
  explicit status and never infer the condition from exception text.
- Conversation composition failures (missing/duplicate/foreign/missing-member runtime binding)
  remain `ConversationCompositionError`; identity and cross-principal refusals in the same route
  remain `AuthorityError` — the two families are never interchangeable.
- `TokenizerVocabularyError` must stay a raise, never a fallback. A missing vendored vocabulary is
  a build defect, and the only alternatives are downloading it (the startup network call this
  exists to remove) or silently degrading the counter, which would make the failure visible only
  on machines without egress. It is not an authority or protocol failure and shares no boundary
  with the harness-control family.
- `CertificationContractError.findings` is a deeply immutable snapshot. Registry, plan, and
  terminal-result admission must preserve its typed finding vocabulary rather than replacing it
  with a generic wrapper error.

### Todos

None known for the L4 error boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The blocking client uses the new stage evidence; the bridge/queue keep the native ambiguity type.

| Finding | Anchor | Source |
| --- | --- | --- |
| Certification contract failures recursively freeze JSON-like findings and reject mutable or unsupported payload shapes. | `CertificationContractError`; `_freeze_contract_value` | mcp/src/agents_remember/errors.py:22-49 |
| Structural occupancy, dispatch evidence, dispatch locking, and routing are distinct members of the shared domain family. | `SeatOccupancyError`; `StructuralDispatchError`; `StructuralDispatchLockError`; `StructuralRoutingError` | mcp/src/agents_remember/errors.py:52-65 |
| Future-code candidate capture and currentness refusals use one central typed member with an explicit status. | `FutureCodeCandidateError` | mcp/src/agents_remember/errors.py:126-131 |
| The socket exchange flips `may_have_sent` only after a successful first write and maps post-write response failures accordingly. | `_exchange_control` | mcp/src/agents_remember/serving/harness_control_client.py:541-577 |
| The ordered dispatcher converts native disconnect evidence into requeued or `unknown` receipts without blind resend: a disconnect certified pre-send requeues the head, a `may_have_sent` disconnect installs the ambiguity blocker instead. `HarnessControlQueue` no longer exists — it was deleted in 260731-EFA-L6 as a pure forwarding facade, so `HarnessSubmissionAuthority` is the sole owner rather than the thing behind a facade. | `_preflight_declined`; `_send_and_settle` | mcp/src/agents_remember/serving/harness_submission_authority.py:639-659; mcp/src/agents_remember/serving/harness_submission_authority.py:702-729 |
| The route-index census raises the dedicated type after root validation and preserves timeout/OS/path-classification causes: `_untracked_source_candidates` re-raises `lstat` failures, `_require_repository_root` raises `AuthorityError`, and `_run_git` converts `TimeoutExpired`/`OSError` with `from error`. | `_untracked_source_candidates`; `_require_repository_root`; `_run_git` | mcp/src/agents_remember/kernel/route_index_census.py:126-156; mcp/src/agents_remember/kernel/route_index_census.py:159-179; mcp/src/agents_remember/kernel/route_index_census.py:189-205 |
| The conversation runtime raises `ConversationCompositionError` for missing/duplicate/foreign/missing-member bindings; the resolver raises `AuthorityError` for identity refusals. | "class ConversationRuntime:"; "class LocalOperatorAuthorizationResolver:" | mcp/src/agents_remember/serving/conversation/runtime.py:58-104; mcp/src/agents_remember/serving/conversation/authorization.py:71-107 |
| `_verify_vendored_vocabulary` raises `TokenizerVocabularyError` for an unknown/absent vendored vocabulary and for a digest mismatch. `vendored_vocabulary_cache` calls that verifier before installing the scoped `TIKTOKEN_CACHE_DIR`, and `TiktokenTokenCounter` enters the cache on the import path. | "def _verify_vendored_vocabulary"; "def vendored_vocabulary_cache"; "class TiktokenTokenCounter" | mcp/src/agents_remember/models/tokens.py:70-70; mcp/src/agents_remember/models/tokens.py:110-110; mcp/src/agents_remember/models/tokens.py:184-184 |

## Cross-Repo References

No external repository boundary is implemented by the error declarations.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

The shared error family now distinguishes certified native busy/pre-dispatch failure, immutable
request-id conflict, and bridge-epoch mismatch. These types preserve the first-byte boundary: only a
certified pre-dispatch condition may advertise retry safety; possible-write failures remain unknown.

## 260718-CHATS-L5I Current Delta

`HarnessInteractionNotPendingError` gives direct interaction-response callers a typed refusal when no pending interaction is available. It prevents a normal stale or already-settled response from being reported as an undifferentiated control failure.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260727-CHATS-IM-L2 Native-History Error Delta

`NativeHistoryUnavailable` identifies one child/history read that can fail without invalidating
the shared adapter; its stable `code` carries the exact local reason. The
`NativeHistoryLimitExceeded` subtype adds `actual_bytes` and `limit_bytes` and fixes its code to
cit:([`NativeHistoryUnavailable`; `NativeHistoryLimitExceeded`; "materialization-limit"], mcp/src/agents_remember/errors.py:362-367; mcp/src/agents_remember/errors.py:370-382). These types distinguish child-local acquisition/resource
outcomes from malformed shared protocol and bridge-fatal transport failure.

## 260821-CLIVE-L2 Current Contract

The current source seams include `AgentsRememberError`, `AuthorityError`, `ConfiguredContractAuthorityError`. This supporting seam carries bounded error/command evidence used by the L2 owners. It does not become a second lifecycle authority, exception-family translator, or Git fallback path.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The module exposes the common base, authority, and configured-contract authority types at this ownership boundary. | `AgentsRememberError`; `AuthorityError`; `ConfiguredContractAuthorityError` | mcp/src/agents_remember/errors.py:18-19; mcp/src/agents_remember/errors.py:68-87 |

## MCAR-L02 Curator-Coherence Failure Family

`CuratorCoherenceError` carries the stable status, bounded detail, expected/observed facts, and
legal next action for authority, candidate, judgment, evidence, CAS, generation, and projection
failures. The application boundary translates this family once, so individual tools do not need to
repeat lower-level exception vocabularies. `FutureCodeCandidateError` remains the separate exact
future-code derivation family.

## MCAR-L03 Pair Error Family

`MemoryCandidatePairError` owns one bounded public refusal shape: status, exact field, contract
path, expected/observed facts, and repair action/arguments. `CuratorCoherencePairError` preserves
that evidence when the shared pair validator is consumed through coherence, avoiding repeated
lower-level failure-family implementations.

## Update History

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
  Documented cit:([`TokenizerVocabularyError`], mcp/src/agents_remember/errors.py:256-264) in Purpose and Logic as a build-integrity family
  — the vendored tiktoken vocabulary is absent or not the one shipped — raised instead of letting
  tiktoken download it on the server's import-time startup path, and added the invariant that it
  must stay a raise rather than become a download or a silent degrade. Repaired 2 citations into
  files this leaf changed. (1) The census row's whole-file `L1-L226` → `L126-L205`, which actually
  contains the three claimed raisers: `_untracked_source_candidates` re-raising `lstat` failures
  cit:([`_untracked_source_candidates`], mcp/src/agents_remember/kernel/route_index_census.py:126-156),
  `_require_repository_root` raising `AuthorityError`
  cit:([`_require_repository_root`], mcp/src/agents_remember/kernel/route_index_census.py:159-179), and `_run_git`
  converting `TimeoutExpired`/`OSError` `from error`
  cit:([`_run_git`], mcp/src/agents_remember/kernel/route_index_census.py:189-205); the file is now 229 lines, so the
  old range was both stale and unanchored. (2) The native-history delta's own-file
  cit:([`NativeHistoryUnavailable`; `NativeHistoryLimitExceeded`; "materialization-limit"], mcp/src/agents_remember/errors.py:362-367; mcp/src/agents_remember/errors.py:370-382):
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
