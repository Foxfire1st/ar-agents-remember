# skills/l-01-agent-lifecycles/operations/implementation.md

## Message/file transport

This canonical role/operation requires messages to be short wake-ups naming requested work or a handover and its files. Report, verdict, list and evidence contents travel through file-only `body` or existing-file `attach`, not pasted into message text. Within a shared task, files stay with its record and a leaf workspace exposes the message-folder link. Text uses the effective settings limit without a pinned number. The canonical source and generated copies share this contract; transport does not change their existing write/start powers, peer destinations or independent acceptance authority.

## Governing Overview

[overview](../overview.md)

## Purpose

The Worker's build contract: implement the leaf's primary requirement in the code worktree, leave one truthful report and one uncommitted candidate, freeze it, and hand it directly to the Reviewer — then the hand-off list directly to the Curator after code PASS.

## Code Commentary

`operations/implementation.md` (14 lines) defines the concise Tier-1 Worker implementation loop:
1. Pass coding-guidelines handover checks on a clean copy of the frozen bytes (name check/tree/result; search tracked tests for touched paths/names/rules/IDs; `## Final checks` wait for PASS).
2. Write one local report (`taskReportPath`, naming check/result/gaps and per-finding repairs), append Requirement Attempt Journal records, and regenerate the Curator list per freeze + `handoff-check` (`server_info`).
3. Ask Manager to start Reviewer at first freeze, then send freeze + journal directly to Reviewer (handover counts only on a reply naming the exact object; retry busy refusals).
4. Repair own-file sealed findings directly (no Manager go-ahead) with fast checks + focused tests, then re-freeze to the same Reviewer.
5. After code PASS, run `## Final checks` on the passed tree, record command/result/hash, and send to Manager + Reviewer; send the exact-freeze Curator list directly to Curator once started.
6. Manager notices cover first freeze, final checks, authority/recovery, and sync.

Clean-sync/overlap/memory-conflict procedures, measurement handovers, costly small repairs, post-PASS final-check failure repairs, and out-of-scope weakness/dependent recording live in Tier-2 `reference/worker/sync-and-repairs.md`.

## Current composition and authoring contract

The `ar:roles all` marker exposes the body to Worker alone (the only admitted role of this operation). Candidate-uncommitted, direct own-file finding repair, per-finding freeze reporting, clean-copy handover checks, and post-PASS `## Final checks` remain inline, while sync and exception procedures live in `reference/worker/sync-and-repairs.md`.

## Canonical Source Ownership

The byte-equal package copy is a distribution carrier, not an independent role, task or permission authority. Whole-file source evidence does not certify inherited statements, execution, grading or the whole card.

- Worker first tells Manager to start Reviewer at freeze, then hands that Reviewer the exact freeze and journal records directly once the seat exists. After code PASS and Curator start, its exact-freeze producer list goes directly to Curator. [1]


- The candidate stays uncommitted and the seat starts no role and stages nothing. [2]


- A hand-over counts only on a reply naming its exact object; busy refusals are retried. [3]


- The authored source owns this contract; the distribution copy is not a separate authority. [4]


- The Worker-only operation carries direct repair, per-finding freeze evidence, and Manager-reserved sync boundaries (with full conditional sync and pair reporting for Curator refresh delegated to reference/worker/sync-and-repairs.md); its all-role audience marker adds no other seat. [5]


- Worker repairs sealed own-file findings directly without prior approval, and (via reference/worker/sync-and-repairs.md) distinguishes a clean sync (focused tests rerun plus pair report for Manager/Curator refresh) from overlapping paths or failing focused tests. [6]



- Each repaired finding has its own freeze-report entry; after code PASS and Curator start, the regenerated exact-freeze Curator list and handoff-check go directly to Curator. [7]


- A freeze's focused tests are chosen by a recorded search of the tracked test files for every touched path, name and identifier, and a repair repeats it. [8]
