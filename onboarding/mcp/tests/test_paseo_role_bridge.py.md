# mcp/tests/test_paseo_role_bridge.py

## Governing Overview

[Route overview](overview.md)

## Purpose and current source account

Message send distinguishes idle-turn start, in-flight steering, permission refusal and non-steerable busy providers. Wait follows the turn that consumed the message rather than a later unrelated turn, and reports delivery uncertainty without cancelling work. The native client is replaced by a controlled event/state stub.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]
