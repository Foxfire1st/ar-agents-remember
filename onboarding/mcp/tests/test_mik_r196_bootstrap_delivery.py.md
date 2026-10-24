# mcp/tests/test_mik_r196_bootstrap_delivery.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Drives the one call's continuation and the free seats' chat discovery through the shipped boundaries (MIK-R196 rule 1): the registered start tool with its payload, response model and compact projection, and the receipt-backed document chat read.

## Code Commentary

`_FreeSeatWorld` registers the role tools with a caller harness and a host whose chat route answers, hands the receipt the first-run report in the shape the stage runner returns, and reads the whole result back from the answer's detail file. `FreeSeatDeliveryTests` requires a bootstrap start to answer with its seat and the place the user continues it, requires a dashboard that does not answer to be reported instead of published, and requires a repeat of the same request to reconcile the same seat. `FreeSeatOverrideTests` requires a model-only choice to bind the caller's own harness, refuses a model the bound provider does not offer before a seat exists, and keeps the refusal for another role. `FreeSeatDiscoveryTests` reaches a bootstrap seat behind architect records across pages, answers an explicit bootstrap selection, and answers an exact request read beyond the listing. The module-level cases drive the real installer and require a preparation refusal to report the files already written, an occupied providers path, a partially copied file, a tree removal that names the child it deleted, each returned provision effect's identity, and the successful effects kept when a later HTTP refusal ends the call.

## Invariants And Boundaries

`authority_runtime` puts the host block in the MCP authority settings file because that is the file the product reads, so the cold-start path measured is the shipped one. The first-run report is `FIRST_RUN_STAGES` shaped: scaffold, host authority, host running. Nothing here asserts a call succeeded; each case asserts what the caller received.

## Evidence

### Repo-Internal References

- A start answers with the seat it made and the address at which the user continues it, and a repeat reconciles that seat. [1]

- A model-only choice binds the caller's own harness, and an unoffered model is refused before a seat exists. [2]

- A preparation refusal reports the files already written and each returned effect's identity. [3]
