# Closeout Preparation

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout/preparation` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T21:58:28+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Closeout overview](../overview.md)

## Hot Path Summary

Code intent selection precedes private execution. Exact raw outputs remain selected in the original operation journal. The physical code view and current logical memory pair feed the registered memory-certification producer. Only its exact selected Gate-5 result permits private M/L preparation. Existing outputs require actual Git and ledger proof; preparation alone does not advance logical refs or consume approval.

## Ownership And Boundaries

`policy.py` observes actual configuration/hooks. `private_execution.py` owns command ordering through kernel capabilities, while `output_selection.py` retains exact raw outputs. `code_view.py` separates physical read roots from logical pair identity. `memory_execution.py` reopens certification results and `memory_output.py` prepares ordered M/L outputs. `finalization.py` separately owns guarded ref publication and contract completion; `continuation.py` composes the installed memory producer with that finalizer. Current documentation records implementation, not a passing suite or aggregate acceptance.

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
| Selected intent and command CAS remain outside the transport package. | `select_preparation_intent` | mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py:57-80 |


## Integrated IAS Recovery Contract

M/L preparation reobserves the selected memory result, actual policy and original intent. A retained output is physically re-proven instead of created again. Finalization journals each original publication prestate once, reobserves proven refs, and recognizes that ledger publication advances the shared memory ref beyond intermediate M. `resume_prepared_closeout` requires the same running worker/generation, selected C/M/L outputs and retained ledger bytes before finishing publication; finalized-contract readback returns the original closed result.

## Update History

- 2026-09-06T21:58:28+00:00 — Reconciled this route against the source delta from `245057ab16e19afdaabd5c188c9576b22e0c0870` to `d36109038b3f2b500c138f9dc1ea9c9f9a247489`. Updated current ownership and policy claims; prior verification commit/date and history remain unchanged. Source inspection only; no test, review or acceptance claim.


### 2026-09-06T17:13:06+00:00 — Initial preparation route

Recorded current source ownership with verification metadata unset and no execution or acceptance claim.
