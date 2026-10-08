# scripts/pnt_sandbox/environment.py

## Governing Overview

[Route overview](../../overview.md)

## Purpose and current source account

The scrub removes AR/Paseo/source/former-host prefixes and exact Python/Git/caller-session names, then installs seven sandbox-owned values (`TMUX_TMPDIR`, `XDG_DATA_HOME`, `XDG_STATE_HOME`, `XDG_CACHE_HOME`, `PYTHONPYCACHEPREFIX`, `GIT_OPTIONAL_LOCKS=0`, `AR_DAGGER_AUTHORITY_ROOT`); each child receives its own PWD. Credentials and harness home selectors remain. Running daemon admission compares scrubbed selectors and expected owned values, and the Eve env denylist prevents reintroduction by its external key file.

## Evidence

- The scoped current source carries the module/document behavior described above. [1]

## 260928-MIK-L96 The product session list and sandbox XDG roots

The sandbox environment now reads the product's exact-name session list (`package_data/host-session-environment.json`) and adds its own names, and it sets sandbox-owned XDG data, state and cache roots so a child resolves the sandbox's folders rather than the caller's; the removal stays by exact name and logins remain inherited.

- The sandbox environment constructor. [2]
- The product list the sandbox reads. [3]
