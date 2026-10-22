# dashboard/src/panels/detail-panel/order-block.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin inline sprint wave rows and master task Order/ready-next rows, whole graph navigation and shared delayed pointer marking.

## Code Commentary

Cases use entry stage/activity for Order state, not graph in-flight labels. The parameterized works/paused/unknown control requires each started unit exactly once: works in now, paused/unknown in its dependency wave, with the common status word and no duplicate done row. Every started Order unit has the golden `work` accent for works, paused and unknown activity, while its common status word remains activity-aware (`started` for unknown). The legend says `in work`; other wave units retain distinct ready/waits accents. Graph readiness stays a separate data-readiness annotation. Controlled time distinguishes pass-through pointers from rested selection; neighbor movement retains the prior mark until the next rest, keyboard focus marks immediately, and reduced motion drops the fade rather than the rest. The master case keeps Order after Now, graph-ready planned L2 under Can start next, L3's served planned word and major progress, relation text and exact taskdoc navigation. Mixed/all-completed cycle fixtures retain all marked member titles where an unfinished wave exists and hide completed entry marks; all-completed cases have neither a wave nor a ready-next block. These are seeded component assertions, not native graph/SCC opportunities or a Curator test run.


**L184 — INV-XZYGEB.** The block is one of the places a task's word is shown, so its test holds the word's behaviour in place. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Boundaries

This card describes the executable assertions and fixture seams of this module. It does not turn a mocked or seeded unit observation into system-wide acceptance. Keep fixture provenance, controlled time and actual producer opportunities explicit when extending the cases.

## Evidence

- Sprint display/whole-graph and rest/focus/reduced-motion assertions remain; the seeded master case pins placement, ready-only next tasks, projected progress, relation text and exact navigation. Source inspection only. [1]

- Seeded mixed/all-completed cycle assertions name both legacy members where a wave remains, hide completed entry marks and require no separate done row, and omit an all-completed wave and ready-next block. This is not a native SCC producer opportunity or new execution. [2]

- Parameterized Order cases pin the started work accent independently of the activity word, the restored legend, and distinct ready/waits wave accents. This is source assertion coverage, not a fresh execution. [3]
