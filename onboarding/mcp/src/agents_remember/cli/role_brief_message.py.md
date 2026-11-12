# mcp/src/agents_remember/cli/role_brief_message.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Assembles one role's first message in one order, once each, from the parts the launch already holds: who started the seat, the direction to split independent work, the AR-tools paragraph, the first-read paragraph, the optional shared block, the compiled capsule and the hand-over projection.

## Code Commentary

The split-work direction the message carries is the shared SPLIT_WORK_DIRECTION text, and its boundaries travel with it: own-assignment helpers from the start with no cap, another role's work through the role-start tool, the named serial exceptions, the role as single writer of its stage's records, helper verification, and the report's split-or-why-not duty — stated in role_launch_preparation.py where the constant lives. brief_prompt composes the parts in that fixed order and never writes a file; the projection's file reference is planned from the bytes the launch will write beside the message, so the message can name a file that does not exist yet. BriefParts carries the texts so the composition reads as one sequence rather than a chain of string concatenations. shared_block writes the optional block under its heading only when the compilation carries non-empty text, so an empty block changes nothing in the message.

## Evidence

- The message is assembled in one fixed order and each part stands once. [1]
- The optional shared block is written only when the compilation carries non-empty text. [2]
- The parts of one message are carried together rather than as separate arguments. [3]
