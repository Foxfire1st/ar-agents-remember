# Selected Closeout Certification

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout/certification/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea` |
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Closeout integration overview](../overview.md)

## What This Area Is

The production bridge between closeout lifecycle ownership and repository-neutral certification. It freezes real admission, retains exact original evidence in the existing store, selects it through the operation journal and executes the permitted suffix. Door/task authority, immutable storage and the journal remain separate owners.

## Hot Path Summary

Read `observation.py` and `admission.py` for actual candidate admission, `selection.py` for full graph readback/CAS, and `execution.py` for gate starts and continuation handoff. `recovery.py` owns change classification and complete prior-red context; `retained_output.py` recognizes only physically proven code output from the selected generation.

## Operating Model

1. Lifecycle coordination classifies generation reuse or a new admission. New admission validates the configured profile, performs strict staged preparation and freezes actual owner input.
2. Initial selection publishes/reopens original authority, admission and recovery records. The existing store/coordinator atomically binds the initial state before claimed-door publication and worker launch.
3. Execution reopens explicit original references and current authority. Complete lower green gates may be reused; red catalogs require an explicit corrective successor. Interrupted uncertified terminal replacement retains its original history.
4. The admitted recovery decision selects the code suffix. Real returned terminals are selected through currentness checks and journal CAS, with complete publication generations protected from pruning.
5. Gate-5 reuse requires current canonical memory input. Finalization-only reuse checks memory again immediately before handoff. The default application bundle installs `PreparedCloseoutContinuation`; selected certificates and physical readback remain required.

## Local Invariants And Traps

- There is no latest-object search, missing-selection recovery by refreezing, or regenerated original provenance.
- Shape-valid wire records alone do not establish actual source, task, current-memory or publication authority.
- Selected results retain red evidence; a missing certificate is not proof of an interruption or success.
- Route-review movement, cancellation, owner/CAS loss or changed authority refuses before selection or handoff.
- Same-generation retained output normalizes only a fully proven code commit. Memory/ledger output cannot enter through that exception.
- Source review and fixture success do not constitute complete production closeout or certified delivery.

## File-Level Onboarding Map

| Source File | Onboarding | Role |
| --- | --- | --- |
| `__init__.py` | [__init__.py.md](__init__.py.md) | Documentation-only namespace |
| `observation.py` | [observation.py.md](observation.py.md) | Actual task/Git/mutation/generated authority inputs |
| `admission.py` | [admission.py.md](admission.py.md) | Strict preparation and original initial selection |
| `recovery.py` | [recovery.py.md](recovery.py.md) | Owner-derived input changes and prior-red admission |
| `selection.py` | [selection.py.md](selection.py.md) | Explicit graph readback and journal CAS |
| `execution.py` | [execution.py.md](execution.py.md) | Selected suffix and current-memory/finalization handoff |
| `retained_output.py` | [retained_output.py.md](retained_output.py.md) | Narrow physically proven code-output comparison |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Admission freezes actual preparation and current owner input; selection binds the exact originals. | `prepare_closeout_certification`; `initial_certification_state` | mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:86-172; mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:274-340 |
| Currentness rechecks the profile, owner semantics and route review. | `validate_selected_currentness` | mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:343-386 |
| Recovery derives actual input changes and requires complete prior-red correction. | `derive_certificate_input_changes`; `build_prior_red_context` | mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:123-152; mcp/src/agents_remember/worktrees/integration/closeout/certification/recovery.py:155-203 |
| Journal selection reopens the complete original graph before its live-owner CAS. | `require_selected_certification`; `select_certification_state` | mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:128-132; mcp/src/agents_remember/worktrees/integration/closeout/certification/selection.py:580-598 |
| Execution first refuses the prepared path on converted memory (MIK-R09, gap 3), then admits only the selected suffix and current memory/finalization boundary. | "def execute_selected_closeout(" | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:348-391 |
| Retained output permits only the selected physically proven code commit. | `require_retained_output_currentness` | mcp/src/agents_remember/worktrees/integration/closeout/certification/retained_output.py:28-77 |
| The ordinary service construction installs the prepared closeout continuation. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:211-224 |

## 260928-MIK-L09 The Prepared Closeout Fails Closed On Converted Memory

**Route impact (MIK-R09@v2, leaf 260928-MIK-L09, ruling 2026-09-30T14:38:47 gap 3).** This certified (prepared)
closeout binds its memory commit to the exact curator-attested candidate, so it cannot set `closed: true` in the leaf's
history file (MIK-R07 rule 7), which MIK-R09 rule 3 requires of a closeout memory commit. `execute_selected_closeout`
therefore first asks `worktrees/knowledge_gate.prepared_closeout_refusal(contract)`, before recovery, and on
converted memory refuses with `prepared-closeout-knowledge-history-unclosable`, naming why and that the leaf should
close out through the worktree closeout commit; `application/prepared_certification._realize_prepared_memory` carries
the same check. The path has no production caller today; unconverted memory is untouched. Tested by
`test_the_prepared_closeout_path_fails_closed_on_converted_memory`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The refusal before recovery. | "unclosable = prepared_closeout_refusal(contract)" | mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:359-361 |

## Docs And Cross-Repo References

The configured Domain Documentation registry has no entries. The adjacent closeout, lifecycle and quality owners supply the same-repository authority boundaries; this package defines no external protocol.


## Integrated IAS Recovery Contract

Execution first resumes an already claimed prepared publication, before attempting original-head admission. Otherwise `_refresh_selected_recovery` reobserves canonical memory inputs before choosing reusable certificates. Selection still binds the exact candidate, profile, plan and prior-red disposition. Retained code-output reuse separately proves both original prestates and the current physical commit; helper extraction does not weaken those comparisons.

## Update History

- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **route body updated for MIK-R09.** Added the section "260928-MIK-L09 The Prepared Closeout Fails Closed On Converted Memory" (ruling 14:38:47 gap 3): `execute_selected_closeout` refuses `prepared-closeout-knowledge-history-unclosable` on converted memory before recovery; one row. **Reopened claim reworded:** the execution row (it now names the new first refusal); its generated bullet is committed history (2026-09-09) and untouched. The fixer normalised the rows. No verification stamp was advanced. **Re-anchored:** claims bind by anchor text and a committed generated bullet names the old anchor, so the reworded execution row was re-anchored on line-exact quotes ("def execute_selected_closeout("); no committed history line was edited.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  admission/selection/service ranges the earlier entry re-derived were re-checked and hold; the
  retained-output row is corrected in the entry above. No other wording changed. Verification
  metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the retained-output row
  cited a range that begins at the module imports and ends inside the next function. Repointed
  `require_retained_output_currentness` to `:28-77`, its own extent. Noting that this staleness is
  pre-existing — it did not come from this master's change. Verification metadata remains
  closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the
  `mcp/src/agents_remember/worktrees/integration/closeout/certification/` route changed since the
  recorded verification commit. Re-read the card against the frozen on-disk source and re-checked
  its claims and cited ranges: nothing this card asserts is falsified by the change, so no wording
  changed. Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): route files moved since
  the recorded verification commit (the live door read, plus an earlier import shift). Re-derived
  the cited admission, selection and service-bundle ranges against the current source; no claim text
  changed. Verification metadata remains closeout-owned.
- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `validate_selected_currentness` repointed to mcp/src/agents_remember/worktrees/integration/closeout/certification/admission.py:343-386. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `execute_selected_closeout` repointed to mcp/src/agents_remember/worktrees/integration/closeout/certification/execution.py:344-384. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T02:35:47+02:00 — CCR-L38 inherited route reconciliation: re-read this route's purpose, member inventory, route summary, and invariants against frozen candidate code tree `4c6b7bc2362bc03d50fc7a0643f34b591b805d45`; the candidate's changed paths are outside source route `mcp/src/agents_remember/worktrees/integration/closeout/certification`, so no route/member/prose/invariant change is required. route-member-count=7; source inspection only; verification metadata remains unchanged pending producer-owned realization. No acceptance or certification claim.

- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.


- 2026-09-06T14:58:25+00:00 — Created the nearest route after full source review at `c69d5171187fa1957025e393270db9f5a864ab14`. Reused the parent route's separation of door/task, coherence and journal ownership while distinguishing implemented selected admission/execution from the unbound production continuation. Source verification is not gate or acceptance evidence.
