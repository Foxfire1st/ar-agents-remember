# mcp/src/agents_remember/worktrees/integration/integration_quality_checkout.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_quality_checkout.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `997305a9ced4caea67edb826224bf0351264fd56` |
| lastVerifiedCommitDate | 2026-09-17T19:54:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

Materializes a temporary detached checkout at the accepted candidate commit for the integration quality gate.

## Code Commentary

`integration_quality_checkout` now accepts an optional `commit`; a leaf with no commit reuses the ordinary worktree, while a pinned commit yields a detached exact-candidate checkout.

`integration_quality_checkout` creates an isolated temporary worktree from the exact journaled code candidate, yields it to the gate, and removes it afterward. Atomic series gates therefore test the candidate itself rather than whichever branch the repository-root checkout happens to own.

## Invariants And Boundaries

- Quality input is commit-addressed and detached from ambient checkout state.
- Temporary checkout cleanup is part of the context-manager boundary.
- This helper does not authorize or move integration refs.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The context manager creates and tears down the exact candidate checkout. | `integration_quality_checkout` | mcp/src/agents_remember/worktrees/integration/integration_quality_checkout.py:14-38 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **dead governing-overview body link repaired, and the field brought into agreement with it.** The field named `overview.md` — which resolves, but only under the onboarding root rather than against this card's own route — while the body link named `../../../overview.md` and resolved card-relative to nothing, so a reader clicking it landed nowhere and the two declarations disagreed. Both now name `overview.md`, the route-local overview of this card's own directory, so the field and the link agree by construction. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_quality_checkout.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:30+02:00 — 260815-DAG-L5: the detached checkout now accepts an explicit `commit` for the exact final candidate rather than only ambient branch state. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created exact integration quality checkout onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
