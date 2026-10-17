# mcp/tests/test_capsule_replay_integrity.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Replay and delayed held-seat integrity of frozen instruction detail artifacts.

## Code Commentary

Builds two frozen details through real launch composition and checks every saved revision, missing/symlink/directory/FIFO refusal, canonical report-folder rebound and malformed reference refusal while allowing detail-free legacy receipts. Saved-start replay reaches a fake host seam with good bytes, then refuses missing detail before any call. Held opening similarly rejects changed detail and leaves the waiting claim recoverable.

The preparation regression exercises Worker, Reviewer and Curator detail-bearing capsules with a real local role-reports directory, distinct from the report's task collection destination. It runs actual preparation, detail validation and handover restoration after deletion, checks frozen detail bytes and exercises delayed held opening. The shipped Worker capsule has no details, so that case supplies one explicit detail at the compiler-delivery seam; Reviewer and Curator use their shipped corpus through the fixture compiler. Legacy missing-link restoration and malformed detail-source/path/handover controls extend the existing replay cases. No host launches in the preparation test.

The preparation fixture captures the compiler binding before unittest setup. Its four local overrides live in a private monkeypatch context that unwinds before unittest cleanup restores the entry compiler; it does not undo the shared pytest monkeypatch stack. After unittest cleanup, the fixture asserts identity with the captured compiler. This local postcondition is not by itself a check after every pytest teardown owner. The complete-lifecycle observer and its run receipts are task evidence, not a new installed test or host proof.

## Evidence Boundaries

- The source assertions bind frozen bytes and canonical report access without regenerating from mutable current corpus.
- Positive controls reach a deliberately stopping fake-host boundary; negative controls assert no call and recoverable receipt/queue state.
- No native agent is created, opened or consumed by a model.
- Regular-open/canonical checks are bounded to the tested paths; there is no universal filesystem race proof or authority to silently repair corrupted frozen bytes.

This card describes assertion/support/document source, not a test invocation, independent verdict or publication.

## Evidence


- Source assertion: test_replay_checks_every_frozen_revision_without_reading_the_current_corpus. The declaration is not an execution receipt. [1]


- Source assertion: test_replay_refuses_missing_or_nonregular_detail_targets. The declaration is not an execution receipt. [2]


- The canonical-folder case refuses a rebound link despite matching bytes and restores an absent valid legacy link. The declaration is not an execution receipt. [3]



- Shape controls also refuse mismatched source-derived detail names, given paths and malformed or non-sibling saved handover references. The declaration is not an execution receipt. [4]



- Real local preparation and receipt restoration preserve frozen detail bytes for three role cases; Worker detail is supplied at the compiler seam, and no host is launched. [7]


- Source assertion: test_saved_start_replay_refuses_missing_details_before_the_host_call. The declaration is not an execution receipt. [5]


- Source assertion: test_held_opening_refuses_changed_details_and_preserves_waiting_messages. The declaration is not an execution receipt. [6]



- The fixture closes its private override stack before unittest cleanup and checks the captured compiler identity without undoing the shared pytest stack. [8]
