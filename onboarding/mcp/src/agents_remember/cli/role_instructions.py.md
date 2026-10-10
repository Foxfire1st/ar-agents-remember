# mcp/src/agents_remember/cli/role_instructions.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Composes plaintext user instructions over the role baseline at the launch boundary, with metadata that never repeats raw text.

## Code Commentary

`compose_role_instructions` appends user text to the baseline by default; a first-nonblank-line `<overwrite>` tag replaces only the host instruction block, and an empty replacement refuses before creation. Returned records distinguish baseline, effective and raw-text digests with delivered blocks, keeping the structural capsule outside the replaced range. `launch_choice_metadata` replaces raw notes text with its digest, presence and baseline-replaced flags and strips profile notes; `instruction_metadata` strips delivered text from blocks for public answers.

## Evidence

- Role notes compose as plain text with first-nonempty-overwrite semantics. [1]
- Choice metadata digests note text and strips profile notes. [2]
- Instruction records drop delivered text from stored blocks. [3]
