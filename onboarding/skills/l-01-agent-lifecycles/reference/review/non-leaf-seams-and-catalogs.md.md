# skills/l-01-agent-lifecycles/reference/review/non-leaf-seams-and-catalogs.md

## Governing Overview

[overview](../../overview.md)

## Purpose

Tier-2 review detail binding criteria catalogs to every review seam and defining master-exit, atomic-master integration, portfolio plan, and super-exit review procedures.

## Code Commentary

Maps all five review seams (organizational leaf route, atomic-master integration, master-exit, portfolio plan, super-exit) to their binding target, start leaf, and verdict recipient, forbidding review of a hosting leaf's enclosure candidate instead of the intake candidate. Assigns criteria catalogs solely from the six-row Review Type table (`code-seam.md`, `doctrine.md`, `onboarding-memory.md`, `report-verification.md`, `plan-review.md`) and requires recording catalog binding and conditional reasons in the verdict. Specifies affirmative non-sampled completion accounting (`addressed`, `delta justified`, `MISSING`) for master-exit, isolated branch diff review for atomic-master integration, Architect-brokered portfolio plan and super-exit reviews (no startable Reviewer seat), and non-leaf `BLOCK` decomposition rules (baseline blocks emit decomposable fix leaves; fix-verification blocks return only sealed IDs; integration branches are not repair workbenches).

## Relationships

Offloaded from `roles/reviewer.md` to keep the Tier-1 manual focused on the single leaf seam; absorbs retired `reference/review-master-exit.md` (verified by `test_l84_unique_detail_pointers_rules.py`). Registered in `composition-manifest.json` (`step_detail: true`), mirrored under `package_data/runtime/skills/`, and links all five files under `skills/l-01-agent-lifecycles/criteria/`.

## Evidence

- The seam and review-type tables bind each seam's target/start-leaf/recipient and fix exact required vs conditional criteria catalogs without brief or Reviewer overrides. [1]
- Master-exit, atomic-master integration, portfolio plan, super-exit, and non-leaf `BLOCK` rules require full item accounting (`addressed`/`delta justified`/`MISSING`) and decomposable baseline fix leaves. [2]
