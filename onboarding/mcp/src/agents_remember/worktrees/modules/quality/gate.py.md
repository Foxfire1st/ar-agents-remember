# mcp/src/agents_remember/worktrees/modules/quality/gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/quality/gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Owns repository-profile admission and the lifecycle-facing quality gate boundary. It runs or recovers the exact candidate's Dagger generation, publishes the durable test report, and invokes the certification-record adapter around the run.

## Code Commentary

### Logic

`QualityGateTarget` binds checkout, enclosure, repository id and configured profile reference; `QualityGatePlan` carries targeted/full mode and an optional memory cap. A code commit requires one admitted profile. Missing profile authority refuses instead of providing the former wrapper-unavailable opt-out.

`run_strict_code_quality_gate` captures the staged tree, freezes certification admission before `run_clean_quality`, writes the completed test report, rejects failed or uncertified output, then rechecks both the evidence tree and current staged tree. The index is supplied by the caller: this module neither stages nor undoes staging. The recorded task diff base determines the measured change set.

`recover_strict_code_quality_gate` requires matching attestation, tree, profile, plan, selection, adapter and decoder, then validates the published generation and certifying evidence before recording it. Its public report remains the stable developer-facing transcript; the immutable published result path is separate.

The record helper reopens the published decoder artifact and delegates its gate catalog. A nonempty returned refusal list now raises before the caller returns quality success, including exact-generation recovery. The ordinary red-run branch still raises before that helper, so typed result publication for every terminal outcome is not established by this seam. An absent catalog also does not independently prove a complete certificate population.

### Conventions

Only the pinned Dagger path supplies acceptance evidence. A symbolic command in a preview is not execution evidence. Preserve the profile and shared runtime-authority digests in reports and recovered payloads.

### Invariants And Boundaries

- Freeze admission before Gate 1; never manufacture authority after execution from unbound inputs.
- Candidate, profile, selection, decoder and attestation must match during recovery.
- A green quality result and a complete certificate chain are separate facts at this boundary.
- Host diagnostic execution refuses; a failed gate leaves caller-owned staging intact.
- An explicit memory cap changes resource policy, not the test population or evidence requirements.

### Todos

Complete red/interrupted R21 record integration remains pending. The typed lifecycle, telemetry and Gate-5 executors are not wired by this helper.

## Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Required profile authority governs execution and preview. | `requires_strict_code_quality`; `code_quality_gate_preview` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:125-139; mcp/src/agents_remember/worktrees/modules/quality/gate.py:142-185 |
| Admission precedes Dagger and the exact staged tree is rechecked. | `run_strict_code_quality_gate` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:243-324 |
| Recovery requires the exact published generation and evidence. | `recover_strict_code_quality_gate`; `_strict_quality_success_payload` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:327-399; mcp/src/agents_remember/worktrees/modules/quality/gate.py:402-448 |
| Host diagnostics refuse and certificate-record refusals propagate. | `run_local_quality_diagnostic`; `_record_certification_generation` | mcp/src/agents_remember/worktrees/modules/quality/gate.py:451-461; mcp/src/agents_remember/worktrees/modules/quality/gate.py:478-507 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-05T22:19+00:00 — L30 source review at `6e4ab81f6ae52bce35003377bb3aec7877554ed7`: Propagated actual record refusals on fresh and recovered green generations; retained the explicit ordinary red-run publication gap.

- 2026-09-05T06:14:14+00:00 — Updated the accumulated profile gate to document admission freeze, successful-generation recording, and the remaining gap between quality success and certificate-chain completeness.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the runtime-authority cutover - `_QualityGateReport` and the success payload carry `runtimeAuthorityDigest`, preview returns it as None, the strict run reads it from the published schema-v3.1 manifest, and the test-results transcript renders it; re-anchored gate.py reference ranges to the current layout.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): rewrote the card for the repository-profile cutover. `QualityGateTarget` gained `repository_id`/`profile_reference`, the plan lost its executor field, `requires_strict_code_quality` now always admits one valid profile for code commits, the `wrapper-unavailable` state and `requires_integrated_acceptance` were removed, preview/success payloads carry profile digest/plan digest/selection/executor adapter id/result artifact, and recovery re-derives the expected plan digest and profile identity before reuse.

- 2026-08-25T08:16+02:00 -- 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T21:23+02:00 -- 260824-PDLS made lifecycle quality consume only verified Dagger evidence.

- 2026-08-24T14:19+02:00 -- 260821-DAGQC-L2: made recovery single-snapshot and strict-manifest-owned, retained stable `reportPath`, and added optional immutable `publishedResultPath` without disturbing the concurrent L4 diagnostic-wording contract.

- 2026-08-24T13:51:26+02:00 -- 260821-DAGQC-L4: recorded the narrowed Python quality refusal wording. Direct targeted Vitest remains a separate diagnostic-only route; the adapter still has no host executor or acceptance fallback.

- 2026-08-22T10:39+02:00 -- 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner.

- 2026-08-17T12:30+02:00 -- 260815-DAG-L5: added `recover_strict_code_quality_gate` and attestation-bound Dagger report recovery for crash-safe full-gate reuse.

- 2026-08-14T12:13:26+02:00 -- R43 curator: reconciled self-owned-wrapper refusal wording and the new direct non-Dagger builder proof.

- 2026-08-14T11:24+02:00 -- R39 curator: replaced the obsolete checkout-only/name-forbidden applicability claim with the two-layer policy: consumer adapter opt-in plus mandatory Agents Remember self-wrapper presence. (The self-policy layer was subsequently removed by CCR-R22 at this commit.)

- 2026-08-14T09:37+02:00 -- Reopened L23 cadence: clarified this runner's two accepting owners -- targeted leaf closeout and full master integration -- and the leaf-integration no-rerun boundary.

- 2026-08-13T14:32+02:00 -- L23 final curator pass: re-read the reopened CONTRIBUTING claim and recorded that this host runner remains diagnostic/generic plumbing while Agents Remember acceptance is Dagger-only with explicit diff-base and no fallback.

- 2026-08-13T08:40+02:00 -- L23 integration-gate repair: documented the extracted strict plan validator and preserved the fail-closed no-fallback executor boundary.

- 2026-08-12T20:10+02:00 -- L23 curator: documented durable-report versus short-scratch ownership.

- 2026-08-12T15:19+02:00 -- L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges.

- 2026-08-12T07:10+02:00 -- 260731-EFA-L24 curator: recorded the host-managed full-gate default, explicit-cap-only wrapping, host swap, unchanged pytest `-n=auto`, and the `memoryPolicy` preview/result/report evidence.

- 2026-08-12T01:38+02:00 -- 260731-EFA-L22 citation maintenance: moved runner-policy proofs to `test_worktree_quality_gate_runner.py` and refreshed retained closeout ranges.

- 2026-08-11T22:28+02:00 -- 260731-EFA-L19 final curator pass: recorded deterministic UTF-8 replacement for captured quality output and non-Windows `/tmp` normalization for ephemeral quality scratch.

- 2026-08-11T17:50+02:00 -- 260731-EFA-L19 curator: recorded the enclosure-owned, atomically replaced `reports/test-results.md` contract, full pass/fail transcript retention, stable `reportPath`, explicit checkout+enclosure target, and interrupted-run preservation.

- 2026-08-08T17:18+02:00 -- 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired.

- 2026-08-08T02:00+02:00 -- 260731-EFA-L17 curator: recorded the altitude-routed plan (`QualityGatePlan` mode `targeted`/`full`, mandatory cap for full runs, `memoryCap` payload, cap-kill naming, invocation labels) and refreshed reference rows to post-L17 ranges.

- 2026-08-04T15:32:44+02:00 -- 260731-EFA-L6 S18-B08 curator: split wrapper applicability from preview reporting and regenerated both operative code-quality function extents.

- 2026-08-02T16:45:41+02:00 -- 260731-EFA-L6 curator W1-B10: repaired 20 manifest citation findings plus the residual cross-repo row; scoped recheck clean.

- 2026-08-01T09:44+02:00 -- 260731-EFA-L4 curator: recorded the staging-step reason wording and the index-as-scope docstring contract; repaired citations.

- 2026-07-31T21:20+02:00 -- 260731-EFA-L3 curator (second pass): recorded the `quality_environment` dependency on `git_environment()` and the no-selector handover.

- 2026-07-31T20:48+02:00 -- 260731-EFA-L3 curator: documented `diff_base` across deciders/payloads, the one git runner, and re-anchored citations.

- 2026-07-31T16:40+02:00 -- 260731-EFA-L2: corrected citation ranges after the whole-tree `ruff format` pass.

- 2026-07-31T16:10+02:00 -- 260731-EFA-L2 attestation: file touched only by the whole-tree `ruff format` pass (commit `00e8379`); sidecar re-read and deliberately not rewritten.

- 2026-07-31T04:28+02:00 -- 260731-EFA-L1 removed the repository-name hard-code (L1-R10); added the three status constants and the path-not-name boundary.

- 2026-07-24T14:31Z -- 260718-CHATS-L5I incremental curator: created the sidecar for mandatory pre-code-commit quality enforcement, linked-worktree interpreter selection, current-worktree import precedence, and fail-closed bounded error reporting.
