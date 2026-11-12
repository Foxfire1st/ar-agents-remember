# mcp/tests/workflow_chain_guidance_test_support.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The disposable world, the single walk and its derived populations for the workflow chain: two real Git repositories, real task documents and a real registered server, measured over the guidance each response publishes.

## Code Commentary

`WorkflowWorld` authors a master and two leaves whose single step is done, opens a sibling master's enclosure as a concurrent seat, and supplies fixture values for arguments a recommendation leaves to the caller. `Hop` records one operation, the arguments its own guidance supplied and what came back, exposing its state, its operational triple and its guidance channels; `RecommendedCall` records one published triple, the response that published it and what calling it exactly as published produced. `WorkflowChainObservation` performs the one walk: it reads the phase channel or the response's own recommendation, fills the arguments the workflow statement declares, calls the step exactly as given and then again with only the arguments it omitted, and derives the callability population as the union of what each hop's guidance supplied and what each response's operational triple supplied. It also drives the sibling arrangement, the stale-base arrangement and the retry-provider-setup producer. `classify_call` separates a call refused by its own argument model from one that lost the envelope by model identity; `emitted_next_step` translates the answer's hint back into the guidance shape, and `missing_required_args` names the fields the model required and did not receive.

## Invariants And Boundaries

The declaration constants are part of the statement under test: the operations, the expected states and phases, the hops whose guidance withholds an operation, and the steps whose guidance omits a required argument. `FIXTURE_ARGS` states `dry_run` explicitly, because a preview hop that silently lost it would run the real operation in the fixture. Coverage is per response, not per call: a step's own triple counts only when the response that published it was the one called.

## Evidence

### Repo-Internal References

- The walk calls each step exactly as its guidance gave it, then again with only the arguments it omitted. [1]

- The callability population is the union of each hop's guidance and each response's own operational triple. [2]

- A call's failure arm is decided by model identity: the tool's own argument model is the caller's error, any other raise lost the envelope. [3]
