# mcp/tests/test_file_size_detector.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_file_size_detector.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The File Size Budget rail suite: bands, exit codes, wrapper wiring, and scope. Pins `band_for` at the written boundaries (1199 under-limit / 1200 hard-limit / 2000 architectural-failure / 4000 emergency-cleanup), `measure` counting newlines like `wc -l` and flagging only the hard limit, the rendered band lines, the unarmed `--report` exit, the armed FAIL exit, the wrapper wiring (the `file-size` step + `file_size_armed` key + `scope.size_paths`), and the empty-measurement refusal.

## Code Commentary

- `FileSizeBandsTests` — band boundaries and `wc -l` counting.
- Detector CLI tests — `--report` exits 0 with findings; enforced mode exits 1 and names the band; no paths exits 1 (fail-closed).
- Scope/wiring tests — `scope.size_paths` includes index-known Python + `dashboard/src` TS/TSX; the armed key routes through `code_quality/scope.py`.

## Invariants And Boundaries

- The suite mirrors the detector's own boundaries: counting is newline-based, bands follow the written standard, and unreadable/empty inputs fail closed.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The detector under test. | "agents_remember.code_quality.file_size" | mcp/src/agents_remember/code_quality/check.py:312-312 |

## 260824-PDLS Admission Boundary

The wrapper-wiring fixture now passes `QUALITY_TEST_ADMISSION`. File-size policy itself is unchanged;
the shared quality configuration no longer has an authority-free construction path.

## Update History

- 2026-08-24T21:23+02:00 — Added the typed admission precondition to quality wiring.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the detector suite. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
