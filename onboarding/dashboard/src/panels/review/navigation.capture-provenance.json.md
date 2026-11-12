# dashboard/src/panels/review/navigation.capture-provenance.json

## Governing Overview

[Owning route overview](../overview.md)

## Purpose

Retain a test-only input/capture receipt for the reviewer.

## Code Commentary

The facts below are read from the retained source bytes, not from a fresh producer invocation.

### Retained Input Facts

- `manifest_keys`: ["scope", "fixture", "source_manifest", "source_manifest_sha256", "import_origin", "command", "responses"]
- `scope`: "Untouched current public-route member response for the forced-order keyboard regression; not backend classification or installed acceptance."
- `responses.count`: 1
- `responses.rows`: [{"file": "/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l57-ar/scratch/worker/48060148-87d0-4e1e-ad2e-6f1fa353092d/consumer-followup/keyboard-capture-01/raw/navigation.member-753.captured.json", "state": "review", "status": 200, "bytes": 266595, "sha256": "55f535eb3cc5357d0ed8b4c979fd2fa13d4a555fd9e015d64bd85f1578cd68f5"}]

These are fixture facts, not current project knowledge. A receipt states its recorded capture custody; reading it here does not recreate its command or validate an installed dashboard.

## Evidence

- The retained source supplies the facts and declared boundaries described above. [1]
