# l-01-agent-lifecycles/criteria/doctrine.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/criteria/doctrine.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T15:35+02:00 |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063` |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|

## Purpose

The doctrine review criteria catalog — one of the five seed catalogs in the new `criteria/` folder
(leaf 260703-L12). Binds whenever doctrine (skill files, role lifecycles, templates, instruction
surfaces, agent-obeyed docs) is in the change set under review.

## Code Commentary

### Logic

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/criteria/doctrine.md`. Three standing criteria with cited catching
evidence: **D-1 doctrine-vs-code anchoring** (every "X enforces Y" needs a code anchor — L8's
AR-5 inert `requireReviewerVerdictAtSeams` flag, documented as binding while unwired), **D-2
cross-file contradiction sweep** (review against the whole doctrine surface — L10's chat-build
wording surviving in c-09/w-02 against l-01's chat-never-builds invariant), **D-3 stuck-state
walk** (can an obeying agent deadlock — L8 round 2's seam deadlock, resolved by the ruled
`wait=false` + packet-carried-gateId channel). Plus the exploratory mandate (default 2 novel
lenses) and the promotion ratchet (candidate → standing at ≥2 catches; standing → spot-check
after 5 dry engagements; mechanizable criteria graduate into gates — the closeout body gate is
the working example).

### Conventions

Catalog files live beside the templates under `criteria/` and are bound per review type by
`roles/reviewer.md` (the binding table): master-exit adds this catalog when doctrine files ride
the change set; super-exit runs it wholesale.

### Invariants And Boundaries

The standing list MUST run every time the catalog binds; amendments land only through the
promotion ratchet on the loop owner's acceptance.

### Todos

No TODO is recorded for this catalog.

### Docs References

No external domain documentation applies to this repository-local catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [doctrine.md](agents-remember/skills/l-01-agent-lifecycles/criteria/doctrine.md) |
| The reviewer role that binds this catalog per review type. | n/a | [reviewer.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/reviewer.md) |

## Cross-Repo References

No sibling repository evidence is needed for this catalog.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-06T15:35+02:00 — Created file-level onboarding for the new `criteria/doctrine.md` seed catalog (leaf 260703-L12): D-1 doctrine-vs-code anchoring (AR-5), D-2 cross-file contradiction sweep (L10 chat-build survivors), D-3 stuck-state walk (L8 round-2 seam deadlock), with the exploratory mandate and the promotion ratchet. Verification metadata pinned until closeout stamps the L12 commit.
