# skills/l-01-agent-lifecycles/criteria/code-seam.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/criteria/code-seam.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T12:08+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[skills/l-01-agent-lifecycles overview](overview.md)

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
| The quiescence executable counterpart (absent-developer fixed-point probe). | `test_unacked_backlog_reaches_a_fixed_point_with_absent_developer` | mcp/tests/test_agent_notifier_ladder.py:691-750 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository reviewer doctrine only. | — | — |

## Update History

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: created this sidecar and recorded the
  coalescing-invariant wording change (`rung` → `attempt`; the timed escalation ladder is
  retired while the storm history remains catching evidence). Verification metadata pinned
  until closeout stamps the 260713-TES-L5 commit.
