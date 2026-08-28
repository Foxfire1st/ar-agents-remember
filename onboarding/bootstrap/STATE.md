# PDLS Verification-Ownership Memory State

| Field | Value |
| --- | --- |
| workflow | c-03 existing-memory-slice-maintenance + c-05 file-level onboarding |
| state | curation in progress — route/index validation pending |
| change kind | reopened PDLS remediation with verification-authority and evidence-system changes |
| source inventory | 157 path-rule-eligible logical changes plus cleanup of 3 deleted pre-existing fixture sidecars |
| verification route | 50 current Python sources and exactly 50 one-to-one sidecars under `mcp/test_support/agents_remember_test_support` |
| focused test additions | six new behavior cards and six matching file cards |
| deleted slice | Candidate A, retired product verification routes, and deleted Claude 2.1.207 fixture sidecars removed without compatibility shadows |
| candidate | v21 is historical only; a successor is frozen after this curation pass |
| route indexes | refresh and repeat dry run pending |
| handoff | blocked only on deterministic memory validation and successor candidate identity |

## Current Architecture Being Preserved

- Python test and quality machinery is verification infrastructure under `mcp/test_support`, not
  operational product behavior under `mcp/src`.
- Package authority is explicit, exhaustive, and non-overlapping. Unknown or conflicting test
  classifications fail loudly; no unmarked test silently becomes unit evidence.
- Dagger is the sole certifying pytest route. Cadence, retry, causal, diagnostic, and measurement
  reports remain non-accepting even when Dagger produces them.
- Candidate A is retired. Its seven unique product assertions survive as ordinary certifying
  regressions; no host-runner, manifest, classifier, or compatibility reader survives.
- Test selection, retry invalidation, and causal localization consume source-derived import,
  recursive plugin, and literal-consumer facts. Lifecycle declarations validate those facts but
  cannot manufacture completeness.
- Retry proof persists in an integrity-bound Dagger cache and composes retained and fresh coverage
  only after the exact pytest result permits publication.
- The evidence lifecycle contains 34 durable artifacts plus its governed contracts. Every current
  test/support file has one explicit lane and governed support remains non-accepting.
- Requirement acceptance envelopes, architect compilation, and immutable worker/reviewer attempt
  journals remain separate from durable-evidence promotion and from queue authority.

## Current Curation Results

- Every changed eligible current source has a changed one-to-one sidecar.
- Every genuinely deleted or moved source lacks a live old-path sidecar; the three deleted
  Claude 2.1.207 fixture sidecars are removed.
- The verification root has a complete 50-source/50-sidecar census; retired product routes have
  no remaining Python sources or sidecars.
- Six previously missing test sidecars and six high-risk file cards now cover cadence, causal
  localization/preflight, evidence lanes/lifecycle, and route measurement.
- Two stale source comments were corrected during cold read. That invalidated v21 as the final
  evidence identity but did not change runtime behavior.

## Remaining Closeout-Owned Facts

- Refresh route indexes through the sanctioned writer and require a zero-write repeat preview.
- Run c-02 memory-quality checks, then freeze the exact successor code, memory, and task candidates.
- Stamp file cards with the landed code commit/date only after the real code commit exists.
- Keep Q5-Q8 reruns as experimental protocol events; only the later worker handoff creates A002.

## Next Recommended Action

Complete route/index and memory-quality validation, freeze the successor candidate, rerun Q5-Q8
against that exact identity, then append A002 and hand the frozen delta to the same independent Q9
reviewer.
