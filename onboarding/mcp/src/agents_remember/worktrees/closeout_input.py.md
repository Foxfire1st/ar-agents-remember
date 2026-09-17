# mcp/src/agents_remember/worktrees/closeout_input.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_input.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash |  `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate |  2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns the single route- and contract-aware closeout-input normalizer. It captures candidate provenance, derives enabled versus not-applicable legs, validates explicit messages, and returns the only `EffectiveCloseoutInput` value permitted below the public boundary.

## Code Commentary

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Logic

The normalized Git plan has exactly two possible legs, code and memory. Ledger rendering is a cache refresh and contributes neither a commit message nor enabledness to admission, retries, or corrected-call arguments.

`resolve_closeout_plan` derives leg state from route, the already-validated contract model, memory mode, and the captured code candidate rather than from blank sentinels or memory dirtiness. Direct landing has verified-existing code, so code is not applicable; the external memory-content leg is enabled. Worktree leaf code is enabled only when the stable candidate tree differs from HEAD, and external-memory leaves enable memory content. Series and non-external legs receive typed reasons. Unsupported contract kinds are rejected at the model boundary; this owner does not duplicate that impossible-state guard.

`normalize_closeout_input` strips enabled messages once, reports omitted/empty/whitespace or stale/forged values as `CloseoutInputError`, and includes `invalidFields`, `resolvedPlan`, and `correctedCall`. The candidate snapshot is rechecked so a tree or HEAD change during normalization refuses. `require_effective_closeout_plan` validates durable retries against the accepted plan rather than re-deriving it after partial mutation.

`capture_closeout_candidate` delegates ordinary-leaf observation to the strict future-code
identity owner. That owner records the observed HEAD and configured base around the canonical
isolated-index add-all tree computation. Series closeout remains branch-addressed and continues
through its existing committed-tree route.

#### Invariants And Boundaries

- Preview, fingerprint, journal, worker, recovery, and commit code consume the same effective input.
- Validation happens before integration-authority observation, lifecycle journal creation, worker launch, landing lock, mutation intent, or Git.
- Enabledness is contract/candidate truth, not current memory worktree dirtiness.
- A failed request has no queue, authority, journal, or Git effect.
- This module does not select or invalidate closeout-queue candidates.
- Candidate acceptance and lifecycle-operation identity are distinct: this adapter supplies exact
  Git facts, while the lifecycle journal continues to guard unproven HEAD movement.

### Todos

Revision and public recovery controls are deferred to L2.

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `resolve_closeout_plan` derives code/memory enabledness from the admitted route and candidate. | `resolve_closeout_plan` | mcp/src/agents_remember/worktrees/closeout_input.py:80-114 |
| `normalize_closeout_input` validates the two explicit messages and returns one effective input. | `normalize_closeout_input` | mcp/src/agents_remember/worktrees/closeout_input.py:117-170 |
| `effective_message_arguments` renders only enabled code/memory messages for next-call guidance. | `effective_message_arguments` | mcp/src/agents_remember/worktrees/closeout_input.py:316-322 |

| Finding | Anchor | Source |
| --- | --- | --- |
| Leaf candidate capture consumes the strict plane-derived future-code identity, while series capture remains branch-addressed. (`capture_closeout_candidate`) | `capture_closeout_candidate` | mcp/src/agents_remember/worktrees/closeout_input.py:193-207 |
| Enabled/not-applicable legs derive from validated route, contract, and candidate facts. (`resolve_closeout_plan`) | `resolve_closeout_plan` | mcp/src/agents_remember/worktrees/closeout_input.py:80-114 |
| Typed refusal and corrected-call data are emitted together. (`CloseoutInputError`; `normalize_closeout_input`) | n/a | [mcp/src/agents_remember/worktrees/closeout_input.py](mcp/src/agents_remember/worktrees/closeout_input.py) |
| Retried durable input is checked against its accepted plan. (`require_effective_closeout_plan`) | `require_effective_closeout_plan` | mcp/src/agents_remember/worktrees/closeout_input.py:173-190 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=4aa067e9998742ba8d100e221b9319cb75df70f3acb5b07cb2716e2160afd07f. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): all four Repo-Internal
  rows started about two lines before their construct and ended short of it. Re-read the frozen
  source and repointed each range at its declaration (`resolve_closeout_plan` 81-120,
  `CloseoutInputError` 51-79, `normalize_closeout_input` 123-177, `require_effective_closeout_plan`
  180-197, `capture_closeout_candidate` 200-214). The offset predates the imported relocation, so
  the earlier entry's "every cited range still covers its anchor" was too generous; the claims
  themselves are unchanged. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (the future-code-candidate import relocated to `memory_quality`,
  a net-zero line change). Re-read the card against the current source: every cited range still
  covers its anchor. No wording changed; verification metadata remains closeout-owned.
- 2026-08-29T04:55+02:00 — MCAR-L02 citation maintenance: normalized all evidence tables to
  canonical finding/anchor/source cells after the full memory-quality check rejected the obsolete
  link-and-line format.

- 2026-08-29T04:55+02:00 — Routed ordinary-leaf capture through the strict future-code identity
  owner, documented the acceptance-versus-operation-identity boundary, repaired the governing
  overview link, and refreshed exact source citations. Verification metadata remains pinned until
  closeout stamps the real commit.
- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout input-model package relocation to `models.closeout.input`; normalization, leg planning, and retry validation behavior are unchanged.
- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata remains blank until closeout.
