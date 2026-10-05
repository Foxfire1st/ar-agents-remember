# mcp/tests/test_paseo_status.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

Ordered status-table cases distinguish unavailable host, absent/archived agent, closed session, permission wait, running/failed/cancelled/idle turns and unknown states. Refresh uses read commands, preserves an unreachable receipt, and scopes lock duration to the bridge call. Revive resumes the recorded agent only under retained task scope; resume refusal persists until the host shows an open session.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
