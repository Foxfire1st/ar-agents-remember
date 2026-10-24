# docs/concepts.md

## Governing Overview

[Repository overview](../overview.md)

## Purpose

The concept vocabulary page. It fixes the names agents use to decide what to read, what to
trust and what they may change: onboarding unit, memory root, coordination root, the three
ways an agent finds memory, the retrieval-strategy substrates, drift detection,
approval-gated memory, route-local overviews and the memory ledger.

## What The Page Establishes

- An onboarding unit is durable repository knowledge that maps one-to-one from a source file
  to a mirrored Markdown file in that repository's memory repo, and it explains what the code
  does not make obvious rather than restating it.
- Agents reach memory through three substrates. **By path** locates a note directly from the
  path (`src/foo/bar.ts` → `<memory-root>/onboarding/src/foo/bar.ts.md`) with no lookup,
  ranking or index step, so reads stay predictable and similar-but-unrelated material stays
  out of context. **By meaning** is described in the past tense: semantic search over the
  memory found candidate notes, its provider is retired, and the route has no engine now.
  **By relationship** is likewise past tense: a code-relationship graph answered callers,
  callees and dependencies, and that provider is retired too.
- The summary states that by-path notes are the core and need nothing extra, that meaning and
  relationship were served by two opt-in providers that are now retired, and that by-path is
  therefore the route with an engine today.
- The page keeps the router it names next: three substrates, *Intent*, *Semantics* and
  *Relationship*. In that section `Semantics` and `Relationship` repeat the same retirement —
  a provider searched, the provider is retired, the route has no engine. `Intent` — hidden
  contracts, invariants, behavioral expectations, branch-valid truths, code intent — remains
  the default substrate and is served by onboarding plus bounded source confirmation.
- Durability is unchanged by any of this: what becomes durable memory is drift-checked and
  approval-gated, and "finding is not the same as trusting". Provider output is called
  candidate routing evidence, never proof; source files, verified onboarding, drift checks,
  branch validity and approved memory promotion are the truth controls.
- The remaining sections keep their own definitions: drift outcomes (`up to date`,
  `drifted`, `missing verification`, `orphaned`, `unsupported`), approval-gated memory as
  approved current state rather than speculation, route-local overviews as added structure
  that never replaces file-level onboarding, and `memory.md` as the ledger mapping code
  commits to memory commits.

## Boundaries

The page is conceptual guidance, not runtime behaviour. It states that a route has no engine;
it does not describe what happens to leftover provider state, how to clear an old install, or
how a provider was configured — none of that is on this page, and no provider id, setting or
command is named.

It also does not define the router's decision procedure; it names the substrate trio and
points at the retrieval-strategy skill, which is the owner of that procedure. Nothing on the
page is a claim that any route, drift check or approval gate was exercised.

## Evidence

- Onboarding units map one-to-one from source file to mirrored Markdown note and carry what the code does not make obvious. [1]
- By path is direct and index-free; by meaning and by relationship are past tense with retired providers and no engine. [2]
- The substrate trio is Intention/Semantics/Relationship; `Semantics` and `Relationship` carry the retirement, `Intent` remains the default. [3]
- Provider output is candidate routing evidence, not proof; source, onboarding, drift and approval remain the truth controls. [4]
- Drift outcomes, approval gating, route-local overviews and the memory ledger keep their definitions. [5]
