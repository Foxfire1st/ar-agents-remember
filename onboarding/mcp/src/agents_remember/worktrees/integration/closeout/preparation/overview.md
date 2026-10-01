# Closeout Preparation

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout/preparation` |

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

## Evidence

### Repo-Internal References

- Selected intent and command CAS remain outside the transport package. [1]

Current working-candidate evidence for this route:

- The selected bundle contains code and one memory-content output. [2]
- Existing memory reuse binds raw Git facts and a separately certified content tree. [3]
- Final publication proves and publishes the pair, then refreshes the cache. [4]

## Integrated IAS Recovery Contract

Memory preparation reobserves the selected result, actual policy and original intent. A retained output is physically re-proven instead of recreated. Finalization journals each original publication prestate once and reobserves proven code and memory refs. `resume_prepared_closeout` requires the same running worker/generation and the original selected two-output bundle; no ledger leg or retained ledger bytes are required. Cache refresh follows the Git publication and reports availability without changing the transaction result.

## CCR-L42 Refresh Validation Parity

The parity candidate composes the sidecar and governing route body/history checks in `worktrees/modules/onboarding.py::validate_memory_refresh_attestations`; curator memory preparation and closeout call that shared validator independently for both surfaces. This route's existing ownership and source behavior remain unchanged by the validation wiring.
