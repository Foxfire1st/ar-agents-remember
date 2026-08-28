# mcp/tests/test_code_quality_tool_signature_exemption.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_code_quality_tool_signature_exemption.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This architecture-fitness suite owns the one justified PLR0913 exemption: published FastMCP tool
signatures whose Python parameters define their external JSON input schema.

## Logic

The tests require real Dagger admission, prove PLR0913 is armed, pin the sole per-file-ignore, walk
every exempted registration module's AST, reject ordinary functions/classes/lambdas under that
path, ignore source suppression directives during a whole-tree Ruff probe, and prove a normal
seven-argument function still fails under the repository configuration.

## Invariants And Boundaries

- The exemption cannot widen beyond `mcp/src/agents_remember/mcp/registration/*.py`.
- Registrars may contain only tool declarations, docstrings, or same-module registrar delegation.
- The suite is explicit `architecture-fitness` evidence and cannot run as silent unit fallback.
- Ruff invocation mechanics live in `_ruff_repository_evidence.py`; policy remains here.

## Update History

- 2026-08-27T13:32+02:00 — Split the MCP wire-signature exemption from the general quality-wrapper
  suite and registered its explicit evidence lane and lifecycle. Verification remains closeout-owned.
