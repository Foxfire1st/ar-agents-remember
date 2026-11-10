# skills/l-01-agent-lifecycles/reference/curator/current-prose-and-history.md

## Governing Overview

[overview](../../overview.md)

## Purpose

The Curator's rules for keeping current overview prose separate from authored history when updating overviews or answering changed-file and invariant history.

## Code Commentary

An overview never gains a heading named for a leaf or date or a task log; a change goes into the body section that owns its meaning. A truth is preserved when it matters to future correctness, is non-obvious and would be expensive to rediscover; code narration, temporary branch facts, raw test totals, generic implementation chronology and facts obvious from code and tests are omitted. A changed file whose card is brought current is answered by an `onboarding_trace` row through the admitted writer, named in the handover by subject, disposition and reason, with the writer binding it to the source content. Unexplained-hunk or unexplained-file worklist items follow the hand-off template's no-invariant row rules. For invariant history, a `moved` row covers the re-anchored entry, a `changed` row names its effect, a `deleted` row retiring the invariant names only `retire`, and other rows name no effect.

## Evidence

- Overview prose changes in the meaning-owning section, with no leaf or date headings and no chronology. [1]
- Changed-file history is answered by an `onboarding_trace` row through the writer, and unexplained items follow the template's no-invariant rules. [2]
- Invariant history rows name effects only for `changed` and retiring `deleted` rows. [3]
