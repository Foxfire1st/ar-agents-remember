# mcp/src/agents_remember/cli/role_brief_message.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Assembles one role's first message in a KV-cacheable static-prefix-first order, once each, separating the immutable role instructions from dynamic per-launch context at `## Launch Context`.

## Code Commentary

The split-work direction the message carries is the shared `SPLIT_WORK_DIRECTION` text, and its boundaries travel with it: own-assignment helpers from the start with no cap, another role's work through the role-start tool, the named serial exceptions, the role as single writer of its stage's records, helper verification, and the report's split-or-why-not duty — stated in `role_launch_preparation.py` where the constant lives. `brief_prompt` composes the static immutable prefix first (static `AR ROLE BRIEF:` header without `started_from`, `direction`, `ar_tools`, the `IDENTITY_SELF_CHECK_PARAGRAPH` binding self-check, optional `## What every role acts on` shared block, and compiled capsule `instructions`), followed by `LAUNCH_CONTEXT_HEADING` (`## Launch Context`) carrying dynamic per-launch fields (`Started by`, `first_read_paragraph`, and optional `link_roots`) and then `HANDOVER_HEADING` plus the compact JSON projection; it never writes a file, and the projection's file reference is planned from the bytes the launch will write beside the message so the message can name a file that does not exist yet. `BriefParts` carries the text parts, including optional `shared_block` and optional `link_roots`, so the composition reads as one sequence rather than a chain of string concatenations. `shared_block` writes the optional block under its heading only when the compilation carries non-empty text, so an empty block changes nothing in the message.

## Evidence

- `brief_prompt` assembles the static immutable prefix before `LAUNCH_CONTEXT_HEADING` (`## Launch Context`) and places `Started by`, `first_read_paragraph`, optional `link_roots`, and the compact handover projection in the dynamic suffix. [1]
- The optional shared block is written only when the compilation carries non-empty text. [2]
- `BriefParts` carries the message texts, including optional `shared_block` and `link_roots`, together as one value. [3]
- `IDENTITY_SELF_CHECK_PARAGRAPH` stands in the static prefix directly after the AR-tools paragraph, directing every started seat to verify its `server_info` `agentBinding` against its handover before any other call or write and stop with an `IDENTITY MISMATCH:` line on mismatch. [4]
