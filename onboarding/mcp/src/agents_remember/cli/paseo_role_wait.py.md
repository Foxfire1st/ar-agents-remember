# mcp/src/agents_remember/cli/paseo_role_wait.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Waits for the native turn that consumed one delivered role message.

## Code Commentary

wait_for_turn performs a sequence of bounded bridge calls under one tool call and deadline, carrying actual message/turn evidence forward. It stores no transcript or background poller. _turn_result distinguishes ended, resumed, waiting, timeout and undecided native facts without sending the message again.

## Evidence

- Frozen implementation of wait_for_turn supporting the stated file behavior. [1]
- Frozen implementation of _turn_result supporting the stated file behavior. [2]
