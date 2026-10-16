# mcp/src/agents_remember/serving/capsule_delivery.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The generic frozen value carrying one admitted role capsule into a host role launch. It has no Codex app-server parameter builder, refresh planner, legacy switch or serialized carrier-artifact reader.

## Code Commentary

CapsuleBindingIdentity checks nonempty trimmed repository, task, role and operation fields and renders their report. CapsuleDelivery holds that identity, the trusted instruction stream and the compiler semantic digest, refusing blank instructions and a digest without the sha256: prefix. capsule_delivery_from structurally reads the compilation binding and admitted facts, maps role versus launcher seat, and copies render_instructions() plus the compiler digest and frozen detail references without importing the compiler implementation or adding a rerendering policy. No task/tool/model-authored field is a trusted-instruction input.

## Current Contract

CapsuleDelivery now carries default-empty frozen detail_references copied structurally from the compiled capsule, while preserving the instruction stream and semantic digest verbatim. The default empty tuple supports detail-free structural inputs. This module copies compiler-owned values; it does not write, path-substitute, validate replay files, consult settings or grant permissions. The launch artifact owner is responsible for frozen workspace files and their immutable replay binding.

This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence boundary


- Launch copies detail files, substitutes paths, and records frozen revisions. [6]
- Replay validates regular opened files, content revisions and original canonical report binding, not mutable corpus sources. [7]
- Per-request detail artifacts use exact admitted bytes beside the handover and write-once publication. [8]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [9]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [10]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [11]

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs

- [2]
- [4]
- [5]
