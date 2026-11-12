# skills/l-01-agent-lifecycles/capsule-budgets-current.json

## Governing Overview

[overview](overview.md)

## Purpose

The current size record for the delivered role instructions: the word limits and measurements of every role/operation capsule, every declared step detail and the every-role digest, which the budget tests check the compiled texts against.

## Code Commentary

The record has schema `ar-role-capsule-budget-current/v1`. `current_limits` and `current_measurements` hold 34 capsules (the eight launchable roles and the launcher), 38 step details under the new `reference/` subject folders plus `templates/turn-report.md`, and `core/every-role.md` at 2,327 words; `current_measurements` also lists four ordinary linked templates. The role ceilings are Architect 5,474 words, Manager 4,562, Curator 4,537, Reviewer 4,112, Bootstrap 4,000 and every other role 3,742; the step ceiling is 2,500 and the digest ceiling 2,327.

`current_detail_population` must equal the manifest's `step_detail: true` sources, the linked templates must be manifest entries with `step_detail: false`, and `approved_source_sizes` and `compiler_input_revisions` pin each source's words and SHA-256, so a source that changes at the same size still fails. The `decision` block records the size authority and each measured renewal, and binds by SHA-256 the historical registry `capsule-budgets.json`, its predecessor layer `capsule-budgets-d694.json` and the current `core/digest-map.json`. The one sub-record flagged `current` is `measuredCurrentRenewalWaitsAndCodingGuidelines` (the declared helper or background wait line and the coding-guidelines duties); the earlier always-on tool-name sub-record is carried whole inside it as `supersededUncommittedRecord` without a `historicalTree`, because it was current only in the uncommitted candidate and never on a committed tree. A growing text is re-measured and its renewal recorded here in the same change, and a changed digest map renews `currentDigestMapSha256`; the tests never raise a limit themselves.

## Evidence


- The decision block binds the historical registry, the predecessor layer and the digest map by SHA-256. [1]
- Current limits for 34 capsules, the step details and the digest. [2]
- Current measurements, including the ordinary linked templates. [3]
- Role, step and digest ceilings. [4]
- The detail population must equal the manifest's declared step details, and linked templates must be ordinary manifest entries. [5]
- The predecessor layer and the historical registry are bound by hash. [6]
- The capsule tests read their limits from this record. [7]
