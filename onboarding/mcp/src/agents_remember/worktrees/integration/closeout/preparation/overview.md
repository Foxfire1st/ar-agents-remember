# Closeout Preparation

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout/preparation` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-13T23:52+02:00 |
| lastVerifiedCommitHash | `52875e7a8695fc7b67bff21ebb07a67268213967`|
| lastVerifiedCommitDate | 2026-09-14T00:06:58+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Closeout overview](../overview.md)

## Hot Path Summary

Code intent selection precedes private execution. Exact raw outputs remain selected in the original operation journal. The physical code view and current logical memory pair feed the registered memory-certification producer. Only its exact selected Gate-5 result permits private M/L preparation. Existing outputs require actual Git and ledger proof; preparation alone does not advance logical refs or consume approval.

## Ownership And Boundaries

`policy.py` observes actual configuration/hooks. `private_execution.py` owns command ordering through kernel capabilities, while `output_selection.py` retains exact raw outputs. `code_view.py` separates physical read roots from logical pair identity. `memory_execution.py` reopens certification results and `memory_output.py` prepares ordered M/L outputs. `finalization.py` separately owns guarded ref publication and contract completion; `continuation.py` composes the installed memory producer with that finalizer. Current documentation records implementation, not a passing suite or aggregate acceptance.

Since 260913-LCA-L4 this route owns one of the five memory-content producers, and it is the one with no
reachable public entry point. `memory_output.py` renders the **memory-content** leg's `normalizedMessage`
through `kernel.memory_attribution.render_memory_content_message` against
`result.candidate.codeView.codeCommit` — the kernel's one writer of the `Code-Commit:` trailer — while the
**ledger** leg keeps the plain `effective.message_for("ledger")` and carries none. The rendered message is
what `private_execution.py` creates the private commit with, and `finalization.py` publishes that exact
object to the live memory ref, so the attribution is inside the object the ref receives and cannot be
appended afterwards without rewriting it. Because `certification/execution.execute_selected_closeout` has
no production caller today, this leg's protection is the source census in
`mcp/tests/test_memory_attribution_producers.py` rather than a behavioural case of its own — a residual gap
that is stated on the kernel card rather than hidden.

## File-Level Onboarding Map

- [__init__.py.md](__init__.py.md) — Private preparation package marker.
- [selected.py.md](selected.py.md) — Immutable selected preparation transport.
- [policy.py.md](policy.py.md) — Actual Git configuration, identity environment and hook policy observation.
- [private_execution.py.md](private_execution.py.md) — At-most-once journal-bound private Git execution.
- [output_selection.py.md](output_selection.py.md) — Exact raw output publication into the existing object store and journal.
- [code_output.py.md](code_output.py.md) — Selected code preparation intent and original prefix binding.
- [code_execution.py.md](code_execution.py.md) — Private code creation or genuine existing-code observation.
- [code_view.py.md](code_view.py.md) — Physical code execution view for selected preparation.
- [memory_port.py.md](memory_port.py.md) — Typed prepared-memory certification request, result and port.
- [memory_execution.py.md](memory_execution.py.md) — Prepared memory candidate observation and selected result currentness.
- [memory_reuse.py.md](memory_reuse.py.md) — Read-only proof of genuine existing memory output.
- [memory_output.py.md](memory_output.py.md) — Ordered post-certification private M and L preparation.

- [finalization.py.md](finalization.py.md) — original prepared output publication and canonical contract completion.
- [continuation.py.md](continuation.py.md) — default selected continuation and producer binding.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selected intent and command CAS remain outside the transport package. | `select_preparation_intent` | mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py:135-158 |


## Integrated IAS Recovery Contract

M/L preparation reobserves the selected memory result, actual policy and original intent. A retained output is physically re-proven instead of created again. Finalization journals each original publication prestate once, reobserves proven refs, and recognizes that ledger publication advances the shared memory ref beyond intermediate M. `resume_prepared_closeout` requires the same running worker/generation, selected C/M/L outputs and retained ledger bytes before finishing publication; finalized-contract readback returns the original closed result.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## Update History
- 2026-09-13T23:52+02:00 — 260913-LCA-L4 (uncommitted change set on `ar/260913-lca-l4-ar`, base
  `5bb124d4`): route impact. `memory_output.py` became one of the five memory-content producers when
  `_intent` began rendering the memory-content leg through
  `kernel.memory_attribution.render_memory_content_message` against the candidate's certified code commit
  (the ledger leg stays plain), which is also the producer the master's 2026-09-13T22:05 census missed and
  the 2026-09-13T23:50 decision added. Recorded on `Ownership And Boundaries`: the memory-content leg is
  attributed and the ledger leg is not, the message is hashed into the private commit that finalization
  publishes to the live memory ref, and this leg's only protection is the source census because
  `execute_selected_closeout` has no production caller. Verification metadata remains closeout-owned; no
  acceptance claim and no verification stamp advanced.
- 2026-09-10T04:35+02:00 — CCR-L42 final citation curation: re-anchored `select_preparation_intent`
  to its current selection and state-persistence range; route ownership and verification metadata
  remain unchanged.
- 2026-09-10T02:27:58+02:00 — CCR-L42 parity curation: No route impact: curator preparation and closeout now run the shared sidecar and route body/history validators independently; this route's ownership and source semantics remain unchanged. No acceptance claim is made.

- 2026-09-09T02:35:47+02:00 — CCR-L38 inherited route reconciliation: re-read this route's purpose, member inventory, route summary, and invariants against frozen candidate code tree `4c6b7bc2362bc03d50fc7a0643f34b591b805d45`; the candidate's changed paths are outside source route `mcp/src/agents_remember/worktrees/integration/closeout/preparation`, so no route/member/prose/invariant change is required. route-member-count=14; source inspection only; verification metadata remains unchanged pending producer-owned realization. No acceptance or certification claim.

- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.


### 2026-09-06T17:13:06+00:00 — Initial preparation route

Recorded current source ownership with verification metadata unset and no execution or acceptance claim.
