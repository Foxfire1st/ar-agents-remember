# Closeout Projection Models Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/models/closeout` |

## Governing Overview

[Models overview](../overview.md)

## Purpose

This directory defines strict wire and persistence models for closeout inputs, door-source facts, disposable queue projections, and task-publication effects. It supplies the vocabulary and validation contracts used by closeout producers and consumers; the projection is scheduling state, not lifecycle or commit evidence.

## Hot Path Summary

`input.py` owns the two accepted commit-message legs and delegates memory attribution to the kernel. `source.py` supplies typed admission/scheduling facts; `projection.py` supplies disposable scheduling state and publication effects, not lifecycle evidence.

## How It Is Built

`input.py` defines public message observations, resolved commit-leg plans, typed input refusals, and the effective message-bearing closeout input. There are exactly two public commit legs: `code` and `memory`. Each effective leg is either enabled with a normalized, nonblank message or not applicable. `message_for` returns an enabled leg's accepted message and refuses a not-applicable leg. There is no ledger message field, commit leg, or enabledness state in this contract.

`EffectiveCloseoutInput.memory_content_message(code_commit)` is the closeout-shaped entry to the kernel's attribution renderer. Worktree closeout in `worktrees/modules/closeout_external.py` and branch-addressed direct landing in `worktrees/integration/direct_landing/direct_landing_execution.py` both use it when publishing their memory-content commit. The renderer preserves the accepted memory message verbatim and appends one `Code-Commit: <sha>` line as a separate final paragraph, naming the code commit supplied by the closeout caller.

`source.py` defines admission facts, scheduling grades and their provenance, evidence-file hashes, and route-review facts. False resource or admission readiness requires an explanatory reason.

`projection.py` defines queue members and the `valid-built` / `invalid-empty` service conditions, together with source-problem, invalidation, rebuild, and task-document effect payloads. A member carries its waiting generation, task and owning master, candidate tree, door fingerprint, classification, reasons, priority, and order. The member list has no population ceiling; the number of leaves declared by a sprint is not bounded by this model.

### File-Level Onboarding Map

| Source File | Onboarding | Status |
| --- | --- | --- |
| `projection.py` | [projection.py.md](projection.py.md) | covered |

## Invariants And Boundaries

All closeout models reject unknown fields. The input models are also frozen. Text and evidence/problem/reason collections have explicit bounds where declared; this is not a blanket bound on every payload or on queue membership.

A queue contains each waiting generation and each task at most once. An `invalid-empty` projection has no members, accepted source fingerprint, or source classification. A `valid-built` projection requires a source fingerprint and classification and cannot carry unresolved source problems. A terminal `valid-built` projection is empty. Stale rows therefore cannot remain as accepted membership in an invalid projection or become a second lifecycle database.

An incomplete task-document projection effect requires a next action; a completed effect cannot carry one. The model treats `published`, `already-current`, and `would-publish` rebuild outcomes as complete.

The kernel owns both the attribution trailer key and its renderer in `kernel/memory_attribution.py`; this route delegates to that renderer rather than duplicating it. The key is defined and interpolated in the kernel module. `layers.toml` ranks kernel below models, so models may depend on the kernel primitive and the kernel must not import a model to obtain the key or renderer.

No configured external source applies to this slice. Queue producers and application consumers are documented through same-repository source references.

## Evidence

- Accepted closeout message input contains only code and memory. [1]
- The effective two-leg input renders memory attribution through the kernel. [2]
