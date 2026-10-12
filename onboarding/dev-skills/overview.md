# dev-skills Overview

| Field | Value |
|---|---|
| sourceRoute | `dev-skills` |
| onboardingRoute | `dev-skills/overview.md` |
| parentOverview | [`overview.md`](../overview.md) |

## Governing Overview

[Repository overview](../overview.md)

## Purpose

`dev-skills/` holds developer-only Claude Code skills for building and reviewing Agents Remember itself. These internal tools are kept in the repository but are not distributed to Agents Remember users. User-facing skills belong in the canonical `skills/` tree.

The current package, `dashboard-experience-review/`, reviews the cockpit dashboard from the user's perspective: it discovers workflow scenarios, detects missing views and places users get stuck, and judges UX and observability quality. It conducts installed design skills for the craft dimensions and emits findings; dashboard fixes are separate, gated build work.

## Hot Path Summary

Read `dev-skills/README.md` for the distribution and manual-install convention. Enter the dashboard review through `dashboard-experience-review/SKILL.md`; its companion methods, delegation map, and three templates define the analyses and outputs.

## How It Is Built

A dev-skill lives under `dev-skills/<name>/` with a `SKILL.md` entry point. The existing entry point has `name` and `description` frontmatter. The dashboard package contains the conductor, `owned-methods.md`, `delegation-map.md`, and three templates for the scenario catalog, review report, and missing-view matrix.

| Path | Role |
|---|---|
| `dev-skills/README.md` | The convention: dev-only, non-distributed, hand-installed |
| `dev-skills/dashboard-experience-review/` | The cockpit dashboard UX & workflow-gap reviewer skill |

The conductor scopes a live dashboard, discovers entities and workflow scenarios, observes the app, runs its owned analyses, delegates bounded craft dimensions, consolidates findings, and emits the report inline. It supports standalone review and review within an ongoing build worktree. Its output contract also refreshes the durable scenario catalog at `docs/design/dashboard/scenario-catalog.md`.

The owned methods cover cognitive walkthroughs, missing views and states, observability parity, motion as communication, terminal control-plane UX, and information scent and progressive disclosure. The delegation map supplies the craft assignments and constraints. The templates connect scenario steps and forced UI states to coverage matrices, a ranked missing-view backlog, severity-rated findings, and delegated outputs by reference.

To use a dev-skill, copy its folder into a harness skills directory, such as `~/.claude/skills/` or the repository-local `.claude/skills/`, and restart the harness as instructed by the README. This is a manual installation convention, not a package distribution route.

| File | Role | Why It Matters | Onboarding |
|---|---|---|---|
| `dev-skills/README.md` | convention | Declares the distribution boundary and manual-install procedure; distribution and onboarding inclusion are distinct | covered |
| `dev-skills/dashboard-experience-review/SKILL.md` | skill conductor | Entry point and pipeline for the dashboard review | covered |

### File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
|---|---|---|---|
| `dev-skills/README.md` | [`README.md.md`](README.md.md) | covered | convention |
| `dev-skills/dashboard-experience-review/SKILL.md` | [`dashboard-experience-review/SKILL.md.md`](dashboard-experience-review/SKILL.md.md) | covered | conductor |
| `dev-skills/dashboard-experience-review/owned-methods.md` | [`dashboard-experience-review/owned-methods.md.md`](dashboard-experience-review/owned-methods.md.md) | covered | analysis passes |
| `dev-skills/dashboard-experience-review/delegation-map.md` | [`dashboard-experience-review/delegation-map.md.md`](dashboard-experience-review/delegation-map.md.md) | covered | delegate map |
| `dev-skills/dashboard-experience-review/templates/scenario-catalog-template.md` | [`dashboard-experience-review/templates/scenario-catalog-template.md.md`](dashboard-experience-review/templates/scenario-catalog-template.md.md) | covered | template |
| `dev-skills/dashboard-experience-review/templates/review-report-template.md` | [`dashboard-experience-review/templates/review-report-template.md.md`](dashboard-experience-review/templates/review-report-template.md.md) | covered | template |
| `dev-skills/dashboard-experience-review/templates/missing-view-matrix-template.md` | [`dashboard-experience-review/templates/missing-view-matrix-template.md.md`](dashboard-experience-review/templates/missing-view-matrix-template.md.md) | covered | template |

There are no child overviews in this route. The dashboard skill is covered here and by its file-level onboarding. When changing a file, read this overview and that file's onboarding, then confirm the relevant current source.

## Invariants And Boundaries

`scripts/sync-skills.py` copies the canonical `skills/` tree into fixed MCP package-data and harness starter targets. It does not copy `dev-skills/`. Its `--check` operation compares those targets with `skills/`; it does not inspect the `dev-skills/` source tree. A manually installed folder inside a checked target can nevertheless be reported as extra target content.

Do not add a dev-skill to the sync targets or move it into `skills/` without deciding that it should ship to users. Changes under this route remain outside that distribution flow and are used through manual installation.

| Nearby Thing | Belongs Instead In |
|---|---|
| User-facing / shipped skills (synced to harnesses) | `skills/` |
| Product design docs (scenario catalog, doctrine) | `docs/design/` (excluded by the inspected memory settings) |

Distribution and onboarding scope are separate boundaries. Existing onboarding Markdown and JSON sidecars cover this route, but the inspected memory `system/settings.json` does not list `dev-skills/**` among its include paths. The source README likewise says this tree is outside the include scope, then incorrectly infers that no onboarding sidecars exist. Existing cards establish coverage already present; they do not establish current inclusion or provider indexing. Retain the existing coverage unless the owner separately changes inclusion policy; this overview does not change that policy or claim provider indexing.

Dashboard review findings must be grounded in the live system and observed views. The skill requires settled-beat observation to avoid mistaking transient animation states for absent controls. Delegates remain findings-only, and an unavailable delegate is reported as a coverage gap rather than silently skipped. The review package's named tools and installed-skill inventory describe its instructions and dependencies, not proof that those dependencies are available in a particular session.

If another dev-skill is added, whether the dashboard package needs a child overview remains an open organizational question; the current overview does not impose that split.

The source skill identifies the scenario catalog and review doctrine under `docs/design/dashboard/`; both paths exist in the current checkout. They are related design documents outside the inspected onboarding include scope. No cross-repository evidence is used here.

## Evidence

- `sync-skills.py` copies only `REPO_ROOT/"skills"` into its fixed targets, so `dev-skills/` is outside this distribution flow. Checking compares the canonical tree with target contents, so an independently copied dev-skill inside a checked target can be reported as extra; this does not inspect the `dev-skills/` source tree. [1]
