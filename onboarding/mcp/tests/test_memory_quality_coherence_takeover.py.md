# mcp/tests/test_memory_quality_coherence_takeover.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Pins memory-quality recovery projection when the coherence readiness join supplies a refusal.

## Code Commentary

A real parentless task fixture requires task-document-parent-missing with task_doc as recovery. The second test also uses a parentless fixture without publishing an authority. It checks refusal, coherence-required status, equal code/coherenceStatus strings and a truthy nextAction; it does not discriminate stale authority or require the exact publish action. These assertions protect the application join and answer projection, not a favorable default or independent memory certification.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.

- Missing-parent failure keeps code and task_doc action. [1]
- A parentless fixture retains generic refusal identity/status and a nonempty recovery action; no stale-authority or exact-publish discriminator is asserted. [2]
