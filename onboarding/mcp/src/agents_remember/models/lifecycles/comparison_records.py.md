# mcp/src/agents_remember/models/lifecycles/comparison_records.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Retains assessment-availability facts in immutable historical comparison manifests without restoring a review dashboard channel.

## Code Commentary

`ComparisonAssessmentAvailability.records` admits only `assessments`. It retains owner, availability state, optional count, detail, unreadable identities and next action. `recorded` and `none_recorded` must carry counts, respectively positive and exactly zero. `unavailable`, `not_measured` and `not_selected` must carry no count and must name a nonblank next action.

This narrow lifecycle value preserves the distinction between an owner’s measured empty collection and an unanswered collection. It is not the removed multi-class `ReviewRecordChannel`: evidence claims, observations, detection and assessment-currentness channels are not admitted here.

## Invariants And Boundaries

Historical assessment publication and immutable comparison decoding remain separate from present intent-review display. The value performs no reading, counting, currentness measurement or endorsement, and is not a relocated implementation of the deleted dashboard channel.

## Evidence

- Only assessment availability survives here; count/state/next-action combinations are constructor-checked. [1]

- Immutable manifests retain optional captured assessment availability, omit it from old canonical encoding when absent, and check its count against bound assessments. [2]
