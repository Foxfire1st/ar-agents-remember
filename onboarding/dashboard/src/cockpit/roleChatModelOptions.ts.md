# dashboard/src/cockpit/roleChatModelOptions.ts

## Governing Overview

[Dashboard source](../overview.md)

## Purpose

Loads feature options for the launcher’s shown provider and model.

## Code Commentary

The pane waits for current catalogue metadata before requesting the resolved pair. It keeps each result for the current Refresh generation and deduplicates in-flight requests. A superseded result cannot update the current generation. The chosen model remains selectable while its options are pending. A new Start sends feature overrides only when the shown pair’s feature answer is fresh.

## Evidence

- Each request and cached answer is bound to the resolved pair and the active Refresh generation. [1]

- The pane requests its shown pair after current metadata. The Start dispatcher strips feature values when the pair lacks a fresh answer. [2]
