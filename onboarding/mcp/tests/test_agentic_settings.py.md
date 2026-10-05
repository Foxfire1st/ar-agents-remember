# test_agentic_settings.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Two-layer agentic settings merge and authority-boundary tests.

## Current source account

Three added serviceTier cases prove independent inheritance through flat/global/repository/per-level roles, rejection of invalid values and fast boolean, and explicit refusal when legacy terminal spawning cannot carry a tier. Retained model/effort merge and authority cases remain; this adds no paid-model qualification.

## Code Commentary

### Logic

Local leaf overrides preserve global siblings; arrays replace and absent files expose defaults. Retained refusals name malformed settings paths, reject local gate delegation, human-pinned delegation and executor authority in agentic settings. Role overrides inherit flat defaults; harness references resolve against the effective merged registry.

Two harness-vocabulary contracts are pinned the same way the source states them:

- `test_new_id_adds_a_harness_with_defaults_derived` reads the expected builtin id prefix from
  `HARNESSES` instead of transcribing `["claude", "codex", "pi"]`, so adding a builtin row cannot
  silently pass an ordering check.
- `test_a_builtin_override_keeps_its_runtime_readiness_probe` asserts that overriding a builtin's launch
  mapping preserves its readiness probe — eve is detected through a runtime probe, not a PATH lookup, and
  an override must not downgrade that — while a settings-defined id (hermes) declares no probe to
  inherit.

### Conventions

The baseline cases retained from IAS `d3610903` are joined by the current source account above. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Executor selection is not an agentic-settings option. The remaining tests do not establish the removed unknown-key, free-form knob or effort-policy matrices.

**A builtin's readiness probe survives an override and a new id has none.** The override case asserts
both halves, so a merge change that drops the probe fails here rather than in production detection.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

- The curated table the order assertion derives its expected prefix from, and the probe-carry merge the override case pins. [1]
- The two harness-vocabulary cases this change set touched. [2]

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Local leaf overrides global leaf and siblings survive. [3]
- Arrays replace never concatenate. [4]
- Absent files mean documented defaults. [5]
- Local gate delegation is refused global layer only. [6]
- Malformed json fails loud with path. [7]
- Human pinned gate kind cannot be delegated. [8]
- Level override deep merges over the flat default. [9]
- New id adds a harness with defaults derived. [10]
- Cross layer reference and partial override merge. [11]
- Reference to an id known nowhere fails naming the manual. [12]
- Executor authority is not accepted in agentic settings. [13]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
