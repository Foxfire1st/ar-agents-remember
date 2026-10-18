# mcp/tests/test_converted_onboarding_drift.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

One test per rule of the truthful converted onboarding drift packet (MIK-R44@v2). Each behavioural
case is written to discriminate its change with fail-before/pass-after expectations; this card
describes static definitions and assertions, not a fresh run or renewed acceptance. The
description, parity and packaging cases assert exact surfaces instead — every required statement on
every surviving named surface and its generated copies, equal numbers at the three entrances with
`include_drift=false`, and report/snapshot content from one measurement.

## Code Commentary

Rule coverage runs through the shipped seams on real repositories under `tmp_path`: the converted
branch of `run_drift_summary`, the retained internal drift-summary call, the context-packet drift block,
and both baseline tools (no public `drift_check` adapter is restored), the converted adoption gate, and the private-index staging interval. The
retained interval-failure case injects `RuntimeError("boom")` at `memory_commit_refusal` and, for
`dry_run=True` and `False`, asserts the matching exception, unchanged `_fingerprint` and
`ls-files --stage` output, the intent-to-add empty-blob entry, the untracked symlink's unchanged
target and absence from the worktree index, and the staged file's unchanged text. `_fingerprint`
compares HEAD (or `unborn`), `git write-tree` stdout, porcelain status and a digest of non-`.git`
file paths/bytes; it does not measure raw index bytes or flags. Separate tests assert committed-tree
identity with the validated candidate. A rewriting pre-commit hook runs and refuses without
HEAD/main publication, restoring the original layout/index except its untracked marker; a passing
hook runs once and publishes the validated tree. Successful adoption leaves `git write-tree`
equal to `HEAD^{tree}`. These stored cases do
not witness concurrent edits, ignore-file restoration or mode, preparation failures, or Git failures.

The description case rejects restoration of `drift_check` registration, then checks the surviving `context_packet` include-drift description, its longer-explanation pointer and both shipped skill populations. It also requires each c-02 copy to contain the ordinary-candidate statements "a current `onboarding_trace` row about the file" and "a counted change of its card alone never answers". Those static corpus assertions do not remove L53's amended, leaf-local old-MAIN-LINE counted-card exception. Measurement/currentness/advisory obligations survive the retired tool; the removed registration sentence does not. Context requests no longer carry the removed `include_providers` argument.

The complete-finding regression changes a reference slot beyond the retained one-row sample: counts and sample remain equal while `actionableFingerprint` changes. Repeating the same measurement or using detail_limit=0 leaves the fingerprint unchanged; malformed sidecar input yields null instead of a trusted complete fingerprint.

## Evidence

- Full actionable findings, not the limited sample, own fingerprint identity; incomplete input yields null. [16]
- Converted trees return a checked, nonempty drift summary whose report state agrees; no forbidden legacy-discovery callback is installed by this case. The converted-branch title is not a new mocked legacy-callback assertion. [1]
- The converted result names every measured field. [2]
- Empty, missing and unbuildable-base trees report truthfully, never as checked-zero. [3]
- Report and snapshot come from the same measured result. [6]
- Converted baseline states block on violations first, then on unaccepted drift. [7]
- Accepting drift never clears a validator violation. [8]
- The first baseline commits exactly the validated tree. [9]
- A successful would-adopt dry-run preview and a separate blocked-invalid live refusal each preserve the HEAD/unborn, write-tree-stdout, porcelain-status and non-.git path/byte fingerprint. [10]

- The context-packet leaf route binds the leaf base. [12]

- Injected RuntimeError("boom") is asserted for dry_run=True and False with equal HEAD/unborn, write-tree-stdout, porcelain-status and non-.git path/byte fingerprints and ls-files --stage output; the intent-to-add empty-blob entry, unstaged symlink target and staged file text remain as asserted. [13]

- `test_carried_anchor_is_refused_as_carried_stale_never_as_new` asserts deleted-path carried anchors refuse R22.6-carried-stale, never new-anchor R22.6-anchor-path; it does not cover all content staleness. [4]
- Consumers return the same summary; the carried deleted-path context/summary fixture asserts matching R22.6-carried-stale samples and three violations. [5]
- Surviving surfaces and generated copies assert measurement/currentness/advisory wording; c-02 copies additionally assert ordinary-candidate current-row/no-counted-edit-alone doctrine. [11]
- Static description assertions check surviving surfaces, current-row doctrine and generated copies, and reject restoration of the removed adapter. [14]
- Current source delta inspected statically: Repair carried-anchor refusal/parity captions and current-row corpus witness; separate static tests from execution and rollout exception. [15]
