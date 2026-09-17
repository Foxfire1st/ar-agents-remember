# skills/l-01-agent-lifecycles/criteria/code-seam.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/criteria/code-seam.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-07T00:34+02:00 |
| lastVerifiedCommitHash | `997305a9ced4caea67edb826224bf0351264fd56` |
| lastVerifiedCommitDate | 2026-09-17T19:54:27+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[skills/l-01-agent-lifecycles overview](../overview.md)

## Purpose

The `code-seam` reviewer criterion: verify production wiring end to end, hunt fail-open
shapes, require validate-then-mutate, and prove quiescence (D1-D4) when a change touches a
reusable primitive or a feedback actor. It is the criteria-catalog home of the
escalation-storm catching evidence and the "no event, message, or row outranks system
health" ruled invariant.

## Code Commentary

### Logic

The criterion's D4 quiescence question demands a multi-cycle zero-input simulation for any
feedback actor whose output is a member of its own input class. Its ruled invariant says
notification rows coalesce — a re-firing condition updates its ONE existing row (date, tries,
attempt) and never appends a sibling. The catching evidence records the 2026-07-09
escalation-storm meltdown (every ladder rung transition minted a new pending row) as the D4
seed and the HFX2-L7 O(n^2) re-fold as the scaling seed.

### Conventions

Criterion files are reviewer-facing doctrine: candidate criteria get promoted with a second
catching engagement, and catching evidence must name the exact leaf/commit that caught the
defect class.

### Invariants And Boundaries

- The coalescing invariant is doctrine: one row per root cause, purgeable stores, and the
  durable artifact on disk never being the queue row.
- Since 260713-TES-L5 the wording says "date, tries, attempt" — "rung" is gone with the
  retired escalation ladder; the escalation-storm history stays as catching evidence, not a
  live mechanism.

### Todos

None.


## CCR-R12@v5 Review Scope

This criteria catalog supplies evidence only when the corresponding review is explicitly requested. It does not create a closeout or integration prerequisite; routine handoff uses the worker and curator targeted/scoped check records and preserves any failed or not-run state.

## Docs References

No relevant external documentation found after checking the resolved source registry; the
reviewer criteria catalog and the cited catching leaves are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this criterion; catching evidence is leaf-cited. | `## Standing Criteria (MUST RUN — the regression floor)` | skills/l-01-agent-lifecycles/criteria/code-seam.md:10-12 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical criterion file's standing/candidate structure, mirrored into the packaged runtime copies. | `### CS-6 — Scaling & reclamation *(promoted — 2 catches)*` | skills/l-01-agent-lifecycles/criteria/code-seam.md:70-84 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository reviewer doctrine only. | — | — |


## Update History
- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **both governing declarations repaired.** The field named `overview.md` and the body link named `overview.md`; each resolved card-relatively to nothing, and they did not agree with each other. Both now name `../overview.md`, the route-local overview of this card's own directory. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-09-07T00:34+02:00 — Reconciled current source anchors and diagnostic/four-worker policy; removed obsolete test-proof claims without altering verification pins.


- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: created this sidecar and recorded the
  coalescing-invariant wording change (`rung` → `attempt`; the timed escalation ladder is
  retired while the storm history remains catching evidence). Verification metadata pinned
  until closeout stamps the 260713-TES-L5 commit.
