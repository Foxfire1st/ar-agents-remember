# dashboard/src/cockpit/frameTrayChannel.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specify the tray/frame-channel contract through a mounted iframe window and the real PaseoFrameControl.

## Code Commentary

### Logic

Cases reject foreign origins/windows, malformed picks and missing message times, then deliver valid picks with page and message identity until unsubscribe.

Cases assert hello precedes tray wishes, wishes are deduplicated, heights are rounded and page-specific, non-picking plugins receive no tray messages, and stopped controllers receive no further updates.

Cases keep composer/pick reports per page until a fresh ready report, clear a notice only after a trusted pick, and follow shown-chat reports without posting navigation. The showing capability takes precedence over selection-based inference.

### Invariants And Boundaries

These are checked-in simulated frame/controller assertions, not a new browser/Paseo execution or test-run claim.

## Evidence

- Trusted pick admission and unsubscribe [1]
- Ready/capability/height/report lifecycle [2]
- Shown-chat observation without steering [3]
