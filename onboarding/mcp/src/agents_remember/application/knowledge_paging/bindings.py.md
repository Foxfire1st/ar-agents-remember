# mcp/src/agents_remember/application/knowledge_paging/bindings.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_paging/bindings.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T21:41:17+02:00 |
| lastVerifiedCommitHash | `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4`|
| lastVerifiedCommitDate | 2026-09-29T22:20:46+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Minting a continuation, and refusing one whose bindings do not hold (MIK-R02 rule 3).** A token is checked before the selection is read (format, view, threshold, policy and version, memory tree) and once the selection exists (manifest and position); either way no rows are returned on a refusal.

## Code Commentary

### Logic

- `mint_continuation(binding, *, response, view, seeds, position)`: the token that resumes a walk at `position` of `seeds[0]`, with the rest queued (a collapsed block tail); it binds the build's threshold and the walk's code tree.
- `read_continuation(token, *, view)`: not this format, or another view's walk, is `continuation_unreadable` (the meaning the view codec already gives it).
- `request_binding_refusal`: a changed memory tree (naming both the minted and the now-selected tree), another threshold, or another policy/version is `continuation_binding_mismatch`.
- `resolution_refusal`: a caller-named `codeTreeId` other than the walk's is a mismatch naming both trees (ruling Q6, 19:56:40).
- `ordering_refusal`: a caller-named `orderingInput` other than the walk's effective ordering is a mismatch; a scope walk has the scope read's declared item order, so naming any ordering for it is refused (ruling Q5, 19:56:40).
- `position_refusal`: another manifest, or a position past the end, is a mismatch.
- `PagingRefusal(code, detail)`; codes `continuation_unreadable`, `continuation_binding_mismatch` and `selected_input_unavailable` (the last used by `tree_read` for a code root that does not hold the walk's tree). Every mismatch detail ends by telling the caller to restart from the seed.

### Conventions

- Refusal details name what did not hold; the caller restarts from the seed (Failure And Recovery).

### Invariants And Boundaries

- **A continuation whose binding does not hold is refused with a named code and no partial page.**
- Existing binding refusals keep their meaning (Preservation Boundary): `continuation_unreadable` for another view's walk is unchanged.

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R02@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`02_bounded-continuation-accepted-by-the-mounted-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module statement: two halves of checks, and no rows on a refusal. | "Minting a continuation, and refusing one" | mcp/src/agents_remember/application/knowledge_paging/bindings.py:1-16 |
| The refusal and its three codes. | `PagingRefusal`; `PagingRefusalCode` | mcp/src/agents_remember/application/knowledge_paging/bindings.py:45-57 |
| Minting binds the build's threshold and queues the rest. | `mint_continuation` | mcp/src/agents_remember/application/knowledge_paging/bindings.py:60-84 |
| Not this format, or another view's walk, is unreadable. | `read_continuation` | mcp/src/agents_remember/application/knowledge_paging/bindings.py:87-104 |
| A changed tree names both trees; threshold and policy are bound. | `request_binding_refusal` | mcp/src/agents_remember/application/knowledge_paging/bindings.py:107-132 |
| A named code tree or ordering other than the walk's is refused. | `resolution_refusal`; `ordering_refusal` | mcp/src/agents_remember/application/knowledge_paging/bindings.py:135-171 |
| Manifest and position, once the selection exists. | `position_refusal` | mcp/src/agents_remember/application/knowledge_paging/bindings.py:174-189 |

## Cross-Repo References

No meaningful cross-repo references found: the checks compare a token with the call's own selection.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): created this card for the new file MIK-R02 adds. It records the architect rulings of 2026-09-29 19:56:40 (Q5 the effective ordering is bound; Q6 page 1's code tree is bound) and 20:40:40 (F2 the token carries no local path). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
