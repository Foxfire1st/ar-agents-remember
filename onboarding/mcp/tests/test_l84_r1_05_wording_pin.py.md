# mcp/tests/test_l84_r1_05_wording_pin.py

## Governing Overview

[overview](overview.md)

## Purpose

Pins individual lifecycle wording that must stay exact: the correct-write hand-write sentence in every carrier, manifest steps derived from their pointers, and a few rules that must stand once in their source homes.

## Code Commentary

- **Hand-write sentence.** `SENTENCE` ("If no admitted route works, record the refusal, tell the owner, then make that write openly by hand and log it; never keep a blanket ban on writing it by hand.") must stand exactly once, directly after "before applying a stop.", in each of `CARRIERS`: `core/authority.md` and `core/every-role.md` in the canonical and packaged lifecycle trees, `cli/role_launch_preparation.py` and `docs/reference/settings-json.md` (compared with line wrapping undone). Removing either half fails the pin, and every carrier also names the same tool and input class.
- **Manifest steps.** In both trees every step-detail reference declares a step, and each declared step and audience equals the one `manifest_mismatches` derives from the first-message sentences that link the file; an invented step or role fails. No reference description mentions a refused push or starts with "Named-step".
- **Digest map.** A `core/` unit listed in `core/digest-map.json` does not link to its own place in `every-role.md`.
- **Source homes.** `core/invariants.md` defines a guard as a check that refuses, holds back or switches off an operation; `core/authority.md` names sandbox versions and harness-created files; the two sandbox rules stand once each in `core/authority.md` and `core/every-role.md` and not in `reference/sandbox-actors.md`; the Reviewer role keeps its repair-and-continue rule and its stops.

## Evidence

- The hand-write sentence is spelled once. [1]
- The carriers are the canonical and packaged core files, the launch preparation and the settings reference. [2]
- The sentence is pinned once in every carrier and fails when cut. [3]
- Core unit sources do not link their own digest place. [4]
- Manifest steps and audiences equal the pointer-derived actions. [5]
- The source homes carry the Architect wording. [6]
- The sandbox rules hold once in each home and not in the sandbox detail. [7]
- The Reviewer's repair-and-continue rule is pinned. [8]
- Every carrier names the same tool and input class. [9]
