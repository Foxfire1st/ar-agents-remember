# mcp/tests/test_memory_opt_out_refused_routes.py

## Governing Overview

[Onboarding overview](overview.md)

## Purpose

MIK-R50 rules 3-4: a contract on disk that carries the removed `disabled` mode stays readable where status, attach, and guarded abandon need it, while every other route — admission, sync, integrate, direct landing, reopen, closeout, and the lifecycle layer — refuses it with the way out. Start refusals live in the companion start module.

## Code Commentary

Rule 3 keeps three surfaces reading legacy contracts without refusal: status shows leaf, series, and degraded unknown-cell contracts as they are; attach resumes live worktrees since the removed mode is not its business; and the way out works end to end — abandon dry run, abandon real run, then a modeless restart at the same task address whose successor contract has external memory. The dirty legacy case proves abandon-blocked and retained worktrees, not a forced retry. No later landing of the restarted task is invoked or asserted here.

Admission refuses a published legacy contract with status, reason, the raw cell where the read degraded, and the abandon-first way out projected to a dry-run abandon call, never asking a developer decision. A leaf start under a disabled series names the series escape rather than an edge correction.

Rule 4 refuses without the configured-authority check across the lifecycle layer: closeout preview and apply, sync, integrate, checkpoint landing, record landing, pause, cleanup, finalize, reopen and reopen-series, and the operation-control entry, plus direct-landing preview and apply raising the same status with the same detail. The four retained knowledge-gate sites (landing_gate_refusal, leaf_cutover_refusal, leaf_gate_refusal and direct_gate_verdict) answer the refusal instead of nothing-to-judge, and the behind-entry gate realizations refuse by name. Tool-level closeout, reopen, cleanup, and finalize cases close the module on published legacy contracts.

## Granted fixture, disabled-memory refusal

Direct tool/apply probes seed their canonical leaf grant rather than enable a settings flag. Their status/detail equality covers these disabled-contract probes, not universal preview/apply response parity or successful direct publication.

## Evidence



- Retained disabled-memory tests separate readable surfaces, admission refusal and knowledge-gate refusal. [1]




- Rule 3 retains status and attach answers, including legacy series and unknown-cell contracts. [2]




- Admission refusal retains the abandon-first way out and names the raw unknown cell. [3]




- Abandon retains dry/real escape and its own legacy-contract refusals. [4]




- A disabled series names the new-master escape. [5]




- Named lifecycle routes refuse disabled-memory authority; the direct-landing case compares preview with apply. [6]




- Knowledge gates and behind-entry sites name disabled-contract refusal rather than nothing-to-judge. [7]




- Closeout and public reopen/cleanup/finalize guards retain named disabled-contract refusals. [8]
