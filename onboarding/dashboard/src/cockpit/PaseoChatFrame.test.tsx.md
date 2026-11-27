# dashboard/src/cockpit/PaseoChatFrame.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The suite exercises the real dashboard frame component/controller/model and role-pane wiring with explicit backend/channel fixtures.

## Code Commentary

Grouped-navigation cases are removed with the dashboard's own sidebar (MIK-R75 rule 7). The remaining cases reject exact-origin/window lookalikes and malformed selection values, match pending agent replies, scope Parent errors to a currently selected source and exercise unavailable control/Retry; the companion plugin-side `paseoHierarchy.test.ts` cases, not this local suite, cover an unknown front source (no pill) and a known wide selection (pill returns). The recovery cases anchor post-load readiness timing to iframe `onLoad` (10 s deadline -> ping -> 10 s), verify the 45 s cold-load cap settles without reloading while accepting a late trusted `ready` (rejecting wrong origin/source), verify an unconfirmed URL-landed agent stays under a waiting notice with Retry while unavailable, and require an unanswered request ping before an open-request URL fallback; Retry remains explicit, and workspace moves retain generation. `paseoFrameLateAnswer.test.tsx` owns detailed late-ready, responsive late-open and post-recovery held-selection schedules. A deadline alone is not proof of a dead application.

The document-page preload case mounts an inactive pane with `preload`, reads its descriptor once and loads the Projects document page without an agent in the URL. Activating the same pane and delivering ready sends the selected agent and workspace through `ar.open`; the descriptor count, frame element and generation stay unchanged. The opt-in preload case is separate from the ordinary inactive pane that asks nothing before activation.

## Invariants And Boundaries

These fixtures establish source/component behavior, not live native failure transitions. Clipboard policy has its own browser e2e probe; neither suite implies whole-PNT qualification.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The workspace cases move by message without reload. [3]
- Opt-in hidden preload reads the descriptor once, names no agent in the initial URL and activates by message in the same frame generation. [4]

- The recovery fixtures anchor post-load readiness to onLoad, require unanswered request ping before URL fallback, keep waiting notice with Retry when unconfirmed, and preserve explicit Retry. [1]
- The no-second-load case pins that cold readiness timeout keeps generation 1 open and Retry reloads once. [2]
- Cold-load cap settles without reloading while rejecting wrong-origin/wrong-source messages and accepting a late trusted ready. [5]
