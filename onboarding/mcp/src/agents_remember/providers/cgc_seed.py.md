# mcp/src/agents_remember/providers/cgc_seed.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc_seed.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:50+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`cgc_seed.py` owns CodeGraphContext seed request options, configured root resolution, source/target validation, export/load lifecycle orchestration, and seed result payloads.

## Code Commentary

### Logic

It defines `CgcSeedOptions` and the internal `CgcSeedContext`, resolves source and target CGC roots from explicit arguments or settings, checks repository HEAD compatibility unless mismatches are allowed, protects same-coordination-root cross-path seeding unless explicitly allowed or isolated, starts the source backend, exports a bundle, rewrites paths, and loads the rewritten bundle into the target.

### Invariants And Boundaries

- Seed source settings must come from explicit provider settings or from the same coordination root's active settings path.
- CGC seed is an optimization; callers decide whether a failed seed can fall back to full refresh.
- Bundle path rewriting is delegated to `cgc_bundle.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider-level CGC setup calls this module before optional refresh fallback. | [cgc_setup.py](cgc_setup.py.md) |
| Bundle path rewriting is delegated to the CGC bundle module. | [cgc_bundle.py](cgc_bundle.py.md) |
| Worktree setup constructs CGC seed options through the provider setup request. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |

## Update History

- 2026-05-25T19:50+02:00: Created when CGC seed orchestration was extracted out of `provider_setup.py`.
