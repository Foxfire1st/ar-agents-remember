# dashboard/src/cockpit/PaseoChatFrame.retry.test.tsx

## Governing Overview

[Governing overview](../overview.md)

## Purpose

The mounted tests exercise transient open failures on a ready Operations chat frame.

## Code Commentary

The cases check bounded retry for the same document and agent, cancellation on target changes, and a fresh ready notification that resumes the matching pending open.

## Relationships

The frame controller owns retry state and timing. The tests drive its exposed behavior through the mounted frame.

## Evidence

- The retry cases exercise ready binding, cancellation and terminal settlement. [1]
