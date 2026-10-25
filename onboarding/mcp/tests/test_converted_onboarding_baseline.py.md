# mcp/tests/test_converted_onboarding_baseline.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_converted_onboarding_baseline.py` owns one converted-baseline case: accepting drift never waives a stale reference anchor, and a repaired pair adopts with its recorded code-commit trailer. Status, general baseline validation, dry-run and CLI cases remain in `test_converted_onboarding_drift.py`; leaf-route transaction cases remain in their own module.

## Code Commentary

The module imports shared builders from `converted_onboarding_drift_support`. Its local `bound_validation` fixture installs the real `WorktreeServices`/`GitKnowledgeValidation` binding. The case first requires a stale-anchor world to refuse as `blocked-drift`; `accept_drift=True` still refuses as `blocked-invalid` naming `R198.1-reference-anchor`. It then creates a separate `card=True` repaired world, requires adoption and checks the paired `Code-Commit:` trailer. These are source assertions, not a fresh run.

## Evidence


- Related baseline coverage in the retained drift suite: `accept_drift` never clears a validator violation. [2]

- A stale anchor refuses the baseline even when drift is accepted, and the repaired tree adopts with its code trailer [3]
