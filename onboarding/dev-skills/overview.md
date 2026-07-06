# dev-skills Overview

| Field | Value |
|---|---|
| repository | agents-remember |
| doc_type | `route-local-overview` |
| sourceRoute | `dev-skills` |
| onboardingRoute | `dev-skills/overview.md` |
| parentOverview | [`overview.md`](../overview.md) |
| lastUpdated | 2026-06-23T05:31 |
| lastVerifiedCommitHash | `8e39b62c3550e974486479203d191aac39a0f0f3`|
| lastVerifiedCommitDate | 2026-06-23T06:11:39+02:00|

## What This Area Is

`dev-skills/` holds **developer-only, non-distributed** Claude Code skills — internal tooling for
building Agents Remember itself, not shipped to any AR user. Unlike the canonical `skills/` tree,
nothing here is copied by `scripts/sync-skills.py` into the MCP `package_data` or the harness starter
packages, and the pre-commit `sync-skills.py --check` gate never inspects it. A dev-skill is installed
by hand (copy its folder into a harness skills dir) when wanted. This route **is** in the onboarding
include scope, so its files carry sidecars; it is **not** in the distribution path.

## Hot Path Summary

`dev-skills/README.md` states the non-distributed convention; `dev-skills/dashboard-experience-review/`
is a conductor skill that reviews the cockpit dashboard like a user (scenario discovery, missing-view
detection, observability/UX judgment) and delegates craft dimensions to installed design skills.

## What Belongs Here

| Path | Role |
|---|---|
| `dev-skills/README.md` | The convention: dev-only, non-distributed, hand-installed |
| `dev-skills/dashboard-experience-review/` | The cockpit dashboard UX & workflow-gap reviewer skill |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
|---|---|
| User-facing / shipped skills (synced to harnesses) | `skills/` |
| Product design docs (scenario catalog, doctrine) | `docs/design/` (excluded from onboarding scope) |

## Structures Found Here

A `README.md` defining the tree's contract, and one skill package
(`dashboard-experience-review/`) made of a `SKILL.md` conductor, two companion docs
(`owned-methods.md`, `delegation-map.md`), and a `templates/` folder with three output templates.

## Operating Model

1. A dev-skill is authored under `dev-skills/<name>/` with a `SKILL.md` (same frontmatter shape as
   `skills/`).
2. It is **not** registered with `sync-skills.py`; it ships to nobody.
3. To use it, copy the folder into the harness skills dir and restart the harness.

## Main Flows

### Install a dev-skill by hand

1. Pick the skill folder under `dev-skills/`.
2. Copy it into `~/.claude/skills/` (or the repo-local `.claude/skills/`).
3. Restart the harness so it registers.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
|---|---|---|---|
| `dev-skills/README.md` | convention | Declares why this tree is outside the distribution + memory-include boundary | covered |
| `dev-skills/dashboard-experience-review/SKILL.md` | skill conductor | Entry point + pipeline for the dashboard review | covered |

## Local Invariants And Traps

- Never add a `dev-skills/` entry to `scripts/sync-skills.py` targets or move it into `skills/` unless
  you have decided it should ship to users.
- The distribution boundary (no sync / no package_data / no starter packages) and the onboarding-scope
  boundary are **separate**: this route is onboarded but not distributed.

## Repo-Internal References

The non-distribution guarantee is enforced structurally by the sync helper, which only copies the
canonical `skills/` tree — never `dev-skills/`.

| Finding | Citations | Source Path |
|---|---|---|
| `sync-skills.py` copies only `REPO_ROOT/"skills"` into its fixed targets, so `dev-skills/` is never distributed. | L14-L56 | [scripts/sync-skills.py](agents-remember/scripts/sync-skills.py) |

## Cross-Repo References

No relevant cross-repo evidence found.

## Docs References

No relevant documentation found.

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
|---|---|---|---|
| `dev-skills/README.md` | [`README.md.md`](README.md.md) | covered | convention |
| `dev-skills/dashboard-experience-review/SKILL.md` | [`dashboard-experience-review/SKILL.md.md`](dashboard-experience-review/SKILL.md.md) | covered | conductor |
| `dev-skills/dashboard-experience-review/owned-methods.md` | [`dashboard-experience-review/owned-methods.md.md`](dashboard-experience-review/owned-methods.md.md) | covered | analysis passes |
| `dev-skills/dashboard-experience-review/delegation-map.md` | [`dashboard-experience-review/delegation-map.md.md`](dashboard-experience-review/delegation-map.md.md) | covered | delegate map |
| `dev-skills/dashboard-experience-review/templates/scenario-catalog-template.md` | [`dashboard-experience-review/templates/scenario-catalog-template.md.md`](dashboard-experience-review/templates/scenario-catalog-template.md.md) | covered | template |
| `dev-skills/dashboard-experience-review/templates/review-report-template.md` | [`dashboard-experience-review/templates/review-report-template.md.md`](dashboard-experience-review/templates/review-report-template.md.md) | covered | template |
| `dev-skills/dashboard-experience-review/templates/missing-view-matrix-template.md` | [`dashboard-experience-review/templates/missing-view-matrix-template.md.md`](dashboard-experience-review/templates/missing-view-matrix-template.md.md) | covered | template |

## Child Overviews

None. The `dashboard-experience-review/` skill is covered by this route overview plus its file sidecars.

## How To Use This Area

When changing files under this route:

1. Read this overview.
2. Read the file-level onboarding for the file you are touching.
3. Remember the distribution boundary: a change here ships to nobody until hand-installed.

## Needs Verification

- [LOW] If a second dev-skill is added, consider whether `dashboard-experience-review/` should get its
  own child overview.

## Update History

- 2026-07-06T12:10+02:00 — No route impact: reviewed during the 260703-L10 one-vocabulary sweep — `dev-skills/` carries no retired lifecycle vocabulary (no `l-01-session-job-lifecycle`/`l-02` names, no dead phase axis), so nothing changed on this route.
<!-- newest first; append-only -->

- 2026-06-23T05:31 — Created the `dev-skills/` route overview when the slice was added to the onboarding include scope (issue #92).
