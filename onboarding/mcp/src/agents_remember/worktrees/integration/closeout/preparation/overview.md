# Closeout Preparation

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration/closeout/preparation` |

## Governing Overview

[Closeout overview](../overview.md)

## Purpose

This package prepares and proves the exact code and memory-content outputs selected for an external-memory closeout, then publishes that pair through guarded Git refs and completes the canonical contract. Preparation retains actual Git objects without moving the logical branches; finalization consumes the selected originals rather than discovering replacement commits.

## Hot Path Summary

Code intent selection precedes private execution. The journal retains exact code and memory-content outputs. The physical code view and current logical memory pair feed memory certification; only the exact current, selected fifth result permits memory-output preparation. Existing output reuse proves raw Git head, ref and tree facts separately from the certified memory-content tree. Finalization publishes or retains the code output first, then the memory output, proves the resulting pair, completes the contract and refreshes the derived cache.

## How It Is Built

`selected.py` carries an immutable selected intent, its object reference and its current certification handoff. Intent selection and command compare-and-swap operations live outside this transport package in `preparation_selection.py`.

`code_output.py` selects the code intent and binds its original four-certificate prefix. `code_execution.py` either completes permitted private commands or observes genuine existing code. `private_execution.py` orders the kernel-authorized create, materialize and commit commands through the operation journal. `output_selection.py` retains exact raw commit outputs in the certificate object store and selects their references in that journal. `policy.py` observes effective Git configuration, identity environment and configured hooks.

`code_view.py` separates the physical code read root from logical pair identity. Created code uses its selected private root; existing code uses its logical root. It also provides read-only reproof of selected code after a worker has returned `input-required`, without requiring a live worker lease.

`memory_port.py` defines the typed certification request, result and producer port. `memory_execution.py` observes current memory content against the proved code view, invokes the installed producer and reopens its selected result. `memory_output.py` selects one memory-content output after code preparation. Its commit message uses the kernel's shared `Code-Commit:` renderer. `memory_reuse.py` proves whether the current existing memory commit can supply the certified content without creating a replacement commit.

`continuation.py` composes the installed memory producer, output preparation and finalization. `finalization.py` rechecks ownership, certificates, policy, candidate authority, route review and approval before publishing the selected pair and completing the contract.

Onboarding refresh validation belongs to the supporting memory producers. The curator memory-quality controller uses the shared sidecar and governing-route validator for an unconverted tree and the history-file trace gate for a converted tree. The prepared closeout adapter likewise checks both refresh surfaces for an unconverted tree, but calls their validators separately; converted trees use the history-file trace gate. The adapter also enforces its prepared-closeout eligibility guards. These checks do not change this package's ownership of selected outputs and publication.

### File-Level Onboarding Map

- [__init__.py.md](__init__.py.md) — Private preparation package marker.
- [selected.py.md](selected.py.md) — Immutable selected preparation transport.
- [policy.py.md](policy.py.md) — Actual Git configuration, identity environment and hook policy observation.
- [private_execution.py.md](private_execution.py.md) — At-most-once journal-bound private Git execution.
- [output_selection.py.md](output_selection.py.md) — Exact raw output retention in the existing object store and journal.
- [code_output.py.md](code_output.py.md) — Selected code preparation intent and original prefix binding.
- [code_execution.py.md](code_execution.py.md) — Private code creation or genuine existing-code observation.
- [code_view.py.md](code_view.py.md) — Physical code execution view for selected preparation.
- [memory_port.py.md](memory_port.py.md) — Typed prepared-memory certification request, result and port.
- [memory_execution.py.md](memory_execution.py.md) — Prepared memory candidate observation and selected result currentness.
- [memory_reuse.py.md](memory_reuse.py.md) — Read-only proof of genuine existing memory output.
- [memory_output.py.md](memory_output.py.md) — Post-certification selection of the single memory-content output.
- [finalization.py.md](finalization.py.md) — Original prepared output publication and canonical contract completion.
- [continuation.py.md](continuation.py.md) — Default selected continuation and producer binding.

## Invariants And Boundaries

A constructed producer response does not authorize publication. Memory preparation reopens the exact selected result and verifies its current candidate, operation owner, result manifest, certificate, memory tree and logical pair authority. Missing producer composition is an explicit prepublication refusal.

Private execution records each command start before launch and completes only an unstarted suffix. An uncertain original start is not repeated. Retained outputs are physically re-proven rather than recreated, and memory preparation reobserves actual policy and the original selected intent.

Root `memory.md` is excluded from the certified memory-content view. Existing memory reuse preserves the actual commit and its raw tree while binding the separately certified tree without that cache. Cache removal and ignore preparation occur alongside substantive memory work; a clean old commit containing the cache does not cause a maintenance commit. Cache state cannot request an additional output or publication.

Finalization journals each original publication prestate once and reobserves already-proven code and memory refs. Recovery requires the same running worker and generation and the original selected two-output bundle; an already-finalized contract returns through the closed-result path. There is no ledger publication leg or requirement for retained ledger bytes. Cache refresh follows Git publication and pair proof. The cache helper returns its availability status without deciding Git transaction success; the closed-result payload does not include that status.

This overview documents source behavior; it does not establish aggregate acceptance.

## Evidence

- Selected intent and command CAS remain outside the transport package. [1]
- The selected bundle contains code and one memory-content output. [2]
- Existing memory reuse binds raw Git facts and a separately certified content tree. [3]
- Final publication proves and publishes the pair, then refreshes the cache. Publication intent retains the original prestate; the cache helper reports availability internally, while the closed-result payload omits that status. [4]
