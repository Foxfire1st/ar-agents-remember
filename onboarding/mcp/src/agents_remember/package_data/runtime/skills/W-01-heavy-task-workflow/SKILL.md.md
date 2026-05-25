# W-01 heavy task workflow SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/W-01-heavy-task-workflow/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90`         |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|

## Purpose

This skill is the orchestrator entrypoint for the full heavy task workflow.

## Notes

It owns developer interaction, root artifact ownership, checkpoint routing, and phase-skill delegation. Its phase-local skill packages live under this package's local `skills/` directory.

## Update History

- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-15T01:55+02:00: Created with pending verification metadata for the runtime skill-tree move.
