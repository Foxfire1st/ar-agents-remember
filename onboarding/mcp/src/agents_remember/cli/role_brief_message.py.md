# mcp/src/agents_remember/cli/role_brief_message.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Assembles one role's first message in one order, once each, from the parts the launch already holds: who started the seat, the direction to split independent work, the AR-tools paragraph, the identity self-check paragraph, the first-read paragraph, the optional shared block, the compiled capsule and the hand-over projection.

## Code Commentary

The split-work direction the message carries is the shared SPLIT_WORK_DIRECTION text, and its boundaries travel with it: own-assignment helpers from the start with no cap, another role's work through the role-start tool, the named serial exceptions, the role as single writer of its stage's records, helper verification, and the report's split-or-why-not duty — stated in role_launch_preparation.py where the constant lives. brief_prompt composes the parts in that fixed order and never writes a file; the projection's file reference is planned from the bytes the launch will write beside the message, so the message can name a file that does not exist yet. BriefParts carries the texts so the composition reads as one sequence rather than a chain of string concatenations. shared_block writes the optional block under its heading only when the compilation carries non-empty text, so an empty block changes nothing in the message. `IDENTITY_SELF_CHECK_PARAGRAPH` stands in `brief_prompt` immediately after the AR-tools paragraph and before the first-read paragraph: it directs every started seat, as its first action before any other call or write, to call `server_info` on `agents-remember-task`, verify `agentBinding.requestId`, `agentBinding.role`, and task document refs against `requestId`, `role`, and `selection` in its handover (ignoring `host.parent.agentId`), and on any mismatch or unanswered server do no work, make no write, send no `role_message`, and end its turn with one final line (at most 300 characters) beginning `IDENTITY MISMATCH:`.

## Evidence


- The message is assembled in one fixed order and each part stands once. [1]

- The optional shared block is written only when the compilation carries non-empty text. [2]
- The parts of one message are carried together rather than as separate arguments. [3]

- `IDENTITY_SELF_CHECK_PARAGRAPH` defines the mandatory `server_info` binding self-check and `IDENTITY MISMATCH:` stop line, inserted by `brief_prompt` between the AR-tools and first-read paragraphs. [4]
