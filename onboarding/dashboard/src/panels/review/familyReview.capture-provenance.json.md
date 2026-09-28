# familyReview.capture-provenance.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.capture-provenance.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:42:25+02:00 |
| lastVerifiedCommitHash | `9b2f775f1ab0fca5f82b4f661785dd8216d4a8b3` |
| lastVerifiedCommitDate | 2026-09-28T17:43:09+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

**The capture receipt for the `familyReview.*.captured.json` route bodies.** It binds each re-captured
family-review fixture to the exact producer run that wrote it, and it states — separately and as the
worker's own statement, not the producer's — which sibling fixtures were **not** re-captured and why. The
consuming cases (`ReviewWorkspace.family.test.tsx`, `ReviewReadCycle.family.test.tsx`) point at this
receipt from their headers instead of naming a script.

## Code Commentary

### Logic

**The run-level facts come first and apply to every listed fixture.** `captured_source_tree` and
`captured_at` date the run; `command` is the exact producer invocation; `route` states that bodies were
read over HTTP from `GET /api/review/intent` served by the real review routes wired with the dashboard's
own serving collaborators (review routes only); `capture_record` and `capture_record_sha256` bind the
per-request status/digest record; `selection_rule` and `signature` state how a build was accepted — the
scenario was rebuilt with fresh identities until every body carried the earlier committed capture's
structural signature (selection and statement states, family order, per-side member label/state pairs in
served order, page arithmetic) — and `attempts` records how many builds each group took. `scope` says
the bodies are test evidence over disposable enclosures, not product knowledge or mounted acceptance.

**`fixtures` lists what this run wrote**: `familyReview.complete.captured.json` and
`familyReview.identical.captured.json`, each with its sha256, the scenario builder it came from, its
request name and the one normalization (`repository_id` replaced by `<repository_id>`; keys sorted,
compact separators).

**`not_recaptured` is a worker-authored section and says so** (`stated_by`). It explains that the route at
the earlier capture listed only membership items on a roster page, while the current route also resolves
the member revisions that content and claim items represent, so `truncated`, `oneSided`, `walkFinal` and
`familyPaging` cannot be reproduced (0 matching builds), `continued` depends on `truncated`'s cursor, and
`emptyRoster` is reproducible but carries no member source and was left as captured. It lists the
analysis files that evidence those counts. Those fixtures keep their original bytes and lack the
member-source fields `locator`, `resolved_ranges` and `locator_state`.

### Conventions

- Fixture bytes come only from the producer; this receipt is the provenance, and a `*.captured.json` is
  never hand-edited to match it.
- The `command`, `capture_record` and `not_recaptured.evidence` paths point into the task's notes, outside
  the repository. They are task-local evidence with an expiry: once removed, re-capturing means re-creating
  an equivalent producer, and the receipt remains the record of what was run.

### Invariants And Boundaries

- **A listed fixture's sha256 must match its file.** A re-capture that changes a fixture replaces its row.
- **Producer facts and worker statements stay separate.** The `not_recaptured` section is not producer
  output, and it must not be read as a claim that the listed fixtures are current route bytes.
- **Test evidence only.** The receipt grants no production knowledge authority and certifies no mounted
  behaviour.

### Todos

The five fixtures named under `not_recaptured` still pin pre-change route states; re-capturing them from
the current route, or retiring them with a recorded reason, is open work outside this file, together with
the dashboard cases that currently assert those older states.

## Docs References

No Domain Documentation source is configured; the receipt and the fixtures it binds are local test
evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The rows name the receipt's own keys and the case headers that point at it.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The run-level provenance: source tree, time, command, route and capture record.** | "captured_source_tree"; "capture_record_sha256" | dashboard/src/panels/review/familyReview.capture-provenance.json:2-7 |
| **How a build was accepted: the selection rule, the structural signature and the attempts per group.** | "selection_rule"; "signature"; "attempts" | dashboard/src/panels/review/familyReview.capture-provenance.json:8-15 |
| **The two re-captured fixtures with their digests, scenarios, requests and normalization.** | "familyReview.complete.captured.json"; "familyReview.identical.captured.json" | dashboard/src/panels/review/familyReview.capture-provenance.json:16-35 |
| **The worker-stated section naming the fixtures that were not re-captured, the reason, and the evidence.** | "not_recaptured"; "stated_by" | dashboard/src/panels/review/familyReview.capture-provenance.json:36-52 |
| The workspace case header that points at this receipt and states which fixtures it covers. | "familyReview.capture-provenance.json" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:8-19 |
| The read-cycle case header that points at this receipt for the paging fixture it did not re-capture. | "familyReview.capture-provenance.json" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:13-19 |

## Cross-Repo References

The producer command and evidence paths name task-local files in the coordination workspace; they are
provenance pointers, not a repository or system boundary this fixture depends on at test time.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional production cross-repository contract is asserted. | — | — |

## Update History

- 2026-09-28T16:42:25+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): created this one-to-one card for the family-review capture receipt added when `complete` and `identical` were re-captured from the real route so their member sources carry the structured locator fields; it records the run-level provenance, the acceptance rule, the two re-captured rows and the worker-stated `not_recaptured` section, following the sibling `subjectReview.capture-provenance.json` card. The file is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf base and the verified basis is the working-tree delta on top of it; the closeout records the real commit.
