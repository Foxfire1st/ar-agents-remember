# dashboard/src/cockpit/PaseoChatFrame.retry.test.tsx

## Governing Overview

[Governing overview](../overview.md)

## Purpose

The mounted tests exercise transient open failures on a ready Operations chat frame.

## Code Commentary

The cases check bounded automatic retry for the same document and agent, cancellation on target changes, a fresh ready notification that resumes the matching pending open, explicit Retry on `paseo-frame-agent-problem` (resending `ar.open` without reload when ready and reloading when unavailable), and non-reloading re-sync when `active` flips from false to true with an unshown target.

## Relationships

The frame controller owns retry state and timing. The tests drive its exposed behavior through the mounted frame.

## Evidence

- The retry cases exercise bounded transient retry, cancellation, terminal settlement, ready/unavailable problem Retry, and reveal re-sync without reload. [1]
