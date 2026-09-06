# mcp/tests/gate_certification_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/gate_certification_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Owns the shared fixture composition for gate-record and retained-evidence tests: isolated Git candidates, admitted repository plans and exact synthetic report bytes.

## Code Commentary

### Logic

`_checkout_with_profile` creates a real temporary Git repository and copies the current profile. `_lane_for` derives the staged tree, repository plan and five-gate lane through the production compilers. `_artifact_paths` reads the actual Dagger binding map; `_fixture_record` writes deterministic fixture bytes and returns their real SHA-256 and size.

`_gate_catalog` builds the planned Gates 1–4 catalog from those exact per-rail log and artifact paths. `_green_outcome_factory` publishes the exported bytes with the real host report owner, reopens the manifest and returns a `CleanQualityOutcome` for an injected successful Dagger boundary. Tests can therefore exercise actual admission, certificate stores and retention while keeping the synthetic producer visible.

### Conventions

Only the record and retained-evidence suites consume this permanent lifecycle-cataloged helper. Scenario mutations belong in those tests; the common builder remains one fixture owner.

### Invariants And Boundaries

- Fixture reports and a synthetic successful subprocess are not real Dagger execution or master acceptance.
- Evidence digests and sizes describe actual written bytes, not invented placeholder hashes.
- Artifact IDs use the current producer binding map; no duplicate artifact catalog is maintained.
- Gate 5 is deliberately excluded from the synthetic code-gate catalog.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture candidates have real Git identity and the current profile. | `_checkout_with_profile` | mcp/tests/gate_certification_test_support.py:59-71 |
| Production owners compile candidate-bound plans and memory rail declarations. | `_lane_for` | mcp/tests/gate_certification_test_support.py:74-90 |
| Artifact path mapping comes from the actual Dagger source. | `_artifact_paths` | mcp/tests/gate_certification_test_support.py:93-97 |
| Fixture report bindings match bytes written to the export. | `_fixture_record` | mcp/tests/gate_certification_test_support.py:100-106 |
| Each planned code rail receives complete fixture evidence/artifact bindings. | `_gate_catalog` | mcp/tests/gate_certification_test_support.py:109-162 |
| The synthetic runner boundary composes real report publication and manifest reopening. | `_green_outcome_factory` | mcp/tests/gate_certification_test_support.py:165-203 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Created the sidecar for the extracted gate test composition owner, preserving the distinction between real host storage behavior and synthetic rail execution.
