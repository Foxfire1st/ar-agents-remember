# mcp/src/agents_remember/models/knowledge/review_meaning_effects.py

## Governing Overview

[Owning route](../overview.md)

## Purpose

Own the typed recorded-step and outline-answer contracts, their three mutually exclusive states, and the fixed label explanations.

## Code Commentary

A step preserves attempt, row ID, history path, closed status, reason and the row’s own effect/revision. Missing effect/revision is the historical family-row boundary, not an inferred present family value. Record answers require a nonempty step list exactly for steps, and the fixed no-recorded-effect text exactly for none. Outline answers carry labels only for steps.

The nine explanations follow ADMITTED_EFFECT_LABELS in its own order. They describe the vocabulary without endorsing the curator’s judgment. ReviewMeaningEffects is the existing subject response’s record collection; it covers returned family/member context, including continued members, not every record in the repository.

## Evidence

- Record answers enforce steps versus none/unavailable and the fixed absence text. [1]
- Outline state and labels are validated together. [2]
- The explanations match the admitted label vocabulary and order. [3]
