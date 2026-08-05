# mcp/src/agents_remember/providers/context_common.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/context_common.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:05+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../../../overview.md`                              |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`context_common.py` contains shared provider context helpers that are not specific to CGC or GrepAI. It lives at the `providers/` package level — deliberately OUTSIDE the `providers/context/` facade package — so modules loaded during `cgc.context`/`grepai.context` package init can import it without re-entering the facade's own initialization.

## Code Commentary

### Logic

It defines `ContextProviderError` (subclass of `AgentsRememberError`), `to_container_path` (host → in-container POSIX path: Windows drive letter stripped, POSIX identity), template expansion, copied requirements-file helpers, provider pin parsing, generic provider state JSON writing, file hashing, and guarded runtime-path removal. `stable_provider_id` is no longer defined here; it is re-exported from `agents_remember.providers.identity` (its canonical source) so the `providers.context` facade still exposes the name.

`to_container_path` moved here from `cgc/context/core.py` (which keeps a re-export): it is provider-agnostic Docker plumbing. The module itself moved out of `providers/context/` in the same change: as `providers.context.common`, importing it initialized the parent facade package, and any import of `cgc.context` before `providers.context` re-entered the facade init mid-flight, star-collected an empty `cgc.context`, and left the facade permanently missing every CGC name — an import-order-dependent ImportError (GitHub #58). At `providers.context_common` no facade init is triggered, and its minimal imports (errors + identity only) keep it cycle-safe for low-level modules like `cgc/seed.py`.

### Invariants And Boundaries

- The `providers.context` facade star-exports this module's names; there is no `context_providers.py` compatibility fallback.
- This module must stay OUTSIDE the `providers/context/` package: moving it back re-creates the facade re-entrancy diamond.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.
- Keep this module's imports minimal (errors + identity); it is the cycle-safe import target for low-level provider modules, which must not import the `providers.context` or `cgc.context` package facades.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| CGC context module imports shared error, path, pin, and removal helpers from here. | "from agents_remember.providers.context_common import" | mcp/src/agents_remember/providers/cgc/context/core.py:27-27 |
| GrepAI context module imports shared error, path, pin, and removal helpers from here. | "from agents_remember.providers.context_common import" | mcp/src/agents_remember/providers/grepai/context/layout.py:10-10 |

## Update History

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 3 initial citation findings (1 anchor, 0 prose, 2 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-06-10T07:25+02:00 — Module moved from `providers/context/common.py` to `providers/context_common.py`: living inside the facade package made importing it initialize the facade, whose star-import of a mid-init `cgc.context` collected nothing (import-order-dependent ImportError; GitHub #58). Sidecar moved with it.
- 2026-06-10T07:05+02:00 — `to_container_path` moved here from `cgc/context/core.py` (re-export kept there): provider-agnostic, and cycle-safe to import from `cgc/seed.py` for the GitHub #58 container-path fix. Added the minimal-imports invariant.
- 2026-05-31T12:30+02:00 — `stable_provider_id` now re-exported from `providers.identity` (canonical source moved) and `ContextProviderError` rebased on `AgentsRememberError` (1.0.0 review remediation).
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
