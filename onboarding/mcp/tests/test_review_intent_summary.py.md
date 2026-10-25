# mcp/tests/test_review_intent_summary.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pins changed-intent summary counts and typed answer states over real before/after snapshot pairs.

## Code Commentary

Nine test definitions, including one parametrized definition, retain five summary/route cases and add four worklist, code-fact and verdict cases. The retained summary cases distinguish added/revised/removed statements and guarantees from
realization-only and membership-only changes. A revised statement two families share counts once on
each side. A record-only successor — the same text with a changed origin state, or only a new
version — counts once on each side like any revision, while a successor that only changes a
family's members stays membership-only. Divergent successors cannot be retained (rule 3: one text
record holds one revision), so the no-single-head branch is unmeasured; absent knowledge carries an
unavailable refusal and no counts. The route returns typed answers with 200 and an unwired process
with 503. The added cases check unexplained-kind counts from a matching stored worklist and fallback to the readable summary for absent, mismatched, malformed, non-UTF-8, directory or permission-denied worklist input; unavailable code facts for a damaged entry side; a `counted change` witness rather than an incidental history row; and answered, stale-row open, missing-history open and undecided verdicts. The worklist expectation sums unexplained item kinds and does not independently exercise per-item open-state filtering. The `_REMOVED` partial-summary helper is not a test definition.

`_shared_base` and `_build_side` populate real snapshots through test-only RowStore, family,
membership and realization constructors imported from knowledge_rows_test_support. The actual
intent_summary_of and route readers are exercised by the assertions; no shipped canonical writer,
write lock or admission guarantee is measured by those fixture constructors.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References



- `test_counts_statement_and_guarantee_heads_and_keeps_other_changes_apart` supplies the current fixture or assertion described above. [9]








- `test_missing_knowledge_is_unavailable_with_its_refusal_never_zero` supplies the current fixture or assertion described above. [12]




- The route test verifies counted and unavailable bodies with HTTP 200 and an unwired process with 503; the removed partial-state measurement is not exercised. [13]



- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [14]



- Test-only RowStore mutates text-tree fixture rows and rebuilds their derived index without a shipped production admission plane. [15]




- _shared_base carries the directory used to build independent before/after sides from shared specifications. [16]


- Added/revised/removed as +/−, relationship-only as typed counts. [17]


- A shared revised member counts once per side. [18]


- Record-only successors count; a same-guarantee member change stays typed. [19]


- Absent knowledge is `unavailable`, never zero. [21]


- The route test verifies counted and unavailable bodies with HTTP 200 and an unwired process with 503; the removed partial-state measurement is not exercised. [22]





> Retained earlier citation wording: - The lane registration. Source caption: `test_review_intent_summary` [23]




- A revised statement shared by two families counts once on each side without a membership-only change. [10]
- Record-only status/version changes count as revisions; a same-guarantee member change remains membership-only. The removed partial-summary helper is not assertion evidence for this property. [11]
- The four added test definitions check matching stored-worklist unexplained-kind counts and auxiliary-file fallbacks, damaged-side code-fact refusal, counted-change witness attribution, and parametrized answered/open/undecided verdicts. The parameter table supplies two cases rather than two additional declarations. [24]

## Comparison-aware summary test port

The route fixture's summary callback accepts the optional comparison-number argument before the read observer. Its counted and absent requests omit a number and select canned answers by leaf. The existing 200 counted/unavailable and 503 unwired assertions are unchanged; this callback adaptation supplies no separate numbered-comparison selection proof.

- The comparison-shaped callback retains counted/unavailable 200 and unwired 503 assertions. [25]

- The lane registration. Source caption: `test_review_intent_summary` [23]
