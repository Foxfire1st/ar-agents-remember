# mcp/tests/test_review_assessment_history_repairs.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Pins rejection of invalid retained assessment evidence before canonical curator authority replacement.

## Code Commentary

One parametrized test supplies escaping-alias and corrupt-retained-byte inputs. The fixture prepares a nonempty curator authority and an assessment; one branch points an evidence alias outside the admitted namespace, and the other corrupts a retained evidence file after generation publication but before validation. Both expect CuratorCoherenceError, unchanged canonical bytes and a still-readable current authority.

The remaining test is this integrity/publication-order boundary. The four former namespace, provenance, channel/custody and snapshot-loss journeys named by the historical module description are no longer current coverage.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `_nonempty_fixture` supplies the current fixture or assertion described above. [6]
- `_request` supplies the current fixture or assertion described above. [7]
- `test_integrity_rejection_precedes_canonical_authority_replacement` supplies the current fixture or assertion described above. [8]
