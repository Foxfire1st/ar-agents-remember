# dashboard/src/data/reviewTrees.cards.test.ts

## Governing Overview

[governing overview](overview.md)

## Purpose

Exercise the mounted reviewTrees.cards owner and its delivered read/selection states.

## Code Commentary

The cases mount `useChangeSetCards` against deferred fetches and check shared pending/completed answers across remounts, order-insensitive sets, 500-ID chunk sizing, no old answer under a new question, a failed chunk retried after remount, and unavailable memory values retried by Refresh. Successful recovered values are reused; a genuinely unconverted after side remains cacheable. No second product state or installation acceptance is introduced.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- Exercise the mounted reviewTrees.cards owner and its delivered read/selection states. [1]
