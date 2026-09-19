# mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T19:52+02:00 |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c` |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](overview.md)

## Purpose

Resolves the exact Git repository and local-branch facts consumed by integration authority without owning topology or lifecycle policy.

## Code Commentary

The module canonicalizes local branch spellings and symbolic aliases, resolves remote-only code default authority, admits the exact initialized external-memory default when its ref exists, and enumerates linked worktrees that own a canonical local branch. Each query fails closed when Git cannot prove the requested identity.

## Invariants And Boundaries

- Code repository defaults come only from a valid remote `origin/HEAD`; a local config value cannot replace PR-gated code authority.
- The local external-memory default is the exact `main` authority installed by `memory_init`, and its local ref must exist before lifecycle mutation.
- Symbolic aliases, cycles, malformed targets, and Git errors do not degrade to ordinary branch spellings.
- This module reports repository facts; task-derived protected-surface ownership remains in `integration_branch_authority.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical local-branch identity rejects ambiguous symbolic authority. | `canonical_local_branch` | mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:10-39 |
| Code and external-memory default resolvers keep their authority sources distinct. | `repository_default_branch`, `memory_repository_default_branch` | mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:58-67; mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:51-79 |
| Linked-worktree enumeration reports exact canonical branch owners. | `branch_worktree_owners` | mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:132-152 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Bounded Repository Failure Detail

Git failures while resolving canonical branch authority or linked-worktree ownership now surface
stable unreadable-authority messages. Raw stderr/stdout, repository paths, and backend-specific
detail stay behind this lowest repository boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Symbolic branch resolution translates Git failure to a bounded authority message. | `canonical_local_branch` | mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:10-36 |
| Linked-worktree enumeration applies the same bounded failure posture. | `branch_worktree_owners` | mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:132-152 |

## 260918-TSIP-L6 `BranchAuthorityUnavailable`: A Condition, Not A Crash

`BranchAuthorityUnavailable` (`:11-28`) is new, and it is a **typed member of the product's error
family** (`AgentsRememberError`) rather than a bare `RuntimeError`, so a caller can answer it in
the response envelope instead of losing `ok`/`status`/`nextAction` to a traceback. The two raise
sites are `repository_default_branch` (`:58-69`, no `origin/HEAD`) and
`memory_repository_default_branch` (`:70-107`, the memory repository does not record its default
branch); each message already named its own remedy, which is what makes the condition answerable.

Deliberately **not** this class: a recorded authority that is malformed, or that names a ref which
does not resolve. Those refuse a state a caller must understand and change rather than an absence
a sibling tool already reports, and they keep raising — widening this type would move the boundary
the authority tests hold. The first consumer is
`application/memory_tools.py::memory_baseline_adopt_tool`, which now catches exactly this type
(`T34`).

## Update History
- 2026-09-19T19:52+02:00 — 260918-TSIP-L6 (uncommitted change set on `ar/260918-tsip-l6-ar`, base `a1351504`): recorded the new typed `BranchAuthorityUnavailable` and the boundary it does not cross — malformed or unresolvable recorded authority still raises. Every citation range re-derived against the repaired file. Verification metadata stays closeout-owned.

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **dead governing-overview body link repaired, and the field brought into agreement with it.** The field named `overview.md` — which resolves, but only under the onboarding root rather than against this card's own route — while the body link named `../../../overview.md` and resolved card-relative to nothing, so a reader clicking it landed nowhere and the two declarations disagreed. Both now name `overview.md`, the route-local overview of this card's own directory, so the field and the link agree by construction. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled bounded Git authority failures. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-16T03:24+02:00 — 260815-DAG-L4: split exact Git repository and branch facts from the integration authority owner to satisfy the bounded source-file size gate without duplicating policy. Verification remains closeout-owned.
