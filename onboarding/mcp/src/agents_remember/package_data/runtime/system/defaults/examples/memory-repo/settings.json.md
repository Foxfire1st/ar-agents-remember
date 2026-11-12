# settings.json

## Purpose

This JSON example models machine-readable settings for a external memory repo.

## Code Commentary

### Logic

The example uses settings version 2, `memory-repo` onboarding storage, include/exclude path rules with common generated/vendor/build/local excludes, and a branch-gated `crossRepo.allow` entry.

### Conventions

This file demonstrates memory-owned policy, not coordinator routing.

### Invariants And Boundaries

`onboarding.storage` decides where eligible onboarding lives, `onboarding.pathRules` decides eligibility, the standard excludes prevent common generated or local-machine artifacts from being selected, and `crossRepo.allow` opts into adjacent repositories.

### Todos

None.

### Docs References

No external documentation is needed.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The JSON example declares version 2 memory-repo storage and path-rule include/exclude filters with common generated/vendor/build/local exclusions. [1]
- The JSON example shows a branch-gated cross-repo allowance with code and memory inclusion flags. [2]

### Cross-Repo References

No sibling repository evidence is needed.

No meaningful cross-repo references found.
