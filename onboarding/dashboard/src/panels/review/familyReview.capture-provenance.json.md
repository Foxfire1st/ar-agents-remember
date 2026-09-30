# familyReview.capture-provenance.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.capture-provenance.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:52:00+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c` |
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[overview.md](../overview.md)

## Purpose

**The capture receipt for the `familyReview.*.captured.json` route bodies and `familyPaging.captured.json`.** It
binds each re-captured family-review fixture to the exact producer run that wrote it: the earlier run that wrote
`complete` and `identical`, and, since MIK-L31, a second, worker-stated run (`mik_l31_recapture`) that re-captured
the six fixtures the earlier receipt had listed as not re-captured (MIK-R31 rule 6, the L44-R1-F5 remainder). The
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

**`mik_l31_recapture` replaced the earlier `not_recaptured` section (MIK-L31).** The earlier section, stated by
the ICR-L44 worker, explained that the current route cannot emit the committed shapes (since L38 a roster page
also carries the member revisions its content and claim items represent) and left six fixtures at their old
bytes. MIK-L31 re-captured them instead of retiring them: `stated_by` names the MIK-L31 worker; the run's
`captured_source_tree` is `18b77329` (the L10-synced tree) and `captured_at` 2026-09-30T04:17:22Z; `command` runs the
task-local `recapture_family_fixtures.py` against the worktree; `route` is `GET /api/review/intent` over HTTP under
uvicorn; the `producer` is L44's, unchanged except for the selection rule and output paths; **`selection_rule`
accepts the first build of each scenario and matches no signature**, and `attempts` records one build per group
(`bounded`, `one-sided`, `paging`, `walk`, `empty`); `capture_record` and `capture_record_sha256` bind the
per-request record; `why` states that each fixture is now the current route's body with the member-source fields
`locator`, `resolved_ranges` and `locator_state`, and that the dashboard expectations were updated to them. One row
per fixture (`truncated`, `continued`, `oneSided`, `familyPaging`, `walkFinal`, `emptyRoster`) gives its sha256,
scenario and requests; the `continued` body continues the `truncated` body's retry-budget-family after-side cursor.
A `tree_note` records that the later L05 sync touches no review-route module (review R2-4).

### Conventions

- Fixture bytes come only from the producer; this receipt is the provenance, and a `*.captured.json` is
  never hand-edited to match it.
- The `command`, `capture_record` and `not_recaptured.evidence` paths point into the task's notes, outside
  the repository. They are task-local evidence with an expiry: once removed, re-capturing means re-creating
  an equivalent producer, and the receipt remains the record of what was run.

### Invariants And Boundaries

- **A listed fixture's sha256 must match its file.** A re-capture that changes a fixture replaces its row.
- **Producer facts and worker statements stay separate.** The `mik_l31_recapture` section is the MIK-L31
  worker's statement of a producer run; the first-build selection rule means each body is one draw of fresh
  identities, so counts that depend on the draw are read from the body by the consuming cases (review F7).
- **Test evidence only.** The receipt grants no production knowledge authority and certifies no mounted
  behaviour.

### Todos

- **Resolved by MIK-L31:** the six fixtures are re-captured from the current route and the dashboard cases assert
  its states (the one branch no real body reaches is covered by a labelled SYNTHETIC body, ruling Q3).
- The consumer headers (`ReviewWorkspace.family.test.tsx`, `ReviewReadCycle.family.test.tsx`) were refreshed to
  name `mik_l31_recapture` (a comment-only follow-up).

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
| **The earlier run's provenance: source tree, time, command, route and capture record.** | "a8039b8e036e2c0d83100e9b4683901d6d54bd0d"; "aeae0851e110a5244ccebfa34555479662e2e8e6a5a611695e3a167be5fb0172" | dashboard/src/panels/review/familyReview.capture-provenance.json:2-7 |
| **How the earlier run accepted a build: the structural signature and the attempts per group.** | "until every route body it produced carried the committed capture's structural signature" | dashboard/src/panels/review/familyReview.capture-provenance.json:8-15 |
| **The two re-captured fixtures with their digests, scenarios, requests and normalization.** | "familyReview.complete.captured.json"; "familyReview.identical.captured.json" | dashboard/src/panels/review/familyReview.capture-provenance.json:16-35 |
| **The MIK-L31 worker-stated re-capture: source tree, time, command, route, producer, first-build selection, one attempt per group, the capture record and why.** | "mik_l31_recapture"; "the first build of each scenario is accepted (MIK-L31); no signature is matched" | dashboard/src/panels/review/familyReview.capture-provenance.json:36-53 |
| **One row per re-captured fixture, and the tree note.** | "familyReview.truncated.captured.json"; "familyPaging.captured.json"; "familyReview.emptyRoster.captured.json"; "tree_note" | dashboard/src/panels/review/familyReview.capture-provenance.json:54-123 |
| The workspace case header that points at this receipt and names both captures, the MIK-L31 one as `mik_l31_recapture`. | "familyReview.capture-provenance.json"; "mik_l31_recapture" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:9-21 |
| The read-cycle case header that points at this receipt for the re-captured paging fixture. | "familyReview.capture-provenance.json"; "re-captured by MIK-L31 with ICR-L44's" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:22-28 |

## Cross-Repo References

The producer command and evidence paths name task-local files in the coordination workspace; they are
provenance pointers, not a repository or system boundary this fixture depends on at test time.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional production cross-repository contract is asserted. | — | — |

## Update History
- 2026-09-30T10:52:00+02:00 — 260928-MIK-L31 curator (follow-up after the L31 worker's comment-only edits, staged; the change set is now 46 files over `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`): **resolved Todo:** the two consumer headers now name `mik_l31_recapture` (the worker's comment-only follow-up). The Todo bullet says so, and the two consumer-header rows are reworded and re-measured (`ReviewWorkspace.family.test.tsx:8-19` → `9-21`, `ReviewReadCycle.family.test.tsx:26-26` → `22-28`).
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. The `not_recaptured` section is gone: MIK-L31 re-captured the six fixtures (MIK-R31 rule 6, the L44-R1-F5 remainder) and recorded the run as `mik_l31_recapture` (first build accepted, one attempt per group, source tree `18b77329`, review F7 and R2-4). Purpose, Logic, an invariant and the Todos (now resolved, plus the stale consumer headers) are rewritten. **Claims re-anchored:** the `not_recaptured` row is replaced by two rows on the new section; the two consumer-header rows are reworded (this pass's generated bullet for the read-cycle row removed); the earlier run's two rows are re-anchored on values that occur once, since the new section repeats their key names.

- 2026-09-28T16:42:25+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): created this one-to-one card for the family-review capture receipt added when `complete` and `identical` were re-captured from the real route so their member sources carry the structured locator fields; it records the run-level provenance, the acceptance rule, the two re-captured rows and the worker-stated `not_recaptured` section, following the sibling `subjectReview.capture-provenance.json` card. The file is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf base and the verified basis is the working-tree delta on top of it; the closeout records the real commit.
