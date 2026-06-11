# test_provider_context_imports.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_context_imports.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T08:39+02:00                     |
| lastVerifiedCommitHash | `f62c732df2acc30ec3766f83c176a24b39c0bc46`                         |
| lastVerifiedCommitDate | 2026-06-10T10:41:09+02:00|
| governingOverview      | `overview.md`                              |

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
(the chain that originally failed via `controllers.context_packet`), and
`grepai.context.layout` first — each followed by importing the CGC/GrepAI
constants from the facade.

### Invariants And Boundaries

Modules inside `providers/cgc/**` and `providers/grepai/**` must not import
through the `providers.context` facade package (only `providers.context_common`
or their own subpackages); these tests fail if such a back-edge returns.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The facade whose initialization order is being pinned. | [__init__.py](agents-remember/mcp/src/agents_remember/providers/context/__init__.py) |
| The relocated shared helpers that broke the cycle. | [context_common.py](agents-remember/mcp/src/agents_remember/providers/context_common.py) |
| The chain that originally surfaced the bug (settings imports the facade). | [settings.py](agents-remember/mcp/src/agents_remember/providers/settings.py) |

## Update History

- 2026-06-10T08:39+02:00: Created in the issue #54 series after both parallel chats independently hit the 3.11 facade cycle; pins the #53-landed `context_common.py` relocation with three fresh-interpreter import-order scenarios.
