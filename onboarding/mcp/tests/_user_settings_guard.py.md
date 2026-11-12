# mcp/tests/_user_settings_guard.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

The single settings-path guard for shared test support. Call `user_settings_path_for_write` before creating the settings parent, writing the stub, or removing it. The function returns the product's selected path only when it differs from the protected account-default path; it creates nothing.

## Code Commentary

When the account database is readable, the protected path is the account home plus `.config/agents-remember/settings.json`, independent of a changed `HOME`. Equality includes resolved filesystem paths, so a symlink spelling of the protected path is refused too. The refusal names `XDG_CONFIG_HOME` and directs the caller to a temporary configuration folder.

When the account database cannot supply a home, comparison uses `_EARLIEST_OBSERVED_HOME`, captured at the guard's first import. A matching path is refused and the error names both the unreadable database and the observed home. A different path is returned. This observation is not a proven process-start home: an environment change before import is unobservable in-process. Do not silently describe that fallback as knowledge of the account's true home.

## Boundaries

This card states a fact about what the file provides, not an obligation: it asserts nothing on its own, and what it builds is exercised by the suites that read it.

## Evidence

- The guard compares the product path before returning it and creates no folder or file. [1]
- Account lookup returns no home when the database is unavailable. [2]
- Refusal identifies the temporary-XDG remedy, and equality includes realpath. [3]
- The made-up-account test requires refusal and an absent home; no real account is written. [4]
- The fallback tests distinguish refusal on a match, a moved folder, and honest first-import provenance. [5]
