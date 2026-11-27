# skills/l-01-agent-lifecycles/operations/review.md

## Rounds and record-only repair

`operations/review.md` keeps separate CODE and MEMORY review lanes under the settings limit (beyond-limit rounds need recorded Architect/developer approval; clean syncs open no round). Unchanged-candidate record-only rechecks, round-limit verification, post-seal `addedFindings`, and `OM-6`/`cutCards`/`addedFiles` memory-review rules live in Tier-2 `reference/review/rounds-and-late-findings.md`.

## Message/file transport

Message-file payload rules live in `reference/message-handover.md`; `operations/review.md` directs direct peer verdict/list handovers and the single ready-for-closeout notice to Manager after code PASS, memory PASS, and settled final checks.

On consolidation leaves (`consolidationList` present), review runs in the memory lane only (no code review round); findings and PASS verdicts hand directly between Reviewer and Consolidator, and ready-for-closeout goes to Manager once memory PASS settles.

## Governing Overview

[overview](../overview.md)

## Purpose

Independent review that runs only when requested: one pass/block recommendation per requirement with coverage, findings and checks, handed directly to the Worker — and code PASS directly to the Curator — with the memory check kept as a separate sealed lane.

## Code Commentary

An Architect-only note routes advisory independent review commissioning and findings routing to `reference/review/advisory-reviews.md`. In leaf reviews, a baseline covers the complete candidate diff and reruns/repeats the Worker's focused-test search; fix-verification checks only sealed outstanding IDs (returning repair freezes missing per-finding entries without counting a round). Clean syncs open no round. Ordinary rounds follow the live settings limit; beyond-limit work requires recorded Architect-or-developer approval. MEMORY uses `begin_review`/`record_review` with `reviewKind=memory`, separate sealed reports/IDs/count, and never opens or resets CODE. After code PASS, memory PASS, and settled final checks, the Reviewer sends Manager one ready-for-closeout notice with the passed freeze, both verdicts, and final-check evidence. Reviewer-scoped `## Boundaries` text directs answering Curator code concerns directly even after code PASS.

## Current composition and authoring contract

Audience markers separate the Architect-only advisory-review pointer (`<!-- ar:roles architect -->`), Reviewer-only intake/handover/code-concern steps (`<!-- ar:roles reviewer -->`), and all-role review-round and lane rules (`<!-- ar:roles all -->`). Detailed non-leaf seams, advisory reviews, round-limit/record-only rechecks, post-seal routes, and memory-change (`cutCards`/`addedFiles`/`OM-6`) checks live in `reference/review/*.md`.

## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.

- On leaf code PASS, Reviewer first tells Manager to start Curator, then hands the verdict directly to Worker and the passed freeze/verdict to Curator once that seat exists. Memory review and its verdict stay direct and separate. [1]



- Fix-verification checks the sealed outstanding IDs; ordinary rounds follow the settings limit and extras need recorded Architect-or-developer approval. [2]




- Reviewer does not implement, accept tasks, start roles or publish Git. It records its ordinary review begin/result; separately recorded MEMORY reports, IDs and pass counts do not reset CODE, and scoped record-write recovery retains its own conditions. [3]




- A record-only repair is checked on the last recorded round only when every candidate finding is closed and candidate bytes are identical; begin_review is not called and the count stays. A repair that changes the candidate uses the ordinary next round; a clean sync with passing focused tests sends no new freeze and begins no round (with the Manager obtaining the Curator's read for a changed pair before routine closeout). Fix verification within the settings limit is an ordinary round; a beyond-limit round needs recorded architect/developer approval. Separate MEMORY reports/counts do not reset CODE. [4]


- Reviewer returns a repair freeze missing its per-finding entries without counting a round, and receives no new freeze or round for a clean sync (where the Manager obtains the Curator's read for a changed pair before routine closeout). [8]



- The authored source owns this contract; the distribution copy is not a separate authority. [5]




- Current review separates common output/round/boundary rules from Architect advisory-review routing and Reviewer handover and code-concern duties, records MEMORY as a separate lane under the same settings limit, and delegates record-only repair checks to reference/review/rounds-and-late-findings.md. [6]




- A baseline review reruns and repeats the Worker's focused-test search, and fix-verification applies it to the repair's own names. [9]
