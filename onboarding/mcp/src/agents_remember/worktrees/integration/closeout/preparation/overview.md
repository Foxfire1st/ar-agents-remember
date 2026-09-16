# Closeout Preparation

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout/preparation` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-15T00:56:17+00:00 |
| lastVerifiedCommitHash | `806649b91bdce18f7b915bfbbf6727967f4e7a88`|
| lastVerifiedCommitDate | 2026-09-16T12:23:53+02:00|
| reviewedWorkingCandidate | `ar/260913-lca-l9` uncommitted source; base `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| governingOverview | `../overview.md` |

## Governing Overview

[Closeout overview](../overview.md)

## Hot Path Summary

Code intent selection precedes private execution. The journal retains exact code and memory-content outputs. The physical code view and current logical memory pair feed the selected memory-certification result; only that exact result permits private memory preparation. Existing output reuse proves the raw Git head/ref/tree and the certified content tree independently. Root `memory.md` is excluded only from the memory content view; cache state cannot request another output or publication.

## Ownership And Boundaries

`policy.py` observes actual configuration/hooks. `private_execution.py` owns command ordering through kernel capabilities, while `output_selection.py` retains exact raw outputs. `code_view.py` separates physical read roots from logical pair identity. `memory_execution.py` reopens certification results, and `memory_output.py` selects one memory-content output after the code output. `finalization.py` publishes the selected pair under guarded refs; `continuation.py` composes the installed memory producer and finalizer.

The memory-content message uses the kernel's shared `Code-Commit:` renderer. `memory_reuse.py` keeps the actual existing commit and its raw tree unchanged while binding the separately certified tree without root `memory.md`. Cache removal/ignore preparation occurs only alongside substantive memory work; a clean old commit that still contains the cache does not create a maintenance commit. This is source documentation, not an aggregate acceptance claim.

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
- [memory_output.py.md](memory_output.py.md) — Post-certification selection of the single memory-content output.

- [finalization.py.md](finalization.py.md) — original prepared output publication and canonical contract completion.
- [continuation.py.md](continuation.py.md) — default selected continuation and producer binding.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selected intent and command CAS remain outside the transport package. | `select_preparation_intent` | mcp/src/agents_remember/worktrees/integration/closeout/preparation_selection.py:135-158 |

Current working-candidate evidence for this route:

| Finding | Citations | Source Path |
| --- | --- | --- |
| The selected bundle contains code and one memory-content output. | L45-L48 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_output.py) |
| Existing memory reuse binds raw Git facts and a separately certified content tree. | L19-L63 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/memory_reuse.py) |
| Final publication proves and publishes the pair, then refreshes the cache. | L533-L569 | [mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py](mcp/src/agents_remember/worktrees/integration/closeout/preparation/finalization.py) |

## Integrated IAS Recovery Contract

Memory preparation reobserves the selected result, actual policy and original intent. A retained output is physically re-proven instead of recreated. Finalization journals each original publication prestate once and reobserves proven code and memory refs. `resume_prepared_closeout` requires the same running worker/generation and the original selected two-output bundle; no ledger leg or retained ledger bytes are required. Cache refresh follows the Git publication and reports availability without changing the transaction result.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.


## Update History

- 2026-09-15T00:56:17+00:00 — LCA ledger-retirement working-candidate curation: Replaced M/L and C/M/L proof/publication with exact code and memory-content outputs and cache-free certified reuse. Existing verified commit/date remain historical provenance until producer-owned closeout. Source inspection only; no aggregate acceptance claim.

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
