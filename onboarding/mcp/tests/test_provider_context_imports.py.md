# test_provider_context_imports.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_context_imports.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                         |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

Regression guard for the `providers.context` facade import cycle: importing a
cgc/grepai context submodule first used to initialize the facade while
`cgc.context` was still partially initialized, permanently caching the facade
without the CGC constants (`ImportError: cannot import name CGC_NETWORK_NAME`).
Fired on Python 3.11 in focused test runs; full-suite collection order masked
it in CI. Fixed by relocating `common.py` to `providers/context_common.py`
(landed with the issue #53/#58 merge); these tests pin the fix.

## Code Commentary

### Logic

Import-order bugs only reproduce in a fresh interpreter, so each scenario runs
`sys.executable -c "<import statement>"` as a subprocess with `cwd` at
`mcp/src`. Scenarios: `cgc.context.cleanup` first, `providers.settings` first
(the chain that originally failed via `application.context_packet`), and
`grepai.context.layout` first — each followed by importing the CGC/GrepAI
constants from the facade.

### Invariants And Boundaries

Modules inside `providers/cgc/**` and `providers/grepai/**` must not import
through the `providers.context` facade package (only `providers.context_common`
or their own subpackages); these tests fail if such a back-edge returns.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The facade whose initialization order is being pinned. | "from agents_remember.providers.context_common import *" | mcp/src/agents_remember/providers/context/__init__.py:14-14 |
| The relocated shared helpers that broke the cycle. | `ContextProviderError`, `to_container_path` | mcp/src/agents_remember/providers/context_common.py:18-19; mcp/src/agents_remember/providers/context_common.py:22-37 |
| The chain that originally surfaced the bug (settings imports the facade). | "from agents_remember.providers.context import (" | mcp/src/agents_remember/providers/settings.py:14-14 |

## Update History

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 6 initial citation findings (3 anchor, 0 prose, 3 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-10T08:39+02:00: Created in the issue #54 series after both parallel chats independently hit the 3.11 facade cycle; pins the #53-landed `context_common.py` relocation with three fresh-interpreter import-order scenarios.
