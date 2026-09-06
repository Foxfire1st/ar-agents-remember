# mcp/tests/test_terminal_rail_failure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_terminal_rail_failure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `ce7f10b565f82bc41421d60ba914ee1d0abf61c4` |
| lastVerifiedCommitDate | 2026-09-04T17:04:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fully standalone CCR-R20 typed terminal rail-failure propagation suite (260831-CCR-L20, code
commit `ce7f10b5`). Every fixture builds its own published rail report (schema-3.1 quality
manifest) from canonical helpers; no certification-run, evidence-lifecycle, telemetry stream, or
Dagger artifact is shared with these tests. The suite falsifies the typed census and envelope
translation the detached lifecycle worker applies in `OperationRuntime.fail`, so a red rail
report is journaled as a typed `gate-result` envelope and never collapses to a generic worker
exception. The module is explicitly classified as `integration` evidence in
`test-evidence-lanes.toml` (row 465) because it publishes real temporary report sets and
advances real lifecycle stores.

## Code Commentary

### Logic

`publish_rail_report` (test_terminal_rail_failure.py:80-144) publishes one canonical
schema-3.1 quality report set for a red/green run under a candidate tree, and `_rail`
(test_terminal_rail_failure.py:147-165) / `_red_payload` (test_terminal_rail_failure.py:168-217)
build typed rail rows with failed IDs, versions, corrective owners, blocked/skipped facts, and
artifact digests. `TestPublishedGateResult` (test_terminal_rail_failure.py:237-361) proves red
rail facts are preserved across every independent failed rail and never truncated to one catalog;
`TestUnclassifiedAndUnavailable` (test_terminal_rail_failure.py:364-504) proves pre-rail
crashes, profile/executor-prerequisite families, candidate-mismatch, unreadable-manifest,
missing/malformed/contradictory-terminal-artifact cases resolve to the correct unavailable or
unclassified class; `TestBoundednessAndParity` (test_terminal_rail_failure.py:507-598) proves
raw logs, secrets, environment, prompt, and command bytes never enter the envelope and that
telemetry facts and the classifier reflect one terminal identity. `TestLifecycleJournalIntegration`
(test_terminal_rail_failure.py:601-639) drives `OperationRuntime.fail` through a real
`LifecycleOperationStore` and proves the typed `gate-result` envelope lands in the journal
and is exposed by the status/wait projection. `_integrate_store`
(test_terminal_rail_failure.py:642-680) and the `TestCatalogRowVariants`
(test_terminal_rail_failure.py:798-893), `TestClassifierAndCensusEdges`
(test_terminal_rail_failure.py:896-950), `TestClassifierCoverageEdges`
(test_terminal_rail_failure.py:953-966), and `TestRemainingBranchEdges`
(test_terminal_rail_failure.py:969-995) classes cover catalog-row identity/blocker/evidence
variants and remaining classifier and publication edges.

### Conventions

- Fully standalone: each fixture publishes its own report set; no test-support or fixture-module
  import is shared, so the evidence-lifecycle catalog observes no transitive consumer here.
- Every envelope is checked for the closed class vocabulary and the content-bound
  `terminalId`.

### Invariants And Boundaries

- A red published rail report is never truncated to one catalog row or replaced by a generic
  exception.
- Unavailable and unclassified outcomes are typed; no rail outcome is fabricated.
- Boundedness: raw logs, secrets, environment values, prompts, transcripts, and command bytes
  never enter the envelope.
- The suite tests the census and envelope translation, never repository-profile execution.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; CCR-R20 and the 260831-CCR-L20 delivery record
are the governing artifacts.

| Finding | Anchor | Source |
| --- | --- | --- |
| Expected verification requires red-gate, pre-rail-crash, unavailable-evidence, boundedness, and journal-integration fixtures. | `test_fail_records_typed_gate_result_in_the_journal` | mcp/tests/test_terminal_rail_failure.py:602-622 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite publishes its own schema-3.1 quality report sets under a candidate tree. | `publish_rail_report` | mcp/tests/test_terminal_rail_failure.py:80-144 |
| Red rail facts survive across every independent failed rail and are never truncated to one catalog. | `TestPublishedGateResult` | mcp/tests/test_terminal_rail_failure.py:237-361 |
| Typed unavailable/unclassified census covers crash, profile, executor-prerequisite, and evidence-state edges. | `TestUnclassifiedAndUnavailable` | mcp/tests/test_terminal_rail_failure.py:364-504 |
| Boundedness keeps raw logs/secrets/environment/prompt/command bytes out of the envelope. | `TestBoundednessAndParity` | mcp/tests/test_terminal_rail_failure.py:507-598 |
| `OperationRuntime.fail` records the typed envelope in a real lifecycle journal. | `TestLifecycleJournalIntegration` | mcp/tests/test_terminal_rail_failure.py:601-639 |
| The suite is explicitly integration evidence in the closed lane manifest. | "mcp/tests/test_terminal_rail_failure.py" | mcp/tests/test-evidence-lanes.toml:495-495 |

## Cross-Repo References

No cross-repository evidence is required.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite is repository-local and exercises the production detached-worker failure boundary through its standalone fixtures. | `TestLifecycleJournalIntegration` | mcp/tests/test_terminal_rail_failure.py:601-639 |

## Update History

- 2026-09-06T04:32:25+00:00 — L32 incoming-evidence curation: verified the exact cited lane member or current test-function owner against private C b34f4a59 and corrected only its moved coordinates. Existing own-source verification provenance is retained.

- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the cited evidence-lane member and its declared classification and corrected its incoming range. Existing source verification provenance is retained.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T17:15+02:00 - 260831-CCR-L20 Gate-5 memory pass: created for the fully standalone
  CCR-R20 typed terminal rail-failure propagation suite (code commit `ce7f10b5`): published
  rail-report fixtures, gate-result/unavailable/unclassified census falsification, boundedness and
  parity checks, and real lifecycle-journal integration; registered explicitly as `integration`
  evidence in `test-evidence-lanes.toml`. Verification stamp is the full leaf code commit
  `ce7f10b565f82bc41421d60ba914ee1d0abf61c4`.
