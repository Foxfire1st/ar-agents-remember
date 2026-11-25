# mcp/tests/test_review_intent_summary.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pins changed-intent summary counts and typed answer states over real before/after snapshot pairs.

## Code Commentary

Twelve source test definitions include the five retained summary/route tests, four worklist, code-fact and verdict tests, two revision-population tests and the empty-unexplained-worklist binding test. Two definitions are parametrized: revision-population preservation and item-verdict state coverage. The retained summary cases distinguish added/revised/removed statements and guarantees from
realization-only and membership-only changes. A revised statement two families share counts once on
each side. A record-only successor with the same authored text and a new revision counts once on each side. A successor confined to changes in a family's members stays membership-only. Divergent successors cannot be retained (rule 3: one text
record holds one revision), so the no-single-head branch is unmeasured; absent knowledge carries an
unavailable refusal and no counts. The route returns typed answers with 200 and an unwired process
with 503. The worklist cases check unexplained-kind counts from a matching stored worklist and fallback to the readable summary for absent, mismatched, malformed, non-UTF-8, directory or permission-denied worklist input; unavailable code facts for a damaged entry side; a `counted change` witness rather than an incidental history row; and answered, stale-row open, missing-history open and undecided verdicts. The worklist expectation sums unexplained item kinds and does not independently exercise per-item open-state filtering. The `_REMOVED` partial-summary helper is not a test definition.

`_shared_base` and `_build_side` populate real snapshots through test-only RowStore, family,
membership and realization constructors imported from knowledge_rows_test_support. The actual
intent_summary_of and route readers are exercised by the assertions; no shipped canonical writer,
write lock or admission guarantee is measured by those fixture constructors.

## Retained Full-Card Audit Context

The following distinct accounts are retained from memory base `81cfe4a8`. Dates, source coordinates, counts, outcomes and ownership describe that recorded epoch. They add no fresh execution, mutation result or acceptance. Historical numeric reference labels are custody text and do not select live sidecar anchors.

### Four-case addition account

Summary of the earlier card account:

> The earlier card identifies the four worklist, code-fact, witness and item-verdict test definitions as additions to the retained summary population. The parameter table supplies two cases rather than two additional declarations.

This preserves the prior addition attribution; the current twelve-definition behavior and parameterization account above is unchanged.

The record-only fixture retains both authored statements and family guarantees while changing the selected revision number. The summary counts those successors once per side. A same-guarantee change confined to family members stays membership-only.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References











- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [14]


















- A revised statement shared by two families counts once on each side without a membership-only change. [10]



## Comparison-aware summary test port

The route fixture's summary callback accepts the optional comparison-number argument before the read observer. Its counted and absent requests omit a number and select canned answers by leaf. The existing 200 counted/unavailable and 503 unwired assertions are unchanged; this callback adaptation supplies no separate numbered-comparison selection proof.

- The comparison-shaped callback retains counted/unavailable 200 and unwired 503 assertions. [25]


- The four test definitions check matching stored-worklist unexplained-kind counts and auxiliary-file fallbacks, damaged-side code-fact refusal, counted-change witness attribution, and parametrized answered/open/undecided verdicts. The parameter table supplies two cases rather than two additional declarations. [24]


- The exact fixture uses higher revision numbers for the unchanged statement and guarantee. [31]
- The version-only successor counts as a revision. A same-guarantee member change stays membership-only. [11]

- The unit-regression lane selects mcp/tests/test_review_intent_summary.py. [23]

- _shared_base carries the directory used to build independent before/after sides from shared specifications. [16]

- Test-only RowStore mutates text-tree fixture rows and rebuilds their derived index without a shipped production admission plane. [15]
- Record-only successors count; a same-guarantee member change stays typed. [19]
- `test_missing_knowledge_is_unavailable_with_its_refusal_never_zero` supplies the current fixture or assertion described above. [12]
- The route test verifies counted and unavailable bodies with HTTP 200 and an unwired process with 503; the removed partial-state measurement is not exercised. [13]
- Added/revised/removed as +/−, relationship-only as typed counts. [17]
- A shared revised member counts once per side. [18]
- Absent knowledge is `unavailable`, never zero. [21]
- The route test verifies counted and unavailable bodies with HTTP 200 and an unwired process with 503; the removed partial-state measurement is not exercised. [22]
- `test_counts_statement_and_guarantee_heads_and_keeps_other_changes_apart` supplies the current fixture or assertion described above. [9]
