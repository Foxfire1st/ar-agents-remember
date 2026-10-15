# dashboard/src/dev/taskSkeletonDocs.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Provide explicitly invented DEV-only documents and supported response data for sprint, master and task reader demonstrations, without claiming coverage of every current block.

## Code Commentary

The exported rich document set contains a sprint, a master and tasks with enough statuses, progress, review, registers, decisions, references and graph edges to exercise the reader. Their text and approvals are made up. richApiAnswer answers only the developer demo's supported task-page requests from those invented documents. Leaf progress counts only major steps; completed leaves receive synthetic completedAt values. The rich master retains a made-up product_record alongside authored decisions. The rich task/master do not supply Non-goals, Acceptance, task waitsFor or a master Order graph; their dependency/order prose is invented fixture text, not evidence of the current authoring contract.

A sample count or recorded-looking approval here is fixture data, not a real native review or developer decision. This rich demo differs from the genuine older-producer recordings used by recovery tests.

## Boundaries

No real task document is read or authored. These fixtures do not establish API producer fidelity, native findings, landing or independent browser acceptance.

## Evidence


- The rich exports and supported API answers are invented; leaf counts/times and the retained master product record are fixture examples, not native proof. [1]
