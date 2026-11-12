# skills/l-01-agent-lifecycles/criteria/report-verification.md

## Governing Overview

[overview](../overview.md)

## Purpose

Canonical report-verification catalog for an assigned adversarial review and for the loop owner verifying a builder round. It checks reports, owner claims and handover summaries against artifacts. Report verification is standing across the review types in the reviewer binding table; the catalog itself does not make review a routine closeout or integration prerequisite.

## Code Commentary

### Logic And Boundaries

The standing criteria are RV-1, RV-2, RV-4, RV-5 and RV-6; RV-3 remains a candidate. RV-1 opens the artifact behind each claim and forbids sampling the load-bearing ones. A complete-tree claim checks content and mode rows in the same filesystem view, including executable-bit changes that content-only diffs miss.

The same complete-tree claim covers every nonignored untracked path using NUL-delimited or equivalently path-safe enumeration. Inspection is no-follow: record type, numeric mode, executable significance and intention; regular files get size and bounded escaped text or a binary/sensitive classification with hash; symlinks get link text without dereference; directories and special objects need an explicit disposition. Races or inaccessible objects are disclosed and a consistent view is re-established, never silently skipped. This is semantic evidence work, not another verifier or authority to dump sensitive bytes.

RV-2 enumerates the whole sibling class behind an instance-level finding. RV-4 preserves scope-expanding owner supplements and load-bearing builder disclosures in the task decision log, not only a report. RV-5 proves the exact invocation's resolved source/import path and task/contract are the reviewed artifacts; a green result from a different editable install or a command refused before output is not evidence for the change set.

RV-3 asks whether a partial fix made claims about the changed artifacts false elsewhere. It runs under baseline exploration with one recorded catch. Baseline exploration, the limits of fix-verification and promotion follow the shared catalog review rules in `criteria/code-seam.md`. RV-6 is standing by direct requirement and only a developer ruling can demote it: a report calling a check complete or the gate names what ran and what was left out, a pre-existing failure must fail on the base for the same message and subtest, and a carried run stays valid only while the files it exercises are byte-identical. The catalog's catching counts and environment examples are not fresh executions or automatic lifecycle prerequisites.

## Evidence
The rows cite canonical source text and narrowly relevant neighbor definitions. A historical example or declared check remains distinct from a check result. The packaged source is a propagation twin, not an independent authority.

- The canonical catalog owns report-verification doctrine rather than the generated bundle. [1]

- The generator retains a target record type; this declaration is not a fresh synchronization check. [2]
- The current generator derives skill targets from the checkout declaration rather than an old TARGETS constant. [3]

- The reviewer binding table includes report-verification in every listed review type. [4]

- RV-1 requires artifacts behind claims and checks both content and mode in the same filesystem view. [5]

- RV-1 adds path-safe untracked enumeration, no-follow inspection, bounded content and explicit race/intent handling. [6]

- RV-2 enumerates sibling classes; RV-4 records load-bearing disclosures in the decision log. [7]

- RV-5 proves the resolved invocation source and contract rather than trusting nominally canonical commands. [8]

- RV-3 remains a candidate; baseline exploration and promotion, under the shared catalog rules, do not expand sealed fix-verification. [9]

- RV-6 is standing by requirement beside RV-1, RV-2, RV-4 and RV-5; RV-3 remains a candidate. RV-6 checks what a claimed complete or gate run included and omitted, requires the same message/subtest cause on the base before a failure is called pre-existing, and permits carried evidence only when the files it exercises remain byte-identical to the earlier run. [10]
