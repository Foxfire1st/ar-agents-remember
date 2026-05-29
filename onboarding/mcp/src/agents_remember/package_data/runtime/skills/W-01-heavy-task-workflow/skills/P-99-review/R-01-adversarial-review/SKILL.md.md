# R-01 adversarial review SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/W-01-heavy-task-workflow/skills/P-99-review/R-01-adversarial-review/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T08:59+02:00                     |
| lastVerifiedCommitHash | `495e9fa503b8708cc2b05a7e67f447071690ee41`         |
| lastVerifiedCommitDate | 2026-05-29T09:04:31+02:00|

## Purpose

This review skill runs W-01 checkpoint adversarial reviews.

## Notes

It is independent review guidance for CP1 through CP5 and writes review-only artifacts under P-99.

The SKILL.md now declares its W-01 phase scope explicitly (description guard plus a `## Scope` section) so the flat-installed copy is not used in the chat (W-03) or light (W-02) workflows.

## Update History

- 2026-05-29T08:59+02:00: SKILL.md gained an explicit W-01-only scope guard (description prefix plus a `## Scope` section) so the flat-installed skill is not triggered in chat (W-03) or light (W-02) workflows.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-15T01:55+02:00: Created with pending verification metadata for the runtime skill-tree move.
