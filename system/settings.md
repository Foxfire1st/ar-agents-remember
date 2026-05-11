# agents-remember-md Memory Settings

This is the committed memory settings file for the `agents-remember-md` shared memory repo.

## Scope

The sibling `settings.json` is the machine-readable source for onboarding storage, path eligibility, and cross-repo policy for this memory repo.

This memory repo is selected by the local coordinator at `C:\ew\ar-coordination`, but durable repo policy belongs here, not in the untracked coordinator settings.

## Storage

Onboarding uses `memory-repo` storage. Eligible onboarding artifacts live under this memory repo's `onboarding/` directory.

## Path Eligibility

The path rules in `settings.json` are unscoped because this memory repo maps to exactly one code repo: `agents-remember-md`.

## Cross-Repo Policy

`crossRepo.allow` is currently empty. Neighboring repositories are not included unless this committed memory settings file explicitly allows them.
