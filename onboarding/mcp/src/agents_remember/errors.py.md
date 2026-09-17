# mcp/src/agents_remember/errors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/errors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T09:38+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[Governing route overview](../../overview.md)

## Purpose

Defines the common typed failure vocabulary used by certification, memory, lifecycle, authority, and harness boundaries. The base remains a ValueError, while subclasses preserve the distinctions callers need to refuse unsafe work, present bounded diagnostics, or determine whether a retry could duplicate an operation.

## Code Commentary

### Logic

`LockCapabilityError` names a failed resource-filesystem exclusion capability. The shared kernel lock raises it without assigning a coordinator role or registry policy. Control-plane callers translate it to `UnsafeLockFilesystemError`; the Dagger registry translates it to `DaggerRuntimeAuthorityError` with finding `runtime-authority-registry-lock-unsafe`.

`CertificationContractError` recursively freezes findings, including nested mappings and sequences. Profile admission, unavailable executor prerequisites, contradictory readiness, and invalid shared Dagger authority remain separate subclasses with stable statuses. `DaggerRuntimeAuthorityError` covers invalid declarations, connection-only inspection failures, authority conflicts and live-owner transition barriers before executor launch.

Task-intent failures carry an explicit next action. Seat occupancy, dispatch evidence, dispatch locking and structural routing retain separate error types. Configured-contract authority errors expose the failing authority cell; reread errors retain a closed reason and bounded expected/observed facts rather than leaking backend exception input.

`CuratorCoherenceError`, `MemoryCandidatePairError`, `CuratorCoherencePairError` and `FinalCertificationError` have distinct public response fields. Pair errors preserve the exact failing field and recovery arguments; the coherence adapter forwards the shared pair diagnosis. Final certification uses `certificationStatus`, while pair validation uses `pairStatus` and `pairField`.

Harness errors distinguish a request that sent no bytes, one that may have been sent, a busy adapter that proved zero bytes were sent, request-id conflicts, stale bridge epochs and non-pending interaction responses. Tokenizer and grammar failures remain explicit integrity failures; native-history unavailability does not automatically invalidate the harness adapter.

The role-capsule compiler adds a fourth family at the end of the module. cit:([`CapsuleCompilationError`], mcp/src/agents_remember/errors.py:464-506) is the typed refusal a capsule compilation raises, and its shape is what makes a refusal *explainable* rather than merely fatal: `status` is a stable, branchable code (the thirteen in `agents_remember.models.role_capsules.statuses`, plus the application tier's source-admission codes), `detail` names the exact defect for an operator who does not know the internals, `next_action` names **the owner that has to change something**, and `conflicts` carries the structured contradiction rows when the refusal is a stopped conflict. `conflicts` is frozen through `MappingProxyType` per row, so a caller cannot mutate a refusal's evidence after the fact. Two projections are provided: cit:([`render`], mcp/src/agents_remember/errors.py:490-496) is the one-line operator-facing text (`"<status>: <detail> (remedy: <next_action>)"`, with the remedy omitted when empty), and cit:([`response_fields`], mcp/src/agents_remember/errors.py:497-506) is the bounded fact set that adds `nextAction` and `conflicts` only when present, so a lower-layer diagnostic never leaks into a response.

Two subclasses narrow the family by defect source and are declarative today: cit:([`CapsuleManifestError`], mcp/src/agents_remember/errors.py:508-511) for an invalid canonical manifest or declared source path, and cit:([`CapsuleSourceError`], mcp/src/agents_remember/errors.py:512-513) for an absent, unreadable, unconfined, or non-UTF-8 instruction source. Neither overrides the base behavior; they exist so a caller can distinguish *which side of the boundary* refused without parsing the status string. **A third subclass, `CapsuleBindingError`, was removed on the A3 candidate** — the binding-defect class no longer has a distinct type, so do not cite one.

The **task-context projection** appends a separate family at the very end of the module rather than a fourth `Capsule*` member. cit:([`TaskProjectionSourceError`], mcp/src/agents_remember/errors.py:516-560) is raised when an admitted task/worktree binding cannot be projected into task context, and it deliberately subclasses `AgentsRememberError` **directly**, not `CapsuleCompilationError`: a projection that could not read its task has failed *before* any capsule compilation, and filing that under the capsule family would tell a caller the compiler refused when it was never reached. It keeps the same explainable-refusal shape — `status` a stable branchable code, `detail` the exact defect for an operator who does not know the internals, `next_action` the **owner that has to change something** — and adds one field of its own: `owner_status` carries the status the existing AR owner raised when this refusal wraps one, **so a caller can still branch on the owner's own vocabulary instead of matching prose**.

Its status vocabulary is **not** registered in `agents_remember.models.role_capsules.statuses`; the sixteen codes are raised at their own sites under `application/task_projection/`: `projection-binding-mismatch`, `projection-binding-unresolved`, `projection-branch-mismatch`, `projection-contract-unavailable`, `projection-memory-binding-unavailable`, `projection-operation-unsupported`, `projection-repository-mismatch`, `projection-requirement-declaration-unresolved`, `projection-requirement-packet-invalid`, `projection-requirement-packet-missing`, `projection-requirement-packet-unresolved`, `projection-role-altitude-mismatch`, `projection-scope-ambiguous`, `projection-task-binding-mismatch`, `projection-task-reference-invalid`, `projection-task-unknown`. Because they are absent from `CAPSULE_STATUSES`, do not assert membership there: the projection codes and the capsule codes are two vocabularies with two owners.

The family's defining invariant is that **a projection is either complete or refused** — there is no partial projection and no fallback to another branch, another task or a broader scope. It never repairs what it could not resolve, so the current task document is untouched by any of these refusals.

**The class is not interchangeable with `CapsuleCompilationError`.** `TaskProjectionSourceError` has no `conflicts` field and its `response_fields()` publishes `status`/`detail` plus `nextAction`/`ownerStatus`; the capsule family publishes `nextAction`/`conflicts`. A caller that branches on one family's response keys must not assume the other's.

### Conventions

Raise the narrow typed family rather than a generic exception when a domain contract is known. Expected and observed dictionaries are copied at response boundaries; only certification findings are recursively frozen.

### Invariants And Boundaries

- Lock capability failure must stay explicit through each caller's domain error; a shared primitive does not grant caller authority.
- Preserve certification refusal codes and ownership details; do not flatten them into successful or generic lifecycle output.
- A busy-adapter error means zero operation bytes were sent. Generic disconnects cannot establish that retry safety.
- Pair, coherence and final certification errors report missing authority; constructing an error does not validate or repair that authority.
- Grammar and tokenizer failures never silently replace the configured parser or vendored vocabulary.
- A capsule refusal is a **value with a remedy**, not a bare abort: `status` is a stable branching contract, `detail` is operator-facing prose, and `next_action` names the owner that has to change something.
- `conflicts` rows are frozen at construction. A caller may read a refusal's structured contradiction evidence but must not mutate it.
- `response_fields()` is the **bounded** projection: it adds `nextAction` and `conflicts` only when they exist, and it must never be widened to carry lower-layer diagnostics.
- The three `Capsule*` subclasses are boundary markers, not behavior. Adding a distinct meaning to one of them is a contract change for every caller that branches on the exception type.
- A compilation failure never becomes a partially valid capsule, so this family is raised **instead of** returning content — it is never a warning channel.
- A task-context projection is **either complete or refused**. There is no partial projection, no fallback branch, no nearest task match and no silent scope widening; a projection never repairs what it could not resolve.
- `TaskProjectionSourceError` keeps the wrapped owner's own status in `owner_status`. Do not collapse it into the projection's vocabulary — the whole point is that a caller can branch on the owner's code rather than on prose.
- `TaskProjectionSourceError` subclasses `AgentsRememberError` directly and **not** `CapsuleCompilationError`: a projection failure happens before any capsule compilation, so `except CapsuleCompilationError` must not be read as covering it.
- The sixteen `projection-*` codes are not members of `CAPSULE_STATUSES`. Do not assert membership there or register them in `models/role_capsules/statuses.py`.

### Todos

No additional source change is performed by this documentation pass.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

The error families preserve distinct authority, recovery and transport meanings. The shared lock capability has two domain-specific callers.

| Finding | Anchor | Source |
| --- | --- | --- |
| Policy-free lock capability failure. | `LockCapabilityError` | mcp/src/agents_remember/errors.py:22-23 |
| Immutable certification findings and pre-execution statuses. | `CertificationContractError`; `CertificationProfileError`; `CertificationExecutorPrerequisiteError`; `CloseoutReadinessContractError`; `DaggerRuntimeAuthorityError` | mcp/src/agents_remember/errors.py:26-37; mcp/src/agents_remember/errors.py:38-43; mcp/src/agents_remember/errors.py:44-49; mcp/src/agents_remember/errors.py:50-55; mcp/src/agents_remember/errors.py:56-69 |
| Bounded configured-contract authority and reread errors. | `ConfiguredContractAuthorityError`; `ConfiguredContractRereadError` | mcp/src/agents_remember/errors.py:123-133; mcp/src/agents_remember/errors.py:143-165 |
| Separate coherence, exact-pair and final-certification response shapes. | `CuratorCoherenceError`; `MemoryCandidatePairError`; `CuratorCoherencePairError`; `FinalCertificationError` | mcp/src/agents_remember/errors.py:180-211; mcp/src/agents_remember/errors.py:226-262; mcp/src/agents_remember/errors.py:265-285; mcp/src/agents_remember/errors.py:288-318 |
| Composition, integrity, harness retry safety and history failures. | `ConversationCompositionError`; `TokenizerVocabularyError`; `GrammarUnavailableError`; `HarnessAdapterDisconnectedError`; `NativeHistoryLimitExceeded` | mcp/src/agents_remember/errors.py:325-334; mcp/src/agents_remember/errors.py:335-345; mcp/src/agents_remember/errors.py:346-356; mcp/src/agents_remember/errors.py:373-387; mcp/src/agents_remember/errors.py:449-463 |
| Control-plane translation preserves the durable-store error family. | `exclusive_access` | mcp/src/agents_remember/controlplane/durable_store.py:319-360 |
| Host registry translation preserves typed pre-launch authority refusal. | `AuthorityRegistry` | mcp/src/agents_remember/worktrees/modules/quality/dagger_authority.py:588-846 |
| Role-capsule compilation refusal with its stable status, remedy and frozen conflict rows. | `CapsuleCompilationError`; `render`; `response_fields` | mcp/src/agents_remember/errors.py:464-506 |
| The two capsule subclasses that mark which boundary refused. `CapsuleBindingError` was removed on the A3 candidate and must not be cited. | `CapsuleManifestError`; `CapsuleSourceError` | mcp/src/agents_remember/errors.py:508-511; mcp/src/agents_remember/errors.py:512-513 |
| The consumer that turns this family into a value with an explanation instead of an escaping exception. | `compile_admitted_capsule`; `CapsuleCompilationOutcome` | mcp/src/agents_remember/application/role_capsules/compilation.py:89-122; mcp/src/agents_remember/application/role_capsules/compilation.py:44-80 |
| The registered refusal-code vocabulary these errors carry. | `CAPSULE_STATUSES` | mcp/src/agents_remember/models/role_capsules/statuses.py:27-41 |
| The failure cases that assert a refusal advertises its own reason and remedy. | `test_a_refusal_still_produces_an_explanation_manifest` | mcp/tests/test_role_capsule_compiler.py:851-867 |
| The task-context projection refusal: complete-or-refused, with the wrapped owner's status preserved. It subclasses `AgentsRememberError` directly, so it is **not** in the `Capsule*` family and is not covered by `except CapsuleCompilationError`. | `TaskProjectionSourceError`; `render`; `response_fields` | mcp/src/agents_remember/errors.py:516-560; mcp/src/agents_remember/errors.py:545-550; mcp/src/agents_remember/errors.py:552-560 |
| The producer that raises this family for every unresolved or contradictory binding input. | `resolve_task_projection_scope`; `read_packet` | mcp/src/agents_remember/application/task_projection/scope.py:292-373; mcp/src/agents_remember/application/task_projection/packets.py:83-130 |
| The refusal that proves `None` is never a substitute for an unprojectable admitted task. | `TaskProjectionSource` | mcp/src/agents_remember/application/task_projection/provider.py:56-103 |
| The case that pins the failure taxonomy: each unresolvable input returns its own status. | `test_every_unresolvable_input_returns_its_own_source_resolution_status` | mcp/tests/test_task_projection.py:834-997 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_every_unresolvable_input_returns_its_own_source_resolution_status` repointed to mcp/tests/test_task_projection.py:834-997. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: body updated for the second family this route's leaf appended, `TaskProjectionSourceError` (`CAPS-R03@v1`, `+47/−0`). Recorded it as a family that subclasses `AgentsRememberError` **directly rather than `CapsuleCompilationError`** — a projection failure happens before any compilation, so `except CapsuleCompilationError` must not be read as covering it — with the `status`/`detail`/`next_action` shape it shares with L2's family plus its own `owner_status` field, and the explicit note that its sixteen `projection-*` codes are **not** in `CAPSULE_STATUSES`. Added four invariants and four Repo-Internal rows. **Line numbers of every pre-existing class were re-verified against the current source and are unchanged**: the append is purely additive at the end of the file, so no earlier citation in this card or in any other card citing `errors.py` needed repair. Note one deliberate non-repair: the two L2 entries immediately below cite `CapsuleCompilationError` at `464-506` and `render`/`response_fields` at `490-496`/`497-506`, while the current source has `464-505`, `490-495` and `497-505` — each end bound one line long. Those citations belong to the L2 leaf and this L3 append did not move them (the append starts at 516, below both), so they are left exactly as L2 wrote them rather than silently rewritten from a different leaf's pass. Verification metadata is left at its previous stamp because the source is uncommitted — the governed closeout stamps the real code commit, and no hash was invented here.

- 2026-09-16T09:38+02:00 — 260915-CAPS-L2 curator: corrected against the A3 candidate (review follow-up, not a source change). `CapsuleBindingError` **no longer exists** — the family is now `CapsuleCompilationError` plus only `CapsuleManifestError` and `CapsuleSourceError`, and the file shrank 517 → 513 lines, so the previous entry's "purely additive, no earlier citation needed repair" no longer holds. Replaced the three-subclass sentence with the two that exist, stated the removal explicitly so no later reader re-cites it, widened `CapsuleSourceError`'s description to include the new non-UTF-8 case, and corrected both ranges (`508-511`, `512-513`). **The removal also falsified the created entry's claim that every pre-existing class range was unchanged.** Because the family shrank, the tail classes moved (513 total now vs 517), and this card's own citation table carried ranges that were **already stale before this leaf** and are now further off: the certification row was hand-repaired from stale pre-leaf values to the current `26-37`/`38-43`/`44-49`/`50-55`/`56-69`, and the harness/history row to `325-334`/`335-345`/`346-356`/`373-387`/`449-463`. The explanation-only rows for `CuratorCoherenceError`, `ConfiguredContractAuthorityError`/`RereadError` and the pair/final-certification family are text-only and are deliberately re-pointed in a later pass, not here; the `TokenizerVocabularyError` and `NativeHistoryUnavailable` ranges visible in the July 31 history entry below are **inert historical provenance** the entry itself declares as such and are not current citations. Verification metadata stays at its previous stamp — the source is uncommitted and no hash was invented here.

- 2026-09-16T09:38+02:00 — 260915-CAPS-L2 curator: body updated for the typed role-capsule refusal family this leaf appended (`CAPS-R02@v1`). Added the Logic paragraph for `CapsuleCompilationError` (stable `status`, operator-facing `detail`, the `next_action` owner remedy, `MappingProxyType`-frozen `conflicts`) with its two projections `render()` and the bounded `response_fields()`, plus the three boundary-marker subclasses `CapsuleManifestError`, `CapsuleSourceError` and `CapsuleBindingError`; added five invariants covering remedy-carrying refusals, frozen conflict rows, the bounded projection, the subclasses as contract, and the never-a-partial-capsule rule; added five Repo-Internal rows for the new family and its consumer. **Line numbers of every pre-existing class were re-checked and are unchanged**: the append is purely additive at the end of the file (449-461 still holds `NativeHistoryLimitExceeded`), so no earlier citation in this card or in the 19 other cards citing this file needed repair. Verification metadata is left at its previous stamp because the source is uncommitted — the governed closeout stamps the real code commit, and no hash was invented here.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:28+02:00 — Documented LockCapabilityError and the distinct durable-store/host-registry translations; reopened all current error-family references against the prepared L30 commit.


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
