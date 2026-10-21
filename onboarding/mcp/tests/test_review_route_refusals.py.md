# mcp/tests/test_review_route_refusals.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Declare actionable review transport refusal contracts and comparison-number forwarding against the real registered routes with injected application ports.

## Code Commentary

The evidence_unit module builds a bare FastAPI app with real register_review_routes and roots that resolve no actual workspace. ACTIONABLE names status, detail and nextAction. Both unwired review/catalogue routes require503 and a composition-root action; invalid selector admission is a400 that runs no port and names the offending value and admitted kinds.

The review-port exception cases preserve AuthorityError detail/action as400 bad-path and FileNotFoundError path/offendingInput/action as404 not-found. The typed candidate_dataset_absent result remains404 with the complete refusal and no payload. The parametrized catalogue case declares four absence codes as404 and comparison_refused as400, preserving entries=[] and the owner action.

The added catalogue test sends comparison=-1 and requires actionable400 bad-request naming -1 without calling its injected port. A subsequent comparison=3 must return200 and pass exactly3 to that port. Catalogue test doubles now accept the optional fourth comparison argument. These are admission/forwarding checks, not a test that the application resolved a real comparison3.

## Invariants And Boundaries

The registered route is real; application resolution is injected. These assertions establish their declared in-process body/status contract when run, not rendered UI, native HTTP, stored-comparison truth or fresh execution. Historical source-docstring HTTP evidence is not rerun evidence. The two port-exception cases cover the review route, not a new exception catch around the catalogue port.

## Evidence

- Bare-app helpers and source-declared unwired/selector refusal cases exercise the actual registrar. [18]
- The review route preserves actionable exception bodies and whole typed refusals. [19]
- Five parametrized catalogue refusals retain their own status family and empty entries. [20]
- Negative comparison admission runs no port; positive3 forwards unchanged. [21]
