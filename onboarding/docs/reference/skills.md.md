# docs/reference/skills.md

## Current A10 retained-source account

The public skill reference now documents package-served skills only. The tool server publishes every skill as an MCP resource (the SEP-2640 skills extension), so a harness reads the served text from the running server instead of a copy in a project or home skill folder: there is no `skills_install` tool any more, no harness mirror, and no copied coordination-root `skills/` tree. Exactly one skill copy is kept current — the generated package copy at `mcp/src/agents_remember/package_data/runtime/skills/`, refreshed from root `skills/` by `python3 scripts/sync-skills.py`, declared in `generated-copies.json` and checked by the pre-commit and pre-push hooks through `--check`. The page also states that native role agents receive one role file/operation, that an unbound chat creates or resolves the sprint, records the request and starts the Architect with `role_start`, and that another role is selected only on explicit developer instruction. The former spawn-environment/first-brief/dispatch routing account, the installed `ar-coordination/skills/` location and the manual `skills_install()` maintenance path are historical, not this page's current content.


- The page documents only package-served skills: MCP resources with the server's own origin and URI, one generated package copy kept current by `sync-skills.py`, no `skills_install` tool and no harness mirror or coordination-root skill tree, plus the one-call first-run path that needs no skill read. [3]




## Governing Overview

[root repo overview](../../overview.md) — governed by the route-local [docs/reference overview](overview.md).

## Purpose

Public skills reference: the canonical and served skill trees, the one `scripts/sync-skills.py`
regeneration step, how a harness reads a served skill and its resource origin, the
lifecycle/workflow skill table after the retirements, and the one-call first-run path that needs no
skill read at all.

## Code Commentary

The page documents one canonical location (`agents-remember/skills/`) and the one served package copy (`mcp/src/agents_remember/package_data/runtime/skills/`). `python3 scripts/sync-skills.py` regenerates it; `generated-copies.json` declares the refresh and the pre-commit/pre-push hooks check it through `--check`. Served MCP resources retain the server's own origin and URI. There is no installed coordination-root skill tree.

The lifecycle reference row names architect, backend orchestrator, designer, strategist, manager, worker, curator, investigator and adversarial reviewer. It describes native role agents receiving one role file and operation, and free chat creating or resolving the sprint, recording the developer's request, and starting an Architect with `role_start`; another role is selected this way only when the developer names the role and task. That reference row is documentation, not a claim that every listed lifecycle is a public launchable role.

The retained Core Skills table lists `c-00`, `c-03`, `c-04`, `c-05`, `c-08`, `c-10`, `c-13` and `c-14`. Quality/findings procedures live with `c-05`; carryover lives with `c-10`; closeout and worktree lifecycle procedures remain inside the retained skills instead of separate skills. The first-run path needs one Bootstrap call and no skill read: compiled role/operation instructions arrive in its first message. The c-13 table row still includes the words "provider indexing"; that is retained reference wording, not evidence that current setup starts indexing or a watcher.

## Invariants And Boundaries

- Public documentation, not runtime code; the canonical role/router doctrine lives in
  `skills/l-01-agent-lifecycles/SKILL.md` — this page must stay consistent with it.
- `docs/**` is excluded from file-level onboarding by the active path rules; this sidecar exists
  by explicit HFX-L6 manager instruction to cover the L6R5 role-list delta.

## Evidence

### Repo-Internal References

- Canonical lifecycle and role-document registry to which this reference defers. [1]
- Sync script the page instructs running after skill edits. [2]

- Current source account and its stated boundaries. [4]
