# mcp/tests/test_converted_onboarding_drift.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

One test per rule of the truthful converted onboarding drift packet (MIK-R44@v2). Each behavioural
case discriminates its change: the named scenario fails before its fix and passes after. The
description, parity and packaging cases assert exact surfaces instead — every required statement on
every surviving named surface and its generated copies, equal numbers at the three entrances with
`include_drift=false`, and report/snapshot content from one measurement.

## Code Commentary

Rule coverage runs through the shipped seams on real repositories under `tmp_path`: the converted
branch of `run_drift_summary`, the retained internal drift-summary call, the context-packet drift block,
and both baseline tools (no public `drift_check` adapter is restored), the converted adoption gate, and the private-index staging interval. The
L44-C1 repair cases pin the staging-interval guarantees: a staged refusal restores the prepared
ignore line and preserves a concurrent edit, a validation exception restores state and keeps its
name on dry run and real adoption, preparation and Git failures restore, an unreadable ignore file
is preserved with the refusal, a malicious hook cannot change the recorded tree, and success brings
the real index to the adopted state.

The description case rejects restoration of `drift_check` registration, then checks the surviving `context_packet` include-drift description, its longer-explanation pointer and both shipped skill populations. Measurement/currentness/advisory obligations survive the retired tool; the removed registration sentence does not. Context requests no longer carry the removed `include_providers` argument.

## Evidence

- Converted trees take the converted branch and skip legacy discovery. [1]
- The converted result names every measured field. [2]
- Empty, missing and unbuildable-base trees report truthfully, never as checked-zero. [3]
- A carried anchor is reported stale, never refused as newly written. [4]
- The three consumers return one answer from the same summary. [5]
- Report and snapshot come from the same measured result. [6]
- Converted baseline states block on violations first, then on unaccepted drift. [7]
- Accepting drift never clears a validator violation. [8]
- The first baseline commits exactly the validated tree. [9]
- A dry run and a refusal change nothing. [10]
- Every named surface states what the check is, and the generated copies match. [11]
- The context-packet leaf route binds the leaf base. [12]
- An interval failure leaves everything untouched. [13]

- The description proof checks surviving surfaces and rejects restoration of the removed adapter. [14]
