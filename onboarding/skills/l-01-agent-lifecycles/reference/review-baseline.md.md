# skills/l-01-agent-lifecycles/reference/review-baseline.md

## Governing Overview

[overview](../overview.md)

## Purpose

The Reviewer's detail for a baseline review: partitioning routes, checking evidence, telling recorded knowledge from findings, sealing the first review's findings and selecting focused tests.

## Code Commentary

The Reviewer organises route work itself, with sub-agents if its harness offers them; no harness arrangement is required. Baseline runs the bound catalogs, required routes and exploratory mandate, covers all three lenses explicitly (completion against task documents, scoped implementation evidence, onboarding against code) and tries to refute each claim before confirming it. Evidence must match the requirement's class: mounted user interface proof for rendering or visibility, operation-level proof for scheduling or ordering, the parsed artifact for a persisted shape, and the file plus its enforcing mechanism for doctrine; wrong-class evidence is a finding and cannot support PASS.

A weakness record or a document's staleness is never a finding: an out-of-scope weakness and a document standing on changed code are recorded knowledge and refuse no review, gate or closeout. An unrepaired in-scope weakness is a finding, as is a changed document whose dependent record is not confirmed, and a weakness record never substitutes for such a finding. An empty first-pass issue list is a valid terminating baseline. Focused tests are chosen across every changed surface and relevant gate; full-suite authority stays in the Reviewer role's inspection section, which points here before a baseline review.

## Evidence

- Route work is organised by the Reviewer with optional harness helpers. [1]
- All three lenses are covered and evidence must match the requirement's class. [2]
- Weakness records and document staleness are recorded knowledge, not findings, except in-scope unrepaired weaknesses and unconfirmed dependents. [3]
- An empty first-pass list terminates the baseline; focused tests cover every changed surface, with full-suite authority in the role. [4]
- The Reviewer role points here before preparing a baseline review. [5]
