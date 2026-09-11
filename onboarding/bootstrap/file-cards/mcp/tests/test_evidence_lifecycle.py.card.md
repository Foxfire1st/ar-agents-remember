# File Card — mcp/tests/test_evidence_lifecycle.py

| Field | Value |
| --- | --- |
| repo | agents-remember |
| sourceFile | `mcp/tests/test_evidence_lifecycle.py` |
| targetOnboardingFile | `onboarding/mcp/tests/test_evidence_lifecycle.py.md` |
| generated | 2026-08-28T06:28+02:00 |

## Classification

| Field | Value |
| --- | --- |
| Priority | high |
| Role | durable-evidence lifecycle contract |
| Risk | asserted consumers, ghost evidence, or permanent temporary artifacts |
| Suggested action | create onboarding |
| Suggested wave | onboarding-wave-005 |

## Governing Context

| Field | Value |
| --- | --- |
| nearestGoverningOverview | `onboarding/mcp/tests/overview.md` |
| ancestorOverviews | `onboarding/overview.md`, `onboarding/mcp/overview.md` |
| localArea | Python evidence tests |

## Why This File Matters

It closes the evidence catalog over real artifacts, consumers, replacement nodes, and expiry.

## What The Worker Must Explain

- source-observed consumer completeness;
- governed baseline/fixture discovery;
- stale metadata and contract refusal;
- executable replacement and expiry behavior.

## Inputs For Worker

| Input | Path | Required? | Why |
| --- | --- | --- | --- |
| Source file | `mcp/tests/test_evidence_lifecycle.py` | yes | forcing behavior |
| Governing overview | `onboarding/mcp/tests/overview.md` | yes | test-area model |
| Catalog | `mcp/tests/evidence-lifecycle.toml` | yes | lifecycle declaration |

## Known Traps

- Catalog declarations cannot manufacture consumers or replacement nodes.

## Questions To Resolve

None.

## Done When

- The sidecar records closed-world discovery, consumer truth, and expiry boundaries.
