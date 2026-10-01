# l-01-agent-lifecycles/templates/verdict.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

This template is the **adversarial reviewer's** artifact of the `l-01-agent-lifecycles` report-template library. It lands under the series `notes/reports/` directory and attaches to the handover gate as **judge evidence** at either of the two review seams — **master-exit** (before a manager hands to the orchestrator) and **super-exit** (before the orchestrator hands to the developer). The two variants now share rules but carry different review shapes because master-exit reviews one completed master branch while super-exit reviews the accumulated super branch.
**Single-source marker (260915-CAPS-L1):** the canonical template now states that it *shapes the
artifact and does not author the rules* — the reviewer's duties and the criteria-catalog binding live in
`../roles/reviewer.md`, the mode contract in `../operations/review.md`, and the adjudication and truth
boundary in `../core/acceptance.md`, and where wording differs those files win. Since 260703-L12 round 2 the template also serves three-party-loop reviews via the Loop-Review Adaptation note (master-exit shape minus the gate machinery; decider = the loop owner) and forces the criteria-catalog results the reviewer doctrine demands.

## Code Commentary

### Logic

The file is a sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical `skills/l-01-agent-lifecycles/templates/verdict.md`. It carries a prose header naming the writer (`roles/reviewer.md`), a numbered **Rules** block, and two fenced variants. The **Master-Exit Variant** records the master integration branch, master/leaf task docs, recommendation, decider, artifact path, and exact gate evidence ref (`kind=reviewer-verdict`, `ref=...`, `verdict=...`), then reviews completion against master task docs, code quality for the master branch, onboarding-vs-code for master-side sidecars/route overviews, ranked refute-tested findings, and manager fix leaves for a BLOCK. The **Super-Exit Variant** records the super branch, portfolio/master task docs, recommendation, decider, artifact path, and the same gate evidence ref shape, then reviews portfolio completion, whole-super branch quality, accumulated onboarding/carry-over/ledger coherence, ranked findings, and orchestrator-routed fix leaves for a BLOCK. As of 260703-L12 round 2 (L12R-3) BOTH variants carry a **Criteria Catalog Results** section (one row per bound criterion — Criterion id · catalog · Ran · Finding · Evidence — plus a proposed-amendments line for the promotion ratchet), Rule 6 makes reporting every bound catalog criterion mandatory (the binding table lives in `roles/reviewer.md`), and a closing **Loop-Review Adaptation** section defines the loop-review shape: the master-exit variant minus the gate-evidence row and Judge-Evidence Note, decider = the loop owner (owning seat / orchestrator for the plan review), delta-verifies appending a dated delta section to the same artifact.

### Conventions

Every finding is **refute-or-confirm**: it must survive an attempt to refute it, findings are ranked, and each cites a backing evidence file. All three lenses (completion · code quality · onboarding-vs-code) are covered explicitly, even to state a lens is clean. Regressions are checked against the past via route indexes, `cgc`, and `grepai`. The gate evidence reference is part of the artifact contract, not optional prose.

### Invariants And Boundaries

A verdict is **evidence, not a decision**: it states an explicit pass / pass-with-notes / block **recommendation**, and the gate's **decider** (manager, orchestrator, or developer per L4 policy) decides — the verdict is never written as if it were the gate outcome. A **BLOCK must decompose into fix leaves** (concrete, leaf-shaped findings the owning manager/orchestrator can dispatch); a block that cannot be named as fix leaves is invalid and resolves to pass-with-notes or names the leaves. Prose-only complaints are not a valid block.

### Todos

No TODO markers are present in this report template.


## CCR-R12@v5 Handoff Boundary

This template records the exact checks and their failed or not-run status as handoff evidence, together with the curator's complete memory-quality result. Closeout and integration consume the prepared code, memory-content, and ledger transaction and carry that completed curation as a prerequisite; full code quality, full tests, certification, and review are explicit requests rather than automatic template gates.

### Docs References

No external domain documentation applies to this repository-local report template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

This bundle copy is the shape the adversarial-reviewer job writes at each seam; its lenses cite the impact-analysis and onboarding-coherency backing reports.

- Sync-propagated bundle copy of the canonical templates source. [1]
- The adversarial reviewer writes this verdict at the master-exit and super-exit seams as judge evidence. [2]
- The master-exit completion and code-quality lenses name impact-analysis and quality/impact backing evidence. [3]
- The master-exit onboarding lens names a backing onboarding-coherency report. [4]
- The frame defines the evidence-not-decision doctrine in `core/loop.md` and `operations/review.md`, and the block-decomposes-into-fix-leaves doctrine in the reviewer role. [5]
- The adversarial reviewer writes this verdict at the master-exit and super-exit seams as judge evidence, and each seam's blocking rule returns fix leaves to its owner. [6]
- The two seams and the evidence-not-decision doctrine now live in `core/loop.md` and `operations/review.md`; the block-decomposes-into-fix-leaves doctrine lives in the reviewer role. [7]

As of cycle 4 the decider rows are ruled: master-exit = orchestrator (delegated master-handover-approval; serious issues escalate to the developer); super-exit = developer (human review concentrates at the super gate); the reviewer role file reference is roles/reviewer.md.

### Cross-Repo References

No sibling repository evidence is needed for this report template.

No meaningful cross-repo references found.

## 260815-DAG-L2 Verdict Scope

Master-exit verdicts carry execution nature and review the exact proposed organizational super
candidate or isolated atomic branch. The plan-review adaptation returns to the architect as loop
owner. Super-exit BLOCK packets name only owning/reopened or new scoped fix leaves; they cannot
send work to an integration ref. Option cells use rectangular Markdown-safe comma/or wording so
the report shape remains machine-checkable.

## 260815-DAG-L15 Review-Doctrine

Rule 7 now requires the reviewer seat to be distinct from the author seat and every requirement
verdict to cite evidence of the requirement's class — rendering → mounted-UI proof, scheduling →
operation-level proof, data model → artifact-level proof; a self-review or a wrong-class verdict
is a verdict-laundering finding. The Leaf Route-Review Variant gains the explicit "author seat"
row beside the reviewer-seat row.

## M38 Verdict Projection

Every verdict variant now repeats the mandatory stable-ID adjudication block. The reviewer records
its own inspection rationale and independently validates implementation/deliverable and
verification citations. Missing rationale, invalid or wrong-class evidence, or absent developer
approval rejects the row; no variant may pass with a rejected row. Evidence promotion remains a
separate disposition.
The reviewer rejects a missing or unapproved version-addressed packet or absent packet-local corpus
ruling before evaluating the rest of the acceptance envelope.

## M41-M43 Verdict Projection

The installed verdict appends an independent record against the exact worker attempt/candidate,
classifies rejection, preserves worker immutability, and separates regression proof from the
owning seat's bounded invalidation record.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.
