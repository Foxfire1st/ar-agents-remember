# mcp/src/agents_remember/cli/role_step_up_decisions.py

## Purpose

Reconcile task-owned durable step-up metadata from saved and observed launch facts.

## Governing Overview

[MCP package overview](../../../overview.md)

## Current Contract

recorded_step_up scans decisions newest-first for the exact Step-up <role>. label whose rationale is a JSON object with schema ar-role-step-up/v1. It skips unrelated human prose rather than overwriting it.

record_step_up resolves the selected task/master/sprint reference and holds the existing repository task-publication lock across reread/update. With no prior recognized decision it appends requested destination, request ID, selected source and sanitized choices through task_doc_tool; no ephemeral prepared object or second store is required.

For the same recorded request with an existing host agent, _record_observed updates the recognized decision’s actual destination/model/choices while preserving requestedTo and requestedModel, other decision rows and task fields. A failed writer answer raises retry-the-same-request advice; later exact reconciliation must occur without creating another agent.

This is launch metadata published by the canonical task owner, not evidence that a requested destination actually ran before observation, a review verdict, an extra round or permission to loosen the fixed findings/limit.

## Evidence

- Newest recognized structured role decision wins; human prose is not parsed as metadata. [1]
- Existing task lock and writer publish the first decision. [2]
- Observed destination updates are request-bound and preserve requested fields. [3]
- Test source exercises failed/lost decision acknowledgment, deduplication and receipt loss. [4]
- Test source preserves unrelated same-label prose and requested-vs-observed destination. [5]
